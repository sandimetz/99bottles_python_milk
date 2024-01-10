from bottles import Bottles


def test_the_first_verse():
  expected = (
    '99 bottles of milk on the wall, '
    '99 bottles of milk.\n'
    'Take one down and pass it around, '
    '98 bottles of milk on the wall.\n'
  )
  assert Bottles().verse(99) == expected


def test_another_verse():
  expected = (
    '3 bottles of milk on the wall, '
    '3 bottles of milk.\n'
    'Take one down and pass it around, '
    '2 bottles of milk on the wall.\n'
  )
  assert Bottles().verse(3) == expected
