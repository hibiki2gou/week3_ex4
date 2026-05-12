import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import japanize_matplotlib

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

def prepare_dataset(n=20, seed=0):   # 演習1.2で作成するデータセットを準備する関数。デフォルトで
    np.random.seed(seed)
    x = np.random.uniform(-1, 1, n) # -1≦n≦1の範囲でランダムなn個の観測点xを生成
    y = true_function(x)
    noize = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=n) / 2.0  # 演習1.3でnoizeを作成
    df = pd.DataFrame({
        "観測点": x,
        "真値": y, 
        "観測値": y + noize # 真値にnoizeを付与したものを観測点とした
    })
    
    return df

def export_dataset(df, filename="dataset1.tsv"):    # 1.4でTSV形式で出力するために追加
    df.to_csv(filename, sep='\t', index=False)
    
def load_dataset(filename="dataset1.tsv"):  # 1.5でtsvファイルをDataFrameとして読み込む
    df = pd.read_csv(filename, sep='\t')
    return df

if __name__ == "__main__":
    x = np.linspace(-1, 1, 100)
    y = true_function(x)
    
    df_dataset = prepare_dataset()
    
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
    export_dataset(df_dataset)  # 1.4 tsvファイル出力
    df_loaded = load_dataset("dataset1.tsv") # 1.5 保存したファイルを読み込んで、df_loadedに格納する
    print(df_loaded.head()) # 先頭5行を出力して、正しく読み込むことができているかをテストする