from dataclasses import dataclass, field
from typing import List


@dataclass
class FinancialTimeSeries:

    company: str

    years: List[int]

    revenue: List[float] = field(default_factory=list)

    operating_income: List[float] = field(default_factory=list)

    net_income: List[float] = field(default_factory=list)

    operating_cash_flow: List[float] = field(default_factory=list)

    free_cash_flow: List[float] = field(default_factory=list)

    total_assets: List[float] = field(default_factory=list)

    total_liabilities: List[float] = field(default_factory=list)

    shareholders_equity: List[float] = field(default_factory=list)