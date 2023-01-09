
def contentprint(total):
    print('Number of products in the database = '+str(total))
    
    print("1. Add product to the database")
    print("2. List products")
    print("3. Remove product from the database")
    print("4. see options & total again")
    print("5. Exit program")
   
productdb={}
print("Product Database Program")
print("------------------------")
print("")
print("Main Menu")
print("---------")
print("")
contentprint(len(productdb))
while True:
    mc = input('Enter menu option> ')
    if mc == '1':
        name = input('Enter product name> ')
        serialnum = input('Enter serial number> ')
        quantity = input('Enter quantity in stock> ')
        productdb.update({name:{'serial':serialnum,'quantity':quantity}})
        print('product added to database')
    
    elif mc == '2':
        products='product\tserial\tquantity\n-------------------------\n\n'
        index=1
        for i in productdb:
            products = products+str(index)+'. '+i+'\t'+productdb[i]['serial']+'\t'+productdb[i]['quantity']+'\n'
            index=index+1
        print(products)
    elif mc == '3':
        todelete=input('input name, or serial of product> ')
        for i in productdb:
            if i == todelete:
                productdb.pop(i)
                print('producted deleted')
                break
            elif productdb[i]['serial'] == todelete:
                productdb.pop(i)
                print('product deleted')
                break
            else:
                print('product not found')
    elif mc =='4':
        contentprint(len(productdb))
    elif mc == '5':
        exit()
    else:
        print('command not found')
