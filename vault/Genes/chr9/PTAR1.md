---
symbol: "PTAR1"
type: "gene"
col: 12036
ensembl_id: "ENSG00000188647"
name: "protein prenyltransferase alpha subunit repeat containing 1"
location: "9q21.12"
module: 25
arm: "+"
pooled_cpm: 85.32
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PTAR1

*protein prenyltransferase alpha subunit repeat containing 1* — 9q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.40× (z +6.3, q 2e-07, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.555× (z -15.5, q 0e+00, down in 48 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (SW480 0.359×, HOP62 0.408×, SHP-77 0.366×, LoVo 0.399×, …); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.145×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.406×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NHLRC2]] (+0.69, fdr 7e-06), [[OCRL]] (+0.65, fdr 6e-05), [[EFR3A]] (+0.65, fdr 7e-06); moves opposite to [[SPSB2]] (-0.64, fdr 1e-05), [[MILIP]] (-0.59, fdr 1e-04), [[MED26]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +6.3 | 2e-07 | 38/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 1e-05 | 34/48 (BT-474, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 3e-05 | 33/48 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +5.1 | 6e-05 | 27/48 (HT-29, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.066 | 23/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.081 | 22/48 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.11 | 19/47 (KATO III, J82, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.13 | 18/47 (NCI-H460, C-33 A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12036.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (SW480 0.359×, HOP62 0.408×, SHP-77 0.366×, LoVo 0.399×, …); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.107×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.145×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.406×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.555×** | -15.5 | 0e+00 | 48/49 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.754×** | -5.1 | 1e-04 | 32/48 (C32, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.633×** | -4.5 | 0.001 | 27/49 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -4.4 | 0.001 | 22/48 (HOP62, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.790×** | -4.2 | 0.002 | 27/50 (SW480, C-33 A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.799×** | -4.2 | 0.002 | 27/48 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.821×** | -3.7 | 0.018 | 21/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.891× | -3.1 | 0.15 | 4/48 (HT-29, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 171 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -18.4) |
| [[C32 (line)]] | wt | 137 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.7) |
| [[A498 (line)]] | wt | 121 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.88× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 51.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.7) |
| [[RKO (line)]] | wt | 85.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.1) |
| [[SNU-1 (line)]] | wt | 111 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.0) |
| [[A-427 (line)]] | wt | 49.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.7) | — |
| [[A549 (line)]] | wt | 91.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -10.0) |
| [[BT-474 (line)]] | alt | 48.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 98.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 43.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.1) |
| [[CHP-212 (line)]] | wt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -13.5) |
| [[HOP62 (line)]] | alt | 73.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -15.1) |
| [[HT-29 (line)]] | alt | 76.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.0) | — |
| [[J82 (line)]] | alt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -8.7) |
| [[KATO III (line)]] | alt | 75.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.6) | — |
| [[LoVo (line)]] | wt | 63.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.8) |
| [[LS 180 (line)]] | wt | 56.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 79.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.5) |
| [[NCI-H661 (line)]] | alt | 93.8 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.143× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 77.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -13.5) |
| [[SHP-77 (line)]] | alt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -14.5) |
| [[SNU-423 (line)]] | alt | 90.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -11.0) |
| [[SW 1088 (line)]] | alt | 76.9 | 0 | 1 | — | [[Arbutin (drug)]] 0.5 µM 0.0868× (z -8.5) |
| [[SW1417 (line)]] | alt | 82.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -10.0) |
| [[A-172 (line)]] | wt | 78.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[OCRL]] | +0.65 | +0.38 / +0.76 | both halves | 6e-05 |  |
| [[EFR3A]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[VPS36]] | +0.65 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[HUS1]] | +0.64 | +0.40 / +0.75 | both halves | 4e-05 |  |
| [[MBTPS2]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[MANEA]] | +0.62 | +0.38 / +0.69 | both halves | 7e-05 |  |
| [[TEX261]] | +0.62 | +0.33 / +0.70 | both halves | 1e-04 |  |
| [[HDHD2]] | +0.60 | +0.28 / +0.75 | both halves | 3e-04 |  |
| [[GCFC2]] | +0.60 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[TMEM209]] | +0.60 | +0.40 / +0.68 | both halves | 4e-05 |  |
| [[ALG10B]] | +0.60 | +0.42 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPSB2]] | -0.64 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[MILIP]] | -0.59 | -0.36 / -0.66 | both halves | 1e-04 |  |
| [[MED26]] | -0.57 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[RNF122]] | -0.57 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[ADORA1]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[TMEM41A]] | -0.54 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[F2]] | -0.54 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[NUDT22]] | -0.54 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[TTLL13]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[HYAL1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SHPK]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[MARK4]] | -0.53 | -0.37 / -0.55 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PTAR1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[C3orf14]] | B | C3orf14 activity raises PTAR1's level | lines that do not express C3orf14 (12) vs lines expressing it (38) | 1.29× lower at baseline in the lines without C3orf14 | 0.044 | ⚠ within organs, on part of the lines; also absent: PTPRG-AS1, EVC, WIPF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.5, -15.6); signed map (-11.6, -39.8). **Vector** length 99.8, 26.1% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.6 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.5 | +2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.2 | -15.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.9 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.0 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.2 | -5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | protein prenyltransferase alpha subunit repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.12 — chr9:69,709,522-69,760,011 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Prenyltransferase alpha subunit repeat containing; Protein geranylgeranyltransferase type III subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6K3](https://www.uniprot.org/uniprotkb/Q7Z6K3) (Protein prenyltransferase alpha subunit repeat-containing protein 1):

> Substrate-recognition subunit of the geranylgeranyl transferase type 3 (GGTase-3) complex. The GGTase-3 complex geranylgeranylates and targets FBXL2 to the cellular membranes, where FBXL2 forms part of the E3 ubiquitin-protein ligase complex SCF(FBXL2) that mediates the degradation of membrane-anchored proteins. The GGTase-3 complex geranylgeranylates Golgi v-SNARE protein YKT6 at 'Cys-194' and this prenylation is required for Golgi SNARE complex assembly.

**Summary**, from NCBI Gene [375743](https://www.ncbi.nlm.nih.gov/gene/375743):

> Predicted to enable protein prenyltransferase activity. Predicted to contribute to Rab geranylgeranyltransferase activity. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30449) · Entrez [375743](https://www.ncbi.nlm.nih.gov/gene/375743) · UniProt [Q7Z6K3](https://www.uniprot.org/uniprotkb/Q7Z6K3) · Ensembl [ENSG00000188647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188647)

## Data

Gene col 12036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12036); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12036]; `tensor/DDL_lfc|DDL_z.npy` [12036]; `embed/gene_vectors.npy` [12036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12036 or target_col == 12036). Every well: [[PTAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
