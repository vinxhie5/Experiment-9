import pandas as pd

table = {'Box':['Box 1', 'Box 1', 'Box 1', 'Box 2', 'Box 2', 'Box 2'], 
          'Dimension':['Length', 'Width', 'Height', 'Length', 'Width', 'Height'], 
          'Value': [6,4,2,5,3,4]}

messy = pd.DataFrame(table, columns=['Box', 'Dimension', 'Value'])

tidy_data = messy.pivot_table(index=['Box'], columns = 'Dimension', values = 'Value')

vol = tidy_data.assign(Volume=lambda tidy_data: tidy_data.Length*tidy_data.Height*tidy_data.Width)
print (vol)
