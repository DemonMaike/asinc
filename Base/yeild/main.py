# create function with yeild
def test(long):
    for i in range(long):
        yield i

print(type(test)) # printed function

gen = test(3) # create generator
print(type(gen)) # printed generator

dir(gen) # we look dunder __next__ and we can use func next()
print('gen')
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 2


# Use yeild from is more convesiese, becouse it join yield and cicle for
def test2(long):
    yield from range(long)

gen2 = test2(3) # create gen
print('\ngen2')
print(next(gen2)) # 0
print(next(gen2)) # 1
print(next(gen2)) # 2
# print(next(gen2)) # raised StopIteration

# But general idea for yield from is take data from anouther generator, subgenerator

def subgenerator():
    yield 'World'

def generator():
    yield 'Hello'
    yield from subgenerator()
    yield '!'

for i in generator():
    print(i, end=' ')
