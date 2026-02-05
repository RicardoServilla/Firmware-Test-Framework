from device.simulated_device import SimulatedDevice

def test_power_on():
    """Testa se o dispositivo liga corretamente"""
    print("🧪 Testando ligar dispositivo...")
    device = SimulatedDevice()
    response = device.power_on()
    assert response == "DEVICE ON"
    assert device.get_status() == "READY"
    print("✅ Dispositivo ligou corretamente!")

def test_power_off():
    """Testa se o dispositivo desliga corretamente"""
    print("🧪 Testando desligar dispositivo...")
    device = SimulatedDevice()
    device.power_on()
    response = device.power_off()
    assert response == "DEVICE OFF"
    assert device.get_status() == "OFF"
    print("✅ Dispositivo desligou corretamente!")

def test_double_power_on():
    """Testa ligar dispositivo já ligado"""
    print("🧪 Testando ligar dispositivo já ligado...")
    device = SimulatedDevice()
    device.power_on()
    response = device.power_on()
    assert response == "DEVICE ON"
    print("✅ Comando reconhecido mesmo já ligado!")