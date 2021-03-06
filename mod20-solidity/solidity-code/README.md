# Financial Automation via Solidity

This repository contains Solidity code for three smart contracts (run over the Kovan Ethereum testnet) that handle compensation distribution in one of three ways:

* [`AssociateProfitSplitter.sol`](Solidity-Code/AssociateProfitSplitter.sol) - This will accept Ether into the contract and divide the Ether evenly among the associate level employees. This will allow the Human Resources department to pay employees quickly and efficiently.

!['AssociateProfitSplitter'](Images/associate.png)

* [`TieredProfitSplitter.sol`](Solidity-Code/TieredProfitSplitter.sol) - Will distribute different percentages of incoming Ether to employees at different tiers/levels. For example, the CEO gets paid 60%, CTO 25%, and Bob gets 15%.

!['TieredProfitSplitter'](Images/tiered.png)

* [`DeferredEquityPlan.sol`](Solidity-Code/DeferredEquityPlan.sol) - This models traditional company stock plans. This contract will automatically manage 1000 shares with an annual distribution of 250 over 4 years for a single employee.

!['DeferredEquityPlan'](Images/deferred.png)
