from relay import Relay
from time import sleep

# Create a relay object, using the vendor/product, which you can find with `lsusb`,
# then just add the 0x prefix. The id/vendor pair below are the default parameters,
# so you can try to instantiate with Relay() and hope you are lucky.
relay = Relay(idVendor=0x16c0, idProduct=0x5df)

# 16c0:05df


# (Setter) Turn switch 1 on

# (Getter) Print the status of switch 1 (returns True/False)
print(relay.state(1))
# This is just here so you hear a audible 'click' when the relay trips

r = 1

for i in range(5):
	relay.state(r, on=True)
	sleep(0.05)
	relay.state(r, on=False)
	sleep(2)

	# relay.state(2, on=True)
	# sleep(0.5)
	# relay.state(2, on=False)
	# sleep(1)


# Turn all switches off
relay.state(0, on=False)

# Print the state of all switches (returns a list of True/False 
# per relay)
print(relay.state(0))
