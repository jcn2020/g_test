**Sensors**
Sensors are a way to integrate external systems and events with StackStorm. Sensors are pieces of Python code that either periodically poll some external system, or passively wait for inbound events. They then inject triggers into StackStorm, which can be matched by rules, for potential action execution.

Sensors are written in Python, and must follow the StackStorm-defined sensor interface requirements.

Examples: https://scm.starbucks.com/SRE-Automation/st2examples/tree/master/sensors

Additonal Documentation: https://docs.stackstorm.com/sensors.html