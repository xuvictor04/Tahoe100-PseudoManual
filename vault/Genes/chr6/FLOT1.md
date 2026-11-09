---
symbol: "FLOT1"
type: "gene"
col: 6001
ensembl_id: "ENSG00000137312"
name: "flotillin 1"
location: "6p21.33"
module: 109
arm: "+"
pooled_cpm: 74.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# FLOT1

*flotillin 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.99× (z +10.2, q 1e-21, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.50× (z +8.5, q 8e-15, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.557× (z -12.1, q 4e-31, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHG2]] (+0.51, fdr 2e-05), [[TGIF1]] (+0.47, fdr 4e-05), [[GAPLINC]] (+0.45, fdr 5e-05); moves opposite to [[CTPS2]] (-0.43, fdr 0.001, ⚠ not reproduced), [[GPX8]] (-0.39, fdr 3e-04), [[SLC10A7]] (-0.39, fdr 1e-04), [[TMEM101]] (-0.39, fdr 2e-04).
> It is in [[Module 109]], a single-armed module (immediate early).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +10.2 | 1e-21 | 41/49 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +8.5 | 8e-15 | 34/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.0 | 2e-13 | 32/44 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +6.0 | 4e-07 | 32/48 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.8 | 2e-04 | 24/45 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.32×** | +4.2 | 0.003 | 24/48 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.003 | 26/47 (NCI-H23, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.4 | 0.041 | 20/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Elagolix sodium (drug)]] 5 µM |  | 1.16× | +3.2 | 0.10 | 13/48 (PANC-1, LS 180, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6001.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -12.1 | 4e-31 | 37/48 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.586×** | -7.8 | 1e-12 | 34/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.649×** | -6.0 | 4e-07 | 35/48 (SW48, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -5.9 | 7e-07 | 37/48 (SW48, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -5.0 | 6e-05 | 29/48 (BT-474, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -4.6 | 3e-04 | 30/48 (SW48, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.746×** | -4.3 | 0.002 | 25/48 (PANC-1, A-172, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.735×** | -3.9 | 0.006 | 27/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.803×** | -3.2 | 0.083 | 18/48 (J82, SHP-77, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.804×** | -3.2 | 0.083 | 22/48 (PANC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.807×** | -3.1 | 0.092 | 21/48 (C-33 A, J82, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 395 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -16.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.114× (z -16.0) |
| [[A-172 (line)]] | wt | 68.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.06× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 72.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -11.7) |
| [[HOP62 (line)]] | alt | 75.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.6) |
| [[LS 180 (line)]] | wt | 40.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +9.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -9.2) |
| [[SW480 (line)]] | alt | 74.4 | 2 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 2.11× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -8.8) |
| [[A549 (line)]] | wt | 39.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 57.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 55.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +12.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 85.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.2) |
| [[LoVo (line)]] | wt | 41.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 87.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -10.4) |
| [[RKO (line)]] | wt | 94.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 52.6 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.6) ⚠ cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -9.5) |
| [[A-427 (line)]] | wt | 68.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.7) |
| [[A498 (line)]] | wt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 58.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 84.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.2) |
| [[J82 (line)]] | alt | 161 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 37.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 52.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.0) |
| [[SHP-77 (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.2) |
| [[SNU-1 (line)]] | wt | 73.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -11.9) |
| [[SW 900 (line)]] | alt | 46.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHG2]] | +0.51 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[TGIF1]] | +0.47 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[GAPLINC]] | +0.45 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[TADA3]] | +0.45 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[WASL-DT]] | +0.44 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[CPM]] | +0.43 | +0.33 / +0.41 | both halves | 1e-04 |  |
| [[ITPRIP]] | +0.43 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[RGL1]] | +0.41 | +0.27 / +0.41 | both halves | 3e-04 |  |
| [[SBNO2]] | +0.41 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[STMN3]] | +0.41 | +0.28 / +0.38 | both halves | 3e-04 |  |
| [[JUNB]] | +0.40 | +0.26 / +0.45 | both halves | 3e-04 |  |
| [[PTPN12]] | +0.40 | +0.32 / +0.46 | both halves | 2e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS2]] | -0.43 | -0.16 / -0.44 | ⚠ not reproduced | 0.001 |  |
| [[GPX8]] | -0.39 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[SLC10A7]] | -0.39 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[TMEM101]] | -0.39 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[ZRSR2]] | -0.38 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[NXF1]] | -0.38 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[ZFPL1]] | -0.38 | -0.21 / -0.36 | both halves | 6e-04 |  |
| [[IGHMBP2]] | -0.37 | -0.29 / -0.35 | both halves | 3e-04 |  |
| [[KIF21A]] | -0.37 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[DHDDS]] | -0.36 | -0.21 / -0.41 | both halves | 6e-04 |  |
| [[PSMC4]] | -0.36 | -0.30 / -0.32 | both halves | 2e-04 | pathway: Programmed Cell Death |
| [[FAM227A]] | -0.36 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[CAP2]] | -0.36 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.383). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.1, 7.1); signed map (8.9, 32.1). **Vector** length 86.4, 19.3% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +8.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | -0.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.7 | -6.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.1 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | flotillin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,727,709-30,742,732 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flotillins |
| Reactome | 13 pathways, smallest: Synaptic adhesion-like molecules; RIPK1-mediated regulated necrosis; Regulation of necroptotic cell death |
| Matched by | ensembl_id |

**Function**, from UniProt [O75955](https://www.uniprot.org/uniprotkb/O75955) (Flotillin-1):

> May act as a scaffolding protein within caveolar membranes, functionally participating in formation of caveolae or caveolae-like vesicles.

**Summary**, from NCBI Gene [10211](https://www.ncbi.nlm.nih.gov/gene/10211):

> This gene encodes an protein that localizes to the caveolae, which are small domains on the inner cell membranes. This protein plays a role in vesicle trafficking and cell morphology. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:3757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3757) · Entrez [10211](https://www.ncbi.nlm.nih.gov/gene/10211) · UniProt [O75955](https://www.uniprot.org/uniprotkb/O75955) · Ensembl [ENSG00000137312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137312)

## Data

Gene col 6001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6001); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6001]; `tensor/DDL_lfc|DDL_z.npy` [6001]; `embed/gene_vectors.npy` [6001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6001 or target_col == 6001). Every well: [[FLOT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLOT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
