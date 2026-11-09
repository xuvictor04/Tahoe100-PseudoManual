---
symbol: "ALDH1A2"
type: "gene"
col: 4932
ensembl_id: "ENSG00000128918"
name: "aldehyde dehydrogenase 1 family member A2"
location: "15q21.3"
module: 80
arm: "+"
pooled_cpm: 19.53
n_lines_expressing: 37
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# ALDH1A2

*aldehyde dehydrogenase 1 family member A2* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.71× (z +17.4, q 0e+00, up in 20 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.495× (z -8.9, q 4e-16, down in 21 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.499× (z -8.8, q 4e-16, down in 24 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01483]] (+0.67, fdr 1e-05), [[LINC02068]] (+0.66, fdr 3e-05), [[TMC1]] (+0.64, fdr 3e-05); moves opposite to [[ANAPC5]] (-0.50, fdr 1e-04), [[LINC01881]] (-0.50, fdr 9e-05), [[ATP7B]] (-0.49, fdr 9e-04, ⚠ one half only (not replicated)).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[WFDC10B]] → it (grade B ⚠); 10 go from it, the strongest it → [[ELF3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +17.4 | 0e+00 | 20/34 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +12.3 | 3e-32 | 28/35 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.14×** | +9.6 | 1e-19 | 28/33 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.11×** | +9.4 | 6e-19 | 22/33 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.3 | 2e-14 | 23/35 (SK-MEL-2, SNU-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.5 | 5e-09 | 5/19 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.2 | 2e-05 | 6/24 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.007 | 7/34 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.013 | 4/34 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.6 | 0.016 | 9/32 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +3.5 | 0.023 | 11/35 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.029 | 9/34 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.029 | 8/33 (BT-474, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.041 | 6/32 (HepG2/C3A, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.064 | 5/33 (SK-MEL-2, SW 1271, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.073 | 9/33 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.495×** | -8.9 | 4e-16 | 21/32 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.499×** | -8.8 | 4e-16 | 24/34 (HepG2/C3A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.499×** | -8.7 | 4e-16 | 26/34 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.615×** | -6.1 | 1e-07 | 19/34 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.704×** | -4.4 | 0.001 | 19/34 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.706×** | -4.4 | 0.001 | 14/34 (H4, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.713×** | -4.2 | 0.002 | 17/34 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -4.2 | 0.002 | 10/33 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.539×** | -4.1 | 0.003 | 16/33 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.723×** | -4.1 | 0.003 | 19/34 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -3.9 | 0.004 | 10/32 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.774×** | -3.1 | 0.095 | 9/35 (SW 1271, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.784× | -3.0 | 0.10 | 17/34 (HepG2/C3A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 135 | 0 | 12 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0675× (z -17.5) ⚠ toxic; cell-cycle shift, explains ~51% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0828× (z -16.8) |
| [[COLO 205 (line)]] | alt | 87.7 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0723× (z -20.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0435× (z -17.4) |
| [[SW480 (line)]] | alt | 45.5 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.185× (z -11.0) |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.158× (z -8.8) |
| [[SNU-1 (line)]] | wt | 283 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 217 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 6.93 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0895× (z -14.1) |
| [[H4 (line)]] | wt | 19.2 | 0 | 2 (2 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0536× (z -9.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 4.93 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +9.7) | — |
| [[KATO III (line)]] | alt | 5.99 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +9.1) | — |
| [[A-172 (line)]] | wt | 7.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 5.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.81× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 5.19 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.31× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01483]] | +0.67 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LINC02068]] | +0.66 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[TMC1]] | +0.64 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[LINC01348]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CEACAM16-AS1]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[LINC02889]] | +0.62 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[LIPC]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HIVEP2-DT]] | +0.61 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[TTC6]] | +0.59 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CFAP54]] | +0.59 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[LYPD1]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[SERPINB9P1]] | +0.58 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | +0.57 | +0.53 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC5]] | -0.50 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[LINC01881]] | -0.50 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[ATP7B]] | -0.49 | -0.53 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC10B]] | B | WFDC10B activity raises ALDH1A2's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.49× lower at baseline in the lines without WFDC10B | 0.031 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[LIPC]] | B | LIPC activity raises ALDH1A2's level | lines that do not express LIPC (18) vs lines expressing it (32) | 2.92× lower at baseline in the lines without LIPC | 0.048 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ALDH1A2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FBXO39]] | B | FBXO39 activity raises ALDH1A2's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.16× lower at baseline in the lines without FBXO39 | 0.091 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ALDH1A2 activity raises ELF3-AS1's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without ALDH1A2 | 0.031 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[FBXO39]] | B | ALDH1A2 activity raises FBXO39's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without ALDH1A2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[LINC02889]] | B | ALDH1A2 activity raises LINC02889's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 2.05× lower at baseline in the lines without ALDH1A2 | 0.042 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[PLB1]] | B | ALDH1A2 activity raises PLB1's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without ALDH1A2 | 0.045 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[RNF103-CHMP3]] | B | ALDH1A2 activity raises RNF103-CHMP3's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without ALDH1A2 | 0.053 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[STS]] | B | ALDH1A2 activity raises STS's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without ALDH1A2 | 0.054 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[LINC01504]] | B | ALDH1A2 activity raises LINC01504's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without ALDH1A2 | 0.065 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[SLC9C1]] | B | ALDH1A2 activity raises SLC9C1's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without ALDH1A2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[LINC00578]] | B | ALDH1A2 activity raises LINC00578's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without ALDH1A2 | 0.099 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[FBXW10B]] | B | ALDH1A2 activity raises FBXW10B's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.62× lower at baseline in the lines without ALDH1A2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 23.2); signed map (51.8, 22.3). **Vector** length 83.7, 18.1% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +17.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +1.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 1 family member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:57,953,424-58,497,866 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RALDH2 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: RA biosynthesis pathway; Signaling by Retinoic Acid; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [O94788](https://www.uniprot.org/uniprotkb/O94788) (Retinal dehydrogenase 2):

> Catalyzes the NAD-dependent oxidation of aldehyde substrates, such as all-trans-retinal and all-trans-13,14-dihydroretinal, to their corresponding carboxylic acids, all-trans-retinoate and all-trans-13,14-dihydroretinoate, respectively. Retinoate signaling is critical for the transcriptional control of many genes, for instance it is crucial for initiation of meiosis in both male and female (Probable). Recognizes retinal as substrate, both in its free form and when bound to cellular …

**Summary**, from NCBI Gene [8854](https://www.ncbi.nlm.nih.gov/gene/8854):

> This protein belongs to the aldehyde dehydrogenase family of proteins. The product of this gene is an enzyme that catalyzes the synthesis of retinoic acid (RA) from retinaldehyde. Retinoic acid, the active derivative of vitamin A (retinol), is a hormonal signaling molecule that functions in developing and adult tissues. The studies of a similar mouse gene suggest that this enzyme and the cytochrome CYP26A1, concurrently establish local embryonic retinoic acid levels which facilitate posterior …

**Accessions** — [HGNC:15472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15472) · Entrez [8854](https://www.ncbi.nlm.nih.gov/gene/8854) · UniProt [O94788](https://www.uniprot.org/uniprotkb/O94788) · Ensembl [ENSG00000128918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128918)

## Data

Gene col 4932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4932); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4932]; `tensor/DDL_lfc|DDL_z.npy` [4932]; `embed/gene_vectors.npy` [4932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4932 or target_col == 4932). Every well: [[ALDH1A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH1A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
