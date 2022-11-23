import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.point import Point


def main():

    # create two cycles, adds positions and colors
    cycle_one = Cycle(
        Point(int(constants.MAX_X - 500), int(constants.MAX_Y / 2)))
    cycle_two = Cycle(
        Point(int(constants.MAX_X - 200), int(constants.MAX_Y / 2)))
    cycle_one.set_cycle_color(constants.GREEN)
    cycle_two.set_cycle_color(constants.RED)
    # cycle_one_name = "Player 1"
    # cycle_two_name = "Player 2"
    # cycle_one.set_name(cycle_one_name)
    # cycle_two.set_name(cycle_two_name)

    # Create the cast
    cast = Cast()
    cast.add_actor("cycle_one", cycle_one)
    cast.add_actor("cycle_two", cycle_two)

    # score1 = Score()
    # score2 = Score()

    # add: where will the scores be positioned?
    # score1.add_points(0)
    # score2.add_points(0)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
