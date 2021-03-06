# Copyright 2016 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

target(
  name = 'all',
  dependencies = [
    ':analysis_extraction',
    ':benchmark_run',
    ':binary_create',
    ':bootstrap_jvm_tools',
    ':bundle_create',
    ':consolidate_classpath',
    ':check_published_deps',
    ':checkstyle',
    ':classmap',
    ':coursier_resolve',
    ':detect_duplicates',
    ':ivy_imports',
    ':ivy_outdated',
    ':jar_create',
    ':jar_import_products',
    ':jar_publish',
    ':javadoc_gen',
    ':junit_run',
    ':jvm_binary_task',
    ':jvm_dependency_check',
    ':jvm_dependency_usage',
    ':jvm_platform_analysis',
    ':jvm_run',
    ':jvm_task',
    ':jvm_tool_task_mixin',
    ':jvmdoc_gen',
    ':nailgun_task',
    ':prepare_resources',
    ':prepare_services',
    ':properties',
    ':provide_tools_jar',
    ':resources_task',
    ':resolve_shared',
    ':run_jvm_prep_command',
    ':scala_repl',
    ':scaladoc_gen',
    ':scalafix',
    ':scalafmt',
    ':scalastyle',
    ':unpack_jars',
    'src/python/pants/backend/jvm/tasks/jvm_compile:all',
  ],
)

