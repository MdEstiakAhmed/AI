def dimension(puzzle):
	length = len(puzzle)
	return length
	

def blank_position(puzzle):
	length = dimension(puzzle)
	position = 0
	for i in range(length):
		for j in range(length):
			if puzzle[i][j] == ' ':
				position = length - i
	return position


def inversion(puzzle):
	length = dimension(puzzle)
	inversion_count = {}
	count = 0
	new_puzzle = []

	for i in puzzle:
		new_puzzle.extend(i)

	new_length = dimension(new_puzzle)

	for i in range(new_length):
		for j in range(i+1, new_length):
			if new_puzzle[i] == ' ' or new_puzzle[j] == ' ':
				continue
			else:
				if new_puzzle[i] > new_puzzle[j]:
					count = count + 1
					inversion_count.update({new_puzzle[i]:count})
		count = 0
	return sum(inversion_count.values())


def solvable(puzzle):
	dimension_ = dimension(puzzle)
	inversion_ = inversion(puzzle)
	blank_position_ = blank_position(puzzle)

	if dimension_ % 2 != 0 and inversion_ % 2 == 0:
		print("dimension is odd and value:", dimension_)
		print("inversion is even and value:", inversion_)
		print("puzzle is solvable")
		print("**************************************************")
	elif dimension_ % 2 == 0 and inversion_ % 2 == 0 and blank_position_ % 2 != 0:
		print("dimension is even and value:", dimension_)
		print("inversion is even and value:", inversion_)
		print("black box at odd row and row number is:", blank_position_)
		print("puzzle is solvable")
		print("**************************************************")
	elif dimension_ % 2 == 0 and inversion_ % 2 != 0 and blank_position_ % 2 == 0:
		print("dimension is even and value:", dimension_)
		print("inversion is odd and value:", inversion_)
		print("black box at even row and row number is:", blank_position_)
		print("puzzle is solvable")
		print("**************************************************")
	else:
		print(f"dimension: {dimension_}, inversion: {inversion_}, blank position: {blank_position_}")
		print("puzzle is not solvable")
		print("**************************************************")



puzzle1 = [[7, 1, 2], [5, ' ', 4], [8, 3, 6]]
puzzle2 = [[6, 1, 10, 2], [7, 11, 4, 14], [5, ' ', 9, 15], [8, 12, 13, 3]]
puzzle3 = [[6, 1, 10, 2], [7, 11, 4, 14], [5, ' ', 9, 15],[8, 12, 13, 3]]
puzzle4 = [[13, 10, 11, 6], [5, 7, 4, 8], [1, 12, 14, 9], [3, 15, 2, ' ']]

solvable(puzzle1)
solvable(puzzle2)
solvable(puzzle3)
solvable(puzzle4)