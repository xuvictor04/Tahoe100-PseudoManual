---
symbol: "RNFT1"
type: "gene"
col: 12081
ensembl_id: "ENSG00000189050"
name: "ring finger protein, transmembrane 1"
location: "17q23.1"
module: 94
arm: "+"
pooled_cpm: 11.98
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# RNFT1

*ring finger protein, transmembrane 1* — 17q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +16.0, q 0e+00, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.593× (z -7.3, q 1e-10, down in 15 of 29 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-423 0.0559×, Panc 03.27 0.130×, A-427 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.165×, PANC-1 0.174×; ⚠ toxic; transcription drop); [[Arbutin (drug)]] 0.05 µM in 1 line (SW48 0.0663×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.139×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMCX5]] (+0.63, fdr 7e-06), [[ZFP37]] (+0.62, fdr 2e-05), [[TATDN3]] (+0.61, fdr 1e-05); moves opposite to [[SLC25A10]] (-0.60, fdr 1e-05), [[PDCD6]] (-0.60, fdr 1e-05), [[RNPS1]] (-0.56, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +16.0 | 0e+00 | 37/47 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +11.6 | 2e-28 | 35/45 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +10.3 | 1e-22 | 33/41 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +9.9 | 7e-21 | 35/46 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +8.9 | 5e-17 | 34/48 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.5 | 8e-12 | 25/46 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +7.1 | 8e-11 | 20/47 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +7.1 | 9e-11 | 27/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +7.0 | 1e-10 | 22/47 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +6.6 | 2e-09 | 23/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.9 | 2e-07 | 23/47 (RKO, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +5.7 | 6e-07 | 20/47 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.4 | 3e-06 | 19/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.4 | 3e-06 | 17/47 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.28×** | +5.3 | 3e-06 | 22/48 (A498, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 9e-06 | 21/47 (BT-474, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 6e-05 | 17/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12081.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-423 0.0559×, Panc 03.27 0.130×, A-427 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.165×, PANC-1 0.174×; ⚠ toxic; transcription drop); [[Arbutin (drug)]] 0.05 µM in 1 line (SW48 0.0663×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.139×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.593×** | -7.3 | 1e-10 | 15/29 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 0.844× | -3.6 | 0.086 | 12/48 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.799×** | -3.4 | 0.095 | 13/47 (SW 900, NCI-H2030, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.854× | -3.4 | 0.095 | 20/47 (Hs 766T, SNU-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.3 | 0.095 | 5/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Clotrimazole (drug)]] 5 µM |  | 0.858× | -3.3 | 0.11 | 8/48 (A549, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 33.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +17.6) | — |
| [[SW480 (line)]] | alt | 22.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -16.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.67× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 8.67 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[CFPAC-1 (line)]] | alt | 6.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -8.9) ⚠ cell-cycle shift, explains ~1% of this change |
| [[HT-29 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[RPMI-7951 (line)]] | alt | 8.95 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.139× (z -8.5) |
| [[SNU-423 (line)]] | alt | 9.58 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW48 (line)]] | wt | 16.4 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0663× (z -10.5) |
| [[A-172 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX5]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZFP37]] | +0.62 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TATDN3]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[XPA]] | +0.59 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[NFU1]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[TMEM126A]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[THUMPD2]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ZNF226]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CLK4]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[RAB9A]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[BTN2A3P-1]] | +0.57 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A10]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PDCD6]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.56 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SMG1P6]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[IVNS1ABP]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ACLY]] | -0.54 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[HDAC4]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[CFL1]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[GNB1L]] | -0.53 | -0.66 / -0.36 | both halves | 9e-05 |  |
| [[TOMM40]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[PPIA]] | -0.52 | -0.57 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RNFT1's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.0, 8.1); signed map (-15.1, -13.6). **Vector** length 82.0, 15.4% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +16.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +9.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -5.4 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein, transmembrane 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.1 — chr17:59,952,240-59,964,761 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTD016 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5M7Z0](https://www.uniprot.org/uniprotkb/Q5M7Z0) (E3 ubiquitin-protein ligase RNFT1):

> E3 ubiquitin-protein ligase that acts in the endoplasmic reticulum (ER)-associated degradation (ERAD) pathway, which targets misfolded proteins that accumulate in the endoplasmic reticulum (ER) for ubiquitination and subsequent proteasome-mediated degradation. Protects cells from ER stress-induced apoptosis.

**Summary**, from NCBI Gene [51136](https://www.ncbi.nlm.nih.gov/gene/51136):

> Enables ubiquitin binding activity and ubiquitin protein ligase activity. Involved in positive regulation of ERAD pathway and protein autoubiquitination. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30206) · Entrez [51136](https://www.ncbi.nlm.nih.gov/gene/51136) · UniProt [Q5M7Z0](https://www.uniprot.org/uniprotkb/Q5M7Z0) · Ensembl [ENSG00000189050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189050)

## Data

Gene col 12081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12081); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12081]; `tensor/DDL_lfc|DDL_z.npy` [12081]; `embed/gene_vectors.npy` [12081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12081 or target_col == 12081). Every well: [[RNFT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNFT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
