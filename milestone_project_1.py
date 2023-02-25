MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []


def movie_info():
  title = input("Enter the movie title: ")
  director = input("Enter the movie director: ")
  year = input("Enter the movie release year: ")

  movies.append({
      'title': title,
      'director': director,
      'year': year
  })
  

def list_movies():
   for movie in movies:
      print_movie(movie)


def print_movie(movie):
   print(f"\nTitle: {movie['title']}")    
   print(f"Director: {movie['director']}") 
   print(f"Release year: {movie['year']}")

def find_movie():
   movie_query = input("Enter the movie title you are looking for: ")
   for movie in movies:
      if movie_query == movie['title']:
         print(f"\n{movie_query} is in the movie list.")
         print_movie(movie)


user_options = {
  'a': movie_info,
  'l': list_movies, 
  'f': find_movie
}


def menu_selector():
  selection = input(MENU_PROMPT)
  while selection != 'q':
      if selection in user_options:
        selected_function = user_options[selection] 
        selected_function()
      else:
          print('Unknown command. Please try again.')

      selection = input(MENU_PROMPT)

menu_selector()