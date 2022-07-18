**Triggers**
Triggers are StackStorm constructs that identify the incoming events to StackStorm. A trigger is a tuple of type (string) and optional parameters (object). Rules are written to work with triggers. Sensors typically register triggers though this is not strictly required. For example, there is a generic webhooks trigger registered with StackStorm, which does not require a custom sensor.

Examples: https://scm.starbucks.com/SRE-Automation/st2examples/tree/master/triggers

Additonal Documentation: https://docs.stackstorm.com/sensors.html