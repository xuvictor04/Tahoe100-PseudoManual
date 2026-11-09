---
symbol: "LMO4"
type: "gene"
col: 6670
ensembl_id: "ENSG00000143013"
name: "LIM domain only 4"
location: "1p22.3"
module: 133
arm: "+"
pooled_cpm: 46.05
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# LMO4

*LIM domain only 4* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +8.1, q 4e-13, up in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.69× (z +5.1, q 4e-05, up in 37 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.277×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.303×; ⚠ cell-cycle shift, explains ~32% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.344×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (AN3 CA 0.220×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUPR1]] (+0.66, fdr 1e-05), [[EIF2S2]] (+0.65, fdr 1e-05), [[CEBPG]] (+0.63, fdr 7e-06); moves opposite to [[NOC2L]] (-0.52, fdr 3e-05), [[BCAP31]] (-0.50, fdr 4e-05), [[CHID1]] (-0.50, fdr 5e-05).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PTPN13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.79×** | +8.1 | 4e-13 | 30/46 (NCI-H1792, C32, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +6.9 | 2e-09 | 40/44 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.3 | 3e-05 | 22/37 (SHP-77, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +5.1 | 4e-05 | 37/46 (NCI-H23, C32, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +5.1 | 4e-05 | 29/41 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.63×** | +4.8 | 2e-04 | 34/46 (NCI-H460, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.4 | 9e-04 | 22/45 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.37×** | +4.3 | 1e-03 | 28/46 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.3 | 0.001 | 28/43 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.004 | 26/46 (SW48, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.50×** | +4.0 | 0.004 | 27/46 (C32, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.006 | 30/46 (RKO, SW1417, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +3.8 | 0.007 | 25/46 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.008 | 24/46 (NCI-H460, J82, …) | two highest doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.028 | 26/46 (J82, NCI-H460, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.048 | 20/46 (J82, C32, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.075 | 18/47 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.098 | 18/46 (SNU-1, RKO, …) | rises with dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.277×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.303×; ⚠ cell-cycle shift, explains ~32% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.344×; ⚠ cell-cycle shift, explains ~0% of this change); [[Verteporfin (drug)]] 5 µM in 1 line (AN3 CA 0.220×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.0 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 64.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +9.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[AN3 CA (line)]] | alt | 189 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.220× (z -8.7) |
| [[C32 (line)]] | wt | 25.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +15.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 20.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +11.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 64.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +12.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 57.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[CFPAC-1 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +13.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 56.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +13.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +16.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.72 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUPR1]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[EIF2S2]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[CEBPG]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[DMGDH]] | +0.61 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[YARS1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC3A2]] | +0.60 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NIBAN1]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MIA2]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ZCCHC8]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PCK2]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[CBX4]] | +0.58 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ZBED3]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOC2L]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.50 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[CHID1]] | -0.50 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[HARS1]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[RNGTT]] | -0.48 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[CDC42EP2]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[CD59]] | -0.48 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TUBG1]] | -0.48 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[CDC37]] | -0.47 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[APEX2]] | -0.47 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[CAP1]] | -0.46 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[PDCD6]] | -0.46 | -0.46 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN13]] | B | PTPN13 activity raises LMO4's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 1.71× lower at baseline in the lines without PTPN13 | 0.015 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[TBL1X]] | C | TBL1X activity raises LMO4's level | lines that do not express TBL1X (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without TBL1X | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF160, ZNF845, CRPPA; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.4, 47.5); signed map (-12.3, 22.5). **Vector** length 111, 33.2% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.5 | +8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.2 | +5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.1 | +6.9 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.1 | +4.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.6 | +2.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.5 | +3.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain only 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:87,328,880-87,348,923 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LIM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P61968](https://www.uniprot.org/uniprotkb/P61968) (LIM domain transcription factor LMO4):

> Transcription cofactor. Plays a role in establishing motor neuron identity, in concert with MNX1, acting, at least in part, to disrupt LDB1-LHX3 complexes thereby negatively modulating interneuron genes in motor neurons.

**Summary**, from NCBI Gene [8543](https://www.ncbi.nlm.nih.gov/gene/8543):

> This gene encodes a cysteine-rich protein that contains two LIM domains but lacks a DNA-binding homeodomain. The encoded protein may play a role as a transcriptional regulator or as an oncogene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:6644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6644) · Entrez [8543](https://www.ncbi.nlm.nih.gov/gene/8543) · UniProt [P61968](https://www.uniprot.org/uniprotkb/P61968) · Ensembl [ENSG00000143013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143013)

## Data

Gene col 6670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6670); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6670]; `tensor/DDL_lfc|DDL_z.npy` [6670]; `embed/gene_vectors.npy` [6670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6670 or target_col == 6670). Every well: [[LMO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
