# Tap conversion using formula from Wikipedia LFSR example
# https://en.wikipedia.org/wiki/Linear-feedback_shift_register
#
# Wikipedia code: bit = (lfsr ^ (lfsr >> 1) ^ (lfsr >> 3) ^ (lfsr >> 12)) & 1
# For polynomial taps [16, 15, 13, 4], shifts are [0, 1, 3, 12]
# Formula: code_shift = register_size - diagram_tap

def convert_taps(register_size, diagram_taps):
    return tuple(register_size - tap for tap in diagram_taps)

lfsr12_taps = convert_taps(12, [2, 7])
lfsr19_taps = convert_taps(19, [5, 11])

print(f"LFSR-12: {lfsr12_taps}")
print(f"LFSR-19: {lfsr19_taps}")
