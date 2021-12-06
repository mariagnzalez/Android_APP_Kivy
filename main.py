from kivy.logger import Logger
from able import BluetoothDispatcher, GATT_SUCCESS
 
#Setup BLE interface 
 
class BLE(BluetoothDispatcher):
 
    def on_connection_state_change(self, status, state):
        Logger.info("on_connection_state_change: status=%s, state=%s", status, state)
        if status == GATT_SUCCESS and state:
            Logger.info("Connection: succeed")
 
    def on_services(self, status, services):
        Logger.info("on_services: status=%s", status)
        if status == GATT_SUCCESS:
            Logger.info("services discovered: %s", list(services.keys()))
            # save discovered services object
            self.services = services
 
    def on_characteristic_read(self, characteristic, status):
        Logger.info("on_characteristic_read: status=%s, characteristic=%s", status,
                    characteristic.getUuid().toString())
        if status == GATT_SUCCESS:
            Logger.info("Characteristic read: succeed")
 

ble = BLE()
print(ble)
 
#Get list of paired BLE devices
 
for device in ble.bonded_devices:
    # device: https://developer.android.com/reference/android/bluetooth/BluetoothDevice
    print(type(device), device.getName(), "address:", device.getAddress())

#Connect to remote device by a hardware address¶
 
ble.connect_by_device_address("AA:AA:AA:AA:AA:11")
 
#Discover device services and characteristics
ble.discover_services()
