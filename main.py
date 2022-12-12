from base_function import talk, command
from function import makeSomething

if __name__ == '__main__':
    talk("Привет, чем я могу помочь вам?")

    while True:
        makeSomething(command())
