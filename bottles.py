class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, upper, lower):
    return '\n'.join(self.verse(i) for i in reversed(range(lower, upper + 1)))

  def verse(self, number):
    match number:
      case 0:
        return (
          'No more bottles of milk on the wall, '
          'no more bottles of milk.\n'
          'Go to the store and buy some more, '
          '99 bottles of milk on the wall.\n'
        )
      case 1:
        return (
          f'1 bottle of milk on the wall, '
          f'1 bottle of milk.\n'
          f'Take it down and pass it around, '
          f'no more bottles of milk on the wall.\n'
        )
      case _:
        return (
          f'{number} bottles of milk on the wall, '
          f'{number} bottles of milk.\n'
          f'Take one down and pass it around, '
          f'{number-1} {self.container(number-1)} of milk on the wall.\n'
        )

  def container(self, number):
    if number == 1:
      return 'bottle'
    return 'bottles'
