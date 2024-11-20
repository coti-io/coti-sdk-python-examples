from dotenv import load_dotenv

import importlib.resources
import json

from confidential_erc20_methods import *


# script deploys (or uses already deployed) confidential erc20 contract
# that is possible to transfer funds in a clear or encrypted manner
# pending enhancements: approval, allowance, mint in encrypted manner and gas estimations
def main():
    account_hex_encryption_key, eoa, eoa_private_key, web3 = init()

    gas_limit = 10000000
    gas_price_gwei = 30
    token_name = "My Confidential Token"
    token_symbol = "CTOK"
    token_initial_balance = 500000000

    tx_params = {'web3': web3, 'gas_limit': gas_limit, 'gas_price_gwei': gas_price_gwei,
                 'eoa_private_key': eoa_private_key}
    deployed_contract = deploy(web3, eoa, token_name, token_symbol, tx_params)
    view_functions(deployed_contract, eoa)
    testing_functions(deployed_contract, eoa, account_hex_encryption_key, tx_params)


def deploy(web3: Web3, eoa: Account, name, symbol, tx_params):
    kwargs = {
        'name_': name,
        'symbol_': symbol
    }
    resource = importlib.resources.files('artifacts') / 'contracts' / 'PrivateToken.sol' / 'PrivateToken.json'

    with open(resource, 'r') as file:
        data = json.load(file)
    
    PrivateToken = web3.eth.contract(abi=data['abi'], bytecode=data['bytecode'])

    tx = PrivateToken.constructor(**kwargs).build_transaction({
        'from': eoa.address,
        'nonce': web3.eth.get_transaction_count(eoa.address)
    })

    signed_tx = web3.eth.account.sign_transaction(tx, eoa._private_key)

    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    deployed_contract = web3.eth.contract(address=tx_receipt.contractAddress, abi=data['abi'])

    print('contract address: ', deployed_contract.address)

    return deployed_contract


def init():
    load_dotenv()  # loading .env
    eoa_private_key = get_account_private_key()  # Get EOA Private key for execution
    account_hex_encryption_key = get_hex_account_encryption_key()  # Get Hex key used to encrypt on network
    eoa = get_eoa(eoa_private_key)  # Get EOA
    web3 = init_web3(get_node_https_address(), eoa)  # Init connection to node
    validate_minimum_balance(web3)  # validate minimum balance
    return account_hex_encryption_key, eoa, eoa_private_key, web3


def testing_functions(deployed_contract, eoa, account_hex_encryption_key, tx_params):
    # Generate a new Ethereum account for Alice
    alice_address = Account.create()
    plaintext_integer = 5

    test_mint(deployed_contract, eoa, tx_params)
    account_balance_at_first = get_account_balance(account_hex_encryption_key, deployed_contract, eoa)
    account_balance_at_end = test_transfer_input_text(account_balance_at_first, account_hex_encryption_key, alice_address,
                                                      deployed_contract, eoa, plaintext_integer, tx_params)

    print('account balance at first: ', account_balance_at_first, ' account balance at end:', account_balance_at_end)


def test_mint(deployed_contract, eoa: Account, tx_params):
    print("************* Minting 500000000 to my address *************")
    kwargs = {'account': eoa.address, 'amount': 500000000}
    tx_receipt = mint(deployed_contract, kwargs, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)

def test_approve(account_hex_encryption_key, deployed_contract, eoa, tx_params):
    print("************* Approve InputText 50 to my address *************")
    kwargs = {'_spender': eoa.address, '_itCT': 50, '_itSignature': bytes(65)}
    tx_receipt = approve(deployed_contract, kwargs, 50, account_hex_encryption_key, eoa, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    allowance_cipher_text = deployed_contract.functions.allowance(eoa.address, eoa.address).call({'from': eoa.address})
    allowance = decrypt_uint(allowance_cipher_text, account_hex_encryption_key)
    assert allowance >= 50


def test_transfer_from(account_balance_before, account_hex_encryption_key, alice_address, deployed_contract, eoa,
                       plaintext_integer, tx_params, bob_address, bob_hex_encryption_key):
    print("************* Transfer clear ", plaintext_integer, " from my account to Alice with allowance **********")
    kwargs = {'_from': eoa.address, '_to': bob_address.address, '_itCT': 5,
              '_itSignature': bytes(65), 'revealRes': False}
    tx_receipt = transfer_from(deployed_contract, kwargs, bob_address, bob_hex_encryption_key, 5,
                               tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    account_balance_after = get_account_balance(account_hex_encryption_key, deployed_contract, eoa)
    assert account_balance_before - plaintext_integer == account_balance_after
    return account_balance_after


def test_approve(account_hex_encryption_key, deployed_contract, eoa, plaintext_integer, tx_params, bob_address):
    print("************* Approve ", plaintext_integer * 10, " to my address *************")
    allowance_amount = plaintext_integer * 10
    kwargs = {'_spender': bob_address.address, '_value': allowance_amount}
    tx_receipt = approveClear(deployed_contract, kwargs, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    allowance_cipher_text = deployed_contract.functions.allowance(eoa.address, bob_address.address).call(
        {'from': eoa.address})
    allowance = decrypt_uint(allowance_cipher_text, account_hex_encryption_key)
    assert allowance == allowance_amount


def test_transfer_input_text(account_balance_before, account_hex_encryption_key, alice_address, deployed_contract, eoa,
                             plaintext_integer, tx_params):
    print("************* Transfer IT ", plaintext_integer, " to Alice *************")
    kwargs = {'to': alice_address.address, 'value': (5, bytes(65))}
    tx_receipt = transfer_encrypted(deployed_contract, kwargs, eoa, account_hex_encryption_key, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)
    account_balance_after = get_account_balance(account_hex_encryption_key, deployed_contract, eoa)
    assert account_balance_before - plaintext_integer == account_balance_after
    return account_balance_after


def view_functions(deployed_contract, eoa):
    print("************* View functions *************")
    name = deployed_contract.functions.name().call({'from': eoa.address})
    print("Function call result name:", name)
    symbol = deployed_contract.functions.symbol().call({'from': eoa.address})
    print("Function call result symbol:", symbol)
    decimals = deployed_contract.functions.decimals().call({'from': eoa.address})
    print("Function call result decimals:", decimals)


if __name__ == "__main__":
    main()