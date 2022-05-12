import numpy as np
incomplete = ["# Misc.",
              "# Theory",
              "# Recommendation Systems",
              "# ML/Statistical Models",
              "# K-NN",
              "# Kernels",
              "# Language Modeling",
              "# Advanced Normalization",
              "# Ensemble Learning", 
              "# The Centroid Method"]
              # "# CNNs",
              # "# RNNs",

with open('research/history.txt', 'r') as f:
    history = eval("[" + ', '.join(f.read().split('\n')) + ']')[-6:]
    print(history)


with open('research/history_rand.txt', 'r') as f:
    history_rand = eval("[" + ', '.join(f.read().split('\n')) + ']')[-50:]
    print(history_rand)



def create_answers():
    with open('research/answers.md', 'r') as f:
        lines = f.read().split('\n')

    titles = []
    for l in lines:
        if "# " in l[:2] and l not in incomplete and l not in history:
            titles.append(l)

    titles = list(set(titles))
    titles = list(set(titles))

    rand_idx = np.random.randint(len(titles))

    print("Today's topic is: ", titles[rand_idx][2:])

    with open('research/history.txt', 'a') as f:
        f.write('"' + titles[rand_idx] + '"\n')

    lines[7] = "\n" + "<!-- " + "\n" + lines[7]
    
    lines[-1] = lines[-1] + "\n\n" + "--> " + "\n\n"

    topic_idx = -1
    for idx, line in enumerate(lines):
        if titles[rand_idx] in line:
            lines[idx - 1] = "\n" + "-->" + "\n" + lines[idx - 1]
            topic_idx = idx

    for idx in range(topic_idx, len(lines)):
        if "***" in lines[idx]:
            lines[idx - 1] = "\n" + "<!-- " + "\n" + lines[idx - 1]
            break


    with open('research/answers_today.md', 'w') as f:
        for l in lines:
            if "permalink" in l:
                f.write(l + "_today" + '\n')
            else:
                f.write(l + '\n')
    # with open('research/answers_today.md', 'w') as f:
    #     for l in lines:
    #         if "permalink" in l:
    #             f.write(l + "_today" + '\n')
    #         else:
    #             f.write(l + '\n')
    return titles[rand_idx]


def create_questions(title):
    with open('research/questions.md', 'r') as f:
        lines = f.read().split('\n')

    lines[7] = "\n" + "<!-- " + "\n" + lines[7]
    lines[-1] = lines[-1] + "\n\n" + "--> " + "\n\n"

    topic_idx = -1
    for idx, line in enumerate(lines): 
        if title in line:
            lines[idx - 1] = "\n" + "-->" + "\n" + lines[idx - 1]
            topic_idx = idx

    for idx in range(topic_idx, len(lines)):
        if "***" in lines[idx]:
            lines[idx - 1] = "\n" + "<!-- " + "\n" + lines[idx - 1]
            break


    with open('research/questions_today.md', 'w') as f:
        for l in lines:
            if "permalink" in l:
                f.write(l + "_today" + '\n')
            else:
                f.write(l + '\n')
    with open('research/questions_today.md', 'w') as f:
        for l in lines:
            if "permalink" in l:
                f.write(l + "_today" + '\n')
            else:
                f.write(l + '\n')
    return

# title = create_answers()
# create_questions(title)



def not_valid(i, lines):
    j = i
    while "# " != lines[j][:2]:
        j -= 1

    if lines[j] in incomplete:
        return True
    return False

def get_title(i, lines):
    j = i
    while "# " != lines[j][:2]:
        j -= 1
    return lines[j]

def create_rand_answers(n):
    with open('research/answers.md', 'r') as f:
        lines = f.read().split('\n')

    qs_idxs = []
    for idx, l in enumerate(lines):
        if l[:2] == "1.":
            qs_idxs.append(idx)

    lens = []
    new_qs = []
    new_as = []
    for _ in range(n):
        rand_idx = np.random.randint(len(qs_idxs))
        while rand_idx in lens or not_valid(qs_idxs[rand_idx], lines) or rand_idx in history_rand:
            rand_idx = np.random.randint(len(qs_idxs))
        lens.append(rand_idx)


        # new_qs.append()
        new_qs.append(lines[qs_idxs[rand_idx]] + ' _(' + get_title(qs_idxs[rand_idx], lines)[2:] + ')_  ')
        new_as.append(lines[qs_idxs[rand_idx]])
        for i in range(qs_idxs[rand_idx]+1, len(lines)):
            if ": hidden" in lines[i]:
                continue
            if "1." == lines[i][:2] or "***" == lines[i] or "# " in lines[i][:2]:
                break
            if "1." not in lines[i] or "blue" not in lines[i]:
                new_as.append(lines[i])
            if "button" in lines[i]:
                new_qs.append("__HIDDEN__<br>")
            if "1." in lines[i] and "blue" in lines[i]:
                new_qs.append(lines[i])
                new_as.append(lines[i])

    with open('research/history_rand.txt', 'a') as f:
        for l in lens:
            f.write('' + str(l) + '\n')

    with open('research/answers_today.md', 'w') as f:
        for l in lines[:6]:
            if "permalink" in l:
                f.write(l + "_today" + '\n')
            else:
                f.write(l + '\n')

        f.write('\n\n')

        for l in new_as:
            f.write(l + '\n')

    with open('research/questions_today.md', 'w') as f:
        for l in lines[:6]:
            if "permalink" in l:
                f.write(l[:-7] + "prep_qs_today" + '\n')
            else:
                f.write(l + '\n')

        f.write('\n\n')

        for l in new_qs:
            f.write(l + '\n')



# title = create_answers()
# create_questions(title)

# with open('research/questions_today.md', 'a') as f:
#     f.write('\n')
# with open('research/answers_today.md', 'a') as f:
#     f.write('\n')
# with open('research/questions_today.md', 'a') as f:
#     f.write('\n')
# with open('research/answers_today.md', 'a') as f:
#     f.write('\n')

create_rand_answers(n=3)