---
symbol: "PAQR4"
type: "gene"
col: 8477
ensembl_id: "ENSG00000162073"
name: "progestin and adipoQ receptor family member 4"
location: "16p13.3"
module: 77
arm: "+"
pooled_cpm: 7.12
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# PAQR4

*progestin and adipoQ receptor family member 4* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.77× (z +4.8, q 8e-04, up in 15 of 29 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.317× (z -13.3, q 2e-37, down in 36 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNE1]] (+0.69, fdr 1e-05), [[ZMYND19]] (+0.68, fdr 1e-05), [[VAV2]] (+0.64, fdr 1e-05); moves opposite to [[OCIAD1]] (-0.67, fdr 1e-05), [[NDUFA5]] (-0.64, fdr 7e-06), [[AIMP1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.77×** | +4.8 | 8e-04 | 15/29 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.57×** | +3.7 | 0.064 | 3/11 (SW1417, KATO III, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | 1.52× | +3.4 | 0.12 | 8/30 (SW480, J82, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 1.47× | +3.2 | 0.17 | 15/45 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.45× | +3.1 | 0.20 | 7/26 (SNU-423, CFPAC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.44× | +3.1 | 0.20 | 10/40 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.30× | +3.0 | 0.22 | 6/45 (SNU-1, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.317×** | -13.3 | 2e-37 | 36/40 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.288×** | -10.5 | 2e-23 | 31/40 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.171×** | -7.0 | 5e-10 | 29/43 (AsPC-1, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.428×** | -6.9 | 8e-10 | 30/42 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.450×** | -6.8 | 2e-09 | 28/45 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.305×** | -4.7 | 2e-04 | 24/37 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.566×** | -4.5 | 4e-04 | 21/42 (SK-MEL-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.592×** | -4.3 | 0.001 | 24/41 (NCI-H23, LS 180, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.624×** | -4.0 | 0.004 | 17/44 (BT-474, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.372×** | -3.9 | 0.005 | 11/42 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.639×** | -3.8 | 0.007 | 18/44 (A-172, KATO III, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.622×** | -3.8 | 0.007 | 19/43 (BT-474, SW48, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.426×** | -3.4 | 0.030 | 10/34 (SK-MEL-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.651×** | -3.3 | 0.039 | 9/45 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.664×** | -3.2 | 0.052 | 8/44 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.670×** | -3.1 | 0.063 | 12/45 (HCT15, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0946× (z -18.4) |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0370× (z -21.3) |
| [[A-427 (line)]] | wt | 24.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -12.8) |
| [[NCI-H2030 (line)]] | alt | 6.28 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -9.4) |
| [[PANC-1 (line)]] | alt | 8.07 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0465× (z -11.3) |
| [[SW48 (line)]] | wt | 13.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -10.3) |
| [[SW480 (line)]] | alt | 7.13 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -9.3) |
| [[A498 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -9.6) |
| [[BT-474 (line)]] | alt | 7.56 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0742× (z -8.8) |
| [[HS-578T (line)]] | alt | 5.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0507× (z -11.7) |
| [[J82 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 4.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0578× (z -9.3) |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -8.7) |
| [[RKO (line)]] | wt | 8.15 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -8.5) |
| [[A549 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNE1]] | +0.69 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[VAV2]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[TMEM201]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[FANCE]] | +0.63 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[PGP]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PBX4]] | +0.61 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ZBED4]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GNA12]] | +0.60 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[GINS2]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FEN1]] | +0.59 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[DOCK9]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCIAD1]] | -0.67 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[AIMP1]] | -0.63 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[C1orf43]] | -0.62 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[FAM204A]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PMPCB]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ETFRF1]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ZSCAN30]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[KPNA5]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[BPNT1]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[COPS5]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CYB5D2]] | -0.57 | -0.42 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MR1]] | B | MR1 activity lowers PAQR4's level | lines that do not express MR1 (5) vs lines expressing it (45) | 2.05× higher at baseline in the lines without MR1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-15.9, 1.9); signed map (-47.9, -16.1). **Vector** length 72.6, 14.2% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.0 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.6 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +0.7 |
|  | [[vincristine (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | -0.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | -3.3 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.3 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | progestin and adipoQ receptor family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,969,270-2,973,484 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30002 |
| Gene groups (HGNC) | Progestin and adipoQ receptor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4S7](https://www.uniprot.org/uniprotkb/Q8N4S7) (Progestin and adipoQ receptor family member 4):

> Plays a role in maintaining adipose tissue function through the regulation of ceramide levels. Mediates the stability of ceramide synthetases, CERS2 and CERS5, and their activities (Probable).

**Summary**, from NCBI Gene [124222](https://www.ncbi.nlm.nih.gov/gene/124222):

> Enables molecular adaptor activity. Involved in protein stabilization and regulation of ceramide biosynthetic process. Located in Golgi membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26386) · Entrez [124222](https://www.ncbi.nlm.nih.gov/gene/124222) · UniProt [Q8N4S7](https://www.uniprot.org/uniprotkb/Q8N4S7) · Ensembl [ENSG00000162073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162073)

## Data

Gene col 8477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8477); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8477]; `tensor/DDL_lfc|DDL_z.npy` [8477]; `embed/gene_vectors.npy` [8477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8477 or target_col == 8477). Every well: [[PAQR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAQR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
