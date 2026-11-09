---
symbol: "PROX1"
type: "gene"
col: 3944
ensembl_id: "ENSG00000117707"
name: "prospero homeobox 1"
location: "1q32.3"
module: 27
arm: "+"
pooled_cpm: 35.98
n_lines_expressing: 20
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 39
direction_downstream: 23
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PROX1

*prospero homeobox 1* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.16× (z +13.5, q 6e-39, up in 12 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.534× (z -7.8, q 5e-12, down in 12 of 18 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.740× (z -5.3, q 4e-05, down in 11 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PROX1-AS1]] (+0.81, fdr 7e-06, ⚠ same locus), [[ST18]] (+0.79, fdr 7e-06), [[FGD5]] (+0.73, fdr 7e-06), [[GJB1]] (+0.72, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[LINC01091]] → it (grade B ⚠); 23 go from it, the strongest it → [[PELI2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +13.5 | 6e-39 | 12/18 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.89×** | +11.1 | 2e-26 | 8/18 (Hs 766T, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +10.2 | 4e-22 | 5/18 (LoVo, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +9.0 | 3e-17 | 9/18 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +8.1 | 7e-14 | 0/16 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.0 | 2e-10 | 3/13 (AsPC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +7.0 | 3e-10 | 1/14 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +6.1 | 1e-07 | 5/18 (RPMI-7951, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.7 | 6e-07 | 6/18 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +5.5 | 3e-06 | 14/18 (LoVo, SW 900, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +5.0 | 2e-05 | 1/18 (RPMI-7951) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 4e-05 | 3/18 (RKO, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 10/18 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.004 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.009 | 1/18 (H4) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.030 | 2/18 (H4, RKO) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.534×** | -7.8 | 5e-12 | 12/18 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.740×** | -5.3 | 4e-05 | 11/18 (C32, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.697×** | -4.5 | 0.002 | 11/18 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.707×** | -4.3 | 0.003 | 7/18 (C32, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.727×** | -3.9 | 0.009 | 10/18 (C32, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.728×** | -3.9 | 0.009 | 10/18 (SW480, COLO 205, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.018 | 3/18 (Hs 766T, NCI-H1573, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.046 | 4/18 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.046 | 8/18 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.046 | 13/18 (SW480, COLO 205, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.764×** | -3.3 | 0.046 | 8/18 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.046 | 10/18 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.621×** | -3.1 | 0.090 | 8/18 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | 0.627× | -3.0 | 0.10 | 1/18 (C32) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 362 | 0 | 18 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -20.4) |
| [[C32 (line)]] | wt | 41.4 | 0 | 7 (2 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.151× (z -10.4) |
| [[LoVo (line)]] | wt | 21.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +19.8) | — |
| [[COLO 205 (line)]] | alt | 164 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0617× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -13.1) |
| [[SHP-77 (line)]] | alt | 92.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -11.6) |
| [[SW 900 (line)]] | alt | 62.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +14.1) | — |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.163× (z -14.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 61.8 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.191× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 22.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0780× (z -9.2) |
| [[Hs 766T (line)]] | wt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +10.4) | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.38 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.99 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.59 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROX1-AS1]] | +0.81 | +0.76 / +0.79 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ST18]] | +0.79 | +0.79 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[FGD5]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[LINC02254]] | +0.71 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[IGFL4]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NKD1]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[VWA2]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[RIMBP2]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[KCNH8]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[LINC02058]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[SMOC2]] | +0.64 | +0.59 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 3, C 36. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01091]] | B | LINC01091 activity raises PROX1's level | lines that do not express LINC01091 (16) vs lines expressing it (34) | 3.01× lower at baseline in the lines without LINC01091 | 0.021 | ⚠ within organs, on part of the lines; also absent: TOX3, BCAS1; maybe low, not absent |
| [[HS3ST5]] | B | HS3ST5 activity raises PROX1's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without HS3ST5 | 0.048 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[PELI2]] | B | PELI2 activity raises PROX1's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.84× lower at baseline in the lines without PELI2 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[PROX1-AS1]] | C | PROX1-AS1 activity raises PROX1's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 5.58× lower at baseline in the lines without PROX1-AS1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises PROX1's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 3.56× lower at baseline in the lines without TSHZ2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises PROX1's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 5.84× lower at baseline in the lines without TFF3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises PROX1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 4.35× lower at baseline in the lines without TOX3 | 0.001 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[INPP5D]] | C | INPP5D activity raises PROX1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 5.30× lower at baseline in the lines without INPP5D | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[ST18]] | C | ST18 activity raises PROX1's level | lines that do not express ST18 (39) vs lines expressing it (11) | 5.32× lower at baseline in the lines without ST18 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000213981, CALCA, KCNB2; maybe low, not absent; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises PROX1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 6.41× lower at baseline in the lines without CLRN3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[LOXL4]] | C | LOXL4 activity raises PROX1's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without LOXL4 | 0.006 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises PROX1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 5.83× lower at baseline in the lines without GJB1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 10, C 13. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PELI2]] | B | PROX1 activity raises PELI2's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 3.96× lower at baseline in the lines without PROX1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[RGL1]] | B | PROX1 activity raises RGL1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 2.28× lower at baseline in the lines without PROX1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[LINC02466]] | B | PROX1 activity raises LINC02466's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without PROX1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[PLCB1]] | B | PROX1 activity raises PLCB1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without PROX1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[FHDC1]] | B | PROX1 activity raises FHDC1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without PROX1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[FKBP9P1]] | B | PROX1 activity raises FKBP9P1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without PROX1 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[BCAR3-AS1]] | B | PROX1 activity raises BCAR3-AS1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 1.60× lower at baseline in the lines without PROX1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[ZNF703]] | B | PROX1 activity raises ZNF703's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without PROX1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| cells under [[Pimitespib (drug)]] 5 µM | B | PROX1 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express PROX1 (30) vs lines expressing it (18) | the lines without PROX1: 1.31× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[NDUFA4L2]] | B | PROX1 activity raises NDUFA4L2's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without PROX1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[PROX1-AS1]] | C | PROX1 activity raises PROX1-AS1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without PROX1 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964; co-absent with the target |
| [[CHN2]] | C | PROX1 activity raises CHN2's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 3.99× lower at baseline in the lines without PROX1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.0, 43.9); signed map (63.3, 15.2). **Vector** length 72.1, 23.9% of its response variance represented; |z| ≥ 3 in 497 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +13.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -7.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | prospero homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:213,983,181-214,041,510 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PROS class homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92786](https://www.uniprot.org/uniprotkb/Q92786) (Prospero homeobox protein 1):

