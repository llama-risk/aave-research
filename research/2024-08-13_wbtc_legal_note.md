# WBTC Custody Transition: Preliminary Findings and Outstanding Queries

## Background

Wrapped Bitcoin (WBTC) is an ERC-20 token representing Bitcoin on the Ethereum blockchain. It enables Bitcoin holders to participate in Decentralized Finance (DeFi) ecosystems and expand its utility beyond its typical role as a store of value. The WBTC protocol implements a structure involving custodians, merchants, and a token smart contract managed by a multisig wallet. This multisig has nonetheless [remained inactive](https://etherscan.io/address/0xB33f8879d4608711cEBb623F293F8Da13B8A37c5) over the past year.

BitGo serves as the primary custodian for WBTC, maintaining custody of the Bitcoin that collateralizes the WBTC tokens. Merchants function as intermediaries in the WBTC ecosystem, facilitating the minting and burning processes of WBTC tokens. Merchants can initiate the minting process after completing Know Your Customer (KYC) and Know Your Business (KYB) verifications. This involves transferring the requisite BTC collateral to BitGo, which then holds the BTC in a 1:1 ratio with the WBTC it issues. Consequently, for each WBTC token created, an equivalent amount of BTC is held in custody, thereby ensuring that the underlying Bitcoin assets fully back the value of WBTC.

The [proof of reserve](https://wbtc.network/dashboard/audit) mechanism for WBTC is on-chain, allowing instant verification directly on the blockchain. Third parties regularly conduct independent audits to confirm that the BitGo custodian holds sufficient Bitcoin to back the issued WBTC tokens. While [this information can be verified on-chain](https://wbtc.network/dashboard/audit), these formal third-party audits are not documented. 

On Friday, August 9th, BitGo announced it would transfer the management of the WBTC product to a [new joint venture with BiT Global in 60 days](https://blog.bitgo.com/bitgo-to-move-wbtc-to-multi-jurisdictional-custody-to-accelerate-global-expansion-plan-2ea0623fa2c8). This announcement has resulted in elevated scrutiny from stakeholders regarding whether WBTC DeFi integrations need evaluation, hence this forum topic. 

Below, we present our initial findings and a list of further clarifications we seek to address through our established communication channel with BitGo representatives.

## BitGo Licensing Status

BitGo holds a Major Payment Institution license issued by the Monetary Authority of Singapore. Custodianship may be admitted under the Digital Payment Token Services. DPT service providers must meet requirements for segregation and custody of customers' assets. 

![image|1062x594](upload://dtS3ZKMl9fUKSSG45rdGhlMiyBn.png)
Source: [MAS](https://eservices.mas.gov.sg/fid/institution/detail/420728-BITGO-SINGAPORE-PTE-LTD), August 12th, 2024

Given the circumstances, it appears that the jurisdictional expansion into Singapore, as highlighted in the [official blog announcement](https://blog.bitgo.com/bitgo-to-move-wbtc-to-multi-jurisdictional-custody-to-accelerate-global-expansion-plan-2ea0623fa2c8), could have potentially been achieved through BitGo's existing corporate structure and its subsidiaries, without necessitating a joint venture.

## BiT Global Regulatory Compliance

The blog post claims that *BiT Global is a global custody platform with regulated operations based in Hong Kong, registered as a Trust and Company Service Provider (TCSP)*.

### Hong Kong TCSP

An inquiry with the TCSP registry confirms an active license in the name of "BIT GLOBAL TRUST LIMITED."

![image|1504x794](upload://hqlQdmtm2rfcC0uV3iY89QUuvRU.png)
Source: [TCSP Registry](https://www.tcsp.cr.gov.hk/tcspls/index)

The regulatory framework governing trust and company service providers (TCSPs) was instituted on March 1st, 2018, following the enactment of the Anti-Money Laundering and Counter-Terrorist Financing (Financial Institutions) (Amendment) Ordinance 2018. This legislative amendment was introduced to align Hong Kong's regulatory practices with international standards aimed at combating money laundering and the financing of terrorism, thereby expanding the scope of the existing Anti-Money Laundering and Counter-Terrorist Financing Ordinance.

In accordance with these regulations, a TCSP may encompass an individual entity (such as a sole proprietorship), a partnership, or a corporation that offers one or more of the following services to clients:

- Formation of corporations or other legal entities.
- Acting or facilitating the appointment of another individual to act as a director, named secretary, partner of a corporation or partnership, or in a comparable position concerning other legal entities.
- Provision of a registered office, business address, correspondence, or administrative address for a corporation, partnership, or any other legal entity or arrangement.
- Acting, or arranging for another person to act, as a trustee of an express trust or similar legal arrangement.
- Acting or facilitating the appointment of another person to act as a nominee shareholder for a party other than a publicly listed entity.

A licensee with a presence in other jurisdictions—whether through branches, subsidiaries, or affiliated entities—must adhere to additional regulatory requirements. Specifically, the licensee is required to maintain comprehensive records demonstrating that its operations in foreign jurisdictions align as closely as possible with Hong Kong's regulatory standards, subject to the constraints imposed by local laws and practices.

In circumstances where both Hong Kong and BVI  BiT Global entities (see below) belong to the same corporate group, the existence of foreign establishments must be duly reported to the Hong Kong TCSP Registry.

Notably, the list of TCSP services outlined above does not specifically address digital asset arrangements, particularly custody services for digital assets. While compliance with AML regulations mitigates certain risk categories, it should not be construed as a comprehensive mechanism for ensuring customer protection. Consequently, the mere possession of a TCSP license does not provide assurance that BIT GLOBAL TRUST LIMITED has adopted best practices for digital asset custody, such as asset segregation and the utilization of cold storage solutions.

### BVI FSC

Further research reveals that the entity "BiT Global Custody Ltd" is registered with the BVI Financial Services Commission.

![image|468x234](upload://2SqKwzofX2OcgjiWsvzbvYFc7G0.png)
Source: [BVI FSC](https://www.bvifsc.vg/regulated-entities/bit-global-custody-ltd), August 12th, 2024

The Securities and Investment Business Act (SIBA) imposes ongoing obligations on entities regulated and licensed under its jurisdiction. These obligations include the annual filing of financial statements, the continuous presence of at least two directors, the appointment of an authorized representative, and stringent record-keeping requirements. The ability of an investment fund to safeguard and secure its assets is crucial to its operations and the protection of investor interests. The safekeeping protocols that an investment fund must establish are contingent upon the types of assets held by the fund. Should there be any cessation or alteration in these safekeeping arrangements, the fund is mandated to notify the Financial Services Commission of such changes.

## Clarification Required

BitGo has cited in their [announcement post](https://blog.bitgo.com/bitgo-to-move-wbtc-to-multi-jurisdictional-custody-to-accelerate-global-expansion-plan-2ea0623fa2c8) that the primary motivation for this multi-jurisdictional custody arrangement is to upgrade the security of WBTC operations through jurisdictional and geographical diversification. There are open questions about the advantageous qualities of the proposed structure and speculations about undisclosed motivations that may pose additional risks to WBTC. LlamaRisk is actively seeking clarifications to the follow-up items and is communicating with BitGo representatives to provide more informed guidance to the Aave DAO.

**1. Which entity will serve as the major partner in this new venture with BitGo?**

It is of utmost importance to identify the entity nominated to serve as the major partner in the joint venture with BitGo. This identification is crucial as it will allow for a comprehensive analysis of the applicable legal framework and an evaluation of its reliability. The regulatory environment governing the nominated entity will directly influence the joint venture's security, compliance, and overall credibility, particularly in the context of digital asset custody. 

**2. In which jurisdiction will WBTC collateral be custodied?**

While the entities involved may operate within a unified international structure, clarifying the jurisdiction where the funds will be held in custody is essential. Specifically, determining whether the custody of funds will be managed under the regulatory framework of the British Virgin Islands or that of Hong Kong is critical. Each jurisdiction presents distinct regulatory requirements and standards, which may significantly impact the joint venture's operational integrity and legal oversight. 

If further data about the major partner cannot be obtained, the assessment of license credibility would be complicated. Compared to the BVI's, Hong Kong's regime offers a higher level of adoption and recognition. At the same time, the BVI's regime has a strict requirement for asset segregation - a condition not present in the Hong Kong licensing framework.

**3. What is a safe way to transition confidential information regarding the legal setup?**

LlamaRisk has access to legal resources and is prepared to enter into a non-disclosure agreement (NDA) with BitGo. This arrangement would facilitate the provision of crucial information to the Aave DAO, enabling informed decision-making regarding WBTC's status. This approach aligns with Mike Belshe's statement on BitGo's willingness to engage, as expressed in the [Maker forum](http://forum.makerdao.com/t/wbtc-changes-and-risk-mitigation-10-august-2024/24844/18). Implementing this process could yield significant benefits for Aave and BitGo, allowing for a more comprehensive and appropriate response to the current situation.
