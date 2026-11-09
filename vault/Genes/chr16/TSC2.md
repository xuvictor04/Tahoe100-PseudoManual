---
symbol: "TSC2"
type: "gene"
col: 2334
ensembl_id: "ENSG00000103197"
name: "TSC complex subunit 2"
location: "16p13.3"
module: 30
arm: "+"
pooled_cpm: 31.89
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TSC2

*TSC complex subunit 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +13.6, q 2e-39, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.799× (z -5.9, q 2e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LCMT1]] (+0.72, fdr 1e-05), [[MIGA2]] (+0.72, fdr 8e-06), [[PLD3]] (+0.69, fdr 1e-05); moves opposite to [[NCR3LG1]] (-0.64, fdr 4e-05), [[ZC3H4]] (-0.61, fdr 3e-05), [[ADAMTS3]] (-0.60, fdr 5e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +13.6 | 2e-39 | 46/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +13.0 | 4e-36 | 48/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +10.1 | 9e-22 | 43/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.1 | 2e-07 | 20/38 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 2e-05 | 25/47 (LoVo, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +4.6 | 4e-04 | 20/48 (KATO III, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.002 | 16/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.017 | 11/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.6 | 0.021 | 16/44 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.072 | 10/48 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.073 | 13/47 (SW48, NCI-H661, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2334.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.9 | 2e-06 | 25/48 (AsPC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.768×** | -4.8 | 4e-04 | 23/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.836× | -4.7 | 4e-04 | 23/47 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.799×** | -4.2 | 0.004 | 20/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -3.8 | 0.016 | 21/48 (A-172, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.818×** | -3.7 | 0.017 | 17/48 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.820×** | -3.7 | 0.017 | 17/48 (AsPC-1, hTERT-HPNE, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.693×** | -3.6 | 0.024 | 14/49 (AsPC-1, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.1 | 0.11 | 14/48 (NCI-H460, CHP-212, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.848× | -3.1 | 0.12 | 12/48 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | 0.844× | -3.0 | 0.12 | 17/47 (HEC-1-A, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 32.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 41.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.7) |
| [[LoVo (line)]] | wt | 20.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.07× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 36.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.398× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 47.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.4) |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 40.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.373× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 34.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.4) |
| [[A-427 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | +0.72 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[MIGA2]] | +0.72 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[PLD3]] | +0.69 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 | same gene group |
| [[CEP131]] | +0.68 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[IFT52]] | +0.68 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[E4F1]] | +0.64 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[HEATR5B]] | +0.64 | +0.61 / +0.48 | both halves | 2e-05 | same gene group |
| [[PSMD9]] | +0.64 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[ABCD4]] | +0.64 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[RANBP10]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[EVI5L]] | +0.63 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCR3LG1]] | -0.64 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H4]] | -0.61 | -0.57 / -0.45 | both halves | 3e-05 | same gene group |
| [[ADAMTS3]] | -0.60 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[LEKR1]] | -0.59 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TASOR]] | -0.59 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[PATL2]] | -0.59 | -0.52 / -0.33 | both halves | 1e-04 | same gene group |
| [[ARAP2]] | -0.59 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ZNF747]] | -0.57 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[CTBP1-DT]] | -0.57 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD31]] | -0.57 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[KRT8P12]] | -0.57 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[TRIM59]] | -0.57 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.5, -3.3); signed map (-35.4, -0.7). **Vector** length 102, 22.9% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | +13.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.0 | +10.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.9 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.2 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -1.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | TSC complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,047,967-2,089,491 (+) |
| Ensembl biotype | protein_coding |
| Also known as | tuberin, LAM, PPP1R160; previously TSC4 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Armadillo like helical domain containing; TSC complex |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MYOGENESIS |
| Reactome | 17 pathways, smallest: Inhibition of TSC complex formation by AKT (PKB); AKT phosphorylates targets in the cytosol; Constitutive Signaling by AKT1 E17K in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P49815](https://www.uniprot.org/uniprotkb/P49815) (Tuberin):

> Catalytic component of the TSC-TBC complex, a multiprotein complex that acts as a negative regulator of the canonical mTORC1 complex, an evolutionarily conserved central nutrient sensor that stimulates anabolic reactions and macromolecule biosynthesis to promote cellular biomass generation and growth. Within the TSC-TBC complex, TSC2 acts as a GTPase-activating protein (GAP) for the small GTPase RHEB, a direct activator of the protein kinase activity of mTORC1. In absence of nutrients, the …

**Summary**, from NCBI Gene [7249](https://www.ncbi.nlm.nih.gov/gene/7249):

> This gene is a tumor suppressor gene that encodes the growth inhibitory protein tuberin. Tuberin interacts with hamartin to form the TSC protein complex which functions in the control of cell growth. This TSC protein complex negatively regulates mammalian target of rapamycin complex 1 (mTORC1) signaling which is a major regulator of anabolic cell growth. Mutations in this gene have been associated with tuberous sclerosis and lymphangioleiomyomatosis. [provided by RefSeq, May 2022]

**Accessions** — [HGNC:12363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12363) · Entrez [7249](https://www.ncbi.nlm.nih.gov/gene/7249) · UniProt [P49815](https://www.uniprot.org/uniprotkb/P49815) · Ensembl [ENSG00000103197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103197)

## Data

Gene col 2334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2334); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2334]; `tensor/DDL_lfc|DDL_z.npy` [2334]; `embed/gene_vectors.npy` [2334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2334 or target_col == 2334). Every well: [[TSC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
