import importlib.resources
import json

from eth_abi.abi import decode
from examples.onboard.onboard_account import *
from math import ceil

# script demonstrates basic network capabilities on encrypt/decrypt of values saved in a contract
def main():
    account_hex_encryption_key, eoa, eoa_private_key, web3 = init()

    gas_limit = 10000000
    gas_price_gwei = 30

    tx_params = {'web3': web3, 'gas_limit': gas_limit, 'gas_price_gwei': gas_price_gwei,
                 'eoa_private_key': eoa_private_key}
    deployed_contract = deploy(web3, eoa, tx_params)

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
                "components": [
                    {
                    "internalType": "ctUint64[]",
                    "name": "value",
                    "type": "uint256[]"
                    }
                ],
                "indexed": false,
                "internalType": "struct ctString",
                "name": "ctUserSomeEncryptedStringValue",
                "type": "tuple"
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
                "components": [
                    {
                    "internalType": "ctUint64[]",
                    "name": "value",
                    "type": "uint256[]"
                    }
                ],
                "internalType": "struct ctString",
                "name": "ctSomeEncryptedValue",
                "type": "tuple"
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
                "components": [
                    {
                    "components": [
                        {
                        "internalType": "ctUint64[]",
                        "name": "value",
                        "type": "uint256[]"
                        }
                    ],
                    "internalType": "struct ctString",
                    "name": "ciphertext",
                    "type": "tuple"
                    },
                    {
                    "internalType": "bytes[]",
                    "name": "signature",
                    "type": "bytes[]"
                    }
                ],
                "internalType": "struct itString",
                "name": "_itInputString",
                "type": "tuple"
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
        "bytecode": "0x608060405234801561001057600080fd5b50600436106100f55760003560e01c80638d7eadec11610097578063a40674b711610066578063a40674b714610202578063af384ac714610220578063d7c496011461023c578063fee511d61461025a576100f5565b80638d7eadec146101a05780639c82c7c7146101be5780639f3f69de146101da578063a2e12869146101e4576100f5565b80634f2be91f116100d35780634f2be91f1461015257806361eeffcd1461015c57806371091de31461016657806380b9de4b14610184576100f5565b806305bdf1db146100fa57806318312545146101185780634f0bc49114610136575b600080fd5b610102610264565b60405161010f9190610f43565b60405180910390f35b61012061026e565b60405161012d9190610f43565b60405180910390f35b610150600480360381019061014b9190611003565b610278565b005b61015a6102fa565b005b61016461033b565b005b61016e6103ad565b60405161017b9190610f43565b60405180910390f35b61019e60048036038101906101999190611087565b6103b7565b005b6101a86103fc565b6040516101b59190610f43565b60405180910390f35b6101d860048036038101906101d391906110d0565b610406565b005b6101e2610410565b005b6101ec6104ff565b6040516101f99190610f43565b60405180910390f35b61020a610509565b6040516102179190611120565b60405180910390f35b61023a60048036038101906102359190611167565b610526565b005b610244610546565b604051610251919061127c565b60405180910390f35b6102626105b8565b005b6000600354905090565b6000600154905090565b610280610e54565b8381600001818152505082828080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050816020018190525060006102e28261062a565b90506102ed816106d1565b6004819055505050505050565b600061030760035461076e565b9050600061031660045461076e565b90506000610324838361080b565b905061033081336108a2565b600581905550505050565b600061034860045461076e565b905061035481336108a2565b6002819055503373ffffffffffffffffffffffffffffffffffffffff167f958094500e56c659b01cdefb25c66c88f025c3c800f69b2a2141f8c73b30e0566002546040516103a29190610f43565b60405180910390a250565b6000600454905090565b60006103cb826103c69061166d565b610961565b90506103d681610ac2565b600760008201518160000190805190602001906103f4929190610e6e565b509050505050565b6000600554905090565b8060038190555050565b600061047f60076040518060200160405290816000820180548060200260200160405190810160405280929190818152602001828054801561047157602002820191906000526020600020905b81548152602001906001019080831161045d575b505050505081525050610b9a565b905061048b8133610c72565b600660008201518160000190805190602001906104a9929190610e6e565b509050503373ffffffffffffffffffffffffffffffffffffffff167f8137412c935bcf66b07e7f46876a6a63d0f08458ada5df0d661d96dc611c45d160066040516104f49190611781565b60405180910390a250565b6000600254905090565b60008060009054906101000a900467ffffffffffffffff16905090565b600061053182610d4c565b905061053c816106d1565b6003819055505050565b61054e610ebb565b6006604051806020016040529081600082018054806020026020016040519081016040528092919081815260200182805480156105aa57602002820191906000526020600020905b815481526020019060010190808311610596575b505050505081525050905090565b60006105c560035461076e565b90506105d181336108a2565b6001819055503373ffffffffffffffffffffffffffffffffffffffff167f958094500e56c659b01cdefb25c66c88f025c3c800f69b2a2141f8c73b30e05660015460405161061f9190610f43565b60405180910390a250565b6000606473ffffffffffffffffffffffffffffffffffffffff1663e4f36e1060048081111561065c5761065b6117a3565b5b60f81b846000015185602001516040518463ffffffff1660e01b81526004016106879392919061189b565b6020604051808303816000875af11580156106a6573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906106ca9190611905565b9050919050565b6000606473ffffffffffffffffffffffffffffffffffffffff1663c50c9c02600480811115610703576107026117a3565b5b60f81b846040518363ffffffff1660e01b8152600401610724929190611932565b6020604051808303816000875af1158015610743573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906107679190611905565b9050919050565b6000606473ffffffffffffffffffffffffffffffffffffffff1663d2c135e56004808111156107a05761079f6117a3565b5b60f81b846040518363ffffffff1660e01b81526004016107c1929190611932565b6020604051808303816000875af11580156107e0573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906108049190611905565b9050919050565b6000606473ffffffffffffffffffffffffffffffffffffffff16638c5d01506108376004806000610df3565b85856040518463ffffffff1660e01b815260040161085793929190611996565b6020604051808303816000875af1158015610876573d6000803e3d6000fd5b505050506040513d601f19601f8201168201806040525081019061089a9190611905565b905092915050565b6000606473ffffffffffffffffffffffffffffffffffffffff16633c6f0e686004808111156108d4576108d36117a3565b5b60f81b85856040516020016108e99190611a47565b6040516020818303038152906040526040518463ffffffff1660e01b81526004016109169392919061189b565b6020604051808303816000875af1158015610935573d6000803e3d6000fd5b505050506040513d601f19601f820116820180604052508101906109599190611905565b905092915050565b610969610ece565b600082602001515190508083600001516000015151146109be576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016109b590611abf565b60405180910390fd5b600060405180602001604052808367ffffffffffffffff8111156109e5576109e46112b4565b5b604051908082528060200260200182016040528015610a135781602001602082028036833780820191505090505b508152509050610a21610e54565b60005b83811015610ab6578560000151600001518181518110610a4757610a46611adf565b5b602002602001015182600001818152505085602001518181518110610a6f57610a6e611adf565b5b60200260200101518260200181905250610a888261062a565b83600001518281518110610a9f57610a9e611adf565b5b602002602001018181525050806001019050610a24565b50819350505050919050565b610aca610ebb565b60008260000151519050600060405180602001604052808367ffffffffffffffff811115610afb57610afa6112b4565b5b604051908082528060200260200182016040528015610b295781602001602082028036833780820191505090505b50815250905060005b82811015610b8f57610b6185600001518281518110610b5457610b53611adf565b5b60200260200101516106d1565b82600001518281518110610b7857610b77611adf565b5b602002602001018181525050806001019050610b32565b508092505050919050565b610ba2610ece565b60008260000151519050600060405180602001604052808367ffffffffffffffff811115610bd357610bd26112b4565b5b604051908082528060200260200182016040528015610c015781602001602082028036833780820191505090505b50815250905060005b82811015610c6757610c3985600001518281518110610c2c57610c2b611adf565b5b602002602001015161076e565b82600001518281518110610c5057610c4f611adf565b5b602002602001018181525050806001019050610c0a565b508092505050919050565b610c7a610ebb565b60008360000151519050600060405180602001604052808367ffffffffffffffff811115610cab57610caa6112b4565b5b604051908082528060200260200182016040528015610cd95781602001602082028036833780820191505090505b50815250905060005b82811015610d4057610d1286600001518281518110610d0457610d03611adf565b5b6020026020010151866108a2565b82600001518281518110610d2957610d28611adf565b5b602002602001018181525050806001019050610ce2565b50809250505092915050565b6000606473ffffffffffffffffffffffffffffffffffffffff1663d9b60b60600480811115610d7e57610d7d6117a3565b5b60f81b8467ffffffffffffffff166040518363ffffffff1660e01b8152600401610da9929190611932565b6020604051808303816000875af1158015610dc8573d6000803e3d6000fd5b505050506040513d601f19601f82011682018060405250810190610dec9190611905565b9050919050565b6000816002811115610e0857610e076117a3565b5b60ff166008846004811115610e2057610e1f6117a3565b5b61ffff16901b61ffff166010866004811115610e3f57610e3e6117a3565b5b62ffffff16901b171760e81b90509392505050565b604051806040016040528060008152602001606081525090565b828054828255906000526020600020908101928215610eaa579160200282015b82811115610ea9578251825591602001919060010190610e8e565b5b509050610eb79190610ee1565b5090565b6040518060200160405280606081525090565b6040518060200160405280606081525090565b5b80821115610efa576000816000905550600101610ee2565b5090565b6000819050919050565b6000819050919050565b6000610f2d610f28610f2384610efe565b610f08565b610efe565b9050919050565b610f3d81610f12565b82525050565b6000602082019050610f586000830184610f34565b92915050565b6000604051905090565b600080fd5b600080fd5b610f7b81610efe565b8114610f8657600080fd5b50565b600081359050610f9881610f72565b92915050565b600080fd5b600080fd5b600080fd5b60008083601f840112610fc357610fc2610f9e565b5b8235905067ffffffffffffffff811115610fe057610fdf610fa3565b5b602083019150836001820283011115610ffc57610ffb610fa8565b5b9250929050565b60008060006040848603121561101c5761101b610f68565b5b600061102a86828701610f89565b935050602084013567ffffffffffffffff81111561104b5761104a610f6d565b5b61105786828701610fad565b92509250509250925092565b600080fd5b60006040828403121561107e5761107d611063565b5b81905092915050565b60006020828403121561109d5761109c610f68565b5b600082013567ffffffffffffffff8111156110bb576110ba610f6d565b5b6110c784828501611068565b91505092915050565b6000602082840312156110e6576110e5610f68565b5b60006110f484828501610f89565b91505092915050565b600067ffffffffffffffff82169050919050565b61111a816110fd565b82525050565b60006020820190506111356000830184611111565b92915050565b611144816110fd565b811461114f57600080fd5b50565b6000813590506111618161113b565b92915050565b60006020828403121561117d5761117c610f68565b5b600061118b84828501611152565b91505092915050565b600081519050919050565b600082825260208201905092915050565b6000819050602082019050919050565b6111c981610f12565b82525050565b60006111db83836111c0565b60208301905092915050565b6000602082019050919050565b60006111ff82611194565b611209818561119f565b9350611214836111b0565b8060005b8381101561124557815161122c88826111cf565b9750611237836111e7565b925050600181019050611218565b5085935050505092915050565b6000602083016000830151848203600086015261126f82826111f4565b9150508091505092915050565b600060208201905081810360008301526112968184611252565b905092915050565b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6112ec826112a3565b810181811067ffffffffffffffff8211171561130b5761130a6112b4565b5b80604052505050565b600061131e610f5e565b905061132a82826112e3565b919050565b600080fd5b600067ffffffffffffffff82111561134f5761134e6112b4565b5b602082029050602081019050919050565b600061137361136e84611334565b611314565b9050808382526020820190506020840283018581111561139657611395610fa8565b5b835b818110156113bf57806113ab8882610f89565b845260208401935050602081019050611398565b5050509392505050565b600082601f8301126113de576113dd610f9e565b5b81356113ee848260208601611360565b91505092915050565b60006020828403121561140d5761140c61129e565b5b6114176020611314565b9050600082013567ffffffffffffffff8111156114375761143661132f565b5b611443848285016113c9565b60008301525092915050565b600067ffffffffffffffff82111561146a576114696112b4565b5b602082029050602081019050919050565b600080fd5b600067ffffffffffffffff82111561149b5761149a6112b4565b5b6114a4826112a3565b9050602081019050919050565b82818337600083830152505050565b60006114d36114ce84611480565b611314565b9050828152602081018484840111156114ef576114ee61147b565b5b6114fa8482856114b1565b509392505050565b600082601f83011261151757611516610f9e565b5b81356115278482602086016114c0565b91505092915050565b600061154361153e8461144f565b611314565b9050808382526020820190506020840283018581111561156657611565610fa8565b5b835b818110156115ad57803567ffffffffffffffff81111561158b5761158a610f9e565b5b8086016115988982611502565b85526020850194505050602081019050611568565b5050509392505050565b600082601f8301126115cc576115cb610f9e565b5b81356115dc848260208601611530565b91505092915050565b6000604082840312156115fb576115fa61129e565b5b6116056040611314565b9050600082013567ffffffffffffffff8111156116255761162461132f565b5b611631848285016113f7565b600083015250602082013567ffffffffffffffff8111156116555761165461132f565b5b611661848285016115b7565b60208301525092915050565b600061167936836115e5565b9050919050565b600081549050919050565b60008190508160005260206000209050919050565b60008160001c9050919050565b6000819050919050565b60006116ca6116c5836116a0565b6116ad565b9050919050565b60006116dd82546116b7565b9050919050565b6000600182019050919050565b60006116fc82611680565b611706818561119f565b93506117118361168b565b8060005b8381101561174957611726826116d1565b61173088826111cf565b975061173b836116e4565b925050600181019050611715565b5085935050505092915050565b6000602083016000808401858303600087015261177383826116f1565b925050819250505092915050565b6000602082019050818103600083015261179b8184611756565b905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b60007fff0000000000000000000000000000000000000000000000000000000000000082169050919050565b611807816117d2565b82525050565b61181681610efe565b82525050565b600081519050919050565b600082825260208201905092915050565b60005b8381101561185657808201518184015260208101905061183b565b60008484015250505050565b600061186d8261181c565b6118778185611827565b9350611887818560208601611838565b611890816112a3565b840191505092915050565b60006060820190506118b060008301866117fe565b6118bd602083018561180d565b81810360408301526118cf8184611862565b9050949350505050565b6118e281610efe565b81146118ed57600080fd5b50565b6000815190506118ff816118d9565b92915050565b60006020828403121561191b5761191a610f68565b5b6000611929848285016118f0565b91505092915050565b600060408201905061194760008301856117fe565b611954602083018461180d565b9392505050565b60007fffffff000000000000000000000000000000000000000000000000000000000082169050919050565b6119908161195b565b82525050565b60006060820190506119ab6000830186611987565b6119b8602083018561180d565b6119c5604083018461180d565b949350505050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006119f8826119cd565b9050919050565b60008160601b9050919050565b6000611a17826119ff565b9050919050565b6000611a2982611a0c565b9050919050565b611a41611a3c826119ed565b611a1e565b82525050565b6000611a538284611a30565b60148201915081905092915050565b600082825260208201905092915050565b7f4d50435f434f52453a20494e56414c49445f494e5055545f5445585400000000600082015250565b6000611aa9601c83611a62565b9150611ab482611a73565b602082019050919050565b60006020820190508181036000830152611ad881611a9c565b9050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fdfea2646970667358221220aa9690f4e763a835b2caa462c13db056d15ad7831d7fc9ce76fc5f38c26155e564736f6c63430008180033"
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
    onboard_deployed_contract = get_contract(alice_web3, testnet_onboard_contract['abi'],
                                             testnet_onboard_contract['bytecode'],
                                             testnet_onboard_contract['address'])
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
    
    print(user_cipher_string_text_from_contract)
    print(user_encrypted_strings_from_event)
    print(user_some_value_clear)

    for item_from_event, item_from_get_method in zip(user_encrypted_strings_from_event['value'],
                                                     user_cipher_string_text_from_contract[0]):
        assert item_from_event == item_from_get_method

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
    kwargs = { 'itValue': (clear_input, bytes(65)) }
    func_selector = deployed_contract.functions.setSomeEncryptedValueEncryptedInput(**kwargs).selector
    eoa_private_key = tx_params['eoa_private_key']
    hex_account_private_key = bytes.fromhex(eoa_private_key)
    input_text = build_input_text(clear_input, account_hex_encryption_key, eoa, deployed_contract, func_selector,
                                             hex_account_private_key)
    kwargs['itValue'] = input_text
    func = deployed_contract.functions.setSomeEncryptedValueEncryptedInput(**kwargs)
    return exec_func_via_transaction(func, tx_params), clear_input, input_text


