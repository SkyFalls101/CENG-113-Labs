def load_cities_from_file(filename):
    
    cities = {}

    with open(filename, "r") as file:
        for lines in file:
            words = lines.strip().split(",")
            words[4] = set(words[4].split(";"))
            
            tags_dictionary = {}

            tags_dictionary.update({"name": words[1], "country": words[2], "population": words[3], "tags": words[4]})
            
            cities[words[0]] = tags_dictionary

        return cities

def add_city(cities, city_id, name, country, population): 
    tags = set()
    if city_id in cities:
        print("Warning: city id already exists")
    else:
        temp_dictionary = {

        "name" : name,
        "country" : country,
        "population" : population,
        "tags" : tags

        }

        cities[city_id] = temp_dictionary

def remove_city(cities, city_id):
    if city_id not in cities:
        print("Warning: city id does not exist")
    else:
        del cities[city_id]

def add_tag(cities, city_id, tag):
    if city_id not in cities:
        print("Warning: city id does not exist")
    else:
        cities[city_id]["tags"].add(tag)

def remove_tag(cities, city_id, tag):
    if city_id not in cities:
        print("Warning: city id does not exist")
    else:
        if tag not in cities[city_id]["tags"]:
            print("Warning: tag does not exist")
        else:
            cities[city_id]["tags"].remove(tag)

def print_cities(cities):
    print("CityID     |Name                  |Country               |Population    |Tags")
    print("------------------------------------------------------------------------------------------------")
    for city_id, city_data in cities.items():
        tags = list(city_data["tags"])
        tag_string = ""
        for i in tags:
            tag_string += f"{i}, "
        tag_string = tag_string[:len(tag_string)-2]
        print(f"{city_id:<10} | {city_data['name']:<20} | {city_data['country']:<20} | {city_data['population']:<12} | {tag_string}")

def linear_search_iterative(city_ids, target_id):
    found = False
    for id in city_ids:
        if id == target_id:
            found = True
            return city_ids.index(id)
    return -1

def linear_search_recursive(city_ids, target_id, index=0):
    if index == len(city_ids):
        return -1
    if target_id == city_ids[index]:
        return index
    else:
        return linear_search_recursive(city_ids, target_id, index+1)

def binary_search_iterative(city_ids, target_id):
    left = 0
    right = len(city_ids) - 1

    while left <= right:
        middle = (left + right) // 2 
        guess = city_ids[middle]

        if guess == target_id:
            return middle
        if guess > target_id:
            right = middle - 1 
        else:
            left = middle + 1 

    return -1

def binary_search_recursive(city_ids, target_id, left, right):
    if right is None:
        right = len(city_ids) - 1

    if left > right:
        return -1

    middle = (left + right) // 2
    guess = city_ids[middle]

    if guess == target_id:
        return middle
    
    if guess > target_id:
        return binary_search_recursive(city_ids, target_id, left, middle - 1)
    else:
        return binary_search_recursive(city_ids, target_id, middle + 1, right)

def main():

    try:
        cities = load_cities_from_file("cities.txt")
        print_cities(cities)

        add_city(cities, "1100", "Moscow", "Russia", 3.6)
        remove_city(cities, "1008")
        print_cities(cities)

        add_tag(cities, "1100", "Cold")
        remove_tag(cities, "1007", "parks")
        print_cities(cities)


        cityids = []
        for ids in cities:
            cityids.append(ids)

        print(linear_search_iterative(cityids, "1001"))
        print(linear_search_recursive(cityids, "1007"))
        print(binary_search_iterative(cityids, "1200"))
        print(binary_search_recursive(cityids, "1100", 0, 9))
    except Exception as e:
        print("Please check the file directory", e)

main()