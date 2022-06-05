def product_number(tpl):
    a = 1
    for i in tpl:
        a = a*i

    return a

tpl =input ('Enter numbers split numbers with (,) for example 2.5,2,10.0 : ')
if tpl =='' or tpl ==None:
    answer = product_number(tpl)
    print(answer)
else:
    tpl = tuple(float(x) for x in tpl.split(","))
    answer = product_number(tpl)
    print(answer)