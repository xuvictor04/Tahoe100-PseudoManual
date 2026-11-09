---
symbol: "PEX19"
type: "gene"
col: 8573
ensembl_id: "ENSG00000162735"
name: "peroxisomal biogenesis factor 19"
location: "1q23.2"
module: 25
arm: "+"
pooled_cpm: 15.7
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PEX19

*peroxisomal biogenesis factor 19* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.69× (z +15.6, q 0e+00, up in 25 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.87× (z +10.3, q 1e-22, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.768× (z -6.1, q 5e-07, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMU1]] (+0.74, fdr 7e-06), [[LIN7C]] (+0.71, fdr 7e-06), [[NRAS]] (+0.71, fdr 1e-05); moves opposite to [[COX5A]] (-0.68, fdr 7e-06, ⚠ COX5A in the vector space only through flagged drug-doses), [[SNHG9]] (-0.59, fdr 2e-05), [[SAC3D1]] (-0.58, fdr 3e-05), [[ZBTB7A]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8573.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +15.6 | 0e+00 | 25/28 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +15.4 | 0e+00 | 33/38 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +10.7 | 1e-24 | 26/36 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +10.3 | 1e-22 | 35/46 (C32, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +8.2 | 3e-14 | 30/48 (A-172, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +5.6 | 2e-06 | 23/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 1e-05 | 19/47 (LOX-IMVI, A498, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 4e-05 | 20/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.6 | 3e-04 | 12/38 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 4e-04 | 22/47 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +4.2 | 0.001 | 18/47 (A-172, A-427, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.17× | +3.5 | 0.020 | 14/47 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.022 | 11/48 (A-172, BT-474, …) | rises with dose | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.30×** | +3.0 | 0.098 | 10/42 (KATO III, AsPC-1, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Phenytoin (sodium) (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.098 | 3/47 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8573.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.768×** | -6.1 | 5e-07 | 27/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -4.3 | 0.004 | 18/47 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.790×** | -3.9 | 0.021 | 16/46 (C-33 A, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.825× | -3.0 | 0.25 | 14/45 (A-427, HepG2/C3A, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.774× | -3.0 | 0.25 | 8/45 (H4, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.833× | -3.0 | 0.25 | 9/48 (SW 1271, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +10.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 32.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.96× (z +8.8) | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 11.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.05× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.60× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 32.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMU1]] | +0.74 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.71 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[NRAS]] | +0.71 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[GPN1]] | +0.70 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[VAMP3]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[STX16]] | +0.68 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[AP2M1]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[NCSTN]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TWF1]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[RTF2]] | +0.64 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[GBA1]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX5A]] ⚠ | -0.68 | -0.60 / -0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | -0.59 | -0.46 / -0.65 | both halves | 2e-05 |  |
| [[SAC3D1]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[ZBTB7A]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NSUN5P2-1]] ⚠ | -0.57 | -0.42 / -0.59 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL22L1]] ⚠ | -0.56 | -0.29 / -0.62 | both halves | 3e-04 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[C15orf61]] ⚠ | -0.56 | -0.44 / -0.54 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.56 | -0.37 / -0.57 | both halves | 7e-05 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[SNHG25]] | -0.55 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[RPL36]] | -0.55 | -0.33 / -0.62 | both halves | 1e-04 | pathway: Protein localization |
| [[PTMAP2]] ⚠ | -0.55 | -0.39 / -0.55 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARID3A]] | -0.54 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[IMP3]] | -0.54 | -0.20 / -0.66 | both halves | 7e-04 |  |
| [[FOXA2]] | -0.54 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[LSM2]] | -0.53 | -0.36 / -0.59 | both halves | 9e-05 |  |
| [[CCDC85B]] | -0.53 | -0.27 / -0.65 | both halves | 3e-04 |  |
| [[TMEM131L]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CDKN2D]] | -0.53 | -0.37 / -0.61 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.7, -21.1); signed map (-16.9, -36.0). **Vector** length 84.5, 15.9% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.4 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +10.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.6 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:160,276,807-160,286,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HK33, D1S2223E, PMP1, PMPI, PXMP1; previously PXF |
| Gene groups (HGNC) | Peroxins |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 8 pathways, smallest: ABC transporters in lipid homeostasis; Class I peroxisomal membrane protein import; ABC-family protein mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P40855](https://www.uniprot.org/uniprotkb/P40855) (Peroxisomal biogenesis factor 19):

> Necessary for early peroxisomal biogenesis. Acts both as a cytosolic chaperone and as an import receptor for peroxisomal membrane proteins (PMPs). Binds and stabilizes newly synthesized PMPs in the cytoplasm by interacting with their hydrophobic membrane-spanning domains, and targets them to the peroxisome membrane by binding to the integral membrane protein PEX3. Excludes CDKN2A from the nucleus and prevents its interaction with MDM2, which results in active degradation of TP53.

**Summary**, from NCBI Gene [5824](https://www.ncbi.nlm.nih.gov/gene/5824):

> This gene is necessary for early peroxisomal biogenesis. It acts both as a cytosolic chaperone and as an import receptor for peroxisomal membrane proteins (PMPs). Peroxins (PEXs) are proteins that are essential for the assembly of functional peroxisomes. The peroxisome biogenesis disorders (PBDs) are a group of genetically heterogeneous autosomal recessive, lethal diseases characterized by multiple defects in peroxisome function. These disorders have at least 14 complementation groups, with …

**Accessions** — [HGNC:9713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9713) · Entrez [5824](https://www.ncbi.nlm.nih.gov/gene/5824) · UniProt [P40855](https://www.uniprot.org/uniprotkb/P40855) · Ensembl [ENSG00000162735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162735)

## Data

Gene col 8573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8573); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8573]; `tensor/DDL_lfc|DDL_z.npy` [8573]; `embed/gene_vectors.npy` [8573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8573 or target_col == 8573). Every well: [[PEX19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
