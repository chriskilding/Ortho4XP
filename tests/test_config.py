""" Tests for the config module.
"""

import pathlib

from src.config import AppConfig, Config


class TestConfig:
    def test_inializes(self):
        config = Config()
        assert isinstance(config.app, AppConfig)


class TestAppConfig:
    def test_intializes_to_default_values(self):
        app_config = AppConfig()
        assert app_config.verbosity == 1
        assert app_config.cleaning_level == 1
        assert app_config.overpass_server_choice is None
        assert app_config.skip_downloads is False
        assert app_config.skip_converts is False
        assert app_config.max_convert_slots == 4
        assert app_config.check_tms_response
        assert app_config.http_timeout == 10
        assert app_config.max_connect_retries == 5
        assert app_config.max_baddata_retries == 5
        assert app_config.ovl_exclude_pol == [0]
        assert app_config.ovl_exclude_net == []
        assert app_config.xplane_install_dir is pathlib.Path()
        assert app_config.custom_overlay_src == pathlib.Path()
