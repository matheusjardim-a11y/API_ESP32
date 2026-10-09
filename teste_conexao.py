import json
import time

import serial

PORTA = "COM5"
BAUD = 115200  # tem que ser igual ao Serial.begin(115200) do ESP32


def abrir_porta():
    ser = serial.Serial()
    ser.port = PORTA
    ser.baudrate = BAUD
    ser.timeout = 3
    ser.dtr = False  # evita reiniciar o ESP32 ao abrir a porta
    ser.rts = False
    ser.open()
    ser.reset_input_buffer()
    return ser


ser = None
print(f"Lendo {PORTA}... (Ctrl+C para parar)")

try:
    while True:
        # (Re)conecta se a porta ainda não está aberta
        if ser is None:
            try:
                ser = abrir_porta()
                print("Porta aberta.")
            except serial.SerialException as e:
                print(f"Aguardando a porta {PORTA}... ({e})")
                time.sleep(2)
                continue

        try:
            linha = ser.readline().decode("utf-8", errors="ignore").strip()
        except serial.SerialException as e:
            print(f"Conexão perdida: {e}")
            ser.close()
            ser = None
            time.sleep(2)
            continue

        if not linha.startswith("{"):
            continue  # ignora linhas vazias ou mensagens soltas do boot

        try:
            dados = json.loads(linha)
        except json.JSONDecodeError:
            continue  # linha cortada no início da leitura

        if "erro" in dados:
            print(f"Sensor com problema: {dados['erro']}")
        elif "temperatura" in dados:
            print(f"Temperatura: {dados['temperatura']} °C | Umidade: {dados['umidade']} %")

except KeyboardInterrupt:
    print("\nEncerrado.")
finally:
    if ser is not None and ser.is_open:
        ser.close()