**Workflows**
Typical datacenter operations and processes involve taking multiple actions across various systems. To capture and automate these operations, we use workflows. A workflow strings atomic actions into a higher level automation, and orchestrates their executions by calling the right action, at the right time, with the right input. It keeps state, passes data between actions, and provides reliability and transparency to the execution.

Just like any actions, workflows are exposed in the automation library, and can be called manually, or triggered by rules. Workflows can even be called from other workflows.

Examples: https://scm.starbucks.com/SRE-Automation/st2examples/tree/master/actions/workflows

Additonal Documentation: https://docs.stackstorm.com/workflows.html