# Method 1 to find the love_score using variable method
# def love_score_finder(data1, data2):
#     data = (data1 + data2).upper()
#     true_score = 0
#     love_score = 0
#     for char in data:
#         if char in "TRUE":
#             true_score += 1
#         if char in "LOVE":
#             love_score += 1
#     print(f"True Total = {true_score}")
#     print(f"Love Total = {love_score}")
#     print("Your love score is",str(true_score) + str(love_score))
#
# love_score_finder("Masud Alam","christeena")


#finding Love_score using built_in function .count()
def calculate_love_score(name1,name2):
    names = (name1 + name2).upper()

    def word(count):
        return "times" if count > 1 else "time"

    def true_score():
        t = names.count("T")
        r = names.count("R")
        u = names.count("U")
        e = names.count("E")
        print(f"T occurs {t} {word(t)}.")
        print(f"R occurs {r} {word(r)}.")
        print(f"U occurs {u} {word(u)}")
        print(f"E occurs {e} {word(e)}")
        total = t + r + u + e
        print(f"True Total = {total}")
        return total

    def love_score():
        l = names.count("L")
        o = names.count("O")
        v = names.count("V")
        e = names.count("E")
        print(f"L occurs {l} {word(l)}.")
        print(f"O occurs {o} {word(o)}.")
        print(f"V occurs {v} {word(v)}.")
        print(f"E occurs {e} {word(e)}.")
        total = l + o + v + e
        print(f"Love Total = {total}")  # \n will create a litter Gap
        return total

    print(f"Your love score is {str(true_score()) + str(love_score())}.")

calculate_love_score("Turtle","Crocodile")

