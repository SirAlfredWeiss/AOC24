text = open('C:\\Users\\Julian\\Desktop\\AOC24\\04\\input.txt').read()
dat = [list(line) for line in text.split('\n')]
SIZE = len(dat)

def unroll(board):
	rows = ["".join(row) for row in board]
	cols = ["".join(col) for col in zip(*board)]
	diags = ["".join(board[j][j-i] for j in range(max(0,i), SIZE+min(0, i))) for i in range(-SIZE+1,SIZE)]
	rev_diags = ["".join(board[SIZE-j-1][j-i] for j in range(max(0,i), SIZE+min(0, i))) for i in range(-SIZE+1,SIZE)]
	return "-".join(rows + cols + diags + rev_diags)

print(unroll(dat).count("XMAS") + unroll(dat).count("SAMX"))

n = 0
for y in range(1,SIZE-1):
	for x in range(1,SIZE-1):
		if dat[y][x] != "A":
			continue
		if {dat[y-1][x-1], dat[y+1][x+1]} != {"M", "S"}:
			continue
		if {dat[y-1][x+1], dat[y+1][x-1]} != {"M", "S"}:
			continue
		n += 1
print(n)