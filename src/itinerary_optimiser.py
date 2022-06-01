ARTIST = 0
START_TIME = 1
END_TIME = 2
DAY = 3
STAGE = 4


def artists_clash(artist_1: list[str], artist_2: list[str]):
  day_1 = artist_1[DAY]
  day_2 = artist_2[DAY]

  if day_1 != day_2:
    return False

  if starts_during(artist_1, artist_2):
    return True

  if starts_during(artist_2, artist_1):
    return True

  return False

def starts_during(artist_1: list[str], artist_2: list[str]):
  return True