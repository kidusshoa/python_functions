import types

def is_user_defined_function(func):
    return isinstance(func, (types.FunctionType, types.LambdaType))

def custom_function():
    return "I am a user-defined function"

builtin_function = len  

lambda_function = lambda x: x * 2

print(f"Is 'custom_function' user-defined? {is_user_defined_function(custom_function)}")  
print(f"Is 'builtin_function' (len) user-defined? {is_user_defined_function(builtin_function)}")  
print(f"Is 'lambda_function' user-defined? {is_user_defined_function(lambda_function)}")  
