---
symbol: "HPSE"
type: "gene"
col: 10338
ensembl_id: "ENSG00000173083"
name: "heparanase"
location: "4q21.23"
module: 176
arm: "+"
pooled_cpm: 3.39
n_lines_expressing: 42
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# HPSE

*heparanase* — 4q21.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 5.24× (z +19.8, q 0e+00, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.681× (z -6.5, q 5e-08, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PODXL2]] (+0.69, fdr 1e-05), [[SUSD4]] (+0.69, fdr 5e-05), [[AIF1L]] (+0.68, fdr 1e-05); moves opposite to [[BMS1P4-1]] (-0.64, fdr 5e-05), [[ATE1OSP]] (-0.60, fdr 4e-05), [[NMNAT1]] (-0.60, fdr 3e-05).
> It is in [[Module 176]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **5.24×** | +19.8 | 0e+00 | 32/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **4.63×** | +18.3 | 0e+00 | 36/38 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.74×** | +17.0 | 0e+00 | 34/37 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.83×** | +16.0 | 0e+00 | 33/35 (PANC-1, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.38×** | +14.5 | 1e-45 | 8/11 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.45×** | +14.2 | 7e-44 | 4/5 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.01×** | +13.1 | 2e-37 | 31/37 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.87×** | +12.6 | 2e-34 | 26/32 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.22×** | +8.8 | 8e-17 | 7/8 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +8.5 | 1e-15 | 16/38 (RKO, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.12×** | +7.1 | 7e-11 | 13/31 (NCI-H2030, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +6.7 | 9e-10 | 4/18 (A498, SW48, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +6.3 | 1e-08 | 12/26 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.53×** | +5.1 | 2e-05 | 7/36 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **1.52×** | +4.8 | 6e-05 | 5/18 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.012 | 1/23 (RKO) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.027 | 1/37 (NCI-H2347) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.030 | 4/36 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.29×** | +2.9 | 0.086 | 1/36 (LoVo) | inconsistent across doses |  |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.088 | 2/32 (RKO, HT-29) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.681×** | -6.5 | 5e-08 | 16/27 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.634×** | -5.2 | 5e-05 | 11/32 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.665×** | -4.9 | 2e-04 | 12/29 (HCT15, SW48, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.704×** | -4.2 | 0.004 | 9/37 (KATO III, LoVo, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.828× | -3.2 | 0.17 | 9/37 (RPMI-7951, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 9.06 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -10.9) |
| [[SHP-77 (line)]] | alt | 9.42 | 0 | 2 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0916× (z -9.7) |
| [[LoVo (line)]] | wt | 15.1 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0423× (z -9.9) |
| [[LS 180 (line)]] | wt | 4.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0524× (z -14.3) |
| [[A-172 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.894 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PODXL2]] | +0.69 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SUSD4]] | +0.69 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[AIF1L]] | +0.68 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[KCTD17]] | +0.65 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[GLB1L2]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 | pathway: Glycosaminoglycan metabolism |
| [[SMARCD3]] | +0.63 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CDCA7L]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ATP1A3]] | +0.61 | +0.30 / +0.67 | both halves | 2e-04 |  |
| [[RADX]] | +0.60 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[SEPTIN3]] | +0.60 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[TMEM98]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[UGT8]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P4-1]] | -0.64 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ATE1OSP]] | -0.60 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[NMNAT1]] | -0.60 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[TAS2R4]] | -0.59 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[ZNF785]] | -0.59 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[MTG2]] | -0.58 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[GTF2IRD2B]] | -0.58 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[CHD1-DT]] | -0.57 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[KRIT1]] | -0.57 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[GTF2IRD2]] | -0.57 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[RAB30-DT]] | -0.57 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[FNBP4]] | -0.57 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.2, 36.3); signed map (-22.3, 30.5). **Vector** length 54.5, 8.62% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +17.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.3 | +14.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +19.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +7.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | -0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -4.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | heparanase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23 — chr4:83,292,461-83,335,153 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPA, HSE1, HPSE1 |
| Gene groups (HGNC) | Heparanase family |
| Reactome | 6 pathways, smallest: HS-GAG degradation; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y251](https://www.uniprot.org/uniprotkb/Q9Y251) (Heparanase):

> Endoglycosidase that cleaves heparan sulfate proteoglycans (HSPGs) into heparan sulfate side chains and core proteoglycans. Participates in extracellular matrix (ECM) degradation and remodeling. Selectively cleaves the linkage between a glucuronic acid unit and an N-sulfo glucosamine unit carrying either a 3-O-sulfo or a 6-O-sulfo group. Can also cleave the linkage between a glucuronic acid unit and an N-sulfo glucosamine unit carrying a 2-O-sulfo group, but not linkages between a glucuronic …

**Summary**, from NCBI Gene [10855](https://www.ncbi.nlm.nih.gov/gene/10855):

> Heparan sulfate proteoglycans are major components of the basement membrane and extracellular matrix. The protein encoded by this gene is an enzyme that cleaves heparan sulfate proteoglycans to permit cell movement through remodeling of the extracellular matrix. In addition, this cleavage can release bioactive molecules from the extracellular matrix. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:5164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5164) · Entrez [10855](https://www.ncbi.nlm.nih.gov/gene/10855) · UniProt [Q9Y251](https://www.uniprot.org/uniprotkb/Q9Y251) · Ensembl [ENSG00000173083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173083)

## Data

Gene col 10338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10338); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10338]; `tensor/DDL_lfc|DDL_z.npy` [10338]; `embed/gene_vectors.npy` [10338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10338 or target_col == 10338). Every well: [[HPSE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPSE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
