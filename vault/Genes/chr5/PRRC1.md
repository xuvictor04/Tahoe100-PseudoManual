---
symbol: "PRRC1"
type: "gene"
col: 8910
ensembl_id: "ENSG00000164244"
name: "proline rich coiled-coil 1"
location: "5q23.2"
module: 56
arm: "+"
pooled_cpm: 130.78
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 34
n_dd_up_clean: 2
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# PRRC1

*proline rich coiled-coil 1* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.20× (z +5.3, q 7e-05, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.306× (z -19.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GORASP2]] (+0.86, fdr 7e-06), [[COG6]] (+0.86, fdr 7e-06), [[TMEM39A]] (+0.85, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.68, fdr 3e-05), [[ITPA]] (-0.65, fdr 3e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.20×** | +5.3 | 7e-05 | 39/49 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +4.7 | 8e-04 | 32/48 (A-427, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.42 | 25/48 (A498, NCI-H2030, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8910.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.306×** | -19.4 | 0e+00 | 47/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.406×** | -14.9 | 0e+00 | 47/49 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.326×** | -13.8 | 5e-41 | 42/44 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.347×** | -13.0 | 1e-36 | 45/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.371×** | -12.7 | 1e-34 | 46/49 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.405×** | -10.7 | 1e-24 | 42/45 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.557×** | -10.1 | 3e-22 | 45/48 (A-172, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.460×** | -9.9 | 3e-21 | 39/48 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.549×** | -7.6 | 1e-12 | 34/48 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -7.2 | 2e-11 | 33/48 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.585×** | -6.8 | 4e-10 | 41/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.586×** | -6.8 | 4e-10 | 40/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -5.5 | 2e-06 | 37/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.648×** | -5.3 | 4e-06 | 38/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -5.2 | 8e-06 | 36/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -5.1 | 1e-05 | 30/48 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -4.8 | 6e-05 | 36/50 (HOP62, AsPC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.776×** | -4.1 | 0.001 | 29/48 (hTERT-HPNE, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.744×** | -3.8 | 0.005 | 34/49 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.750×** | -3.7 | 0.007 | 32/49 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 147 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -30.2) |
| [[A-172 (line)]] | wt | 135 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -26.5) |
| [[A498 (line)]] | wt | 268 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -22.3) |
| [[AsPC-1 (line)]] | alt | 180 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -31.4) |
| [[HS-578T (line)]] | alt | 249 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -24.7) |
| [[NCI-H2347 (line)]] | alt | 264 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -28.1) |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.4) |
| [[SW 900 (line)]] | alt | 143 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.1) |
| [[H4 (line)]] | wt | 209 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.6) |
| [[Hs 766T (line)]] | wt | 179 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -20.4) |
| [[CFPAC-1 (line)]] | alt | 156 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.191× (z -15.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 158 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -21.1) |
| [[J82 (line)]] | alt | 105 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.0) |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 136 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -24.8) |
| [[LoVo (line)]] | wt | 172 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 112 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0728× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.7) |
| [[SNU-1 (line)]] | wt | 149 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0716× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -13.3) |
| [[SW480 (line)]] | alt | 82.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -10.5) |
| [[C32 (line)]] | wt | 103 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -15.0) |
| [[KATO III (line)]] | alt | 101 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -13.2) |
| [[HCT15 (line)]] | alt | 159 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 105 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 154 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -16.6) |
| [[A549 (line)]] | wt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 79.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.6) |
| [[HT-29 (line)]] | alt | 102 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -14.4) |
| [[LOX-IMVI (line)]] | wt | 80.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.5) |
| [[LS 180 (line)]] | wt | 170 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -11.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 85.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -15.9) |
| [[SK-MEL-2 (line)]] | alt | 95.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -13.2) |
| [[SW1417 (line)]] | alt | 88.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -13.4) |
| [[SW48 (line)]] | wt | 156 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.357× (z -8.6) |
| [[A-427 (line)]] | wt | 67.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.1) |
| [[AN3 CA (line)]] | alt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.8) |
| [[COLO 205 (line)]] | alt | 138 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.4) |
| [[SW 1088 (line)]] | alt | 283 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -13.4) |
| [[SW 1271 (line)]] | alt | 132 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0765× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.218× (z -9.2) |
| [[BT-474 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 77.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.9) |
| [[C-33 A (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GORASP2]] | +0.86 | +0.88 / +0.80 | both halves | 7e-06 |  |
| [[COG6]] | +0.86 | +0.87 / +0.80 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.85 | +0.92 / +0.82 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.84 | +0.89 / +0.69 | both halves | 7e-06 | STRING 796 |
| [[NUS1]] | +0.81 | +0.88 / +0.61 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.81 | +0.85 / +0.75 | both halves | 7e-06 | STRING 592 |
| [[IER3IP1]] | +0.80 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[COPB1]] | +0.79 | +0.84 / +0.70 | both halves | 7e-06 | STRING 415 |
| [[CLINT1]] | +0.79 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.78 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.78 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[SUCO]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.68 | -0.74 / -0.45 | both halves | 3e-05 |  |
| [[ITPA]] | -0.65 | -0.66 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRRC1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SNHG18]] | B | SNHG18 activity raises PRRC1's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without SNHG18 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[IQSEC2]] | C | IQSEC2 activity raises PRRC1's level | lines that do not express IQSEC2 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without IQSEC2 | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, ARHGAP10, UGDH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.7, -32.9); signed map (-50.7, 9.8). **Vector** length 152, 63.0% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.69 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.70 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.70 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +7.2 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.2 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | -0.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.6 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | -1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -9.6 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -9.5 | -7.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -9.3 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -19.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.0 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.9 | -10.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -2.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | proline rich coiled-coil 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:127,517,617-127,555,085 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32875 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M27](https://www.uniprot.org/uniprotkb/Q96M27) (Protein PRRC1):

> May act as a regulator of the protein kinase A (PKA) activity during embryonic development.

**Summary**, from NCBI Gene [133619](https://www.ncbi.nlm.nih.gov/gene/133619):

> Predicted to enable protein kinase A regulatory subunit binding activity. Predicted to be involved in epithelial structure maintenance. Predicted to be located in Golgi apparatus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28164) · Entrez [133619](https://www.ncbi.nlm.nih.gov/gene/133619) · UniProt [Q96M27](https://www.uniprot.org/uniprotkb/Q96M27) · Ensembl [ENSG00000164244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164244)

## Data

Gene col 8910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8910); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8910]; `tensor/DDL_lfc|DDL_z.npy` [8910]; `embed/gene_vectors.npy` [8910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8910 or target_col == 8910). Every well: [[PRRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
