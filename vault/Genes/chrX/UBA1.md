---
symbol: "UBA1"
type: "gene"
col: 5152
ensembl_id: "ENSG00000130985"
name: "ubiquitin like modifier activating enzyme 1"
location: "Xp11.3"
module: 96
arm: "+"
pooled_cpm: 88.66
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# UBA1

*ubiquitin like modifier activating enzyme 1* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +12.8, q 1e-34, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.788× (z -5.1, q 2e-04, down in 29 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.176×; ⚠ toxic; transcription drop); [[Sunitinib (drug)]] 5 µM in 1 line (SW 1088 0.102×; ⚠ toxic); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1088 0.112×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACADVL]] (+0.69, fdr 1e-05), [[WDR1]] (+0.67, fdr 1e-05), [[MED16]] (+0.64, fdr 3e-05); moves opposite to [[MIR4458HG]] (-0.58, fdr 6e-05), [[SPCS1]] (-0.56, fdr 2e-05), [[SELENOH]] (-0.56, fdr 1e-04).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEC]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +12.8 | 1e-34 | 40/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +8.5 | 4e-15 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +7.1 | 3e-10 | 39/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.3 | 4e-08 | 32/49 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 1e-05 | 31/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +5.2 | 2e-05 | 31/45 (MIA PaCa-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 7e-05 | 32/48 (SK-MEL-2, A549, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +4.8 | 1e-04 | 38/49 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +4.4 | 6e-04 | 38/48 (MIA PaCa-2, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.35×** | +4.4 | 7e-04 | 25/43 (A-172, HOP62, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 30/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.27×** | +3.6 | 0.014 | 25/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.6 | 0.014 | 27/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.046 | 23/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +3.2 | 0.050 | 21/48 (NCI-H460, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5152.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.176×; ⚠ toxic; transcription drop); [[Sunitinib (drug)]] 5 µM in 1 line (SW 1088 0.102×; ⚠ toxic); [[Thymol (drug)]] 0.5 µM in 1 line (SW 1088 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -5.1 | 2e-04 | 29/49 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.804× | -3.3 | 0.22 | 29/48 (SW 1088, LOX-IMVI, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.05 µM |  | 0.851× | -3.2 | 0.22 | 18/49 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.866× | -3.1 | 0.26 | 15/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.754× | -3.1 | 0.26 | 20/48 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 97.7 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +18.2) | — |
| [[PANC-1 (line)]] | alt | 87.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +19.5) | — |
| [[A498 (line)]] | wt | 63.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +20.4) | — |
| [[A549 (line)]] | wt | 76.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 66.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +15.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 177 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 92.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 58.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -13.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 55.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.1) | — |
| [[LoVo (line)]] | wt | 72.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 73.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +12.6) | — |
| [[SW 1088 (line)]] | alt | 92.5 | 0 | 2 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.102× (z -9.0) ⚠ toxic · without an alert: [[Thymol (drug)]] 0.5 µM 0.112× (z -8.6) |
| [[SW1417 (line)]] | alt | 115 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.0) | — |
| [[A-172 (line)]] | wt | 75.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | — |
| [[HEC-1-A (line)]] | alt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 60.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.0) | — |
| [[HT-29 (line)]] | alt | 90.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 67.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.3) | — |
| [[KATO III (line)]] | alt | 111 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 61.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 68.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 55.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 67.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 117 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 67.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 57.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 47.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.0) | — |
| [[SW48 (line)]] | wt | 145 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +10.4) | — |
| [[SW480 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 131 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACADVL]] | +0.69 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[WDR1]] | +0.67 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[MED16]] | +0.64 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[CELSR3]] | +0.64 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[HAPSTR1]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DBNL]] | +0.63 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[PIGO]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CDK16]] | +0.61 | +0.48 / +0.69 | both halves | 2e-05 | STRING 603; ⚠ same locus (2.7 kb, same strand: neighbours can correlate without regulation) |
| [[SRSF6]] | +0.60 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SPTAN1]] | +0.60 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ZYX]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CDC42]] | +0.60 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[LIN7C]] | +0.60 | +0.45 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4458HG]] | -0.58 | -0.39 / -0.64 | both halves | 6e-05 |  |
| [[SPCS1]] | -0.56 | -0.46 / -0.65 | both halves | 2e-05 |  |
| [[SELENOH]] | -0.56 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[MZT2A]] | -0.55 | -0.38 / -0.63 | both halves | 7e-05 |  |
| [[TRIM52-AS1]] | -0.53 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[ATP5MK]] | -0.52 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[COX6B1]] | -0.52 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[RPL35A]] | -0.52 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[C15orf61]] ⚠ | -0.52 | -0.51 / -0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | -0.52 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[NDUFA1]] | -0.52 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[RPL36AL]] ⚠ | -0.52 | -0.37 / -0.60 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BCL7A]] | -0.51 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[RPS12]] | -0.51 | -0.43 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEC]] | C | PLEC activity raises UBA1's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.50× lower at baseline in the lines without PLEC | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.7, -20.1); signed map (-8.1, 33.5). **Vector** length 119, 34.8% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | +9.7 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +5.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +6.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +12.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.7 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.4 | +0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.3 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +0.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.8 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -5.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.0 | +1.7 |
|  | [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.8 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -2.6 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like modifier activating enzyme 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:47,190,861-47,215,128 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBE1X, POC20, CFAP124; previously A1S9T, GXP1, UBE1 |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes; Cilia and flagella associated |
| Reactome | 8 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Dengue Virus Attachment and Entry; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [P22314](https://www.uniprot.org/uniprotkb/P22314) (Ubiquitin-like modifier-activating enzyme 1):

> Catalyzes the first step in ubiquitin conjugation to mark cellular proteins for degradation through the ubiquitin-proteasome system. Activates ubiquitin by first adenylating its C-terminal glycine residue with ATP, and thereafter linking this residue to the side chain of a cysteine residue in E1, yielding a ubiquitin-E1 thioester and free AMP. Essential for the formation of radiation-induced foci, timely DNA repair and for response to replication stress. Promotes the recruitment of TP53BP1 and …

**Summary**, from NCBI Gene [7317](https://www.ncbi.nlm.nih.gov/gene/7317):

> The protein encoded by this gene catalyzes the first step in ubiquitin conjugation to mark cellular proteins for degradation. This gene complements an X-linked mouse temperature-sensitive defect in DNA synthesis, and thus may function in DNA repair. It is part of a gene cluster on chromosome Xp11.23. Alternatively spliced transcript variants that encode the same protein have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12469) · Entrez [7317](https://www.ncbi.nlm.nih.gov/gene/7317) · UniProt [P22314](https://www.uniprot.org/uniprotkb/P22314) · Ensembl [ENSG00000130985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130985)

## Data

Gene col 5152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5152); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5152]; `tensor/DDL_lfc|DDL_z.npy` [5152]; `embed/gene_vectors.npy` [5152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5152 or target_col == 5152). Every well: [[UBA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
