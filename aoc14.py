from functools import reduce

harddisk = []

for j in range(128):
	lengths_string = "flqrgnkx-" + str(j)
	lengths = []
	stuff = list(range(256))

	current_position = 0
	skip_size = 0

	for c in lengths_string:
		lengths.append(ord(c))
	lengths += [17, 31, 73, 47, 23]

	for _ in range(64):
		for length in lengths:
			temp = list(stuff)
			for i in range(length):
				stuff[(current_position + i) % len(stuff)] = temp[(current_position + (length - 1 - i)) % len(stuff)]

			current_position = (current_position + length + skip_size) % len(stuff)
			skip_size += 1

	stuff_reduced = []
	for i in range(16):
		chunk = list(stuff[i*16:(i+1)*16])
		stuff_reduced.append(reduce(lambda x,y:x^y, chunk))

	harddisk.append(stuff_reduced)

harddisk_binary = []
for record in harddisk:
	harddisk_binary.append(list(reduce(lambda x,y: x + y, list(map(lambda x: "{:08b}".format(x), record)))))

harddisk_binary_hash = []
for record in harddisk_binary:
	harddisk_binary_hash.append(list(map(lambda x: '#' if x == '1' else '0', record)))

# harddisk_binary_hash = [
# 	['#', '#', '0', '#', '0', '#', '0', '0'],
# 	['0', '#', '0', '#', '0', '#', '0', '#'],
# 	['0', '0', '0', '0', '#', '0', '#', '0'],
# 	['#', '0', '#', '0', '#', '#', '0', '#'],
# 	['0', '#', '#', '0', '#', '0', '0', '0'],
# 	['#', '#', '0', '0', '#', '0', '0', '#'],
# 	['0', '#', '0', '0', '0', '#', '0', '0'],
# 	['#', '#', '0', '#', '0', '#', '#', '0']
# ]


def mark_adjacent(x, y):
	adjacent = [
		[x + 1, y],
		[x - 1, y],
		[x, y + 1],
		[x, y - 1]
	]
	for cell in adjacent:
		try:
			if harddisk_binary_hash[cell[0]][cell[1]] == '#':
				harddisk_binary_hash[cell[0]][cell[1]] = harddisk_binary_hash[x][y]
				mark_adjacent(cell[0], cell[1])
		except:
			pass


def check():
	for x, i in enumerate(harddisk_binary_hash):
		for y, j in enumerate(i):
			if j == '#':
				return x, y
	return -1, -1

x, y = check()
current = '1'
while x != -1 and y != -1:
	harddisk_binary_hash[x][y] = current
	mark_adjacent(x, y)
	current = str(int(current) + 1)
	x, y = check()

for line in harddisk_binary_hash:
	for c in line[:16]:
		print(c + " ", end='')
	print()


