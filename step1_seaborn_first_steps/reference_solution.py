import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    [
    ['Alice', 168, 65],
    ['Bob', 175, 72],
    ['Charlie', 180, 78],
    ['Diana', 165, 63],
    ['Eve', 158, 60],
    ['Frank', 182, 80],
    ['Grace', 170, 68],
    ['Hank', 177, 74],
    ['Ivy', 160, 62],
    ['Jack', 185, 83],
    ['Karen', 172, 69],
    ['Leo', 167, 64],
    ['Mona', 178, 76],
    ['Nina', 155, 58],
    ['Oscar', 185, 82],
    ['Paul', 162, 63],
    ['Quinn', 174, 71],
    ['Rita', 168, 66],
    ['Sam', 176, 75],
    ['Tina', 161, 61]],columns=['name','height','weight']
)

sns.set_theme()
fig, ax = plt.subplots(1,2,figsize=(10,5))

sns.histplot(df,x='height',ax=ax[0])
ax[0].set_title('Histogram')
ax[0].set_ylabel('Count')
ax[0].set_xlabel('Height')

sns.scatterplot(df,x='height',y='weight',ax=ax[1])
ax[1].set_title('Scatter plot')
ax[1].set_ylabel('Weight')
ax[1].set_xlabel('Height')

plt.tight_layout()

if __name__ == '__main__':
    plt.show()


