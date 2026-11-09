---
symbol: "CACNG4"
type: "gene"
col: 1122
ensembl_id: "ENSG00000075461"
name: "calcium voltage-gated channel auxiliary subunit gamma 4"
location: "17q24.2"
module: 82
arm: "+"
pooled_cpm: 9.84
n_lines_expressing: 29
n_dd_up: 16
n_dd_down: 18
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 6
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# CACNG4

*calcium voltage-gated channel auxiliary subunit gamma 4* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.14× (z +12.5, q 3e-33, up in 7 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.52× (z +6.4, q 2e-08, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.432× (z -12.9, q 1e-35, down in 17 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FXYD6]] (+0.58, fdr 2e-05), [[INHBB]] (+0.56, fdr 1e-05), [[PTK7]] (+0.53, fdr 3e-05); moves opposite to [[TBCK]] (-0.40, fdr 3e-04), [[LINC01684]] (-0.40, fdr 4e-04), [[METTL15]] (-0.40, fdr 4e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EPS8L2]] → it (grade B ⚠); 6 go from it, the strongest it → [[EPS8L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +12.5 | 3e-33 | 7/18 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.9 | 2e-09 | 5/13 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +6.4 | 2e-08 | 13/24 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +6.3 | 3e-08 | 14/24 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.40×** | +5.2 | 2e-05 | 15/24 (BT-474, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +4.3 | 0.001 | 12/26 (NCI-H460, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 7/25 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.1 | 0.003 | 3/14 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.003 | 8/22 (BT-474, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.021 | 5/24 (A-427, PANC-1, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.026 | 8/25 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.029 | 4/24 (NCI-H23, CFPAC-1, …) | two highest doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.039 | 7/26 (HT-29, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.039 | 6/24 (HT-29, HepG2/C3A, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.74×** | +3.2 | 0.059 | 3/19 (BT-474, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +3.1 | 0.079 | 3/26 (NCI-H460, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.432×** | -12.9 | 1e-35 | 17/23 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.391×** | -10.0 | 3e-21 | 18/21 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.411×** | -9.7 | 5e-20 | 21/26 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -9.4 | 1e-18 | 18/22 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.412×** | -9.3 | 1e-18 | 20/25 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.484×** | -7.9 | 2e-13 | 15/26 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.563×** | -6.3 | 3e-08 | 17/26 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.552×** | -6.1 | 7e-08 | 17/24 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -5.6 | 1e-06 | 16/24 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -5.6 | 2e-06 | 13/26 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.628×** | -5.1 | 2e-05 | 12/25 (A-172, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.636×** | -4.9 | 4e-05 | 11/26 (A-172, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.566×** | -4.4 | 4e-04 | 9/26 (PANC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.669×** | -4.2 | 1e-03 | 16/22 (A-172, Panc 03.27, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.479×** | -4.2 | 1e-03 | 13/24 (PANC-1, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.512×** | -3.8 | 0.005 | 7/22 (PANC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.032 | 13/24 (A-172, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 47.7 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -29.3) |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 13 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0330× (z -21.7) |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -22.7) |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0732× (z -25.3) |
| [[SW1417 (line)]] | alt | 32.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0800× (z -24.1) |
| [[SW480 (line)]] | alt | 17.6 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0826× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.5) |
| [[BT-474 (line)]] | alt | 80.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -21.9) |
| [[MIA PaCa-2 (line)]] | alt | 8.09 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0279× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 24.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0874× (z -16.7) |
| [[Panc 03.27 (line)]] | alt | 6.86 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0626× (z -9.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Imiquimod (maleate) (drug)]] 5 µM 0.0657× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.0) |
| [[A-427 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.969 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FXYD6]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 | pathway: Cardiac conduction |
| [[INHBB]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[PTK7]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[DPYSL5]] | +0.51 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[PRR36]] | +0.48 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[LOXL1-AS1]] | +0.48 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[VOPP1]] | +0.48 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[CRMP1]] | +0.46 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[TBX1]] | +0.45 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[ROR2]] | +0.44 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[MEGF9]] | +0.44 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[KIF3C]] | +0.44 | +0.37 / +0.45 | both halves | 7e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.40 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[LINC01684]] | -0.40 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[METTL15]] | -0.40 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[RPAP2]] | -0.40 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[GALK2]] | -0.39 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[SEC23B]] | -0.39 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[GOLGA1]] | -0.37 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[SRBD1]] | -0.37 | -0.29 / -0.37 | both halves | 3e-04 |  |
| [[MYSM1]] | -0.36 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[MLKL]] | -0.36 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[ALG13]] | -0.36 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[HSCB]] | -0.36 | -0.36 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L2]] | B | EPS8L2 activity raises CACNG4's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without EPS8L2 | 0.049 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[PRR36]] | B | PRR36 activity raises CACNG4's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 2.21× lower at baseline in the lines without PRR36 | 0.091 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[PALM]] | C | PALM activity raises CACNG4's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.73× lower at baseline in the lines without PALM | 0.075 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[MAP6]] | C | MAP6 activity raises CACNG4's level | lines that do not express MAP6 (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without MAP6 | 0.078 | ⚠ within organs, on part of the lines; also absent: PCSK1N, ZFP28, SNAP91; co-absent with the target |
| [[FXYD6]] | C | FXYD6 activity raises CACNG4's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without FXYD6 | 0.084 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises CACNG4's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without KIF1A | 0.095 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L2]] | B | CACNG4 activity raises EPS8L2's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without CACNG4 | 0.028 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N |
| [[HES2]] | B | CACNG4 activity raises HES2's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 1.64× lower at baseline in the lines without CACNG4 | 0.033 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N |
| [[AFDN]] | B | CACNG4 activity raises AFDN's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 1.24× lower at baseline in the lines without CACNG4 | 0.061 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N |
| [[STOX2]] | C | CACNG4 activity raises STOX2's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 2.60× lower at baseline in the lines without CACNG4 | 0.011 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N; co-absent with the target |
| [[FXYD6]] | C | CACNG4 activity raises FXYD6's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without CACNG4 | 0.028 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N; co-absent with the target |
| [[PALM]] | C | CACNG4 activity raises PALM's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 2.55× lower at baseline in the lines without CACNG4 | 0.058 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.0, 43.5); signed map (52.1, 17.0). **Vector** length 74.5, 18.8% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -9.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.4 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit gamma 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:66,964,707-67,033,398 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC11138, MGC24983 |
| Gene groups (HGNC) | Calcium channel auxiliary gamma subunits |
| Reactome | 11 pathways, smallest: LGI-ADAM interactions; Phase 2 - plateau phase; Presynaptic depolarization and calcium channel opening |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBN1](https://www.uniprot.org/uniprotkb/Q9UBN1) (Voltage-dependent calcium channel gamma-4 subunit):

> Regulates the activity of L-type calcium channels that contain CACNA1C as pore-forming subunit. Regulates the trafficking and gating properties of AMPA-selective glutamate receptors (AMPARs), including GRIA1 and GRIA4. Promotes their targeting to the cell membrane and synapses and modulates their gating properties by slowing their rates of activation, deactivation and desensitization and by mediating their resensitization.

**Summary**, from NCBI Gene [27092](https://www.ncbi.nlm.nih.gov/gene/27092):

> The protein encoded by this gene is a type I transmembrane AMPA receptor regulatory protein (TARP). TARPs regulate both trafficking and channel gating of the AMPA receptors. This gene is part of a functionally diverse eight-member protein subfamily of the PMP-22/EMP/MP20 family and is located in a cluster with two family members, a type II TARP and a calcium channel gamma subunit. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:1408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1408) · Entrez [27092](https://www.ncbi.nlm.nih.gov/gene/27092) · UniProt [Q9UBN1](https://www.uniprot.org/uniprotkb/Q9UBN1) · Ensembl [ENSG00000075461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075461)

## Data

Gene col 1122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1122); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1122]; `tensor/DDL_lfc|DDL_z.npy` [1122]; `embed/gene_vectors.npy` [1122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1122 or target_col == 1122). Every well: [[CACNG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