def save_string_input_text_network_encrypted_in_contract(deployed_contract, account_hex_encryption_key, eoa,
                                                         hex_account_private_key, tx_params):
    clear_input = "test string"
    encoded_clear_input = bytearray(list(clear_input.encode('utf-8')))
    _itCiphertext = [123 for _ in range(ceil(len(encoded_clear_input) / 8))]
    _itSignature = [bytes(65) for _ in range(ceil(len(encoded_clear_input) / 8))]
    kwargs = {
        'itValue': ((_itCiphertext,), _itSignature)
    }
    func_selector = deployed_contract.functions.setSomeEncryptedStringEncryptedInput(**kwargs).selector
    eoa_private_key = tx_params['eoa_private_key']
    hex_account_private_key = bytes.fromhex(eoa_private_key)
    input_text = build_string_input_text(clear_input, account_hex_encryption_key, eoa, deployed_contract, func_selector,
                                         hex_account_private_key)

    kwargs['itValue'] = input_text
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

    input_text_from_tx = decode(['(uint256,bytes)'], bytes.fromhex(tx_from_block['input'].hex()[10:]))[0][0]

    # assert that value encrypted locally was saved in block
    assert input_text['ciphertext'] == input_text_from_tx
    # assert that value saved in block is not clear
    assert str(input_text_from_tx) != str(user_some_value_clear)
    decrypted_input_from_tx = decrypt_uint(int(input_text_from_tx), account_hex_encryption_key)
    # assert that value saved in block is as clear after decryption
    assert int(decrypted_input_from_tx) == user_some_value_clear


