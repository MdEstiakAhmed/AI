def sorting(m):
	map_value_count = {}
	map_key = list(map.keys())

	for i in map_key:
		map_value_count.update({i:len(map[i])})

	x = sorted(map_value_count.items(), key = lambda kv:(kv[1], kv[0]))
	return x

map = {
	'WA':['NT', 'SA'], 
	'NT':['WA', 'SA', 'Q'], 
	'SA':['WA', 'NT', 'Q', 'NSW', 'V'], 
	'Q':['NT', 'SA', 'NSW'], 
	'NSW':['Q', 'V', 'SA'], 
	'V':['SA', 'NSW'], 
	'T':[]
}


new_sort = sorting(map)
print(new_sort)