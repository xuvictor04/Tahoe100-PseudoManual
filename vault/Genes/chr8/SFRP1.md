---
symbol: "SFRP1"
type: "gene"
col: 2444
ensembl_id: "ENSG00000104332"
name: "secreted frizzled related protein 1"
location: "8p11.21"
module: 13
arm: "+"
pooled_cpm: 18.7
n_lines_expressing: 18
n_dd_up: 14
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 13
direction_downstream: 11
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SFRP1

*secreted frizzled related protein 1* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.22× (z +18.9, q 0e+00, up in 12 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +8.3, q 2e-14, up in 4 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.435× (z -8.3, q 7e-14, down in 14 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PODXL]] (+0.67, fdr 1e-05), [[F2R]] (+0.66, fdr 1e-05), [[ITGA11]] (+0.64, fdr 7e-06); moves opposite to [[CEBPD]] (-0.57, fdr 2e-05), [[RNF115]] (-0.54, fdr 4e-05), [[N4BP2L2]] (-0.53, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[INSYN2B]] → it (grade C ⚠); 11 go from it, the strongest it → [[COL13A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.22×** | +18.9 | 0e+00 | 12/13 (SNU-423, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.43×** | +18.5 | 0e+00 | 11/12 (SNU-423, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.70×** | +12.5 | 9e-34 | 11/12 (SNU-423, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +8.3 | 2e-14 | 4/15 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.09×** | +7.6 | 3e-12 | 13/16 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.6 | 4e-12 | 3/14 (hTERT-HPNE, C32, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.86×** | +6.4 | 1e-08 | 13/16 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.81×** | +6.2 | 5e-08 | 12/16 (NCI-H23, J82, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.79×** | +5.6 | 2e-06 | 6/12 (hTERT-HPNE, C32, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.5 | 3e-06 | 8/16 (NCI-H23, A-427, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.54×** | +4.5 | 4e-04 | 13/16 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.8 | 0.008 | 3/14 (CFPAC-1, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.45×** | +3.7 | 0.010 | 3/14 (C32, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.41×** | +3.6 | 0.015 | 8/16 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.435×** | -8.3 | 7e-14 | 14/15 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.456×** | -8.1 | 1e-13 | 11/16 (SW 900, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.465×** | -7.9 | 5e-13 | 14/15 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -5.7 | 2e-06 | 13/14 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.582×** | -5.0 | 6e-05 | 8/16 (PANC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.620×** | -4.9 | 7e-05 | 12/16 (SNU-423, SW 900, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.628×** | -4.4 | 7e-04 | 5/16 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.753×** | -4.1 | 0.002 | 9/16 (SW 900, SNU-423, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.674×** | -4.1 | 0.003 | 6/16 (SNU-423, SW 900, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.472×** | -4.1 | 0.003 | 5/15 (HOP62, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -4.0 | 0.003 | 14/16 (A-427, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.690×** | -3.8 | 0.006 | 4/16 (NCI-H23, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.715×** | -3.5 | 0.022 | 15/16 (J82, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **0.528×** | -3.5 | 0.022 | 4/15 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.721×** | -3.4 | 0.025 | 8/16 (A-427, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.721×** | -3.4 | 0.025 | 10/16 (HOP62, PANC-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 121 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -20.3) |
| [[A-427 (line)]] | wt | 15.8 | 1 (1 ⚠) | 4 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.29× (z +8.7) ⚠ cell-cycle shift, explains ~36% of this change | [[Digitoxin (drug)]] 5 µM 0.152× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.192× (z -9.9) |
| [[A549 (line)]] | wt | 20.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 6.06× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0988× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 5.81 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +10.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.86× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 73.9 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0740× (z -14.5) |
| [[J82 (line)]] | alt | 20.5 | 1 (1 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 5.66× (z +8.6) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.1) |
| [[SNU-423 (line)]] | alt | 320 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -21.3) |
| [[PANC-1 (line)]] | alt | 36.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -19.3) |
| [[C32 (line)]] | wt | 28.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +10.0) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0490× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 99.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 38.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.4) |
| [[AN3 CA (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0389× (z -11.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PODXL]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[F2R]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[DKK3]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 | STRING 775 |
| [[PCDHGC3]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TRIM9]] | +0.62 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[KCNK3]] | +0.61 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[INSYN2B]] | +0.61 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[SLIT3]] | +0.60 | +0.63 / +0.47 | both halves | 2e-05 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[VAT1L]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ECE1]] | +0.60 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[NMNAT2]] | +0.60 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPD]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[RNF115]] | -0.54 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[N4BP2L2]] | -0.53 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[BTN2A1]] | -0.53 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[FBXO6]] | -0.51 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ZC3HC1]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[RNF146]] | -0.50 | -0.45 / -0.33 | both halves | 1e-04 | pathway: Signaling by WNT |
| [[DAXX]] | -0.50 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[RPP38]] | -0.50 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[POLR3C]] | -0.49 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[ZCCHC10]] | -0.49 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[MGST1]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INSYN2B]] | C | INSYN2B activity raises SFRP1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 6.13× lower at baseline in the lines without INSYN2B | 0.007 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[PLEKHG4B]] | C | PLEKHG4B activity raises SFRP1's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 4.26× lower at baseline in the lines without PLEKHG4B | 0.010 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises SFRP1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.53× lower at baseline in the lines without COL5A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises SFRP1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 4.08× lower at baseline in the lines without DKK3 | 0.022 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[SCUBE1]] | C | SCUBE1 activity raises SFRP1's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 4.55× lower at baseline in the lines without SCUBE1 | 0.023 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises SFRP1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 3.14× lower at baseline in the lines without COL15A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises SFRP1's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 3.46× lower at baseline in the lines without SPOCK1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises SFRP1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.55× lower at baseline in the lines without ITGA11 | 0.046 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[SLIT3]] | C | SLIT3 activity raises SFRP1's level | lines that do not express SLIT3 (31) vs lines expressing it (19) | 3.17× lower at baseline in the lines without SLIT3 | 0.050 | ⚠ within organs, on part of the lines; also absent: GLYATL2, KIRREL3, NTRK3; co-absent with the target |
| [[TRIM9]] | C | TRIM9 activity raises SFRP1's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 4.27× lower at baseline in the lines without TRIM9 | 0.054 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[RNF182]] | C | RNF182 activity raises SFRP1's level | lines that do not express RNF182 (22) vs lines expressing it (28) | 3.98× lower at baseline in the lines without RNF182 | 0.054 | ⚠ within organs, on part of the lines; also absent: PTX3, FZD8, ENSG00000230615; co-absent with the target |
| [[NTNG2]] | C | NTNG2 activity raises SFRP1's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.85× lower at baseline in the lines without NTNG2 | 0.056 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL13A1]] | B | SFRP1 activity raises COL13A1's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without SFRP1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2 |
| [[ZCCHC24]] | B | SFRP1 activity raises ZCCHC24's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 1.94× lower at baseline in the lines without SFRP1 | 0.083 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2 |
| [[NTNG2]] | C | SFRP1 activity raises NTNG2's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 2.36× lower at baseline in the lines without SFRP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[PLEKHG4B]] | C | SFRP1 activity raises PLEKHG4B's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 3.34× lower at baseline in the lines without SFRP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[HTRA1]] | C | SFRP1 activity raises HTRA1's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 2.94× lower at baseline in the lines without SFRP1 | 0.036 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[COL15A1]] | C | SFRP1 activity raises COL15A1's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without SFRP1 | 0.050 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[INSYN2B]] | C | SFRP1 activity raises INSYN2B's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 4.26× lower at baseline in the lines without SFRP1 | 0.062 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[SLIT3]] | C | SFRP1 activity raises SLIT3's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 3.00× lower at baseline in the lines without SFRP1 | 0.076 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[VIM]] | C | SFRP1 activity raises VIM's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 5.25× lower at baseline in the lines without SFRP1 | 0.080 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[LOXL2]] | C | SFRP1 activity raises LOXL2's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 3.15× lower at baseline in the lines without SFRP1 | 0.085 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |
| [[COL5A1]] | C | SFRP1 activity raises COL5A1's level | lines that do not express SFRP1 (32) vs lines expressing it (18) | 4.04× lower at baseline in the lines without SFRP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: LAYN, INSYN2B, EVC2; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.6, 14.5); signed map (22.7, 43.2). **Vector** length 68.1, 21.5% of its response variance represented; |z| ≥ 3 in 537 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +18.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.9 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | +1.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -7.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.1 | -5.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | secreted frizzled related protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:41,261,962-41,309,473 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SARP2, FRP, FRP-1 |
| Gene groups (HGNC) | Secreted frizzled-related proteins; MicroRNA protein coding host genes |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Negative regulation of TCF-dependent signaling by WNT ligand antagonists; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N474](https://www.uniprot.org/uniprotkb/Q8N474) (Secreted frizzled-related protein 1):

> Soluble frizzled-related proteins (sFRPS) function as modulators of Wnt signaling through direct interaction with Wnts. They have a role in regulating cell growth and differentiation in specific cell types. SFRP1 decreases intracellular beta-catenin levels (By similarity). Has antiproliferative effects on vascular cells, in vitro and in vivo, and can induce, in vivo, an angiogenic response. In vascular cell cycle, delays the G1 phase and entry into the S phase (By similarity). In kidney …

**Summary**, from NCBI Gene [6422](https://www.ncbi.nlm.nih.gov/gene/6422):

> This gene encodes a member of the SFRP family that contains a cysteine-rich domain homologous to the putative Wnt-binding site of Frizzled proteins. Members of this family act as soluble modulators of Wnt signaling; epigenetic silencing of SFRP genes leads to deregulated activation of the Wnt-pathway which is associated with cancer. This gene may also be involved in determining the polarity of photoreceptor cells in the retina. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:10776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10776) · Entrez [6422](https://www.ncbi.nlm.nih.gov/gene/6422) · UniProt [Q8N474](https://www.uniprot.org/uniprotkb/Q8N474) · Ensembl [ENSG00000104332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104332)

## Data

Gene col 2444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2444); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2444]; `tensor/DDL_lfc|DDL_z.npy` [2444]; `embed/gene_vectors.npy` [2444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2444 or target_col == 2444). Every well: [[SFRP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFRP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
