# Корутины или сопрограмы


# После последнего шага, для удоства, решено сделать декоратор для возможности пропускать этап передачи генератору и сразу работать с 
# генератором, нужно посредством дегоратора передать none при выполении последней функции

def corutine(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        x.send(None)
        return x
    return inner

# В yield можно передавать значения, проверить статус генератора можно через getgeneratorstate модуля inspect
# Передача данных в yield происходит через .send() объекта генератора, при первой итерации по стандарту передаётся None, после можно
# передавать требующиеся значения.
def subgen():
    message = yield
    print(message)
    

# # Пример задачи с использованием такого свойства генераторов
# Проблема. Требуется найти среднее значение данных, которые постепенно поступают для формирования статистики(посещение сайта, продажи и т.д.)
# Реализуем генератор, который будет готов к получению данных и расчёту среднего значения.
@corutine
def avarege():
    count = 0
    summ = 0
    avarege = None
    
    while True:
        try:
            x = yield # не забываем что yield работает как return, то есть он возвращает значения!
        
        except StopIteration:
            print('Done')
        
        else:
            count += 1
            summ += x
            avarege = round(summ / count, 2)


# Сейчас сделаем делегирующий генератор и саб генератор

# Создадим пустое исключение чтобы увидеть, что дальше мы получим return, но после break.
# В ручную поднять исключение в объекте генератора можно с помощью метода .throw(exception)
# Остановить генератор можно с помощью .close()
class BlaBlaExc(Exception):
    pass

#@corutine
def subgen():
    while True:
        try:
            x = yield
            print(x)
            
        except BlaBlaExc:
            print('Bye!')
            
        except StopIteration:
            break
    
    return 'Really bye!'


# @corutine
# def delgen(g):
#     while True:
#         x = yield
#         g.send(x)

# Здесь мы упрощаем выше указаный код, переопределяя делегирующий генератор при помощи yield from
# Yield from по PEP 380 определяет, что передаваемая корутина уже будет в статусе Suspended, в связи с этим можно убрать самодельный декоратор
# из саб-генератора

@corutine
def delgen(g):
    result = yield from g # При этом нам даже не нужен бесконечный цикл, очень сильно упрощается код
    print(result)