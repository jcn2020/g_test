**Action Aliases**
Action Aliases are a simplified and more human readable representation of actions in StackStorm. They are useful in text based interfaces, notably ChatOps.

Action Alias Structure
Action aliases are content like actions, rules, and sensors. They are defined in YAML files and deployed via packs, e.g.:

---
name: "remote_shell_cmd"
pack: "examples"
action_ref: "core.remote"
description: "Execute a command on a remote host via SSH."
formats:
  - "run {{cmd}} on {{hosts}}"

In the above example remote_shell_cmd is an alias for the core.remote action. The supported format for the alias is specified in the formats field. A single alias can support multiple formats for the same action.

Examples: https://scm.starbucks.com/SRE-Automation/st2examples/tree/master/aliases

Additonal Documentation: https://docs.stackstorm.com/chatops/aliases.html