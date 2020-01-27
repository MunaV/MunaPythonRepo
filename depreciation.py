## calculating depreciation in python
## A motorbike costs 2000 and loses 10% of its value every year.
## Print the bike's value every year until falls bellow 1000

year = 2020
bikeValue = 2000
depreciatedValuePercentage = 0.9

print('In year {}, the bike value is {}'.format(str(year), str(int(bikeValue))))


while bikeValue >= 1000 :

    bikeValue *= depreciatedValuePercentage
    year += 1

    print('In year {}, the bike value is {}'.format(str(year), str(int(bikeValue))))








