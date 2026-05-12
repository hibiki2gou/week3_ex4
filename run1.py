import dataset1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import japanize_matplotlib

x = np.linspace(-1, 1, 100)
y = dataset1.true_function(x)

df_dataset = dataset1.prepare_dataset()

plt.figure(figsize=(8,5))

plt.plot(x, y, label = "真の関数: y = sin(π * x * 0.8) * 10", color="blue") # 1.1のプロット
plt.scatter(df_dataset["観測点"], df_dataset["真値"], label="サンプル（真値）", color="orange", s=20) # 1.2のプロット
plt.scatter(df_dataset["観測点"], df_dataset["観測値"], label="観測値（ノイズあり）", color="red", marker="x", s=30) # 1.3のプロット

plt.title("演習1.3：ノイズを付与した観測値")
plt.xlabel("入力 (x)")
plt.ylabel("出力 (y)")
plt.grid(True)
plt.legend()

plt.savefig("graph/ex1.3.png")
dataset1.export_dataset(df_dataset)  # 1.4 tsvファイル出力
df_loaded = dataset1.load_dataset("dataset1.tsv") # 1.5 保存したファイルを読み込んで、df_loadedに格納する
print(df_loaded.head()) # 先頭5行を出力して、正しく読み込むことができているかをテストする