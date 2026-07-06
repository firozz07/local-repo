import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy.stats import pearsonr
x=np.linspace(1,100,100)
y_linear=2*x+np.random.normal(0,10,100)
y_nonlinear=2**x+np.random.normal(0,1000,100)
y_random=np.random.rand(100)*100

def analyze_correlation(x,y,title):
    r,p=pearsonr(x,y)
    print(f"{title}")
    print(f"correlation coefficient(r):{r:.4f}")
    print(f"P-value:{p:.4f}")
    plt.figure(figsize=(5,4))
    sns.scatterplot(x=x,y=y)
    plt.title(f"{title}\nr={r:.2f}")
    plt.show()


analyze_correlation(x,y_linear,"linear relationship")
analyze_correlation(x,y_nonlinear,"nonlinear relationship")
analyze_correlation(x,y_random,"no relationship")