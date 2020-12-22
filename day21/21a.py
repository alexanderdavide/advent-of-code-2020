def get_all_allergens(dish):
    return [allergen.strip() for allergen in dish.split("contains ")[1][:-1].split(",")]


def get_all_ingredients(lines):
    all_ingredients = []
    for recipe in lines:
        for ingredient in recipe.split("(")[0].strip().split(" "):
            all_ingredients.append(ingredient)
    return all_ingredients


def get_dishes_by_ingredient(lines):
    allergen_dishes = {}
    for dish in lines:
        all_ingredients = get_all_ingredients([dish])
        all_allergens = get_all_allergens(dish)
        for a in all_allergens:
            allergen_dishes.setdefault(a, []).append(all_ingredients)
    return allergen_dishes


def get_true_allergens(dishes_by_allergen):
    suspects = {}
    true_allergens = []
    for allergen, dishes in dishes_by_allergen.items():
        if allergen not in suspects:
            suspects[allergen] = []
        for dish in dishes:
            for ingredient in dish:
                suspects[allergen].append(ingredient)
        for allergen, sus in suspects.items():
            for s in sus:
                if sus.count(s) == len(dishes_by_allergen[allergen]):
                    true_allergens.append(s)
    return set(true_allergens)


def main():
    with open("21.txt") as input:
        lines = [line.strip() for line in input.readlines()]
        all_ingredients = get_all_ingredients(lines)
        t = get_dishes_by_ingredient(lines)
        ta = get_true_allergens(t)
        na = [x for x in all_ingredients if x not in ta]
        print(sum([1 for x in all_ingredients if x in na]))
    return 0


if __name__ == "__main__":
    exit(main())