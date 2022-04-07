from dataclasses import dataclass

@dataclass
class LiquidityPool:
    token: str
    value: float
    shares: float

@dataclass
class SingleStaker:
    token: str    
    wallet: float
    lp_ratio: float
    staked: float
    

@dataclass
class LPStake:
    id: int # the id of this stake
    shares: float # shares owned from the pool. Equal to the input value of the stake
    step_last_added: int # step on which the stake was last added for ILP calculation.

@dataclass
class Fund:
    token: str
    value: float
    lp_stake: LPStake
    