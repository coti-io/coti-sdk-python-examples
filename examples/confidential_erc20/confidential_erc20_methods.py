from coti.crypto_utils import build_input_text, decrypt_uint

from examples.basics.utils import *


def approve(deployed_contract, kwargs, plaintext_integer, account_hex_encryption_key, eoa, tx_params):
    eoa_private_key = tx_params['eoa_private_key']
    func_selector = deployed_contract.functions.approve(**kwargs).selector
    hex_account_private_key = bytes.fromhex(eoa_private_key)
    input_text = build_input_text(plaintext_integer, account_hex_encryption_key, eoa, deployed_contract, func_selector,
                                     hex_account_private_key)
    kwargs['_itCT'] = input_text['ciphertext']
    kwargs['_itSignature'] = input_text['signature']
    func = deployed_contract.functions.approve(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def get_account_balance(account_hex_encryption_key, deployed_contract, eoa):
    cipher_text_balance = deployed_contract.functions.balanceOf(eoa.address).call({'from': eoa.address})
    account_balance = decrypt_uint(cipher_text_balance, account_hex_encryption_key)
    return account_balance


def approveClear(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.approveClear(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def transfer_from_clear(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.contractTransferFromClear(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def transfer_from(deployed_contract, kwargs, eoa, account_hex_encryption_key, plaintext_integer, tx_params):
    account_private_key = eoa.key.hex()[2:]  # tx_params['eoa_private_key']
    func_selector = deployed_contract.functions.transferFrom(**kwargs).selector
    hex_account_private_key = bytes.fromhex(account_private_key)
    input_text = build_input_text(plaintext_integer, account_hex_encryption_key, eoa, deployed_contract, func_selector,
                                     hex_account_private_key)
    kwargs['_itCT'] = input_text['ciphertext']
    kwargs['_itSignature'] = input_text['signature']
    func = deployed_contract.functions.transferFrom(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def transfer_encrypted(deployed_contract, kwargs, eoa, account_hex_encryption_key, tx_params):
    eoa_private_key = tx_params['eoa_private_key']
    plaintext_integer = kwargs['value'][0]
    func_selector = deployed_contract.functions.transfer(**kwargs).selector
    hex_account_private_key = bytes.fromhex(eoa_private_key)
    input_text = build_input_text(plaintext_integer, account_hex_encryption_key, eoa, deployed_contract, func_selector,
                                     hex_account_private_key)
    kwargs['value'] = input_text
    func = deployed_contract.functions.transfer(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def transfer_clear(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.contractTransferClear(**kwargs)
    return exec_func_via_transaction(func, tx_params)


def transfer(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.transfer(**kwargs)
    return exec_func_via_transaction(func, tx_params)

def mint(deployed_contract, kwargs, tx_params):
    func = deployed_contract.functions.mint(**kwargs)
    return exec_func_via_transaction(func, tx_params)