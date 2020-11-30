class minetrack:
    def __init__(self, dir):
        self.dir = dir
        self.cart = None

    def addCart(self, minecart):
        self.cart = minecart

    def removeCart(self):
        self.cart = None

class minecart:
    def __init__(self, state):
        self.state = state
        self.t = 'L'

    def turn(self):
        dir = self.t
        if dir == 'L':
            self.t = 'C'
        elif dir == 'C':
            self.t = 'R'
        else:
            self.t = 'L'
        return dir

def getTurnDir(dir, turn):
    if turn == 'L':
        if dir == '<':
            return 'v'
        elif dir == 'v':
            return '>'
        elif dir == '>':
            return '^'
        else:
            return '<'
    elif turn == 'R':
        if dir == '<':
            return '^'
        elif dir == '^':
            return '>'
        elif dir == '>':
            return 'v'
        else:
            return '<'
    else:
        return dir

def moveCart(rails, nbrCarts, crashes, newCarts, x, y):
    key = str(x) + ',' + str(y)
    c_track = rails.get(key)
    cart = c_track.cart
    nextKey = ''
    if cart.state == '<':
        nextKey = str(x)+','+str(y - 1)
    elif cart.state == '>':
        nextKey = str(x) + ',' + str(y + 1)
    elif cart.state == '^':
        nextKey = str(x - 1) + ',' + str(y)
    elif cart.state == 'v':
        nextKey = str(x + 1) + ',' + str(y)
    n_track = rails.get(nextKey)
    if n_track.cart is not None:
        print("Crash at y,x = " + nextKey)
        n_track.removeCart()
        c_track.removeCart()
        idx = -1
        n = nextKey.split(',')
        t = (int(n[0]), int(n[1]))
        crashes.append(t)
        for i in range(len(newCarts)):
            if newCarts[i] == t:
                idx = i
                break
        if idx != -1:
            newCarts.pop(idx)
        nbrCarts -= 2
        print("Number of carts left: " + str(nbrCarts))
        return nbrCarts

    else:
        if cart.state == '<':
            if n_track.dir == '\\':
                cart.state = '^'
            elif n_track.dir == '/':
                cart.state = 'v'
            elif n_track.dir == '+':
                t = cart.turn()
                cart.state = getTurnDir(cart.state, t)
        elif cart.state == '^':
            if n_track.dir == '\\':
                cart.state = '<'
            elif n_track.dir == '/':
                cart.state = '>'
            elif n_track.dir == '+':
                t = cart.turn()
                cart.state = getTurnDir(cart.state, t)
        elif cart.state == '>':
            if n_track.dir == '\\':
                cart.state = 'v'
            elif n_track.dir == '/':
                cart.state = '^'
            elif n_track.dir == '+':
                t = cart.turn()
                cart.state = getTurnDir(cart.state, t)

        else:
            if n_track.dir == '\\':
                cart.state = '>'
            elif n_track.dir == '/':
                cart.state = '<'
            elif n_track.dir == '+':
                t = cart.turn()
                cart.state = getTurnDir(cart.state, t)

        c_track.removeCart()
        n_track.addCart(cart)
        n = nextKey.split(',')
        newCarts.append((int(n[0]),int(n[1])))
        return nbrCarts


lines = list()
with open('day13.txt', 'r') as f:
    lines = f.readlines()
    f.close()

rails = dict()
carts = list()
y_max = 0
x_max = 0
nbrCarts = 0
for x in range(len(lines)):
    if x > x_max:
        x_max = x
    line = lines[x].replace('\n', '')
    for y in range(len(line)):
        if y > y_max:
            y_max = y
        if line[y] != ' ':
            key = str(x) + ',' + str(y)
            cart = None
            track = None
            if line[y] == '<' or line[y] == '>' or line[y] == '^' or line[y] == 'v':
                cart = minecart(line[y])
                nbrCarts += 1
                if line[y] == '<' or line[y] == '>':
                    track = minetrack('-')
                else:
                    track = minetrack('|')
                track.addCart(cart)
                c = (x, y)
                carts.append(c)
            else:
                track = minetrack(line[y])
            rails[key] = track

crash = False
crash_x = 0
crash_y = 0
carts.sort()
while not crash:
    newCarts = list()
    crashes = list()
    for cart in sorted(carts, key=lambda cart: (cart[0], cart[1])):
        if cart not in crashes:
            x = cart[0]
            y = cart[1]
            track = rails.get(key)
            nbrCarts = moveCart(rails, nbrCarts, crashes, newCarts, x, y)
            if nbrCarts <= 1:
                crash = True
    carts = newCarts



print(newCarts)

