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

x = [('2020-02-23 05:26:52'), ('2020-02-24 05:26:52')]
y = [(77041,), (77041,)]
line(x, y)

