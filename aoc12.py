# stuff = """0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5""".split("\n")

stuff = ""
with open('aoc12.txt', 'r') as f:
	stuff = f.read()
	f.close()
stuff = stuff.split("\n")

connections = {}
seen = set()
current_groups = 0

for line in stuff:
	connections[line.split(" <-> ")[0]] = line.split(" <-> ")[1].split(", ")

def checkConnections(seen, connections, current):
	for i in connections[current]:
		if i not in seen:
			seen.add(i)
			checkConnections(seen, connections, i)

while connections.keys() - seen != set():
	current_groups += 1
	checkConnections(seen, connections, (connections.keys() - seen).pop())

print(current_groups)