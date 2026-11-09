---
symbol: "CCDC51"
type: "gene"
col: 8846
ensembl_id: "ENSG00000164051"
name: "coiled-coil domain containing 51"
location: "3p21.31"
module: 12
arm: "+"
pooled_cpm: 4.18
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CCDC51

*coiled-coil domain containing 51* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.24× (z +8.1, q 3e-13, up in 4 of 7 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.03× (z +7.4, q 2e-11, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.478× (z -7.7, q 6e-12, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEX264]] (+0.65, fdr 7e-06), [[RRN3]] (+0.63, fdr 7e-06), [[PEX12]] (+0.62, fdr 9e-06); moves opposite to [[PHTF2]] (-0.51, fdr 3e-05), [[HINT1]] (-0.50, fdr 9e-04, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8846.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.24×** | +8.1 | 3e-13 | 4/7 (HOP62, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +7.6 | 7e-12 | 14/23 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +7.4 | 2e-11 | 27/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.98×** | +7.2 | 1e-10 | 27/45 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +6.9 | 8e-10 | 18/37 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +6.2 | 4e-08 | 11/24 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.74×** | +5.8 | 6e-07 | 21/44 (SW480, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.8 | 1e-04 | 5/44 (SW480, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.56×** | +4.7 | 2e-04 | 7/22 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 3e-04 | 11/44 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.4 | 6e-04 | 6/47 (J82, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.0 | 0.003 | 7/41 (SW1417, LS 180, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +3.9 | 0.004 | 11/45 (PANC-1, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +3.8 | 0.005 | 10/40 (A549, LOX-IMVI, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.006 | 12/35 (LS 180, SW48, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.006 | 5/45 (NCI-H460, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.010 | 6/45 (CHP-212, J82, …) | rises with dose | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.075 | 6/35 (NCI-H1792, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.079 | 12/37 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8846.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.478×** | -7.7 | 6e-12 | 28/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -6.7 | 6e-09 | 22/34 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.557×** | -6.1 | 2e-07 | 21/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.578×** | -5.8 | 1e-06 | 19/44 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -4.3 | 0.002 | 16/44 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.689×** | -3.6 | 0.028 | 4/44 (BT-474, SNU-423, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.740× | -3.2 | 0.13 | 11/39 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8846. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.71 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +13.1) | [[Isocorydine (drug)]] 0.5 µM 0.0779× (z -8.5) |
| [[LoVo (line)]] | wt | 6.18 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0660× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -9.8) |
| [[SW480 (line)]] | alt | 5.38 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.197× (z -8.8) |
| [[A-427 (line)]] | wt | 4.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0873× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 4.15 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0562× (z -8.5) |
| [[HS-578T (line)]] | alt | 3.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 5.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +9.0) | — |
| [[A-172 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8846), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX264]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RRN3]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PEX12]] | +0.62 | +0.73 / +0.57 | both halves | 9e-06 |  |
| [[PHAX]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.61 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[ZNF180]] | +0.60 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[MRM2]] | +0.58 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.58 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[TARS2]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[MRPL58]] | +0.58 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[KLHL9]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[RPUSD2]] | +0.57 | +0.44 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHTF2]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[HINT1]] | -0.50 | -0.62 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.4, -0.0); signed map (-2.3, -22.5). **Vector** length 47.3, 5.64% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +0.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 51 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,432,164-48,440,456 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12436, MITOK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ER9](https://www.uniprot.org/uniprotkb/Q96ER9) (Mitochondrial potassium channel):

> Pore-forming subunit of the mitochondrial ATP-gated potassium channel (mitoK(ATP)). Together with ATP-binding subunit ABCB8/MITOSUR of the mitoK(ATP) channel, mediates ATP-dependent K(+) currents across the mitochondrial inner membrane. An increase in ATP intracellular levels closes the channel, inhibiting K(+) transport, whereas a decrease in ATP levels enhances K(+) uptake in the mitochondrial matrix. May contribute to the homeostatic control of cellular metabolism under stress conditions by …

**Summary**, from NCBI Gene [79714](https://www.ncbi.nlm.nih.gov/gene/79714):

> Enables mitochondrial ATP-gated potassium channel activity. Involved in cell volume homeostasis and mitochondrial potassium ion transmembrane transport. Located in mitochondrial inner membrane and nucleoplasm. Part of mitochondrial ATP-gated potassium channel complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25714) · Entrez [79714](https://www.ncbi.nlm.nih.gov/gene/79714) · UniProt [Q96ER9](https://www.uniprot.org/uniprotkb/Q96ER9) · Ensembl [ENSG00000164051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164051)

## Data

Gene col 8846: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8846); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8846, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8846]; `tensor/DDL_lfc|DDL_z.npy` [8846]; `embed/gene_vectors.npy` [8846]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8846 or target_col == 8846). Every well: [[CCDC51 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC51.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
