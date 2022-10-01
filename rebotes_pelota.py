#INPUT
h=int(input("\nDigite la altura a la que cae la pelota: "))

#PROCESSING
b=h/5
rebote=0
while h>b:
    h=h*0.9
    rebote = rebote + 1

#OUTPUT
print("\nLa pelota no alcanzara la quinta parte de su altura inicial en el rebote numero " + str(rebote))