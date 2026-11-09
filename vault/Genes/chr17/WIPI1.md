---
symbol: "WIPI1"
type: "gene"
col: 956
ensembl_id: "ENSG00000070540"
name: "WD repeat domain, phosphoinositide interacting 1"
location: "17q24.2"
module: 56
arm: "+"
pooled_cpm: 42.51
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 47
n_dd_up_clean: 0
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# WIPI1

*WD repeat domain, phosphoinositide interacting 1* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.32× (z +4.0, q 0.035, up in 21 of 46 measured lines) ⚠ cell-cycle shift, explains ~34% of this change.
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.220× (z -28.2, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERLEC1]] (+0.73, fdr 7e-06), [[ARFGAP3]] (+0.73, fdr 7e-06), [[BET1L]] (+0.72, fdr 7e-06); moves opposite to [[SF3B3]] (-0.63, fdr 1e-05), [[ZNF532]] (-0.63, fdr 3e-05), [[YWHAE]] (-0.62, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.32×** | +4.0 | 0.035 | 21/46 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 1.26× | +3.3 | 0.24 | 10/47 (HOP62, J82, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.49× | +3.2 | 0.30 | 9/45 (A498, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.31 | 8/47 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.220×** | -28.2 | 0e+00 | 45/46 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.200×** | -23.2 | 0e+00 | 45/46 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.268×** | -19.7 | 0e+00 | 46/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.311×** | -17.5 | 0e+00 | 42/46 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.443×** | -12.2 | 4e-32 | 38/47 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.530×** | -11.7 | 9e-30 | 38/47 (HOP62, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -11.0 | 4e-26 | 32/47 (NCI-H1792, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.252×** | -10.8 | 2e-25 | 40/48 (HS-578T, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.493×** | -10.6 | 2e-24 | 33/47 (KATO III, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.508×** | -10.2 | 2e-22 | 30/44 (A498, HOP62, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.513×** | -9.6 | 4e-20 | 33/46 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.504×** | -9.5 | 1e-19 | 24/39 (hTERT-HPNE, KATO III, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.645×** | -8.5 | 8e-16 | 36/47 (HS-578T, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.592×** | -7.8 | 2e-13 | 34/47 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.380×** | -7.6 | 1e-12 | 33/46 (HS-578T, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.582×** | -7.5 | 2e-12 | 32/46 (A549, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.466×** | -6.0 | 6e-08 | 33/47 (HepG2/C3A, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.704×** | -5.2 | 4e-06 | 23/47 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.524×** | -5.1 | 1e-05 | 25/47 (RPMI-7951, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -4.8 | 4e-05 | 22/47 (KATO III, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 101 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0584× (z -33.7) |
| [[KATO III (line)]] | alt | 69.4 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.1) |
| [[A498 (line)]] | wt | 94.8 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0926× (z -31.8) |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 12 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0946× (z -19.2) |
| [[SW 900 (line)]] | alt | 64.5 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0579× (z -25.8) |
| [[HOP62 (line)]] | alt | 63.4 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -26.5) |
| [[A549 (line)]] | wt | 41.8 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0853× (z -20.9) |
| [[AsPC-1 (line)]] | alt | 23.9 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 81.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -28.5) |
| [[A-172 (line)]] | wt | 75.5 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.178× (z -16.2) |
| [[HepG2_C3A (line)]] | wt | 62.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0884× (z -20.0) |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.136× (z -15.4) |
| [[HT-29 (line)]] | alt | 48.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0826× (z -21.9) |
| [[Hs 766T (line)]] | wt | 44.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 39.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -20.2) |
| [[RPMI-7951 (line)]] | alt | 67.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -27.3) |
| [[SW480 (line)]] | alt | 26.7 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.209× (z -13.1) |
| [[LoVo (line)]] | wt | 28.2 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0861× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 28.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -15.7) |
| [[J82 (line)]] | alt | 43.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 3 | — | [[TAK-901 (drug)]] 0.05 µM 0.174× (z -10.0) |
| [[A-427 (line)]] | wt | 28.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.183× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.1) |
| [[COLO 205 (line)]] | alt | 47.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0561× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 76.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -16.2) |
| [[SNU-423 (line)]] | alt | 68.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.4) |
| [[SW 1088 (line)]] | alt | 63.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -9.2) |
| [[BT-474 (line)]] | alt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.8) |
| [[H4 (line)]] | wt | 80.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.7) |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.8) |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0638× (z -9.8) |
| [[SW1417 (line)]] | alt | 58.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.2) |
| [[SW48 (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -9.9) |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERLEC1]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[ARFGAP3]] | +0.73 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[BET1L]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[OSBPL2]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[MPST]] | +0.71 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TULP3]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SELENOS]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TMED9]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[PDXDC1]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[LINC01881]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B3]] | -0.63 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[ZNF532]] | -0.63 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[YWHAE]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[GTF3C6]] | -0.61 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[AFG1L]] | -0.61 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[USP24]] | -0.61 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[ZNF462]] | -0.61 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RIF1]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[UTP20]] | -0.60 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[AGL]] | -0.59 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[FUBP1]] | -0.59 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[SLC16A9]] | -0.59 | -0.53 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WIPI1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GK]] | C | GK activity raises WIPI1's level | lines that do not express GK (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without GK | 0.042 | ⚠ few lines (4 vs 46); across organs; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.6, -35.0); signed map (-47.5, 12.5). **Vector** length 134, 45.1% of its response variance represented; |z| ≥ 3 in 1,409 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.52 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.51 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.2 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.2 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.6 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.6 | -11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -19.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.3 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -23.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -8.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.4 | -7.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.2 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.4 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain, phosphoinositide interacting 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:68,420,948-68,457,513 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10055, WIPI49, ATG18, ATG18A |
| Gene groups (HGNC) | WD repeat domain containing; Autophagy related; WIPI family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 7 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5MNZ9](https://www.uniprot.org/uniprotkb/Q5MNZ9) (WD repeat domain phosphoinositide-interacting protein 1):

> Component of the autophagy machinery that controls the major intracellular degradation process by which cytoplasmic materials are packaged into autophagosomes and delivered to lysosomes for degradation. Plays an important role in starvation- and calcium-mediated autophagy, as well as in mitophagy. Functions downstream of the ULK1 and PI3-kinases that produce phosphatidylinositol 3-phosphate (PtdIns3P) on membranes of the endoplasmic reticulum once activated. Binds phosphatidylinositol …

**Summary**, from NCBI Gene [55062](https://www.ncbi.nlm.nih.gov/gene/55062):

> This gene encodes a WD40 repeat protein. Members of the WD40 repeat family are key components of many essential biologic functions. They regulate the assembly of multiprotein complexes by presenting a beta-propeller platform for simultaneous and reversible protein-protein interactions. Members of the WIPI subfamily of WD40 repeat proteins have a 7-bladed propeller structure and contain a conserved motif for interaction with phospholipids. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:25471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25471) · Entrez [55062](https://www.ncbi.nlm.nih.gov/gene/55062) · UniProt [Q5MNZ9](https://www.uniprot.org/uniprotkb/Q5MNZ9) · Ensembl [ENSG00000070540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070540)

## Data

Gene col 956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 956); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 956]; `tensor/DDL_lfc|DDL_z.npy` [956]; `embed/gene_vectors.npy` [956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 956 or target_col == 956). Every well: [[WIPI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WIPI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
