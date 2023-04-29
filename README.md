# Setup guide

- Tested devices: Razor basilisk v3 pro

- This script Requires 3 main settings

1. `device_name`: This will tell the powershell command what the device name is. You can find your devices name at:<br> `Device Manager > Bluetooth > [mouse, keyboard, headphones name]`.

2. `connectivity_type`: I have only tested this script with my Razor basilisk v3 pro mouse on bluetooth mode. Therefore, I have left this setting at `Bluetooth`. This will find anything that appears in device managers bluetooth dropdown. You can find it at:<br>`Device Manager > Bluetooth`.

3. `device_battery_data`: By default this value is `{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2` since this is where the device battery persentage is stored if it has one. Just to be safe you can check if it's there by going to:<br>`Device Manager > Bluetooth > [mouse, keyboard, headphones name] > Properties > Details > Property > Click on the dropdown and search for {104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2"`<br>or run this command in powershell<br>`(Get-PnpDevice -Class 'Bluetooth' -FriendlyName 'YOUR_DEVICE_NAME' | Get-PnpDeviceProperty -KeyName '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2').Data`.<br>The powershell command should return something like: `90` or `50`<br>The device manager window should display something like `90%` or `50%`.