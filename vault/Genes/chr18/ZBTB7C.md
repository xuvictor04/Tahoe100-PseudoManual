---
symbol: "ZBTB7C"
type: "gene"
col: 11578
ensembl_id: "ENSG00000184828"
name: "zinc finger and BTB domain containing 7C"
location: "18q21.1"
module: 55
arm: "+"
pooled_cpm: 26.16
n_lines_expressing: 25
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 23
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 24
direction_downstream: 15
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# ZBTB7C

*zinc finger and BTB domain containing 7C* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.62× (z +28.0, q 0e+00, up in 9 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.705× (z -5.2, q 1e-04, down in 17 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPX2]] (+0.73, fdr 7e-06), [[BMP4]] (+0.72, fdr 7e-06), [[LINC01819]] (+0.71, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 15 go from it, the strongest it → [[JPH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.62×** | +28.0 | 0e+00 | 9/23 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.68×** | +20.0 | 0e+00 | 10/23 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +16.3 | 0e+00 | 14/23 (HS-578T, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.56×** | +14.5 | 3e-45 | 8/23 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +12.4 | 2e-33 | 11/23 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.05×** | +11.0 | 3e-26 | 12/23 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.0 | 1e-13 | 7/21 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.7 | 2e-09 | 1/21 (NCI-H1573) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +6.6 | 3e-09 | 9/22 (NCI-H460, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.3 | 2e-08 | 6/23 (A498, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 5e-08 | 7/23 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.7 | 7e-07 | 4/22 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 9e-05 | 5/23 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 5e-04 | 12/22 (H4, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.3 | 6e-04 | 4/22 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Arbutin (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.005 | 4/21 (SW1417, RPMI-7951, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.705×** | -5.2 | 1e-04 | 17/22 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.738×** | -4.7 | 6e-04 | 13/22 (COLO 205, LS 180, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.739×** | -4.7 | 6e-04 | 10/22 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.631×** | -3.7 | 0.029 | 14/23 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.041 | 6/22 (A498, NCI-H460, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.792×** | -3.5 | 0.049 | 4/23 (LS 180, HT-29, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.857× | -3.4 | 0.052 | 13/23 (COLO 205, HT-29, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.804×** | -3.4 | 0.052 | 15/22 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.086 | 5/22 (A549, LoVo, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.086 | 11/22 (HT-29, LoVo, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.805×** | -3.1 | 0.099 | 1/22 (AN3 CA) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.821× | -3.1 | 0.11 | 11/23 (LoVo, COLO 205, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 176 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -19.9) |
| [[A-172 (line)]] | wt | 137 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0677× (z -25.0) |
| [[LoVo (line)]] | wt | 78.3 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0528× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.162× (z -13.0) |
| [[COLO 205 (line)]] | alt | 164 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0662× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -14.1) |
| [[LS 180 (line)]] | wt | 43.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -23.5) |
| [[SW480 (line)]] | alt | 67.2 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.352× (z -9.4) |
| [[HT-29 (line)]] | alt | 51.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.1) |
| [[A498 (line)]] | wt | 18.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +12.3) | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.3) |
| [[A549 (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.6) |
| [[BT-474 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 7.04 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.50× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 12.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.02× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 60.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.2) |
| [[A-427 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.52 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPX2]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[BMP4]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[KCNH8]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[EDAR]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[KLK6]] | +0.65 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[CFTR]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[HNF4A]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SKAP1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CLRN3]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 5, C 19. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZBTB7C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CREB3L1]] | B | CREB3L1 activity raises ZBTB7C's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.91× lower at baseline in the lines without CREB3L1 | 0.058 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[PRR15]] | B | PRR15 activity raises ZBTB7C's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without PRR15 | 0.061 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[TFF1]] | B | TFF1 activity raises ZBTB7C's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 1.88× lower at baseline in the lines without TFF1 | 0.065 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[ANO1]] | B | ANO1 activity raises ZBTB7C's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.14× lower at baseline in the lines without ANO1 | 0.091 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[INPP5D]] | C | INPP5D activity raises ZBTB7C's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without INPP5D | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[LINC00589]] | C | LINC00589 activity raises ZBTB7C's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 3.19× lower at baseline in the lines without LINC00589 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8; co-absent with the target |
| [[SPNS2]] | C | SPNS2 activity raises ZBTB7C's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 4.13× lower at baseline in the lines without SPNS2 | 0.003 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises ZBTB7C's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.55× lower at baseline in the lines without CEACAM5 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises ZBTB7C's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.60× lower at baseline in the lines without TMEM45B | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[PROX1-AS1]] | C | PROX1-AS1 activity raises ZBTB7C's level | lines that do not express PROX1-AS1 (29) vs lines expressing it (21) | 3.05× lower at baseline in the lines without PROX1-AS1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST18, AXIN2, PROX1; co-absent with the target |
| [[HPGD]] | C | HPGD activity raises ZBTB7C's level | lines that do not express HPGD (30) vs lines expressing it (20) | 3.41× lower at baseline in the lines without HPGD | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 3, C 12. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH1]] | B | ZBTB7C activity raises JPH1's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 2.69× lower at baseline in the lines without ZBTB7C | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A |
| [[IL20RA]] | B | ZBTB7C activity raises IL20RA's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 2.33× lower at baseline in the lines without ZBTB7C | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A |
| [[KLK10]] | B | ZBTB7C activity raises KLK10's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 1.74× lower at baseline in the lines without ZBTB7C | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A |
| [[XYLT1]] | C | ZBTB7C activity raises XYLT1's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 3.91× lower at baseline in the lines without ZBTB7C | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[SPNS2]] | C | ZBTB7C activity raises SPNS2's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 2.82× lower at baseline in the lines without ZBTB7C | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[SULF2]] | C | ZBTB7C activity raises SULF2's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without ZBTB7C | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[CAPN8]] | C | ZBTB7C activity raises CAPN8's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 3.30× lower at baseline in the lines without ZBTB7C | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[ALDH3A1]] | C | ZBTB7C activity raises ALDH3A1's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without ZBTB7C | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[HPGD]] | C | ZBTB7C activity raises HPGD's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without ZBTB7C | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[CEACAM5]] | C | ZBTB7C activity raises CEACAM5's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 3.01× lower at baseline in the lines without ZBTB7C | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[GPX2]] | C | ZBTB7C activity raises GPX2's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without ZBTB7C | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[PROX1-AS1]] | C | ZBTB7C activity raises PROX1-AS1's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 2.18× lower at baseline in the lines without ZBTB7C | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.741). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 47.4); signed map (63.9, 11.2). **Vector** length 92.9, 29.3% of its response variance represented; |z| ≥ 3 in 769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +28.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.4 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | +6.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +4.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 7C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:48,026,672-48,410,752 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF857C; previously ZBTB36 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A1YPR0](https://www.uniprot.org/uniprotkb/A1YPR0) (Zinc finger and BTB domain-containing protein 7C):

> May be a tumor suppressor gene.

**Summary**, from NCBI Gene [201501](https://www.ncbi.nlm.nih.gov/gene/201501):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in negative regulation of cell population proliferation. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31700) · Entrez [201501](https://www.ncbi.nlm.nih.gov/gene/201501) · UniProt [A1YPR0](https://www.uniprot.org/uniprotkb/A1YPR0) · Ensembl [ENSG00000184828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184828)

## Data

Gene col 11578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11578); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11578]; `tensor/DDL_lfc|DDL_z.npy` [11578]; `embed/gene_vectors.npy` [11578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11578 or target_col == 11578). Every well: [[ZBTB7C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB7C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
