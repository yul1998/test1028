import pickle

# 定义文件路径
file_path = './data/nus-wide/clip_train.pkl'

# 使用pickle模块加载文件
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# 打印加载的数据
# print(data)
key_to_access = 'image'
if key_to_access in data:
    value = data[key_to_access]
    print(f"The value for '{key_to_access}' is: {value}")
    length = len(value)
    print(f"The length of the value for '{key_to_access}' is: {length}")
else:
    print(f"Key '{key_to_access}' not found in the file.")

# if isinstance(data, dict):
#     # 获取字典中键的数量
#     number_of_keys = len(data)
#     print(f"There are {number_of_keys} keys in the file.")
#     print("\nKeys and their values:")
#     # 遍历字典，打印每个键及其对应的值
#     for key, value in data.items():
#         print(f"Key: {key}, Value: {value}")
# else:
#     print("The loaded data is not a dictionary.")
# print(data)

key_to_access = 'text'
if key_to_access in data:
    value = data[key_to_access]
    print(f"The value for '{key_to_access}' is: {value}")
    length = len(value)
    print(f"The length of the value for '{key_to_access}' is: {length}")
else:
    print(f"Key '{key_to_access}' not found in the file.")