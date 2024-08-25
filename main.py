// Start the UART service (this will make the Micro:Bit advertise itself over BLE)
bluetooth.startUartService()

// Handle received data from the UART service
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    let received = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    bluetooth.uartWriteString(received)  // Echo the received message back
})

// Optional: Add a visual indication that the Micro:Bit is ready and advertising
basic.showString("ADV")

basic.forever(function () {
    basic.pause(100)  // Keep the program running
})

