#2. Đọc file input cho các bản đồ không có cổng dịch chuyển
def read_file (file_name):
	with open(file_name, 'r') as f:

		#___đọc số lượng điểm thưởng
		n_bonus = int(next(f)[:-1])  # next(f) trỏ tới phần tử tiếp theo, [:-1] cắt bỏ \n  
		bonus = []   #tạo mảng điểm thưởng
		for i in range(n_bonus):
			x, y, point = map(int,next(f)[:-1].split(' '))
			bonus.append((x,y,point))

		#___đọc mê cung
		text = f.read()
		maze = [list(i) for i in text.splitlines()]  
		#chia 1 chuỗi thành list, thực hiện tại ngắt dòng
		#list(i) lấy từng phần tử của list splitlines thành từng list riêng

	return bonus, maze

# Đọc file input của các bản đồ có cổng dịch chuyển
def read_file_2(file_name):
	with open(file_name, 'r') as f:
		#___đọc số lượng điểm dịch chuyển 
		n_teleportations = int(next(f)[:-1])  # next(f) trỏ tới phần tử tiếp theo, [:-1] cắt bỏ \n  
		teleportations = {}   #tạo dictionary các cổng dịch chuyển
		for i in range(n_teleportations):
			x, y, x2, y2 = map(int,next(f)[:-1].split(' '))
			teleportations[(x, y)] = (x2, y2)

		#___đọc mê cung
		text = f.read()
		maze = [list(i) for i in text.splitlines()]  
		#chia 1 chuỗi thành list, thực hiện tại ngắt dòng
		#list(i) lấy từng phần tử của list splitlines thành từng list riêng

	return teleportations, maze