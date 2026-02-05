class SimulatedDevice:
    def __init__(self):
        self.power = False
        self.status = "OFF"

    def power_on(self):
        self.power = True
        self.status = "READY"
        return "DEVICE ON"

    def power_off(self):
        self.power = False
        self.status = "OFF"
        return "DEVICE OFF"

    def get_status(self):
        return self.status

    def send_command(self, command):
        if not self.power:
            return "ERROR: DEVICE OFF"

        if command == "PING":
            return "PONG"
        elif command == "RESET":
            self.status = "RESET"
            return "DEVICE RESET"
        elif command == "GET_TEMP":
            return "TEMP: 25°C"
        else:
            return "UNKNOWN COMMAND"

    def simulate_failure(self):
        """Simula uma falha no dispositivo"""
        if self.power:
            self.status = "ERROR"
            return "SIMULATED FAILURE"
        return "DEVICE IS OFF"