import re

def intention_dbs():
    dbs=[
        
        {
            "reg": "^(start)$",
            "key": "handle_start",
            "default": None,
            "dics": None,
        },
        # ---------------help--------------
        {
            "reg": "^(help)$",
            "key": "handle_help",
            "default": None,
            "dics": None,
        },
        {
            "reg": "^(how to)?(withdraw)[ ]?([a-zA-Z0-9\-]{2,16})?$",
            "key": "handle_withdraw_help",
            "default": None,
            "dics": None,
        },
        {
            "reg": "^(deposit)$",
            "key": "handle_deposit_help",
            "default": None,
            "dics": None,
        },
        {
            "reg": "^(wallet|wallet list)$",
            "key": "handle_wallet_list",
            "default": None,
            "dics": None,
        },
        {
            "reg": "^(help)[ ]?(price|deposit|withdraw|tip|rain|password|pair|swap|bind_mobile|verify_mobile|switch_wallet)$",
            "key": "handle_help",
            "default": None,
            "dics": [{
                "reg": "^(help)[ ]?(price|deposit|withdraw|tip|rain|password|pair|swap|bind_mobile|verify_mobile|switch_wallet)$",
                "is_read_keys": True,
                "slot_keys": [
                    {"field": "fix", "default": None},
                    {"field": "help", "default": None}
                ],
                "key": "handle_help",
                "keys": [
                    {"name": "price", "key": "handle_price_help"},
                    {"name": "deposit", "key": "handle_deposit_help"},
                    {"name": "withdraw", "key": "handle_withdraw_help"},
                    {"name": "tip", "key": "handle_tip_help"},
                    {"name": "rain", "key": "handle_rain_help"},
                    {"name": "password", "key": "handle_password_help"},
                    {"name": "pair", "key": "handle_swap_pair_help"},
                    {"name": "swap", "key": "handle_swap_help"},
                    {"name": "bind_mobile", "key": "handle_bind_mobile_help"},
                    {"name": "verify_mobile", "key": "handle_verify_mobile_help"},
                    {"name": "switch_wallet", "key": "handle_switch_wallet_help"},
                ],
            }]
        },
        {
            "reg": "^(help)?[ ]?(price|deposit|withdraw|tip|password|pair|swap|bind_mobile|verify_mobile|switch_wallet)$",
            "key": "handle_help",
            "default": None,
            "dics": [{
                "reg": "^(help)?[ ]?(price|deposit|withdraw|tip|password|pair|swap|bind_mobile|verify_mobile|switch_wallet)$",
                "is_read_keys": True,
                "slot_keys": [
                    {"field": "fix", "default": None},
                    {"field": "help", "default": None}
                ],
                "key": "handle_help",
                "keys": [
                    {"name": "price", "key": "handle_price_help"},
                    {"name": "deposit", "key": "handle_deposit_help"},
                    {"name": "withdraw", "key": "handle_withdraw_help"},
                    {"name": "tip", "key": "handle_tip_help"},
                    {"name": "password", "key": "handle_password_help"},
                    {"name": "pair", "key": "handle_swap_pair_help"},
                    {"name": "swap", "key": "handle_swap_help"},
                    {"name": "bind_mobile", "key": "handle_bind_mobile_help"},
                    {"name": "verify_mobile", "key": "handle_verify_mobile_help"},
                    {"name": "switch_wallet", "key": "handle_switch_wallet_help"},
                ],
            }]
        },
        # ------------balance-------------
        {
            "reg": "^(balance)[ ]?([a-zA-Z0-9\-]{2,16})?$",
            "key": "handle_balance",
            "default": None,
            "dics": [{
                "reg": "^(balance)[ ]?([a-zA-Z0-9\-]{2,16})?$",
                "slot_keys": [
                    {"field": "fix", "default": None},
                    {"field": "coin", "default": None}
                ],
                "key": "handle_balance",
                "is_read_keys": False,
                "keys": []
            }],
        },
        {
            "reg": "^(check)*[ ]?([a-zA-Z0-9\-]{2,16})?[ ]?(balance)$",
            "key": "handle_balance",
            "default": None,
            "dics": [{
                "reg": "^(check)*[ ]?([a-zA-Z0-9\-]{2,16})?[ ]?(balance)$",
                "slot_keys": [
                    {"field": "fix", "default": None},
                    {"field": "coin", "default": None},
                    {"field": "action", "default": None}
                ],
                "key": "handle_balance",
                "is_read_keys": False,
                "keys": []
            }],
        },
        # ---------------deposit---------------
        {
            "reg": "^(deposit)[ ]?([a-zA-Z0-9\-]{2,16})?$",
            "key": "handle_deposit",
            "default": None,
            "dics": [{
                "reg": "^(deposit)[ ]?([a-zA-Z0-9\-]{2,16})?$",
                "slot_keys": [
                    {"field": "will", "default": None},
                    {"field": "fix", "default": None},
                    {"field": "coin", "default": "IFT"}
                ],
                "key": "handle_deposit",
                "is_read_keys": False,
                "keys": []
            }],
        },
        # --------------withdraw-------------
        {
            "reg": "^(withdraw)[ ]?",
            "key": None,
            "default": None,
            "dics": [{
                "reg": "^(withdraw)[ ]?([a-zA-Z0-9\-]{2,16})$",
                "slot_keys": [],
                "key": "handle_withdraw_help",
                "is_read_keys": False,
                "keys": []
                }, {
                "reg": "^(withdraw)[ ]?([+-]?\d+[\.\d]*)[ ]?([a-zA-Z0-9\-]{2,16})?[ ]+([a-zA-Z0-9:]{30,66})[ ]+([a-z0-9A-Z]{1,30})?$",
                "slot_keys": [
                    {"field": "will", "default": None},
                    {"field": "fix", "default": None},
                    {"field": "amount", "default": None},
                    {"field": "coin", "default": None},
                    {"field": "address", "default": None},
                    {"field": "memo", "default": None},
                ],
                "key": "handle_withdraw",
                "is_read_keys": False,
                "keys": []
            },
            {
                "reg": "^(withdraw)[ ]?(\d+[\.\d]*)[ ]?([a-zA-Z0-9\-]{2,16})[ ]?[到|到地址|to]?[ ]+([a-zA-Z0-9:]{30,66})[ ]?(memo|MEMO)?[ ]?([a-z0-9A-Z]{1,30})?$",
                "slot_keys": [
                    {"field": "will", "default": None},
                    {"field": "fix", "default": None},
                    {"field": "amount", "default": None},
                    {"field": "coin", "default": None},
                    {"field": "address", "default": None},
                    {"field": "memo_title", "default": None},
                    {"field": "memo", "default": None}
                ],
                "key": "handle_withdraw",
                "is_read_keys": False,
                "keys": []
            }]
        },
        # --------------tip-------------
        {
            "reg": "^(tip|\+)[ ]?[\w\W]+",
            "key": None,
            "default": None,
            "dics": [
                {
                    "reg": "^(tip|\+)[ ]?([+-]?\d+[\.\d]*)?[ ]?([a-zA-Z0-9\-]{2,16})?[ ]*$",
                    "slot_keys": [
                        {"field": "fix", "default": None},
                        {"field": "amount", "default": 1},
                        {"field": "coin", "default": 'IFT'},
                    ],
                    "key": "handle_reply_tip",
                    "is_read_keys": False,
                    "keys": []
                },
                {
                    "reg": "^(tip)[ ]?[@]?((?<!\ \d)[\w\W]*?)[ ]?([+-]?\d+[\.\d]*)?[ ]?([a-zA-Z0-9\-]{2,16})?[ ]*$",
                    "slot_keys": [
                        {"field": "fix", "default": None},
                        {"field": "users", "default": None},
                        {"field": "amount", "default": None},
                        {"field": "coin", "default": 'IFT'},
                    ],
                    "key": "handle_tip",
                    "is_read_keys": False,
                    "keys": []
                }
            ],
        },
        # --------------password-------------
        {
            "reg": "^(password)[\w\W]+",
            "key": None,
            "default": None,
            "dics": [{
                "reg": "^(password)[ ]*(\d+)?[ ]*(people| )?[ ]?([+-]?\d+[\.\d]*)?[ ]?([a-zA-Z0-9\-]{2,16})?[ ]?[#]([\w\W]+)$",
                "slot_keys": [
                    {"field": "fix", "default": None},
                    {"field": "share", "default": None},
                    {"field": "share_name", "default": None},
                    {"field": "amount", "default": None},
                    {"field": "coin", "default": 'IFT'},
                    {"field": "password", "default": None},
                ],
                "key": "handle_password_red_packet",
                "is_read_keys": False,
                "keys": []
            }],
        },
        # --------------normal red packets-------------
        """
        {
            "reg": "^(红包|发红包|红包雨|红包暴雨|airdrop|rain|storm)[\w\W]*",
            "key": None,
            "default": None,
            "dics": [{
                "reg": "^(红包|发红包|红包雨|红包暴雨|airdrop|rain|storm)[ ]?(\d+)?[ ]?(个|people|share| )?[ ]?(共|总共|总额|total)?[ ]?([+-]?\d+[\.\d]*)?[ ]?([a-zA-Z0-9\-]{2,16})?[ ]?$",
                "slot_keys": [
                    {"field": "fix", "default": None},
                    {"field": "share", "default": 5},
                    {"field": "share_name", "default": None},
                    {"field": "total_name", "default": None},
                    {"field": "amount", "default": 10},
                    {"field": "coin", "default": 'IFT'},
                ],
                "key": "handle_rain",
                "is_read_keys": False,
                "keys": []
            }],
        },
        
        # --------------Grab-------------
        {
            "reg": "^#[\w\W]*$",
            "key": None,
            "default": None,
            "dics": [{
                "reg": "^#([\w\W]*)$",
                "slot_keys": [
                    {"field": "password", "default": None},
                ],
                "key": "handle_grab",
                "is_read_keys": False,
                "keys": []
            }]
        },
        {
            "reg": "^(Grab|grab|Claim|claim|Airdrop|airdrop)$",
            "key": None,
            "default": None,
            "dics": [{
                "reg": "^(Grab|grab|Claim|claim|Airdrop|airdrop)$",
                "slot_keys": [
                    {"field": "password", "default": None},
                ],
                "key": "handle_grab",
                "is_read_keys": False,
                "keys": []
            }]
        },
        # --------------coin lore-------------
        {
            "reg": "^[=＝]([a-zA-Z0-9\-]{2,16})$",
            "key": "handle_coin_lore",
            "default": None,
            "dics": [{
                "reg": "^[=＝]([a-zA-Z0-9\-]{2,16})$",
                "slot_keys": [
                    {"field": "symbol", "default": None}
                ],
                "key": "handle_coin_lore",
                "is_read_keys": False,
                "keys": []
            }],
        },
        """
        # --------------last: price-------------
        {
            "reg": "^(Latest price)[ ]?([a-zA-Z0-9\-]{2,16})$",
            "key": "handle_price",
            "default": None,
            "dics": [{
                "reg": "^(Latest price)[ ]?([a-zA-Z0-9\-]{2,16})$",
                "slot_keys": [
                    {"field": "fix", "default": None},
                    {"field": "coin", "default": None},
                ],
                "key": "handle_price",
                "is_read_keys": False,
                "keys": []
            }],
        },
        {
            "reg": "^[\$]([a-zA-Z0-9\-]{2,16})$",
            "key": "handle_price",
            "default": None,
            "dics": [{
                "reg": "^[\$]([a-zA-Z0-9\-]{2,16})$",
                "slot_keys": [
                    {"field": "coin", "default": None}
                ],
                "key": "handle_price",
                "is_read_keys": False,
                "keys": []
            }],
        }
    ]
    return dbs


def parse_msg(msg):
    '''
    Parse User Message
    '''
    datas = {}
    ret = {"datas": None, "key": None}

    records = intention_dbs()
    for record in records:
        if not re.match(r''+record['reg'], msg, re.IGNORECASE):
            continue

        if not record["dics"]:
            ret["datas"] = record["default"]
            ret["key"] = record["key"]
            return ret

        ret["key"] = record["key"]
        for dic in record["dics"]:
            r = re.match(r''+dic['reg'], msg)
            if not r:
                continue

            items = r.groups()
            items_len = len(items)

            if not dic['slot_keys']: # no parameters
                ret["key"] = dic["key"]
                break  # if match, break

            slot_keys_len = len(dic['slot_keys'])
            if slot_keys_len != items_len:
                continue

            ret["key"] = dic["key"]
            if dic["is_read_keys"]:
                for s_key in dic["keys"]:
                    if s_key["name"] == items[1]:
                        ret["key"] = s_key["key"]
            else:
                for i in range(items_len):
                    slot_key_item = dic['slot_keys'][i]
                    datas[slot_key_item["field"]] = items[i] if items[i] else slot_key_item['default']
                ret["datas"] = datas

            return ret

        return ret

    return ret
