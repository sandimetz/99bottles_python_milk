class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in reversed(range(lower, upper + 1)))

  def verse(self, number):
    bottle_number = BottleNumber(number)

    return (
      f'{bottle_number} of milk on the wall, '.capitalize() +
      f'{bottle_number} of milk.\n'
      f'{bottle_number.action()}, '
      f'{bottle_number.successor()} of milk on the wall.\n'
    )


class BottleNumber:
  def __new__(cls, number):
    candidates = [BottleNumber6, BottleNumber1, BottleNumber0, BottleNumber]
    for candidate in candidates:
      if candidate.handles(number):
        return super().__new__(candidate)

  @staticmethod
  def handles(number):
    return True

  def __init__(self, number):
    self._number = number

  def __str__(self):
    return f'{self.quantity()} {self.container()}'

  def quantity(self):
    return str(self._number)

  def container(self):
    return 'bottles'

  def action(self):
    return f'Take {self.pronoun()} down and pass it around'

  def pronoun(self):
    return 'one'

  def successor(self):
    return BottleNumber(self._number - 1)


class BottleNumber0(BottleNumber):
  @staticmethod
  def handles(number):
    return number == 0

  def quantity(self):
    return 'no more'

  def action(self):
    return 'Go to the store and buy some more'

  def successor(self):
    return BottleNumber(99)


class BottleNumber1(BottleNumber):
  @staticmethod
  def handles(number):
    return number == 1

  def container(self):
    return 'bottle'

  def pronoun(self):
    return 'it'


class BottleNumber6(BottleNumber):
  @staticmethod
  def handles(number):
    return number == 6

  def quantity(self):
    return '1'

  def container(self):
    return 'six-pack'
