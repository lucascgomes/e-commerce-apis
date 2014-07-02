from paypal.standard.ipn.signals import payment_was_successful

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # You need to check 'payment_status' of the IPN

    if ipn_obj.payment_status == "Completed":
        print "SUCESS AND COMPLETED"
        # # Undertake some action depending upon `ipn_obj`.
        # if ipn_obj.custom == "Upgrade all users!":
        #     Users.objects.update(paid=True)
    else:
        print "SUCESS AND NOT NOT NOT COMPLETED"

payment_was_successful.connect(show_me_the_money)
