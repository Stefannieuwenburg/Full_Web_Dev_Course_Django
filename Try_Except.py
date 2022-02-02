#⌨️ (2:45:35) Try Except In Python

try:
    input_nr = int(input('input a integer: '))
    print(input_nr)
except ValueError as ValueError:
  print('Invalid Input',ValueError) 
except Exception as ExceptionError: 
    print('something went wrong ... please try again',ExceptionError)
finally:
    print('The Programa finished')


'''
Try_except:

/ZeroDivisionError/ Exception/ ValueError /TypeError/ SyntaxError/ ZeroDivisionError /except (RuntimeError, TypeError, NameError):

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

'''

a = 5
b = 2
k = int(input ="5"('Enter a number')) 

try:
    print(a/b)
except ZeroDivisionError as ZeroDivisionError:
    print('hey , You cannot divide a number by zero', ZeroDivisionError) 
except ValueError as ValueError:
    print('Invalid Input !',ValueError) 
except Exception as ExceptionError:
    print('Something went wrong',ExceptionError)
finally:
    print('The Prog finished')
  
