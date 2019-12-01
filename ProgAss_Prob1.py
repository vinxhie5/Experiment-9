import pandas as pd

table1 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'Math':[80, 95, 79]}
t1 = pd.DataFrame(table1, columns=['Student', 'Math'])

table2 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'Electronics':[85, 81, 83]}
t2 = pd.DataFrame(table2, columns=['Student', 'Electronics'])

table3 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'GEAS':[90, 79, 93]}
t3 = pd.DataFrame(table3, columns=['Student', 'GEAS'])

table4 = {'Student':['Ice Bear', 'Panda', 'Grizzly'], 'ESAT':[93, 89, 88]}
t4 = pd.DataFrame(table4, columns=['Student', 'ESAT'])


s1 = pd.merge(t1, t2, how='outer', on = 'Student')

s2 = pd.merge(t3, t4, how='outer', on = 'Student')

scores = pd.merge(s1, s2, how='outer', on = 'Student')

tidy_scores = pd.melt(scores, id_vars = 'Student', value_vars = ['Math', 'Electronics', 
                                                                 'GEAS', 'ESAT'])

a = tidy_scores.rename (columns = {'variable':'Subject', 'value':'Grades'})

b = a.sort_values('Student')

c = b.reset_index()

long_format = c.drop(columns = 'index')

print (long_format)