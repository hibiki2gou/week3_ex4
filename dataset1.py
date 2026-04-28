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
    
    df = pd.DataFrame({
        "観測点": x,
        "真値": y
    })
    
    return df
    
if __name__ == "__main__":
    x = np.linspace(-1, 1, 100)
    y = true_function(x)
    
    df_dataset = prepare_dataset()  # 演習1.2範囲内でシート値(デフォルト値0)を指定した上で、ランダムにn個(デフォルト値20)の観測点を用意した。
    
    plt.figure(figsize=(8,5))
    # plt.plot(x, y, label = "真の関数: y = sin(π * x * 0.8) * 10", color="blue") # 演習1.1のplotを一時的にコメントアウトする。
    plt.scatter(df_dataset["観測点"], df_dataset["真値"], label="サンプル（真値）", color="orange", s=20)
    
    plt.title("演習1.2：観測点と真値")
    plt.xlabel("入力 (x)")
    plt.ylabel("出力 (y)")
    plt.grid(True)
    plt.legend()
    
    plt.savefig("graph/ex1.2.png")