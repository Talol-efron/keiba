import pandas as pd

url = "https://db.netkeiba.com/race/202105010411"
#始め4桁:20xx年 今回は2020
#中2桁: 開催都市　01;札幌 02;函館 03;福島 04;新潟 05;東京 06;中山 07;中京 08;京都 09;阪神 10;小倉 
#中2桁: x回(1~5)
#中2桁: x日目(1~9)
#最後2桁: xR(ラウンド(1~12))

pul= pd.read_html(url)[0]
print(pul)
