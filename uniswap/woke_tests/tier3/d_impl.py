from woke_tests.common import *
from .c_hooks import *

class Impl(Hooks):
    def impl_random_int(s, x: int):
        # ===== Effects =====
        # ===== Checks  =====
        assert x >= 0
        assert x <= 10

    def impl_mint(s, user: Account, pair: UniswapV2Pair, t0: UniswapV2ERC20, t1: UniswapV2ERC20, amount0: int, amount1: int):
        _ = t0.transfer(pair, amount0, from_=user)
        _ = t1.transfer(pair, amount1, from_=user)
        liq = pair.mint(user, from_=user).return_value
        assert liq > 0
    
    def impl_burn(s, user: Account, pair: UniswapV2Pair):
        _ = pair.burn(user).return_value
        assert True
    
    def impl_swap(
        s,
        user: Account,
        pair: UniswapV2Pair,
        t0_or_t1_from_user: Union[Literal[0], Literal[1]],
        token_from_user: UniswapV2ERC20,
        amount_from_user: int,
    ):
        reserves = pair.getReserves()
        x = reserves[t0_or_t1_from_user]
        y = reserves[1 - t0_or_t1_from_user]
        amount_from_user = min(amount_from_user, y)

        deltaY = s.constant_product(x, y, 996 * amount_from_user // 1000)
        _ = token_from_user.transfer(pair, amount_from_user, from_=user)
        _ = pair.swap(
            int(deltaY * t0_or_t1_from_user),
            int(deltaY * (1 - t0_or_t1_from_user)),
            user,
            b"",
            from_=user,
        ).return_value

        assert True
    
    def impl_create_pair(s, user: Account, token0: UniswapV2ERC20, token1: UniswapV2ERC20):
        should_revert = False
        if token0 == token1:
            should_revert = True
        if s.factory.getPair(token0, token1) != Address.ZERO:
            should_revert = True

        if should_revert:
            # ===== Failure =====
            with must_revert(TransactionRevertedError):
                _ = s.factory.createPair(token0, token1, from_=user)
        else:
            # ===== Success =====
            pair = UniswapV2Pair(
                s.factory.createPair(token0, token1, from_=user).return_value
            )
            # first mint needs to have geometric average at least MINIMUM_LIQUIDITY
            # = 1000
            _ = token0.mint(user, 1001, from_=user)
            _ = token1.mint(user, 1001, from_=user)
            _ = token0.transfer(pair, 1001, from_=user)
            _ = token1.transfer(pair, 1001, from_=user)
            liq = pair.mint(user, from_=user).return_value
            assert liq == 1
 
            s.pairs.append(pair)
    
