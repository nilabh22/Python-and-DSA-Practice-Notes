############### HASHING ################
# Hashing is a method of sorting and indexing data. Hashing uses a magic function that converts the String to a number.
# That number is array or list's index which stores the string.
# Hashing is ideal for searching purposes because in best case, it takes O(1) time.

########## TERMINOLOGIES ###############

# HASH FUNCTION - It is a magical function that converts the string to numbers.
# KEY - Input data by the user.
# HASH VALUE - A value that is returned by hash function. (numbers)
# HASH TABLE - A table which stores the string under the index. The array.
# COLLISION - When two different keys to a hash function gives the same output.
### WE use the ASCII value to store in the hash table.

########### COLLISION RESOLUTION METHODS #############

# 1. Direct Chaining - It uses linked lists to avoid collison. It stores the physical location of node in the hash table whenever we get collision.
# 2. Open Addressing - Colliding elements are stored in vacant buckets.
## Three Types - A). Linear Probing - We store the colliding string to the next empty cell index.
            #    B). Quadratic Probing - We store in 1^2, 2^2, 3^2,.....
                        # If index is 2 then 2+1^2  = 3(for 1st collision)
                        # If again same index the, 2+2^2 = 6, and so on
            #    C). Double Hashing - 2nd Hash function is called.
                        # we insert 1st, then in second which have the same index as 1st - we call 2nd hash function. 2+4 = 6 (for 1st collision)
                        # In 3rd , we call call function but index of 2nd function is multiplied bt 2...... 2+ (2*4) = 10 (for 2nd collision)

######## PROS AND CONS OF COLLISION RESOLUTION TECHNIQUES ##############

# 1. Direct Chaining - Since it uses linked lists , the hash table will neve get full.
# But huge linked list causes performance leaks O(N).


# 2. Open Addressing - Easy Implementation.
## But when hash table is full, it results in performance leaks.


def mod(number, cellNumber):
    return number % cellNumber


# print(mod(400, 24))


def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

print(modASCII("ABC", 24))
