from grid import Grid


def test_algorithm(grid):
    error = 0  # start error at 0 for bitwise XOR
    for i in range(grid.size):
        if grid.bits[i]:
            error = error ^ i  # if the bit at index i is true/1 then XOR it with the current error
    if error == 0:
        print("\nNo error found\n")
        return True
    else:
        return False


# Test grids
test1 = Grid()
test1.load_bits(1)
test2 = Grid()
test2.load_bits(2)
test3 = Grid()
test3.load_bits(3)

# Hamming code
test1.print()
test1.hamming()
test1.print()
if test_algorithm(test1):
    print("Well done! Test 1 complete")
else:
    print("Try again")
print("-----------------------------------")

test2.print()
test2.hamming()
test2.print()
if test_algorithm(test2):
    print("Well done! Test 2 complete")
else:
    print("Try again")
print("-----------------------------------")

test3.print()
test3.hamming()
test3.print()
if test_algorithm(test3):
    print("Well done! Test 3 complete")
else:
    print("Try again")
print("-----------------------------------")
