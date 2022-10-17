import pandas as pd

original = pd.read_csv('./outbreaks.csv', sep=',')
cases = pd.read_csv('./cases.csv', sep=',')
print(len(original))
print(len(original[original.index.isin(list(cases['case_id']))]))
# new_df = original[not original.index.isin(list(cases['case_id']))]
# new_df.to_csv('outbreaks_v2.csv', index=False)
x = list(map(lambda x: x - 1, list(cases['case_id'])))
new_df = original[original.index.isin(x)]
print(cases['case_id'])
new_df.to_csv('test.csv', index=False)
