from matplotlib import pyplot as plt


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# 막대 너비의 기본값은 0.8이므로, 막대가 가운데로 오도록 좌표에 0.1 더해주기
xs = [i for i, _ in enumerate(movies)]

# 왼편으로부터 x축의 위치가 xs이고 높이가 num_oscars인 막대
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# 막대의 가운데에 오도록 영화 제목 레이블을 달자
plt.xticks([i for i, _ in enumerate(movies)], movies)


if __name__ == '__main__':
    plt.show()
