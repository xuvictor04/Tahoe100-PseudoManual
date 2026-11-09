---
symbol: "GUCA1B"
type: "gene"
col: 3385
ensembl_id: "ENSG00000112599"
name: "guanylate cyclase activator 1B"
location: "6p21.1"
module: 37
arm: "+"
pooled_cpm: 12.57
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# GUCA1B

*guanylate cyclase activator 1B* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.01× (z +16.4, q 0e+00, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.530× (z -6.7, q 1e-08, down in 24 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.643× (z -4.5, q 0.002, down in 19 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.197×, HEC-1-A 0.228×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.235×, LoVo 0.275×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LS 180 0.0814×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BNIPL]] (+0.70, fdr 7e-06), [[TMEM269]] (+0.64, fdr 7e-06), [[MIA]] (+0.64, fdr 1e-05); moves opposite to [[ZDHHC21]] (-0.60, fdr 1e-05), [[DHX9]] (-0.59, fdr 3e-05), [[YWHAQ]] (-0.58, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.01×** | +16.4 | 0e+00 | 37/41 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.93×** | +11.3 | 3e-27 | 40/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +11.2 | 5e-27 | 40/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +10.7 | 1e-24 | 33/43 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +8.4 | 4e-15 | 38/46 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +8.1 | 8e-14 | 30/38 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +7.8 | 3e-13 | 30/41 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +7.6 | 2e-12 | 33/45 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +7.3 | 1e-11 | 31/43 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +7.1 | 7e-11 | 28/46 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.72×** | +5.7 | 5e-07 | 27/46 (COLO 205, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.5 | 2e-06 | 21/46 (NCI-H23, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.1 | 1e-05 | 25/44 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.4 | 4e-04 | 20/46 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.3 | 6e-04 | 19/47 (NCI-H2347, Hs 766T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.2 | 1e-03 | 21/45 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.1 | 0.001 | 20/46 (SNU-423, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3385.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.197×, HEC-1-A 0.228×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.235×, LoVo 0.275×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LS 180 0.0814×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.530×** | -6.7 | 1e-08 | 24/34 (A498, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.643×** | -4.5 | 0.002 | 19/45 (C32, SNU-423, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.732× | -3.3 | 0.18 | 13/46 (NCI-H1573, COLO 205, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.808× | -3.2 | 0.20 | 14/47 (NCI-H1573, SW 1088, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 98.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 10.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.61× (z +10.0) | — |
| [[SW480 (line)]] | alt | 15.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0814× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 16.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +10.8) | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 7.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +9.4) | — |
| [[KATO III (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +8.7) | — |
| [[LoVo (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 6.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.03× (z +12.6) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 9.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[A-172 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BNIPL]] | +0.70 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.64 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MIA]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ELMOD3]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TNFSF13B]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.62 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[RAB4B]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TMEM101]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[DCAF4L1]] | +0.61 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[COG7]] | +0.61 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[AGAP5]] | +0.60 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PPP2R2D]] | +0.60 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC21]] | -0.60 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[DHX9]] | -0.59 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ECHS1]] | -0.56 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[AKAP11]] | -0.56 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[UCP2]] | -0.55 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[PFKM]] | -0.55 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ACTR3]] | -0.55 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TTLL12]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RBBP9]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[DCTN1]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GUCA1B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, -18.6); signed map (9.5, 2.7). **Vector** length 94.6, 21.9% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.2 | +5.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +3.5 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +16.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +8.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.1 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | guanylate cyclase activator 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,183,284-42,194,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCAP2, RP48, GCAP-2, GCAP-II |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 4 pathways, smallest: Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMX6](https://www.uniprot.org/uniprotkb/Q9UMX6) (Guanylyl cyclase-activating protein 2):

> Regulates the activity of retinal membrane guanylyl cyclases (GUCY2D/RetGC1 and GUCY2F/RetGC2) in a Ca(2+)-dependent manner. At low intracellular Ca(2+) concentrations, GCAP2 binds to and allosterically activates RetGC, stimulating cGMP synthesis and restoring cGMP levels in photoreceptors during the recovery phase of phototransduction. At high Ca(2+) concentrations, GCAP2 inhibits RetGC activation, contributing to the Ca(2+)-dependent negative feedback loop that maintains photoreceptor …

**Summary**, from NCBI Gene [2979](https://www.ncbi.nlm.nih.gov/gene/2979):

> The protein encoded by this gene is a calcium-binding protein that activates photoreceptor guanylate cyclases. This gene may have arisen due to a gene duplication event since there is a highly similar gene clustered with it on chromosome 6. Mutations in this gene can cause a form of retinitis pigmentosa. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:4679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4679) · Entrez [2979](https://www.ncbi.nlm.nih.gov/gene/2979) · UniProt [Q9UMX6](https://www.uniprot.org/uniprotkb/Q9UMX6) · Ensembl [ENSG00000112599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112599)

## Data

Gene col 3385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3385); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3385]; `tensor/DDL_lfc|DDL_z.npy` [3385]; `embed/gene_vectors.npy` [3385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3385 or target_col == 3385). Every well: [[GUCA1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUCA1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
