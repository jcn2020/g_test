**Rules**
StackStorm uses rules and workflows to capture operational patterns as automations. Rules map triggers to actions (or workflows), apply matching criteria and map trigger payloads to action inputs.

Note

Rules not working as expected? Check the Rules Troubleshooting documentation. This walks through rules testing, checking enforcements, logging and troubleshooting.

Rule Structure
Rules are defined in YAML. Rule definition structure, as well as required and optional elements are listed below:

---
    name: "rule_name"                      # required
    pack: "examples"                       # optional
    description: "Rule description."       # optional
    enabled: true                          # required

    trigger:                               # required
        type: "trigger_type_ref"

    criteria:                              # optional
        trigger.payload_parameter_name1:
            type: "regex"
            pattern : "^value$"
        trigger.payload_parameter_name2:
            type: "iequals"
            pattern : "watchevent"

    action:                                # required
        ref: "action_ref"
        parameters:                        # optional
            foo: "bar"
            baz: "{{ trigger.payload_parameter_1 }}"

Examples: https://scm.starbucks.com/SRE-Automation/st2examples/tree/master/rules

Additonal Documentation: https://docs.stackstorm.com/rules.html