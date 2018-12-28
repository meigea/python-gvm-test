
if __name__ == '__main__':
    from dao.data_extract import extract_item
    # apscheduler 重复调用这个接口就可以写入当前得报告到数据库
    _data = extract_item()
    print(_data)
    from gvmd.task_manager import Task
    #_resp = Task().create_task_and_runnow()
    # print(_resp)
	########## 打印当前正在运行得任务情况
    # print(Task().get_the_lattest_running_task_info())
