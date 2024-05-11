from dataclasses import dataclass, field
from rentacar_app.core.results.result import Result

@dataclass
class DataResult(Result):
    data:any = field(default=None)