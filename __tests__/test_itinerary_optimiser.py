from src.itinerary_optimiser import artists_clash, starts_during

def test_artists_clash_does_clash():
  artist_1 = ['BILLIE EILISH','22:15','23:45','FRIDAY','PYRAMID STAGE']
  artist_2 = ['FOALS','22:30','23:45','FRIDAY','OTHER STAGE']

  clashes = artists_clash(artist_1, artist_2)

  assert clashes == True

def test_artists_clash_dont_clash_same_day():
  artist_1 = ['BILLIE EILISH','22:15','23:45','FRIDAY','PYRAMID STAGE']
  artist_2 = ['COLIN','23:50','00:00','FRIDAY','ANOTHER STAGE']

  clashes = artists_clash(artist_1, artist_2)

  assert clashes == False

def test_artists_clash_dont_clash_different_day():
  artist_1 = ['BILLIE EILISH','22:15','23:45','FRIDAY','PYRAMID STAGE']
  artist_2 = ['FOALS','22:30','23:45','SATURDAY','OTHER STAGE']

  clashes = artists_clash(artist_1, artist_2)

  assert clashes == False

def test_starts_during():
  artist_1 = ['','22:15','23:45','','']
  artist_2 = ['','22:30','23:45','','']
  artist_3 = ['','23:45','00:00','','']
  artist_4 = ['','23:45','00:00','','']

  assert starts_during(artist_1, artist_2) == False
  assert starts_during(artist_2, artist_1) == True
  assert starts_during(artist_3, artist_2) == False
  assert starts_during(artist_3, artist_4) == True