from woke_tests.common import *
from .d_impl import *

class Flows(Impl):
    @flow()
    def flow_random_int(s):
        # ===== Randomize =====
        x = random_int(0, 10)

        # ===== Implement =====
        s.impl_random_int(x)


    @flow()
    def flow_ask(s):
        user = s.random_user()
        s.impl_ask(user, s.daiFab.tub(), random_int(1, s.gem.balanceOf(user)))
    
    @flow()
    def flow_bid(s):
        user = s.random_user()
        s.impl_bid(user, s.daiFab.tub(), random_int(1, s.gem.balanceOf(user)))
    
    @flow()
    def flow_join(s):
        user = s.random_user()
        val = random_int(1, s.gem.balanceOf(user))
        print(val)
        s.impl_join(user, s.daiFab.tub(), s.gem, val)
        
