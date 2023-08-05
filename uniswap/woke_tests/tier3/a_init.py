from woke_tests.common import *
from pytypes.contracts.univ2.UniswapV2Factory import UniswapV2Factory
from pytypes.contracts.univ2.UniswapV2Pair import UniswapV2Pair
from pytypes.contracts.univ2.UniswapV2ERC20 import UniswapV2ERC20

class Init(FuzzTest):
    chain: Chain
    paccs: Tuple[Account, ...]
    users: Tuple[Account, ...]
    state: State # pyright: ignore [reportUninitializedInstanceVariable]

    # put your contracts here
    tokens: List[UniswapV2ERC20]
    factory: UniswapV2Factory
    pairs: List[UniswapV2Pair]
    ...

    def __init__(s):
        # ===== Initialize accounts =====
        super().__init__()
        s.chain = default_chain
        s.paccs = tuple(s.chain.accounts[i] for i in range(NUM_PACCS))
        s.users = s.chain.accounts[NUM_PACCS:NUM_PACCS+NUM_USERS]


        # ===== Add labels =====
        for idx, usr in enumerate(s.users):
            usr.label = crypto_names[idx]

