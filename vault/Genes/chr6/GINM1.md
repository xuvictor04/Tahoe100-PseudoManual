---
symbol: "GINM1"
type: "gene"
col: 625
ensembl_id: "ENSG00000055211"
name: "glycosylated integral membrane protein 1"
location: "6q25.1"
module: 30
arm: "+"
pooled_cpm: 43.36
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# GINM1

*glycosylated integral membrane protein 1* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.24× (z +14.2, q 7e-43, up in 40 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +11.7, q 3e-29, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.688× (z -9.2, q 2e-17, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCN2]] (+0.68, fdr 7e-06), [[ATP6AP2]] (+0.65, fdr 7e-06), [[ZNF277]] (+0.64, fdr 1e-05); moves opposite to [[METTL1]] (-0.63, fdr 2e-05), [[SLC35A4]] (-0.61, fdr 7e-06), [[MTNR1A]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.24×** | +14.2 | 7e-43 | 40/47 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.00×** | +11.7 | 2e-29 | 33/42 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +11.7 | 3e-29 | 40/48 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.50×** | +6.6 | 6e-09 | 28/45 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +6.3 | 4e-08 | 37/48 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.38×** | +5.6 | 2e-06 | 37/48 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 2e-06 | 31/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.2 | 1e-05 | 23/48 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.33×** | +5.1 | 3e-05 | 31/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.30×** | +4.6 | 2e-04 | 25/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.28×** | +4.3 | 8e-04 | 27/48 (LoVo, LS 180, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.26×** | +4.0 | 0.002 | 25/48 (SW480, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +4.0 | 0.003 | 24/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.24×** | +3.7 | 0.009 | 20/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.009 | 11/48 (HS-578T, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 625.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.688×** | -9.2 | 2e-17 | 28/48 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.8 | 2e-12 | 31/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -4.1 | 0.009 | 24/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.816×** | -3.5 | 0.058 | 20/48 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.779×** | -3.3 | 0.091 | 12/48 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -3.3 | 0.091 | 9/48 (HEC-1-A, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 0.881× | -3.1 | 0.16 | 7/48 (PANC-1, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 49.7 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.4) |
| [[SNU-423 (line)]] | alt | 71.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 56.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 47.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -8.8) |
| [[A-172 (line)]] | wt | 58.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.2) | — |
| [[H4 (line)]] | wt | 28.2 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0966× (z -13.0) |
| [[HS-578T (line)]] | alt | 54.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 45.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -19.2) |
| [[NCI-H2347 (line)]] | alt | 39.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.6) | — |
| [[SW480 (line)]] | alt | 43.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[A498 (line)]] | wt | 31.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 71.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.7) |
| [[C32 (line)]] | wt | 40.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.5) |
| [[Hs 766T (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 64.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -10.1) |
| [[SHP-77 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.344× (z -8.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 41.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.6) |
| [[SW 1271 (line)]] | alt | 81.3 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.116× (z -9.2) |
| [[A-427 (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ATP6AP2]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ZNF277]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[AP2A1]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.61 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PIGN]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SUMF2]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.59 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[PPP2R5E]] | +0.59 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[RECK]] | +0.59 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[GTF2IP4]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL1]] | -0.63 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[SLC35A4]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[MTNR1A]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[C3orf20]] | -0.59 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[PPP1R10]] | -0.57 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[RTL6]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[KICS2]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PTER]] | -0.56 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[HSD17B2-AS1]] | -0.56 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[ZNF317]] | -0.55 | -0.37 / -0.59 | both halves | 9e-05 |  |
| [[SRSF6]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.55 | -0.61 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GINM1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RECK]] | B | RECK activity raises GINM1's level | lines that do not express RECK (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without RECK | 0.060 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[ZNF480]] | C | ZNF480 activity raises GINM1's level | lines that do not express ZNF480 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without ZNF480 | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-19.9, -18.4); signed map (-49.9, -6.2). **Vector** length 92.8, 23.0% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +11.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.1 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.7 | +11.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.6 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | glycosylated integral membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,566,294-149,591,748 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ12G14.2; previously C6orf72 |
| Matched by | ensembl_id |

UniProt [Q9NU53](https://www.uniprot.org/uniprotkb/Q9NU53) carries no function annotation.

**Summary**, from NCBI Gene [116254](https://www.ncbi.nlm.nih.gov/gene/116254):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21074) · Entrez [116254](https://www.ncbi.nlm.nih.gov/gene/116254) · UniProt [Q9NU53](https://www.uniprot.org/uniprotkb/Q9NU53) · Ensembl [ENSG00000055211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055211)

## Data

Gene col 625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 625); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 625]; `tensor/DDL_lfc|DDL_z.npy` [625]; `embed/gene_vectors.npy` [625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 625 or target_col == 625). Every well: [[GINM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GINM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
