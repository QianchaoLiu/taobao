# encoding=utf-8

# buyer_list = []
# parent = []
# trade = []
# with open('/Volumes/Eden/pad/pad2/Tmp_cl_yw_append_trade0606.csv') as f:
#     # auction_id	spu_id	seller_id	trade_id	winner_id	gmt_receive_pay	parent_id	level1	total_fee	bid	ID	quantity	brand	auction_title
#     for i, line in enumerate(f):
#         if i > 0:
#             seq_line = line.split(',')
#             buyer_id = seq_line[4]
#             seller_id = seq_line[2]
#             parent_id = seq_line[6]
#             trade_id = seq_line[3]
#
#             trade.append(trade_id)
#             parent.append(parent_id)
#             buyer_list.append(buyer_id)
#
# print len(buyer_list)
# print len(set(buyer_list))
#
# print 'parent:'
# print len(parent)
# print len(set(parent))
#
# print 'trade:'
# print len(trade)
# print len(set(trade))


with open('/Volumes/Eden/pad/pad3/tmp_cl_yw_ww_all.csv') as f:
    for i, line in enumerate(f):
        if i<10:
            print line.decode('gbk')
