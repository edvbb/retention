df = pd.DataFrame({'time1' : ['13.10.2015 17:50:14', '13.10.2015 17:50:14'], 'time2' : ['15.01.2009', ''] })
df['time2'] = pd.to_datetime(df.time2)
df['time1'] = pd.to_datetime(df.time1)

df['exp_months'] = df['time1'].values.astype('datetime64[M]').astype(int) - df['time2'].values.astype('datetime64[M]').astype(int)

df['exp_days'] = df['time1'].values.astype('datetime64[D]').astype(int) - df['time2'].values.astype('datetime64[D]').astype(int)
