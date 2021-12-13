# Nicholas Bennett
# ETGG 1803
# 2-21-19

from math import *

class Vector(object):
    """This is a general vector class"""

    def __init__(self, *args):      # References a variable length as long as you like and is optional to have or not.
        """  """
        self.mData = []
        for i in args:
            self.mData.append(float(i))
        self.mDim = len(args)
        if self.mDim == 2:
            self.__class__ = Vector2
        if self.mDim == 3:
            self.__class__ = Vector3

    def __getitem__(self, index):
        """  """
        return self.mData[index]

    def __len__(self):
        """ Can now get the length of the Vector easily """
        return self.mDim

    def __setitem__(self, index, new_val):
        """
        :param index: An integer
        :param new_val: A value that can be converted into a float
        :return: None
        """
        self.mData[index] = float(new_val)

    def __str__(self):
        """ v = Vector(1, 2, 3)    <Vector3:1,2,3>
        returns a string representation of our vector """
        s = "<Vector" + str(self.mDim) + ": "
        for i in range(self.mDim):
            s += str(self.mData[i])
            if i < self.mDim - 1:
                s += ", "
        s += ">"
        return s

    def copy(self):
        """ creates a deep copy of this vector
         returns the deep vector copy """
        v = Vector(*self.mData)
        v.__class__ = self.__class__
        return v

    def __eq__(self, other):
        """
        :param other: can be any value
        :return: boolean, true if other = our vector
        """
        if isinstance(other, Vector) and len(self) == len(other):
            for i in range(self.mDim):
                if self[i] != other[i]:
                    return False
            return True
        return False

    def __mul__(self, scalar):
        """ this gives the mult of the scalar on the right of the *
        :param scalar: number to multiply vector by, scalar must be on the right of * (int, float)
        :return: a copy of this vector with all value multiplied by scalar
        """
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            e = "Vector" + str(self.mDim)
            raise TypeError("You can only multiply this" + e + "and a scalar. You attempted to "
                                                                   "multiply by " + str(scalar) + ".")
        r = self.copy()
        for i in range(self.mDim):
            r[i] *= scalar
        return r

    def __rmul__(self, scalar):
        """ This gives the mult of the scalar on the left of *
        :param scalar: number to multiply vector by, scalar must be on the right of * (int, float)
        :return: a copy of this vector with all value multiplied by scalar
        """
        if not isinstance(scalar, int) and not isinstance(scalar, float):
            e = "Vector " + str(self.mDim)
            raise TypeError("You can only multiply this " + e + " and a scalar. You attempted to "
                                                               "multiply by " + str(scalar) + ".")
        r = self.copy()
        for i in range(self.mDim):
            r[i] *= scalar
        return r

    def __add__(self, other_vec):
        """ Adds other_vec to self as long as other_vec is a vector and same length to self
        :param other_vec: vector of equal length to self
        :return: vector with all added
        """
        if isinstance(other_vec, Vector) and isinstance(self, Vector) and self.mDim == len(other_vec):
            r = self.copy()
            for i in range(self.mDim):
                r[i] += other_vec[i]
            return r
        raise TypeError("You must add 2 vectors of equal length and other_vec must be a vector yout tried to add " +
                        str(other_vec) + " to " + str(self) + ".")

    def __sub__(self, other_vec):
        """
        able to use subtraction sign for subtracting vec
        :param other_vec: vector that should be same length as self
        :return: vector with every corresponding value added
        """
        if isinstance(other_vec, Vector) and self.mDim == len(other_vec):
            r = self.copy()
            for i in range(self.mDim):
                r[i] -= other_vec[i]
            return r
        raise TypeError("You must subtract 2 vectors of equal length and other_vec must be a vector")

    def __neg__(self):
        """flips every value in vector to negative
        returns: self. but with every value multiplied by 1 using the rmult method"""
        if not isinstance(self, Vector):
            raise TypeError(str(self) + " must be a Vector of any length.")

        return -1*self

    def __truediv__(self, scalar):
        """takes a scalar and divides a vector by that
        :param scalar: what to divide by
        :return: returns added vector
        """
        if not isinstance(scalar, int) or not isinstance(scalar, float):
            raise TypeError("The scalar" + str(scalar) + "must be an integer")
        r = self.copy()
        for i in range(len(r)):
            r[i] /= scalar
        return r

    @property
    def mag(self):
        """Returns the 2-norm of this Vector"""
        length = 0
        if isinstance(self, Vector):
            for i in range(self.mDim):
                length += self.mData[i] ** 2
            return length ** 0.5
        raise TypeError(str(self) + " must be a Vector.")

    @property
    def mag_squared(self):
        """Returns the square of the 2-norm without using the square roots"""
        length = 0
        if isinstance(self, Vector):
            for i in range(self.mDim):
                length += self.mData[i] ** 2
            return length
        raise TypeError(str(self) + " must be a Vector.")

    @property
    def normalize(self):
        if isinstance(self, Vector):
            denominator = 1/self.mag
            return self*denominator
        raise TypeError("Self must be a Vector object instead of " + str(self) + ".")

    @property
    def is_zero(self):
        """since this is a property we can call v.is_zero rather than v.is_zero()
        :return: True if self is the zero Vector, False otherwise
        """
        if not isinstance(self, Vector):
            raise TypeError("The self must be a Vector not" + str(self))
        for value in self:
            if value != 0.0:
                return False
        return True

    @property
    def i(self):
        """Returns a tuple of the coordinates of this Vector converted to integers"""
        if isinstance(self, Vector):
            list = []
            for i in range(self.mDim):
                list.append(int(self.mData[i]))
            return tuple(list)
        raise TypeError("The self must be a Vector not " + str(self) + ".")

