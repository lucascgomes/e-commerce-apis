from paypal.standard.ipn.signals import payment_was_flagged

def show_me_the_flag(sender, **kwargs):
    ipn_obj = sender
    # You need to check 'payment_status' of the IPN
    print str(ipn_obj.flag) + " --- " + str(ipn_obj.flag_info)

payment_was_flagged.connect(show_me_the_flag)
