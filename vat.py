x = True

#creates loop
while x == True:
    answer = input("Does the item has VAT with invoices? y/n: ")
    if answer == "y":
        
        #asks user for input on listing price and profit then calculates VAT sale price
        basePrice = float(input("What is the price of the product on the listing? "))
        exvatPrice = basePrice/1.2
        exvatProfit = float(input("How much profit do you want to make? "))
        vatProfit = exvatProfit*1.2
        vatsalePrice = basePrice+vatProfit
        
        #prints different information based in the sale price
        print("---------------------------------------")
        print("Cost price ex-vat: {:.2f}".format(exvatPrice))
        print("Sale price for profit: {:.2f}".format(vatsalePrice))
        print("Profit made: {:.2f}".format(exvatProfit))
        print("---------------------------------------")
        
        #restarts the loop if needed again otherwise ends the loop
        answer2 = input("Would you like to price up another item? y/n: ")
        if answer2 == "y":
            print("---------------------------------------")
        elif answer2 != "y":
            print("Ending program... ")
            x = False
            
    #changes to VMS calculation
    elif answer == "n":
        
        #asks user for input on listing price and profit then calculates VMS sale price
        print("Then it must be VMS... ")
        basePrice = float(input("What is the price of the product on the listing? "))
        vmsprofitStart = float(input("How much profit do you want to make? "))
        vmsprofitAdd = vmsprofitStart*0.166
        vmsprofitFinal = vmsprofitAdd+vmsprofitStart
        vmssalePrice = vmsprofitFinal+basePrice

        #prints different information based in the sale price
        print("---------------------------------------")
        print("Cost price ex-vat: {:.2f}".format(basePrice))
        print("Sale price for profit: {:.2f}".format(vmssalePrice))
        print("Profit made: {:.2f}".format(vmsprofitStart))
        print("---------------------------------------")
        print(vmssalePrice)
        
        #restarts the loop if needed again otherwise ends the loop
        answer2 = input("Would you like to price up another item? y/n: ")
        if answer2 == "y":
            print("---------------------------------------")
        elif answer2 != "y":
            print("Ending program... ")
            x = False
    #catches any invalid input and restarts the loop
    else:
        print("Answer not recognised. Try again... ")
        
        
