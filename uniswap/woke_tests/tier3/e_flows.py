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
    def flow_mint(s):
        user = s.random_user()
        pair = s.random_pair()
        t0 = UniswapV2ERC20(pair.token0())
        t1 = UniswapV2ERC20(pair.token1())

        (r0, r1, _) = pair.getReserves()
        t0_bal = t0.balanceOf(user)
        t1_bal = t1.balanceOf(user)
        bound_by_t0 = t0_bal / r0 < t1_bal / r1

        if bound_by_t0:
            amount0 = random_int(0, t0.balanceOf(user))
            amount1 = amount0 * r1 // r0
        else:
            amount1 = random_int(0, t1.balanceOf(user))
            amount0 = amount1 * r0 // r1

        s.impl_mint(user, pair, t0, t1, amount0, amount1)
    
    @flow()
    def flow_swap(s):
        user = s.random_user()
        pair = s.random_pair()
        t0 = UniswapV2ERC20(pair.token0())
        t1 = UniswapV2ERC20(pair.token1())

        t0_or_t1_from_user = random.choice((0, 1))
        if t0_or_t1_from_user == 0:
            token = t0
            t0_bal = t0.balanceOf(user)
            amount_from_user = random_int(0, t0_bal)
        else:
            token = t1
            t1_bal = t1.balanceOf(user)
            amount_from_user = random_int(0, t1_bal)

        s.impl_swap(user, pair, t0_or_t1_from_user, token, amount_from_user)
    
    @flow()
    def flow_create_pair(s):
        token0 = s.random_token()
        token1 = s.random_token()
        user = s.random_user()

        s.impl_create_pair(user, token0, token1)
    
    
    

