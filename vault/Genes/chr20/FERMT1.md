---
symbol: "FERMT1"
type: "gene"
col: 2114
ensembl_id: "ENSG00000101311"
name: "FERM domain containing kindlin 1"
location: "20p12.3"
module: 34
arm: "+"
pooled_cpm: 52.75
n_lines_expressing: 28
n_dd_up: 4
n_dd_down: 41
n_dd_up_clean: 1
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 21
direction_downstream: 11
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# FERMT1

*FERM domain containing kindlin 1* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.38× (z +10.4, q 2e-22, up in 11 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Gallic acid (hydrate) (drug)]] 0.05 µM: 1.33× (z +3.6, q 0.044, up in 10 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 4.81×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (SW48 4.45×; ⚠ cell-cycle shift, explains ~9% of this change); [[Mebendazole (drug)]] 5 µM in 1 line (SW480 2.92×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 5.27×).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.319× (z -20.0, q 0e+00, down in 25 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GJB3]] (+0.77, fdr 7e-06), [[PLEK2]] (+0.75, fdr 7e-06), [[KLK10]] (+0.75, fdr 7e-06); moves opposite to [[SELENOP]] (-0.57, fdr 1e-05), [[MTUS1-DT]] (-0.51, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[PSD3]] → it (grade B ⚠); 11 go from it, the strongest it → [[BCR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2114.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (SW48 4.81×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (SW48 4.45×; ⚠ cell-cycle shift, explains ~9% of this change); [[Mebendazole (drug)]] 5 µM in 1 line (SW480 2.92×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 5.27×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +10.4 | 2e-22 | 11/20 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +8.1 | 1e-13 | 12/25 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +6.8 | 2e-09 | 8/22 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.044 | 10/26 (CFPAC-1, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2114.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.319×** | -20.0 | 0e+00 | 25/26 (LoVo, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -11.2 | 9e-27 | 25/26 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.405×** | -11.2 | 1e-26 | 25/26 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.447×** | -9.9 | 4e-21 | 23/26 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.589×** | -9.2 | 3e-18 | 20/26 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.511×** | -8.3 | 1e-14 | 25/25 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.664×** | -7.0 | 3e-10 | 19/26 (SW48, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.519×** | -6.7 | 1e-09 | 19/27 (SW48, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.617×** | -6.7 | 1e-09 | 19/26 (SW48, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -6.6 | 2e-09 | 20/26 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.689×** | -6.3 | 2e-08 | 19/26 (SW48, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.586×** | -6.3 | 2e-08 | 19/27 (SW48, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -6.0 | 1e-07 | 21/25 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.597×** | -6.0 | 1e-07 | 19/26 (AsPC-1, SW48, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.617×** | -5.9 | 1e-07 | 20/27 (SW48, LoVo, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.598×** | -5.8 | 2e-07 | 19/25 (AsPC-1, SW48, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 571 | 2 (1 ⚠) | 36 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.81× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.0244× (z -25.1) |
| [[LoVo (line)]] | wt | 182 | 0 | 27 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0556× (z -27.5) |
| [[AsPC-1 (line)]] | alt | 363 | 0 | 26 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0526× (z -20.7) |
| [[SW480 (line)]] | alt | 63.6 | 1 | 20 (2 ⚠) | [[Mebendazole (drug)]] 5 µM 2.92× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -21.8) |
| [[NCI-H1573 (line)]] | alt | 100 | 0 | 17 | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -18.6) |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 15 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0389× (z -24.8) |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 14 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.216× (z -25.8) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0647× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 88.2 | 0 | 13 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -17.7) |
| [[KATO III (line)]] | alt | 63.0 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -20.1) |
| [[LS 180 (line)]] | wt | 253 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0883× (z -21.5) |
| [[COLO 205 (line)]] | alt | 69.3 | 1 | 4 | [[Homoharringtonine (drug)]] 0.5 µM 5.27× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0900× (z -17.4) |
| [[A-427 (line)]] | wt | 44.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.3) |
| [[Hs 766T (line)]] | wt | 62.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 43.9 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.389× (z -14.7) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.132× (z -13.1) |
| [[RKO (line)]] | wt | 44.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.0) |
| [[HT-29 (line)]] | alt | 27.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 40.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -9.3) |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -10.5) |
| [[A549 (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.7) |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -9.4) |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -11.1) |
| [[A-172 (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.93 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.59 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJB3]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PLEK2]] | +0.75 | +0.74 / +0.78 | both halves | 7e-06 | same gene group; STRING 800 |
| [[KLK10]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB5]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 | STRING 478 |
| [[ANO1]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LAMC2]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 | STRING 484 |
| [[KIAA0040]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[TMC7]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[HS3ST1]] | +0.70 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[LCK]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[BLACAT1]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ACSL5]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOP]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MTUS1-DT]] | -0.51 | -0.43 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 5, C 16. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSD3]] | B | PSD3 activity raises FERMT1's level | lines that do not express PSD3 (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without PSD3 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000253557, LINC00511, ZFPM2-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises FERMT1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LEMD1]] | B | LEMD1 activity raises FERMT1's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without LEMD1 | 0.080 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises FERMT1's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without MTUS1-DT | 0.082 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[BLACAT1]] | B | BLACAT1 activity raises FERMT1's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.90× lower at baseline in the lines without BLACAT1 | 0.096 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[SCEL]] | C | SCEL activity raises FERMT1's level | lines that do not express SCEL (35) vs lines expressing it (15) | 4.53× lower at baseline in the lines without SCEL | 0.002 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1; co-absent with the target |
| [[GJB3]] | C | GJB3 activity raises FERMT1's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 5.44× lower at baseline in the lines without GJB3 | 0.009 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises FERMT1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 5.31× lower at baseline in the lines without SERPINB5 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[CASC19]] | C | CASC19 activity raises FERMT1's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 4.74× lower at baseline in the lines without CASC19 | 0.019 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4; co-absent with the target |
| [[DHRS9]] | C | DHRS9 activity raises FERMT1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 3.66× lower at baseline in the lines without DHRS9 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; co-absent with the target |
| [[ITGB4]] | C | ITGB4 activity raises FERMT1's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 4.75× lower at baseline in the lines without ITGB4 | 0.024 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3; co-absent with the target |
| [[LINC00659]] | C | LINC00659 activity raises FERMT1's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 4.16× lower at baseline in the lines without LINC00659 | 0.029 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCR]] | B | FERMT1 activity raises BCR's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without FERMT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |
| [[RHOF]] | B | FERMT1 activity raises RHOF's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 2.09× lower at baseline in the lines without FERMT1 | 0.069 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |
| [[BCL2L1]] | B | FERMT1 activity raises BCL2L1's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 2.50× lower at baseline in the lines without FERMT1 | 0.082 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |
| [[NECTIN1]] | B | FERMT1 activity raises NECTIN1's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 2.10× lower at baseline in the lines without FERMT1 | 0.091 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |
| [[PSD3]] | B | FERMT1 activity raises PSD3's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 1.44× lower at baseline in the lines without FERMT1 | 0.095 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |
| [[RAPGEF3]] | B | FERMT1 activity raises RAPGEF3's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 1.44× lower at baseline in the lines without FERMT1 | 0.097 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |
| [[CASC19]] | C | FERMT1 activity raises CASC19's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 5.80× lower at baseline in the lines without FERMT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN; co-absent with the target |
| [[GJB3]] | C | FERMT1 activity raises GJB3's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 3.87× lower at baseline in the lines without FERMT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN; co-absent with the target |
| [[TNS4]] | C | FERMT1 activity raises TNS4's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 5.26× lower at baseline in the lines without FERMT1 | 0.059 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN; co-absent with the target |
| [[SCEL]] | C | FERMT1 activity raises SCEL's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 2.82× lower at baseline in the lines without FERMT1 | 0.064 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN; co-absent with the target |
| [[LAMC2]] | C | FERMT1 activity raises LAMC2's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 3.80× lower at baseline in the lines without FERMT1 | 0.096 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.734). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 53.0); signed map (2.5, 39.2). **Vector** length 130, 45.1% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | -11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | -1.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.7 | -6.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.3 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.0 | -5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.0 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing kindlin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:6,074,845-6,123,214 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20116, URP1, KIND1, UNC112A; previously C20orf42 |
| Gene groups (HGNC) | Fermitins; Pleckstrin homology domain containing; FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQL6](https://www.uniprot.org/uniprotkb/Q9BQL6) (Fermitin family homolog 1):

> Involved in cell adhesion. Contributes to integrin activation. When coexpressed with talin, potentiates activation of ITGA2B. Required for normal keratinocyte proliferation. Required for normal polarization of basal keratinocytes in skin, and for normal cell shape. Required for normal adhesion of keratinocytes to fibronectin and laminin, and for normal keratinocyte migration to wound sites. May mediate TGF-beta 1 signaling in tumor progression.

**Summary**, from NCBI Gene [55612](https://www.ncbi.nlm.nih.gov/gene/55612):

> This gene encodes a member of the fermitin family, and contains a FERM domain and a pleckstrin homology domain. The encoded protein is involved in integrin signaling and linkage of the actin cytoskeleton to the extracellular matrix. Mutations in this gene have been linked to Kindler syndrome. [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:15889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15889) · Entrez [55612](https://www.ncbi.nlm.nih.gov/gene/55612) · UniProt [Q9BQL6](https://www.uniprot.org/uniprotkb/Q9BQL6) · Ensembl [ENSG00000101311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101311)

## Data

Gene col 2114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2114); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2114]; `tensor/DDL_lfc|DDL_z.npy` [2114]; `embed/gene_vectors.npy` [2114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2114 or target_col == 2114). Every well: [[FERMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FERMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
