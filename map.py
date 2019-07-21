def selection_sort(l, m):
   n = len(l)
   for i in range(0, n-1):
   	index_min = i
   	for j in range(i+1, n):
   		if l[j] < l[index_min]:
   			index_min = j
   	if index_min != i:
   		l[i], l[index_min] = l[index_min], l[i]
   		m[i], m[index_min] = m[index_min], m[i]

   return m

def sorted_by_value(m):
	map_value_count = {}
	map_key = list(map.keys())

	for i in map_key:
		map_value_count.update({i:len(map[i])})

	map_key = list(map_value_count.keys())
	map_value = list(map_value_count.values())

	sorted_map = selection_sort(map_value, map_key)

	return sorted_map


map = {
	'WA':['NT', 'SA'], 
	'NT':['WA', 'SA', 'Q'], 
	'SA':['WA', 'NT', 'Q', 'NSW', 'V'], 
	'Q':['NT', 'SA', 'NSW'], 
	'NSW':['Q', 'V', 'SA'], 
	'V':['SA', 'NSW'], 
	'T':[]
}


sort_map = sorted_by_value(map)
print(sort_map)

# new_map = []
# for i in sort_map:
# 	new_map.append([i,len(map[i])])
# print(new_map)
