import argparse
import numpy as np
from my_modules.foo import Foo


def main(args):
    assert args.x > 0, "x should be positive"
    x = np.random.rand(args.x, args.x)
    foo = Foo(x)
    y = foo.my_func(1.0)
    print(y.sum())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int)
    args = parser.parse_args()
    main(args)
