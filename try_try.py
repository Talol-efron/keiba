import pandas as pd

url = "https://db.netkeiba.com/race/202001010103/"
dfs = pd.read_html(url)
#print(dfs)

df = dfs[0]

def put():
    df_name1 = df["騎手"]
    print(df_name1[:3])
    df_name2 = df["馬名"]
    print(df_name2[:3])
    

#put()

#hoge.csv
df["騎手"].to_csv('/Users/taro/beginner_python/data_ex/hoge.csv', index=False)

