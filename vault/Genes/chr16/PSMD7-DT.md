---
symbol: "PSMD7-DT"
type: "gene"
col: 15343
ensembl_id: "ENSG00000261404"
name: "PSMD7 divergent transcript"
location: "16q23.1"
module: 26
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 4
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PSMD7-DT

*PSMD7 divergent transcript* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 13.5× (z +37.3, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.519× (z -6.6, q 2e-08, down in 25 of 46 measured lines) ⚠ unreliable plate only. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HEC-1-A 0.0700×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.0694×; ⚠ cell-cycle shift, explains ~44% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0753×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Malotilate (drug)]] 0.5 µM in 1 line (A-172 0.0802×); [[Terfenadine (drug)]] 0.05 µM in 1 line (J82 0.0506×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS6-AS1]] (+0.89, fdr 7e-06), [[LINC02646]] (+0.85, fdr 7e-06), [[NEB]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **13.5×** | +37.3 | 0e+00 | 38/38 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.96×** | +17.4 | 0e+00 | 32/35 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +14.7 | 0e+00 | 37/40 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.09×** | +14.3 | 6e-44 | 40/45 (A-172, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.26×** | +11.7 | 2e-29 | 31/47 (HOP62, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +11.5 | 2e-28 | 29/41 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.34×** | +8.6 | 5e-16 | 27/45 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.1 | 3e-14 | 4/8 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +7.3 | 2e-11 | 27/47 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +6.7 | 1e-09 | 21/39 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +5.6 | 9e-07 | 21/46 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +5.5 | 2e-06 | 19/46 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.3 | 6e-06 | 16/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +4.6 | 2e-04 | 4/12 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +4.5 | 2e-04 | 11/25 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.003 | 8/47 (A-172, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.005 | 8/46 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.006 | 7/47 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15343.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HEC-1-A 0.0700×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.0694×; ⚠ cell-cycle shift, explains ~44% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0753×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change); [[Malotilate (drug)]] 0.5 µM in 1 line (A-172 0.0802×); [[Terfenadine (drug)]] 0.05 µM in 1 line (J82 0.0506×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.519×** | -6.6 | 2e-08 | 25/46 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.594×** | -5.3 | 4e-05 | 19/45 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.646×** | -4.4 | 0.002 | 17/39 (NCI-H2030, NCI-H1573, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.467×** | -4.0 | 0.008 | 12/34 (RKO, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.634× | -3.3 | 0.11 | 3/47 (NCI-H1792, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.699× | -3.2 | 0.12 | 9/44 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.565× | -3.0 | 0.20 | 5/43 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.13 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.6× (z +18.4) | — |
| [[A-172 (line)]] | wt | 4.37 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.2× (z +15.4) | [[Malotilate (drug)]] 0.5 µM 0.0802× (z -8.7) |
| [[LoVo (line)]] | wt | 5.57 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +17.5) | — |
| [[NCI-H2030 (line)]] | alt | 7.71 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.7× (z +14.6) | [[Digitoxin (drug)]] 5 µM 0.0753× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW480 (line)]] | alt | 6.46 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +20.6) | — |
| [[HCT15 (line)]] | alt | 10.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 8.90 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +14.9) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0700× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 7.76 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +16.5) | — |
| [[J82 (line)]] | alt | 2.22 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +11.2) | [[Terfenadine (drug)]] 0.05 µM 0.0506× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 8.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.25× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 4.54 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 6.05 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +11.0) | — |
| [[A-427 (line)]] | wt | 5.98 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0694× (z -10.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 3.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +15.2) | — |
| [[A549 (line)]] | wt | 3.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.1× (z +11.1) | — |
| [[BT-474 (line)]] | alt | 5.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +9.5) | — |
| [[C32 (line)]] | wt | 7.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 6.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 4.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 3.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.8× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 2.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.9× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 8.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +9.8) | — |
| [[KATO III (line)]] | alt | 6.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.19× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.2× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 3.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 4.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 1.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.83× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.3× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +14.1) | — |
| [[RKO (line)]] | wt | 5.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 3.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.1× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 5.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 2.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.4× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6-AS1]] | +0.89 | +0.90 / +0.74 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.85 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[NEB]] | +0.85 | +0.84 / +0.76 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.85 | +0.88 / +0.62 | both halves | 7e-06 |  |
| [[MGAM]] | +0.84 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.84 | +0.82 / +0.61 | both halves | 7e-06 | same gene group |
| [[SIAH2-AS1]] | +0.83 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.83 | +0.87 / +0.63 | both halves | 7e-06 |  |
| [[ALG1L9P]] | +0.83 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.83 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[LINC01762]] | +0.82 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[HSD17B3]] | +0.82 | +0.75 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises PSMD7-DT's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without FSIP2-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PSMD7-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CRB1]] | B | CRB1 activity raises PSMD7-DT's level | lines that do not express CRB1 (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without CRB1 | 0.017 | ⚠ within organs, on part of the lines; also absent: DNAI1, RBFOX1, RHBDL3; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises PSMD7-DT's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.29× lower at baseline in the lines without SLC26A4 | 0.048 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[LINC02112]] | B | LINC02112 activity raises PSMD7-DT's level | lines that do not express LINC02112 (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without LINC02112 | 0.068 | ⚠ within organs, on part of the lines; also absent: DNAH6, IQCM, LINC02932; maybe low, not absent |
| [[DDR2]] | B | DDR2 activity raises PSMD7-DT's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.37× lower at baseline in the lines without DDR2 | 0.075 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity strengthens PSMD7-DT's drug response | lines that do not express LINC02641 (14) vs lines expressing it (34) | the lines without LINC02641 respond 0.87× as strongly (z diff +0.74); strongest at Homoharringtonine 5 µM: 1.68x vs 3.04x (z diff +3.0) | 0.076 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LINC01762]] | B | LINC01762 activity raises PSMD7-DT's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without LINC01762 | 0.080 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |
| [[IQCJ]] | B | IQCJ activity raises PSMD7-DT's level | lines that do not express IQCJ (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without IQCJ | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000222042, MR1, HECTD2; maybe low, not absent |
| [[LRRIQ3]] | C | LRRIQ3 activity raises PSMD7-DT's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.27× lower at baseline in the lines without LRRIQ3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.931). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.0, 18.1); signed map (24.7, -1.5). **Vector** length 75.3, 13.7% of its response variance represented; |z| ≥ 3 in 1,242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.9 | +14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +37.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +17.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +14.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +11.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.3 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | PSMD7 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16q23.1 — chr16:73,943,078-74,296,762 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53056) · Entrez [101928035](https://www.ncbi.nlm.nih.gov/gene/101928035) · Ensembl [ENSG00000261404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261404)

## Data

Gene col 15343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15343); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15343]; `tensor/DDL_lfc|DDL_z.npy` [15343]; `embed/gene_vectors.npy` [15343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15343 or target_col == 15343). Every well: [[PSMD7-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD7-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
