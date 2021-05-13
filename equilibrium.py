import random
import matplotlib.pyplot as plt
import argparse

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--population_1', type=int, 
		default='10',
		help='Number of particles in population 1. Default: 10')

	parser.add_argument('--population_2', type=int, 
		default=10000,
		help='Number of particles in population 2. Default: 10,000')

	parser.add_argument('--transition_likelihood', type=float, 
		default=0.125,
		help='Likelihood of an element of population 1 making a transition to population 2, or vice versa. Default: 0.125')

	parser.add_argument('--iterations', type=int, 
		default=100,
		help='Number of simulation iterations. Default: 100')

	args = parser.parse_args()
	return args



def main(r1, r2, threshold, iterations):
	r1_list = []
	r2_list = []
	for i in range(iterations):
		r1_list.append(r1)
		r2_list.append(r2)
		to_move_R1 = 0
		to_move_R2 = 0
		for i in range(r1):
			roll_1 = random.random()
			if roll_1 < threshold:
				to_move_R1 += 1
		for i in range(r2):
			roll_2 = random.random()
			if roll_2 < threshold:
				to_move_R2 += 1
		r2 += to_move_R1
		r1 -= to_move_R1
		r1 += to_move_R2
		r2 -= to_move_R2

	plt.plot(r1_list, label="Population 1")
	plt.plot(r2_list, label="Population 2")
	plt.xlabel("Iterations")
	plt.ylabel("Population")
	plt.legend()
	plt.show()

if __name__ == "__main__":
	global args
	args = parse_args()
	main(args.population_1, args.population_2, args.transition_likelihood, args.iterations)


