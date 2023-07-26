import time

print("Готовы к старту?")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Старт!")
start_time = time.time()

input("Нажмите Enter, чтобы остановить таймер.")
end_time = time.time()

race_time = end_time - start_time

print("Ваше время: ", round(race_time, 2), "секунд.")
.
