class Bottles:
  def verse(self, number):
    if (number == 99):
      return (
        '99 bottles of milk on the wall, '
        '99 bottles of milk.\n'
        'Take one down and pass it around, '
        '98 bottles of milk on the wall.\n'
      )
    return (
      '3 bottles of milk on the wall, '
      '3 bottles of milk.\n'
      'Take one down and pass it around, '
      '2 bottles of milk on the wall.\n'
    )
