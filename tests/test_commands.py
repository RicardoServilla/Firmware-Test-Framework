from device.simulated_device import SimulatedDevice

def test_ping_command():
    """Testa comando PING"""
    print("🧪 Testando comando PING...")
    device = SimulatedDevice()
    device.power_on()
    response = device.send_command("PING")
    assert response == "PONG"
    print("✅ PING retornou PONG!")

def test_reset_command():
    """Testa comando RESET"""
    print("🧪 Testando comando RESET...")
    device = SimulatedDevice()
    device.power_on()
    response = device.send_command("RESET")
    assert response == "DEVICE RESET"
    assert device.get_status() == "RESET"
    print("✅ Dispositivo resetado!")

def test_get_temp_command():
    """Testa comando GET_TEMP"""
    print("🧪 Testando comando GET_TEMP...")
    device = SimulatedDevice()
    device.power_on()
    response = device.send_command("GET_TEMP")
    assert "TEMP" in response
    print(f"✅ Temperatura: {response}")

def test_multiple_commands():
    """Testa sequência de comandos"""
    print("🧪 Testando sequência de comandos...")
    device = SimulatedDevice()
    
    # Ligar
    assert device.power_on() == "DEVICE ON"
    
    # Ping
    assert device.send_command("PING") == "PONG"
    
    # Temperatura
    assert "TEMP" in device.send_command("GET_TEMP")
    
    # Reset
    assert device.send_command("RESET") == "DEVICE RESET"
    
    print("✅ Todos os comandos funcionaram!")