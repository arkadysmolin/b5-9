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
		self.mode="constructor"
		self.num_runs=num_runs # В режиме конструктора берём аргумент num_runs

	def __call__(self, *args):
		if self.mode=="constructor": # если сейчас режим конструктора
			self.function=args[0] # в аргументе будет лежать функция
			self.mode="decor" # для следующего запуска будем работать как декоратор
			return self # возвращаем функции декоратора

		av_time_sum=0
		for _ in range(self.num_runs):
			t_begin = time.time()
			self.function(args[0])
			t_end = time.time()
			func_time = t_end-t_begin
			av_time_sum += func_time
		av_time = av_time_sum / self.num_runs
		print ("Декоратор как класс - время {} сек на {} прогонов".format(av_time,self.num_runs))
		return self

@Timer(10)
def z(x):
	for j in range(x):
		pass

z(10000000)





class Timer_with:
	def __init__(self, num_runs):
		self.num_runs=num_runs

	def __enter__(self):
		return self

	def __call__(self, function, *args):
		self.function = function # забираем функцию

		av_time_sum=0
		for _ in range(self.num_runs):
			t_begin = time.time()
			self.function(args[0]) # выполняем функцию с соответствующем аргументом
			t_end = time.time()
			func_time = t_end-t_begin
			av_time_sum += func_time
		av_time = av_time_sum / self.num_runs
		print ("Декоратор как контекстный менеджер - время {} сек на {} прогонов".format(av_time,self.num_runs))
		

	def __exit__(self, exc_type, exc_val, exc_tb):
		return self


def dad(ggg):
	for j in range(ggg):
		pass
	


repeat=10
ggg=10000000

with Timer_with(repeat) as tw: # передаем количество повторений
	asd=tw(dad,ggg) # передаем функцию и аргумент











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



