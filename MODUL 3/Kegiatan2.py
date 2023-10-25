data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

output_data = []

for item in data:
    data_split = item.split()
    filtered_data = list(filter(lambda x: x.isdigit(), data_split))
    output_data.append(filtered_data)

if __name__ == '__main__':
    for item in output_data:
        print(item)
