import numpy as np
import matplotlib.pyplot as plt 
import japanize_matplotlib

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

if __name__ == "__main__":
    x = np.linspace(-1, 1, 100)
    y = true_function(x)
    
    plt.figure(figsize=(8,5))
    plt.plot(x, y, label = "真の関数: y = sin(π * x * 0.8) * 10", color="blue")
    
    plt.title("演習1.1：真の関数")
    plt.xlabel("入力 (x)")
    plt.ylabel("出力 (y)")
    plt.grid(True)
    plt.legend()
    
    plt.savefig("graph/ex1.1.png")