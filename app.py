# TODO: impliment factorial for python programming languages

def _fectorial(n):
    if n == 0:
        return 1
    else:
        return n * _fectorial(n-1)



number = int(input('Enter a number:'))
result = _fectorial(number)


def revarse__string(string):
    return string[::-1]

strings = str(input('Given a string:'))

reverse = revarse__string(strings)

print(reverse)