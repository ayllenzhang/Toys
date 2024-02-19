word_list = [
    "about", "after", "again", "below", "could", "every",
    "first", "found", "great", "house", "large", "learn", 
    "never", "other", "place", "plant", "point", "right", 
    "small", "sound", "spell", "still", "study", 
    "their", "there", "these", "thing", "think", "three", 
    "water", "where", "which", "world", "would", "write"
]

input_info = "Provide pos and alphabet (e.g. \"1 ABSCV\" ) to guess.\nr - restart, q - quit."

if __name__ == "__main__":
    current_list = []
    tested_pos = []
    need_init = True
    while True:
        if need_init:
            need_init = False
            current_list = word_list
            tested_pos = []
            print(input_info)
        s = input()
        if s.upper() == "Q":
            break
        elif s.upper() == "R":
            current_list = word_list
            print("\nStart a new guess\n")
            need_init = True
        else:
            s_params = s.split(" ")
            s_pos = s_params[0]
            if len(s_params) == 2 and s_pos.isnumeric() and 0 < int(s_pos) <= 5:
                pos = int(s_pos) - 1
                new_list = []
                alphabet = [ch for ch in s_params[1]]
                for word in current_list:
                    if word[pos] in alphabet:
                        new_list.append(word)
                current_list = new_list
                pos_type = [{w[pos] for w in current_list} for pos in range(5)]
                pos_count = [len(ptype) for ptype in pos_type]
                print(f"Available words: {current_list}")
                if len(current_list) > 3:
                    tested_pos.append(pos)
                    for tp in tested_pos:
                        pos_count[tp] = -1
                    max_count_pos = pos_count.index(max(pos_count))
                    print(f"Suggest to try pos {max_count_pos + 1} ({sorted(pos_type[max_count_pos])})")
                else:
                    print("Remaining word <=3. Automatically restart.\n")
                    need_init = True
            else:
                print("Invalid input. Try again.")
