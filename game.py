from modules import Game, printm


def main():
    try:
        Game().run()
    except EOFError:
        printm("The input stream was cut off.\nClosing game now...", 0.03)
        exit(1)
    except KeyboardInterrupt:
        print()
        printm("Forcefully ending the game.", 0.05)
        exit(0)


if __name__ == "__main__":
    main()
