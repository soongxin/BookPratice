"""
TidBid计算机商店有一个针对计算机销售的信用卡计划。
这包括一个10%的分期付款和一个年息12%的利息。每个月
的付款是销售定价的5%再减去分期付款，编写一个程序，
它接受销售价格作为输入。程序应该显示一个表格，它拥有
相应的表头，包括借贷的整个还款周期的支付计划，表的
每一行应该包含如下的项：
* 第几个月（从1开始）;
* 当前的欠款总额；
* 该月所欠利息；
* 该月所欠本金；
* 该月还款额；
* 在还款之后的所欠款总额。
一个月的利息等于余额*利率/12，一个月的本金额等于该月的
还款减去所欠的利息
"""
title = [
	'当前欠款总额',
	'该月所欠利息',
	'该月所欠本经',
	'该月所欠本金',
	'该月还款额',
	'还款后欠款总额'
	]


TAB_WIDTH = 20
def format_table(data):
	data = [item for item in map(to_mix_str, data)]
	print(type(data[0]))
	for i in range(10):
		for i in range(len(data)):
			print('+'+('-'*(TAB_WIDTH-1)), end='')
			if i == len(data) - 1:
				print('+')
		for i in range(len(data)):
			print('|'+ data[i].just((TAB_WIDTH-1), ' '), end='')
			if i==len(data) - 1:
				print('|')
	for i in range(len(data)):
		print('+'+('-'*(TAB_WIDTH-1)), end='')
		if i==len(data) - 1:
			print('+')


class MixStr(object):
	'''方便打印输出的字符串类，将中文解析为两个字符串长度'''
	def __init__(self, string):
		self.value = string

	@staticmethod
	def is_chinese(c):
		return True if '\u4e00' < c < '\u9fff' else False

	def __len__(self):
		length = 0
		for i in self.value:
			if self.is_chinese(i):
				length += 2
			else:
				length += 1
		return length

	def just(length, char=' '):
		if length < self.__len__():
			return self.value
		else:
			remain_left = (length - self.__len__()) // 2
			return (' '*remain_left
					+ self.value
					+ ' ' * (length-self.__len__()-remain_left))


def to_mix_str(data):
	return MixStr(data)

def is_chinese(c):
	return True if '\u4e00' < c < '\u9fff' else False

if __name__ == '__main__':
	format_table(title)
