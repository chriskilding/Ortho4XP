import pytest

from Ortho4XP_v130 import main


def test_help():
    with pytest.raises(SystemExit) as e:
        main()
