def main():
    filename = "wimbledon.csv"
    wimbledon_datas = get_wimbledon_datas(filename)
    champion_to_count = get_champion_to_count(wimbledon_datas)
    country_set = get_country_set(wimbledon_datas)
    countries = list(country_set)
    countries.sort()
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(",".join(countries))
    # print(champion_to_count)
    # print(countries)


def get_wimbledon_datas(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        wimbledon_datas = in_file.readlines()
    del (wimbledon_datas[0])
    return wimbledon_datas


def get_champion_to_count(wimbledon_datas):
    champion_to_count = {}
    for line in wimbledon_datas:
        champion_name = line.split(",")[2]
        if champion_name in champion_to_count.keys():
            champion_to_count[champion_name] += 1
        else:
            champion_to_count[champion_name] = 1
    return champion_to_count


def get_country_set(wimbledon_datas):
    country_set = set()
    for line in wimbledon_datas:
        country_set.add(line.split(",")[1])
    return country_set


main()
