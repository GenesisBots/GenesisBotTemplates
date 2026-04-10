import json
from pathlib import Path


def load_config() -> dict:
    cfg_path = Path(__file__).parent / "config.example.json"
    with open(cfg_path, "r", encoding="utf-8") as f:
        return json.load(f)


def run():
    cfg = load_config()
    mode = cfg.get("mode", "paper")
    task = cfg.get("task", {})

    print(f"[INFO] Running in mode: {mode}")
    print(f"[INFO] Task description: {task.get('description')}")

    print("[MOCK] This is a template bot. Add your logic here.")


if __name__ == "__main__":
    run()
