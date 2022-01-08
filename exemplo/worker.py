import time

def runTask(group_owner, group_description):
    print('[STARTING] run_task')
    time.sleep(5)
    print('[DONE] run_task')
    
    return {"group_name": group_owner, "group_description": group_description}