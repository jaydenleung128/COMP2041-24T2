#!/usr/bin/env python3

import sys
from collections import Counter

weights = Counter()
for n in sys.argv[1:]:
    weights[n] += int(n)

print(weights.most_common(1)[0][0])