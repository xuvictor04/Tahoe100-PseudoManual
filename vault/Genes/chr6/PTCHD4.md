---
symbol: "PTCHD4"
type: "gene"
col: 14414
ensembl_id: "ENSG00000244694"
name: "patched domain containing 4"
location: "6p12.3"
module: 62
arm: "+"
pooled_cpm: 41.36
n_lines_expressing: 17
n_dd_up: 35
n_dd_down: 15
n_dd_up_clean: 29
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 11
direction_downstream: 31
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# PTCHD4

*patched domain containing 4* — 6p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.11× (z +11.7, q 1e-28, up in 1 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +8.9, q 2e-16, up in 6 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.433× (z -8.6, q 6e-15, down in 14 of 15 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDA2R]] (+0.81, fdr 7e-06), [[PINCR]] (+0.80, fdr 7e-06), [[ACTA2]] (+0.78, fdr 7e-06); moves opposite to [[MBOAT2]] (-0.45, fdr 2e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 31 go from it, the strongest it → [[ZMAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +11.7 | 1e-28 | 1/14 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.9 | 2e-16 | 6/14 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.7 | 4e-16 | 12/15 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +8.7 | 5e-16 | 1/11 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.20×** | +8.1 | 5e-14 | 13/15 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +6.9 | 4e-10 | 9/13 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +6.7 | 2e-09 | 1/11 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **1.58×** | +6.6 | 2e-09 | 13/15 (RKO, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.82×** | +6.2 | 4e-08 | 13/15 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.6 | 1e-06 | 7/16 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.6 | 1e-06 | 13/15 (NCI-H460, H4, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.78×** | +5.5 | 2e-06 | 7/14 (A-172, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.6 | 2e-04 | 11/15 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.3 | 7e-04 | 5/11 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +4.3 | 7e-04 | 12/15 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.001 | 12/16 (NCI-H460, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.004 | 9/15 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.011 | 11/15 (H4, A-172, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.43×** | +3.4 | 0.019 | 11/14 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.020 | 8/15 (HepG2/C3A, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.433×** | -8.6 | 6e-15 | 14/15 (C32, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.440×** | -8.4 | 1e-14 | 14/15 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.472×** | -7.7 | 3e-12 | 14/15 (C32, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.565×** | -5.6 | 3e-06 | 10/15 (C32, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.587×** | -5.4 | 6e-06 | 11/14 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.599×** | -5.2 | 2e-05 | 14/15 (C32, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.602×** | -5.0 | 4e-05 | 3/15 (H4, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -4.5 | 6e-04 | 6/15 (SHP-77, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.671×** | -3.9 | 0.006 | 8/15 (CHP-212, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.018 | 12/15 (HepG2/C3A, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.709×** | -3.4 | 0.039 | 7/15 (H4, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.731×** | -3.2 | 0.066 | 2/15 (SNU-1, SHP-77) | two highest doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -3.1 | 0.074 | 5/15 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM |  | **0.654×** | -3.1 | 0.080 | 0/15 | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.566×** | -3.0 | 0.089 | 10/16 (SHP-77, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.2 | 9 (1 ⚠) | 4 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.30× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.112× (z -14.7) |
| [[SHP-77 (line)]] | alt | 357 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -23.3) |
| [[HepG2_C3A (line)]] | wt | 459 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0719× (z -16.8) |
| [[C32 (line)]] | wt | 454 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0422× (z -24.8) |
| [[H4 (line)]] | wt | 231 | 1 | 5 | [[Selinexor (drug)]] 5 µM 3.32× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.0225× (z -21.5) |
| [[A-172 (line)]] | wt | 74.8 | 4 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 5.66× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 50.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0726× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 365 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0552× (z -19.2) |
| [[A498 (line)]] | wt | 60.8 | 3 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.39× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 28.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0558× (z -16.6) |
| [[CHP-212 (line)]] | wt | 29.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0443× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +14.9) | — |
| [[RKO (line)]] | wt | 13.5 | 1 | 0 | [[Amsacrine (drug)]] 5 µM 8.29× (z +10.0) | — |
| [[A-427 (line)]] | wt | 7.44 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.60 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.95 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.43 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.50 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDA2R]] | +0.81 | +0.66 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PINCR]] | +0.80 | +0.65 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[ACTA2]] | +0.78 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[PURPL]] | +0.77 | +0.55 / +0.80 | both halves | 1e-05 | **novel candidate** |
| [[GRIN2C]] | +0.75 | +0.60 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[BAX]] | +0.74 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.74 | +0.47 / +0.78 | both halves | 2e-05 |  |
| [[ZMAT3]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MDM2]] | +0.73 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[FDXR]] | +0.70 | +0.57 / +0.76 | both halves | 8e-06 |  |
| [[RRM2B]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[FAS]] | +0.68 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT2]] | -0.45 | -0.44 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PTCHD4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises PTCHD4's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 4.04× lower at baseline in the lines without GRIN2C | 0.039 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[GDF15]] | B | GDF15 activity raises PTCHD4's level | lines that do not express GDF15 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without GDF15 | 0.069 | ⚠ within organs, on part of the lines; also absent: PCSK5, ALOX5, LINC03040 |
| [[KCNMB2-AS1]] | B | KCNMB2-AS1 activity raises PTCHD4's level | lines that do not express KCNMB2-AS1 (14) vs lines expressing it (36) | 3.48× lower at baseline in the lines without KCNMB2-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: FIRRE, STXBP6, LINC01980; maybe low, not absent |
| [[FAM13C]] | B | FAM13C activity raises PTCHD4's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.28× lower at baseline in the lines without FAM13C | 0.089 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[PINCR]] | C | PINCR activity raises PTCHD4's level | lines that do not express PINCR (29) vs lines expressing it (21) | 7.21× lower at baseline in the lines without PINCR | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; co-absent with the target |
| [[EDA2R]] | C | EDA2R activity raises PTCHD4's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 5.11× lower at baseline in the lines without EDA2R | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3; co-absent with the target |
| [[MBOAT2]] | C | MBOAT2 activity lowers PTCHD4's level | lines that do not express MBOAT2 (3) vs lines expressing it (47) | 9.42× higher at baseline in the lines without MBOAT2 | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: ZXDA, TMEM132A, IL27RA |
| [[NLGN4Y]] | C | NLGN4Y activity raises PTCHD4's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 3.41× lower at baseline in the lines without NLGN4Y | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[SCN2A]] | C | SCN2A activity raises PTCHD4's level | lines that do not express SCN2A (26) vs lines expressing it (24) | 4.34× lower at baseline in the lines without SCN2A | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTPRN, ENSG00000286251, EDA2R; maybe low, not absent; co-absent with the target |
| [[LRATD1]] | C | LRATD1 activity raises PTCHD4's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 3.09× lower at baseline in the lines without LRATD1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 28, C 3. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMAT3]] | B | PTCHD4 activity raises ZMAT3's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 3.35× lower at baseline in the lines without PTCHD4 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[PPM1D]] | B | PTCHD4 activity raises PPM1D's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.72× lower at baseline in the lines without PTCHD4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[FDXR]] | B | PTCHD4 activity raises FDXR's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.80× lower at baseline in the lines without PTCHD4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[RRM2B]] | B | PTCHD4 activity raises RRM2B's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.86× lower at baseline in the lines without PTCHD4 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[MDM2]] | B | PTCHD4 activity raises MDM2's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.31× lower at baseline in the lines without PTCHD4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[ZMAT3]] | B | PTCHD4 activity weakens ZMAT3's drug response | lines that do not express PTCHD4 (28) vs lines expressing it (16) | the lines without PTCHD4 respond 1.43× as strongly (z diff -1.04); strongest at Panobinostat 0.5 µM: 2.21x vs 0.84x (z diff -5.9) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; both ways; artifact flags |
| [[RPS27L]] | B | PTCHD4 activity strengthens RPS27L's drug response | lines that do not express PTCHD4 (33) vs lines expressing it (16) | the lines without PTCHD4 respond 1.08× as strongly (z diff +0.06); strongest at Idarubicin (hydrochloride) 5 µM: 1.17x vs 1.54x (z diff +3.2) | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; both ways; artifact flags |
| [[BLOC1S2]] | B | PTCHD4 activity raises BLOC1S2's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.43× lower at baseline in the lines without PTCHD4 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[MDM2]] | B | PTCHD4 activity strengthens MDM2's drug response | lines that do not express PTCHD4 (33) vs lines expressing it (15) | the lines without PTCHD4 respond 0.67× as strongly (z diff +2.43); rises at some drug-doses, falls at others (74% from rises): Idarubicin (hydrochloride) 0.5 µM: 1.54x vs 4.67x (z diff +5.2); Auranofin 5 µM: 0.75x vs 0.40x (z diff +4.6); Selinexor 5 µM: 1.40x vs 2.99x (z diff +3.7) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[TP53INP1]] | B | PTCHD4 activity raises TP53INP1's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.10× lower at baseline in the lines without PTCHD4 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[SESN1]] | B | PTCHD4 activity strengthens SESN1's drug response | lines that do not express PTCHD4 (33) vs lines expressing it (16) | the lines without PTCHD4 respond 0.91× as strongly (z diff +0.88); rises at some drug-doses, falls at others (74% from rises): Idarubicin (hydrochloride) 0.5 µM: 1.56x vs 2.46x (z diff +3.4); Topotecan (hydrochloride) 5 µM: 1.76x vs 2.78x (z diff +3.2); Dinaciclib 5 µM: 0.55x vs 0.29x (z diff +3.1) | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[PHLDA3]] | B | PTCHD4 activity raises PHLDA3's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without PTCHD4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 36.7); signed map (42.6, -23.7). **Vector** length 89.8, 33.8% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.63 to 26); *p53 pathway* (hallmark, mean cos +0.56 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.62 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +7.3 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +8.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.5 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.0 | -8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -7.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.9 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | patched domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.3 — chr6:47,856,673-48,111,197 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTCH53, SLC65C2, FLJ41841, dJ402H5.2; previously C6orf138 |
| Gene groups (HGNC) | Solute carrier family 65 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZW05](https://www.uniprot.org/uniprotkb/Q6ZW05) (Patched domain-containing protein 4):

> Could act as a repressor of canonical hedgehog signaling by antagonizing the effects of SMO, as suggested by down-regulation of hedgehog target genes, including GLI1, PTCH1, and PTCH2 in PTCHD4-expressing cells.

**Summary**, from NCBI Gene [442213](https://www.ncbi.nlm.nih.gov/gene/442213):

> Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21345) · Entrez [442213](https://www.ncbi.nlm.nih.gov/gene/442213) · UniProt [Q6ZW05](https://www.uniprot.org/uniprotkb/Q6ZW05) · Ensembl [ENSG00000244694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244694)

## Data

Gene col 14414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14414); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14414]; `tensor/DDL_lfc|DDL_z.npy` [14414]; `embed/gene_vectors.npy` [14414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14414 or target_col == 14414). Every well: [[PTCHD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTCHD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
