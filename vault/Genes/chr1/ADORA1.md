---
symbol: "ADORA1"
type: "gene"
col: 8700
ensembl_id: "ENSG00000163485"
name: "adenosine A1 receptor"
location: "1q32.1"
module: 38
arm: "+"
pooled_cpm: 4.49
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 13
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ADORA1

*adenosine A1 receptor* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.47× (z +18.9, q 0e+00, up in 26 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.330× (z -9.9, q 3e-20, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00672]] (+0.77, fdr 7e-06), [[PYGM]] (+0.77, fdr 7e-06), [[LINC00654]] (+0.75, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[POLN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8700.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.47×** | +18.9 | 0e+00 | 26/29 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.86×** | +9.0 | 5e-17 | 14/26 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +8.0 | 2e-13 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.2 | 7e-08 | 17/37 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +6.2 | 7e-08 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.9 | 3e-07 | 13/29 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.86×** | +5.5 | 3e-06 | 15/41 (LoVo, SW 900, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.4 | 5e-06 | 10/37 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +4.8 | 1e-04 | 13/38 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +4.7 | 2e-04 | 14/33 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +4.5 | 4e-04 | 10/39 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.63×** | +4.2 | 0.001 | 5/19 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.38×** | +4.1 | 0.002 | 7/37 (NCI-H460, LoVo, …) | rises with dose | low cells (technical?) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.53×** | +3.5 | 0.019 | 5/26 (BT-474, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.5 | 0.019 | 1/17 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pimozide (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.089 | 4/28 (A-427, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.095 | 4/35 (SW 900, C-33 A, …) | two highest doses |  |
| [[Trimetrexate (drug)]] 0.05 µM |  | **1.39×** | +2.9 | 0.100 | 0/34 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.330×** | -9.9 | 3e-20 | 27/40 (H4, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.393×** | -8.3 | 2e-14 | 24/36 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.476×** | -6.6 | 6e-09 | 21/35 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -6.6 | 6e-09 | 20/26 (BT-474, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.512×** | -6.0 | 3e-07 | 18/30 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.633×** | -5.8 | 8e-07 | 18/28 (BT-474, SW 900, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.564×** | -5.1 | 3e-05 | 19/39 (H4, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -4.7 | 1e-04 | 16/36 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.578×** | -4.7 | 2e-04 | 18/35 (BT-474, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.592×** | -4.7 | 2e-04 | 19/34 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.367×** | -4.7 | 2e-04 | 14/27 (C32, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | **0.643×** | -3.8 | 0.007 | 14/33 (A-172, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -3.4 | 0.033 | 12/36 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -3.3 | 0.041 | 10/28 (C32, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.681×** | -3.2 | 0.046 | 12/34 (BT-474, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.704×** | -3.1 | 0.063 | 7/36 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.514×** | -3.1 | 0.063 | 12/34 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 23.7 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0311× (z -14.2) |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0635× (z -16.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0550× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 7.70 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.109× (z -9.1) |
| [[A-172 (line)]] | wt | 7.82 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +9.7) | [[Erlotinib (drug)]] 5 µM 0.0792× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 7.60 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0318× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 5.44 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 8.90 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.0752× (z -9.2) |
| [[A498 (line)]] | wt | 7.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +10.8) | — |
| [[C32 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0442× (z -10.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.95 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0536× (z -13.1) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A-427 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00672]] | +0.77 | +0.68 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PYGM]] | +0.77 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[LINC00654]] | +0.75 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[XG]] | +0.74 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[VWCE]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.72 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.72 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.71 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.71 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[PLCD4]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[OIT3]] | +0.70 | +0.59 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADORA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[XG]] | B | XG activity raises ADORA1's level | lines that do not express XG (5) vs lines expressing it (45) | 2.21× lower at baseline in the lines without XG | 0.070 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLN]] | B | ADORA1 activity raises POLN's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without ADORA1 | 0.009 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[STON1]] | B | ADORA1 activity raises STON1's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without ADORA1 | 0.039 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[MSANTD1]] | B | ADORA1 activity raises MSANTD1's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without ADORA1 | 0.049 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[OSMR-DT]] | B | ADORA1 activity raises OSMR-DT's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without ADORA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[PHYHD1]] | B | ADORA1 activity lowers PHYHD1's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.97× higher at baseline in the lines without ADORA1 | 0.063 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[ROPN1L]] | B | ADORA1 activity raises ROPN1L's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without ADORA1 | 0.071 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[MFSD2B]] | B | ADORA1 activity raises MFSD2B's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without ADORA1 | 0.089 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[MPP4]] | B | ADORA1 activity raises MPP4's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without ADORA1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.1, -17.2); signed map (14.9, 11.4). **Vector** length 63.0, 10.2% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +18.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +5.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -6.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.1 | -4.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -4.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | adenosine A1 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:203,090,654-203,167,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RDC7 |
| Gene groups (HGNC) | Adenosine receptors |
| Reactome | 7 pathways, smallest: Adenosine P1 receptors; Nucleotide-like (purinergic) receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P30542](https://www.uniprot.org/uniprotkb/P30542) (Adenosine receptor A1):

> Receptor for adenosine. The activity of this receptor is mediated by G proteins such as GNAI2 which inhibit adenylyl cyclase.

**Summary**, from NCBI Gene [134](https://www.ncbi.nlm.nih.gov/gene/134):

> The protein encoded by this gene is an adenosine receptor that belongs to the G-protein coupled receptor 1 family. There are 3 types of adenosine receptors, each with a specific pattern of ligand binding and tissue distribution, and together they regulate a diverse set of physiologic functions. The type A1 receptors inhibit adenylyl cyclase, and play a role in the fertilization process. Animal studies also suggest a role for A1 receptors in kidney function and ethanol intoxication. Transcript …

**Accessions** — [HGNC:262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:262) · Entrez [134](https://www.ncbi.nlm.nih.gov/gene/134) · UniProt [P30542](https://www.uniprot.org/uniprotkb/P30542) · Ensembl [ENSG00000163485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163485)

## Data

Gene col 8700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8700); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8700]; `tensor/DDL_lfc|DDL_z.npy` [8700]; `embed/gene_vectors.npy` [8700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8700 or target_col == 8700). Every well: [[ADORA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADORA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
