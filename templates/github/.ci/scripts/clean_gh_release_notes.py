#!/usr/bin/env python3

# This script is running with elevated privileges from the main branch against pull requests.

# This script cleans the input from artifacts which are used by the pulp documentation internally, but clutter for GitHub releases
import re
import sys

RE_VERSION = re.compile(r"^## (\d+\.\d+\.\d+)")


def main():
    plugin_name = sys.argv[1]
    version_str = ""
    for line in sys.stdin:
        if line.endswith("\n"):
            line = line[:-1]
        if line.startswith("#"):
            print(line.split(" {: #")[0])
            match = RE_VERSION.match(line)
            if match and version_str == "":
                version_str = match.group(1)
                docs_url = f"https://pulpproject.org/{plugin_name}/changes/#{version_str}"
                print("")
                print("> [!NOTE]")
                print(f"> Changes are also available on [Pulp docs]({docs_url})")
        else:
            print(line)


if __name__ == "__main__":
    main()
