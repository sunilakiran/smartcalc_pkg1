import yaml
import os
from .exceptions import SmartCalcException

def load_config(config_path="config/config.yaml"):
    if not os.path.exists(config_path):
        return {"logging": {"level": "INFO"}}
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise SmartCalcException(f"Failed to load config: {e}")
