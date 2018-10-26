def calc_pi(times):
	rate = -1
	result = 1
	for i in range(1, times + 1):
		result = result + rate / (2*i + 1)
		rate = -rate
	return result * 4


if __name__ == '__main__':
	times = int(input('请输入要迭代的次数：'))
	print(calc_pi(times))
