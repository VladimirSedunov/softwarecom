from datetime import datetime


def test_time():
    # if you encounter a "year is out of range" error the timestamp
    # may be in milliseconds, try `ts /= 1000` in that case

    from datetime import datetime

    print()
    ts = int('1678968490036') / 1000
    print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

    ts = int('1679391260446') / 1000
    print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
