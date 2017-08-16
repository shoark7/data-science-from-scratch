from matplotlib import pyplot as plt


mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

plt.ticklabel_format(useOffset=False)

plt.axis([2012.5, 2014.5, 0, 600])
plt.title("Look at teh 'Huge' Increase!")


if __name__ == '__main__':
    plt.show()
