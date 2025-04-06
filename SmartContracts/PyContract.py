 # অ্যাকাউন্ট কন্ট্রাক্টের উদাহরণ (সরলীকৃত)
@contract
class MyAccount:
    func __init__(public_key: felt):
        self.public_key = public_key  # আপনার পাবলিক কী সেভ করে

    func execute_tx(tx_details):
        verify_signature(tx_details)  # সিগনেচার চেক করে
        run_transaction(tx_details)  # ট্রানজেকশন এক্সিকিউট করে
