# Brief Update on Maker's RWA Portfolio

*We prepared the brief below for Aave DAO's consideration. We are actively monitoring changes in DAI collateral and are determined to provide timely updates as the situation evolves.*

## Summary

In September 2023, we examined [Maker's exposure to real-world assets](https://cryptorisks.substack.com/p/asset-risk-assessment-dai-exposure) (RWA), most notably exposure to short-term bonds, Coinbase Custody, and private credit. While the macro environment has changed since then, with on-chain yields now exceeding Treasury bill yields, monitoring these RWA positions backing DAI remains important. This brief aims to provide an update on the Monetalis arrangements and review the proposed structure for onboarding additional USDe.

## DAI Collateral and Revenue Generation

Recent data from Makerburn indicates that DAI allocated to Morpho and Spark through the D3M facility is now generating substantial yields for Maker. These on-chain revenues have overshadowed RWA-yielding strategies, leading to a reduced focus on such approaches. Notably, the Monetalis Clydesdale vault, once a top revenue earner, has now fallen out of the top five contributors.

![image|850x824](upload://79r1BQOlwYRjRTFYhPCye603foa.png)
Source: [Makerburn](https://makerburn.com/#/rundown), May 22nd, 2024

## Review of Monetalis Arrangements

In light of the recent [findings](http://forum.makerdao.com/t/mip102c2-sp30-mip-amendment-subproposal/23729/2) regarding Monetalis's non-performance, the notes herein aim to examine the role of Monetalis in the RWA structure devised by MakerDAO. The Coinbase Custody [Legal Assessment](https://forum.makerdao.com/t/coinbase-custody-legal-assessment/20384/17) discloses the [reporting agreement](https://gateway.pinata.cloud/ipfs/QmaTv4e42sUQ8DzefdzWisHZoJnQdAcSpqjmjP4EFvQVhr) between JAMES ASSET (PTC) LIMITED ("JAL") and MONETALIS SERVICES LIMITED ("Monetalis").

Incorporated under British Virgin Islands laws, Monetalis has agreed to act as the Reporting Agent. The firm was tasked with delivering specific reporting services pertinent to the management of trust assets, notably concerning the intended reallocation of 500 million USDC from the Protocol Stability Module (PSM) to Coinbase Custody, as outlined in [MIP65](https://forum.makerdao.com/t/rwa-007-mip65-monetalis-clydesdale-legal-assessment/17834). It is critical to note that JAMES ASSET LIMITED manages additional assets from other Maker's transactions in distinct trusts—specifically, assets related to MIP65 are segregated into two trusts: James Asset Trust 1 (JAT 1) and James Asset Trust 2 (JAT 2).

Furthermore, Monetalis's responsibilities include acquiring and disseminating information concerning the Trust Assets to MakerDAO, as detailed in Schedule 1 of the agreement.

![image|996x374](upload://c7kQV1pU7ySVCChHRImfBJJXaKu.png)

Under the terms of this agreement, any non-performance is governed by the provisions outlined in Section 9, "REMEDIES AND WAIVERS." This section clearly articulates that neither the failure nor delay in exercising any right or remedy by any party constitutes a waiver thereof, nor does it preclude any further or subsequent exercise of such rights or other remedies.

Our analysis suggests that JAL retains the right to enforce Monetalis' obligations under the agreement and to seek damages for any delayed performance. JAL is authorized to terminate Monetalis' engagement with at least one month's written notice. Additionally, any legal disputes emanating from this agreement are to be exclusively adjudicated in the courts of the British Virgin Islands.

Monetalis' operational role in the fund's distribution primarily involves transferring USDC from the Protocol Stability Module (PSM) to a JAL account at Coinbase by executing a smart contract's push function. Each transfer requires collaborative action from both JAL's director and the Administrator in alignment with the relevant resolutions passed by MakerDAO.

The custodianship and management of funds are securely divided between two separate entities—JAL and Coinbase—neither of which has any affiliationto Monetalis. Monetalis is primarily charged with post-transaction reporting, positioning it in a role with a comparatively lower risk profile. There is no immediate risk of Monetalis performing unauthorized transactions or becoming insolvent, jeopardizing the counterpart's funds.

Notwithstanding, Monetalis remains liable for the accuracy of the information it provides and for fulfilling its contractual duties. Based on our review of publicly available resources, we find no immediate risk to the assets if the custodianship arrangement with Coinbase has not been deprecated.

The recent scrutiny from the community has [compelled Monetalis to answer](https://forum.makerdao.com/t/mip102c2-sp30-mip-amendment-subproposal/23729) questions regarding their inconsistent actions. Vigilant oversight by multiple stakeholders is undeniably beneficial; however, these events highlight the necessity for the community to consider implementing a process wherein an independent third-party professional audits the role of the arranger.

## Proposal for Purchase of USDe via Existing Andromeda Facility

While the above-reviewed arrangements are pertinent to a functional collateral setup (i.e. [Monetals Clydesdale RWA007-A](https://makerburn.com/#/collateral/RWA007-A)), the following examines a [proposal](https://forum.makerdao.com/t/bt-project-ethena-risk-legal-assessment/23978) made earlier this year for the purchase of USDe/sUSDe via the existing [RWA-015 Andromeda vault](https://makerburn.com/#/collateral/RWA015-A). It is important to note that this proposal has yet to be voted on.

### Recap of Maker's Legal Structure for USDe Purchases

The USDe purchase is envisioned through DAI deployments from the Andromeda Vault (utilized by Maker to purchase T-bills). These transactions should be facilitated through a multi-layered legal structure comprised of:

- TACO & SUBS, LLC, a Cayman Islands limited liability company, is a wholly-owned subsidiary of TACO Foundation, an exempted limited guarantee foundation based out of the Cayman Islands.
- Leeward Management Limited, a Cayman Islands ordinary resident company engaged by TACO Foundation to act as Director Agent.
- BlockTower Capital Advisors LP, a Delaware limited partnership, is an institutional investment firm [supervised by the SEC](https://adviserinfo.sec.gov/firm/summary/290170).
- Ankura Trust Company LLC, a New Hampshire state-chartered trust company, acts as an independent, conflict-free indenture trustee, loan administrative agent, escrow agent, creditor representative, and other trustee services.
- Coinbase has been chosen as the primary exchange and custodial platform for executing transactions related to the Ethena protocol.

The flow of funds specifics:
1) Leeward Management receives deployment instructions from a specific email address associated with the Maker's Ecosystem team. The resolution indicates the amount of USDC to be deployed into the Ethena Protocol and the acceptable slippage threshold.
2) TACO & SUBS's instructions are also emailed to responsible parties.
3) Ankura Trust Company, as a paying agent, calls RWA015_A_OUTPUT_CONDUIT to mint DAI, swap it for USDC, and deposit it into the Coinbase Prime account.
4) Once the Coinbase deposit is completed, BlockTower mints USDe and stakes it using Ethena's front end.
5) sUSDe is held in the Coinbase Prime account, subject to a multiparty approval workflow requiring at least one initiator (BlockTower) and one approver (Ankura/TACO).
6) BlockTower confirms the completion of the deployment via email to TACO & SUBS.

The return of capital presupposes all actions done in reverse by the same responsible parties with the difference that relevant [INPUT](https://forum.makerdao.com/t/bt-project-ethena-risk-legal-assessment/23978#:~:text=call%20the%20relevant-,RWA015_A_INPUT_CONDUIT_URN_USDC,-contracts%20to%20deposit) smart contracts are called. 

### Weak Spots Evaluated

Upon observation of the multifaceted operations, we should highlight several instances of potential vulnerabilities:

* **Email correspondence** - Sending instructions over email without additional verification poses a risk of spoofing, impersonation, and other technical manipulation of the stream.
* **BlockTower indemnity** - BlockTower is provided with an indemnity capped at $2,500,000 and available for 48 months to insulate the investment advisor against regulatory actions in the US. Should BlockTower need to access the indemnity amount, Ankura can provide the necessary funds from TACO's bank account. Extended financial commitments to BlockTower are made on top of a guaranteed total minimum fee of $2,500,000 over one year.
* **BlockTower conflict of interests** - BlockTower [reportedly](https://forum.makerdao.com/t/bt-project-ethena-risk-legal-assessment/23978#:~:text=theft%20of%20assets.-,Conflicts%20of%20Interest,-.%20The%20Arranger) has a conflict of interest due to advising a client who is an investor and equity holder in Ethena. Other clients advised by BlockTower hold Maker-issued digital assets (MKR and/or DAI). In connection with the above-discussed indemnity provided to BlockTower, we consider the interconnectedness of the investment advisor with parties on both ends of the USDe purchase process a concerning factor that should be subject to a more detailed financial analysis.
* **Intertwining with [Project Andromeda](https://forum.makerdao.com/t/project-andromeda-risk-legal-assessment/20969)** - Digital assets from the Andromeda Vault (created for the purchase of short-dated US Treasuries) are deployed to acquire USDe and stake such USDe. Among the parties involved in the operations is a subsidiary of the TACO Foundation, which Foundation was in use for Project Andromeda. As per [disclosures](https://forum.makerdao.com/t/bt-project-ethena-risk-legal-assessment/23978#:~:text=theft%20of%20assets.-,Conflicts%20of%20Interest,-.%20The%20Arranger), the digital assets used to fund the TACO Account originate from the Andromeda vault. Therefore, the user should be aware that *"…the Digital Assets contained in the vault are used to back DAI's peg to the U.S. Dollar), any losses sustained by the TACO Account as a result of the contemplated transactions may negatively affect the value of DAI, and in severe, adverse scenarios, may cause potential de-pegs of DAI from the U.S. Dollar."*

Based on the uncertainties in the above legal structure, stringent oversight is essential for implementing the proposed USDe purchase stream. It is prudent for MakerDAO to re-assess the suggested framework and critically evaluate the flow of funds mechanism in light of the deficiencies observed in Monetalis' arrangements.

Nonetheless, this examination has been performed on the grounds of publicly accessible data. Confidential documents representing an inseparable part of such a complex legal structure may display information leading to different conclusions.