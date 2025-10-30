import requests
import time
import threading
from datetime import datetime

class InteractiveDoorMonitor:
    def __init__(self):
        self.BLYNK_AUTH = "DRqlWX25YznvYkOvUgNGGUX_xRKtSM5F"
        self.BLYNK_SERVER = "blynk.cloud"
        self.VIRTUAL_PIN = "V26"
        
        self.last_door_state = None
        self.is_monitoring = True
        self.user_input_active = False
    
    
    def get_door_status(self):
        try:
            url = f"https://{self.BLYNK_SERVER}/external/api/get"
            params = {
                'token': self.BLYNK_AUTH,
                self.VIRTUAL_PIN: ''
            }
            
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                value = response.text.strip()
                return value
            else:
                print(f"Failed to get door status: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error reading door status: {str(e)}")
            return None
    
    def send_door_command(self, command):
        try:
            url = f"https://{self.BLYNK_SERVER}/external/api/update"
            params = {
                'token': self.BLYNK_AUTH,
                self.VIRTUAL_PIN: 1 if command == "open" else 0
            }
            
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                print(f"Door command sent: {command.upper()}")
                return True
            else:
                print(f"Failed to send command: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"Error sending command: {str(e)}")
            return False
    
    
    def get_user_input(self):
        self.user_input_active = True

        print("DOOR IS CLOSED!")
        print("Would you like to open the door?")
        print("Options:")
        print("  [y] Yes - Open the door")
        print("  [n] No - Keep door closed")
        print("  [q] Quit monitoring")

        
        while self.user_input_active:
            try:
                user_choice = input("Enter your choice (y/n/q): ").lower().strip()
                
                if user_choice in ['y', 'yes']:
                    print("Opening door...")
                    if self.send_door_command("open"):
                        print("Door opening command sent successfully!")
                    break
                    
                elif user_choice in ['n', 'no']:
                    print("Door will remain closed.")
                    break
                    
                elif user_choice in ['q', 'quit']:
                    print("Stopping door monitor...")
                    self.is_monitoring = False
                    break
                    
                else:
                    print("Invalid choice. Please enter 'y', 'n', or 'q'")
                    
            except Exception as e:
                print(f"Input error: {str(e)}")
                break
        
        self.user_input_active = False
        print("-" * 50)
    

    def monitor_door(self):
        while self.is_monitoring:
            try:
                if self.user_input_active:
                    time.sleep(1)
                    continue
            
                current_status = self.get_door_status()
                
                if current_status is not None:
                    if current_status != self.last_door_state:
                        if current_status == "0":
                            print(f"Door Closed")
                            self.get_user_input()
                            
                        elif current_status == "1":
                            print(f"Door status: OPEN")
                        
                        self.last_door_state = current_status
                    
                    else:
                        status_text = "OPEN" if current_status == "1" else "CLOSED"
                        print(f"Door status: {status_text} (monitoring...)")
                
                time.sleep(1)
                
            except Exception as e:
                print(f"Monitoring error: {str(e)}")
                time.sleep(5)
    

    def start(self):
        try:
            initial_status = self.get_door_status()
            print("STARTING MONITORING")
            self.last_door_state = initial_status
            
            print()
            
            self.monitor_door()
            
        except Exception as e:
            print(f"Monitor error: {str(e)}")
        finally:
            print("\nDoor monitor stopped")


if __name__ == "__main__":
    monitor = InteractiveDoorMonitor()
    monitor.start()