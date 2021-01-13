import numpy as np

# Base Salary
S = None

# 401k max contrib amnt
K = 19_500

# Set contrib rate
R = None

# Num paychecks per year
N = None

# Employer match amnt
E = None

B = np.arange(1, 1.21, .01)

# derived from
# R(SB/N)(N-1) + R_tild*(SB/N) = K
# N-1 payments of SB/N at rate R plus final month, R_tild * SB/N, is 401k max

R_tild = N*K/S/B - R*(N-1)

print('contrib rate:', R)
print("bonus multiplier | final paycheck's contrib rate to max 401k")
for b, r in zip(B, R_tild):
    if r < E:
        msg = 'Not getting full match'
    elif r > R:
        msg = 'Manual contrib rate change required'
    else:
        msg = ''
    print(f'{b:.2f} {r:.2f} {msg}')

