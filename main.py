import argparse
from analysis import report



def get_args(argv=None):
    parser = argparse.ArgumentParser(description="Arguments for RENFE report")
    parser.add_argument('-d', '--destination', type=str, help="[BARCELONA, VALENCIA or SEVILLA]")
    parser.add_argument('-p', '--period', type=str, help="[month, week, weekdays, daytime and hour]")
    return parser.parse_args()


def main():
    args = get_args()
    return report(args.destination,args.period)
    


if __name__ == '__main__':
    main()