import pandas as pd

empty_series=pd.Series()
print(empty_series)

series1=pd.Series([1,2,3,4])
series2=pd.Series([5,6,7,8])

addition_result=series1+series2
print("Addition result: ")
print(addition_result)

subtraction_result=series1-series2
print("Subtraction result: ")
print(subtraction_result)

multiplication_result=series1*series2
print("Multiplication result: ")
print(multiplication_result)

division_result=series1/series2
print("Division result: ")
print(division_result)

exponent_result=series1**series2
print("Exponent result: ")
print(exponent_result)

floor_division_result=series1//series2
print("Division result: ")
print(floor_division_result)

series3=pd.Series([2,4,6,8,10])
series4=pd.Series([1,3,5,7,10])

comparision_result=series3==series4
print("Comparision Result: ")
print(comparision_result)