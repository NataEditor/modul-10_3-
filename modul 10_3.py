import threading
import random
import time
from threading import Thread, Lock



class Bank():
    
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock=Lock()
    
    
    def deposit(self):
        for p in range(100):
            replenishment=random.randint(50,500)
            try:
                self.balance = self.balance + replenishment
                if self.balance >=  500 and self.lock.locked():
                    self.lock.release()
            finally:
                print(f'Пополнение на: {replenishment}. Баланс: {self.balance}')
                time.sleep(0.001)
    
    
    def take(self):
        for t in range(100):
            withdrawal=random.randint(50,500)
            print(f'запрос на: {withdrawal}')
            if withdrawal <= self.balance:
                self.balance = self.balance - withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
            try:
                if withdrawal>= self.balance:
                    self.lock.acquire
            finally:
                
                time.sleep(0.001)
            
    
    
    
    
    
bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')