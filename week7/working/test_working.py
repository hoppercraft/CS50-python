from working import convert
import pytest

def test_offhours():
    assert convert("12 AM to 1 PM") == "00:00 to 13:00"
    assert convert("1:00 AM to 3:05 PM") == "01:00 to 15:05"

def test_valueerror():
    with pytest.raises(ValueError):
        convert("1 - 5")
    with pytest.raises(ValueError):
        convert("14 AM to 3 PM")


