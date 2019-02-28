import argparse
import numpy as np
from my_modules.foo import Foo


def main(args):
    x = np.random.rand(x, x)
    foo = Foo(x)
    y = foo.my_func(1.0)
    print y.sum()


if __name__ == "__main__":
    parser = argpare.ArgumentParser()
    parser.add_argument("x", type=int)
    args = parser.parse_args()
    main(args)
