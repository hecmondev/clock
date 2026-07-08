from pathlib import Path


def get_root_path() -> Path:
    return Path(__file__).resolve().parent.parent


def get_asset(filename: str) -> str:
    asset_path = get_root_path() / 'ui' / 'assets' / filename
    if not asset_path.exists():
        raise FileNotFoundError(f"Asset '{filename}' not found in assets directory")
    return str(asset_path)
