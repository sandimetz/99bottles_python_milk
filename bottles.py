class Bottles:
  def verse(self, number):
    if (number == 2):
      return (
        '2 bottles of milk on the wall, '
        '2 bottles of milk.\n'
        'Take one down and pass it around, '
        '1 bottle of milk on the wall.\n'
      )
    return (
      f'{number} bottles of milk on the wall, '
      f'{number} bottles of milk.\n'
      f'Take one down and pass it around, '
      f'{number-1} bottles of milk on the wall.\n'
    )
