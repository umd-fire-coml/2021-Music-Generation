from src.check_env import check_env
from src.dummy_trainer import get_history

def test_trainer():
     assert(get_history() is not None)