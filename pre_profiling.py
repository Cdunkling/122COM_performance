import sys

def find_first_n_version1(self, n):
	primes = [2]

	counter = 3
	while len(self.primes) < n:
		prime = True

		for i in range(3,counter):
			if counter % i == 0:
				prime = False

		if prime:
			self.primes.append(counter)

		counter += 1

	return primes

def find_first_n_version2(self, n):
	primes = []

	counter = 2
	while len(self.primes) < n:
		prime = True

		for i in self.primes:
			if counter % i == 0:
				prime = False

		if prime:
			self.primes.append(counter)

		counter += 1

	return primes

def main():
	primesToFind = 1000

	find_first_n_version1( primesToFind )
	find_first_n_version2( primesToFind )

if __name__ == '__main__':
	sys.exit(main())