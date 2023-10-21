import numpy as np

def arraydefiner():
	x = np.linspace(0,2*np.pi,1000)
	y = np.sin(x)
	table = np.array([x,y],float)
	return table

def arrayprinter(table):
	print('',end='\t')
	for x in table[0]:
		print(x,end=', ')
	print()
	for j in table[1]:
		print(j,end='\t')
		for i in table[0]:
			print(j*i,end=', ')
		print()


def main():
	table = arraydefiner()
	arrayprinter(table)

if __name__=='__main__':
	main()
