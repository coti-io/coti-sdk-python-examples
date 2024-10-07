from coti.crypto_utils import *
from dotenv import load_dotenv

from examples.basics.utils import *

false = False
true = True

testnet_onboard_contract = {"contract_name": "AccountOnboard", "address": "0x60eA13A5f263f77f7a2832cfEeF1729B1688477c",
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
                                           "name": "userKey1",
                                           "type": "bytes"
                                       },
                                       {
                                           "indexed": false,
                                           "internalType": "bytes",
                                           "name": "userKey2",
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
                            "bytecode": "0x608060405234801561001057600080fd5b5061087f806100206000396000f3fe608060405234801561001057600080fd5b506004361061002b5760003560e01c8063afaea1bd14610030575b600080fd5b61004a600480360381019061004591906104d9565b61004c565b005b60008061005b868686866100b7565b915091503373ffffffffffffffffffffffffffffffffffffffff167ffc83efa19b7c2bc399a672494bb0af52f9bbd678357edf30e55b5ac4e65878ba83836040516100a79291906105ea565b60405180910390a2505050505050565b606080600086869050858590506100ce919061065a565b67ffffffffffffffff8111156100e7576100e661068e565b5b6040519080825280601f01601f1916602001820160405280156101195781602001600182028036833780820191505090505b50905060005b858590508110156101965785858281811061013d5761013c6106bd565b5b9050013560f81c60f81b82828151811061015a576101596106bd565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350808060010191505061011f565b5060005b8787905081101561021f578787828181106101b8576101b76106bd565b5b9050013560f81c60f81b8282888890506101d2919061065a565b815181106101e3576101e26106bd565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350808060010191505061019a565b506000606473ffffffffffffffffffffffffffffffffffffffff1663a85f0ca2836040518263ffffffff1660e01b815260040161025c91906106ec565b6000604051808303816000875af115801561027b573d6000803e3d6000fd5b505050506040513d6000823e3d601f19601f820116820180604052508101906102a49190610800565b9050600061010067ffffffffffffffff8111156102c4576102c361068e565b5b6040519080825280601f01601f1916602001820160405280156102f65781602001600182028036833780820191505090505b509050600061010067ffffffffffffffff8111156103175761031661068e565b5b6040519080825280601f01601f1916602001820160405280156103495781602001600182028036833780820191505090505b50905060005b82518110156103c55783818151811061036b5761036a6106bd565b5b602001015160f81c60f81b838281518110610389576103886106bd565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a905350808060010191505061034f565b5060005b815181101561044c5783610100826103e1919061065a565b815181106103f2576103f16106bd565b5b602001015160f81c60f81b8282815181106104105761040f6106bd565b5b60200101907effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916908160001a90535080806001019150506103c9565b508181955095505050505094509492505050565b6000604051905090565b600080fd5b600080fd5b600080fd5b600080fd5b600080fd5b60008083601f84011261049957610498610474565b5b8235905067ffffffffffffffff8111156104b6576104b5610479565b5b6020830191508360018202830111156104d2576104d161047e565b5b9250929050565b600080600080604085870312156104f3576104f261046a565b5b600085013567ffffffffffffffff8111156105115761051061046f565b5b61051d87828801610483565b9450945050602085013567ffffffffffffffff8111156105405761053f61046f565b5b61054c87828801610483565b925092505092959194509250565b600081519050919050565b600082825260208201905092915050565b60005b83811015610594578082015181840152602081019050610579565b60008484015250505050565b6000601f19601f8301169050919050565b60006105bc8261055a565b6105c68185610565565b93506105d6818560208601610576565b6105df816105a0565b840191505092915050565b6000604082019050818103600083015261060481856105b1565b9050818103602083015261061881846105b1565b90509392505050565b6000819050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b600061066582610621565b915061067083610621565b92508282019050808211156106885761068761062b565b5b92915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b6000602082019050818103600083015261070681846105b1565b905092915050565b600080fd5b61071c826105a0565b810181811067ffffffffffffffff8211171561073b5761073a61068e565b5b80604052505050565b600061074e610460565b905061075a8282610713565b919050565b600067ffffffffffffffff82111561077a5761077961068e565b5b610783826105a0565b9050602081019050919050565b60006107a361079e8461075f565b610744565b9050828152602081018484840111156107bf576107be61070e565b5b6107ca848285610576565b509392505050565b600082601f8301126107e7576107e6610474565b5b81516107f7848260208601610790565b91505092915050565b6000602082840312156108165761081561046a565b5b600082015167ffffffffffffffff8111156108345761083361046f565b5b610840848285016107d2565b9150509291505056fea2646970667358221220b9ef12093036f880e2c927bf49d4bc43abb14a9af8f661cd21085081a1fc69ee64736f6c63430008180033",
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
    deployed_contract = get_contract(web3, testnet_onboard_contract['abi'],
                                     testnet_onboard_contract['bytecode'],
                                     testnet_onboard_contract['address'])
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

    user_key_events = deployed_contract.events.AccountOnboarded().process_receipt(tx_receipt)
    key_0_share = user_key_events[0].args.userKey1
    key_1_share = user_key_events[0].args.userKey2

    if key_0_share is None or key_1_share is None:
        raise Exception("Failed to find the key shares of the account address in the transaction receipt.")

    decrypted_aes_key = recover_user_key(private_key, key_0_share, key_1_share)
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
