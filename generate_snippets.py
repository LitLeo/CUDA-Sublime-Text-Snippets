import os
import string
import re
# encoding=utf8

# Device_Management
# Error_Handling
# Event_Management
# Execution_Control
# Memory_Management
# Occupancy
# Peer_Device_Memory_Access
# Stream_Management
# Thread_Management
# Unified_Addressing


dirs=[
'CUDA_Runtime_API/Device_Management/',
'CUDA_Runtime_API/Error_Handling/',
'CUDA_Runtime_API/Event_Management/',
'CUDA_Runtime_API/Execution_Control/',
'CUDA_Runtime_API/Memory_Management/',
'CUDA_Runtime_API/Occupancy/',
'CUDA_Runtime_API/Peer_Device_Memory_Access/',
'CUDA_Runtime_API/Stream_Management/',
'CUDA_Runtime_API/Unified_Addressing/'
]

filename='func'
for dir in dirs:
	# print d
	file_buffer = open(dir + filename)
	print 'open '+dir+filename

	# delete all files
	for f in os.listdir(dir):
		if f.find('snippet') != -1:
			os.remove(dir + f)
	# exit()

	alllines = file_buffer.readlines()
	for line in alllines:
		if line.find('__host__') != -1:
			# print line
			reResult = re.search('(__.*__) (.*_t) (.*) \( (.*) \)', line, re.U)
			if reResult:
				Zuoyongyu = reResult.group(1)
				Return = reResult.group(2)
				Funname = reResult.group(3)
				Params = reResult.group(4)

				NewParams = ''
				Params_split = Params.split(', ')
				# print len(Params_split)
				# cudaChooseDevice(${1:int* device}, ${2:const cudaDeviceProp* prop})
				for x in xrange(0,len(Params_split)):
					Params_split[x].strip()
					Params_split[x].replace('  ', ' ')

				for x in xrange(0,len(Params_split) - 1):
					NewParams += '${' + str(x) + ':' + Params_split[x] + '}, '
				NewParams += '${' + str(len(Params_split) - 1) + ':' + Params_split[len(Params_split) - 1] + '}'
				# print NewParams
				out_buffer = open(dir+Funname + '.sublime-snippet', 'w')
				out_buffer.write('<snippet> \n\
	<content><![CDATA[\n' + 
Funname + '(' + NewParams + ')' +
'\n]]></content> \n\
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet --> \n\
	<tabTrigger>'+ Funname +'</tabTrigger> \n\
	<!-- Optional: Set a scope to limit where the snippet will trigger --> \n\
	<scope>source.cuda-c++</scope> \n\
</snippet>')

				out_buffer.close()
			# exit()

	file_buffer.close()

