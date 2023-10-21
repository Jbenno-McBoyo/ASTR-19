class Animal():
	def __init__(self,armlength,leglength,numeyes,hastail,isfurry):
		self.alen=armlength
		self.llen=leglength
		self.eyes=numeyes
		self.tail=hastail
		self.fur=isfurry

	def describeself(self):
		if self.tail:
			tstat='and has'
		else:
			tstat='but does not have'
		if self.fur:
			fstat=''
		else:
			fstat='not '
		print(f"My animal is {fstat}a furry animal. They have {self.alen} ft long arms, and {self.llen} ft long legs. They also have {self.eyes} big eyes {tstat} a tail!")

def main():
	homunculi=Animal(5.,6.,3,True,False)
	homunculi.describeself()

if __name__=='__main__':
	main()