#!/usr/bin/env python3

from rock_paper_scissors import RockPaperScissors as RPS

from argparse import ArgumentParser

def main():
    parser = ArgumentParser()

    parser.add_argument('-p','--player', type=str, default=None)

    args = parser.parse_args()

    if args.player:
        game = RPS.playersVsComputer(args.player)
    else:
        game = RPS.computerVsComputer()

    game.play()
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
