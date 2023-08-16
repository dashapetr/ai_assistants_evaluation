import pandas as pd

data = {0: [1, 2, 3, 4], 1: [2, 3], 2: [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# ValueError: All arrays must be of the same length

# code after the bug correction (didn't correct the bug):

import pandas as pd

data = {0: [1, 2, 3, 4], 1: [2, 3], 2: [1, 2, 3, 4, 5]}
df = pd.DataFrame(data, index=[0, 1, 2])

# ValueError: Length of values (4) does not match length of index (3)
