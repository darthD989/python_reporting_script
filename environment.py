import sys
k8s_namespace = sys.argv[1] 
environment = k8s_namespace.split('-') 
environment = environment[1]
print(environment)
