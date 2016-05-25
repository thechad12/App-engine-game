# Blackjack API

-This is an API using Google App Engine for a game of blackjack. It is ready
to be used with any front-end to create an app.

-SET UP:

  -Update the value of application in app.yaml to match the App ID given to you in the app engine console.

  -Run your app locally through the app engine launcher.

-GAME:
  -This is a game of Blackjack: it generates 2 random cards for you, and you try to get to 21 or as close to 21 as possible without going over. Once your cards are dealt you can choose to hit or stay, meaning you can either get another card or keep the hand you have, respectively. If you go over 21, the game ends and your score will be 0. If you do not go over 21, your score will be the sum of your hand divided by 21 and multiplied by 100.


-ENDPOINTS:

* new_game: 
  * Path:'/game'
  * Method: POST
  * Parameters: Username
  * Returns: New game form
  * Description: Creates a new game

* get_game: 
  * Path: '/game/urlsafe_game_key'
  * Method: GET
  * Parameters: urlsafe_game_key
  * Returns: Game form with current state of game
  * Description: Returns the current state of a game

* make_move:
  * Path: '/game/urlsafe_game_key/move'
  * Method: POST
  * Parameters: urlsafe_game_key
  * Returns: Game form with a win or loss and final score
  * Description: Endpoint to make a move in the game. Deals cards and then allows user to choose to hit or stay.

* get_scores:
  * Path: '/scores'
  * Method: GET
  * Parameters: None
  * Returns: All scores of the game, unordered
  * Description: Returns all scores in the game

* get_user_scores:
  * Path: '/scores/user/username'
  * Method: GET
  * Parameters: Username
  * Returns: All scores for a given user
  * Description: Returns all scores for a user

* get_high_scores:
  * Path: '/scores/highscores'
  * Method: GET
  * Parameters: None
  * Returns: All scores in order of highest to lowest
  * Description: Gets all scores and orders them to see high scores

* get_user_rankings:
  * Path: '/users/user-rankings'
  * Method: GET
  * Parameters: None
  * Returns: User rankings ordered by percentage of wins over games played
  * Description: Creates user rankings for the game

* cancel_game: 
  * Path: '/game/urlsafe_game_key/cancel'
  * Method: POST
  * Parameters: urlsafe_game_key
  * Returns: Game form with cancelled set to true
  * Description: Cancels a game 

* get_user_games:
  * Path: '/username/games'
  * Method: GET
  * Parameters: Username
  * Returns: All games for a user
  * Description: Gets all games for a user

* get_game_history: 
  * Path: '/game/urlsafe_game_key/history'
  * Method: GET
  * Parameters: urlsafe_game_key
  * Returns: History of a particular game, which includes cards dealt and moves made
  * Description: Allows access to a specific game's history

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
