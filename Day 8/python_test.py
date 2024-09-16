



# def calculate_love_score(name_1, name_2):
#     Ttotal = 0
#     Rtotal = 0
#     Utotal = 0
#     Etotal = 0
#     name_dictionaryc = [name_1, name_2]
#     name_dict = []
#     for dict in name_dictionaryc:
#         name_dict += dict
#     capitalized_list = [item.upper() for item in name_dict]
#     for name_Check in capitalized_list:
#         if name_Check == "T":
#             Ttotal += 1
#         elif name_Check == "R":
#             Rtotal += 1
#         elif name_Check == "U":
#             Utotal += 1
#         else:
#             if name_Check == "E":
#                 Etotal += 1
#     print(f"T occurs {Ttotal} times")
#     print(f"R occurs {Rtotal} times")
#     print(f"U occurs {Utotal} times")
#     print(f"E occurs {Etotal} times")
#     print(f"Total {Ttotal+Rtotal+Utotal+Etotal}")
#
#     print("\n")
#
#     Ltotal = 0
#     Ototal = 0
#     Vtotal = 0
#     Eetotal = 0
#
#     capitalized_list = [item.upper() for item in name_dict]
#     for name_Check in capitalized_list:
#         for char in name_Check:
#             if char == "L":
#                 Ltotal += 1
#             elif char == "O":
#                 Ototal += 1
#             elif char == "V":
#                 Vtotal += 1
#             else:
#                 if char == "E":
#                     Eetotal += 1
#     print(f"L occurs {Ltotal} times")
#     print(f"O occurs {Ototal} times")
#     print(f"V occurs {Vtotal} times")
#     print(f"E occurs {Etotal} times")
#     print(f"Total {Ltotal + Ototal + Vtotal + Eetotal}")
#
#     print(f"Love Score {Ttotal+Rtotal+Utotal+Etotal}{Ltotal + Ototal + Vtotal + Eetotal}")


def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)



# calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
