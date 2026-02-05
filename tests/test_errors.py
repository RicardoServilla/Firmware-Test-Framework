from device.simulated_device import SimulatedDevice

def test_command_when_off():
    """Testa enviar comando com dispositivo desligado"""
    print("🧪 Testando comando com dispositivo DESLIGADO...")
    device = SimulatedDevice()
    response = device.send_command("PING")
    assert "ERROR" in response
    print(f"✅ Erro correto: {response}")

def test_unknown_command():
    """Testa comando desconhecido"""
    print("🧪 Testando comando DESCONHECIDO...")
    device = SimulatedDevice()
    device.power_on()
    response = device.send_command("COMANDO_INEXISTENTE")
    assert response == "UNKNOWN COMMAND"
    print("✅ Comando desconhecido tratado!")

def test_simulate_failure():
    """Testa simulação de falha"""
    print("🧪 Testando simulação de falha...")
    device = SimulatedDevice()
    device.power_on()
    response = device.simulate_failure()
    assert response == "SIMULATED FAILURE"
    assert device.get_status() == "ERROR"
    print("✅ Falha simulada com sucesso!")

def test_failure_when_off():
    """Testa falha com dispositivo desligado"""
    print("🧪 Testando falha com dispositivo DESLIGADO...")
    device = SimulatedDevice()
    response = device.simulate_failure()
    assert response == "DEVICE IS OFF"
    print("✅ Falha bloqueada quando desligado!")