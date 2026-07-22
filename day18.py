from matplotlib import pyplot as plt

days =[1,2,3,4,5,6,7,8,9,]

worker1 =[2,3,5,4,7,6,8,7,1]
worker2 =[3,2,5,1,6,8,7,9,2]
worker3 =[8,6,4,2,3,9,1,5,7]
worker4 =[4,8,1,6,2,4,8,3,9]

lables =['worker1','worker2','worker3','worker4']

colors=['red','pink','green','blue']

plt.stackplot(days,worker1,worker2,worker3,worker4,labels=lables,colors=colors)

plt.title("working hours of workers a Day")
plt.legend()
plt.show()