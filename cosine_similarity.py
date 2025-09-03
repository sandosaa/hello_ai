def x_dot_y(X,Y):
    dot_result = 0
    dot_list=[X[i]*Y[i] for i in range(len(Y))]
    for i in dot_list:
        dot_result+=i
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
