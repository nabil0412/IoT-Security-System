# IoT Security System

A comprehensive IoT-based security system featuring remote door control, motion detection, real-time camera monitoring, and intelligent intruder alert mechanisms using ESP32 microcontroller and PyQt5 GUI application.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Hardware Components](#hardware-components)
- [Software Components](#software-components)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Technical Details](#technical-details)
- [Demo Videos](#demo-videos)
- [Contributors](#contributors)

## 🔍 Overview

This IoT Security System provides a complete home security solution with remote monitoring and control capabilities. The system integrates hardware components (ESP32, PIR sensor, servo motor, buzzer) with a user-friendly desktop application for real-time surveillance and door control.

##  Features

### Hardware Features
- **Automated Door Control**: Servo motor-based door mechanism with open/close functionality
- **Motion Detection**: PIR sensor for detecting unauthorized entry
- **Audio Alerts**: Buzzer for immediate audible warnings
- **WiFi Connectivity**: ESP32-based wireless communication
- **Cloud Integration**: Blynk IoT platform for remote control

### Software Features
- **Real-time Camera Feed**: Live video streaming from connected camera
- **Video Recording**: Capture and save security footage with timestamps
- **Remote Door Control**: Open/close door remotely via GUI
- **User Authentication**: Secure login system with email/password
- **Status Monitoring**: Real-time door status updates
- **Intruder Detection Alert**: Automatic notification when motion is detected
- **Modern UI**: Dark-themed, responsive PyQt5 interface

## System Architecture

The system consists of three main layers:

1. **Hardware Layer**: ESP32 microcontroller with sensors and actuators
2. **Cloud Layer**: Blynk IoT platform for device communication
3. **Application Layer**: Python GUI for user interaction and monitoring

```
┌─────────────────┐
│   PyQt5 GUI     │ ← User Interface
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Blynk Cloud    │ ← Communication Layer
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  ESP32 + IoT    │ ← Hardware Layer
│   Sensors       │
└─────────────────┘
```

## 🔧 Hardware Components

| Component | Description | Pin Connection |
|-----------|-------------|----------------|
| ESP32 DevKit | Main microcontroller | - |
| PIR Motion Sensor | HC-SR501 motion detector | GPIO 14 |
| Servo Motor | SG90 180° servo | GPIO 27 |
| Buzzer | Active buzzer module | GPIO 26 |
| USB Camera | Video capture device | USB Port |

### Circuit Connections
- **PIR Sensor**: VCC → 5V, GND → GND, OUT → GPIO 14
- **Servo Motor**: VCC → 5V, GND → GND, Signal → GPIO 27
- **Buzzer**: VCC → 5V, GND → GND, Signal → GPIO 26

## Software Components

### Arduino Code (`Control_on_WiFi.ino`)
- ESP32 firmware written in C++
- Blynk library integration for cloud connectivity
- Real-time sensor monitoring and actuator control
- Automatic door closing on motion detection

### Python GUI Application
**Main Files:**
- `NetworkMain.py`: Main application logic and event handlers
- `UI_MainWindow.py`: Auto-generated UI components from Qt Designer
- `bridge1.py`: Blynk API communication bridge
- `form.ui`: Qt Designer UI layout file
- `resources_rc.py`: Compiled Qt resources

### Key Technologies
- **PyQt5**: GUI framework
- **OpenCV (cv2)**: Camera capture and video recording
- **Blynk API**: IoT device communication
- **Qt Designer**: UI design tool

## Installation

### Prerequisites
- Python 3.7 or higher
- Arduino IDE 1.8 or higher
- ESP32 board support in Arduino IDE
- USB camera connected to computer

### Hardware Setup
1. Install Arduino IDE
2. Add ESP32 board support:
   - Go to File → Preferences
   - Add to Additional Board URLs: `https://dl.espressif.com/dl/package_esp32_index.json`
3. Install required libraries:
   - Blynk (by Volodymyr Shymanskyy)
   - ESP32Servo

### Software Setup

1. **Clone the repository:**
```bash
git clone https://github.com/nabil0412/IoT-Security-System.git
cd IoT-Security-System
```

2. **Install Python dependencies:**
```bash
pip install PyQt5
pip install opencv-python
pip install requests
```

3. **Upload Arduino code:**
   - Open `Arduino Code/Control_on_WiFi/Control_on_WiFi.ino`
   - Update WiFi credentials:
     ```cpp
     char ssid[] = "YOUR_WIFI_SSID";
     char pass[] = "YOUR_WIFI_PASSWORD";
     ```
   - Select ESP32 board and port
   - Upload to ESP32

4. **Configure Blynk:**
   - Create a Blynk account at [blynk.io](https://blynk.io/)
   - Create a new template/device
   - Add a Virtual Pin V26 (Switch widget)
   - Update the auth token in both Arduino and Python code

## Usage

### Running the Application

1. **Power on the ESP32 device**
2. **Launch the Python application:**
```bash
cd "Main App (GUI)/NetworksGUI"
python NetworkMain.py
```

3. **Login with credentials:**
   - Default: `mohamed.elsayedt10@gmail.com` / `1234`
   - Test account: `test` / `123`

### Using the System

1. **Monitor Camera Feed**: View real-time video in the main window
2. **Control Door**:
   - Click "Open Door" to unlock
   - Click "Close Door" to lock
3. **Record Video**:
   - Click "Start Record" to begin recording
   - Click "Stop Record" to save footage
4. **Monitor Status**: Check the status label for door state and alerts

### Intruder Detection
When motion is detected:
1. PIR sensor triggers
2. Buzzer sounds briefly
3. Door automatically closes (if open)
4. GUI displays "Intruder Detected - Door Closed" alert

## Configuration

### Blynk Configuration
Update the following in both `Control_on_WiFi.ino` and `bridge1.py`:
```cpp
#define BLYNK_AUTH_TOKEN "YOUR_TOKEN_HERE"
```

### WiFi Configuration
In `Control_on_WiFi.ino`:
```cpp
char ssid[] = "YOUR_WIFI_SSID";
char pass[] = "YOUR_WIFI_PASSWORD";
```

### User Accounts
In `NetworkMain.py`, modify the login credentials:
```python
self.LoginData = {
    "your.email@example.com": your_password,
    "test": 123
}
```

## Technical Details

### Communication Protocol
- **Blynk Virtual Pin V26**: Door control (0 = closed, 1 = open)
- **HTTP REST API**: GET requests for status updates and commands
- **Polling Interval**: 2 seconds for door status checks

### Video Recording
- **Format**: MP4 (mp4v codec)
- **Frame Rate**: 30 FPS
- **Storage**: `recordings/` directory with timestamp-based filenames
- **Naming**: `recording_YYYYMMDD_HHMMSS.mp4`

### Door States
- **0°**: Closed position (servo angle 0)
- **90°**: Open position (servo angle 90)
- **Transition Time**: 500ms

## Demo Videos

The repository includes demonstration videos showing:
- **Login Process**: `Log In.mkv`
- **Door Operation**: `Opening & Closing Door.mkv`
- **Intruder Detection**: `Intruder Detected.mkv`

*(Note: Video files are not included in the git repository)*

## 📄 Project Documentation

Detailed project report available in the PDF documentation (not included in repository).

## Security Considerations

- Change default login credentials before deployment
- Use strong WiFi passwords
- Keep Blynk auth tokens private
- Regularly update firmware and software
- Ensure camera feed is on secure network

## Troubleshooting

### ESP32 Won't Connect to WiFi
- Verify SSID and password
- Check WiFi signal strength
- Ensure 2.4GHz WiFi is enabled (ESP32 doesn't support 5GHz)

### Camera Not Working
- Check camera permissions
- Verify camera is connected and recognized by OS
- Try changing camera index in `CameraThread` (change `cv2.VideoCapture(0)` to `(1)`)

### Door Not Responding
- Verify Blynk credentials
- Check internet connection
- Ensure ESP32 is powered and connected
- Test servo motor separately

### GUI Not Opening
- Verify all Python dependencies are installed
- Check for Qt compatibility issues
- Review console for error messages

##  Contributors

This project was developed as part of the Advanced Networks course (4302).
Abdelrahman Mahmoud
Muhammed Sherief
Laila Kariem
Mohamed Elsayed

##  License

This project is for educational purposes. Feel free to modify and use for your own security system implementations.

## 🔗 Links

- [Blynk IoT Platform](https://blynk.io/)
- [ESP32 Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)

##  Support

For issues and questions, please open an issue on the GitHub repository.

---

**Version**: 1.0  
**Last Updated**: 2025  
**Project Type**: IoT Security System

