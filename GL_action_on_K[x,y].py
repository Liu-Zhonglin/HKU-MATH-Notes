# GL_action_on_K[x,y]
MOD = 3

# Store a polynomial
poly = [
            [1,2,0,1],  #   x^3+  2*x+  1
            [1,0,2,1],  #   x^3+2*x^2+  1
            [2,2,0,1],  #   x^3+  2*x+  2
            [1,0,2,2],  # 2*x^3+2*x^2+  1
            [2,0,1,1],  #   x^3+  x^2+  2
            [1,1,0,2],  # 2*x^3+    x+  1
            [2,1,0,2],  # 2*x^3+    x+  2
            [2,0,1,2],  # 2*x^3+  x^2+  2
            [2,1,1,1],  #   x^3+  x^2+  x+2
            [1,1,1,2],  # 2*x^3+  x^2+  x+1
            [1,2,1,1],  #   x^3+  x^2+2*x+1
            [1,1,2,1],  #   x^3+2*x^2+  x+1
            [2,2,2,1],  #   x^3+2*x^2+2*x+2
            [1,2,2,2],  # 2*x^3+2*x^2+2*x+1
            [2,2,1,2],  # 2*x^3+  x^2+2*x+2
            [2,1,2,2]   # 2*x^3+2*x^2+  x+2
        ]

# Add two polynomials
def add_poly(f,g):
    h = eval(str(f))
    for i in range(0,len(g),1):
        if i>=len(f):
            h.append(g[i])
        else:
            h[i] = (h[i] + g[i]) % MOD
    while len(h)>0 and h[len(h)-1] == 0:
        del h[len(h)-1]
    return h

def mult_poly(f,g):
    h = []
    for i in range(0,len(g),1):
        k = [g[i]*f[j] for j in range(0,len(f),1)]
        h = add_poly(h,[0 for j in range(0,i,1)]+k)
    return h

a,b = 1,1
c,d = 1,2

#现在就是求和f[k]*[(a*x+c)**(k)][(b*x+d)**(m-k)]

def trans_poly(f):
    m = len(f) - 1
    h = []
    AC = [[1]]
    BD = [[1]]
    T = []
    for i in range(1,m+1,1):
        AC.append(mult_poly(AC[i-1],[c,a]))
        BD.append(mult_poly(BD[i-1],[d,b]))
    for i in range(0,m+1,1):
        T.append(mult_poly(AC[i],BD[m-i]))
    for i in range(0,m+1,1):
        k = [f[i]*T[i][j] for j in range(0,len(T[i]),1)]
        h = add_poly(h,k)
    return h
        

