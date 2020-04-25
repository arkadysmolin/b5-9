import time

def time_this(num_runs):
	def decorator(func):
		def timer():
			av_time_sum=0
			for _ in range(num_runs):
				t_begin = time.time()
				func()
				t_end = time.time()
				func_time = t_end-t_begin
				av_time_sum += func_time
			av_time = av_time_sum / num_runs
			return "Просто декоратор - время {} сек на {} прогонов".format(av_time, num_runs)
		return timer
	return decorator


@time_this(10)
def s():
	for j in range(10000000):
		pass

print(s())





class Timer:
	def __init__(self, num_runs):
		self.num_runs=num_runs
		self.mode="num_runs_read" # для первого прогона берём аргумент num_runs

	def __call__(self, *args):
		if self.mode=="num_runs_read":
			self.function=args[0] # при втором прогоне в аргументе будет лежать функция
			self.mode="decor" # во втором прогоне работаем как декоратор
			return self

		av_time_sum=0
		for _ in range(self.num_runs):
			t_begin = time.time()
			self.function(args[0])
			t_end = time.time()
			func_time = t_end-t_begin
			av_time_sum += func_time
		av_time = av_time_sum / self.num_runs
		print ("Декоратор как класс - время {} сек на {} прогонов".format(av_time,self.num_runs))
		return self.function(*args)

@Timer(10)
def z(x):
	for j in range(x):
		pass

z(10000000)



















# @time_this(10)
# def asd():
# 	max_f=40000000000
# 	m2=0
# 	m1=1
# 	m=0
# 	f=[]
# 	fe=[]
# 	while m<max_f:
# 		m=m2+m1
# 		if m<max_f:
# 			f.append(m)
# 			if m % 2 ==0:
# 				fe.append(m)
# 			m2=m1
# 			m1=m
# 	# print (f[-1])
# 	asd=sum(fe)
# 	print(asd)

# print (asd())





