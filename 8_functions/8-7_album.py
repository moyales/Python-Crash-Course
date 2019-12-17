#8.7 Album

# Write a function called make_album() that builds a dictionary
# describing a music album.
# Should contain artist name and album title, then return a dict.

def make_album(artist_name, album_title, track_number = ''):
	"""Return a dict. of info about an album."""
	album = {'artist' : artist_name, 'title' : album_title}
	if track_number:
		album['track_number'] = track_number
	return album

music = make_album('queen', 'news of the world')
print(music)

other_music = make_album('boston', 'third stage', track_number = 10)
print(other_music)
	
