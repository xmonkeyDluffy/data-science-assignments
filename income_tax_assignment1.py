annual_income=int(input())
hra=int(input())
od=int(input())
tax_amount=annual_income-(hra*12+od)
actual_tax=tax_amount-300000
if(actual_tax<300000):
    tax=actual_tax
    print(tax)
elif(actual_tax>300000 and actual_tax<600000):
    tax=actual_tax*0.10
    print(tax)
elif(actual_tax>600000 and actual_tax<1000000):
    tax=actual_tax*0.15
    print(tax)
else:
    tax=actual_tax*0.20
    print(tax)
