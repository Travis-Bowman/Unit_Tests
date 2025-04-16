# tests/test_mode_switcher.py

from controltower.mode_switcher import get_mode_from_channel

def test_manual_mode():
    assert get_mode_from_channel(1100) == "MANUAL"

def test_semi_mode():
    assert get_mode_from_channel(1500) == "SEMI"

def test_auto_mode():
    assert get_mode_from_channel(1800) == "AUTO"
