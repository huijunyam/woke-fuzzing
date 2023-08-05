from woke_tests.common import *
from .b_helpers import *

class Hooks(Helpers):
    @override
    def pre_sequence(s):
        s.tokens = []
        s.pairs = []

        for i in range(NUM_TOKENS):
            decimals = random_int(
                # TOKEN_MIN_DECIMALS,
                18,
                # TOKEN_MAX_DECIMALS,
                18,
            )
            total_supply = NUM_USERS * NUM_TOKENS_EACH_USER * 10**decimals
            token: UniswapV2ERC20 = UniswapV2ERC20.deploy(from_=s.paccs[0])
            token.label = num_to_letter(i).upper()
            token.mint(s.paccs[0], total_supply,from_=s.paccs[0])
            print(f'Created token {token.label} with {decimals} decimals and {total_supply} total supply')
            
            s.tokens.append(token)
            
            for j in range(NUM_USERS):
                _ = token.transfer(s.users[j], NUM_TOKENS_EACH_USER * 10**decimals, from_=s.paccs[0])
        
        s.factory = UniswapV2Factory.deploy(s.paccs[0], from_=s.paccs[0])
        pair = UniswapV2Pair(
            s.factory.createPair(s.tokens[0], s.tokens[1], from_=s.paccs[0]).return_value
        )

        # add liquidity
        _ = s.tokens[0].transfer(pair, 1001, from_=s.users[0])
        _ = s.tokens[1].transfer(pair, 1001, from_=s.users[0])
        liq = pair.mint(s.users[0], from_=s.users[0]).return_value
        assert liq == 1
        
        s.pairs.append(pair)

    @override
    def pre_flow(s, flow: Callable[..., None]):
        with open(csv, 'a') as f:
            _ = f.write(f'{s.sequence_num},{s.flow_num},{flow.__name__}\n')

    @override
    def post_sequence(s):
        s.tokens = None  # pyright: ignore [reportGeneralTypeIssues]
        s.factory = None  # pyright: ignore [reportGeneralTypeIssues]
        s.pairs = None  # pyright: ignore [reportGeneralTypeIssues]
