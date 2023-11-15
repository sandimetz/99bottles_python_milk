class Bottles:
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
          '1 bottle of milk on the wall, '
          '1 bottle of milk.\n'
          'Take it down and pass it around, '
          'no more bottles of milk on the wall.\n'
        )
      case 2:
        return (
          '2 bottles of milk on the wall, '
          '2 bottles of milk.\n'
          'Take one down and pass it around, '
          '1 bottle of milk on the wall.\n'
        )
      case _:
        return (
          f'{number} bottles of milk on the wall, '
          f'{number} bottles of milk.\n'
          f'Take one down and pass it around, '
          f'{number-1} bottles of milk on the wall.\n'
        )
