def x_dot_y(X,Y):
    dot_result = 0
    for index_i,i in enumerate(X):
        for index_j,j in enumerate(Y):
            if index_i==index_j:
                dot_result+= i*j
            else :
                continue
    return dot_result

def norm(num):
    norm_total=0
    for k in num:
        k_squared = k**2
        norm_total+=k_squared
    return norm_total**(1/2)

def cosine_similarity(X,Y):
    cos_result=(x_dot_y(X,Y)/(norm(X)*norm(Y)))
    return cos_result

X=[1,2,3]
Y=[1,3,5]
print(x_dot_y(X,Y))
print(norm(X))
print(norm(Y))
print(cosine_similarity(X,Y))
