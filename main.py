def test_task():
    from localtool.task_manager import Task
    #_resp = Task().create_task_and_runnow()
    #print(_resp)
    #print("===========RUN==================")
    print( Task().get_task_info() )


def test_report():
    from localtool.report_manager import Report
    # Report().find_rw()

def test_infos():
    pass


if __name__ == '__main__':
    # test_task()

    test_infos()


