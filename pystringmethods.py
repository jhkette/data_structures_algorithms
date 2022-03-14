def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common =[]
  for c in string_one:
    #   c in string returns True or False 
    #  so you do (c in string_two) and not(c in common):
    if (c in string_two) and not(c in common):
      common.append(c)
  return common


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password



authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names=authors.split(',')

# basic string splitting
author_last_names =[]
for name in author_names:
  author_last_names.append(name.split()[1])