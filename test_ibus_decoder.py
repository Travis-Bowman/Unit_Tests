# tests/test_ibus_decoder.py

from controltower.ibus_decoder import decode_channel

def test_decode_channel_center():
    assert decode_channel(1500) == 0.0

def test_decode_channel_max():
    assert decode_channel(2000) == 1.0

def test_decode_channel_min():
    assert decode_channel(1000) == -1.0
