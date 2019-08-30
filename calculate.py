a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

exec(open("math_lib.py").read());

div_answer = div(a,b)
add_answer = add(a,b)

print("a/b = ", div_answer)
print("a+b = ", add_answer)

