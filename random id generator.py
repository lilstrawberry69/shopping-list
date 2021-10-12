import random

alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
              'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'
              ,'R','S','T','U','V','W','X','Y','Z']

num_list = ['1','2','3','4','5','6','7','8','9']

spe_list = ['!','@',"#","$","%","^","&","*","(",")"]
key = random.choice(alpha_list) + random.choice(num_list) + random.choice(spe_list) + random.choice(alpha_list) + random.choice(num_list) + random.choice(spe_list)
print(random.randint(1,100000000))
