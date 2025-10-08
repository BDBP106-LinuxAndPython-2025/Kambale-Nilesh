# #(3) Define a dictionary containing 10 fruits and their colours. Make sure that the colours
# are repeated as values. Write a loop to iterate over the key-value pairs, and check which
# all fruits are green in colour (this means that your dictionary should contain at least two
# fruits with green as its value (for this example to work well).
a={"mango":"yellow","pineapple":"yellow","Custard apple":"green","banana":"yellow","blueberry":"blue","Apple":"red","Grapes":"Purple","Litchi":"pink","Dragonfruit":"red","maulberry":"black","Orange":"orange",}
for key,value in a.items():
    if value == "green":
        print(key)
        