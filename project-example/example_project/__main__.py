# Import stuff from other files
# from . import module

from . import utils



def main():
    print(utils.greet("Hello", "World"))

if __name__ == '__main__':
    main()