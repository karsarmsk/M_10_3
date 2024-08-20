import threading
import random
from time import sleep
class Bank:
    def __init__(self, balance=500): # начальный баланс 500
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            pop = random.randint(50, 500)
            self.lock.acquire()
            if (self.balance >= 500 and self.lock == self.lock.locked()):
                self.lock.release()
            self.balance += pop
            self.lock.release()
            print(f'{i+1}) Пополнение:{pop}, Баланс: {self.balance}  ')
            sleep(0.001)
#  сделал нумерацию, чтобы видеть число транзакций
    def take(self):
        for i in range(100):
            snt = random.randint(50, 500)
            print(f'Запрос на {snt}  ')
            if self.balance >= snt:
                with self.lock:
                    self.balance -= snt
                print(f'{i+1}) Снятие: {snt}, Баланс:{self.balance}  ')
                sleep(0.001)
            elif self.balance < snt:
                print('Запрос отклонён, недостаточно средств ')


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')