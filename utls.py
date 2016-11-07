# encoding=utf-8
import datetime

target_users = []

with open('/Users/liuqianchao/Desktop/taobao/tmp_cl_yw_ww_all.csv') as f:
    for i, line in enumerate(f):
        if i > 0:
            if i % 100000 == 0:
                print i
            seq_line = line.split(',')
            buyer_user_id = seq_line[8].strip('\r\n')
            target_users.append(buyer_user_id)
target_users = list(set(target_users))[:1001]
# select 1000 users who chatted with sellers
target_users.remove('')


# SECTION 1
ww_buyer_list = []  # 5147827 2065730
ww_buyer_info_dict = {}
with open('/Users/liuqianchao/Desktop/taobao/tmp_cl_yw_ww_all.csv') as f:
    for i, line in enumerate(f):
        if i > 0:
            if i % 100000 == 0:
                print i
            seq_line = line.split(',')
            seller_user_id = seq_line[3]
            #selerfirstresponse = datetime.datetime.strptime(seq_line[4], "%Y-%m-%d %H:%M:%S")
            selerfirstresponse = seq_line[4]
            seller_send_num = seq_line[5]
            buyerfirstsendtime = seq_line[6]
            sellerreceivednum = seq_line[7]
            buyer_user_id = seq_line[8].strip('\r\n')
            if buyer_user_id in target_users:
                ww_buyer_list.append(buyer_user_id)
                if buyer_user_id not in ww_buyer_info_dict.keys():
                    ww_buyer_info_dict[buyer_user_id] = [[seller_user_id, seller_send_num, sellerreceivednum, selerfirstresponse, buyerfirstsendtime]]
                else:
                    ww_buyer_info_dict[buyer_user_id].append([seller_user_id, seller_send_num, sellerreceivednum, selerfirstresponse, buyerfirstsendtime])

ww_buyer_list_set = set(ww_buyer_list)


# SECTION 2
buyer_list = []
parent = []
trade = []
trade_buyer_dict = {}
with open('/Users/liuqianchao/Desktop/taobao/Tmp_cl_yw_append_trade0606.csv') as f:
    # auction_id	spu_id	seller_id	trade_id	winner_id	gmt_receive_pay	parent_id	level1	total_fee	bid	ID	quantity	brand	auction_title
    for i, line in enumerate(f):
        if i > 0:
            if i%100000 ==0:
                print i
            seq_line = line.split(',')
            buyer_id = seq_line[4]
            if buyer_id in ww_buyer_list_set:
                seller_id = seq_line[2]
                parent_id = seq_line[6]
                trade_id = seq_line[3]
                gmt_receive_pay = seq_line[5]
                total_fee = seq_line[8]
                quantity = seq_line[11]
                trade.append(trade_id)
                parent.append(parent_id)
                buyer_list.append(buyer_id)
                if buyer_id not in trade_buyer_dict.keys():
                    trade_buyer_dict[buyer_id] = [[seller_id, gmt_receive_pay, quantity, total_fee]]
                else:
                    trade_buyer_dict[buyer_id].append([seller_id, gmt_receive_pay, quantity, total_fee])

pane = []
for buyer in set(ww_buyer_list):
    if buyer in trade_buyer_dict.keys():
        for ww in ww_buyer_info_dict[buyer]:
            seller = ww[0]
            if seller in str(trade_buyer_dict[buyer]):
                for trade in trade_buyer_dict[buyer]:
                    if seller in str(trade):
                        print [buyer], [seller], ww, '1'
                        pane.append([buyer] + ww + ['1'] + trade)
                        break
            else:
                print [buyer], [seller], ww, '0'
                pane.append([buyer] + ww + ['0'])
        # to_write.append([buyer] + [len(ww_buyer_info_dict[buyer])] + [len(trade_buyer_dict[buyer])] + ww_buyer_info_dict[buyer] + trade_buyer_dict[buyer])
    else:
        for ww in ww_buyer_info_dict[buyer]:
            seller = ww[0]
            print [buyer], [seller], ww, '0'
            pane.append([buyer] + ww + ['0'])
        # to_write.append([buyer] + [len(ww_buyer_info_dict[buyer])] + [0] + ww_buyer_info_dict[buyer])


with open('./dat/pane.csv','w') as wf:
    for line in pane:
        line = [str(item) for item in line]
        wf.write(','.join(line)+'\n')
