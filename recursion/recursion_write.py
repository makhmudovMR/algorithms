def main():

	def rec(lst):
		if len(lst) <= 0:

			return
		else:
			print(lst[0])
			rec(lst[1:])

	rec([i for i in range(10)])

if __name__ == "__main__":
	main()