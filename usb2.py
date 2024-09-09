import usb.core
import usb.util

# Find the USB device. You can pass specific vendor and product IDs if you know them.
device = usb.core.find(find_all=True)

if device is None:
    raise ValueError("Device not found")

# Loop through devices and print info
for dev in device:
    print(f"Vendor ID: {hex(dev.idVendor)}")
    print(f"Product ID: {hex(dev.idProduct)}")
    
    manufacturer = usb.util.get_string(dev, dev.iManufacturer)
    product = usb.util.get_string(dev, dev.iProduct)
    serial_number = usb.util.get_string(dev, dev.iSerialNumber)

    print(f"Manufacturer: {manufacturer}")
    print(f"Product: {product}")
    print(f"Serial No: {serial_number}")
