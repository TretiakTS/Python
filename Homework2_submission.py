from numpy import *
from matplotlib.pyplot import *

# Task 1
class Interval():                            # Defining the class and initial basic properties of an "Interval" object
    def __init__(self, min, max=None):       # 3 cases are necessary; only 1 number is given (Task 7) , min value is smaller than or equal to the max, or the values are switched, eg. [5, 2]
        if (max==None):
            self.min = min
            self.max = min
        elif (min<=max):
            self.min = min
            self.max = max
        else:
            self.min = max
            self.max = min
        
# Task 2 (and Task 8 incl. reverse operators)
    def __add__(self, other):                # Defining the adding and reverse adding method
        if isinstance(self, Interval) & isinstance(other, Interval):  # Checking if both addents are Intervals
            min1, max1 = self.min, self.max  # Defining the min and max values of the init. interval and the "other" interval
            min2, max2 = other.min, other.max
        elif (isinstance(other, int) or isinstance(other, float)) & isinstance(self,Interval):  # If the "other" addents is of int. or float type
            min1, max1 = self.min, self.max    
            min2, max2  = other, other
        else:
            raise TypeError('Wrong type!')   # Raising error if other addents are neither of Interval, int. nor float type
        return Interval(min1+min2, max1+max2)  # Returning interval type, which will be imortant later!
    def __radd__(self, other): 
        return self + other                  # Defining reverse adding as such because a + b = b + a
    
    def __sub__(self, other):                # Defining the subtraction methods in similar way to addition
        if isinstance(self,Interval) & isinstance(other, Interval):
            min1, max1 = self.min, self.max
            min2, max2 = other.min, other.max
        elif (isinstance(other, int) or isinstance(other, float)) & isinstance(self,Interval):
            min1, max1 = self.min, self.max
            min2, max2  = other, other
        else:
            raise TypeError('Wrong type!')
        return Interval(min1-max2, max1-min2)
    def __rsub__(self, other): 
        return -self + other                 # b - a = - a + b (the -Interval() method is defined below)
    
    def __mul__(self, other):                # Defining multiplication methods
        if isinstance(self,Interval) & isinstance(other, Interval):
            min1, max1 = self.min, self.max
            min2, max2 = other.min, other.max
        elif (isinstance(other, int) or isinstance(other, float)) & isinstance(self,Interval):
            min1, max1 = self.min, self.max
            min2, max2  = other, other
        else:
            raise TypeError('Wrong type!')
        return Interval(min(min1*min2, min1*max2, max1*min2, max1*max2), max(min1*min2, min1*max2, max1*min2, max1*max2))
    def __rmul__(self, other):
        return self * other                  # a * b = b * a
    
    def __truediv__(self, other):            # Defining division method (for Interval/Inteval only)
        if other.min == 0 or other.max == 0: # Task 6
            raise ZeroDivisionError("Both elements in denominating interval must be non-zero")
        return Interval(min(self.min/other.min, self.min/other.max, self.max/other.min, self.max/other.max), max(self.min/other.min, self.min/other.max, self.max/other.min, self.max/other.max))
    
    def __neg__(self):                       # Defining the negation method to be used when calling the reverse subtraction method above
        return Interval(-self.max , -self.min)
# Task 9    
    def __pow__(self, other):                # Defining the method for powers (that is, self**other, or self^other)
        if (other%2!=0):                     # Initial condition is whether the power is even or not.
            return Interval(self.min**other,self.max**other)
        else:                                # If even, then an additional 3 conditions are treated differently
            if (self.min>0):                 # If the lower bound of the interval is positive:
                return Interval(self.min**other,self.max**other)
            elif (self.max<0):               # If the upper bound is negative:
                return Interval(self.max**other,self.min**other)
            else:                            # If none of the above apply (that is, if the power is even, the lower bound is negative, and the upper bound is positive)
                return Interval(0,max(self.max**other,self.min**other))
# Task 3
    def __repr__(self,):
        return f"[{self.min} , {self.max}]"
# Task 5
    def __contains__(self, other):           # Defining method to determine if a given real number is in a given Interval
        return self.min<=other and other<=self.max  # Will return True/False

    def get_min(self):                       # Lastly defining 2 methods to help us fetch the min and max values sepparately later on
       return self.min
    def get_max(self):
        return self.max

# Task 4 - Giant test of above methods
print("Task 4:")
print(Interval(3,2))
print(Interval(1))
I1 = Interval(1, 4) # [1, 4]
I2 = Interval(-2, -1) # [-2, -1]
print(I1 + I2,"-------------") # [-1, 3]
print(I1 - I2) # [2, 6]
print(I1 * I2) # [-8, -1]
print(I1 / I2) # [-4.,-0.5]
print("Interval(2,3) + 1: ",Interval(2,3) + 1 )# [3, 4]
print("1 + Interval(2,3): ",1 + Interval(2,3)) # [3, 4]
print("1.0 + Interval(2,3): ",1.0 + Interval(2,3)) # [3.0, 4.0]
print("Interval(2,3) + 1.0: ",Interval(2,3) + 1.0 )# [3.0, 4.0]
print("1 - Interval(2,3): ", 1 - Interval(2,3)) # [-2, -1]
print("Interval(2,3) -1: ", Interval(2,3) -1) # [1, 2]
print("1.0 - Interval(2,3): ", 1.0 - Interval(2,3) )# [-2.0, -1.0]
print("Interval(2,3) - 1.0: ", Interval(2,3) - 1.0) # [1.0, 2.0]
print("Interval(2,3) * 1: ", Interval(2,3) * 1) # [2, 3]
print("1 * Interval(2,3): ", 1 * Interval(2,3)) # [2, 3]
print("1.0 * Interval(2,3): ", 1.0 * Interval(2,3)) # [2.0, 3.0]
print("Interval(2,3) * 1.0 : ", Interval(2,3) * 1.0 )# [2.0, 3.0]
print("-Interval(4,5)" ,-Interval(4,5)) # see the special method __neg__
x = Interval(-2,2) # [-2, 2]
print("(-2,2)**2: ", x**2) # [ 0, 4]
print("(-2,2)**3: ",x**3) # [-8, 8]
print ("-5 in (-2,2): ",-5 in x)
print ("0 in (-2,2): ",0 in x)

# Task 10
xl=linspace(0.,1,1000)
xu=linspace(0.,1,1000)+0.5
xall=zip(xl,xu)                            # Combining the upper and lower x-linspaces

xall2=[Interval(i[0],i[1]) for i in xall]  # Making list of Intervals with each element-pair of xall
def pol(x):                                # Defining polynomial function
    return 3*x**3-2*x**2-5*x-1
xres=[pol(i) for i in xall2]               # Making list of resulting Intervals from polynomial function
yl=[i.get_min() for i in xres]             # Splitting xres into upper and lower y-lists using the final methods defined above
yu=[i.get_max() for i in xres]

"""                                        Method w/out zip

xall = [Interval(xl[i], xu[i]) for i in range(len(xl))]
def pol(I):
    return 3*I**3 - 2*I**2 - 5*I - 1
xpol=[pol(i) for i in xall]
yl = [i.get_min() for i in xpol]
yu = [i.get_max() for i in xpol]
"""

# Creating plot
ylim([-10,4])
xlim([0,1.0])
title('p(I) = 3I³ - 2I² - 5I - 1, I = Interval(x, x+0,5)')
xlabel('x')
ylabel('p(I)')
plot(xl,yl)
plot(xl,yu)
show()
