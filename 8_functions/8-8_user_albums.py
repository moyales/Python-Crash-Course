#8.8 User Albums

# Start with program from 8.7.
# Write a while loop that allows for user input for artist and title
# Use info to call make_album() with input and print dictionary
# Include a 'quit' value.

def make_album(artist_name, album_title, track_number = ''):
	"""Return a dict. of info about an album."""
	album = {'artist' : artist_name, 'title' : album_title}
	if track_number:
		album['track_number'] = track_number
	return album

while True:
	print("\nCreate a dictionary of an album with your input!")
	print("(press 'q' at any time to quit.)")
	
	a_name = input("Artist Name: ")
	if a_name == 'q':
		break
	
	al_title = input("Album Title: ")
	if al_title == 'q':
		break
	
	album_info = make_album(a_name, al_title)
	print(album_info)
