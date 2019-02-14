# серверная часть
import socket

sock_1 = socket.socket() # создаем сокет
sock_1.bind( ('', 9090) ) # биндим порт и разрешенные IP адреса
sock_1.listen(1) # устанавливаем количество разрешенных пользователей
connect, addres = sock_1.accept() # принятие подключения

while True:
    data = connect.recv(1024) # задаем размер пакета в 1024 байта
    if not data: # если данных нет
        break    # то метов accept ничего не возвращает
    connect.send(data.upper()) # возвращаем строку с обратным порядком символов

connect.close() # закрываем соединение
