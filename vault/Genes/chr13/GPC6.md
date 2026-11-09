---
symbol: "GPC6"
type: "gene"
col: 11370
ensembl_id: "ENSG00000183098"
name: "glypican 6"
location: "13q31.3-q32.1"
module: 152
arm: "+"
pooled_cpm: 397.52
n_lines_expressing: 24
n_dd_up: 7
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# GPC6

*glypican 6* — 13q31.3-q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.32× (z +5.0, q 2e-04, up in 1 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.20× (z +5.0, q 2e-04, up in 6 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.573× (z -14.9, q 0e+00, down in 21 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPA1]] (+0.62, fdr 1e-05), [[PTPRD]] (+0.58, fdr 3e-05), [[PRKD1]] (+0.57, fdr 1e-05); moves opposite to [[PSD4]] (-0.48, fdr 8e-05), [[ALDH1L1]] (-0.43, fdr 1e-04), [[LASTR]] (-0.42, fdr 7e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CASC15]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +5.0 | 2e-04 | 1/21 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.0 | 2e-04 | 6/22 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +4.8 | 4e-04 | 1/22 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.1 | 0.005 | 8/20 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.008 | 0/23 | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.8 | 0.016 | 1/23 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.030 | 2/23 (BT-474, HOP62) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.034 | 5/23 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 1.18× | +3.1 | 0.11 | 3/22 (AN3 CA, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.573×** | -14.9 | 0e+00 | 21/22 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.488×** | -13.6 | 2e-39 | 18/22 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.526×** | -12.1 | 2e-31 | 21/22 (SHP-77, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.535×** | -11.8 | 6e-30 | 20/22 (SHP-77, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.542×** | -11.6 | 7e-29 | 22/22 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -10.9 | 2e-25 | 22/22 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.571×** | -10.6 | 3e-24 | 21/22 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.725×** | -8.6 | 8e-16 | 18/22 (NCI-H2347, SHP-77, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.636×** | -8.2 | 1e-14 | 16/22 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -6.4 | 9e-09 | 10/22 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.756×** | -5.3 | 7e-06 | 14/22 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.760×** | -5.2 | 1e-05 | 16/22 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -4.4 | 4e-04 | 13/22 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.789×** | -4.3 | 7e-04 | 19/22 (C32, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.757×** | -4.2 | 0.001 | 15/22 (H4, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.0 | 0.002 | 15/22 (H4, A-172, …) | rises with dose | plate-row cell shift |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **0.811×** | -3.9 | 0.002 | 2/22 (HOP62, CHP-212) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.808×** | -3.9 | 0.003 | 13/22 (A-172, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 430 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -30.1) |
| [[C32 (line)]] | wt | 4,199 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -33.2) |
| [[NCI-H1792 (line)]] | alt | 980 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0494× (z -38.2) |
| [[HepG2_C3A (line)]] | wt | 1,449 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -21.9) |
| [[A498 (line)]] | wt | 2,406 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -22.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.175× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 1,532 | 0 | 11 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0998× (z -20.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.208× (z -14.6) |
| [[A549 (line)]] | wt | 481 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.162× (z -15.2) |
| [[SNU-423 (line)]] | alt | 502 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 518 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -28.4) |
| [[SHP-77 (line)]] | alt | 1,564 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.209× (z -17.3) |
| [[SW 900 (line)]] | alt | 563 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -16.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.244× (z -13.2) |
| [[PANC-1 (line)]] | alt | 145 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -16.0) |
| [[A-172 (line)]] | wt | 438 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.379× (z -9.6) |
| [[HS-578T (line)]] | alt | 226 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 132 | 1 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.52× (z +9.5) ⚠ unreliable plate only | [[Selinexor (drug)]] 5 µM 0.502× (z -9.9) |
| [[H4 (line)]] | wt | 281 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 209 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -16.5) |
| [[AN3 CA (line)]] | alt | 326 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -11.8) |
| [[CHP-212 (line)]] | wt | 179 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.9) |
| [[A-427 (line)]] | wt | 22.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 33.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 61.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 29.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 32.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 29.7 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 40.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 40.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 27.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 27.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 414 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 84.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 496 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.0 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 62.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 38.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 33.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 93.2 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 38.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 27.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPA1]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[PTPRD]] | +0.58 | +0.45 / +0.67 | both halves | 3e-05 | STRING 581 |
| [[PRKD1]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PTPRM]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[RARB]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LRAT]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 | pathway: Metabolism of fat-soluble vitamins |
| [[NREP]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.55 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[TBX18]] | +0.54 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[NLGN1]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[EYA4]] | +0.53 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[MSC-AS1]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSD4]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[ALDH1L1]] | -0.43 | -0.36 / -0.40 | both halves | 1e-04 | pathway: Metabolism of vitamins and cofactors |
| [[LASTR]] | -0.42 | -0.41 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity raises GPC6's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TRPA1]] | C | TRPA1 activity raises GPC6's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 6.28× lower at baseline in the lines without TRPA1 | 0.029 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[CASC15]] | C | CASC15 activity raises GPC6's level | lines that do not express CASC15 (24) vs lines expressing it (26) | 5.49× lower at baseline in the lines without CASC15 | 0.049 | ⚠ within organs, on part of the lines; also absent: RAB39A, RARB, TRPA1; co-absent with the target |
| [[NRCAM]] | C | NRCAM activity raises GPC6's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 5.06× lower at baseline in the lines without NRCAM | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises GPC6's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.76× lower at baseline in the lines without GPRIN3 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC15]] | C | GPC6 activity raises CASC15's level | lines that do not express GPC6 (26) vs lines expressing it (24) | 3.26× lower at baseline in the lines without GPC6 | 0.080 | ⚠ within organs, on part of the lines; also absent: TRPA1, GALNT13, ZMAT4; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.1, 28.2); signed map (35.7, 41.2). **Vector** length 105, 34.9% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.2 | -11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.5 | -10.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -5.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.8 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | glypican 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q31.3-q32.1 — chr13:93,226,807-94,408,020 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glypicans |
| Reactome | 34 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; Defective B3GALT6 causes EDSP2 and SEMDJL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y625](https://www.uniprot.org/uniprotkb/Q9Y625) (Glypican-6):

> Cell surface proteoglycan that bears heparan sulfate. Putative cell surface coreceptor for growth factors, extracellular matrix proteins, proteases and anti-proteases (By similarity). Enhances migration and invasion of cancer cells through WNT5A signaling.

**Summary**, from NCBI Gene [10082](https://www.ncbi.nlm.nih.gov/gene/10082):

> The glypicans comprise a family of glycosylphosphatidylinositol-anchored heparan sulfate proteoglycans, and they have been implicated in the control of cell growth and cell division. The glypican encoded by this gene is a putative cell surface coreceptor for growth factors, extracellular matrix proteins, proteases and anti-proteases. Mutations in this gene are associated with omodysplasia 1. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:4454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4454) · Entrez [10082](https://www.ncbi.nlm.nih.gov/gene/10082) · UniProt [Q9Y625](https://www.uniprot.org/uniprotkb/Q9Y625) · Ensembl [ENSG00000183098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183098)

## Data

Gene col 11370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11370); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11370]; `tensor/DDL_lfc|DDL_z.npy` [11370]; `embed/gene_vectors.npy` [11370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11370 or target_col == 11370). Every well: [[GPC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
