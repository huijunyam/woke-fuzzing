from woke_tests.common import *
from .b_helpers import *

class Hooks(Helpers):
    @override
    def pre_sequence(s):
        # s.dad = DSGuard.deploy(from_=s.paccs[0])
        # s.dad.setOwner(owner_=s.paccs[0], from_=s.paccs[0])

        # s.sai = DSToken.deploy(symbol_="SAI", from_=s.paccs[0])
        # s.sin = DSToken.deploy(symbol_="SIN", from_=s.paccs[0])
        # s.skr = DSToken.deploy(symbol_="SKR", from_=s.paccs[0])
        s.gov = DSToken.deploy(symbol_="GOV", from_=s.paccs[0])
        s.pip = DSValue.deploy(from_=s.paccs[0])
        s.pep = DSValue.deploy(from_=s.paccs[0])
        
        # s.vox = SaiVox.deploy(par_=10 ** 27, from_=s.paccs[0])
        s.pit = GemPit.deploy(from_=s.paccs[0])
        # decimals = random_int(
        #         # TOKEN_MIN_DECIMALS,
        #         18,
        #         # TOKEN_MAX_DECIMALS,
        #         18,
        #     )
        # total_supply = NUM_USERS * NUM_TOKENS_EACH_USER * 10**decimals
        # s.gem = Erc20.deploy(_totalSupply=total_supply, from_=s.paccs[0])
        # # gem.mint(s.paccs[0], total_supply,from_=s.paccs[0])
        # print(f'Created token with {decimals} decimals and {total_supply} total supply')
        # for j in range(NUM_USERS):
        #     _ = s.gem.transfer(s.users[j], NUM_TOKENS_EACH_USER * 10**decimals, from_=s.paccs[0])

        # s.tub = SaiTub.deploy(sai_=s.sai, sin_=s.sin, skr_=s.skr, gem_=s.gem, gov_=s.gov, pip_=s.pip, pep_=s.pep, vox_=s.vox, pit_= s.pit, from_=s.paccs[0])
        # s.tub.mold(param=bytes("cap", 'utf-8'), val=0, from_=s.paccs[0])
        # s.tub.mold(param=bytes("mat", 'utf-8'), val=1500000000000000000000000000, from_=s.paccs[0])
        # s.tub.mold(param=bytes("axe", 'utf-8'), val=1130000000000000000000000000, from_=s.paccs[0])
        # s.tub.mold(param=bytes("fee", 'utf-8'), val=1000000000158153903837946257, from_=s.paccs[0])
        # s.tub.mold(param=bytes("tax", 'utf-8'), val=1000000000000000000000000000, from_=s.paccs[0])
        # s.tub.mold(param=bytes("gap", 'utf-8'), val=1000000000000000000, from_=s.paccs[0])

        # s.vox.setAuthority(s.dad, from_=s.paccs[0])
        # s.tub.setAuthority(s.dad, from_=s.paccs[0])
        # s.sai.setAuthority(s.dad, from_=s.paccs[0])
        # s.sin.setAuthority(s.dad, from_=s.paccs[0])
        # s.skr.setAuthority(s.dad, from_=s.paccs[0])
        # s.dad.permit(src=s.tub, dst=s.skr, sig=bytes("mint(address,uint256)"), from_=s.paccs[0])
        # # s.dad.permit(address(tub), address(skr), S('burn(address,uint256)'));\
        s.auth = DSAuth.deploy(from_=s.paccs[0])
        decimals = random_int(
                # TOKEN_MIN_DECIMALS,
                18,
                # TOKEN_MAX_DECIMALS,
                18,
            )
        total_supply = NUM_USERS * NUM_TOKENS_EACH_USER * 10**decimals
        s.gem = Erc20.deploy(_totalSupply=total_supply, from_=s.paccs[0])
        print(f'Created token with {decimals} decimals and {total_supply} total supply')
        for j in range(NUM_USERS):
            _ = s.gem.transfer(s.users[j], NUM_TOKENS_EACH_USER * 10**decimals, from_=s.paccs[0])

        gemFab = GemFab.deploy(from_=s.paccs[0])
        voxFab = VoxFab.deploy(from_=s.paccs[0])
        tubFab = TubFab.deploy(from_=s.paccs[0])
        tapFab = TapFab.deploy(from_=s.paccs[0])
        topFab = TopFab.deploy(from_=s.paccs[0])
        momFab = MomFab.deploy(from_=s.paccs[0])
        dadFab = DadFab.deploy(from_=s.paccs[0])
        daiFab = DaiFab.deploy(gemFab_=gemFab, voxFab_=voxFab, tubFab_=tubFab, tapFab_=tapFab, topFab_=topFab, momFab_=momFab, dadFab_=dadFab,from_=s.paccs[0])
        daiFab.makeTokens(from_=s.paccs[0])
        daiFab.makeVoxTub(gem=s.gem, gov=s.gov, pip=s.pip, pep=s.pep, pit=s.pit, from_=s.paccs[0])
        daiFab.makeTapTop(from_=s.paccs[0])
        daiFab.configParams(from_=s.paccs[0])
        daiFab.verifyParams(from_=s.paccs[0])
        daiFab.configAuth(authority=s.auth,from_=s.paccs[0])
        s.daiFab = daiFab
        


    @override
    def pre_flow(s, flow: Callable[..., None]):
        with open(csv, 'a') as f:
            _ = f.write(f'{s.sequence_num},{s.flow_num},{flow.__name__}\n')

    @override
    def post_sequence(s):
        s.gem = None 
        s.auth = None 
        s.gov = None 
        s.pip = None 
        s.pep = None 
        s.pit = None
        s.daiFab = None
