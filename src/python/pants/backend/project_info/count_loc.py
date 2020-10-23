# Copyright 2019 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from typing import Tuple

from pants.core.util_rules.external_tool import (
    DownloadedExternalTool,
    ExternalTool,
    ExternalToolRequest,
)
from pants.engine.console import Console
from pants.engine.fs import Digest, MergeDigests, SourcesSnapshot
from pants.engine.goal import Goal, GoalSubsystem
from pants.engine.platform import Platform
from pants.engine.process import Process, ProcessResult
from pants.engine.rules import Get, collect_rules, goal_rule
from pants.option.custom_types import shell_str
from pants.util.enums import match
from pants.util.logging import LogLevel
from pants.util.strutil import pluralize


class SuccinctCodeCounter(ExternalTool):
    """The Succinct Code Counter, aka `scc` (https://github.com/boyter/scc)."""

    options_scope = "scc"
    default_version = "2.13.0"
    default_known_versions = [
        "2.13.0|darwin|38948467985f0662ab6bf6d676294e84a92202530233d0cc6e98afa309cabac9|2092291",
        "2.13.0|linux|b49d030ce8280252b5928946ee1d7006dd80c6b662bd99ee3fe16af411d80b3c|1973146",
    ]

    @classmethod
    def register_options(cls, register) -> None:
        super().register_options(register)
        register(
            "--args",
            type=list,
            member_type=shell_str,
            passthrough=True,
            help=(
                'Arguments to pass directly to SCC, e.g. `--count-loc-args="--no-cocomo"`. Refer '
                "to https://github.com/boyter/scc."
            ),
        )

    @property
    def args(self) -> Tuple[str, ...]:
        return tuple(self.options.args)

    def generate_url(self, plat: Platform) -> str:
        plat_str = match(plat, {Platform.darwin: "apple-darwin", Platform.linux: "unknown-linux"})
        return (
            f"https://github.com/boyter/scc/releases/download/v{self.version}/scc-{self.version}-"
            f"x86_64-{plat_str}.zip"
        )

    def generate_exe(self, _: Platform) -> str:
        return "./scc"


class CountLinesOfCodeSubsystem(GoalSubsystem):
    """Count lines of code."""

    name = "count-loc"


class CountLinesOfCode(Goal):
    subsystem_cls = CountLinesOfCodeSubsystem


@goal_rule
async def count_loc(
    console: Console,
    succinct_code_counter: SuccinctCodeCounter,
    sources_snapshot: SourcesSnapshot,
) -> CountLinesOfCode:
    if not sources_snapshot.snapshot.files:
        return CountLinesOfCode(exit_code=0)

    scc_program = await Get(
        DownloadedExternalTool,
        ExternalToolRequest,
        succinct_code_counter.get_request(Platform.current),
    )
    input_digest = await Get(
        Digest, MergeDigests((scc_program.digest, sources_snapshot.snapshot.digest))
    )
    result = await Get(
        ProcessResult,
        Process(
            argv=(scc_program.exe, *succinct_code_counter.args),
            input_digest=input_digest,
            description=(
                f"Count lines of code for {pluralize(len(sources_snapshot.snapshot.files), 'file')}"
            ),
            level=LogLevel.DEBUG,
        ),
    )
    console.print_stdout(result.stdout.decode())
    return CountLinesOfCode(exit_code=0)


def rules():
    return collect_rules()
