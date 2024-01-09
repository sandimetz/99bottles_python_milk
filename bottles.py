class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, high, low):
    return '\n'.join(
      self.verse(verse_number) for verse_number in sorted(range(low, high+1), reverse=True)
    )

  def verse(self, number):
    return self.verse_for(number).text()

  def verse_for(self, number):
    def no_more(verse):
      return (
        'No more bottles of milk on the wall, '
        'no more bottles of milk.\n'
        'Go to the store and buy some more, '
        '99 bottles of milk on the wall.\n'
      )

    def last_one(verse):
      return (
        '1 bottle of milk on the wall, '
        '1 bottle of milk.\n'
        'Take it down and pass it around, '
        'no more bottles of milk on the wall.\n'
      )

    def penultimate(verse):
      return (
        '2 bottles of milk on the wall, '
        '2 bottles of milk.\n'
        'Take one down and pass it around, '
        '1 bottle of milk on the wall.\n'
      )

    def default(verse):
      return (
        f'{verse.number} bottles of milk on the wall, '
        f'{verse.number} bottles of milk.\n'
        f'Take one down and pass it around, '
        f'{verse.number - 1} bottles of milk on the wall.\n'
      )

    lyric_functions = [no_more, last_one, penultimate, default]
    chosen_lyric = (
      lyric_functions[0] if number == 0 else
      lyric_functions[1] if number == 1 else
      lyric_functions[2] if number == 2 else
      lyric_functions[3]
    )

    return Verse(number, chosen_lyric)


class Verse:
  def __init__(self, number, lyrics):
    self.number = number
    self.lyrics = lyrics

  def text(self):
    return self.lyrics(self)
