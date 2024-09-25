from examples.onboard.onboard_account import *


# script demonstrates basic network capabilities on encrypt/decrypt of values saved in a contract
def main():
    account_hex_encryption_key, eoa, eoa_private_key, web3 = init()

    gas_limit = 10000000
    gas_price_gwei = 30

    tx_params = {'web3': web3, 'gas_limit': gas_limit, 'gas_price_gwei': gas_price_gwei,
                 'eoa_private_key': eoa_private_key}
    deployed_contract = deploy(account_hex_encryption_key, eoa, tx_params)

    basic_get_value(deployed_contract, eoa, web3)
    a = basic_clear_encrypt_decrypt(account_hex_encryption_key, deployed_contract, eoa, tx_params)

    some_other_aes_key = generate_aes_key()
    basic_decryption_failure(some_other_aes_key, deployed_contract, eoa, tx_params)

    network_decryption_failure(account_hex_encryption_key, deployed_contract, eoa, tx_params)

    b = basic_encrypted_encrypt_decrypt(account_hex_encryption_key, deployed_contract, eoa,
                                        account_hex_encryption_key, tx_params)

    basic_string_encrypt_decrypt(account_hex_encryption_key, deployed_contract, eoa,
                                 account_hex_encryption_key, tx_params)

    basic_add_computation(deployed_contract, tx_params, eoa, account_hex_encryption_key, a + b)
    compute_add_with_different_account(eoa_private_key, gas_limit, gas_price_gwei, web3, deployed_contract, a + b)
    make_sure_data_is_safe(eoa, web3, deployed_contract, tx_params)


