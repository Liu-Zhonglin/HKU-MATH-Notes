#Permutation_Calculator
#形如(1,2,4)(3,5)(7,8)的排列会被存储为
#[(7,8),(3,5),(1,2,4)]
def Permute(p,n):                            #用排列p去排列n
    if p==[]:
        return n
    else:
        temp                  =p[0]
        if n in temp:
            i                 =temp.index(n)
            if i==len(temp)-1:
                m             =temp[0]
            else:
                m             =temp[i+1]
        else:
            m                 =n
        return Permute(p[1:len(p):1],m)
def Permutation_to_LaTeX(p):
    s                         =""
    if len(p)==0:
        s                    +="e"
    else:
        i                     =len(p)-1
        while i>=0:
            s                +=str(p[i])
            i                -=1
    return s
def LaTeX_to_Permutation(s):
    p                         =[]
    if s!="e":
        lower_bound           =len(s)-2      #"("的位置
        upper_bound           =len(s)        #")"的位置+1
        while lower_bound>=0:
            while lower_bound>=0 and s[lower_bound]!="(":
                lower_bound  -=1
            p.append(eval(s[lower_bound:upper_bound:1]))
            upper_bound       =lower_bound
            lower_bound      -=2
    return p        
def Disjoint_Product_Simplification(s0):
    p0                        =LaTeX_to_Permutation(s0)
    Domain                    =set()
    i                         =0
    while i<len(p0):                         #把所有要排列的元素放进定义域
        Domain                =Domain|set(p0[i])
        i                    +=1
    Domain                    =list(Domain)  #给定义域排个序
    Domain.sort()
    Flag                      =[False for i in Domain]
    p1                        =[]
    i                         =0
    while i<len(Domain):
        if Flag[i]!=True:
            temp              =[Domain[i]]
            n                 =Permute(p0,Domain[i])
            while n!=Domain[i]:
                temp.append(n)
                j             =Domain.index(n)
                Flag[j]       =True
                n             =Permute(p0,n)
            if len(temp)>1:
                p1.append(tuple(temp))
        i                    +=1
    s1                        =Permutation_to_LaTeX(p1)
    return s1