def validate_block_has_tx_string_input_encrypted_value(tx_params, tx_receipt, user_some_value_clear,
                                                       account_hex_encryption_key, input_text, contract):
    tx_from_block = tx_params['web3'].eth.get_transaction_by_block(tx_receipt['blockHash'],
                                                                   tx_receipt['transactionIndex'])
    print(tx_from_block)
    tx_inputs = contract.decode_function_input(tx_from_block['input'].hex())
    ciphertexts = input_text['ciphertext']['value']
    for input_text_from_tx, input_text in zip(tx_inputs[1]['itValue']['ciphertext']['value'], ciphertexts):
        # assert that value encrypted locally was saved in block
        assert input_text == input_text_from_tx

    # Decode the bytes to a string
    string_from_input_tx = decrypt_string(tx_inputs[1]['itValue']['ciphertext'], account_hex_encryption_key)

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


def deploy(web3: Web3, eoa: Account, tx_params):
    kwargs = {}

    resource = importlib.resources.files('artifacts') / 'contracts' / 'DataOnChain.sol' / 'DataOnChain.json'

    with open(resource, 'r') as file:
        data = json.load(file)
    
    DataOnChain = web3.eth.contract(abi=data['abi'], bytecode=data['bytecode'])

    tx = DataOnChain.constructor().build_transaction({
        'from': eoa.address,
        'nonce': web3.eth.get_transaction_count(eoa.address)
    })

    signed_tx = web3.eth.account.sign_transaction(tx, eoa._private_key)

    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    deployed_contract = web3.eth.contract(address=tx_receipt.contractAddress, abi=data['abi'])

    print('contract address: ', deployed_contract.address)

    return deployed_contract


if __name__ == "__main__":
    main()