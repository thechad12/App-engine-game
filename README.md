# Blackjack API

-This is an API using Google App Engine for a game of blackjack. It is ready
to be used with any front-end to create an app.

-SET UP:

  -Update the value of application in app.yaml to match the App ID given to you in the app engine console.

  -Run your app locally through the app engine launcher.

-GAME:
  -This is a game of Blackjack: it generates 2 random cards for you, and you try to get to 21 or as close to 21 as possible without going over. Once your cards are dealt you can choose to hit or stay, meaning you can either get another card or keep the hand you have, respectively. If you go over 21, the game ends and your score will be 0. If you do not go over 21, your score will be the sum of your hand divided by 21 and multiplied by 100.


-FUNCTIONS:

  -new_game: Creates a new game with a user. Creates a post request, takes in user_name and initial hand. Returns a game form with the initial game state.

  -get_game: Finds a game by querying for the urlsafe_game_key. Creates a get request, and returns a form with the initial game state.

  -make_move: The function for game moves. This will query for the
  urlsafe_game_key to associate the moves with that game and creates a post request.  It will check that the game is not already over before making any moves. The moves are based on the player's current hand. If it is over 21, it will end the game.
  If it is under 21, the player will have a choice to hit or stay. If they hit,
  it will append a new card to the current hand. If they choose to stay, it
  will end the game and return the sum of their final hand.

  -get_scores: Returns all scores by querying the Scores class. Creates a get request and returns all scores in the database.

  -get_user_scores: Returns all scores associated with a particular user. Creates a get request and will query for the user by the username, then check if that user exists.
  If the user exists, it will query for the scores and return them. If the
  user does not exist, an exception will be raised.

  -get_high_scores: Creates a get request. Queries for all users that exist, then it will return all scores and order the scores in descending order.

  -get_user_rankings: Creates a get request. Returns the rankings of users by querying for all users, scores, and wins. It will take the sum of a user's wins and divide it by the sum of all the games they have played and order the users in descending order.

  -cancel_game: Creates a post request. Queries for the game's urlsafe_game_key and sets game.cancelled to True.

  -get_user_games: Creates a get request. Queries for a user name and checks if that user exists. If the user exists, it will return all games associated with that user. If the user does not exist, it will raise an exception.

  -get_game_history: Creates a get request. Queries for a user and checks if the user exists. If the user exists, it will query for games associated with that user and then send the game forms. It will then return the moves and the cards associated with all games associated with that user.

-MODELS:

  -User:

    -Stores username and email.

  -Game:

    -Stores game state and associated with User model.

  -Score:

    -Records completed game and associated scores as well as a boolean for game won. Associated with users/

-FORMS:

  -GameForm:

    -Representation of a game's current state: urlsafe_key, cards, game_over, message, and user_name.

  -NewGameForm:

    -Used to create a new game, using: user_name, cards.

  -MakeMoveForm:

    -Used to make a move- the user can choose to hit or stay.

  -ScoreForm:

    -A completed game's score: user_name, date, won, cards.

  -ScoreForms:

    -Multiple scores container.

  -StringMessage:

    -General purpose string container.
