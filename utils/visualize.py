import velocity_obstacle.velocity_obstacle as velocity_obstacle
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--filename", help="filename, in case you want to save the animation")

    args = parser.parse_args()
    velocity_obstacle.simulate(args.filename)
