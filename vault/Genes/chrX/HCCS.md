---
symbol: "HCCS"
type: "gene"
col: 58
ensembl_id: "ENSG00000004961"
name: "holocytochrome c synthase"
location: "Xp22.2"
module: 7
arm: "+"
pooled_cpm: 13.35
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# HCCS

*holocytochrome c synthase* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.20× (z +19.7, q 0e+00, up in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.72× (z +12.2, q 8e-32, up in 40 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.155×); [[Vandetanib (drug)]] 0.5 µM in 1 line (C-33 A 0.0736×); [[Resveratrol (drug)]] 0.5 µM in 1 line (SNU-1 0.0868×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSCAN29]] (+0.73, fdr 7e-06), [[ZNF629]] (+0.68, fdr 1e-05), [[FUNDC1]] (+0.68, fdr 7e-06); moves opposite to [[ODF2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 23 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 58.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.20×** | +19.7 | 0e+00 | 42/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.89×** | +12.4 | 4e-33 | 43/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.72×** | +12.2 | 8e-32 | 40/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.29×** | +10.1 | 7e-22 | 38/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.34×** | +9.4 | 9e-19 | 40/46 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.13×** | +9.2 | 4e-18 | 39/47 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +8.7 | 3e-16 | 34/40 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **2.03×** | +8.6 | 6e-16 | 25/35 (A-427, SW480, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.6 | 7e-16 | 31/46 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +8.3 | 5e-15 | 33/46 (SW480, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.95×** | +8.1 | 3e-14 | 37/47 (BT-474, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.92×** | +8.0 | 8e-14 | 34/45 (KATO III, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.82×** | +7.3 | 1e-11 | 34/47 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.81×** | +7.2 | 2e-11 | 33/47 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +7.0 | 7e-11 | 31/48 (NCI-H2347, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.73×** | +6.7 | 9e-10 | 25/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +6.4 | 6e-09 | 30/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.50×** | +5.8 | 2e-07 | 22/44 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.6 | 4e-07 | 21/48 (SNU-423, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +5.3 | 2e-06 | 24/45 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +5.0 | 1e-05 | 25/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.012 | 11/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.017 | 11/45 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.020 | 6/45 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 58.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.155×); [[Vandetanib (drug)]] 0.5 µM in 1 line (C-33 A 0.0736×); [[Resveratrol (drug)]] 0.5 µM in 1 line (SNU-1 0.0868×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.820× | -3.4 | 0.32 | 15/48 (NCI-H2030, SNU-1, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.770× | -3.2 | 0.32 | 6/48 (NCI-H460, A498, …) | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.776× | -3.1 | 0.32 | 7/48 (SW 1088, A498, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 58. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.7 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +15.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.97× (z +12.0) | — |
| [[SW480 (line)]] | alt | 18.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.63× (z +9.1) | — |
| [[KATO III (line)]] | alt | 22.5 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.17× (z +12.4) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[A-427 (line)]] | wt | 22.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -12.6) |
| [[LoVo (line)]] | wt | 10.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +13.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.83× (z +9.0) | — |
| [[A498 (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 11.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[AsPC-1 (line)]] | alt | 8.03 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0736× (z -10.8) |
| [[C32 (line)]] | wt | 8.02 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[H4 (line)]] | wt | 9.54 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 5.89 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +9.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 9.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +11.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 15.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.99× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 8.82 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0868× (z -8.5) |
| [[SNU-423 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +12.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 58), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN29]] | +0.73 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.68 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[FUNDC1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.67 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.67 | +0.76 / +0.46 | both halves | 3e-05 |  |
| [[JAGN1]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.66 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.66 | +0.77 / +0.40 | both halves | 5e-05 |  |
| [[UBQLN2]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.65 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.65 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[TACO1]] | +0.65 | +0.71 / +0.47 | both halves | 2e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ODF2]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HCCS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.9, 10.6); signed map (-2.0, -26.7). **Vector** length 49.4, 7.66% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.5 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.8 | +19.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +8.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -1.5 | +7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -1.5 | +7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -1.3 | +8.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | +0.7 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | holocytochrome c synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:11,111,301-11,123,086 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CCHL; previously MLS |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P53701](https://www.uniprot.org/uniprotkb/P53701) (Holocytochrome c-type synthase):

> Lyase that catalyzes the covalent linking of the heme group to the cytochrome C apoprotein to produce the mature functional cytochrome.

**Summary**, from NCBI Gene [3052](https://www.ncbi.nlm.nih.gov/gene/3052):

> The protein encoded by this gene is an enzyme that covalently links a heme group to the apoprotein of cytochrome c. Defects in this gene are a cause of microphthalmia syndromic type 7 (MCOPS7). Three transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:4837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4837) · Entrez [3052](https://www.ncbi.nlm.nih.gov/gene/3052) · UniProt [P53701](https://www.uniprot.org/uniprotkb/P53701) · Ensembl [ENSG00000004961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004961)

## Data

Gene col 58: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 58); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 58, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 58]; `tensor/DDL_lfc|DDL_z.npy` [58]; `embed/gene_vectors.npy` [58]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 58 or target_col == 58). Every well: [[HCCS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCCS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
