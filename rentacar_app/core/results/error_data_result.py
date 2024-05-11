from dataclasses import dataclass
from rentacar_app.core.results.data_result import DataResult

@dataclass
class ErrorDataResult(DataResult):
    success:False