from src.config import Settings


def test_save_defaults_declared_on_class():
    """預設值宣告在類別上，不受 .env、環境變數與工作目錄影響。"""

    assert Settings.model_fields["okx_testnet"].default is True

    assert Settings.model_fields["okx_api_key"].default == ""

    assert Settings.model_fields["okx_api_secret"].default == ""

    assert Settings.model_fields["default_market"].default == "spot"


def test_env_can_override(monkeypatch, tmp_path):
    """切正式環境靠環境變數，不靠改 config.py 的預設值。"""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("OKX_TESTNET", "false")
    monkeypatch.setenv("OKX_API_KEY", "dummy-key")

    settings = Settings()

    assert settings.okx_testnet is False
    assert settings.okx_api_key == "dummy-key"
