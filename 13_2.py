import math
def load_data() -> list:
    with open("data/data_13.txt") as data_file:
        data_string = data_file.read()
    data_array = data_string.split("\n")

    bus_data = []

    busses = data_array[1].split(",")

    for t, bus in enumerate(busses):
        if bus != "x":
            bus_data.append({"bus": int(bus), "t": int(t)})

    print(bus_data)
    return bus_data

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return  x, y

def remainder_find(a,b, p, q):
    print(f"a: {a}, b:{b}  p: {p} q:{q},")
    pq = q*p

    p1, q1 = egcd(p,q)
    #print(f"array p1: {p1}")
    #print(f"array q1: {q1}")
    y = (a*q*q1 + b*p*p1) % pq
    print(f"y = {a}*{q}*{q1} + {b}*{p}*{p1}")
    print(f"y: {y} PQ: {pq}")

    return  {"bus": pq, "t": y}

def calculate_answer(busses):
    bus_a = busses[0]
    iterbusses = iter(busses)
    next(iterbusses)
    for bus_b in iterbusses:
        bus_a = remainder_find(bus_a['t'], bus_b['t'], bus_a['bus'], bus_b['bus'])
        print(bus_a)
    print("----")
    print(bus_a)
    return (bus_a['bus'] - bus_a['t']) 

busses = load_data()

answer = calculate_answer(busses)


print(f"THIS IS THE AMAZING ANSWER: {answer}")