import os
os.system('python -m pip install xlrd==1.2.0')
try:
    import pandas
except:
    os.system('python -m pip install pandas')