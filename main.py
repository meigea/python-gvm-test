def test_task():
    from localtool.task_manager import Task
    # _data = Task(hosts="192.168.2.1-192.168.2.100").create_task()
    # _resp = Task(hosts="192.168.2.1-192.168.2.100").create_task_and_runnow()
    # print(_resp)

    print("===========RUN==================")
    print( Task().get_task_info() )


def test_report():
    from localtool.report_manager import Report
    # Report().find_rw()


if __name__ == '__main__':
    test_task()
