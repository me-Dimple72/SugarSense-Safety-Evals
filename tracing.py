import json, time
from datetime import datetime, timezone

def traced(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result, error = None, None
        try:
            result = fn(*args, **kwargs)
            return result
        except Exception as e:
            error = str(e)
            raise
        finally:
            record = {
                "time": datetime.now(timezone.utc).isoformat(),
                "step": fn.__name__,
                "input": [str(a) for a in args],
                "output": result,
                "error": error,
                "latency_s": round(time.time() - start, 3),
            }
            with open("traces.jsonl", "a") as f:
                f.write(json.dumps(record) + "\n")
    return wrapper