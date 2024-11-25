my_dict={'sanu':20,'devika':22,'sandra':23,'anu':24}
sorted_by_key_asc=dict(sorted(my_dict.items()))
sorted_by_key_desc=dict(sorted(my_dict.items(),reverse=True))
print("sorted keys(ascending):",sorted_by_key_asc)
print("sorted keys(descending):",sorted_by_key_desc)
