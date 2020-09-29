def hamming(self):
    error = 0  # start error at 0 for bitwise XOR
    for i in range(self.size):
        if self.bits[i]:
            error = error ^ i  # if the bit at index i is true/1 then XOR it with the current error
    if error == 0:  # base case for recursion
        print("\nNo error found\n")
        return
    else:
        print("Error is at", error)
    # Error checking done now we can give the user a choice to fix the error or keep it
    user = input("Would you like to fix the error(y/n): ")
    if user == 'y' or user == 'Y':
        self.bits[error] = int(not self.bits[error])  # flip the error bit
        print("Error has been fixed...\n")
        self.hamming()  # test again to make sure proper bit has been flipped
    print("Have a nice day")
