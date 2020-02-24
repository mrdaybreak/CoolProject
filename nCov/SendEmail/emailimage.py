import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


def line(x, y):
    a = x
    b = y
    plt.ylabel("累计确诊")
    plt.xlabel("日期")
    plt.plot(a, b)
    plt.savefig("ache.png")
    return "ache.png"



