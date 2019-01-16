#Radioactive Decay
#Tyler Hegewald

decay = .12
cobalt = 10

for x in range(5):
    decayed = float(decay * cobalt)
    cobalt = float(cobalt - decayed)
print("The amount of cobalt-60 remaining after five years is",format("%.2f"%cobalt), "grams.")
