#DIFFERENT ERRORS AND TRY AND EXCEPTION

L = [10, 20, 30, 40, 50]

try:
 index = int(input("Enter an index "))
 print(L[index])

except (IndexError, ValueError) as k:
 print( k)


print("terminated gracefully")
little = 1 + 14 + 12 + 11 + 11
print(little)
print(130-little)