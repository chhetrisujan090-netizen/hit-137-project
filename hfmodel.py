# hfmodel.py

from base_model import BaseModel
from decorators import catch_errors, timeit

class HFModel(BaseModel):
    """HuggingFace style model example."""
    def __init__(self, name, version="1.0"):
        super().__init__(name)
        self.version = version

    @catch_errors
    @timeit
    def run_model(self, data):
        """Simulate running the model."""
        print(f"Running {self.name} v{self.version} on data: {data}")
        # Simulate some processing
        result = [d*2 for d in data]  # example
        return result
