import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._is_winner = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_player_collision(cast)
            self._handle_game_over(cast)


    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # score = cast.get_first_actor("scores")
        # food = cast.get_first_actor("foods")
        # snake = cast.get_first_actor("snakes")
        # head = snake.get_head()

        # if head.get_position().equals(food.get_position()):
        #     points = food.get_points()
        #     snake.grow_tail(points)
        #     score.add_points(points)
        #     food.reset()

        player1 = cast.get_first_actor("snakes")
        player2 = cast.get_first_actor("foods")

        player1.grow_tail(1)
        player2.grow_tail(1)

    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("snakes")
        player1_head = player1.get_segments()[0]
        player1_segments = player1.get_segments()[1:]

        player2 = cast.get_first_actor("foods")
        player2_head = player2.get_segments()[0]
        player2_segments = player2.get_segments()[1:]
        
        for player1_segment in player1_segments:
            if player1_head.get_position().equals(player1_segment.get_position()):
                self._is_game_over = True
                self._is_winner = True
            # elif player1_head.get_position().equals(player2_head.get_position()):
            #     self._is_game_over = True
            # elif player2_head.get_position().equals(player1_segment.get_position()):
            #     self._is_game_over = True

        
        # for player2_segment in player2_segments:
        #     if player1_head.get_position().equals(player2_segment.get_position()):
        #         self._is_game_over = True   
        
        # for player1_segment in player1_segments:
        #     if player2_head.get_position().equals(player1_segment.get_position()):
        #         self._is_game_over = True
            
        for player2_segment in player2_segments:
            if player2_head.get_position().equals(player2_segment.get_position()):
                self._is_game_over = True
                self._is_winner = True
            # elif player1_head.get_position().equals(player2_segment.get_position()):
            #     self._is_game_over = True
            #     self._is_winner = True
            

    def _handle_player_collision(self, cast):

        player1 = cast.get_first_actor("snakes")
        player1_head = player1.get_segments()[0]
        player1_segments = player1.get_segments()[1:]

        player2 = cast.get_first_actor("foods")
        player2_head = player2.get_segments()[0]
        player2_segments = player2.get_segments()[1:]

        for player1_segment in player1_segments:
            for player2_segment in player2_segments:
                if player2_head.get_position().equals(player2_segment.get_position()):
                    self._is_game_over = True
            
        
            # if player1_head.get_position().equals(segment.get_position()):
            #     self._is_game_over = True

        
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("snakes")
            player1_segments = player1.get_segments()
            player2 = cast.get_first_actor("foods")
            player2_segments = player2.get_segments()[1:]

            player2_head = player2.get_head()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()

            if self._is_winner:
                message.set_text("Game over: Player 2 wins!")
            elif self._is_winner == False:
                message.set_text("Game over: Player 1 wins!")

            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in player1_segments:
                segment.set_color(constants.WHITE)
            for segment in player2_segments:
                segment.set_color(constants.WHITE)