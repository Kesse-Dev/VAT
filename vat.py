x = True

while x == True:
    answer = input("Does the item has VAT with invoices? y/n: ")
    if answer == "y":
        
        basePrice = float(input("What is the price of the product on the listing? "))
        exvatPrice = basePrice/1.2
        exvatProfit = float(input("How much profit do you want to make? "))
        vatProfit = exvatProfit*1.2
        vatsalePrice = basePrice+vatProfit
        
        print("---------------------------------------")
        print("Cost price ex-vat: {:.2f}".format(exvatPrice))
        print("Sale price for profit: {:.2f}".format(vatsalePrice))
        print("Profit made: {:.2f}".format(exvatProfit))
        print("---------------------------------------")
        
        answer2 = input("Would you like to price up another item? y/n: ")
        if answer2 == "y":
            print("---------------------------------------")
        elif answer2 != "y":
            print("Ending program... ")
            x = False
            
    elif answer == "n":
        
        print("Then it must be VMS... ")
        basePrice = float(input("What is the price of the product on the listing? "))
        vmsprofitStart = float(input("How much profit do you want to make? "))
        vmsprofitAdd = vmsprofitStart*0.166
        vmsprofitFinal = vmsprofitAdd+vmsprofitStart
        vmssalePrice = vmsprofitFinal+basePrice

        print("---------------------------------------")
        print("Cost price ex-vat: {:.2f}".format(basePrice))
        print("Sale price for profit: {:.2f}".format(vmssalePrice))
        print("Profit made: {:.2f}".format(vmsprofitStart))
        print("---------------------------------------")
        print(vmssalePrice)
        
        answer2 = input("Would you like to price up another item? y/n: ")
        if answer2 == "y":
            print("---------------------------------------")
        elif answer2 != "y":
            print("Ending program... ")
            x = False
    else:
        print("Answer not recognised. Try again... ")
        
        
