import usb.core
import usb.util
import usb.backend.libusb1
import sys

def main(fd):
    # Manually specify the libusb1 backend with an explicit path to the library
    backend = usb.backend.libusb1.get_backend(find_library=lambda x: "/data/data/com.termux/files/usr/lib/libusb-1.0.so")

    if backend is None:
        print("libusb backend still not found")
        return

    # Find the USB device using the libusb backend
    dev = usb.core.find(find_all=True, backend=backend)

    if dev is None:
        raise ValueError("Device not found")

    # Print basic device information
    for device in dev:
        print(f"Vendor ID: {hex(device.idVendor)}")
        print(f"Product ID: {hex(device.idProduct)}")
        
        manufacturer = usb.util.get_string(device, device.iManufacturer, backend=backend)
        product = usb.util.get_string(device, device.iProduct, backend=backend)

        print(f"Manufacturer: {manufacturer}")
        print(f"Product: {product}")

        # Get serial number if available
        if device.iSerialNumber:
            serial_number = usb.util.get_string(device, device.iSerialNumber, backend=backend)
            print(f"Serial No: {serial_number}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python usbtest.py <file_descriptor>")
        sys.exit(1)

    fd = sys.argv[1]
    main(fd)
