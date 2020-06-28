def inter_section_arrays(a1, a2):
    out_come = list(filter(lambda z: z in a1, a2))
    print("Intersection of two arrays: ", out_come)

a1 = [2, 3, 4, 6, 8, 10, 12]
a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if __name__ == "__main__":
    print("First array:", a1)
    print("Second array:", a2)
    inter_section_arrays(a1, a2)