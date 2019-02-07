def main():
	entrada = int(input())
	pond = []
	pond = {2.0,3.0,5.0}
	vector = [entrada],[4]

	index = 0
	for index in range(entrada):

		position = 0
		for position in range(3):
			vector[index][position] = float(input())
			vector[index][3] += (vector[index][position] * pond[position])

		vector[index][3] = (vector[index][3] / (pond[0] + pond[1] + pond[2]))

		print(vector[index][3])


main()