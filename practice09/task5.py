print("Vadym Soltys, IT-32")

d = 27
c = 6
n = d * c

divisors = []
divisors_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        divisors_sum += i

print(f"n = {d} * {c} = {n}")
print("Divisors: " + " ".join(str(x) for x in divisors))
print(f"Divisors count: {len(divisors)}, sum: {divisors_sum}")

is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

primes = []
for candidate in range(2, n + 1):
    is_candidate_prime = True
    for i in range(2, candidate):
        if candidate % i == 0:
            is_candidate_prime = False
            break
    if is_candidate_prime:
        primes.append(candidate)

print("Primes up to " + str(n) + ": " + " ".join(str(x) for x in primes))
print(f"Primes count: {len(primes)}")