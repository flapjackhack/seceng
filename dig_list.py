import subprocess

with open("subdomain.list","r") as fd:
    domain=fd.readlines()
for domain_name in domain:
    domain_name=domain_name.strip()
    cmd="dig txt %s"%(domain_name)
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,shell=True).communicate()[0]
    p_list=p.decode("utf-8").split("AUTHORITY SECTION")
    p_l_list=p_list[1].split("\n")
    result=p_l_list[1].split("\t")
    final_result=result[4].split(" ")
    print(domain_name)
    print(final_result)
