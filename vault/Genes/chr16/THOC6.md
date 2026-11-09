---
symbol: "THOC6"
type: "gene"
col: 5229
ensembl_id: "ENSG00000131652"
name: "THO complex subunit 6"
location: "16p13.3"
module: 54
arm: "-"
pooled_cpm: 6.81
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# THOC6

*THO complex subunit 6* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.85× (z +18.1, q 0e+00, up in 38 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.426× (z -6.3, q 2e-07, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CELSR3]] (+0.79, fdr 7e-06), [[MMP25]] (+0.78, fdr 7e-06, ⚠ same locus), [[SRCAP]] (+0.71, fdr 7e-06), [[RBM12]] (+0.71, fdr 7e-06); moves opposite to [[CRYZL1]] (-0.72, fdr 7e-06), [[SEC24B]] (-0.69, fdr 1e-05), [[RNF149]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CLCN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.85×** | +18.1 | 0e+00 | 38/41 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.61×** | +9.3 | 5e-18 | 38/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +8.6 | 1e-15 | 32/40 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +7.3 | 4e-11 | 20/30 (KATO III, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.92×** | +7.1 | 1e-10 | 14/18 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +7.1 | 1e-10 | 10/14 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.47×** | +6.5 | 7e-09 | 28/45 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +6.2 | 5e-08 | 28/45 (LoVo, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +5.9 | 3e-07 | 26/42 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.25×** | +5.6 | 1e-06 | 31/45 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.09×** | +5.3 | 7e-06 | 26/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.84×** | +4.4 | 6e-04 | 23/46 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +3.3 | 0.038 | 12/48 (LS 180, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.426×** | -6.3 | 2e-07 | 34/46 (HepG2/C3A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.445×** | -6.0 | 7e-07 | 26/46 (HT-29, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.544×** | -4.5 | 0.001 | 23/47 (NCI-H23, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.657×** | -4.4 | 0.001 | 21/46 (A-427, HT-29, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.552×** | -4.4 | 0.001 | 26/46 (A-172, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.581×** | -4.0 | 0.005 | 22/42 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.623×** | -3.5 | 0.036 | 12/45 (HOP62, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.688×** | -3.3 | 0.060 | 16/45 (COLO 205, Panc 03.27, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -3.3 | 0.060 | 18/40 (PANC-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.645×** | -3.3 | 0.060 | 18/44 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -3.2 | 0.060 | 18/43 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.637×** | -3.2 | 0.061 | 11/43 (Hs 766T, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.752×** | -3.0 | 0.098 | 17/45 (Panc 03.27, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.666×** | -3.0 | 0.098 | 7/45 (LS 180, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.61 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +18.2) | — |
| [[NCI-H1573 (line)]] | alt | 9.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +15.9) | — |
| [[RPMI-7951 (line)]] | alt | 6.92 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +9.7) | [[Bosentan (hydrate) (drug)]] 0.5 µM 0.0472× (z -9.0) |
| [[SW480 (line)]] | alt | 10.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 10.8× (z +9.7) | — |
| [[A-172 (line)]] | wt | 5.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +10.8) | — |
| [[A549 (line)]] | wt | 6.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.11× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 9.32 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.1× (z +9.0) | — |
| [[C32 (line)]] | wt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 4.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +11.8) | — |
| [[COLO 205 (line)]] | alt | 3.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.3× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 6.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 4.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 3.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +9.2) | — |
| [[LoVo (line)]] | wt | 4.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 6.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 9.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 5.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 4.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +11.1) | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELSR3]] | +0.79 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[MMP25]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 | ⚠ same locus (18.3 kb, same strand: neighbours can correlate without regulation) |
| [[SRCAP]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[RBM12]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PIEZO1]] | +0.71 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[LINC00641]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[REXO1]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R10]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZNF655]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SRSF6]] | +0.66 | +0.58 / +0.62 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[PHF19]] | +0.66 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SFPQ]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ZYX]] | +0.64 | +0.58 / +0.63 | both halves | 8e-06 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL1]] | -0.72 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[SEC24B]] | -0.69 | -0.68 / -0.56 | both halves | 1e-05 |  |
| [[RNF149]] | -0.69 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[KLHDC10]] | -0.69 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[MALSU1]] | -0.68 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[ASB7]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[CNIH4]] | -0.67 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[NENF]] | -0.66 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[SPATA7]] | -0.66 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[KLHL7]] | -0.66 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[MINDY3]] | -0.66 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[PIAS1]] | -0.66 | -0.64 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLCN4]] | B | CLCN4 activity lowers THOC6's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 1.51× higher at baseline in the lines without CLCN4 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ME3]] | B | ME3 activity lowers THOC6's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.37× higher at baseline in the lines without ME3 | 0.092 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-1.4, -13.5); signed map (16.3, -1.0). **Vector** length 96.0, 21.3% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +18.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +6.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Esmolol (hydrochloride) (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -6.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | THO complex subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,024,027-3,027,755 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2655, fSAP35; previously WDR58 |
| Gene groups (HGNC) | WD repeat domain containing; THO complex |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86W42](https://www.uniprot.org/uniprotkb/Q86W42) (THO complex subunit 6):

> Component of the THO subcomplex of the TREX complex which is thought to couple mRNA transcription, processing and nuclear export, and which specifically associates with spliced mRNA and not with unspliced pre-mRNA. Plays a key structural role in the oligomerization of the THO-DDX39B complex. TREX is recruited to spliced mRNAs by a transcription-independent mechanism, binds to mRNA upstream of the exon-junction complex (EJC) and is recruited in a splicing- and cap-dependent manner to a region …

**Summary**, from NCBI Gene [79228](https://www.ncbi.nlm.nih.gov/gene/79228):

> This gene encodes a subunit of the multi-protein THO complex, which is involved in coordination between transcription and mRNA processing. The THO complex is a component of the TREX (transcription/export) complex, which is involved in transcription and export of mRNAs. A missense mutation in this gene is associated with a neurodevelopmental disorder called Beaulieu-Boycott-Innes syndrome. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:28369](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28369) · Entrez [79228](https://www.ncbi.nlm.nih.gov/gene/79228) · UniProt [Q86W42](https://www.uniprot.org/uniprotkb/Q86W42) · Ensembl [ENSG00000131652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131652)

## Data

Gene col 5229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5229); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5229]; `tensor/DDL_lfc|DDL_z.npy` [5229]; `embed/gene_vectors.npy` [5229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5229 or target_col == 5229). Every well: [[THOC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THOC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
