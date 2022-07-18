**Actions**
Actions are pieces of code that can perform arbitrary automation or remediation tasks in your environment. They can be written in any programming language.

To give you a better idea, here is a short list of tasks which can be implemented as actions:

    - restart a service on a server
    - create a new cloud server
    - acknowledge a Nagios/PagerDuty alert
    - send a notification or alert via email or SMS
    - send a notification to an IRC channel
    - send a message to Slack
    - start a Docker container
    - snapshot a VM
    - run a Nagios check

Actions can be executed when a Rule with matching criteria is triggered. Multiple actions can be strung together into a Workflow. Actions can also be executed directly from the clients via CLI, API, or UI.

Examples: https://scm.starbucks.com/SRE-Automation/st2examples/tree/master/actions