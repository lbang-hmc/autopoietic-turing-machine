from relay import Relay
from time import sleep

# Create a relay object, using the vendor/product, which you can find with `lsusb`,
# then just add the 0x prefix. The id/vendor pair below are the default parameters,
# so you can try to instantiate with Relay() and hope you are lucky.
relay = Relay(idVendor=0x16c0, idProduct=0x05df)

sleep(3)

for r in range(1,7):
    relay.state(r, on=True)
    sleep(0.1)
    relay.state(r, on=False)
    sleep(1)
    



# Turn all switches off
relay.state(0, on=False)