python_library(
  name = 'analysis_extraction',
  sources = ['analysis_extraction.py'],
  dependencies = [
    ':nailgun_task',
    'src/python/pants/backend/jvm/subsystems:dependency_context',
    'src/python/pants/backend/jvm/subsystems:zinc',
    'src/python/pants/goal:products',
    'src/python/pants/task',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'benchmark_run',
  sources = ['benchmark_run.py'],
  dependencies = [
    ':jvm_task',
    ':jvm_tool_task_mixin',
    'src/python/pants/java/jar',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:workunit',
    'src/python/pants/java:util',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'binary_create',
  sources = ['binary_create.py'],
  dependencies = [
    ':jvm_binary_task',
    'src/python/pants/base:build_environment',
    'src/python/pants/util:dirutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'consolidate_classpath',
  sources = ['consolidate_classpath.py'],
  dependencies = [
    ':jvm_binary_task',
    'src/python/pants/base:build_environment',
    'src/python/pants/util:dirutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'bootstrap_jvm_tools',
  sources = ['bootstrap_jvm_tools.py'],
  dependencies = [
    ':jar_task',
    'src/python/pants/backend/jvm/subsystems:jvm_tool_mixin',
    'src/python/pants/backend/jvm/subsystems:shader',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:workunit',
    'src/python/pants/invalidation',
    'src/python/pants/ivy',
    'src/python/pants/java:executor',
    'src/python/pants/java:util',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:fileutil',
    'src/python/pants/util:memo',
  ],
  tags = {'partially_type_checked'},
)

python_library(
  name = 'bundle_create',
  sources = ['bundle_create.py'],
  dependencies = [
    '3rdparty/python:dataclasses',
    ':classpath_products',
    ':jvm_binary_task',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:deprecated',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/fs',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:fileutil',
    'src/python/pants/util:ordered_set',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'check_published_deps',
  sources = ['check_published_deps.py'],
  dependencies = [
    ':jar_publish',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'checkstyle',
  sources = ['checkstyle.py'],
  dependencies = [
    ':nailgun_task',
    'src/python/pants/java/jar',
    'src/python/pants/backend/jvm/subsystems:checkstyle',
    'src/python/pants/backend/jvm/subsystems:shader',
    'src/python/pants/base:exceptions',
    'src/python/pants/option',
    'src/python/pants/process',
    'src/python/pants/task',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:ordered_set',
  ],
  tags = {'partially_type_checked'},
)

python_library(
  name = 'classpath_entry',
  sources = ['classpath_entry.py'],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'classpath_util',
  sources = ['classpath_util.py'],
  dependencies = [
    ':classpath_entry',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:ordered_set',
    'src/python/pants/util:strutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'classpath_products',
  sources = ['classpath_products.py'],
  dependencies = [
    ':classpath_entry',
    ':classpath_util',
    'src/python/pants/java/jar',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/goal:products',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:ordered_set',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'detect_duplicates',
  sources = ['detect_duplicates.py'],
  dependencies = [
    ':jvm_binary_task',
    'src/python/pants/base:exceptions',
    'src/python/pants/java/jar',
    'src/python/pants/option',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'ivy_imports',
  sources = ['ivy_imports.py'],
  dependencies = [
    ':classpath_products',
    ':jar_import_products',
    ':nailgun_task',
    'src/python/pants/backend/jvm/targets:jvm',
  ],
  tags = {'partially_type_checked'},
)

python_library(
  name = 'ivy_outdated',
  sources = ['ivy_outdated.py'],
  dependencies = [
    ':classpath_products',
    ':nailgun_task',
    'src/python/pants/backend/jvm:ivy_utils',
    'src/python/pants/backend/jvm/subsystems:shader',
    'src/python/pants/base:deprecated',
    'src/python/pants/ivy',
    'src/python/pants/java/jar',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'coursier_resolve',
  sources = ['coursier_resolve.py'],
  dependencies = [
    ':classpath_products',
    ':nailgun_task',
    ':resolve_shared',
    'src/python/pants/backend/jvm/subsystems:resolve_subsystem',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/backend/jvm/tasks/coursier',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:fingerprint_strategy',
    'src/python/pants/base:revision',
    'src/python/pants/base:workunit',
    'src/python/pants/invalidation',
    'src/python/pants/java:executor',
    'src/python/pants/java:util',
    'src/python/pants/java/distribution',
    'src/python/pants/java/jar',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:fileutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jar_create',
  sources = ['jar_create.py'],
  dependencies = [
    ':jar_task',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:workunit',
    'src/python/pants/backend/jvm/targets:jvm',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name='jar_import_products',
  sources=['jar_import_products.py'],
  dependencies=[
    'src/python/pants/backend/jvm/targets:jvm',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jar_publish',
  sources = ['jar_publish.py'],
  dependencies = [
    ':jar_publish_resources',
    ':jar_task',
    ':properties',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/backend/jvm/targets:scala',
    'src/python/pants/backend/jvm:ossrh_publication_metadata',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:build_file',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:generator',
    'src/python/pants/build_graph',
    'src/python/pants/ivy',
    'src/python/pants/option',
    'src/python/pants/scm',
    'src/python/pants/task',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:ordered_set',
    'src/python/pants/util:strutil',
  ],
  tags = {"partially_type_checked"},
)

resources(
  name = 'jar_publish_resources',
  sources = ['templates/jar_publish/*.mustache'],
)

python_library(
  name = 'jar_task',
  sources = ['jar_task.py'],
  dependencies = [
    ':classpath_util',
    ':nailgun_task',
    'src/python/pants/backend/jvm:argfile',
    'src/python/pants/backend/jvm/subsystems:jar_tool',
    'src/python/pants/backend/jvm/targets:java',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:exceptions',
    'src/python/pants/binaries',
    'src/python/pants/java/jar',
    'src/python/pants/util:contextutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'javadoc_gen',
  sources = ['javadoc_gen.py'],
  dependencies = [
    ':jvmdoc_gen',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/java/distribution',
    'src/python/pants/java:executor',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name =  'junit_run',
  sources = ['junit_run.py'],
  dependencies = [
    ':classpath_util',
    ':jvm_task',
    ':jvm_tool_task_mixin',
    'src/python/pants/backend/jvm/subsystems:junit',
    'src/python/pants/backend/jvm/subsystems:jvm_platform',
    'src/python/pants/backend/jvm/targets:java',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/backend/jvm/tasks/coverage',
    'src/python/pants/backend/jvm/tasks/reports',
    'src/python/pants/backend/jvm:argfile',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:deprecated',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:workunit',
    'src/python/pants/build_graph',
    'src/python/pants/invalidation',
    'src/python/pants/java/distribution',
    'src/python/pants/java/junit',
    'src/python/pants/java:executor',
    'src/python/pants/process',
    'src/python/pants/task',
    'src/python/pants/util:argutil',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:desktop',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:memo',
    'src/python/pants/util:ordered_set',
    'src/python/pants/util:strutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvm_binary_task',
  sources = ['jvm_binary_task.py'],
  dependencies = [
    ':classpath_products',
    ':jar_task',
    'src/python/pants/backend/jvm/subsystems:shader',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/java:util',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:fileutil',
    'src/python/pants/util:memo',
    'src/python/pants/util:ordered_set',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvm_dependency_analyzer',
  sources = ['jvm_dependency_analyzer.py'],
  dependencies = [
    ':classpath_util',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/backend/jvm/targets:scala',
    'src/python/pants/build_graph',
    'src/python/pants/java/distribution',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:memo',
    'src/python/pants/util:ordered_set',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvm_dependency_check',
  sources = ['jvm_dependency_check.py'],
  dependencies = [
    ':jvm_dependency_analyzer',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:exceptions',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/backend/jvm/targets:scala',
    'src/python/pants/build_graph',
    'src/python/pants/java/distribution',
    'src/python/pants/task',
    'src/python/pants/util:contextutil',
    'src/python/pants/util:memo',
    'src/python/pants/util:ordered_set',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvm_dependency_usage',
  sources = ['jvm_dependency_usage.py'],
  dependencies = [
    ':jvm_dependency_analyzer',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:build_environment',
    'src/python/pants/build_graph',
    'src/python/pants/java/distribution',
    'src/python/pants/task',
    'src/python/pants/util:fileutil',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvm_platform_analysis',
  sources = ['jvm_platform_analysis.py'],
  dependencies = [
    '3rdparty/python:ansicolors',
    'src/python/pants/base:exceptions',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/task',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvm_run',
  sources = ['jvm_run.py'],
  dependencies = [
    ':jvm_task',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:workunit',
    'src/python/pants/fs',
    'src/python/pants/java:executor',
    'src/python/pants/java/distribution',
    'src/python/pants/java:util',
    'src/python/pants/task',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:strutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvm_task',
  sources = ['jvm_task.py'],
  dependencies = [
    ':classpath_util',
    'src/python/pants/backend/jvm/subsystems:jvm',
    'src/python/pants/build_graph',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvm_tool_task_mixin',
  sources = ['jvm_tool_task_mixin.py'],
  dependencies = [
    'src/python/pants/backend/jvm/subsystems:jvm_tool_mixin',
    'src/python/pants/base:exceptions',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'jvmdoc_gen',
  sources = ['jvmdoc_gen.py'],
  dependencies = [
    ':jvm_task',
    'src/python/pants/base:exceptions',
    'src/python/pants/binaries',
    'src/python/pants/task',
    'src/python/pants/util:desktop',
    'src/python/pants/util:dirutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'nailgun_task',
  sources = ['nailgun_task.py'],
  dependencies = [
    ':jvm_tool_task_mixin',
    'src/python/pants/java/jar',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:exceptions',
    'src/python/pants/java/distribution:distribution',
    'src/python/pants/java:executor',
    'src/python/pants/java:nailgun_executor',
    'src/python/pants/java:util',
    'src/python/pants/process',
    'src/python/pants/task',
    'src/python/pants/util:enums',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'prepare_resources',
  sources = ['prepare_resources.py'],
  dependencies = [
    ':resources_task',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:build_environment',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:ordered_set',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'prepare_services',
  sources = ['prepare_services.py'],
  dependencies = [
    ':resources_task',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:fingerprint_strategy',
    'src/python/pants/base:hash_utils',
    'src/python/pants/base:payload_field',
    'src/python/pants/util:dirutil',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'properties',
  sources = ['properties.py'],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'provide_tools_jar',
  sources = ['provide_tools_jar.py'],
  dependencies = [
    ':classpath_products',
    ':jvm_tool_task_mixin',
    'src/python/pants/backend/jvm/subsystems:java',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'resources_task',
  sources = ['resources_task.py'],
  dependencies = [
    'src/python/pants/option',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'resolve_shared',
  sources = ['resolve_shared.py'],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'run_jvm_prep_command',
  sources = ['run_jvm_prep_command.py'],
  dependencies = [
    ':classpath_util',
    'src/python/pants/backend/jvm/subsystems:jvm_platform',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:workunit',
    'src/python/pants/java:executor',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'scala_repl',
  sources = ['scala_repl.py'],
  dependencies = [
    ':jvm_task',
    ':jvm_tool_task_mixin',
    'src/python/pants/java/jar',
    'src/python/pants/backend/jvm/subsystems:scala_platform',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/java/distribution',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'scaladoc_gen',
  sources = ['scaladoc_gen.py'],
  dependencies = [
    ':jvmdoc_gen',
    'src/python/pants/backend/jvm/subsystems:scala_platform',
    'src/python/pants/java:executor',
    'src/python/pants/java/distribution',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'scalafix',
  sources = ['scalafix_task.py'],
  dependencies = [
    ':rewrite_base',
    'src/python/pants/backend/jvm/subsystems:scala_linters',
    'src/python/pants/backend/jvm/tasks:nailgun_task',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/java/jar',
    'src/python/pants/option',
    'src/python/pants/task',
  ],
  tags = {'partially_type_checked'},
)

python_library(
  name = 'scalafmt',
  sources = ['scalafmt_task.py'],
  dependencies = [
    ':rewrite_base',
    'src/python/pants/backend/jvm/subsystems:scala_linters',
    'src/python/pants/backend/jvm/tasks:nailgun_task',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/java/jar',
    'src/python/pants/option',
    'src/python/pants/task',
  ],
  tags = {'partially_type_checked'},
)

python_library(
  name = 'rewrite_base',
  sources = ['rewrite_base.py'],
  dependencies = [
    'src/python/pants/backend/jvm/tasks:nailgun_task',
    'src/python/pants/base:deprecated',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/option',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:memo',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'scalastyle',
  sources = ['scalastyle_task.py'],
  dependencies = [
    ':nailgun_task',
    'src/python/pants/backend/jvm/subsystems:scala_linters',
    'src/python/pants/backend/jvm/subsystems:scala_platform',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'src/python/pants/option',
    'src/python/pants/process',
    'src/python/pants/task',
    'src/python/pants/util:dirutil'
  ],
  tags = {'partially_type_checked'},
)

python_library(
  name = 'unpack_jars',
  sources = ['unpack_jars.py'],
  dependencies = [
    '3rdparty/python/twitter/commons:twitter.common.dirutil',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/backend/jvm/tasks:jar_import_products',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:deprecated',
    'src/python/pants/base:fingerprint_strategy',
    'src/python/pants/fs',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)

python_library(
  name = 'classmap',
  sources = ['classmap.py'],
  dependencies = [
    ':classpath_util',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/task',
  ],
  tags = {"partially_type_checked"},
)
