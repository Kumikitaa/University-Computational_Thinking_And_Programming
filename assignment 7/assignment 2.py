def delete(old_list):
    new_list = []
    for word in old_list:
        if word in new_list:
            continue
        new_list.append(word)
    return new_list

fhand = open("romeo.txt", "r")

new_list = []
lines = fhand.read().split()
new_list.extend(lines)
new_list = delete(new_list)
print(sorted(new_list))