# Изменяемые и неизменяемые объекты. Кортежи

immutable_var = ("string", 1, True)           #создать кортеж
print(type(immutable_var))                    #вывести тип переменной
print(immutable_var)                          #распечатать кортеж
# Кортеж относится к неизменяемым типам данных. После создания кортежа, данные внутри него не могут измениться

mutable_list=[1, 2, 5>=3, 'Hotel', 'Home', 'An Apple']   #создать список
print(type(mutable_list))                     #вывести тип переменной
print(mutable_list)                           #распечатать исходный список
mutable_list_pop_ = mutable_list.pop()        #запомнить и удалить из списка
print(type(mutable_list_pop_))                #вывести тип переменной
print(mutable_list)                           #вывести список после .pop
print("Последний элемент в списке был: ", "'" + mutable_list_pop_ +"'")  #вывести запомненное значение из списка
