# SATLite Tool
Tests the proper deployment of different kernals (Amber, Coco, Gromacs, LSDmap) on the remote machine (Stampede)

# Code sample
## To create SATLite handler:
test = SATLite()

## To set attributes:
test.set_attribute( 
		    name = name_of_kernel,
	
		    resource = name_of_target machine,
	
		    arguments = input_arguments_files,
	
		    exe = executable_optional,
	
		    modules = modules_optional,
		    
		    runtime = [min_time, max_time](optional, hh:mm:ss))

## To execute the test:
test.run()


	
