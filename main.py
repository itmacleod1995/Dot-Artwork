import colorgram

colors = colorgram.extract("image.png", 84)
print(colors[0].rgb)