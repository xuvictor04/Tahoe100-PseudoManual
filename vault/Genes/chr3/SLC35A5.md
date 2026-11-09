---
symbol: "SLC35A5"
type: "gene"
col: 6181
ensembl_id: "ENSG00000138459"
name: "solute carrier family 35 member A5"
location: "3q13.2"
module: 3
arm: "-"
pooled_cpm: 15.18
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SLC35A5

*solute carrier family 35 member A5* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.46× (z +6.8, q 8e-09, up in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.394× (z -11.8, q 1e-29, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CGGBP1]] (+0.64, fdr 3e-05), [[CPNE1]] (+0.64, fdr 1e-05), [[TAF9]] (+0.61, fdr 1e-05); moves opposite to [[UBE2R2]] (-0.60, fdr 1e-05), [[MARK4]] (-0.58, fdr 2e-05), [[RABGEF1P1]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.46×** | +6.8 | 8e-09 | 27/48 (SW480, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.34× | +3.6 | 0.10 | 13/28 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.31× | +3.4 | 0.13 | 12/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 1.29× | +3.2 | 0.15 | 9/48 (NCI-H23, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.15 | 9/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.16 | 8/48 (SW480, RPMI-7951, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.0 | 0.19 | 15/48 (SW1417, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.394×** | -11.8 | 1e-29 | 41/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.460×** | -9.9 | 1e-20 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.482×** | -9.3 | 3e-18 | 35/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.498×** | -8.9 | 9e-17 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.502×** | -8.8 | 2e-16 | 36/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.525×** | -7.7 | 9e-13 | 34/47 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.574×** | -7.1 | 1e-10 | 33/47 (PANC-1, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.612×** | -6.3 | 3e-08 | 30/47 (SNU-1, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.632×** | -5.8 | 3e-07 | 32/46 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.429×** | -5.6 | 1e-06 | 28/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.434×** | -5.6 | 1e-06 | 23/37 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.446×** | -5.4 | 4e-06 | 25/45 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -5.1 | 1e-05 | 24/42 (SNU-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.656×** | -3.8 | 0.005 | 14/48 (NCI-H1792, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.734×** | -3.8 | 0.006 | 15/47 (PANC-1, COLO 205, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.758×** | -3.5 | 0.014 | 14/47 (CFPAC-1, NCI-H2030, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.780×** | -3.2 | 0.048 | 17/46 (NCI-H1792, C-33 A, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.786×** | -3.1 | 0.065 | 18/47 (SW48, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.5 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.195× (z -15.8) |
| [[LoVo (line)]] | wt | 15.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.282× (z -9.2) |
| [[KATO III (line)]] | alt | 19.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0871× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 15.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -11.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.285× (z -9.5) |
| [[A-427 (line)]] | wt | 30.6 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0926× (z -18.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 2 (1 ⚠) | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0796× (z -11.6) |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0679× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.207× (z -10.4) |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.267× (z -8.7) |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.223× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 9.16 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.146× (z -8.9) |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | +0.64 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[CPNE1]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TAF9]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[UBAP2L]] | +0.61 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[THAP9]] | +0.59 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[ALG10B]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GUF1]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TRAM2-AS1]] | +0.59 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[HNRNPK]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PRKAR1A]] | +0.58 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CCDC25]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[ANAPC13]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2R2]] | -0.60 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[MARK4]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RABGEF1P1]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[EPS15L1]] | -0.57 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[ANKRD39]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MED31]] | -0.56 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[SLC27A4]] | -0.55 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[UBE2M]] | -0.54 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.53 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[RAD9A]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[DAP3]] | -0.52 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.0, -0.1); signed map (16.0, -33.4). **Vector** length 60.8, 9.60% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +4.3 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.5 | +2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | +0.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.2 | -11.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.5 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -8.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.2 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:112,561,709-112,585,579 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20730 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BS91](https://www.uniprot.org/uniprotkb/Q9BS91) (UDP-sugar transporter protein SLC35A5):

> Probable UDP-sugar:UMP transmembrane antiporter involved in UDP-alpha-D-glucuronate/UDP-GlcA, UDP-GlcNAc/UDP-N-acetyl-alpha-D-glucosamine and UDP-N-acetyl-alpha-D-galactosamine/UDP-GalNAc transport from the cytosol to the lumen of the Golgi.

**Summary**, from NCBI Gene [55032](https://www.ncbi.nlm.nih.gov/gene/55032):

> This gene encodes a transmembrane protein which belongs to subfamily 35A of the solute carrier superfamily. The encoded protein is a nucleoside-sugar transporter. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:20792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20792) · Entrez [55032](https://www.ncbi.nlm.nih.gov/gene/55032) · UniProt [Q9BS91](https://www.uniprot.org/uniprotkb/Q9BS91) · Ensembl [ENSG00000138459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138459)

## Data

Gene col 6181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6181); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6181]; `tensor/DDL_lfc|DDL_z.npy` [6181]; `embed/gene_vectors.npy` [6181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6181 or target_col == 6181). Every well: [[SLC35A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
