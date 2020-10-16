from relay import Relay
from time import sleep

# Create a relay object, using the vendor/product, which you can find with `lsusb`,
# then just add the 0x prefix. The id/vendor pair below are the default parameters,
# so you can try to instantiate with Relay() and hope you are lucky.
relay = Relay(idVendor=0x16c0, idProduct=0x05df)

# # (Setter) Turn switch 1 on
# relay.state(1, on=True)
# sleep(1)
# relay.state(2, on=True)
# sleep(1)
# relay.state(3, on=True)
# sleep(1)
# relay.state(4, on=True)
# sleep(1)
# relay.state(5, on=True)
# sleep(1)

sleep(1)


for i in range(5):
	relay.state(4, on=True)
	sleep(0.1)
	relay.state(4, on=False)
	sleep(0.1)


# relay.state(7, on=True)
# sleep(1)
# relay.state(8, on=True)
# sleep(1)

# for i in range (1,7):
# 	relay.state(i, on=True)
# 	sleep(0.01)
# 	# sleep(0.1 * i)
# 	relay.state(i, on=False)
# 	sleep(0.01)
	

# for i in range (1,9):
# 	relay.state(i, on=False)
# 	# sleep(0.1)




# (Getter) Print the status of switch 1 (returns True/False)
print(relay.state(1))

# This is just here so you hear a audible 'click' when the relay trips
sleep(1)

# Turn all switches off
relay.state(0, on=False)

# Print the state of all switches (returns a list of True/False 
# per relay)
print(relay.state(0))