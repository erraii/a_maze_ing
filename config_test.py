import sys

from config import ConfigParser, validate_config
from pydantic import ValidationError
# now we have pydantic so this is not used
# from config.validator import ConfigValidator

def main() -> None:

    #   Eray Input
    #   settings = load_settings("settings.json")

    """Run the A-Maze-ing program."""
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    try:
        raw_settings = ConfigParser(sys.argv[1]).parse()
        # now we have pydantic so this is not used
        # settings = ConfigValidator(raw_settings).validate()
        settings = validate_config(raw_settings)
    except OSError as err:
        print(f"File error: {err}")
        return
    except ValidationError as err:
        print(f"Config error:\n{err}")
        return
    except ValueError as err:
        print(f"Config error: {err}")
        return

    print("Config is valid.")
    # print(config)

    # app = MazeApplication(settings)
    print(settings)

    #   app.run()


if __name__ == "__main__":
    main()
