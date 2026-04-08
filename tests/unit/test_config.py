from mineralmatrix.config import settings

def test_settings_has_database_url() -> None:
    assert settings.database_url
