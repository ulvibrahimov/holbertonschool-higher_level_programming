[13.03.26, 07:33:04] Ulvi İbrahimov: File: 3-infinite_add.py
[13.03.26, 07:34:15] Yusif Bmu: #!/usr/bin/python3
import sys


if _name_ == "_main_":
    total = 0

    for arg in sys.argv[1:]:
        total += int(arg)

    print(total)
