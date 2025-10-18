import pytest
import app

def test_convert_to_celsius():
    assert app.convert_to_celsius(32.0) == 0.0
    assert app.convert_to_celsius(100.0) == 37.77777777777778

def test_convert_to_fahrenheit():
    assert app.convert_to_fahrenheit(0.0) == 32.0
    assert app.convert_to_fahrenheit(37.77777777777778) == 100.0
    
def test_conversion_logic():
    # Test Fahrenheit to Celsius conversion
    fahrenheit_temp = 68.0
    expected_celsius = app.convert_to_celsius(fahrenheit_temp)
    assert expected_celsius == 20.0

    # Test Celsius to Fahrenheit conversion
    celsius_temp = 20.0
    expected_fahrenheit = app.convert_to_fahrenheit(celsius_temp)
    assert expected_fahrenheit == 68.0