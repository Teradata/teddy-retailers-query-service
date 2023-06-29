'''
def get_discount(tlv,unix_timestamp_last_order):
    print(is_current_customer(unix_timestamp_last_order))
    if is_current_customer(unix_timestamp_last_order):
        if tlv >= 1500:
            return 10
        elif tlv >= 100:
            return 5
        else:
            return 0
    else:
        return 0
'''