def make_sure_data_is_safe(eoa, web3, deployed_contract, tx_params):
    some_other_contract_keeping_data = {
        "contract_name": "DataOnChain",
        "address": "0xbC39Df62e41F69300a413d4F3a262737A1109FC3",
        "abi": [
            {
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "constructor"
            },
            {
            "anonymous": false,
            "inputs": [
                {
                "indexed": true,
                "internalType": "address",
                "name": "_from",
                "type": "address"
                },
                {
                "indexed": false,
                "internalType": "ctUint64[]",
                "name": "ctUserSomeEncryptedStringValue",
                "type": "uint256[]"
                }
            ],
            "name": "UserEncryptedStringValue",
            "type": "event"
            },
            {
            "anonymous": false,
            "inputs": [
                {
                "indexed": true,
                "internalType": "address",
                "name": "_from",
                "type": "address"
                },
                {
                "indexed": false,
                "internalType": "ctUint64",
                "name": "ctUserSomeEncryptedValue",
                "type": "uint256"
                }
            ],
            "name": "UserEncryptedValue",
            "type": "event"
            },
            {
            "inputs": [],
            "name": "add",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "getNetworkSomeEncryptedValue",
            "outputs": [
                {
                "internalType": "ctUint64",
                "name": "ctSomeEncryptedValue",
                "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "getNetworkSomeEncryptedValueEncryptedInput",
            "outputs": [
                {
                "internalType": "ctUint64",
                "name": "ctSomeEncryptedValue",
                "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "getSomeValue",
            "outputs": [
                {
                "internalType": "uint64",
                "name": "value",
                "type": "uint64"
                }
            ],
            "stateMutability": "view",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "getUserArithmeticResult",
            "outputs": [
                {
                "internalType": "ctUint64",
                "name": "value",
                "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "getUserSomeEncryptedStringEncryptedInput",
            "outputs": [
                {
                "internalType": "ctUint64[]",
                "name": "ctSomeEncryptedValue",
                "type": "uint256[]"
                }
            ],
            "stateMutability": "view",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "getUserSomeEncryptedValue",
            "outputs": [
                {
                "internalType": "ctUint64",
                "name": "ctSomeEncryptedValue",
                "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "getUserSomeEncryptedValueEncryptedInput",
            "outputs": [
                {
                "internalType": "ctUint64",
                "name": "ctSomeEncryptedValue",
                "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
            },
            {
            "inputs": [
                {
                "internalType": "ctUint64",
                "name": "networkEncrypted",
                "type": "uint256"
                }
            ],
            "name": "setNetworkSomeEncryptedValue",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
            },
            {
            "inputs": [
                {
                "internalType": "ctUint64[]",
                "name": "_itInputString",
                "type": "uint256[]"
                },
                {
                "internalType": "bytes[]",
                "name": "_itSignature",
                "type": "bytes[]"
                }
            ],
            "name": "setSomeEncryptedStringEncryptedInput",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
            },
            {
            "inputs": [
                {
                "internalType": "uint64",
                "name": "_value",
                "type": "uint64"
                }
            ],
            "name": "setSomeEncryptedValue",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
            },
            {
            "inputs": [
                {
                "internalType": "ctUint64",
                "name": "_itCT",
                "type": "uint256"
                },
                {
                "internalType": "bytes",
                "name": "_itSignature",
                "type": "bytes"
                }
            ],
            "name": "setSomeEncryptedValueEncryptedInput",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "setUserSomeEncryptedStringEncryptedInput",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "setUserSomeEncryptedValue",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
            },
            {
            "inputs": [],
            "name": "setUserSomeEncryptedValueEncryptedInput",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
            }
        ],
        "bytecode": "0x608060405234801561001057600080fd5b5060056000806101000a81548167ffffffffffffffff021916908367ffffffffffffffff160217905550611657806100496000396000f3fe608060405234801561001057600080fd5b50600436106100f55760003560e01c80638d7eadec11610097578063a40674b711610066578063a40674b714610202578063af384ac714610220578063d7c496011461023c578063fee511d61461025a576100f5565b80638d7eadec146101a05780639c82c7c7146101be5780639f3f69de146101da578063a2e12869146101e4576100f5565b80634f0bc491116100d35780634f0bc491146101525780634f2be91f1461016e57806361eeffcd1461017857806371091de314610182576100f5565b806305bdf1db146100fa57806318312545146101185780633b580f3c14610136575b600080fd5b610102610264565b60405161010f9190610da2565b60405180910390f35b61012061026e565b60405161012d9190610da2565b60405180910390f35b610150600480360381019061014b9190610e82565b610278565b005b61016c60048036038101906101679190610f85565b61046f565b005b6101766104f1565b005b610180610532565b005b61018a6105a4565b6040516101979190610da2565b60405180910390f35b6101a86105ae565b6040516101b59190610da2565b60405180910390f35b6101d860048036038101906101d39190610fe5565b6105b8565b005b6101e26105c2565b005b6101ec610789565b6040516101f99190610da2565b60405180910390f35b61020a610793565b6040516102179190611035565b60405180910390f35b61023a6004803603810190610235919061107c565b6107b0565b005b6102446107d0565b6040516102519190611167565b60405180910390f35b610262610828565b005b6000600354905090565b6000600154905090565b60008484905067ffffffffffffffff81111561029757610296611189565b5b6040519080825280602002602001820160405280156102c55781602001602082028036833780820191505090505b5090506102d0610cd9565b60005b868690508110156103a4578686828181106102f1576102f06111b8565b5b90506020020135826000018181525050848482818110610314576103136111b8565b5b905060200281019061032691906111f6565b8080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050826020018190525061037a8261089a565b83828151811061038d5761038c6111b8565b5b6020026020010181815250508060010190506102d3565b5060008686905067ffffffffffffffff8111156103c4576103c3611189565b5b6040519080825280602002602001820160405280156103f25781602001602082028036833780820191505090505b50905060005b835181101561044e57610424848281518110610417576104166111b8565b5b6020026020010151610941565b828281518110610437576104366111b8565b5b6020026020010181815250508060010190506103f8565b508060079080519060200190610465929190610cf3565b5050505050505050565b610477610cd9565b8381600001818152505082828080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050816020018190525060006104d98261089a565b90506104e481610941565b6004819055505050505050565b60006104fe6003546109de565b9050600061050d6004546109de565b9050600061051b8383610a7b565b90506105278133610b12565b600581905550505050565b600061053f6004546109de565b905061054b8133610b12565b6002819055503373ffffffffffffffffffffffffffffffffffffffff167f958094500e56c659b01cdefb25c66c88f025c3c800f69b2a2141f8c73b30e0566002546040516105999190610da2565b60405180910390a250565b6000600454905090565b6000600554905090565b8060038190555050565b600060078054905067ffffffffffffffff8111156105e3576105e2611189565b5b6040519080825280602002602001820160405280156106115781602001602082028036833780820191505090505b50905060005b6007805490508110156106755761064b6007828154811061063b5761063a6111b8565b5b90600052602060002001546109de565b82828151811061065e5761065d6111b8565b5b602002602001018181525050806001019050610617565b506000815167ffffffffffffffff81111561069357610692611189565b5b6040519080825280602002602001820160405280156106c15781602001602082028036833780820191505090505b50905060005b825181101561071e576106f48382815181106106e6576106e56111b8565b5b602002602001015133610b12565b828281518110610707576107066111b8565b5b6020026020010181815250508060010190506106c7565b508060069080519060200190610735929190610cf3565b503373ffffffffffffffffffffffffffffffffffffffff167ff29eb7753999773f8931d432bd17dfc5473e8560c770476b559a2df112617d96600660405161077d919061132f565b60405180910390a25050565b6000600254905090565b60008060009054906101000a900467ffffffffffffffff16905090565b60006107bb82610bd1565b90506107c681610941565b6003819055505050565b6060600680548060200260200160405190810160405280929190818152602001828054801561081e57602002820191906000526020600020905b81548152602001906001019080831161080a575b5050505050905090565b60006108356003546109de565b90506108418133610b12565b6001819055503373ffffffffffffffffffffffffffffffffffffffff167f958094500e56c659b01cdefb25c66c88f025c3c800f69b2a2141f8c73b30e05660015460405161088f9190610da2565b60405180910390a250565b6000606473ffffffffffffffffffffffffffffffffffffffff1663e4f36e106004808111156108cc576108cb611351565b5b60f81b846000015185602001516040518463ffffffff1660e01b81526004016108f79392919061145a565b6020604051808303816000875af1158015610916573d6000803e3d6000fd5b505050506040513d601f19601f8201168201806040525081019061093a91906114c4565b9050919050565b6000606473ffffffffffffffffffffffffffffffffffffffff1663c50c9c0260048081111561097357610972611351565b5b60f81b846040518363ffffffff1660e01b81526004016109949291906114f1565b6020604051808303816000875af11580156109b3573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906109d791906114c4565b9050919050565b6000606473ffffffffffffffffffffffffffffffffffffffff1663d2c135e5600480811115610a1057610a0f611351565b5b60f81b846040518363ffffffff1660e01b8152600401610a319291906114f1565b6020604051808303816000875af1158015610a50573d6000803e3d6000fd5b505050506040513d601f19601f82011682018060405250810190610a7491906114c4565b9050919050565b6000606473ffffffffffffffffffffffffffffffffffffffff16638c5d0150610aa76004806000610c78565b85856040518463ffffffff1660e01b8152600401610ac793929190611555565b6020604051808303816000875af1158015610ae6573d6000803e3d6000fd5b505050506040513d601f19601f82011682018060405250810190610b0a91906114c4565b905092915050565b6000606473ffffffffffffffffffffffffffffffffffffffff16633c6f0e68600480811115610b4457610b43611351565b5b60f81b8585604051602001610b599190611606565b6040516020818303038152906040526040518463ffffffff1660e01b8152600401610b869392919061145a565b6020604051808303816000875af1158015610ba5573d6000803e3d6000fd5b505050506040513d601f19601f82011682018060405250810190610bc991906114c4565b905092915050565b6000606473ffffffffffffffffffffffffffffffffffffffff1663d9b60b60600480811115610c0357610c02611351565b5b60f81b8467ffffffffffffffff166040518363ffffffff1660e01b8152600401610c2e9291906114f1565b6020604051808303816000875af1158015610c4d573d6000803e3d6000fd5b505050506040513d601f19601f82011682018060405250810190610c7191906114c4565b9050919050565b6000816002811115610c8d57610c8c611351565b5b60ff166008846004811115610ca557610ca4611351565b5b61ffff16901b61ffff166010866004811115610cc457610cc3611351565b5b62ffffff16901b171760e81b90509392505050565b604051806040016040528060008152602001606081525090565b828054828255906000526020600020908101928215610d2f579160200282015b82811115610d2e578251825591602001919060010190610d13565b5b509050610d3c9190610d40565b5090565b5b80821115610d59576000816000905550600101610d41565b5090565b6000819050919050565b6000819050919050565b6000610d8c610d87610d8284610d5d565b610d67565b610d5d565b9050919050565b610d9c81610d71565b82525050565b6000602082019050610db76000830184610d93565b92915050565b600080fd5b600080fd5b600080fd5b600080fd5b600080fd5b60008083601f840112610dec57610deb610dc7565b5b8235905067ffffffffffffffff811115610e0957610e08610dcc565b5b602083019150836020820283011115610e2557610e24610dd1565b5b9250929050565b60008083601f840112610e4257610e41610dc7565b5b8235905067ffffffffffffffff811115610e5f57610e5e610dcc565b5b602083019150836020820283011115610e7b57610e7a610dd1565b5b9250929050565b60008060008060408587031215610e9c57610e9b610dbd565b5b600085013567ffffffffffffffff811115610eba57610eb9610dc2565b5b610ec687828801610dd6565b9450945050602085013567ffffffffffffffff811115610ee957610ee8610dc2565b5b610ef587828801610e2c565b925092505092959194509250565b610f0c81610d5d565b8114610f1757600080fd5b50565b600081359050610f2981610f03565b92915050565b60008083601f840112610f4557610f44610dc7565b5b8235905067ffffffffffffffff811115610f6257610f61610dcc565b5b602083019150836001820283011115610f7e57610f7d610dd1565b5b9250929050565b600080600060408486031215610f9e57610f9d610dbd565b5b6000610fac86828701610f1a565b935050602084013567ffffffffffffffff811115610fcd57610fcc610dc2565b5b610fd986828701610f2f565b92509250509250925092565b600060208284031215610ffb57610ffa610dbd565b5b600061100984828501610f1a565b91505092915050565b600067ffffffffffffffff82169050919050565b61102f81611012565b82525050565b600060208201905061104a6000830184611026565b92915050565b61105981611012565b811461106457600080fd5b50565b60008135905061107681611050565b92915050565b60006020828403121561109257611091610dbd565b5b60006110a084828501611067565b91505092915050565b600081519050919050565b600082825260208201905092915050565b6000819050602082019050919050565b6110de81610d71565b82525050565b60006110f083836110d5565b60208301905092915050565b6000602082019050919050565b6000611114826110a9565b61111e81856110b4565b9350611129836110c5565b8060005b8381101561115a57815161114188826110e4565b975061114c836110fc565b92505060018101905061112d565b5085935050505092915050565b600060208201905081810360008301526111818184611109565b905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b600080fd5b600080fd5b600080fd5b60008083356001602003843603038112611213576112126111e7565b5b80840192508235915067ffffffffffffffff821115611235576112346111ec565b5b602083019250600182023603831315611251576112506111f1565b5b509250929050565b600081549050919050565b60008190508160005260206000209050919050565b60008160001c9050919050565b6000819050919050565b60006112a361129e83611279565b611286565b9050919050565b60006112b68254611290565b9050919050565b6000600182019050919050565b60006112d582611259565b6112df81856110b4565b93506112ea83611264565b8060005b83811015611322576112ff826112aa565b61130988826110e4565b9750611314836112bd565b9250506001810190506112ee565b5085935050505092915050565b6000602082019050818103600083015261134981846112ca565b905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b60007fff0000000000000000000000000000000000000000000000000000000000000082169050919050565b6113b581611380565b82525050565b6113c481610d5d565b82525050565b600081519050919050565b600082825260208201905092915050565b60005b838110156114045780820151818401526020810190506113e9565b60008484015250505050565b6000601f19601f8301169050919050565b600061142c826113ca565b61143681856113d5565b93506114468185602086016113e6565b61144f81611410565b840191505092915050565b600060608201905061146f60008301866113ac565b61147c60208301856113bb565b818103604083015261148e8184611421565b9050949350505050565b6114a181610d5d565b81146114ac57600080fd5b50565b6000815190506114be81611498565b92915050565b6000602082840312156114da576114d9610dbd565b5b60006114e8848285016114af565b91505092915050565b600060408201905061150660008301856113ac565b61151360208301846113bb565b9392505050565b60007fffffff000000000000000000000000000000000000000000000000000000000082169050919050565b61154f8161151a565b82525050565b600060608201905061156a6000830186611546565b61157760208301856113bb565b61158460408301846113bb565b949350505050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006115b78261158c565b9050919050565b60008160601b9050919050565b60006115d6826115be565b9050919050565b60006115e8826115cb565b9050919050565b6116006115fb826115ac565b6115dd565b82525050565b600061161282846115ef565b6014820191508190509291505056fea2646970667358221220d395261a7719e2e038106ff468b8032856d9c9cb6626c4088066e6df00910a1b64736f6c63430008180033"
    }

    some_other_deployed_contract = get_contract(web3, some_other_contract_keeping_data['abi'],
                                                some_other_contract_keeping_data['bytecode'],
                                                some_other_contract_keeping_data['address'])

    old_network_encrypted_data = get_network_value(deployed_contract, eoa)
    network_encrypted_data = get_network_value(some_other_deployed_contract, eoa)
    save_network_encrypted_in_contract(deployed_contract, tx_params, network_encrypted_data)
    new_network_encrypted_data = get_network_value(deployed_contract, eoa)
    # assert that previous data and new one are not the same, meaning it was really changed
    assert old_network_encrypted_data != new_network_encrypted_data
    # assert that new data is same as the one we copied it from
    assert new_network_encrypted_data == network_encrypted_data
    tx_receipt = save_network_encrypted_to_user_encrypted_in_contract(deployed_contract, tx_params)
    # assert that it failed to save network encrypted data into user encrypted data, that was actually copied from
    # another contract, hence, keeping different contracts secured
    assert tx_receipt.status == 0


# create another EOA and do the same computation method demonstrating the capability to use the same contract method
# just with different account and having the correct result back encrypted and decrypted with the other EOA
def compute_add_with_different_account(eoa_private_key, gas_limit, gas_price_gwei, web3, deployed_contract, result):
    alice_decrypted_aes_key, alice_eoa, alice_tx_params = create_another_account(eoa_private_key, gas_limit,
                                                                                 gas_price_gwei, web3)
    basic_add_computation(deployed_contract, alice_tx_params, alice_eoa, alice_decrypted_aes_key, result)


# create another EOA account, fund it and onboard it so that you could have the aes key of it
def create_another_account(eoa_private_key, gas_limit, gas_price_gwei, web3):
    alice_eoa = Account.create()
    tx_receipt = transfer_native(web3, alice_eoa.address, eoa_private_key, 0.5, gas_limit)
    print(tx_receipt)
    alice_private_key = alice_eoa._private_key.hex()[2:]
    alice_web3 = init_web3(get_node_https_address(), alice_eoa)
    onboard_deployed_contract = get_contract(alice_web3, devnet_onboard_contract['abi'],
                                             devnet_onboard_contract['bytecode'],
                                             devnet_onboard_contract['address'])
    alice_tx_params = {'web3': alice_web3, 'gas_limit': gas_limit, 'gas_price_gwei': gas_price_gwei,
                       'eoa_private_key': alice_private_key}
    alice_decrypted_aes_key = onboard_for_aes_key(onboard_deployed_contract, alice_private_key, alice_tx_params)
    return alice_decrypted_aes_key, alice_eoa, alice_tx_params


def basic_add_computation(deployed_contract, tx_params, eoa, account_hex_encryption_key, sum_result):
    kwargs = {}
    tx_receipt = add_one_encrypted_value_with_another_on_chain(deployed_contract, kwargs, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    user_encrypted_arithmetic_result = get_user_arithmetic_result(deployed_contract, eoa)
    user_decrypted_arithmetic_result = decrypt_uint(user_encrypted_arithmetic_result, account_hex_encryption_key)
    assert sum_result == user_decrypted_arithmetic_result


# Sending tx with encrypted value, that value will be saved in the field of the contract
# flow: sending tx, asserting value was sent encrypted by data recorded in the block
# receiving back encrypted value via func and event log, asserting that they are the same
# decrypting value and asserting it is as the clear value
def basic_encrypted_encrypt_decrypt(account_hex_encryption_key, deployed_contract, eoa,
                                    hex_account_private_key, tx_params):
    tx_receipt, user_some_value_clear, input_text = \
        save_input_text_network_encrypted_in_contract(deployed_contract, account_hex_encryption_key, eoa,
                                                      hex_account_private_key, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    validate_block_has_tx_input_encrypted_value(tx_params, tx_receipt, user_some_value_clear,
                                                account_hex_encryption_key, input_text)
    kwargs = {}
    tx_receipt = save_network_encrypted_to_user_encrypted_input_in_contract(deployed_contract, kwargs, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    user_cipher_text_from_block = tx_receipt.logs[0].data
    user_cipher_text_from_block_int_value = int(user_cipher_text_from_block.hex(), 16)
    user_cipher_text_from_contract = get_user_value_encrypted_input(deployed_contract, eoa)
    # assert that same value back from view func is one back from event
    assert user_cipher_text_from_block_int_value == user_cipher_text_from_contract
    user_cipher_text_decrypted = decrypt_uint(user_cipher_text_from_contract, account_hex_encryption_key)
    # assert that value saved encrypted within the network is one sent
    assert user_cipher_text_decrypted == user_some_value_clear
    return user_cipher_text_decrypted


# Sending tx with encrypted string value, that value will be saved in the field of the contract
# flow: sending tx, asserting value was sent encrypted by data recorded in the block
# receiving back encrypted value via func and event log, asserting that they are the same
# decrypting value and asserting it is as the clear value
def basic_string_encrypt_decrypt(account_hex_encryption_key, deployed_contract, eoa,
                                 hex_account_private_key, tx_params):
    tx_receipt, user_some_value_clear, input_text = \
        save_string_input_text_network_encrypted_in_contract(deployed_contract, account_hex_encryption_key, eoa,
                                                             hex_account_private_key, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    validate_block_has_tx_string_input_encrypted_value(tx_params, tx_receipt, user_some_value_clear,
                                                       account_hex_encryption_key, input_text, deployed_contract)
    kwargs = {}
    tx_receipt = save_network_encrypted_to_user_encrypted_input_string_in_contract(deployed_contract, kwargs, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)

    user_encrypted_strings_from_event = \
        deployed_contract.events.UserEncryptedStringValue().process_receipt(tx_receipt)[0][
            'args'].ctUserSomeEncryptedStringValue
    user_cipher_string_text_from_contract = get_user_string_value_encrypted_input(deployed_contract, eoa)

    validate_block_event_against_user_encrypted_string(account_hex_encryption_key,
                                                       user_cipher_string_text_from_contract,
                                                       user_encrypted_strings_from_event, user_some_value_clear)


def validate_block_event_against_user_encrypted_string(account_hex_encryption_key,
                                                       user_cipher_string_text_from_contract,
                                                       user_encrypted_strings_from_event, user_some_value_clear):

    for char_from_event, char_from_get_method in zip(user_encrypted_strings_from_event,
                                                     user_cipher_string_text_from_contract):
        assert char_from_event == char_from_get_method

    user_cipher_text_decrypted = decrypt_string(user_encrypted_strings_from_event, account_hex_encryption_key)
    user_decrypt_string_from_contract = decrypt_string(user_cipher_string_text_from_contract, account_hex_encryption_key)

    assert user_cipher_text_decrypted == user_some_value_clear
    assert user_decrypt_string_from_contract == user_some_value_clear

# Sending tx with clear value as tx input, that value will be saved encrypted in the contract (by network key)
# flow: sending tx, asserting value was sent clear by data recorded in the block
# receiving back encrypted value via func and event log, asserting that they are the same
# decrypting value and asserting it is as the clear value
def basic_clear_encrypt_decrypt(account_hex_encryption_key, deployed_contract, eoa, tx_params):
    user_some_value_clear, tx_receipt = save_clear_value_network_encrypted_in_contract(deployed_contract, tx_params)
    validate_block_has_tx_input_clear_value(tx_params, tx_receipt, user_some_value_clear)
    tx_receipt = save_network_encrypted_to_user_encrypted_in_contract(deployed_contract, tx_params)
    user_encrypted_value_from_block = tx_receipt.logs[0].data
    user_encrypted_value_from_block_int_value = int(user_encrypted_value_from_block.hex(), 16)
    user_encrypted_value_from_contract = get_user_encrypted_from_contract(deployed_contract, eoa)
    # assert that same value back from view func is one back from event
    assert user_encrypted_value_from_block_int_value == user_encrypted_value_from_contract
    user_some_value_decrypted = decrypt_uint(user_encrypted_value_from_contract, account_hex_encryption_key)
    # assert that value saved encrypted within the network is one sent
    assert user_some_value_decrypted == user_some_value_clear
    return user_some_value_decrypted


def save_network_encrypted_to_user_encrypted_in_contract(deployed_contract, tx_params):
    kwargs = {}
    tx_receipt = setUserSomeEncryptedValue(deployed_contract, kwargs, tx_params)
    print(tx_receipt)
    return tx_receipt


# asserting that if trying to decrypt value back that was encrypted by user key can't be
# deciphered by another key
def basic_decryption_failure(some_other_account_hex_encryption_key, deployed_contract, eoa, tx_params):
    user_some_value_clear, _ = save_clear_value_network_encrypted_in_contract(deployed_contract, tx_params)
    user_some_value_encrypted = get_user_encrypted_from_contract(deployed_contract, eoa)
    user_some_value_decrypted = decrypt_uint(user_some_value_encrypted, some_other_account_hex_encryption_key)
    # assert that value back cant be decrypted by some other key
    assert user_some_value_decrypted != user_some_value_clear


# asserting that if trying to decrypt the value saved with network key with user key, it will fail
def network_decryption_failure(account_hex_encryption_key, deployed_contract, eoa, tx_params):
    user_some_value_clear, _ = save_clear_value_network_encrypted_in_contract(deployed_contract, tx_params)
    network_some_value_encrypted = get_network_value(deployed_contract, eoa)
    network_some_value_decrypted = decrypt_uint(network_some_value_encrypted, account_hex_encryption_key)
    # assert that network encrypted value cant be decrypted by user key
    assert network_some_value_decrypted != user_some_value_clear


def save_input_text_network_encrypted_in_contract(deployed_contract, account_hex_encryption_key, eoa,
                                                  hex_account_private_key, tx_params):
    clear_input = 8
    kwargs = {'_itCT': clear_input, '_itSignature': bytes(65)}
    func = deployed_contract.functions.setSomeEncryptedValueEncryptedInput(**kwargs)
    func_sig = get_function_signature(func.abi)
    eoa_private_key = tx_params['eoa_private_key']
    hex_account_private_key = bytes.fromhex(eoa_private_key)
    input_text, signature = build_input_text(clear_input, account_hex_encryption_key, eoa, deployed_contract, func_sig,
                                             hex_account_private_key)
    kwargs['_itCT'] = input_text
    kwargs['_itSignature'] = signature
    func = deployed_contract.functions.setSomeEncryptedValueEncryptedInput(**kwargs)
    return exec_func_via_transaction(func, tx_params), clear_input, input_text


def save_string_input_text_network_encrypted_in_contract(deployed_contract, account_hex_encryption_key, eoa,
                                                         hex_account_private_key, tx_params):
    clear_input = "test string"
    encoded_clear_input = array('B', clear_input.encode('utf-8'))
    _itSignature = [bytes(65) for i in encoded_clear_input]
    kwargs = {'_itInputString': encoded_clear_input, '_itSignature': _itSignature}
    func = deployed_contract.functions.setSomeEncryptedStringEncryptedInput(**kwargs)
    func_sig = get_function_signature(func.abi)
    eoa_private_key = tx_params['eoa_private_key']
    hex_account_private_key = bytes.fromhex(eoa_private_key)
    input_text = build_string_input_text(clear_input, account_hex_encryption_key, eoa, deployed_contract, func_sig,
                                         hex_account_private_key)
    ciphertexts = [entry['ciphertext'] for entry in input_text]
    signatures = [entry['signature'] for entry in input_text]

    kwargs['_itInputString'] = ciphertexts
    kwargs['_itSignature'] = signatures
    func = deployed_contract.functions.setSomeEncryptedStringEncryptedInput(**kwargs)
    return exec_func_via_transaction(func, tx_params), clear_input, input_text


def save_clear_value_network_encrypted_in_contract(deployed_contract, tx_params):
    user_some_value_clear = 7
    kwargs = {'_value': user_some_value_clear}
    tx_receipt = setSomeEncryptedValue(deployed_contract, kwargs, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    return user_some_value_clear, tx_receipt


def save_network_encrypted_in_contract(deployed_contract, tx_params, value):
    kwargs = {'networkEncrypted': value}
    tx_receipt = setNetworkSomeEncryptedValue(deployed_contract, kwargs, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)


def validate_block_has_tx_input_clear_value(tx_params, tx_receipt, user_some_value_clear):
    tx_from_block = tx_params['web3'].eth.get_transaction_by_block(tx_receipt['blockHash'],
                                                                   tx_receipt['transactionIndex'])
    print(tx_from_block)
    user_some_value_clear_from_tx = tx_from_block['input'].hex()[10:]
    assert int(user_some_value_clear_from_tx) == user_some_value_clear


def validate_block_has_tx_input_encrypted_value(tx_params, tx_receipt, user_some_value_clear,
                                                account_hex_encryption_key, input_text):
    tx_from_block = tx_params['web3'].eth.get_transaction_by_block(tx_receipt['blockHash'],
                                                                   tx_receipt['transactionIndex'])
    print(tx_from_block)
    input_text_from_tx = tx_from_block['input'].hex()[10:74]
    # assert that value encrypted locally was saved in block
    assert input_text == int(input_text_from_tx, 16)
    # assert that value saved in block is not clear
    assert str(input_text_from_tx) != str(user_some_value_clear)
    decrypted_input_from_tx = decrypt_uint(int(input_text_from_tx, 16), account_hex_encryption_key)
    # assert that value saved in block is as clear after decryption
    assert int(decrypted_input_from_tx) == user_some_value_clear


def validate_block_has_tx_string_input_encrypted_value(tx_params, tx_receipt, user_some_value_clear,
                                                       account_hex_encryption_key, input_text, contract):
    tx_from_block = tx_params['web3'].eth.get_transaction_by_block(tx_receipt['blockHash'],
                                                                   tx_receipt['transactionIndex'])
    print(tx_from_block)
    tx_inputs = contract.decode_function_input(tx_from_block['input'].hex())
    ciphertexts = [entry['ciphertext'] for entry in input_text]
    for input_text_from_tx, input_text in zip(tx_inputs[1]['_itInputString'], ciphertexts):
        # assert that value encrypted locally was saved in block
        assert input_text == input_text_from_tx

    # Decode the bytes to a string
    string_from_input_tx = decrypt_string(tx_inputs[1]['_itInputString'], account_hex_encryption_key)

    # assert that value saved in block is as clear after decryption
    assert string_from_input_tx == user_some_value_clear


def get_user_encrypted_from_contract(deployed_contract, eoa):
    return deployed_contract.functions.getUserSomeEncryptedValue().call({'from': eoa.address})


def get_user_value_encrypted_input(deployed_contract, eoa):
    return deployed_contract.functions.getUserSomeEncryptedValueEncryptedInput().call({'from': eoa.address})


def get_user_string_value_encrypted_input(deployed_contract, eoa):
    return deployed_contract.functions.getUserSomeEncryptedStringEncryptedInput().call({'from': eoa.address})


def get_network_value(deployed_contract, eoa):
    return deployed_contract.functions.getNetworkSomeEncryptedValue().call({'from': eoa.address})


def get_user_arithmetic_result(deployed_contract, eoa):
    return deployed_contract.functions.getUserArithmeticResult().call({'from': eoa.address})


# normal solidity view function to get a value that was saved,
# in this case saved when the contract constructor was executed
def basic_get_value(deployed_contract, eoa, web3):
    some_value = deployed_contract.functions.getSomeValue().call({'from': eoa.address})
    assert some_value == 5
    index_0_at_storage = int(web3.eth.get_storage_at(deployed_contract.address, 0).hex(), 16)
    assert index_0_at_storage == 5


def setUserSomeEncryptedValue(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.setUserSomeEncryptedValue(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def setNetworkSomeEncryptedValue(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.setNetworkSomeEncryptedValue(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def save_network_encrypted_to_user_encrypted_input_in_contract(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.setUserSomeEncryptedValueEncryptedInput(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def save_network_encrypted_to_user_encrypted_input_string_in_contract(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.setUserSomeEncryptedStringEncryptedInput(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def setSomeEncryptedValue(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.setSomeEncryptedValue(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def someEncryptedValueOf(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.someEncryptedValueOf(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def add_one_encrypted_value_with_another_on_chain(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.add(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def init():
    load_dotenv()  # loading .env
    eoa_private_key = get_account_private_key()  # Get EOA Private key for execution
    account_hex_encryption_key = get_hex_account_encryption_key()  # Get Hex key used to encrypt on network
    eoa = get_eoa(eoa_private_key)  # Get EOA
    web3 = init_web3(get_node_https_address(), eoa)  # Init connection to node
    validate_minimum_balance(web3)  # validate minimum balance
    return account_hex_encryption_key, eoa, eoa_private_key, web3


def deploy(account_hex_encryption_key, eoa, tx_params):
    kwargs = {}
    contract_name = "DataOnChain"
    contract_file_name = contract_name + ".sol"
    relative_to_contracts_directory = "examples/"
    relative_to_mpc_core = "../lib/MpcCore.sol"
    deployed_contract, was_already_deployed = \
        get_deployed_contract(contract_name, contract_file_name, relative_to_contracts_directory, tx_params, kwargs,
                              relative_to_mpc_core)
    print('contract address: ', deployed_contract.address)

    return deployed_contract


if __name__ == "__main__":
    main()
