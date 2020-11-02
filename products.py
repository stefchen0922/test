products = []
while True:
	p = []
	name = input("請輸入品項: ")
	if name == 'q':
		break
	price = input("請輸入價格: ")
	p.append(name)
	p.append(price)
	products.append(p)
print(products)	
