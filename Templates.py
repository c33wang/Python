from string import Template

class MyTemplate(Template):
    delimiter = "#"

def Main():
    cart = []
    cart.append(dict(item="Cake", price=2, qty=4))
    cart.append(dict(item="Coke", price=3, qty=3))
    cart.append(dict(item="Moke", price=4, qty=1))

    t = MyTemplate("#qty x #item = #price")
    total = 0
    print "Cart: "
    for data in cart:
        print t.substitute(data)
        total += data["price"]
    print "Total: " + str(total)

if __name__ == "__main__":
    Main()
