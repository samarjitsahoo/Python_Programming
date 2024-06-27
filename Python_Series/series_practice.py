import numpy as np
import pandas as pd

#Program 1
country = ['India', 'Pakistan', 'USA', 'Nepal', 'Sri Lanka']
series = pd.Series(country)
print(series)

#Program 2
runs=[13,24,56,78,100]
runs_ser=pd.Series(runs)
print(runs_ser)
print(runs_ser.index)

#Program 3
marks=[67,57,89,100]
subjects=['maths','english','science','hindi']
print(pd.Series(marks,index=subjects))
print(pd.Series(marks,index=subjects,name='Selmon ke Marks'))

#Program 4
marks={
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}
mark_series=pd.Series(marks,name='Selmon ke Marks')
print(mark_series)

print(mark_series.size)
print(mark_series.dtype)
print(mark_series.name)
print(mark_series.is_unique)
print(mark_series.index)
print(mark_series.values)
