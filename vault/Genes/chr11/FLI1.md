---
symbol: "FLI1"
type: "gene"
col: 7555
ensembl_id: "ENSG00000151702"
name: "Fli-1 proto-oncogene, ETS transcription factor"
location: "11q24.3"
module: 13
arm: "+"
pooled_cpm: 16.42
n_lines_expressing: 19
n_dd_up: 20
n_dd_down: 17
n_dd_up_clean: 14
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 20
direction_downstream: 35
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FLI1

*Fli-1 proto-oncogene, ETS transcription factor* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +13.6, q 2e-39, up in 9 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.397× (z -11.7, q 9e-29, down in 15 of 16 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WNT5B]] (+0.59, fdr 1e-05), [[TWIST2]] (+0.57, fdr 1e-05), [[CNRIP1]] (+0.54, fdr 6e-05); moves opposite to [[BABAM2]] (-0.46, fdr 5e-05), [[TMEM184A]] (-0.45, fdr 2e-04), [[MAP9]] (-0.45, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 35 go from it, the strongest it → [[WIPF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +13.6 | 2e-39 | 9/17 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +12.1 | 2e-31 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +9.8 | 3e-20 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.7 | 1e-12 | 12/17 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +7.4 | 2e-11 | 7/17 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.4 | 2e-08 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +5.0 | 6e-05 | 6/17 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.47×** | +4.6 | 3e-04 | 8/17 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.3 | 9e-04 | 8/16 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +4.3 | 9e-04 | 1/15 (NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.3 | 0.001 | 2/16 (A-172, HS-578T) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.016 | 4/17 (hTERT-HPNE, H4, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.048 | 0/15 | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.2 | 0.058 | 4/12 (hTERT-HPNE, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.063 | 0/16 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.1 | 0.069 | 1/17 (RPMI-7951) | rises with dose |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.069 | 0/16 | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.075 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.077 | 1/17 (hTERT-HPNE) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.081 | 0/16 | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.097 | 1/16 (NCI-H2030) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.397×** | -11.7 | 9e-29 | 15/16 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.432×** | -10.6 | 8e-24 | 17/17 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.522×** | -8.2 | 4e-14 | 15/16 (J82, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.564×** | -7.2 | 6e-11 | 16/17 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.684×** | -6.8 | 1e-09 | 16/17 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.606×** | -6.3 | 2e-08 | 12/17 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.486×** | -4.8 | 1e-04 | 11/16 (H4, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.715×** | -4.8 | 1e-04 | 9/17 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.694×** | -4.4 | 6e-04 | 15/17 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.526×** | -4.2 | 0.001 | 13/16 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.528×** | -4.2 | 0.001 | 13/17 (PANC-1, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.698×** | -4.2 | 0.001 | 2/16 (NCI-H460, HOP62) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.538×** | -4.1 | 0.002 | 12/16 (PANC-1, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.723×** | -3.9 | 0.004 | 1/17 (SW 1088) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.743×** | -3.8 | 0.007 | 7/17 (SK-MEL-2, HOP62, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.753×** | -3.6 | 0.012 | 9/16 (A-172, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.754×** | -3.4 | 0.019 | 8/16 (HOP62, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -17.0) |
| [[A-172 (line)]] | wt | 41.3 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0568× (z -21.2) |
| [[HOP62 (line)]] | alt | 76.5 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0772× (z -21.4) |
| [[HS-578T (line)]] | alt | 33.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.2) |
| [[J82 (line)]] | alt | 66.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -20.6) |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -20.9) |
| [[Hs 766T (line)]] | wt | 91.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0506× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -12.2) |
| [[SNU-423 (line)]] | alt | 86.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -16.4) |
| [[H4 (line)]] | wt | 22.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0916× (z -16.9) |
| [[PANC-1 (line)]] | alt | 19.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 4.21 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0672× (z -8.8) |
| [[A-427 (line)]] | wt | 0.876 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.942 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WNT5B]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TWIST2]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CNRIP1]] | +0.54 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[DENND2A]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ESM1]] | +0.51 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[WIPF1]] | +0.51 | +0.58 / +0.40 | both halves | 5e-05 | STRING 429 |
| [[SCHIP1]] | +0.51 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[AK5]] | +0.51 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[LINC02742]] | +0.51 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[PDCD1LG2]] | +0.50 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[ANXA2R-OT1]] | +0.50 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[RPSAP52]] | +0.49 | +0.40 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BABAM2]] | -0.46 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TMEM184A]] | -0.45 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[MAP9]] | -0.45 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[GSN]] | -0.43 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[AKR1B1]] | -0.42 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[ARHGEF3]] | -0.41 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[KIF16B]] | -0.41 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[HOOK2]] | -0.41 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[NIHCOLE]] | -0.40 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[RORC]] | -0.40 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[FBXO16]] | -0.40 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[LINC01748]] | -0.40 | -0.40 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FLI1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL27A1]] | B | COL27A1 activity raises FLI1's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 3.94× lower at baseline in the lines without COL27A1 | 0.049 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[AKR1B1]] | B | AKR1B1 activity raises FLI1's level | lines that do not express AKR1B1 (16) vs lines expressing it (34) | 3.46× lower at baseline in the lines without AKR1B1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PTPRM, EHD3, SYNM |
| [[RNF217]] | B | RNF217 activity raises FLI1's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 3.29× lower at baseline in the lines without RNF217 | 0.068 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3 |
| [[UBASH3B]] | B | UBASH3B activity raises FLI1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 3.13× lower at baseline in the lines without UBASH3B | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[ADAMTS6]] | C | ADAMTS6 activity raises FLI1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 5.84× lower at baseline in the lines without ADAMTS6 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises FLI1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 5.39× lower at baseline in the lines without PDCD1LG2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[MIR100HG]] | C | MIR100HG activity raises FLI1's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 4.86× lower at baseline in the lines without MIR100HG | 0.009 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises FLI1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 4.11× lower at baseline in the lines without CDH13 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises FLI1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 5.19× lower at baseline in the lines without ADAMTS12 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises FLI1's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.28× lower at baseline in the lines without FRMD4A | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[LINC02742]] | C | LINC02742 activity raises FLI1's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 4.82× lower at baseline in the lines without LINC02742 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 12, C 23. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WIPF1]] | B | FLI1 activity raises WIPF1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 4.32× lower at baseline in the lines without FLI1 | 0.019 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[ARHGAP31]] | B | FLI1 activity raises ARHGAP31's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without FLI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[SCHIP1]] | B | FLI1 activity raises SCHIP1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without FLI1 | 0.025 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[IQCJ-SCHIP1]] | B | FLI1 activity raises IQCJ-SCHIP1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without FLI1 | 0.034 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[NBPF8]] | B | FLI1 activity raises NBPF8's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without FLI1 | 0.043 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[IQCJ-SCHIP1]] | B | FLI1 activity strengthens IQCJ-SCHIP1's drug response | lines that do not express FLI1 (24) vs lines expressing it (18) | the lines without FLI1 respond 0.66× as strongly (z diff +1.59); strongest at Dinaciclib 5 µM: 0.64x vs 0.29x (z diff +4.3) | 0.049 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615; target measured in part of the lines; artifact flags |
| [[NBPF9]] | B | FLI1 activity raises NBPF9's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 1.50× lower at baseline in the lines without FLI1 | 0.061 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[RNF217]] | B | FLI1 activity raises RNF217's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without FLI1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[ZNF175]] | B | FLI1 activity raises ZNF175's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without FLI1 | 0.079 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| cells under [[Procainamide (hydrochloride) (drug)]] 5 µM | B | FLI1 activity raises the cells' numbers under Procainamide (hydrochloride) 5 µM (protects the cells) | lines that do not express FLI1 (31) vs lines expressing it (17) | the lines without FLI1: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[TUFT1]] | B | FLI1 activity strengthens TUFT1's drug response | lines that do not express FLI1 (29) vs lines expressing it (16) | the lines without FLI1 respond 0.85× as strongly (z diff +1.02); strongest at Harringtonine 5 µM: 1.71x vs 2.97x (z diff +2.5) | 0.096 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615; target measured in part of the lines; artifact flags |
| [[LINC02454]] | B | FLI1 activity raises LINC02454's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without FLI1 | 0.097 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.438). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.8, 15.2); signed map (25.8, 49.9). **Vector** length 66.1, 22.5% of its response variance represented; |z| ≥ 3 in 490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +13.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -8.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -4.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | Fli-1 proto-oncogene, ETS transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:128,686,535-128,813,267 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIC-1, EWSR2, FLI-1 |
| Gene groups (HGNC) | ETS transcription factor family |
| Reactome | 1 pathways, smallest: Transcriptional regulation of granulopoiesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01543](https://www.uniprot.org/uniprotkb/Q01543) (Friend leukemia integration 1 transcription factor):

> Sequence-specific transcriptional activator. Recognizes the DNA sequence 5'-C[CA]GGAAGT-3'.

**Summary**, from NCBI Gene [2313](https://www.ncbi.nlm.nih.gov/gene/2313):

> This gene encodes a transcription factor containing an ETS DNA-binding domain. The gene can undergo a t(11;22)(q24;q12) translocation with the Ewing sarcoma gene on chromosome 22, which results in a fusion gene that is present in the majority of Ewing sarcoma cases. An acute lymphoblastic leukemia-associated t(4;11)(q21;q23) translocation involving this gene has also been identified. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:3749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3749) · Entrez [2313](https://www.ncbi.nlm.nih.gov/gene/2313) · UniProt [Q01543](https://www.uniprot.org/uniprotkb/Q01543) · Ensembl [ENSG00000151702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151702)

## Data

Gene col 7555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7555); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7555]; `tensor/DDL_lfc|DDL_z.npy` [7555]; `embed/gene_vectors.npy` [7555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7555 or target_col == 7555). Every well: [[FLI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
