import sys
import traceback as tb
try:
    dividend = int(input("Enter a dividend: "))

    divisor = int(input("Enter divisor: "))

    result = dividend/divisor

    print(result)

except ZeroDivisionError as e:
    
    print(e) #pirnts the cause of exception
    e_type, e_cause,e_trace, = sys.exc_info()
    print(f'{e_trace}, {e_cause}') #prints class and cause of the error


except ValueError as e:
    print(e)
    print(tb.print_exc()) #prints the stack trace
    tb.print_exception(e) #print stacktrace
else:
    print("try is successful")
finally:
    print('Always executes')