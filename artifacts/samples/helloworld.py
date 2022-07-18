import sys
import os
from st2common.runners.base_action import Action

class F5Blacklist(Action):

    def run(self, user):
        try:
            print('Hello {}'.format(user))
        except:
            sys.exit()