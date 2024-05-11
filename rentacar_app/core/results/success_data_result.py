from dataclasses import dataclass
from rentacar_app.core.results.data_result import DataResult

@dataclass
class SuccessDataResult(DataResult):
    success:True