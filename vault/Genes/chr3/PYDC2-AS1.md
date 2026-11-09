---
symbol: "PYDC2-AS1"
type: "gene"
col: 13366
ensembl_id: "ENSG00000223812"
name: "PYDC2 antisense RNA 1"
location: "3q28"
module: 9
arm: "+"
pooled_cpm: 28.12
n_lines_expressing: 24
n_dd_up: 45
n_dd_down: 0
n_dd_up_clean: 37
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PYDC2-AS1

*PYDC2 antisense RNA 1* — 3q28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 5.33× (z +22.0, q 0e+00, up in 8 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.73× (z +20.2, q 0e+00, up in 11 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SK-MEL-2 0.174×, LOX-IMVI 0.225×, RKO 0.259×, KATO III 0.320×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (H4 0.153×, SK-MEL-2 0.261×, LOX-IMVI 0.267×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (KATO III 0.305×, NCI-H661 0.129×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Ritonavir (drug)]] 0.5 µM in 1 line (SHP-77 0.0565×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.272×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSTL5]] (+0.59, fdr 1e-05), [[LINC02241]] (+0.59, fdr 1e-05), [[CPED1]] (+0.57, fdr 1e-05); moves opposite to [[ANG]] (-0.54, fdr 2e-05), [[WDTC1]] (-0.52, fdr 1e-04), [[FCRLA]] (-0.51, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[DPH5-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.33×** | +22.0 | 0e+00 | 8/15 (HEC-1-A, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +20.2 | 0e+00 | 11/20 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.17×** | +16.4 | 0e+00 | 17/22 (RPMI-7951, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +13.7 | 1e-40 | 15/21 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +12.2 | 2e-32 | 2/16 (HEC-1-A, hTERT-HPNE) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +11.4 | 5e-28 | 21/22 (PANC-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +11.2 | 5e-27 | 13/22 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +10.1 | 4e-22 | 1/13 (HS-578T) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +9.7 | 2e-20 | 15/22 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +9.4 | 2e-19 | 17/21 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +9.4 | 3e-19 | 8/22 (C32, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +9.1 | 3e-18 | 11/20 (HS-578T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +8.2 | 8e-15 | 7/20 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.9 | 8e-14 | 8/21 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.89×** | +7.9 | 1e-13 | 4/11 (NCI-H1792, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +7.5 | 2e-12 | 14/22 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +7.2 | 2e-11 | 13/22 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +6.7 | 6e-10 | 14/21 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +6.4 | 5e-09 | 11/22 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +6.2 | 2e-08 | 11/21 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13366.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SK-MEL-2 0.174×, LOX-IMVI 0.225×, RKO 0.259×, KATO III 0.320×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (H4 0.153×, SK-MEL-2 0.261×, LOX-IMVI 0.267×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (KATO III 0.305×, NCI-H661 0.129×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Ritonavir (drug)]] 0.5 µM in 1 line (SHP-77 0.0565×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.272×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.806× | -3.1 | 0.69 | 1/22 (SW 1271) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.862× | -3.0 | 0.69 | 11/22 (KATO III, LS 180, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 135 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.57× (z +14.7) | — |
| [[SK-MEL-2 (line)]] | alt | 243 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.33× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -14.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 155 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.32× (z +13.7) | [[Docetaxel (drug)]] 0.05 µM 0.305× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 36.7 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.02× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 96.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.05× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.23× (z +9.7) | — |
| [[RKO (line)]] | wt | 138 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.34× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -10.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 116 | 3 | 0 | [[Auranofin (drug)]] 5 µM 9.77× (z +15.6) | — |
| [[H4 (line)]] | wt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -12.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 7.30 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 13.9× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 6.25× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 13.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 328 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.129× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 8.78 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0565× (z -10.5) |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSTL5]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[LINC02241]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CPED1]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[LINC02930]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[DISC1FP1]] | +0.56 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[BMPR1B]] | +0.54 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[BAGE2]] | +0.54 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[LINC01320]] | +0.53 | +0.60 / +0.32 | both halves | 2e-04 |  |
| [[GPATCH4]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[DPH5-DT]] | +0.50 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[TTC27]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[UTP20]] | +0.50 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANG]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[WDTC1]] | -0.52 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[FCRLA]] | -0.51 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[A2M]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[HAGH]] | -0.49 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[LINC03047]] | -0.49 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[RNASE4]] | -0.49 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ZCCHC24]] | -0.48 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[PHF12]] | -0.47 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ZER1]] | -0.46 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[GPR146]] | -0.45 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[TMEM50B]] | -0.45 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PYDC2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPH5-DT]] | B | PYDC2-AS1 activity raises DPH5-DT's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.42× lower at baseline in the lines without PYDC2-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[ADNP2]] | B | PYDC2-AS1 activity raises ADNP2's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.31× lower at baseline in the lines without PYDC2-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[CCDC169]] | B | PYDC2-AS1 activity raises CCDC169's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without PYDC2-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[LINC02516]] | B | PYDC2-AS1 activity raises LINC02516's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.51× lower at baseline in the lines without PYDC2-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[COMMD10]] | B | PYDC2-AS1 activity raises COMMD10's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.35× lower at baseline in the lines without PYDC2-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[DISC1FP1]] | B | PYDC2-AS1 activity raises DISC1FP1's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 3.80× lower at baseline in the lines without PYDC2-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[CARD18]] | C | PYDC2-AS1 activity raises CARD18's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without PYDC2-AS1 | 0.017 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2; co-absent with the target |
| [[AEBP1]] | C | PYDC2-AS1 activity raises AEBP1's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 2.89× lower at baseline in the lines without PYDC2-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2; co-absent with the target |
| [[CPED1]] | C | PYDC2-AS1 activity raises CPED1's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 3.55× lower at baseline in the lines without PYDC2-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.292). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.8, 27.1); signed map (38.6, 26.8). **Vector** length 55.0, 12.7% of its response variance represented; |z| ≥ 3 in 580 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +16.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +9.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +4.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | PYDC2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q28 — chr3:191,425,493-191,591,097 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LINCR-0002, RP11-197K6.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52874) · Entrez [103344926](https://www.ncbi.nlm.nih.gov/gene/103344926) · Ensembl [ENSG00000223812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223812)

## Data

Gene col 13366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13366); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13366]; `tensor/DDL_lfc|DDL_z.npy` [13366]; `embed/gene_vectors.npy` [13366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13366 or target_col == 13366). Every well: [[PYDC2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYDC2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
