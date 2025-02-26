from machine import Pin, UART
import time

# Configurarea pinii GPIO
led_red = Pin(15, Pin.OUT)       # LED roșu pe GPIO 15
led_yellow = Pin(14, Pin.OUT)    # LED galben pe GPIO 14
led_green = Pin(13, Pin.OUT)     # LED verde pe GPIO 13

# Configurarea senzorului infraroșu
ir_led = Pin(17, Pin.OUT)        # LED infraroșu pe GPIO 17 (Anod)
ir_receiver = Pin(16, Pin.IN)    # Receptor infraroșu pe GPIO 16 (Colector)

# Configurarea modulului Bluetooth
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Variabilă pentru a controla starea semaforului
semafor_running = False

def set_led_state(red, yellow, green):
    led_red.value(red)
    led_yellow.value(yellow)
    led_green.value(green)
    print(f"LED States - Red: {red}, Yellow: {yellow}, Green: {green}")
    if red == 1:
        ir_led.value(1)  # Aprinde LED-ul infraroșu
    else:
        ir_led.value(0)  # Stinge LED-ul infraroșu

def receive_bluetooth_command():
    if uart.any():
        command = uart.read().decode('utf-8').strip()
        print(f"Received command: {command}")
        return command
    return None

def check_ir_signal():
    if ir_receiver.value() == 1:
        print("IR signal received")
        # Adăugați aici acțiunile pe care doriți să le întreprindeți când se primește un semnal IR

def traffic_light_cycle():
    set_led_state(1, 0, 0)  # Roșu
    time.sleep(5)
    set_led_state(0, 1, 0)  # Galben
    time.sleep(2)
    set_led_state(0, 0, 1)  # Verde
    time.sleep(5)
    set_led_state(0, 1, 0)  # Galben
    time.sleep(2)

def main():
    global semafor_running
    while True:
        command = receive_bluetooth_command()
        if command:
            if command == 'start':
                semafor_running = True
            elif command == 'stop':
                semafor_running = False
                set_led_state(0, 0, 0)  # Oprește toate LED-urile
            else:
                print("Unknown command")

        if semafor_running:
            traffic_light_cycle()
        else:
            time.sleep(0.1)

        check_ir_signal()

if __name__ == '__main__':
    main()
