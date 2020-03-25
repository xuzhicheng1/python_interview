def get_max_score(dest_list, hand_list):
    if max(hand_list)<=min(dest_list):
        return (hand_list,0)
    print(f"dest_list is {dest_list}")
    length = len(dest_list)
    res = length * [0]
    count_dict = {}
    hand_list.sort(reverse=True)
    # hand_list.reverse()
    print(f"hand_list is {hand_list}")
    for i in range(length):
        for j in range(length):
            if dest_list[i] < hand_list[j]:
                if count_dict.get(i):
                    count_dict[i] += 1
                else:
                    count_dict[i] = 1
            else:
                continue
    print(f"count_dict is {count_dict}")
    temp = [x[0] for x in sorted(count_dict.items(), key=lambda x: x[1])]
    # temp.reverse()
    print(f"temp is {temp}")

    for i in range(len(temp)):
        res[temp[i]] = hand_list[i]

    # print(f"i is {i}")
    for k in range(length):
        if not res[k]:
            i = i + 1
            res[k] = hand_list[i]
    # print(res)
    return (res, len(temp))


if __name__ == "__main__":
    print(get_max_score([3, 2, 1], [3, 2, 1]))
