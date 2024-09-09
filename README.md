# termux-usb-esp32 

trying to get python serial pyusb stuff working to communicate with my esp32 over python

https://wiki.termux.com/wiki/Termux-usb. i was able to get the c code working

```sh
gcc usbtest.c -lusb-1.0 -o usbtest
termux-usb -e ./usbtest /dev/bus/usb/002/002
```
