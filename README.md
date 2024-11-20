# COTI V2 Confidentiality Preserving L2 | SDKs and Examples

> [!NOTE]
> Please refer to the latest [tags](https://github.com/coti-io/coti-sdk-python-examples/tags) to find the most stable
version to use.

All repositories specified below contain smart contracts that implement confidentiality features using the COTI V2 protocol.
The contracts provide examples for various use cases, such as Non-Fungible Tokens (NFTs), ERC20 tokens, Auction, and Identity management.

These contracts demonstrate how to leverage the confidentiality features of the COTI V2 protocol to enhance privacy and security in decentralized applications.
The contracts are of Solidity and can be compiled and deployed using popular development tools like Hardhat and Foundry (Work in progress).

#### Important Links:

[Docs](https://docs.coti.io) | [Devnet Explorer](https://explorer-devnet.coti.io) | [Discord](https://discord.gg/cuCykh8P4m) | [Faucet](https://faucet.coti.io)

Interact with the network using any of the following:

1. [Python SDK](https://github.com/coti-io/coti-sdk-python) | [Python SDK Examples](https://github.com/coti-io/coti-sdk-python-examples)
2. [Typescript SDK](https://github.com/coti-io/coti-sdk-typescript) | [Typescript SDK Examples](https://github.com/coti-io/coti-sdk-typescript-examples)
3. [Hardhat Dev Environment](https://github.com/coti-io/confidentiality-contracts)

The following contracts are available in each of the packages:

| Contract                       |            | python sdk | hardhat sdk | typescript sdk | Contract Description                                                                                                                          |
|--------------------------------|------------|------------|-------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `AccountOnboard`               | deployment | ✅ *        | ✅           | ❌              | Onboard a EOA account - During onboard network creates AES unique for that EOA which is used for decrypting values sent back from the network |
| `AccountOnboard`               | execution  | ✅          | ✅           | ✅              | "                                                                                                                                             |
| `ERC20Example`                 | deployment | ✅          | ✅           | ❌              | Confidential ERC20 - deploy and transfer encrypted amount of funds                                                                            |
| `ERC20Example`                 | execution  | ✅          | ✅           | ✅              | "                                                                                                                                             |
| `NFTExample`                   | deployment | ❌          | ✅           | ❌              | Confidential NFT example - saving encrypted data                                                                                              |
| `NFTExample`                   | execution  | ❌          | ✅           | ❌              | "                                                                                                                                             |
| `ConfidentialAuction`          | deployment | ❌          | ✅           | ❌              | Confidential auction - encrypted bid amount                                                                                                   |
| `ConfidentialAuction`          | execution  | ❌          | ✅           | ❌              | "                                                                                                                                             |
| `ConfidentialIdentityRegistry` | deployment | ❌          | ✅           | ❌              | Confidential Identity Registry - Encrypted identity data                                                                                      |
| `ConfidentialIdentityRegistry` | execution  | ❌          | ✅           | ❌              | "                                                                                                                                             |
| `DataOnChain`                  | deployment | ✅          | ❌           | ❌              | Basic encryption and decryption - Good place to start explorining network capabilties                                                         |
| `DataOnChain`                  | execution  | ✅          | ❌           | ✅              | "                                                                                                                                             |
| `Precompile`                   | deployment | ✅          | ✅           | ❌              | Thorough examples of the precompile functionality                                                                                             |
| `Precompile`                   | execution  | ✅          | ✅           | ❌              | "                                                                                                                                             |-              |              

(*) no deployment needed (system contract)

> [!NOTE]  
> Due to the nature of ongoing development, future version might break existing functionality

### Faucet

🤖 To request devnet/testnet funds use our [faucet](https://faucet.coti.io)

# COTI v2 Python SDK Examples

> [!NOTE]
> Please refer to the latest [tags](https://github.com/coti-io/coti-sdk-python-examples/tags) to find the most stable version to use. 

The examples project contains scripts covering various use cases, such as Non-Fungible Tokens (NFTs), ERC20 tokens, Auction, and Identity management. It contains smart contracts that implement confidentiality features using the COTI V2 protocol. These contracts demonstrate how to leverage the confidentiality features of the COTI V2 protocol to implement privacy and enhance security in decentralized applications.

The contracts are written in Solidity and can be compiled and deployed using popular development frameworks such as
Hardhat and Foundry.

The following example contracts are available in the Python SDK for deployment and execution:

| Contract       | Contract Description                                                                                                                          |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| AccountOnboard | Onboard a EOA account - During onboard network creates AES unique for that EOA which is used for decrypting values sent back from the network |
| ERC20Example   | Confidential ERC20 - deploy and transfer encrypted amount of funds                                                                            |
| DataOnChain    | Basic encryption and decryption - Good place to start exploring network capabilities                                                          |

> [!NOTE]  
> Due to the nature of ongoing development, future versions might break existing functionality

## Getting initial funds from the COTI Faucet

The COTI faucet provides devnet/testnet funds for developers. To request devnet/testnet tokens:

1. Head to https://faucet.coti.io/
2. Send a message to the bot in the following format:

```
devnet <your_eoa_address> 
```

For Example:

```
devnet 0x71C7656EC7ab88b098defB751B7401B5f6d8976F
```

## Python SDK Usage

The sample scripts described above reside in the [coti-sdk-python-examples/examples](/examples/) directory, while the solidity contracts are in the [coti-contracts-examples](https://github.com/coti-io/coti-contracts-examples) repository.

When a script executed (for example `data_on_chain.py`) it will deploy the contract.

Inspect the `.env` file for more details.

## Pre-requisites

1. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. [Python >= 3.9, <= 3.10](https://www.python.org/downloads/)
3. [pip](https://pip.pypa.io/en/stable/installation/)

## Getting Started

### Native Transfer

The following process will help you deploy the [**`native_transfer.py`**](https://github.com/coti-io/coti-sdk-python-examples/blob/master/examples/basics/native\_transfer.py) example from the [**COTI Python SDK Examples**](https://github.com/coti-io/coti-sdk-python-examples) project. This script will transfer native funds from your wallet account to a random wallet. It will also:

* Create a EOA (Externally Owned Account)
* Validate minimum balance

> [!TIP]
> Ensure your environment meets all the pre-requisites. Visit the [pre-requisites section of the readme](https://github.com/coti-io/coti-sdk-python/tree/main?tab=readme-ov-file#python-sdk-coti-sdk-python---usage). Alternatively, use an editor like [PyCharm](https://www.jetbrains.com/pycharm/download/) to take care of the pre-requisites for you.

1.  Clone the Python examples repo along with its submodules into your desired location

    ```bash
    git clone --recurse-submodules https://github.com/coti-io/coti-sdk-python-examples.git
    ```


2.  Change directory to the newly create one

    ```bash
    cd coti-sdk-python-examples
    ```


3.  Install the project's requirements

    ```bash
    python3 -m pip install -r requirements.txt
    ```


4.  Set the python path as following

    ```bash
    export PYTHONPATH=$PWD
    ```


5.  Run the `native_transfer.py` script

    ```bash
    python3 examples/basics/native_transfer.py
    ```

    Running the script will automatically create an account and a key/value pair with name: `ACCOUNT_PRIVATE_KEY` (visible in the `.env` file). The script will output something like this:



    ```bash
    So you dont have an account yet, dont worry... lets create one right now!
    Creation done!
    provider:  https://devnet.coti.io
    chain-id:  13068200
    latest block:  0xc9ec7259bad015c46a0bef9b0988cac70a62e2abaed7459b5265e425bc5cecb8
    account address: 0x0287a7A5bD5f4802D4A6048730a11B2713A16bd4
    account balance:  0 wei ( 0  ether)
    account nonce:  0
    Traceback (most recent call last):
      File "/Users/user/projects/coti-sdk-python/examples/basics/native_transfer.py", line 24, in <module>
        main()
      File "/Users/user/projects/coti-sdk-python/examples/basics/native_transfer.py", line 12, in main
        validate_minimum_balance(web3)  # validate minimum balance
      File "/Users/user/projects/coti-sdk-python/examples/basics/utils.py", line 69, in validate_minimum_balance
        raise Exception(
    Exception: Not enough balance!, head to discord faucet and getsome...https://discord.com/channels/386571547508473876/1235539223595978752 , ask the BOT:devnet 0x0287a7A5bD5f4802D4A6048730a11B2713A16bd4

    Process finished with exit code 1

    ```

    \
    It is normal to receive the exception `Not enough balance!` on the first run. This will be resolved once the account is funded.

6. Head to the faucet at [**https://faucet.coti.io**](https://faucet.coti.io) to get devnet funds. \
   Send the following message to the BOT using your newly created `account address`:\
   \
   `devnet <account address>`\
   \
   The bot will reply with the message:\
   \
   `<username> faucet transferred 5 COTIv2 (devnet)` \
   &#x20;
7.  Run the `native_transfer.py` script once more

    ```bash
    python3 examples/basics/native_transfer.py
    ```

    \
    The script will output as following:

    ```bash
    provider:  https://devnet.coti.io
    chain-id:  13068200
    latest block:  0x4f5b68d9ef7debc0f86b4fc4c50a81020c8de315d65b4ce12b4372ebedef4f95
    account address: 0x0287a7A5bD5f4802D4A6048730a11B2713A16bd4
    account balance:  10000000000000000000 wei ( 10  ether)
    account nonce:  0
    AttributeDict({'blockHash': HexBytes('0x3e0534655361da10c9ee6454d622609c900e3f552435acc9cc963e370ca1d36b'), 'blockNumber': 3395902, 'contractAddress': None, 'cumulativeGasUsed': 21000, 'effectiveGasPrice': 1000000000, 'from': '0x0287a7A5bD5f4802D4A6048730a11B2713A16bd4', 'gasUsed': 21000, 'logs': [], 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 'status': 1, 'to': '0x4A68774D7679e63Ea42599Fe076a899036B3642B', 'transactionHash': HexBytes('0x99ad02f33a146945ac3a671857ab5134965b1f3e78fd53a97710bcdcb99dfee7'), 'transactionIndex': 0, 'type': 0})
    ```

    \
    Now that your account is created and funded, you can now onboard the account to get your new network key.

## On-board Account

The following process will help you deploy the [**`onboard_account.py`**](https://github.com/coti-io/coti-sdk-python/blob/main/examples/onboard/onboard\_account.py) example from the [**COTI Python SDK Examples**](https://github.com/coti-io/coti-sdk-python-examples) repo. This script onboards an EOA into the network. It will also:

* Trigger the network to create a unique AES key for the user
* Encrypt the unique user-specific AES key using the Public key so that its value can be viewed only by the EOA owner.

This is a mandatory script for any operation executed in any contract requiring encrypt/decrypt operations which are part of the new EVM precompiles actions.

1.  Run the `onboard_account.py` script

    ```bash
    python3 examples/onboard/onboard_account.py
    ```

    \
    Running the script will automatically create an account and an `ACCOUNT_ENCRYPTION_KEY` (visible in the `.env` file as well as the output). The script output will look something like this:


    ```bash
    provider:  https://devnet.coti.io
    chain-id:  13068200
    latest block:  0x31f5e889a74777e514abcf83ece21839d96c465419b66b6b977f65d052062c2a
    account address: 0x0287a7A5bD5f4802D4A6048730a11B2713A16bd4
    account balance:  9999936985000000000 wei ( 9.999936985  ether)
    account nonce:  3
    tx receipt:  AttributeDict({'blockHash': HexBytes('0x94dac5f2cf57639fe934457cb33354399567cfad233c2fb3d6a271ecd47830a3'), 'blockNumber': 3399673, 'contractAddress': None, 'cumulativeGasUsed': 225968, 'effectiveGasPrice': 30000000000, 'from': '0x0287a7A5bD5f4802D4A6048730a11B2713A16bd4', 'gasUsed': 225968, 'logs': [AttributeDict({'address': '0xbFC922C10B03EA5dbC90b98dfc8fb334849ccB78', 'topics': [HexBytes('0xb67504ecfeef0230a06f661ea388c2947b4125a35e918ebff5889e3553c29c04'), HexBytes('0x0000000000000000000000000287a7a5bd5f4802d4a6048730a11b2713a16bd4')], 'data': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000100702c1a6221b95f4730a6ff7e7e96d4362d75558386340a381714a64ac40cb4100e5e27e5f9606fbc5e89b2064062d15d4a7ad671428ac128eb76eaed7534f36e0829fb4e4cf090db7ae6e1ba3728e6870fe29617c80ec1d0fcfd5c5b39eec6b7252e2d0a1e8f89cf786d9abd288c74e2cad8006f8c8065e6f3ff73bf164d2d9a0e708f26ff938890ea7191655ef6f0a5ffe9acaddaf9f614b2ecc9faf86cfc041b6704cc4865429b069c0fbc02b83ecc5c45f54501542de2c08b85d7c2a88370503c5d7f04ca6e7b0fffeb89dc7b3c8e5834943e93899bab6bc0ac9ce58e8d59247ab8dd7c096c1fe5e65f48a5c3fb6e85e2a6d43f829ebc5da0c75740df33fd'), 'blockNumber': 3399673, 'transactionHash': HexBytes('0x69af701a8f65ebf6c007e512ce6bc5e801884c3ae49ad744f47069053e2ed81e'), 'transactionIndex': 0, 'blockHash': HexBytes('0x94dac5f2cf57639fe934457cb33354399567cfad233c2fb3d6a271ecd47830a3'), 'logIndex': 0, 'removed': False})], 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000400000000000000000000001000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000008000000000000000000000000000000000440000000000000000000000000000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000040000000000000000000000000000000'), 'status': 1, 'to': '0xbFC922C10B03EA5dbC90b98dfc8fb334849ccB78', 'transactionHash': HexBytes('0x69af701a8f65ebf6c007e512ce6bc5e801884c3ae49ad744f47069053e2ed81e'), 'transactionIndex': 0, 'type': 0})
    (True, 'ACCOUNT_ENCRYPTION_KEY', 'fd3d781ddcbd1e1cedd2d75460f30636')
    ```

> [!CAUTION]
> This encryption key is **sensitive.** Ensure it is not uploaded to public places and keep it safe. This key is produced per EOA wallet, meaning a unique wallet/EOA combination will have a unique encryption key.


The `.env` file will also have other useful information, such as the node address, websocket address, and the contract directories.  

Now that the account is onboarded, let's deploy a contract on-chain.

## Deploy Data On-Chain

The following process will help you deploy the [**`data_on_chain.py`**](https://github.com/coti-io/coti-sdk-python-examples/blob/master/examples/data\_onchain/data\_on\_chain.py) example from the [**COTI Python SDK Examples**](https://github.com/coti-io/coti-sdk-python-examples) repo. As its name suggests, the contract will compile and deploy the corresponding [**`DataOnChain.sol`**](https://github.com/coti-io/coti-contracts-examples/blob/main/contracts/DataOnChain.sol) contract, located in the `coti-contracts-examples` directory.

This contract can be used in order to browse and get a feel of the COTI network. The contract allows for the secure handling of encrypted data, enabling storage, transformation, and arithmetic operations on encrypted values using the [**`MpcCore`**](https://github.com/coti-io/coti-contracts/blob/main/contracts/utils/mpc/MpcCore.sol) library. It supports operations where values are encrypted using both network and user keys, ensuring data privacy and security on-chain.


1.  Run the `data_on_chain.py` script

    ```bash
    python3 examples/data_onchain/data_on_chain.py
    ```

    \
    Running the script will deploy the contract and output the address where the contract was deployed. The script output will look something like this (with some omitted block hashes at the end of ther response):\


    ```bash
    provider:  https://devnet.coti.io/rpc
    chain-id:  13068200
    latest block:  0x75a2f9d10db48fdc53f14d9ce565420e680b06231cd34e3c194f14fbd0c5f999
    account address: 0xB101fbd6938AaE2e472E247e36555528d7ff4A89
    account balance:  4993201875000000000 wei ( 4.993201875  ether)
    account nonce:  2
    Compiling DataOnChain...
    Deploying DataOnChain...
    Contract deployed at address: 0x91Af1CD8Bbc3b7dCcd5fF19f522cd9A49067F928
    contract address:  0x91Af1CD8Bbc3b7dCcd5fF19f522cd9A49067F928
    ```

    \
    The deployment will include the transaction data as well as the address the contract was deployed to:

    ```bash
    Contract deployed at address: 0x91Af1CD8Bbc3b7dCcd5fF19f522cd9A49067F928
    ```

    \
    You can now view the contract on devnet explorer using the following convention:\
    `https://explorer-devnet.coti.io/address/<contract deployment address>` \
    \
    In our case: \
    [**https://explorer-devnet.coti.io/contract/0x91af1cd8bbc3b7dccd5ff19f522cd9a49067f928**](https://explorer-devnet.coti.io/contract/0x91af1cd8bbc3b7dccd5ff19f522cd9a49067f928)

Let's note the following facts about the contract and the script:

*   When the contract was deployed, the `uint64 private clearValue` variable was assigned a value of `5` as evidenced by [lines 15-17](https://github.com/coti-io/coti-contracts-examples/blob/befb346932dcf2feb380a8493f85faf0962bdb7b/contracts/DataOnChain.sol#L9) of the contract:&#x20;

    ```solidity
     constructor () {
            clearValue = 5;
        }
    ```
* The function [`getSomeValue`](https://github.com/coti-io/coti-contracts-examples/blob/befb346932dcf2feb380a8493f85faf0962bdb7b/contracts/DataOnChain.sol#L89) of the contract will then return the value of `clearValue`

Now let's take a look on at the basic flow that sends a clear value, encrypts it, and decrypts it.

* The python function [`basic_clear_encrypt_decrypt`](https://github.com/coti-io/coti-sdk-python-examples/blob/master/examples/data\_onchain/data\_on\_chain.py#L429) initiates the process, calling other functions as necessary.
* The python function [`save_clear_value_network_encrypted_in_contract`](https://github.com/coti-io/coti-sdk-python-examples/blob/master/examples/data\_onchain/data\_on\_chain.py#L504) is used to pass a clear value from the user.&#x20;
* Once the value is populated, the script will call the Solidity contract and use its [`setSomeEncryptedValue`](https://github.com/coti-io/confidentiality-contracts/blob/main/contracts/examples/DataOnChain.sol#L41-L43) function. This function in turn calls `setPublic64` from the [`MpcCore`](https://github.com/coti-io/coti-contracts/blob/main/contracts/utils/mpc/MpcCore.sol)  library, which turns the value into GarbledText and then into CipherText using the network key. This value is now encrypted in a network block.
* In order to validate the block had a ClearText input, the block details from the transaction are extracted using the [`validate_block_has_tx_input_encrypted_value`](https://github.com/coti-io/coti-sdk-python-examples/blob/master/examples/data\_onchain/data\_on\_chain.py#L528) function.
* The value is then encrypted using the function [`save_network_encrypted_to_user_encrypted_input_in_contract`](https://github.com/coti-io/coti-sdk-python-examples/blob/master/examples/data\_onchain/data\_on\_chain.py#L602)  , this function saves the network-encrypted value to the user-encrypted input in the contract.
* The encrypted value is retrieved from the contract using the function [`get_user_encrypted_from_contract`](https://github.com/coti-io/coti-sdk-python-examples/blob/master/examples/data\_onchain/data\_on\_chain.py#L563) to ensure the encrypted value can be successfully retrieved with the user's AES key.

## Pending enhancements

* Extending examples such as confidential ERC20 minting, confidential NFT (deployment and actions) and more.

#### To report issues, please create a [github issue](https://github.com/coti-io/coti-sdk-python-examples/issues)
