# клиентская часть
import socket

sock_1 = socket.socket() # создаем сокет
sock_1.connect( ('localhost', 9090) ) # подключаемся к серверу, где 'localhost ИЛИ IP СЕРВЕРА' а после номер порта
sock_1.send(b'hello from Vladimir') # отправка сообщения с переводом в байты

data = sock_1.recv(1024) # устанавливаем размер сообщения в 1024 байта
sock_1.close() # закрытие соединения

print(data.decode())
