from .timezones import timezones


def get_continents() -> list[str]:
    return list(timezones.keys())


def get_countries_by_continent(continent: str) -> dict:
    return timezones[continent]
