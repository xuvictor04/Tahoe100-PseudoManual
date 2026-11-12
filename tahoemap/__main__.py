import os
import sys

from . import cli

if __name__ == "__main__":
    cli.main()
    if cli.LOOKUP_DONE:
        # A look-up only reads and prints. pyarrow's thread pool can hang while Python shuts down (about 1 run in
        # 100 of `similar` was seen to hang), so a finished look-up ends here, after flushing what it printed.
        sys.stdout.flush()
        sys.stderr.flush()
        os._exit(0)
