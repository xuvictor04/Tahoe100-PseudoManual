---
symbol: "FGF2"
type: "gene"
col: 6214
ensembl_id: "ENSG00000138685"
name: "fibroblast growth factor 2"
location: "4q28.1"
module: 202
arm: "+"
pooled_cpm: 29.56
n_lines_expressing: 34
n_dd_up: 49
n_dd_down: 5
n_dd_up_clean: 39
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 13
direction_downstream: 10
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# FGF2

*fibroblast growth factor 2* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 6.28× (z +27.0, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.427× (z -12.5, q 2e-33, down in 24 of 32 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYGO1]] (+0.66, fdr 2e-05), [[TRIML2]] (+0.66, fdr 1e-05), [[CACNA2D1]] (+0.66, fdr 4e-05); moves opposite to [[HEATR5B]] (-0.66, fdr 1e-05), [[SH3GL1]] (-0.65, fdr 1e-05), [[MTMR14]] (-0.64, fdr 3e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TENM3]] → it (grade B ⚠); 10 go from it, the strongest it → [[UST]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.28×** | +27.0 | 0e+00 | 31/32 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.46×** | +25.8 | 0e+00 | 30/32 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +14.8 | 0e+00 | 22/28 (A549, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.90×** | +13.5 | 3e-39 | 26/32 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.49×** | +13.4 | 5e-39 | 26/32 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.39×** | +12.8 | 2e-35 | 27/32 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.35×** | +12.6 | 3e-34 | 23/32 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +11.3 | 8e-28 | 18/23 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +10.9 | 6e-26 | 19/26 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +10.4 | 1e-23 | 22/31 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.09×** | +10.2 | 7e-23 | 24/32 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.94×** | +9.7 | 1e-20 | 25/32 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +9.3 | 8e-19 | 17/32 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.18×** | +8.9 | 2e-17 | 22/32 (MIA PaCa-2, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +6.5 | 2e-09 | 18/29 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.1 | 4e-08 | 16/32 (LOX-IMVI, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 1e-06 | 15/32 (LoVo, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 1e-06 | 16/32 (hTERT-HPNE, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 3e-06 | 14/32 (J82, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +5.0 | 2e-05 | 15/32 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6214.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -12.5 | 2e-33 | 24/32 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.449×** | -11.8 | 8e-30 | 23/32 (A-172, LoVo, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.562×** | -8.5 | 3e-15 | 20/32 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.477×** | -5.7 | 2e-06 | 15/31 (J82, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.740×** | -4.5 | 9e-04 | 12/32 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.809× | -3.1 | 0.16 | 12/32 (J82, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.790× | -3.0 | 0.21 | 10/30 (NCI-H460, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 116 | 9 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -18.3) |
| [[A498 (line)]] | wt | 69.6 | 9 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +29.7) | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -12.6) |
| [[A549 (line)]] | wt | 33.2 | 8 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +20.0) | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 32.9× (z +26.3) | [[Panobinostat (drug)]] 5 µM 0.198× (z -8.7) |
| [[A-172 (line)]] | wt | 184 | 4 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 6.29× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.0568× (z -19.5) |
| [[HOP62 (line)]] | alt | 13.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +20.5) | — |
| [[hTERT-HPNE (line)]] | wt | 97.1 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.153× (z -9.5) |
| [[J82 (line)]] | alt | 55.7 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.152× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 18.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +20.6) | — |
| [[Hs 766T (line)]] | wt | 52.6 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.0795× (z -16.8) |
| [[LoVo (line)]] | wt | 70.3 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 4.13× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.131× (z -18.8) |
| [[SNU-423 (line)]] | alt | 21.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +21.6) | — |
| [[A-427 (line)]] | wt | 18.2 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 8.22× (z +13.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.371× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 12.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.3× (z +23.2) | — |
| [[HS-578T (line)]] | alt | 15.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 15.9 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.89× (z +18.9) | — |
| [[C-33 A (line)]] | alt | 64.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 7.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +17.9) | — |
| [[CHP-212 (line)]] | wt | 37.7 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0685× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 51.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 7.60 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +16.9) | — |
| [[NCI-H1792 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.89× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGO1]] | +0.66 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[TRIML2]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CACNA2D1]] | +0.66 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[IL7R]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 | STRING 591 |
| [[DRAM1]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[TENM3-AS1]] | +0.64 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[ANKRD18B]] | +0.63 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[RBM24]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[LIG4]] | +0.63 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | +0.62 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[BMPR1B]] | +0.62 | +0.58 / +0.44 | both halves | 3e-05 | pathway: Signaling by TGFB family members |
| [[TBCEL]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR5B]] | -0.66 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SH3GL1]] | -0.65 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[MTMR14]] | -0.64 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[GMCL1]] | -0.63 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TRPT1]] | -0.63 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[LCMT1]] | -0.61 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[MPG]] | -0.61 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MED26]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[PLA2G15]] | -0.59 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[METTL26]] | -0.59 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD13D]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[THOC3]] | -0.58 | -0.61 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TENM3]] | B | TENM3 activity raises FGF2's level | lines that do not express TENM3 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without TENM3 | 0.016 | ⚠ within organs, on part of the lines; also absent: TENM3-AS1, ZEB2, SRPX |
| [[TRIML2]] | B | TRIML2 activity raises FGF2's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without TRIML2 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032 |
| [[HDAC6]] | B | HDAC6 activity raises FGF2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TENM3-AS1]] | B | TENM3-AS1 activity raises FGF2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 2.58× lower at baseline in the lines without TENM3-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[SCN3A]] | B | SCN3A activity raises FGF2's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without SCN3A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865 |
| [[ZFY]] | B | ZFY activity raises FGF2's level | lines that do not express ZFY (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without ZFY | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278 |
| [[SPECC1]] | B | SPECC1 activity lowers FGF2's level | lines that do not express SPECC1 (6) vs lines expressing it (44) | 1.59× higher at baseline in the lines without SPECC1 | 0.082 | ⚠ within organs, on part of the lines; also absent: BMP8B, FARP1, KIAA1522 |
| [[SHISAL1]] | B | SHISAL1 activity raises FGF2's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 3.47× lower at baseline in the lines without SHISAL1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[TOP2A]] | B | TOP2A activity lowers FGF2's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RGS20]] | C | RGS20 activity raises FGF2's level | lines that do not express RGS20 (12) vs lines expressing it (38) | 4.95× lower at baseline in the lines without RGS20 | 0.004 | ⚠ within organs, on part of the lines; also absent: MIR130AHG, ENSG00000286964, SIX1; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises FGF2's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 3.66× lower at baseline in the lines without ZEB2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[RBM24]] | C | RBM24 activity raises FGF2's level | lines that do not express RBM24 (23) vs lines expressing it (27) | 2.83× lower at baseline in the lines without RBM24 | 0.010 | ⚠ within organs, on part of the lines; also absent: SRGN, P3H2, FMN2; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UST]] | B | FGF2 activity raises UST's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without FGF2 | 0.025 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[MPG]] | B | FGF2 activity raises MPG's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 1.17× lower at baseline in the lines without FGF2 | 0.040 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[METTL26]] | B | FGF2 activity raises METTL26's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 1.46× lower at baseline in the lines without FGF2 | 0.047 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[TENM3]] | B | FGF2 activity raises TENM3's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without FGF2 | 0.079 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[HACD1]] | B | FGF2 activity raises HACD1's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without FGF2 | 0.083 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[HEATR5B]] | B | FGF2 activity raises HEATR5B's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 1.15× lower at baseline in the lines without FGF2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[ZEB2]] | C | FGF2 activity raises ZEB2's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 6.29× lower at baseline in the lines without FGF2 | 0.014 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2; co-absent with the target |
| [[GJC1]] | C | FGF2 activity raises GJC1's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 4.24× lower at baseline in the lines without FGF2 | 0.023 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2; co-absent with the target |
| [[PYGO1]] | C | FGF2 activity raises PYGO1's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 3.73× lower at baseline in the lines without FGF2 | 0.034 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2; co-absent with the target |
| [[IL7R]] | C | FGF2 activity raises IL7R's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 3.58× lower at baseline in the lines without FGF2 | 0.087 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.3, 23.4); signed map (44.5, 23.9). **Vector** length 104, 28.6% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.4 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +25.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +27.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +10.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -11.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -12.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -8.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -5.7 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast growth factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:122,826,682-122,898,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FGFB |
| Gene groups (HGNC) | Receptor ligands; Fibroblast growth factor family |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 86 pathways, smallest: TGFBR3 regulates FGF2 signaling; FGFR2b ligand binding and activation; FGFR1b ligand binding and activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P09038](https://www.uniprot.org/uniprotkb/P09038) (Fibroblast growth factor 2):

> Acts as a ligand for FGFR1, FGFR2, FGFR3 and FGFR4. Also acts as an integrin ligand which is required for FGF2 signaling. Binds to integrin ITGAV:ITGB3. Plays an important role in the regulation of cell survival, cell division, cell differentiation and cell migration. Functions as a potent mitogen in vitro. Can induce angiogenesis. Mediates phosphorylation of ERK1/2 and thereby promotes retinal lens fiber differentiation.

**Summary**, from NCBI Gene [2247](https://www.ncbi.nlm.nih.gov/gene/2247):

> The protein encoded by this gene is a member of the fibroblast growth factor (FGF) family. FGF family members bind heparin and possess broad mitogenic and angiogenic activities. This protein has been implicated in diverse biological processes, such as limb and nervous system development, wound healing, and tumor growth. The mRNA for this gene contains multiple polyadenylation sites, and is alternatively translated from non-AUG (CUG) and AUG initiation codons, resulting in five different …

**Accessions** — [HGNC:3676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3676) · Entrez [2247](https://www.ncbi.nlm.nih.gov/gene/2247) · UniProt [P09038](https://www.uniprot.org/uniprotkb/P09038) · Ensembl [ENSG00000138685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138685)

## Data

Gene col 6214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6214); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6214]; `tensor/DDL_lfc|DDL_z.npy` [6214]; `embed/gene_vectors.npy` [6214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6214 or target_col == 6214). Every well: [[FGF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
