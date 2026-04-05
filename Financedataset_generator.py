import pandas as pd
import numpy as np

np.random.seed(99)
n = 1000

departments = ['Clinical Operations','Pharmacy','IT & Systems',
               'HR & Staffing','Facilities','Compliance & Legal',
               'Revenue Cycle','Patient Services']
categories  = ['Personnel','Equipment','Supplies','Contracts',
               'Technology','Training','Overhead']
quarters    = ['Q1-2023','Q2-2023','Q3-2023','Q4-2023',
               'Q1-2024','Q2-2024','Q3-2024','Q4-2024']
regions     = ['Northeast','Southeast','Midwest','West','Southwest']
managers    = ['Sarah Mitchell','James Patel','Linda Torres',
               'Kevin Brown','Amy Chen','Robert Davis']

df = pd.DataFrame({
    'Date':            pd.date_range('2023-01-01',periods=n,freq='D').to_series().sample(n,random_state=99).values,
    'Quarter':         np.random.choice(quarters,n),
    'Department':      np.random.choice(departments,n),
    'Category':        np.random.choice(categories,n),
    'Region':          np.random.choice(regions,n),
    'Manager':         np.random.choice(managers,n),
    'Budget_Amount':   np.random.randint(10000,200000,n),
    'Forecast_Amount': np.random.randint(10000,200000,n),
    'Revenue':         np.random.randint(50000,500000,n),
    'Headcount':       np.random.randint(5,150,n),
})

def actual_cost(row):
    if row['Department'] in ['Clinical Operations','Pharmacy']:
        return round(row['Budget_Amount']*np.random.uniform(1.15,1.35),2)
    elif row['Department'] in ['HR & Staffing','Facilities']:
        return round(row['Budget_Amount']*np.random.uniform(0.78,0.95),2)
    else:
        return round(row['Budget_Amount']*np.random.uniform(0.92,1.08),2)

df['Actual_Amount']   = df.apply(actual_cost,axis=1)
df['Budget_Variance'] = (df['Actual_Amount']-df['Budget_Amount']).round(2)
df['Variance_Pct']    = ((df['Budget_Variance']/df['Budget_Amount'])*100).round(1)
df['Profit_Loss']     = (df['Revenue']-df['Actual_Amount']).round(2)
df['Margin_Pct']      = ((df['Profit_Loss']/df['Revenue'])*100).round(1)
df['Over_Budget']     = df['Budget_Variance'].apply(lambda x:'Yes' if x>0 else 'No')
df['Date']            = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
df                    = df.sort_values('Date').reset_index(drop=True)
df.to_csv('healthcare_finance_dataset.csv',index=False)
print("Done!")