from woke_tests.common import *
from .a_init import *

class Helpers(Init):
    def random_user(s) -> Account:
        return random.choice(s.users)

    def random_pair(s) -> UniswapV2Pair:
        return random.choice(s.pairs)

    def random_token(s) -> UniswapV2ERC20:
        return random.choice(s.tokens)
    
    @staticmethod
    def constant_product(x: int, y: int, deltaX: int) -> float:
        num = y * deltaX
        den = x + deltaX
        return num / den
