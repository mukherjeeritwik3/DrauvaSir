"""
Area of a circle can simply be evaluated using following formula.
Area = pi * radius**2
where r is radius of circle
"""
def areaCircle(r):
    area = 3.142*pow(r,2)
    return area
print(areaCircle(5))