---
symbol: "PNKP"
type: "gene"
col: 464
ensembl_id: "ENSG00000039650"
name: "polynucleotide kinase 3'-phosphatase"
location: "19q13.33"
module: 182
arm: "-"
pooled_cpm: 21.05
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# PNKP

*polynucleotide kinase 3'-phosphatase* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.29× (z +16.3, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.794× (z -4.6, q 0.002, down in 14 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35C2]] (+0.57, fdr 1e-05), [[BRD9]] (+0.56, fdr 2e-05), [[TRIM41]] (+0.55, fdr 1e-05); moves opposite to [[FBXO9]] (-0.51, fdr 2e-05), [[CEPT1]] (-0.51, fdr 3e-05), [[ZYG11B]] (-0.50, fdr 5e-05).
> It sits in the **-** arm of [[Module 182]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.29×** | +16.3 | 0e+00 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +14.9 | 0e+00 | 36/47 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +10.6 | 3e-24 | 35/47 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +10.0 | 3e-21 | 36/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +8.4 | 4e-15 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +8.3 | 7e-15 | 29/46 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +7.7 | 8e-13 | 30/47 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 1e-08 | 26/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +6.3 | 3e-08 | 25/47 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +5.1 | 2e-05 | 23/47 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +4.6 | 2e-04 | 13/48 (RKO, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.5 | 3e-04 | 12/47 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.16× | +4.1 | 0.001 | 12/47 (SW480, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.011 | 9/48 (RKO, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +3.2 | 0.046 | 15/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.047 | 13/44 (PANC-1, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 464.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.794×** | -4.6 | 0.002 | 14/48 (RKO, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.827×** | -4.6 | 0.002 | 19/48 (AsPC-1, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.819×** | -3.8 | 0.029 | 13/46 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.877× | -3.7 | 0.030 | 11/48 (LS 180, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.819×** | -3.7 | 0.030 | 7/47 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.4 | 0.054 | 13/47 (A-427, RPMI-7951, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.871× | -3.4 | 0.054 | 12/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Aliskiren (drug)]] 0.5 µM |  | 0.844× | -3.4 | 0.054 | 10/48 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.851× | -3.2 | 0.088 | 8/48 (SW 1271, HEC-1-A, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.093 | 10/46 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.856× | -3.1 | 0.11 | 8/47 (NCI-H2347, SNU-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +16.0) | — |
| [[A-172 (line)]] | wt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +13.5) | — |
| [[A-427 (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +20.8) | — |
| [[A549 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 20.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +10.0) | — |
| [[C32 (line)]] | wt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +9.2) | — |
| [[LoVo (line)]] | wt | 15.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 15.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 22.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +22.2) | — |
| [[NCI-H2030 (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.8) | — |
| [[SHP-77 (line)]] | alt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +11.8) | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0976× (z -9.9) ⚠ toxic; unreliable plate only |
| [[SW480 (line)]] | alt | 19.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35C2]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[BRD9]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[TRIM41]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PROSER3]] | +0.54 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[CYTH2]] | +0.54 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[ADGRL1-AS1]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ZNF628]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[POLD1]] | +0.51 | +0.44 / +0.57 | both halves | 3e-05 | pathway: Base Excision Repair; STRING 480 |
| [[NECAB3]] | +0.51 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[MZF1]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[RTEL1]] | +0.51 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[SLC25A44]] | +0.50 | +0.39 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO9]] | -0.51 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[CEPT1]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ZYG11B]] | -0.50 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SMAD5]] | -0.50 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[SEC24B]] | -0.48 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[FGFR1OP2]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SUCLG1]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DHX29]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[RWDD1]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[RYK]] | -0.45 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[NIPSNAP2]] | -0.45 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ANKRD13C]] | -0.45 | -0.55 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-13.5, -28.7); signed map (0.8, 8.2). **Vector** length 70.8, 11.9% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.2 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.9 | +0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +14.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | polynucleotide kinase 3'-phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,859,882-49,878,351 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PNK |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases; DNA kinases |
| Reactome | 4 pathways, smallest: APEX1-Independent Resolution of AP Sites via the Single Nucleotide Replacement Pathway; Resolution of Abasic Sites (AP sites); Base Excision Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T60](https://www.uniprot.org/uniprotkb/Q96T60) (Bifunctional polynucleotide phosphatase/kinase):

> Plays a key role in the repair of DNA damage, functioning as part of both the non-homologous end-joining (NHEJ) and base excision repair (BER) pathways. Through its two catalytic activities, PNK ensures that DNA termini are compatible with extension and ligation by either removing 3'-phosphates from, or by phosphorylating 5'-hydroxyl groups on, the ribose sugar of the DNA backbone.

**Summary**, from NCBI Gene [11284](https://www.ncbi.nlm.nih.gov/gene/11284):

> This locus represents a gene involved in DNA repair. In response to ionizing radiation or oxidative damage, the protein encoded by this locus catalyzes 5' phosphorylation and 3' dephosphorylation of nucleic acids. Mutations at this locus have been associated with microcephaly, seizures, and developmental delay.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:9154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9154) · Entrez [11284](https://www.ncbi.nlm.nih.gov/gene/11284) · UniProt [Q96T60](https://www.uniprot.org/uniprotkb/Q96T60) · Ensembl [ENSG00000039650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000039650)

## Data

Gene col 464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 464); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 464]; `tensor/DDL_lfc|DDL_z.npy` [464]; `embed/gene_vectors.npy` [464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 464 or target_col == 464). Every well: [[PNKP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNKP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
