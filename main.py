
if __name__ == '__main__':
    # from dao.data_extract import extract_item
    #
    # _data = extract_item()
    #
    # print(_data)
    from gvmd.task_manager import Task
    #_resp = Task().create_task_and_runnow()
    # print(_resp)

    print(Task().get_all_tasks_info())
