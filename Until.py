def countdown():
    for i in range(1, 10):
        print("Counting:", i)
        if i == 5:
            import pdb; pdb.set_trace()  # Set a breakpoint here

countdown()

