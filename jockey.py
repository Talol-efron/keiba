import pandas as pd
import time
"""
nums = 5
for num in range(nums):
    url = "https://db.netkeiba.com/race/20200101010" + str(num + 1)
    dfs = pd.read_html(url)
    df = dfs[0]

    #これだとdataがcsvに上書きされるのみ
    df["騎手"].to_csv('/Users/taro/beginner_python/keiba/hoge.csv', index=False)
    time.sleep(1)
    #print(df["騎手"])
"""
url1 = "https://db.netkeiba.com/race/202001010101"
dfs1 = pd.read_html(url1)
df1 = dfs1[0]
#df1["騎手"].to_csv('/Users/taro/beginner_python/keiba/hoge.csv', index=False)
time.sleep(1)
url2 = "https://db.netkeiba.com/race/202001010102"
dfs2 = pd.read_html(url2)
df2 = dfs2[0]
#df2["騎手"].to_csv('/Users/taro/beginner_python/keiba/hoge.csv', index=False)
df_all = pd.concat([df1,df2],axis=1)
df_all["騎手"].to_csv('/Users/taro/Practice/python/keiba/jockey.csv', index=False)

