# Setup Guide

This guide provides instructions on setting up the script for your Razor Basilisk v3 Pro device.

## Tested Devices
- Razor Basilisk v3 Pro

## Requirements
Before running the script, make sure you have the following:

1. **Device Name**: You need to provide the name of your device for the PowerShell command to work. If you don't, an error will be raised to let you know. You can find the device name in Device Manager under Bluetooth. Navigate to: `Device Manager > Bluetooth > [mouse, keyboard, headphones name]`.

2. **Connectivity Type**: The script has been tested with the Razor Basilisk v3 Pro mouse on Bluetooth mode. Therefore, the default setting is `Bluetooth`. If you're using a different device or connectivity type, you may need to modify this setting. To locate the Bluetooth dropdown in Device Manager, go to: `Device Manager > Bluetooth`.

3. **Device Battery Data**: By default, the script assumes that the device battery percentage is stored at `{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2`. To verify if this is the case, follow these steps:
   - Go to `Device Manager > Bluetooth > [mouse, keyboard, headphones name] > Properties > Details > Property`.
   - Click on the dropdown and search for `{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2"`.
   - Alternatively, you can run the following command in PowerShell: `(Get-PnpDevice -Class 'Bluetooth' -FriendlyName 'YOUR_DEVICE_NAME' | Get-PnpDeviceProperty -KeyName '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2').Data`.
   - The PowerShell command should return the battery percentage value, such as `90` or `50`.
    - The Device Manager window should display the battery percentage as `90%` or `50%`.

## Instructions
Follow these steps to set up the script:

1. You need to import the function into your own script:<br>`from BatteryPersentage import GetDeviceBatteryPersentage`

2. Just for testing purposes, you can print it:<br>`print(GetDeviceBatteryPersentage("YOUR_DEVICE_NAME"))`

## Additional Notes
- Make sure your device is properly paired with your computer before running the script.

feel free to reach out if you have any questions or need further clarification.