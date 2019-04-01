#!/usr/bin/env python3


class Envelope:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __lt__(self, other):
        if (self.width < other.width and self.height < other.height or
                self.width < other.height and self.height < other.width):
            return True
        return False

    def __gt__(self, other):
        if (self.width > other.width and self.height > other.height or
                self.width > other.height and self.height > other.width):
            return False
        return True


def comparison():

    while True:
        try:
            width1 = float(input("Enter width of the first envelop: "))
            height1 = float(input("Enter height of the first envelop: "))
            width2 = float(input("Enter width of the second envelop: "))
            height2 = float(input("Enter height of the second envelop: "))
            if width1 <= 0 or width2 <= 0 or height1 <= 0 or height2 <= 0:
                print("Width or height can't be negative or zero! Please try again..")
                continue
        except ValueError:
            print("Input error: entered incorrect data. Please try again.")
            continue

        first_envelop = Envelope(width1, height1)
        second_envelop = Envelope(width2, height2)

        if first_envelop < second_envelop:
            print("First envelop can be inserted in the second.")
        elif second_envelop < first_envelop:
            print("Second envelop can be inserted in the first.")
        else:
            print("Envelops can't be put in each other")

        try_again = str(input('Do you want to continue? [Y/n] '))
        answer = ['y', 'yes']
        if try_again.lower() not in answer:
            break


def main():
    comparison()


if __name__ == '__main__':
    main()
