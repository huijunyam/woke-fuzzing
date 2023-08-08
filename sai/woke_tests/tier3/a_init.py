from woke_tests.common import *
from pytypes.contracts.deps.token import DSToken
from pytypes.contracts.deps.erc20 import ERC20
from pytypes.contracts.deps.value import DSValue
from pytypes.contracts.vox import SaiVox
from pytypes.contracts.tub import SaiTub
from pytypes.contracts.ERC20 import Erc20
from pytypes.contracts.pit import GemPit
from pytypes.contracts.deps.guard import DSGuard
from pytypes.contracts.fab import *

class Init(FuzzTest):
    chain: Chain
    paccs: Tuple[Account, ...]
    users: Tuple[Account, ...]
    state: State # pyright: ignore [reportUninitializedInstanceVariable]

    # put your contracts here
    # tokens: List[ERC20]
    sai: DSToken
    sin: DSToken
    skr: DSToken
    gov: DSToken
    gem: Erc20
    pip: DSValue
    pep: DSValue
    vox: SaiVox
    tub: SaiTub
    pit: GemPit
    dad: DSGuard

    def __init__(s):
        # ===== Initialize accounts =====
        super().__init__()
        s.chain = default_chain
        s.paccs = tuple(s.chain.accounts[i] for i in range(NUM_PACCS))
        s.users = s.chain.accounts[NUM_PACCS:NUM_PACCS+NUM_USERS]
        

        # ===== Add labels =====
        for idx, usr in enumerate(s.users):
            usr.label = crypto_names[idx]

