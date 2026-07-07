from dataclasses import dataclass, field


@dataclass
class GraphEntities:

    companies: list = field(default_factory=list)

    people: list = field(default_factory=list)

    products: list = field(default_factory=list)

    countries: list = field(default_factory=list)

    risks: list = field(default_factory=list)

    technologies: list = field(default_factory=list)

    competitors: list = field(default_factory=list)

    business_segments: list = field(default_factory=list)