class Vector2(Vector):
    """  """
    def __init__(self, x, y):
        super().__init__(x, y)      # this would look like self = Vector(x, y)

    @property           # able to do v.x to get the x value of the vector
    def x(self):
        """
        able to use decorator, property, to call x as an attribute not a function
        :return: x value of self
        """
        return self[0]

    @x.setter           # able to call v.x = _ so v.x is different depending on the context
    def x(self, newval):
        """ able to use decorator, x.setter, to call v.x and change that value
        :param newval: the new value for v.x
        :return: nothing
        """
        self[0] = float(newval)

    @property
    def y(self):
        """
        able to use decorator, property, to call y as an attribute not a function
        :return: y value of self
        """
        return self[1]

    @y.setter
    def y(self, newval):
        """ able to use decorator, y.setter, to call v.y and change that value
            :param newval: the new value for v.y
            :return: nothing
            """
        self[1] = float(newval)

    @property
    def degrees(self):
        """Returns the degree measure of this cartesian vector in polar space"""
        if isinstance(self, Vector):
            return degrees(atan2(self.y, self.x))
        raise TypeError("Self must be a Vector object instead of " + str(self) + ".")

    @property
    def degrees_inv(self):
        """Returns the y value to account for pygame's y axis"""
        if isinstance(self, Vector):
            return degrees(atan2(-self.y, self.x))
        raise TypeError("Self must be a Vector object instead of " + str(self) + ".")

    @property
    def radians(self):
        """Returns the radian measure of this cartesian vector in polar space"""
        if isinstance(self, Vector):
            return atan2(self.y, self.x)
        raise TypeError("Self must be a Vector object instead of " + str(self) + ".")

    @property
    def radians_inv(self):
        """Negate the y value to account for pygame's y axis"""
        if isinstance(self, Vector):
            return atan2(-self.y, self.x)
        raise TypeError("Self must be a Vector object instead of " + str(self) + ".")

    @property
    def perpendicular(self):
        """Returns a Vector2 perpendicular to this Vector"""
        if isinstance(self, Vector):
            return Vector(-self.y, self.x)
        raise TypeError("Self must be a Vector object instead of " + str(self) + ".")

class Vector3(Vector):
    """  """
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @property  # able to do v.x to get the x value of the vector
    def x(self):
        """
        able to use decorator, property, to call x as an attribute not a function
        :return: x value of self
        """
        return self[0]

    @x.setter  # able to call v.x = _ so v.x is different depending on the context
    def x(self, newval):
        """ able to use decorator, x.setter, to call x.y and change that value
            :param newval: the new value for v.x
            :return: nothing
            """
        self[0] = float(newval)

    @property
    def y(self):
        """
        able to use decorator, property, to call y as an attribute not a function
        :return: y value of self
        """
        return self[1]

    @y.setter
    def y(self, newval):
        """ able to use decorator, y.setter, to call v.y and change that value
            :param newval: the new value for v.y
            :return: nothing
            """
        self[1] = float(newval)

    @property
    def z(self):
        """
        able to use decorator, property, to call z as an attribute not a function
        :return: z value of self
        """
        return self[2]

    @z.setter
    def z(self, newval):
        """ able to use decorator, z.setter, to call v.z and change that value
            :param newval: the new value for v.z
            :return: nothing
            """
        self[2] = newval

def dot(v1, v2):
    """
    dot product of 2 vectors
    :param v1: vector 1
    :param v2: vector 2
    :return: the value of the dot product
    """
    if v1.mDim == v2.mDim and isinstance(v1, Vector) and isinstance(v2, Vector):
        product = 0
        for i in range(len(v1)):
            product += v1[i] * v2[i]
        return product
    raise TypeError("The dot product requires that both parameters be Vector objects of equal length you used " +
                    str(v1) + " as parameter 1 and " + str(v2) + " as parameter 2.")

def cross(v1, v2):
    """
    cross product of 2 3d vectors
    :param v1: vector, must be 3d
    :param v2: vector, must be 3d
    :return: the cross product of the two 3d vectors
    """
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        x = (v1.y*v2.z) - (v1.z*v2.y)
        y = -((v1.x*v2.z) - (v2.x*v1.z))
        z = (v1.x*v2.y) - (v2.x*v1.y)
        return Vector(x, y, z)
    raise TypeError("Both inputs must be Vector objects instead v1 is " + str(v1)
                    + " and v2 is " + str(v2) + ".")

def polar_to_Vector2(radius, theta, negate=False):
    """
    takes raidus and degree mesure to make a 2d vector
    :param radius: integer number for mag of 2d vector
    :param theta: the angle for the vec (or just the direction)
    :param negate: If true then y value is made negative to accomodate for y axis in pygame
    :return: 2d vector made form polar coordinates
    """
    if isinstance(radius, int) or isinstance(radius, float):
        theta = radians(theta)
        x = radius*cos(theta)
        if negate:
            y = -radius*sin(theta)
            return Vector(x, y)
        elif not negate:
            y = radius*sin(theta)
            return Vector(x, y)
    raise TypeError("The radius parameter must be an int or float not "
                    + str(radius) + ".")

def pnorm(vec, p = 2):
    """returns the p-norm(regular length) of vec"""
    if isinstance(vec, Vector):
        sqrLenght = 0
        for i in range(vec.mDim):
            sqrLenght += abs(vec[i]) ** p  # Adds up the **p of everything in vector v
        return sqrLenght ** (1 / p)
    raise TypeError("When using p-norm function the vec input must be a Vector object not "
                    + str(vec) + ".")

if __name__ == "__main__":
    v = Vector(1, 2, 3)
    w = Vector(4, 5, 6)
    r = Vector(1, 1)