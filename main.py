import bluetooth

# Create a GATT service and characteristic for the UART
service_uuid = bluetooth.UUID("12345678-1234-1234-1234-123456789012")
char_uuid = bluetooth.UUID("12345678-1234-1234-1234-123456789013")
service = bluetooth.GATTService(service_uuid, [bluetooth.GATTCharacteristic(char_uuid, bluetooth.GATT_READ | bluetooth.GATT_WRITE)])

# Start advertising
bluetooth.advertise(service_uuid, name="BLE UART Echo")

# Function to handle incoming data
def handle_read(client_id, attribute, data):
    # Echo the received data back to the client
    bluetooth.gatt_server.send(client_id, attribute, data)

# Set the callback for incoming data
bluetooth.gatt_server.register_callback(handle_read)

# Start the GATT server
bluetooth.gatt_server.start()

# Main loop
while True:
    pass

