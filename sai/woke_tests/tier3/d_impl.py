from woke_tests.common import *
from .c_hooks import *

class Impl(Hooks):
    def impl_random_int(s, x: int):
        # ===== Effects =====
        # ===== Checks  =====
        assert x >= 0
        assert x <= 10
    
    def impl_ask(s, user: Account, tub: SaiTub, wad: int):
        v = tub.ask(wad, from_=user)
        assert v > 0
    
    def impl_bid(s, user: Account, tub: SaiTub, wad: int):
        v = tub.bid(wad, from_=user)
        assert v > 0
    
    def impl_join(s, user: Account, tub: SaiTub, gem: ERC20, wad: int):
        gem.approve(tub, wad, from_=user)
        tub.join(wad, from_=user)
        assert True
    
    def impl_exit(s, user: Account, tub: SaiTub, wad: int):
        _ = tub.exit(wad, from_=user)
        assert True
    
    def impl_open(s, user: Account, tub: SaiTub):
        cup = tub.open(from_=user).return_value
        return cup
    
    def impl_give(s, user: Account, tub:SaiTub, to: Account, cup):
        _ = tub.give(cup, to, from_=user)
        assert True
    
    def impl_lock(s, user: Account, tub: SaiTub, skr: DSToken, wad: int, cup):
        skr.approve(tub, wad, from_=user)
        _ = tub.lock(cup, wad, from_=user)
        assert True 
    
    def impl_free(s, user: Account, tub: SaiTub, wad: int, cup):
        _ = tub.free(cup, wad, from_=user)
        assert True 
    
    # def impl_draw(s, user: Account, tub: SaiTub, wad: int, cup):








