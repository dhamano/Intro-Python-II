from textwrap import wrap

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

desc = f'{color.GREEN}North{color.END} of you, a long, unlit gravel pathway leads to the main house. The gate behind you is locked, and topped with several layers of razor wire. Somebody is serious about home security.'
res = wrap(desc, 50)
joined = '\r'.join(res)
print(joined)