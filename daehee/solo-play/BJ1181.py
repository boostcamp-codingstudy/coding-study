for e in sorted(set(open(0).read().split()),key=lambda e:(len(e),e)):
    if not e.isnumeric():print(e)