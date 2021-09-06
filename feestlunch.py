crossaints = 17
cossaintsPrijs = 0.39
stokbrood = 2
stokbroodWaarde = 2.78
kortingBonnen = 3
kortingWaarde = 0.50

koste = crossaints * cossaintsPrijs + stokbrood * stokbroodWaarde - kortingBonnen * kortingWaarde
print('De feestlunch kost je bij de bakker ' + str(koste) + ' euro voor de ' + str(crossaints) + ' croissantjes en de '+ str(stokbrood)+' stokbroden als de '+str(kortingBonnen)+' kortingsbonnen nog geldig zijn')