> Transcription factor involved in developmental processes such as cell fate determination, gene transcriptional regulation and progenitor cell regulation in a number of organs. Plays a critical role in embryonic development and functions as a key regulatory protein in neurogenesis and the development of the heart, eye lens, liver, pancreas and the lymphatic system. Involved in the regulation of the circadian rhythm. Represses: transcription of the retinoid-related orphan receptor RORG, …

**Summary**, from NCBI Gene [5629](https://www.ncbi.nlm.nih.gov/gene/5629):

> The protein encoded by this gene is a member of the homeobox transcription factor family. Members of this family contain a homeobox domain that consists of a 60-amino acid helix-turn-helix structure that binds DNA and RNA. The protein encoded by this gene is conserved across vertebrates and may play an essential role during development. Altered levels of this protein have been reported in cancers of different organs, such as colon, brain, blood, breast, pancreas, liver and esophagus. …

**Accessions** — [HGNC:9459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9459) · Entrez [5629](https://www.ncbi.nlm.nih.gov/gene/5629) · UniProt [Q92786](https://www.uniprot.org/uniprotkb/Q92786) · Ensembl [ENSG00000117707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117707)

## Data

Gene col 3944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3944); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3944]; `tensor/DDL_lfc|DDL_z.npy` [3944]; `embed/gene_vectors.npy` [3944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3944 or target_col == 3944). Every well: [[PROX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
