>>>import os

>>> def function(dir_path=None,dots=4):
	  	if dir_path==None:
			dir_path=raw_input("enter the directory :")
		        dir_path='/'+dir_path.replace("/","")
	  	if os.path.isdir(dir_path):
		  	for f_name in os.listdir(dir_path):
			  	new_path=os.path.join(dir_path,f_name)
			  	if os.path.isdir(new_path):
			   		print '.'*dots,f_name,'/'
				  	function(new_path,dots+4)
			  	else:
				  	print '.'*dots,f_name
	  	else:
	  		print "enter a valid diretory"

			
>>> function() #Calling the function
enter the directory :dev/ #Sample output
#The list will be displayed
