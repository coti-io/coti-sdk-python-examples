from coti.crypto_utils import *
from dotenv import load_dotenv

from examples.basics.utils import *

false = False
true = True

devnet_onboard_contract = {
    "contract_name": "AccountOnboard",
    "address": "0x1599155BF43e67B032E49D86600078b1A050D94f",
    "abi": [
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
            "internalType": "bytes",
            "name": "userKey",
            "type": "bytes"
            }
        ],
        "name": "AccountOnboarded",
        "type": "event"
        },
        {
        "inputs": [
            {
            "internalType": "bytes",
            "name": "publicKey",
            "type": "bytes"
            },
            {
            "internalType": "bytes",
            "name": "signedEK",
            "type": "bytes"
            }
        ],
        "name": "onboardAccount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
        }
    ],
    "bytecode": "0x608060405234801561001057600080fd5b506004361061002b5760003560e01c8063afaea1bd14610030575b600080fd5b61004a6004803603810190610045919061031d565b61004c565b005b600061005a858585856100b1565b90503373ffffffffffffffffffffffffffffffffffffffff167fb67504ecfeef0230a06f661ea388c2947b4125a35e918ebff5889e3553c29c04826040516100a2919061042e565b60405180910390a25050505050565b6060600085859050848490506100c79190610489565b67ffffffffffffffff8111156100e0576100df6104bd565b5b6040519080825280601f01601f1916602001820160405280156101125781602001600182028036833780820191505090505b50905060005b8484905081101561018f57848482818110610136576101356104ec565b5b9050013560f81c60f81b828281518110610153576101526104ec565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a9053508080600101915050610118565b5060005b86869050811015610218578686828181106101b1576101b06104ec565b5b9050013560f81c60f81b8282878790506101cb9190610489565b815181106101dc576101db6104ec565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a9053508080600101915050610193565b50606473ffffffffffffffffffffffffffffffffffffffff1663a85f0ca2826040518263ffffffff1660e01b8152600401610253919061042e565b600060405180830381865afa158015610270573d6000803e3d6000fd5b505050506040513d6000823e3d601f19601f82011682018060405250810190610299919061060d565b915050949350505050565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b600080fd5b60008083601f8401126102dd576102dc6102b8565b5b8235905067ffffffffffffffff8111156102fa576102f96102bd565b5b602083019150836001820283011115610316576103156102c2565b5b9250929050565b60008060008060408587031215610337576103366102ae565b5b600085013567ffffffffffffffff811115610355576103546102b3565b5b610361878288016102c7565b9450945050602085013567ffffffffffffffff811115610384576103836102b3565b5b610390878288016102c7565b925092505092959194509250565b600081519050919050565b600082825260208201905092915050565b60005b838110156103d85780820151818401526020810190506103bd565b60008484015250505050565b6000601f19601f8301169050919050565b60006104008261039e565b61040a81856103a9565b935061041a8185602086016103ba565b610423816103e4565b840191505092915050565b6000602082019050818103600083015261044881846103f5565b905092915050565b6000819050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b600061049482610450565b915061049f83610450565b92508282019050808211156104b7576104b661045a565b5b92915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b600080fd5b610529826103e4565b810181811067ffffffffffffffff82111715610548576105476104bd565b5b80604052505050565b600061055b6102a4565b90506105678282610520565b919050565b600067ffffffffffffffff821115610587576105866104bd565b5b610590826103e4565b9050602081019050919050565b60006105b06105ab8461056c565b610551565b9050828152602081018484840111156105cc576105cb61051b565b5b6105d78482856103ba565b509392505050565b600082601f8301126105f4576105f36102b8565b5b815161060484826020860161059d565b91505092915050565b600060208284031215610623576106226102ae565b5b600082015167ffffffffffffffff811115610641576106406102b3565b5b61064d848285016105df565b9150509291505056fea2646970667358221220f93dffb367f978fdbf9612875f75b512e6ad4bce999dcc63cb75823ef01d77d364736f6c63430008180033"
}


# Script onboards a EOA into the network, meaning, creates a AES key unique to that user,
# and that key will be used to encrypt all data sent back to the wallet
# mandatory script for any operation done in a contract that requires
# encrypt/decrypt (which is basically all new precompiles operations introduced)
def main():
    eoa_private_key, web3 = init()

    gas_limit = 10000000
    gas_price_gwei = 30
    tx_params = {'web3': web3, 'gas_limit': gas_limit, 'gas_price_gwei': gas_price_gwei,
                 'eoa_private_key': eoa_private_key, "address": web3.eth.default_account.address}

    # following uses an already pre-deployed contract that sends back encrypted AES key
    deployed_contract = get_contract(web3, devnet_onboard_contract['abi'],
                                     devnet_onboard_contract['bytecode'],
                                     devnet_onboard_contract['address'])
    if deployed_contract is None:
        deployed_contract = deploy_onboard_contract(tx_params)

    decrypted_aes_key = onboard_for_aes_key(deployed_contract, eoa_private_key, tx_params)
    env_value = set_hex_account_encryption_key(decrypted_aes_key.hex())
    if env_value[0] is not True:
        raise Exception('encryption key not saved in .env!')
    print(env_value)


def onboard_for_aes_key(deployed_contract, eoa_private_key, tx_params):
    # Generate new RSA key pair that is only used to encrypt back the account network key,
    # public key that sent to node, node will encrypt the account network key using public key
    # once its back client will decrypt using private key
    private_key, public_key = generate_rsa_keypair()
    # Sign the public key
    signature = sign(public_key, bytes.fromhex(eoa_private_key))
    kwargs = {"publicKey": public_key, "signature": signature}
    tx_receipt = onboard_user(deployed_contract, kwargs, tx_params)
    print("tx receipt: ", tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    encrypted_user_aes_from_network = tx_receipt.logs[0].data[64:]
    # only the private key could decrypt the account secret key
    decrypted_aes_key = decrypt_rsa(private_key, encrypted_user_aes_from_network)
    return decrypted_aes_key


def deploy_onboard_contract(tx_params):
    kwargs = {}
    contract_name = "AccountOnboard"
    contract_file_name = "AccountOnboard.sol"
    relative_to_contracts_directory = "AccountOnboard/"
    relative_to_mpc_core = "../lib/MpcCore.sol"
    deployed_contract, was_already_deployed = \
        get_deployed_contract(contract_name, contract_file_name, relative_to_contracts_directory, tx_params, kwargs,
                              relative_to_mpc_core)
    print('contract address: ', deployed_contract.address)
    return deployed_contract


def init():
    load_dotenv()  # loading .env
    eoa_private_key = get_account_private_key()  # Get EOA Private key for execution
    eoa = get_eoa(eoa_private_key)  # Get EOA
    web3 = init_web3(get_node_https_address(), eoa)  # Init connection to node
    return eoa_private_key, web3


def onboard_user(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.onboardAccount(*kwargs.values())
    return exec_func_via_transaction(func, tx_params)


if __name__ == "__main__":
    main()
