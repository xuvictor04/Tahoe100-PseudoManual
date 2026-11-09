---
symbol: "EMP1"
type: "gene"
col: 5572
ensembl_id: "ENSG00000134531"
name: "epithelial membrane protein 1"
location: "12p13.1"
module: 78
arm: "+"
pooled_cpm: 207.98
n_lines_expressing: 40
n_dd_up: 3
n_dd_down: 41
n_dd_up_clean: 0
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 6
direction_downstream: 9
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# EMP1

*epithelial membrane protein 1* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.80× (z +6.5, q 4e-08, up in 32 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 4.92×, NCI-H1573 2.91×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (C32 3.87×, MIA PaCa-2 3.31×); [[Tucidinostat (drug)]] 5 µM in 2 lines (BT-474 3.06×, SK-MEL-2 1.86×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 3.18×).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.348× (z -16.4, q 0e+00, down in 35 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA6]] (+0.66, fdr 7e-06), [[MIR222HG]] (+0.63, fdr 7e-06), [[MICAL2]] (+0.62, fdr 8e-06); moves opposite to [[LSM8]] (-0.50, fdr 3e-05), [[VPS33A]] (-0.50, fdr 3e-05), [[PAIP1]] (-0.49, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EFNB2]] → it (grade B ⚠); 9 go from it, the strongest it → [[PTPRE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5572.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 4.92×, NCI-H1573 2.91×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (C32 3.87×, MIA PaCa-2 3.31×); [[Tucidinostat (drug)]] 5 µM in 2 lines (BT-474 3.06×, SK-MEL-2 1.86×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 3.18×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.5 | 4e-08 | 32/39 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.3 | 8e-08 | 29/35 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.6 | 8e-04 | 23/36 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 1.37× | +3.4 | 0.11 | 21/38 (SW 900, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5572.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.348×** | -16.4 | 0e+00 | 35/38 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.453×** | -12.3 | 2e-32 | 34/39 (SW48, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.362×** | -11.2 | 8e-27 | 33/38 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.426×** | -9.4 | 9e-19 | 33/38 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.426×** | -9.0 | 2e-17 | 33/37 (J82, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.459×** | -8.2 | 2e-14 | 33/38 (SK-MEL-2, J82, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.492×** | -7.8 | 6e-13 | 29/38 (J82, H4, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.474×** | -7.8 | 6e-13 | 31/40 (J82, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -7.0 | 1e-10 | 29/38 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.623×** | -6.9 | 3e-10 | 30/38 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.543×** | -6.7 | 1e-09 | 29/37 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.561×** | -6.3 | 1e-08 | 26/38 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.556×** | -6.2 | 3e-08 | 27/38 (KATO III, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.551×** | -6.0 | 6e-08 | 29/38 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.587×** | -5.8 | 2e-07 | 28/39 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.651×** | -5.8 | 3e-07 | 28/38 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5572. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 214 | 1 | 13 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.86× (z +8.6) | [[Cobimetinib (drug)]] 5 µM 0.251× (z -12.7) |
| [[SW480 (line)]] | alt | 232 | 0 | 11 | — | [[Cobimetinib (drug)]] 5 µM 0.101× (z -11.9) |
| [[J82 (line)]] | alt | 125 | 0 | 10 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.193× (z -14.3) |
| [[KATO III (line)]] | alt | 1,022 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -23.3) |
| [[MIA PaCa-2 (line)]] | alt | 265 | 4 (3 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.31× (z +9.2) | [[Adagrasib (drug)]] 0.05 µM 0.523× (z -16.8) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.6) |
| [[hTERT-HPNE (line)]] | wt | 832 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -15.8) |
| [[H4 (line)]] | wt | 242 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -20.8) |
| [[HEC-1-A (line)]] | alt | 266 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -17.0) |
| [[HOP62 (line)]] | alt | 263 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.170× (z -12.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 234 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -19.7) |
| [[RKO (line)]] | wt | 159 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -17.5) |
| [[AsPC-1 (line)]] | alt | 494 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -13.7) |
| [[C32 (line)]] | wt | 187 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.33× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.87× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 229 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -13.9) |
| [[Hs 766T (line)]] | wt | 644 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 770 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -15.0) |
| [[RPMI-7951 (line)]] | alt | 239 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.1) |
| [[LoVo (line)]] | wt | 273 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 329 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -11.5) |
| [[LS 180 (line)]] | wt | 227 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 220 | 0 | 3 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.588× (z -13.4) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.0) |
| [[SW1417 (line)]] | alt | 202 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -11.0) |
| [[SW48 (line)]] | wt | 455 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -17.9) |
| [[HS-578T (line)]] | alt | 155 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.4) |
| [[HT-29 (line)]] | alt | 253 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -11.1) |
| [[BT-474 (line)]] | alt | 57.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.06× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 63.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.1) |
| [[SW 1088 (line)]] | alt | 233 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0992× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 42.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 39.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 46.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5572), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA6]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[MIR222HG]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ASAP2]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NES]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[DUSP5]] | +0.58 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[MPRIP]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[DOCK5]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[RAP1GAP2]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NIBAN2]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[AKAP13]] | +0.56 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[COTL1]] | +0.56 | +0.46 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM8]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[VPS33A]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PAIP1]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TRAFD1]] | -0.48 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[DHX30]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TRAPPC13]] | -0.48 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[C2orf42]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[ALG12]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ACOT2]] | -0.47 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[ZNF775]] | -0.47 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[RWDD3]] | -0.46 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[FBXO6]] | -0.46 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNB2]] | B | EFNB2 activity raises EMP1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 3.49× lower at baseline in the lines without EFNB2 | 0.001 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[PTPRE]] | B | PTPRE activity raises EMP1's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without PTPRE | 0.020 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[MAP2K1]] | B | MAP2K1 activity raises EMP1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.030 | ⚠ off-target possible; 4 compounds |
| [[HMGA2]] | B | HMGA2 activity raises EMP1's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.08× lower at baseline in the lines without HMGA2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[TINAGL1]] | B | TINAGL1 activity raises EMP1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.95× lower at baseline in the lines without TINAGL1 | 0.066 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[S100A16]] | B | S100A16 activity raises EMP1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.90× lower at baseline in the lines without S100A16 | 0.081 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRE]] | B | EMP1 activity raises PTPRE's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 3.03× lower at baseline in the lines without EMP1 | 0.017 | ⚠ within organs, on part of the lines |
| [[RAP1GAP2]] | B | EMP1 activity lowers RAP1GAP2's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.01× higher at baseline in the lines without EMP1 | 0.028 | ⚠ within organs, on part of the lines |
| [[NIBAN2]] | B | EMP1 activity raises NIBAN2's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without EMP1 | 0.042 | ⚠ within organs, on part of the lines |
| [[S100A16]] | B | EMP1 activity raises S100A16's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.84× lower at baseline in the lines without EMP1 | 0.048 | ⚠ within organs, on part of the lines |
| [[BZW1]] | B | EMP1 activity raises BZW1's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 1.23× lower at baseline in the lines without EMP1 | 0.051 | ⚠ within organs, on part of the lines |
| [[ACOT2]] | B | EMP1 activity lowers ACOT2's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.01× higher at baseline in the lines without EMP1 | 0.059 | ⚠ within organs, on part of the lines |
| [[VPS33A]] | B | EMP1 activity lowers VPS33A's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 1.38× higher at baseline in the lines without EMP1 | 0.070 | ⚠ within organs, on part of the lines |
| [[PLAT]] | B | EMP1 activity raises PLAT's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 3.58× lower at baseline in the lines without EMP1 | 0.071 | ⚠ within organs, on part of the lines |
| [[PODXL]] | B | EMP1 activity raises PODXL's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 2.68× lower at baseline in the lines without EMP1 | 0.085 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.6, 6.2); signed map (6.4, 44.4). **Vector** length 131, 43.2% of its response variance represented; |z| ≥ 3 in 1,488 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.5 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | -5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | -11.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +2.5 | +1.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.1 | -8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.7 | -9.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.6 | -5.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.1 | -7.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.0 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.5 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | epithelial membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:13,196,723-13,219,941 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TMP, CL-20 |
| Hallmark sets | APOPTOSIS, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

UniProt [P54849](https://www.uniprot.org/uniprotkb/P54849) carries no function annotation.

**Summary**, from NCBI Gene [2012](https://www.ncbi.nlm.nih.gov/gene/2012):

> Involved in apoptotic process and bleb assembly. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3333) · Entrez [2012](https://www.ncbi.nlm.nih.gov/gene/2012) · UniProt [P54849](https://www.uniprot.org/uniprotkb/P54849) · Ensembl [ENSG00000134531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134531)

## Data

Gene col 5572: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5572); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5572, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5572]; `tensor/DDL_lfc|DDL_z.npy` [5572]; `embed/gene_vectors.npy` [5572]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5572 or target_col == 5572). Every well: [[EMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
