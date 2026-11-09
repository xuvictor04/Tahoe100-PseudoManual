---
symbol: "ABRAXAS1"
type: "gene"
col: 8668
ensembl_id: "ENSG00000163322"
name: "abraxas 1, BRCA1 A complex subunit"
location: "4q21.23"
module: 57
arm: "+"
pooled_cpm: 10.65
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ABRAXAS1

*abraxas 1, BRCA1 A complex subunit* — 4q21.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.83× (z +9.8, q 5e-20, up in 27 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.75× (z +9.1, q 2e-17, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.520× (z -15.0, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM210B]] (+0.65, fdr 1e-05), [[TMOD2]] (+0.65, fdr 1e-05), [[IL17RD]] (+0.63, fdr 1e-05); moves opposite to [[ZNF689]] (-0.55, fdr 1e-04), [[RBX1]] (-0.52, fdr 5e-05), [[RRP8]] (-0.51, fdr 2e-04).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GJA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +9.8 | 5e-20 | 27/36 (SW48, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +9.1 | 2e-17 | 32/47 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +8.7 | 5e-16 | 14/22 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +8.6 | 1e-15 | 30/47 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +8.2 | 2e-14 | 18/28 (A498, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +7.4 | 1e-11 | 21/48 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.9 | 4e-10 | 26/47 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +6.1 | 6e-08 | 19/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 9e-06 | 20/46 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.33×** | +4.7 | 2e-04 | 9/48 (A498, HCT15, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +4.0 | 0.003 | 7/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.18× | +3.9 | 0.005 | 15/48 (SK-MEL-2, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +3.8 | 0.006 | 12/45 (Panc 03.27, LOX-IMVI, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.8 | 0.006 | 9/48 (NCI-H1792, A-427, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.013 | 4/44 (H4, NCI-H1792, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.014 | 2/42 (NCI-H2030, A498) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.017 | 4/48 (A-427, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.018 | 7/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.023 | 10/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.023 | 7/45 (NCI-H1573, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8668.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.520×** | -15.0 | 0e+00 | 36/47 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.596×** | -8.4 | 1e-14 | 28/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.593×** | -8.2 | 5e-14 | 28/46 (A-172, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -7.2 | 8e-11 | 23/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.651×** | -7.0 | 3e-10 | 25/45 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.664×** | -6.7 | 2e-09 | 27/44 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -6.3 | 2e-08 | 23/46 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -5.3 | 9e-06 | 20/44 (KATO III, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.597×** | -4.4 | 7e-04 | 11/46 (A-427, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.755×** | -4.3 | 9e-04 | 16/46 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.786×** | -3.9 | 0.004 | 10/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.794×** | -3.8 | 0.008 | 15/46 (A-172, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.049 | 15/47 (AN3 CA, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.827×** | -3.1 | 0.080 | 13/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 10.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Naproxen (drug)]] 0.05 µM 0.169× (z -9.1) |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -11.3) |
| [[A549 (line)]] | wt | 13.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0503× (z -16.5) |
| [[A498 (line)]] | wt | 8.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -8.8) |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -9.2) |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0959× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0990× (z -9.6) |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0800× (z -10.1) |
| [[J82 (line)]] | alt | 4.38 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0874× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 8.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.7) |
| [[RKO (line)]] | wt | 10.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -8.6) |
| [[A-427 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM210B]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[TMOD2]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[IL17RD]] | +0.63 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PLA2G12A]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[RAB4A]] | +0.62 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CYB5R4]] | +0.61 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[STX7]] | +0.61 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[CREG1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SLC66A3]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.60 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RPS7]] | +0.57 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RPL4]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF689]] | -0.55 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[RBX1]] | -0.52 | -0.40 / -0.51 | both halves | 5e-05 | pathway: Cell Cycle Checkpoints |
| [[RRP8]] | -0.51 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[IL34]] | -0.51 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[NEK8]] | -0.51 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[GPANK1]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[TRIM39]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ZNF101]] | -0.50 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[ACTR3-AS1]] | -0.50 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[DHRS7B]] | -0.50 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[MZF1-AS1]] | -0.50 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[ERI2]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GJA3]] | B | GJA3 activity raises ABRAXAS1's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 1.26× lower at baseline in the lines without GJA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: GBX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.8, -4.2); signed map (-34.2, -13.1). **Vector** length 59.6, 8.75% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.2 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +5.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -15.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.0 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | abraxas 1, BRCA1 A complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23 — chr4:83,459,517-83,523,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13614, ABRA1, ABRAXAS; previously CCDC98, FAM175A |
| Gene groups (HGNC) | BRCA1 A complex |
| Reactome | 14 pathways, smallest: Metalloprotease DUBs; Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWZ7](https://www.uniprot.org/uniprotkb/Q6UWZ7) (BRCA1-A complex subunit Abraxas 1):

> Involved in DNA damage response and double-strand break (DSB) repair. Component of the BRCA1-A complex, acting as a central scaffold protein that assembles the various components of the complex and mediates the recruitment of BRCA1. The BRCA1-A complex specifically recognizes 'Lys-63'-linked ubiquitinated histones H2A and H2AX at DNA lesion sites, leading to target the BRCA1-BARD1 heterodimer to sites of DNA damage at DSBs. This complex also possesses deubiquitinase activity that specifically …

**Summary**, from NCBI Gene [84142](https://www.ncbi.nlm.nih.gov/gene/84142):

> This gene encodes a protein that binds to the C-terminal repeats of breast cancer 1 (BRCA1) through a phospho-SXXF motif. The encoded protein recruits ubiquitin interaction motif containing 1 protein to BRCA1 protein and is required for DNA damage resistance, DNA repair, and cell cycle checkpoint control. Pseudogenes of this gene are found on chromosomes 3 and 8. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:25829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25829) · Entrez [84142](https://www.ncbi.nlm.nih.gov/gene/84142) · UniProt [Q6UWZ7](https://www.uniprot.org/uniprotkb/Q6UWZ7) · Ensembl [ENSG00000163322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163322)

## Data

Gene col 8668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8668); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8668]; `tensor/DDL_lfc|DDL_z.npy` [8668]; `embed/gene_vectors.npy` [8668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8668 or target_col == 8668). Every well: [[ABRAXAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABRAXAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
