import argparse
def fnc_s(n):
    if n <= 2:
        return 1
    else:
        return fnc_s(n - 2) + fnc_s(n - 1)

parser = argparse.ArgumentParser(description='fibonacci')
parser.add_argument('--value', type=int, default=10)
args = parser.parse_args()

if type(args.value) == int:
    print(fnc_s(args.value))
else:
    raise Exception(f"error: [{args.value}]  value is not integer")
