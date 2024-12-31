from random import randint
import threading
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            dep = randint(50, 500)
            with self.lock:
                self.balance += dep
                print(f'Пополнение: {dep}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            withdraw = randint(50, 500)
            print(f'Запрос на {withdraw}')
            self.lock.acquire()
            try:
                if withdraw <= self.balance:
                    self.balance -= withdraw
                    print(f'Снятие: {withdraw}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонен, недостаточно средств.')
            finally:
                self.lock.release()
            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

