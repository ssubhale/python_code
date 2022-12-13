# Lambda function
'''
-It is known as nameless function or anonymous function, They are defined using lambda keyword, instead of def

#Syntax-
fun_object = lambda arguments : expression
function object is returned by lambda function

-This function have many number of arguments but can have only one expression which is evaluate and return
'''

# Normal functions / Named functions
def add(no1,no2):
    return no1 + no2

ans = add(10,12)
print("Addition using normal function : ",ans)

# Lambda functions / Unnamed function / Anonymous function
# lambda parameters : body

add = lambda A,B : A + B
print("Addition using lambda function : ",add(10,12))

## lets check the type of htis function
print(type(add))
