---
symbol: "ZDHHC18"
type: "gene"
col: 12822
ensembl_id: "ENSG00000204160"
name: "zDHHC palmitoyltransferase 18"
location: "1p36.11"
module: 2
arm: "+"
pooled_cpm: 16.56
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ZDHHC18

*zDHHC palmitoyltransferase 18* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.91× (z +11.8, q 2e-29, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.522× (z -11.5, q 1e-27, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PWWP2B]] (+0.65, fdr 1e-05), [[GPSM1]] (+0.64, fdr 7e-06), [[LRRC8E]] (+0.63, fdr 1e-05); moves opposite to [[ATRAID]] (-0.62, fdr 1e-05), [[SELENOF]] (-0.54, fdr 7e-05), [[ITM2B]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +11.8 | 2e-29 | 41/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.65×** | +8.7 | 1e-15 | 31/46 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.1 | 1e-13 | 27/45 (KATO III, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +7.2 | 6e-11 | 29/48 (SW480, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +5.9 | 4e-07 | 23/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.7 | 9e-07 | 21/47 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 1e-06 | 20/47 (HS-578T, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 4e-06 | 21/46 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 1e-05 | 21/45 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 1e-05 | 17/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 22/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.9 | 6e-05 | 21/43 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 3e-04 | 10/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.5 | 3e-04 | 15/38 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.58×** | +4.4 | 5e-04 | 11/42 (Panc 03.27, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.001 | 16/47 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 9/45 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.002 | 8/47 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.003 | 10/46 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12822.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -11.5 | 1e-27 | 33/45 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -10.8 | 1e-24 | 35/47 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -10.7 | 1e-24 | 35/47 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.771×** | -6.7 | 3e-09 | 26/48 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.702×** | -6.5 | 9e-09 | 24/47 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.562×** | -5.5 | 3e-06 | 24/47 (H4, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.654×** | -4.1 | 0.004 | 17/44 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.829×** | -3.3 | 0.064 | 10/30 (SW48, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 25.5 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.1) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.7) |
| [[SW48 (line)]] | wt | 37.8 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0599× (z -16.3) |
| [[HOP62 (line)]] | alt | 20.3 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.0) ⚠ cell-cycle shift, explains ~11% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -15.5) |
| [[RKO (line)]] | wt | 23.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -10.8) |
| [[A-427 (line)]] | wt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -10.8) |
| [[H4 (line)]] | wt | 16.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0837× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -12.6) |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +10.7) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -10.9) |
| [[KATO III (line)]] | alt | 8.91 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.4) |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 12.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +9.7) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -9.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.05× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.3) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +9.7) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0972× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -9.5) |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -10.1) |
| [[SW480 (line)]] | alt | 14.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +8.9) | — |
| [[A-172 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PWWP2B]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GPSM1]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[LRRC8E]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MPP3]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[DVL1]] | +0.61 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ETNK2]] | +0.60 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[GTF2IRD1]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[KCTD21]] | +0.60 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PSMD3]] | +0.60 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[BRF1]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FPGS]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRAID]] | -0.62 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SELENOF]] | -0.54 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[ITM2B]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ANP32A]] | -0.53 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[DECR1]] | -0.53 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[SNHG31]] | -0.53 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[MBNL3]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[TENT5A]] | -0.52 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ACBD5]] | -0.52 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.52 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[TMX4]] | -0.52 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ARL5B]] | -0.51 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZDHHC18's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises ZDHHC18's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-2.8, -26.7); signed map (-29.4, 2.6). **Vector** length 88.5, 17.6% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.4 | +11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.6 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.7 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +3.7 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -10.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -6.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,826,688-26,857,604 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp667O2416 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUE0](https://www.uniprot.org/uniprotkb/Q9NUE0) (Palmitoyltransferase ZDHHC18):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates, such as CGAS, HRAS and LCK. Acts as a negative regulator of the cGAS-STING pathway be mediating palmitoylation and inactivation of CGAS. May also have a palmitoyltransferase activity toward the beta-2 adrenergic receptor/ADRB2 and therefore regulate G protein-coupled receptor signaling.

**Summary**, from NCBI Gene [84243](https://www.ncbi.nlm.nih.gov/gene/84243):

> Enables protein-cysteine S-palmitoyltransferase activity. Involved in negative regulation of cGAS/STING signaling pathway; negative regulation of innate immune response; and peptidyl-L-cysteine S-palmitoylation. Is active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20712) · Entrez [84243](https://www.ncbi.nlm.nih.gov/gene/84243) · UniProt [Q9NUE0](https://www.uniprot.org/uniprotkb/Q9NUE0) · Ensembl [ENSG00000204160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204160)

## Data

Gene col 12822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12822); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12822]; `tensor/DDL_lfc|DDL_z.npy` [12822]; `embed/gene_vectors.npy` [12822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12822 or target_col == 12822). Every well: [[ZDHHC18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
