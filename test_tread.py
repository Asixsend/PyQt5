# тестировка многопоточности
from threading import Thread

def prescript(thefile, num):
    with open(thefile, 'w') as f:
        for i in range(num):
            if num > 10:
                f.write('Много букв\n')
            else:
                f.write('Мало букв\n')

thread1 = Thread(target = prescript, args=('test_tread_1.txt', 2,))
thread2 = Thread(target = prescript, args=('test_tread_2.txt', 12,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
