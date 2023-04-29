
from subprocess import check_output

def GetDeviceBatteryPersentage(device_name: str = None, connectivity_type: str = "Bluetooth", device_battery_data: str = "{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2"):
    """Gets bluetooth devices battery persentage from '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2' and returns data as an integer"""
    if device_name is not None:
        try: 
            powershell_script = f"(Get-PnpDevice -Class '{connectivity_type}' -FriendlyName '{device_name}' | Get-PnpDeviceProperty -KeyName '{device_battery_data}').Data"
            battery_output = check_output(["powershell.exe", "-WindowStyle", "Hidden", "-Command", powershell_script])
            battery_int = int(battery_output.decode().strip())
            return battery_int
        except Exception as error:
            return error
    else:
        raise ValueError("device_name must be provided")

print(GetDeviceBatteryPersentage("BSK V3 PRO")) # "BSK V3 PRO" is the device name. You have to change this to your own device name