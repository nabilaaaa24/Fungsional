random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

def check_type(item):
    if isinstance(item, float):
        return True
    elif isinstance(item, int):
        return True
    elif isinstance(item, str):
        return True
    else:
        return False

# Menggunakan filter() untuk memisahkan nilai float, int, string
filtered_list = filter(check_type, random_list)

def process_data(item):
    if isinstance(item, float):
        return item
    elif isinstance(item, int):
        ratusan = item // 100
        puluhan = (item % 100) // 10
        satuan = item % 10
        return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}
    elif isinstance(item, str):
        return item.upper()

# Menggunakan map() untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
processed_data = list(map(process_data, filtered_list))

float_data = tuple(filter(lambda x: isinstance(x, float), processed_data))
int_data = [data for data in processed_data if isinstance(data, dict)]
str_data = list(filter(lambda x: isinstance(x, str), processed_data))

if __name__ == '__main__':
    print(f"Data Float : {float_data}")
    print("Data Int :")
    for data in int_data:
        print(data)
    print(f"Data String : {str_data}")
