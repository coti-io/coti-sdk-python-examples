# COTI V2 Confidentiality Preserving L2 | SDKs and Examples

All repositories specified below contain smart contracts that implement confidentiality features using the COTI V2 protocol.
The contracts provide examples for various use cases, such as Non-Fungible Tokens (NFTs), ERC20 tokens, Auction, and Identity management.

These contracts demonstrate how to leverage the confidentiality features of the COTI V2 protocol to enhance privacy and security in decentralized applications.
The contracts are of Solidity and can be compiled and deployed using popular development tools like Hardhat and Foundry (Work in progress).

#### Important Links:

[Docs](https://docs.coti.io) | [Devnet Explorer](https://explorer-devnet.coti.io) | [Faucet](https://faucet.coti.io)

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

The examples project contains scripts covering various use cases, such as Non-Fungible Tokens (NFTs), ERC20 tokens, Auction, and Identity management. It contains smart contracts that implement confidentiality features using the COTI V2 protocol. These contracts demonstrate how to leverage the confidentiality features of the COTI V2 protocol to implement privacy and enhance security in decentralized applications.

The contracts are written in Solidity and can be compiled and deployed using popular development frameworks such as
Hardhat and Foundry.

The following example contracts are available in the Python SDK for deployment and execution:

| Contract       | Contract Description                                                                                                                          |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| AccountOnboard | Onboard a EOA account - During onboard network creates AES unique for that EOA which is used for decrypting values sent back from the network |
| ERC20Example   | Confidential ERC20 - deploy and transfer encrypted amount of funds                                                                            |
| DataOnChain    | Basic encryption and decryption - Good place to start exploring network capabilities                                                          |
| Precompile     | Thorough examples of the precompile functionality                                                                                             |

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

The sample contracts described above reside in the [coti-sdk-python-examples/examples](/examples/) directory. The solidity contracts are in the [confidentiality-contracts](/confidentiality-contracts/) directory which is imported as a git submodule.

When a script executed (for example `data_on_chain.py`) it will deploy the contract and create a json file with the details of the deployed contract under the `/compiled_contracts` directory.

Inspect the `.env` file for more details.

The python examples utilizes primitive deployment management that mostly checks if there is a json file under the `/compiled_contracts` directory and doesn't deploy a new one in case one already exists, otherwise it deploys.

### Getting Started

1. Generate EOA: Run the `native_transfer.py` script, it will transfer a small amount of COTI2 to some random address - demonstrating standard native transfer. It will create a new EOA (you will see your public address in the script output), and the account private key will be recorded in your `.env` file. It will fail on first run since the account doesn't have any funds. Refer to the Faucet section above

2. Generate Encryption Key: Run the `onboard_account.py` script, it will ask the network for the AES encryption key specific for this account and it will log it in the `.env` file (mandatory for every action that performs COTI v2 onchain computation).

3. Execute: Now you can run any other example, such as `precompiles_examples.py` (see above for complete list).

In order to follow the transactions sent to the node, use the `web_socket.py` to be notified and see on-chain details.

## Pending enhancements

* Extending examples such as confidential ERC20 minting, confidential NFT (deployment and actions) and more.

#### To report issues, please create a [github issue](https://github.com/coti-io/coti-sdk-python/issues)
