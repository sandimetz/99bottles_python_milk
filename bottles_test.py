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


def test_verse_2():
  expected = (
    '2 bottles of milk on the wall, '
    '2 bottles of milk.\n'
    'Take one down and pass it around, '
    '1 bottle of milk on the wall.\n'
  )
  assert Bottles().verse(2) == expected


def test_verse_1():
  expected = (
    '1 bottle of milk on the wall, '
    '1 bottle of milk.\n'
    'Take it down and pass it around, '
    'no more bottles of milk on the wall.\n'
  )
  assert Bottles().verse(1) == expected


def test_verse_0():
  expected = (
    'No more bottles of milk on the wall, '
    'no more bottles of milk.\n'
    'Go to the store and buy some more, '
    '99 bottles of milk on the wall.\n'
  )
  assert Bottles().verse(0) == expected
