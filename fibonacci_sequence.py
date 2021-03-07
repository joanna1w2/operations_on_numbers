#======================================================
#    functions
#======================================================

"""
creates a list of fibonacci numbers and writes that list into a file
  in  : n - amount of numbers you want to calculate
  out : ls - fibonacci sequence
"""

def fibo_sequence(n):
  
	ls = [1 , 2]
	i = 0
	
	for i in range(0,n):
		add_next_element = ls[i] + ls[i+1]
		ls.append(add_next_element)

	
	return ls


#======================================================
#    main program
#======================================================


N = 20

lcf = licz_ciag_fibo(N)
print "lcf = " , lcf 

# turn function output into a string
s = str(lcf)


# create a file and write function output into it
file_name = "ciag_fibo.txt"

f = open( file_name, 'wb' )

f.write("Zapis informacji do pliku")
f.write("\n")
f.write(s)

f.close()


#======================================================
#    end
#======================================================
