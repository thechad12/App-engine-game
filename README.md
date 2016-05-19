# Blackjack API

-This is an API using Google App Engine for a game of blackjack. It is ready
to be used with any front-end to create an app.

-Please refer to Google to generate your app.

-To launch, use the Google app engine launcher to run locally and to deploy on Google appspot. Once it is deployed, you can create a user to start playing a game of blackjack.

-Functions:

  -new_game: Creates a new game with a user.

  -get_game: Finds a game by querying for the urlsafe_game_key.

  -make_move: The function for game moves. This will query for the
  urlsafe_game_key to associate the moves with that game. It will check
  that the game is not already over before making any moves. The moves are
  based on the player's current hand. If it is over 21, it will end the game.
  If it is under 21, the player will have a choice to hit or stay. If they hit,
  it will append a new card to the current hand. If they choose to stay, it
  will end the game and return the sum of their final hand.

  -get_scores: Returns all scores by querying the Scores class.

  -get_user_scores: Returns all scores associated with a particular user.
  It will query for the user by the username, then check if that user exists.
  If the user exists, it will query for the scores and return them. If the
  user does not exist, an exception will be raised.

  -get_high_scores: Queries for all users that exist, then it will return all
  scores and order the scores in descending order.

  -get_user_rankings: Returns the rankings of users by querying for all users,
  scores, and wins. It will take the sum of a user's wins and divide it by the sum of all the games they have played and order the users in descending order.

  -cancel_game: Queries for the game's urlsafe_game_key and sets game.cancelled to True.

  -get_user_games: Queries for a user name and checks if that user exists. If the user exists, it will return all games associated with that user. If the user does not exist, it will raise an exception.

  -get_game_history: Queries for a user and checks if the user exists. If the user exists, it will query for games associated with that user and then send the game forms. It will then return the moves and the cards associated with all games associated with that user.
