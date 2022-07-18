**Policies**
Policies allows users to enforce different rules regarding action executions.

To list the types of policy that are available, run: st2 policy-type list.

Policy configuration files should be stored in the policies folder in their respective packs, similar to actions and rules. Policies can be loaded into StackStorm via st2ctl reload --register-policies. Once policies are loaded into StackStorm, run the command st2 policy list to view the list of policies in effect.

Additional Documentation: https://docs.stackstorm.com/reference/policies.html
