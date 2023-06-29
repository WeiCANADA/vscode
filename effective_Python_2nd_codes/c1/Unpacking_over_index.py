snacks = [('bacon', 350), ('donut', 240), ('muffin', 190)]
for rank, (name, calories) in enumerate(snacks, 1):# (1, ('bacon', 350))
    print(f'#{rank}: {name} has {calories} calories')
