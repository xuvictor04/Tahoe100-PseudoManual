---
symbol: "SAMD12-AS1"
type: "gene"
col: 15986
ensembl_id: "ENSG00000281641"
name: "SAMD12 antisense RNA 1"
location: "8q24.12"
module: 8
arm: "+"
pooled_cpm: 9.8
n_lines_expressing: 27
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 81
direction_downstream: 71
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SAMD12-AS1

*SAMD12 antisense RNA 1* — 8q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.85× (z +16.1, q 0e+00, up in 15 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.642× (z -4.8, q 7e-04, down in 15 of 25 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.0383×, KATO III 0.0960×, BT-474 0.141×, Panc 03.27 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.0442×, COLO 205 0.0790×; ⚠ cell-cycle shift, explains ~41% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (KATO III 0.0446×, COLO 205 0.0583×; ⚠ cell-cycle shift, explains ~31% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0715×); [[Auranofin (drug)]] 5 µM in 1 line (KATO III 0.250×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L15]] (+0.77, fdr 7e-06), [[TMC5]] (+0.74, fdr 7e-06), [[MUC4]] (+0.74, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 81 arrows point to it, the strongest [[MMP7]] → it (grade B ⚠); 71 go from it, the strongest it → [[LGALS9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +16.1 | 0e+00 | 15/24 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.24×** | +8.8 | 6e-16 | 14/25 (LOX-IMVI, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +7.9 | 7e-13 | 5/17 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +7.3 | 5e-11 | 1/11 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +5.6 | 3e-06 | 2/12 (RPMI-7951, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.3 | 1e-05 | 6/22 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.0 | 4e-05 | 9/25 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 0.001 | 9/25 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.002 | 14/25 (HEC-1-A, AsPC-1, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 11/25 (AsPC-1, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.013 | 4/23 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.023 | 3/25 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.4 | 0.029 | 4/23 (BT-474, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.041 | 9/25 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.045 | 5/25 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.078 | 14/25 (AsPC-1, NCI-H1573, …) | two highest doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.078 | 2/25 (J82, RPMI-7951) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.078 | 4/25 (BT-474, A-172, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15986.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.0383×, KATO III 0.0960×, BT-474 0.141×, Panc 03.27 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.0442×, COLO 205 0.0790×; ⚠ cell-cycle shift, explains ~41% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (KATO III 0.0446×, COLO 205 0.0583×; ⚠ cell-cycle shift, explains ~31% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0715×); [[Auranofin (drug)]] 5 µM in 1 line (KATO III 0.250×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.642×** | -4.8 | 7e-04 | 15/25 (KATO III, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.707×** | -3.8 | 0.044 | 17/25 (COLO 205, KATO III, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.724×** | -3.5 | 0.082 | 14/25 (KATO III, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.754× | -3.1 | 0.29 | 15/25 (KATO III, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 76.0 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0960× (z -21.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.250× (z -8.9) |
| [[COLO 205 (line)]] | alt | 64.4 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0383× (z -26.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 38.8 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 33.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 22.7 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0942× (z -14.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 38.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 6.10 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +9.3) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0618× (z -10.4) ⚠ toxic |
| [[RKO (line)]] | wt | 7.93 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0895× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 5.47 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0631× (z -9.2) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H2347 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 10.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0715× (z -10.2) |
| [[A-172 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L15]] | +0.77 | +0.76 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TMC5]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MUC4]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SAMD12]] | +0.74 | +0.75 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[STS]] | +0.74 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[MUC20]] | +0.71 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[MMP7]] | +0.71 | +0.65 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PLCH1]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SPATA6L]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PDZK1IP1]] | +0.69 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[PRR15]] | +0.68 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[STEAP4]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MGAM2]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 19, C 62. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP7]] | B | MMP7 activity raises SAMD12-AS1's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.78× lower at baseline in the lines without MMP7 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[VNN1]] | B | VNN1 activity raises SAMD12-AS1's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without VNN1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[SPATA6L]] | B | SPATA6L activity raises SAMD12-AS1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.82× lower at baseline in the lines without SPATA6L | 0.016 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SAMD12-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC40A1]] | B | SLC40A1 activity raises SAMD12-AS1's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 2.18× lower at baseline in the lines without SLC40A1 | 0.025 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[RNF220]] | B | RNF220 activity lowers SAMD12-AS1's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.82× higher at baseline in the lines without RNF220 | 0.033 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[C3orf18]] | B | C3orf18 activity lowers SAMD12-AS1's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 3.54× higher at baseline in the lines without C3orf18 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[CCSER1]] | B | CCSER1 activity raises SAMD12-AS1's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without CCSER1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[HDAC6]] | B | HDAC6 activity raises SAMD12-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CCR3]] | B | CCR3 activity raises SAMD12-AS1's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 2.03× lower at baseline in the lines without CCR3 | 0.046 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[IKZF2]] | B | IKZF2 activity raises SAMD12-AS1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without IKZF2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[PROM2]] | B | PROM2 activity raises SAMD12-AS1's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 2.48× lower at baseline in the lines without PROM2 | 0.050 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |

### Downstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 23, C 48. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS9]] | B | SAMD12-AS1 activity raises LGALS9's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without SAMD12-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[RAMP1]] | B | SAMD12-AS1 activity raises RAMP1's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without SAMD12-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[RBM47]] | B | SAMD12-AS1 activity raises RBM47's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 3.41× lower at baseline in the lines without SAMD12-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[PROM2]] | B | SAMD12-AS1 activity raises PROM2's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.15× lower at baseline in the lines without SAMD12-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[MUC20]] | B | SAMD12-AS1 activity raises MUC20's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.72× lower at baseline in the lines without SAMD12-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[SLC37A1]] | B | SAMD12-AS1 activity raises SLC37A1's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.20× lower at baseline in the lines without SAMD12-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[CASP10]] | B | SAMD12-AS1 activity raises CASP10's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without SAMD12-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[VNN1]] | B | SAMD12-AS1 activity raises VNN1's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 1.75× lower at baseline in the lines without SAMD12-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[CCSER1]] | B | SAMD12-AS1 activity raises CCSER1's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.59× lower at baseline in the lines without SAMD12-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[DNAAF9]] | B | SAMD12-AS1 activity lowers DNAAF9's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 3.21× higher at baseline in the lines without SAMD12-AS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[MMP7]] | B | SAMD12-AS1 activity raises MMP7's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without SAMD12-AS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[STS]] | B | SAMD12-AS1 activity raises STS's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without SAMD12-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, 53.8); signed map (59.0, 1.0). **Vector** length 83.8, 25.1% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.57 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +16.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.0 | +3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.8 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.7 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.7 | -4.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | SAMD12 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.12 — chr8:118,620,498-118,906,155 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C8orf26, NCRNA00252 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30937) · Entrez [552860](https://www.ncbi.nlm.nih.gov/gene/552860) · Ensembl [ENSG00000281641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000281641)

## Data

Gene col 15986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15986); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15986]; `tensor/DDL_lfc|DDL_z.npy` [15986]; `embed/gene_vectors.npy` [15986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15986 or target_col == 15986). Every well: [[SAMD12-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD12-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
