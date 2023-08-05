from woke_tests.common import *
from .e_flows import *

class Invariants(Flows):
    @invariant()
    def inv_one_equals_one(s):
        assert 1 == 1
    
    @invariant()
    def inv_pair_total_supply(s):
        for p in s.pairs:
            totalSupply = p.totalSupply()
            totalBalanceOwnedByUser = 0
            for u in s.users:
                totalBalanceOwnedByUser += p.balanceOf(u)
            assert totalSupply == totalBalanceOwnedByUser or totalSupply - totalBalanceOwnedByUser == 1000
    
    @invariant()
    def token_number_equal_balance_of_pool(s):
        for p in s.pairs:
            reserves = p.getReserves()
            reserve0 = reserves[0]
            reserve1 = reserves[1]
            token0 = p.token0()
            token1 = p.token1()
            assert reserve0 == UniswapV2ERC20(token0).balanceOf(p)
            assert reserve1 == UniswapV2ERC20(token1).balanceOf(p)
    
    



