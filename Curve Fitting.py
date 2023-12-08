from scipy.interpolate import UnivariateSpline
import random as rd
import matplotlib.pyplot as plt
import numpy as np


class FitLine:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def calculate_error(self):
		memory = []
		for index in range(len(self.x)):
			print(self.y[index])
			stack = np.column_stack((self.x[index], self.y[index]))
			memory.append((np.std((self.x[index], self.y[index]))))

		# print(memory)
		# return (memory)

	def fit_line(self, smoothing=0):
		self.s = UnivariateSpline(self.x, self.y, s=smoothing)	
		self.xs = np.linspace(0, len(self.y), 100)
		self.ys = self.s(self.xs)

		return self.xs, self.ys
		
	def plot_all(self, errorbar = True):

		xs,ys= self.fit_line()
		
		if errorbar == True:
			error_bar = self.calculate_error()
			plt.errorbar(self.x, self.y, yerr=error_bar, fmt='.k');
			plt.style.use('seaborn-whitegrid')

		plt.style.use('seaborn-whitegrid')
		plt.plot(self.x, self.y, 'o')
		plt.plot(self.xs, self.ys)
		plt.show()


class random_walk:

	def __init__(self):
		self.y = []
		self.x = []
		self.time = 500
		self.starting_position = [0,0]
		for i  in range(self.time):
			upordown = rd.randint(0,1)
			if upordown == 0:
				self.x.append(self.generate_move())
			else:
				self.y.append(self.generate_move())

		a = [0]
		wynik = [0]
		for i in range(len(self.x)):
			a.append(i)
			wynik.append(wynik[i]+self.x[i])

		b = [0]
		wynikb = [0]
		for i in range(len(self.y)):
			b.append(i)
			wynikb.append(wynikb[i]+self.y[i])

		
		self.xa = a
		self.ya = wynik
		self.xb = b
		self.yb = wynikb
		# plt.plot(b, wynikb, label = 'y')
		# plt.plot(a, wynik, label = 'x')
		# plt.legend()

	def make_board(self, size):
		board = []
		for i in range(size):
			board.append([])
			for j in range(size):
				board[i].append(0)
		return board

	def generate_move(self):
		move = rd.randint(-1,1)
		while move == 0:
			move = rd.randint(-1,1)
		return move

	def return_values(self):
		return self.xa, self.ya, self.xb, self.yb


size = 30
y = random_walk().return_values()[1]
x = range(len(y))
FitLine(x, y).plot_all()
