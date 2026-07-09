import numpy as np


def to_json_serializable(obj):

    if isinstance(obj, dict):
        return {
            k: to_json_serializable(v)
            for k, v in obj.items()
        }

    elif isinstance(obj, list):
        return [
            to_json_serializable(v)
            for v in obj
        ]

    elif isinstance(obj, tuple):
        return [
            to_json_serializable(v)
            for v in obj
        ]

    elif isinstance(obj, np.float32):
        return float(obj)

    elif isinstance(obj, np.float64):
        return float(obj)

    elif isinstance(obj, np.int32):
        return int(obj)

    elif isinstance(obj, np.int64):
        return int(obj)

    elif hasattr(obj, "__dict__"):
        return to_json_serializable(obj.__dict__)

    return obj