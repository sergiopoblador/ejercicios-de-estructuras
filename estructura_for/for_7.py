"""Diagrama y programa para imprimir cuanots multiplos de 7 y de 9 hay en los numeors comprendidos entre 1000 y 5000"""

# input

# processing
m_7 = 0
m_9 = 0
for i in range(1000, 5001, 1):
    if i% 7 == 0:
        m_7 += 1
    if i%9 == 0:
        m_9 += 1

# output
print("entre 1000 y 5000 mil hay ")
print(m_7, "multiplos de 7")
print(m_9, "multiplos de 9 ")
