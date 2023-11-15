class Bottles:
  def verse(self, number):
    return (
      f'{number} bottles of milk on the wall, '
      f'{number} bottles of milk.\n'
      f'Take one down and pass it around, '
      f'{number-1} bottles of milk on the wall.\n'
    )
