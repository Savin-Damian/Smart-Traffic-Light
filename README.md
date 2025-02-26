# Smart-Traffic-Light

This project presents a smart traffic light, incorporating a Raspberry Pi microcontroller designed to simulate the operation of a real traffic light. The system uses multiple hardware components to implement and control the traffic light functionality, including a Bluetooth module for receiving external commands.
Through a Python script, the traffic light manages the illumination of LEDs representing the traffic light colors (red, yellow, and green), the control of an infrared (IR) LED to transmit an IR signal to a vehicle equipped with an IR receiver to stop it at the red light, as well as receiving signals via Bluetooth.
To control the smart traffic light via Bluetooth, the Serial Bluetooth Terminal application was used. This app allows text commands to be sent from a phone to the Raspberry Pi via a Bluetooth connection. The recognized commands are start/stop to turn the traffic light on or off. Additionally, the application is available on both Android and iOS platforms.

## System Architecture 
The system uses multiple hardware components to implement and control its functionality, including a Bluetooth module for receiving external commands.

### Hardware Components:
- Breadboard: Used for connecting and organizing hardware components.
- Raspberry Pi Pico H: The main microcontroller that runs the code and manages the traffic light operation.
- Bluetooth Module HC-05: Enables wireless communication to receive start and stop commands.
- LEDs: Three LEDs (red, yellow, and green) representing the traffic light colors.
- Infrared Sensor TCRT5000: Used for transmitting and detecting infrared signals, controlling additional actions.
- Power Cable and Connection Wires: Necessary for connecting all components and ensuring proper power supply.
- Resistors (330Ω, 220Ω, 1kΩ): Limit the current flowing through the LEDs, protecting them from overheating and damage.


### Software Functionalities:
- GPIO Pin Configuration: LEDs are connected to different GPIO pins on the Raspberry Pi for control.
- Traffic Light Control: Functions for setting the LED states (red, yellow, green) and implementing a traffic light cycle that alternates colors to simulate real-world functionality.
- Bluetooth Communication: Configured to receive external commands (start and stop) to control the traffic light operation.
- Infrared Sensor: The infrared LED turns on when the red LED is active, and the IR receiver signal can trigger additional actions.
- Python: Manages the traffic light operation and integrates the above functionalities.
- Thonny: The application used to upload the code to the Raspberry Pi.

### GPIO Pin Configuration
- LEDs:
  - Red LED:
    - Anode: Connected to a 330Ω resistor, then to GPIO 15 of the Raspberry Pi.
    - Cathode: Connected to GND.
  - Yellow LED:
    - Anode: Connected to a 330Ω resistor, then to GPIO 14 of the Raspberry Pi.
    - Cathode: Connected to GND.
  - Green LED:
    - Anode: Connected to a 330Ω resistor, then to GPIO 13 of the Raspberry Pi.
    -Cathode: Connected to GND.

- Bluetooth Module HC-05:
  - VCC: Connected to VBUS of the Raspberry Pi.
  - GND: Connected to GND of the Raspberry Pi.
  - TXD: Connected to GPIO 1 of the Raspberry Pi.
  - RXD: Connected to GPIO 0 of the Raspberry Pi.

- Infrared Sensor TCRT5000:
  - Pin A (Anode): Connected to a 220Ω resistor, then to GPIO 17 of the Raspberry Pi.
  - Pin C (Cathode): Connected to GND of the Raspberry Pi.  
  - Pin C (Collector): Connected to a 1kΩ pull-down resistor, then to GPIO 16 of the Raspberry Pi.
  - Pin E (Emitter): Connected to GND of the Raspberry Pi.
