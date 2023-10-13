def square_matrix(square): 
	tot_sum = 0
	for i in range(3): 
		for j in range(3): 
			tot_sum += square[i][j] 
			
	return tot_sum // 9	  

def boxBlur(image): 
	square = []	 
	square_row = [] 	
	blur_row = [] 
	blur_img = []  
	n_rows = len(image) 
	n_col = len(image[0]) 
	rp, cp = 0, 0 
	while rp <= n_rows - 3: 
		while cp <= n_col-3: 
			for i in range(rp, rp + 3): 
				for j in range(cp, cp + 3): 
					square_row.append(image[i][j]) 
				square.append(square_row) 
				square_row = []  
			blur_row.append(square_matrix(square)) 
			square = []  
			cp = cp + 1 
		blur_img.append(blur_row) 
		blur_row = [] 
		rp = rp + 1  
		cp = 0 
	return blur_img 
		

l=[[36,0,18,9,9,45,27],
 [27,0,54,9,0,63,90],
 [81,63,72,45,18,27,0],
 [0,0,9,81,27,18,45],
 [45,45,27,27,90,81,72],
 [45,18,9,0,9,18,45],
 [27,81,36,63,63,72,81]]
print(boxBlur(l)) 