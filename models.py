from dataclasses import dataclass

@dataclass
class Stake:
    value: float
    shares: float
        
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
    
    