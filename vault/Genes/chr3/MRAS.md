---
symbol: "MRAS"
type: "gene"
col: 8141
ensembl_id: "ENSG00000158186"
name: "muscle RAS oncogene homolog"
location: "3q22.3"
module: 10
arm: "+"
pooled_cpm: 4.87
n_lines_expressing: 39
n_dd_up: 39
n_dd_down: 6
n_dd_up_clean: 32
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 19
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# MRAS

*muscle RAS oncogene homolog* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.36× (z +24.9, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.555× (z -6.2, q 3e-07, down in 17 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (PANC-1 0.143×, LoVo 0.115×, NCI-H2030 0.189×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H23 0.117×, A-427 0.303×; ⚠ cell-cycle shift, explains ~32% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A-427 0.264×, NCI-H23 0.152×; ⚠ cell-cycle shift, explains ~32% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.226×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (C-33 A 0.0630×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEND6]] (+0.65, fdr 7e-06), [[PDIA3P1]] (+0.63, fdr 2e-05), [[LINC01122]] (+0.63, fdr 1e-05); moves opposite to [[PIBF1]] (-0.55, fdr 4e-04), [[TXNDC17]] (-0.54, fdr 1e-04), [[PIGU]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PAX2]] → it (grade B ⚠); 19 go from it, the strongest it → [[MCOLN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.36×** | +24.9 | 0e+00 | 29/30 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +11.0 | 2e-25 | 7/8 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +9.5 | 3e-19 | 14/20 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.7 | 3e-12 | 10/10 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +7.6 | 4e-12 | 18/32 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +7.3 | 2e-11 | 15/28 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +6.8 | 9e-10 | 18/33 (SK-MEL-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.72×** | +6.8 | 1e-09 | 20/34 (A-172, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.50×** | +5.9 | 2e-07 | 18/36 (A-172, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.75×** | +5.8 | 4e-07 | 18/36 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.8 | 4e-07 | 14/36 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.2 | 1e-05 | 14/33 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.62×** | +5.1 | 2e-05 | 15/36 (A-172, SK-MEL-2, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +5.0 | 2e-05 | 11/36 (J82, RKO, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.9 | 3e-05 | 10/37 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.58×** | +4.8 | 6e-05 | 12/36 (A-172, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +4.7 | 9e-05 | 14/34 (A-172, HOP62, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.60×** | +4.7 | 9e-05 | 14/33 (NCI-H23, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8141.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (PANC-1 0.143×, LoVo 0.115×, NCI-H2030 0.189×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H23 0.117×, A-427 0.303×; ⚠ cell-cycle shift, explains ~32% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (A-427 0.264×, NCI-H23 0.152×; ⚠ cell-cycle shift, explains ~32% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.226×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (C-33 A 0.0630×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.555×** | -6.2 | 3e-07 | 17/34 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.572×** | -5.9 | 1e-06 | 18/36 (A-427, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.595×** | -5.5 | 9e-06 | 14/28 (A-427, SNU-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.683×** | -4.0 | 0.008 | 15/35 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.685×** | -4.0 | 0.008 | 15/35 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.715×** | -3.5 | 0.039 | 10/36 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.564× | -3.1 | 0.13 | 6/25 (HS-578T, SW 900, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 24.9 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 9.99 | 0 | 3 (3 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.100× (z -11.1) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 5.98 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.2) |
| [[LoVo (line)]] | wt | 5.78 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.31× (z +12.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -9.7) |
| [[A498 (line)]] | wt | 8.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +8.7) | — |
| [[A549 (line)]] | wt | 2.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.30× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0630× (z -10.4) |
| [[C32 (line)]] | wt | 5.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.63× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 2.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +12.7) | — |
| [[J82 (line)]] | alt | 6.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.189× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 2.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 1.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.88× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 7.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +11.8) | — |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0996× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 2.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.6) | — |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.663 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND6]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PDIA3P1]] | +0.63 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[LINC01122]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ATP6V1E2]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ICA1L]] | +0.60 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[CCDC3]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SIAH1]] | +0.59 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[CNN3-DT]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TENM3-AS1]] | +0.57 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ARL14EP-DT]] | +0.57 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[LINC02026]] | +0.57 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[SYT9-AS1]] | +0.57 | +0.62 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIBF1]] | -0.55 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[TXNDC17]] | -0.54 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[PIGU]] | -0.54 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[PHC2]] | -0.50 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[SMYD4]] | -0.50 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[CKLF]] | -0.50 | -0.45 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX2]] | B | PAX2 activity raises MRAS's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.22× lower at baseline in the lines without PAX2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[MYL9]] | B | MYL9 activity raises MRAS's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without MYL9 | 0.020 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[SAMD11]] | B | SAMD11 activity raises MRAS's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 2.80× lower at baseline in the lines without SAMD11 | 0.037 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[CCDC3]] | B | CCDC3 activity raises MRAS's level | lines that do not express CCDC3 (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without CCDC3 | 0.054 | ⚠ within organs, on part of the lines; also absent: KLHL5, RIPOR3, SLC36A4; maybe low, not absent |
| [[MCOLN3]] | B | MCOLN3 activity raises MRAS's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without MCOLN3 | 0.058 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[TOP2A]] | B | TOP2A activity lowers MRAS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RBM24]] | B | RBM24 activity raises MRAS's level | lines that do not express RBM24 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without RBM24 | 0.062 | ⚠ within organs, on part of the lines; also absent: SRGN, P3H2, FMN2 |
| [[LINC00882]] | B | LINC00882 activity raises MRAS's level | lines that do not express LINC00882 (17) vs lines expressing it (33) | 2.50× lower at baseline in the lines without LINC00882 | 0.083 | ⚠ within organs, on part of the lines; also absent: TUSC3, B3GALT1, EVC |
| [[SLC25A21]] | B | SLC25A21 activity raises MRAS's level | lines that do not express SLC25A21 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without SLC25A21 | 0.084 | ⚠ within organs, on part of the lines; also absent: MIPOL1, EHD3, ZNF790; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises MRAS's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without MIR1915HG | 0.091 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN3]] | B | MRAS activity raises MCOLN3's level | lines that do not express MRAS (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without MRAS | 0.007 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[OGFRL1]] | B | MRAS activity raises OGFRL1's level | lines that do not express MRAS (11) vs lines expressing it (39) | 3.62× lower at baseline in the lines without MRAS | 0.013 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[SHISA4]] | B | MRAS activity raises SHISA4's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.70× lower at baseline in the lines without MRAS | 0.018 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[CNOT10]] | B | MRAS activity raises CNOT10's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without MRAS | 0.037 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[SUMO2P17]] | B | MRAS activity raises SUMO2P17's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without MRAS | 0.042 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[WNT3]] | B | MRAS activity raises WNT3's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without MRAS | 0.044 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[ICA1L]] | B | MRAS activity raises ICA1L's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without MRAS | 0.048 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[SLC16A2]] | B | MRAS activity raises SLC16A2's level | lines that do not express MRAS (11) vs lines expressing it (39) | 3.64× lower at baseline in the lines without MRAS | 0.049 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[SYT9-AS1]] | B | MRAS activity raises SYT9-AS1's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without MRAS | 0.057 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[FAIM]] | B | MRAS activity raises FAIM's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without MRAS | 0.057 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[CCDC3]] | B | MRAS activity raises CCDC3's level | lines that do not express MRAS (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without MRAS | 0.060 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[LINC00882]] | B | MRAS activity raises LINC00882's level | lines that do not express MRAS (11) vs lines expressing it (39) | 3.36× lower at baseline in the lines without MRAS | 0.061 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.5, 33.3); signed map (38.2, -0.4). **Vector** length 67.1, 12.9% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +24.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +6.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.8 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | muscle RAS oncogene homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,347,648-138,405,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | M-RAs, R-RAS3, RRAS3 |
| Gene groups (HGNC) | RAS type GTPase family |
| Hallmark sets | MYOGENESIS |
| Reactome | 9 pathways, smallest: Gain-of-function MRAS complexes activate RAF signaling; SHOC2 M1731 mutant abolishes MRAS complex function; Signaling by MRAS-complex mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [O14807](https://www.uniprot.org/uniprotkb/O14807) (Ras-related protein M-Ras):

> Signal transducer in the Ras-MAPK signaling pathway that regulates cell proliferation and survival. Core component of the SHOC2-MRAS-PP1c (SMP) holophosphatase complex that regulates the MAPK pathway activation. The formation of the SMP complex only occurs when MRAS is GTP-bound. Unlike other Ras proteins, MRAS has low intrinsic GTPase activity and may require additional factors for activation. The SMP complex specifically dephosphorylates the inhibitory phosphorylation at 'Ser-259' of RAF1 …

**Summary**, from NCBI Gene [22808](https://www.ncbi.nlm.nih.gov/gene/22808):

> This gene encodes a member of the Ras family of small GTPases. These membrane-associated proteins function as signal transducers in multiple processes including cell growth and differentiation, and dysregulation of Ras signaling has been associated with many types of cancer. The encoded protein may play a role in the tumor necrosis factor-alpha and MAP kinase signaling pathways. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by …

**Accessions** — [HGNC:7227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7227) · Entrez [22808](https://www.ncbi.nlm.nih.gov/gene/22808) · UniProt [O14807](https://www.uniprot.org/uniprotkb/O14807) · Ensembl [ENSG00000158186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158186)

## Data

Gene col 8141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8141); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8141]; `tensor/DDL_lfc|DDL_z.npy` [8141]; `embed/gene_vectors.npy` [8141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8141 or target_col == 8141). Every well: [[MRAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
