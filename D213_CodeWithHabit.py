class Song:
    def __init__(self, name, genre, length, language, format):
        self.name = name
        self.genre = genre
        self.length = length
        self.language = language
        self.format = format

    
song1 = Song("Raining", "jazz","2:00","English", "mp3")

print(song1.genre)

