# for loop
primes = [2, 3, 5, 7, 11]
for prime in primes:
    print(prime)

# range() function usages
for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)

print("break--------")

# break and continue usages are the same as Java
# else can be used with loop
# else is skipped when break is executed but is not skipped when continue is executed.

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % count)
