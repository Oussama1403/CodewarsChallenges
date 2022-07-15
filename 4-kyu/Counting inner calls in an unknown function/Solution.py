import sys 

def count_calls(func, *args, **kwargs):
    count = 0
    def trace(frame,event,arg=None):
        nonlocal count
        # extracts calling function name
        func_name = frame.f_code.co_name
        if event == "call":
            count += 1  
    sys.settrace(trace)
    """Count calls in function func"""
    rv = func(*args, **kwargs)
    return count-1,rv

assert count_calls(add, 8, 12) == (0, 20)
assert count_calls(add_ten, 5) == (1, 15)
assert count_calls(misc_fun) == (5, 32)
