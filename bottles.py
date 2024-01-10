class Bottles:
  def song(self):
    return self.verses(99, 0)

  def verses(self, big, small):
    return '\n'.join(
      self.verse(bottles) for bottles in range(small, big + 1)[::-1]
    )

  def verse(self, bottles):
    return Round(bottles).to_string()


class Round:
  def __init__(self, bottles):
    self.bottles = bottles

  def to_string(self):
    return self.challenge() + self.response()

  def challenge(self):
    return (
      f'{self.bottles_of_milk().capitalize()} '
      f'{self.on_wall()}, {self.bottles_of_milk()}.\n'
    )

  def response(self):
    return (
      f'{self.go_to_the_store_or_take_one_down()}, '
      f'{self.bottles_of_milk()} {self.on_wall()}.\n'
    )

  def bottles_of_milk(self):
    return (
      f'{self.anglicized_bottle_count()} '
      f'{self.pluralized_bottle_form()} of {self.milk()}'
    )

  def milk(self):
    return 'milk'

  def on_wall(self):
    return 'on the wall'

  def pluralized_bottle_form(self):
    return 'bottle' if self.last_milk() else 'bottles'

  def anglicized_bottle_count(self):
    return 'no more' if self.all_out() else str(self.bottles)

  def go_to_the_store_or_take_one_down(self):
    if self.all_out():
      self.bottles = 99
      return self.buy_new_milk()
    lyrics = self.drink_milk()
    self.bottles -= 1
    return lyrics

  def buy_new_milk(self):
    return 'Go to the store and buy some more'

  def drink_milk(self):
    return f'Take {self.it_or_one()} down and pass it around'

  def it_or_one(self):
    return 'it' if self.last_milk() else 'one'

  def all_out(self):
    return self.bottles == 0

  def last_milk(self):
    return self.bottles == 1
