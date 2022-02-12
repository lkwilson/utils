import numpy as np

current_contrib = 0
remaining_paychecks = 12
salary = 40_000
paycheck_amount = salary / 12
bonus_amount = 0.04 * salary

max_401k_limit = 19_500
match_rate = 0.06

bonus_potential_is_before_last_paycheck = True

contrib_rates = np.arange(match_rate, .60, .005)

def final_contrib_rate(rate, verbose = False):
  if verbose:
    print(f"rate: {rate*100:.2f}%")

  contrib_per_paycheck = paycheck_amount * rate
  if verbose:
    print(f"contrib per paycheck: {contrib_per_paycheck:.2f}")

  bonus_contrib = bonus_amount * rate
  if verbose:
    print(f"bonus contributed to 401k: {bonus_contrib:.2f}")

  pre_last = current_contrib + contrib_per_paycheck * (remaining_paychecks-1)
  if verbose:
    print(f"contributions before last paycheck without / before bonus: {pre_last:.2f}")

  pre_last_bonus = pre_last + bonus_contrib
  if verbose:
    print(f"contributions before last paycheck after bonus: {pre_last_bonus:.2f}")

  remaining_bonus = max_401k_limit - pre_last_bonus
  if verbose:
    print(f"remaining before cap after bonus: {remaining_bonus:.2f}")

  remaining = max_401k_limit - pre_last
  if verbose:
    print(f"remaining before cap without / before bonus: {remaining:.2f}")


  last_rate_pre_bonus = remaining_bonus / paycheck_amount
  if verbose:
    print(f"last contrib rate (bonus before): {last_rate_pre_bonus*100:.2f}%")

  last_rate_post_bonus = remaining / (paycheck_amount + bonus_amount)
  if verbose:
    print(f"last contrib rate (bonus after): {last_rate_post_bonus*100:.2f}%")

  last_rate_no_bonus = remaining / paycheck_amount
  if verbose:
    print(f"last contrib rate (no bonus): {last_rate_no_bonus*100:.2f}%")

  if bonus_potential_is_before_last_paycheck:
    min_rate = min(last_rate_pre_bonus, last_rate_no_bonus)
    max_rate = max(last_rate_pre_bonus, last_rate_no_bonus)
  else:
    min_rate = min(last_rate_pre_bonus, last_rate_post_bonus, last_rate_no_bonus)
    max_rate = max(last_rate_pre_bonus, last_rate_post_bonus, last_rate_no_bonus)

  if verbose:
    print(f"possible rate range: {min_rate*100:.2f}% - {max_rate*100:.2f}%")

  return min_rate, max_rate

goods = []
for contrib_rate in contrib_rates:
  min_rate, max_rate = final_contrib_rate(contrib_rate)
  if max_rate < -.1:
    continue
  elif min_rate > .5:
    continue
  elif min_rate < match_rate:
    comment = "may miss out on match!"
  elif contrib_rate < max_rate:
    comment = "may not max 401k!"
  else:
    comment = ":)"
    goods.append(contrib_rate)
  print(f"[rate:{contrib_rate*100:.2f}] {min_rate*100:7.2f}% {max_rate*100:7.2f}% {comment}")

for contrib_rate in goods:
  final_contrib_rate(contrib_rate, True)
