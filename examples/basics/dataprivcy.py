from tabulate import tabulate

from examples.onboard.onboard_account import *


def main():
    account_hex_encryption_key, eoa, eoa_private_key, web3 = init()

    gas_limit = 10000000
    gas_price_gwei = 30

    tx_params = {'web3': web3, 'gas_limit': gas_limit, 'gas_price_gwei': gas_price_gwei,
                 'eoa_private_key': eoa_private_key}
    deployed_contract = deploy(account_hex_encryption_key, eoa, tx_params)
    print_summary(deployed_contract, eoa)

    if is_operation_allowed(deployed_contract, eoa.address, "op_get_clear_coti_usd_price", eoa.address):
        get_clear_coti_usd_price(deployed_contract, tx_params)
    set_permission(deployed_contract, tx_params, "0x0000000000000000000000000000000000000001", "*", False, True,
                   False, 0, 0, 0, eoa.address, "")
    print_summary(deployed_contract, eoa)


def get_clear_coti_usd_price(deployed_contract, tx_params):
    func = deployed_contract.functions.get_clear_coti_usd_price()
    tx_receipt = exec_func_via_transaction(func, tx_params)
    print(tx_receipt)
    make_sure_tx_didnt_fail(tx_receipt)


def make_sure_tx_didnt_fail(tx_receipt):
    assert tx_receipt.status == 1


def print_summary(deployed_contract, eoa):
    conditions_count = get_conditions_count(deployed_contract, eoa)
    print('Number of conditions:' + str(conditions_count))
    conditions = deployed_contract.functions.getConditions(1, 10).call({'from': eoa.address})

    headers = ["Index", "Address", "Operation", "Is Active", "Always False", "Always True", "Timestamp Before",
               "Timestamp After", "Custom UInt", "Custom Address", "Custom String"]

    print(tabulate(conditions, headers=headers, tablefmt="grid"))


def set_permission(deployed_contract, tx_params, address, operation, active, trueKey, falseKey, timestampBefore,
                   timestampAfter, uintParameter, addressParameter, stringParameter):
    func = deployed_contract.functions.setPermission((address, operation, active, timestampBefore, timestampAfter,
                                                      falseKey, trueKey, uintParameter, addressParameter,
                                                      stringParameter))

    return exec_func_via_transaction(func, tx_params)


def is_operation_allowed(deployed_contract, caller, operation, eoa):
    if deployed_contract.functions.isOperationAllowed(caller, operation).call({'from': eoa}):
        return True
    else:
        print("operation: " + operation + " is not allowed")
        return False


def get_conditions_count(deployed_contract, eoa):
    return deployed_contract.functions.getConditionsCount().call({'from': eoa.address})


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
    contract_name = "OnChainDatabase"
    contract_file_name = contract_name + ".sol"
    relative_to_contracts_directory = "./"
    allowed_paths = ["./*", "../../lib/MpcCore.sol", "lib/MpcCore.sol"]
    deployed_contract, was_already_deployed = \
        get_deployed_contract(contract_name, contract_file_name, relative_to_contracts_directory, tx_params, kwargs,
                              allowed_paths)
    print('contract address: ', deployed_contract.address)
    return deployed_contract


main()
