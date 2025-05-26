temp=float(input("Enter the temperature in Celcius="))
if temp<0:
    print(temp,"WEATHER TYPE=Freezing \nTYPES OF CLOTHES TO WEAR= Thermal base layer with Heavy-duty winter coat \n                          Thick gloves, wool socks, beanie, scarf")
elif temp>=0 and temp<10:
    print(temp,"WEATHER TYPE=Cold Weather \nTYPES OF CLOTHES TO WEAR= Heavy sweaters, wool or fleece tops \n                          Insulated coat or puffer jacket \n                          Thermal underwear or base layers \n                          Beanie, scarf, gloves")
elif temp>=10 and temp<20:
    print(temp,"WEATHER TYPE=Cool weather \nTYPES OF CLOTHES TO WEAR= Sweaters, hoodies, thermal tops \n                          Medium-weight jackets \n                          Long pants, thicker leggings")
elif temp>=20 and temp<30:
    print(temp,"WEATHER TYPE=Mild Weather \nTYPES OF CLOTHES TO WEAR= Long-sleeve shirts, light sweaters \n                          Jeans, chinos, leggings \n                          Light jackets")
elif temp>=30 and temp<40:
    print(temp,"WEATHER TYPE=Warm Weather \nTYPES OF CLOTHES TO WEAR= Short-sleeve shirts, blouses \n                          Lightweight pants, jeans, capris, or skirts \n                          Dresses")
elif temp>=40:
    print(temp,"WEATHER TYPE=Hot Weather \nTYPES OF CLOTHES TO WEAR= Sleeveless tops, tank tops, t-shirts \n                          Shorts, skirts, sundresses \n                          Light colors to reflect sun")
