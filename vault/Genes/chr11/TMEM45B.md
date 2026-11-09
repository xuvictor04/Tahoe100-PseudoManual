---
symbol: "TMEM45B"
type: "gene"
col: 7556
ensembl_id: "ENSG00000151715"
name: "transmembrane protein 45B"
location: "11q24.3"
module: 8
arm: "+"
pooled_cpm: 71.7
n_lines_expressing: 18
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 169
direction_downstream: 214
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TMEM45B

*transmembrane protein 45B* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +10.1, q 3e-21, up in 0 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.52× (z +6.7, q 4e-09, up in 13 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.453× (z -8.6, q 3e-15, down in 14 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPZL2]] (+0.83, fdr 7e-06), [[TMPRSS4]] (+0.83, fdr 7e-06), [[ITGB6]] (+0.82, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 169 arrows point to it, the strongest [[LINC03041]] → it (grade B ⚠); 214 go from it, the strongest it → [[ELF3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +10.1 | 3e-21 | 0/17 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +6.7 | 4e-09 | 13/16 (Panc 03.27, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +5.6 | 5e-06 | 2/15 (Panc 03.27, SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.7 | 4e-04 | 14/17 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.2 | 0.002 | 0/16 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +4.2 | 0.002 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.006 | 2/16 (KATO III, Panc 03.27) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.006 | 1/16 (SW48) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.042 | 0/18 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.4 | 0.042 | 4/16 (KATO III, SW480, …) | top dose only | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.085 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.11 | 0/16 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.453×** | -8.6 | 3e-15 | 14/16 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.596×** | -8.3 | 3e-14 | 16/16 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.527×** | -7.3 | 7e-11 | 15/16 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.600×** | -5.8 | 1e-06 | 14/16 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.628×** | -5.3 | 2e-05 | 16/16 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.615×** | -5.1 | 3e-05 | 3/16 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.646×** | -4.9 | 6e-05 | 10/16 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.454×** | -4.4 | 6e-04 | 11/16 (LS 180, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -4.2 | 0.002 | 12/16 (BT-474, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.708×** | -3.9 | 0.005 | 15/16 (LoVo, BT-474, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.618×** | -3.9 | 0.005 | 10/16 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -3.8 | 0.006 | 14/16 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | **0.734×** | -3.5 | 0.020 | 0/16 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -3.5 | 0.020 | 16/17 (LoVo, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.736×** | -3.5 | 0.020 | 0/16 | inconsistent across doses |  |
| [[Tucatinib (drug)]] 0.5 µM |  | **0.656×** | -3.4 | 0.023 | 0/16 | inconsistent across doses | noisy plate (z scaled) |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.667×** | -3.3 | 0.034 | 0/16 | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.5 µM |  | **0.671×** | -3.2 | 0.038 | 0/16 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 234 | 0 | 29 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -21.0) |
| [[LoVo (line)]] | wt | 307 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0499× (z -34.1) |
| [[NCI-H1573 (line)]] | alt | 313 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0482× (z -35.2) |
| [[CFPAC-1 (line)]] | alt | 199 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -23.3) |
| [[HepG2_C3A (line)]] | wt | 195 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.2) |
| [[HT-29 (line)]] | alt | 279 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0938× (z -28.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.194× (z -19.9) |
| [[LS 180 (line)]] | wt | 338 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -23.5) |
| [[KATO III (line)]] | alt | 386 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -21.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.256× (z -16.3) |
| [[SW480 (line)]] | alt | 75.1 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 184 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -23.9) |
| [[COLO 205 (line)]] | alt | 208 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -22.6) |
| [[SW1417 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.7) |
| [[SW48 (line)]] | wt | 44.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -11.1) |
| [[HCT15 (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.89 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.46 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.20 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPZL2]] | +0.83 | +0.81 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.83 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ITGB6]] | +0.82 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CATSPERB]] | +0.81 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.76 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM5]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SLC28A3]] | +0.75 | +0.69 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ADCY4]] | +0.74 | +0.66 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMEM125]] | +0.74 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[TMC4]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.71 | +0.64 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*169 arrows, 169 of them with an alert ⚠; grade A 0, B 19, C 150. Shown: the 12 strongest; 157 more arrows (157 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03041]] | B | LINC03041 activity lowers TMEM45B's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 10.11× higher at baseline in the lines without LINC03041 | 0.001 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[BNC2]] | B | BNC2 activity lowers TMEM45B's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 8.02× higher at baseline in the lines without BNC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[BOLA3-DT]] | B | BOLA3-DT activity lowers TMEM45B's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 10.46× higher at baseline in the lines without BOLA3-DT | 0.004 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[DCLK2]] | B | DCLK2 activity lowers TMEM45B's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 7.82× higher at baseline in the lines without DCLK2 | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[DZIP1L]] | B | DZIP1L activity lowers TMEM45B's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 17.79× higher at baseline in the lines without DZIP1L | 0.007 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises TMEM45B's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 4.05× lower at baseline in the lines without EPS8L1 | 0.029 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises TMEM45B's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 4.98× lower at baseline in the lines without SPATA6L | 0.032 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises TMEM45B's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 4.63× lower at baseline in the lines without ELF3-AS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises TMEM45B's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 3.49× lower at baseline in the lines without TJP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[MYO1D]] | B | MYO1D activity raises TMEM45B's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 3.79× lower at baseline in the lines without MYO1D | 0.045 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[RNF220]] | B | RNF220 activity lowers TMEM45B's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 3.40× higher at baseline in the lines without RNF220 | 0.050 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[TNFRSF21]] | B | TNFRSF21 activity raises TMEM45B's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 4.70× lower at baseline in the lines without TNFRSF21 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |

### Downstream of this gene

*214 arrows, 214 of them with an alert ⚠; grade A 0, B 58, C 156. Shown: the 12 strongest; 202 more arrows (202 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | TMEM45B activity raises ELF3-AS1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 4.53× lower at baseline in the lines without TMEM45B | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[GAREM1]] | B | TMEM45B activity raises GAREM1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 4.03× lower at baseline in the lines without TMEM45B | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[EPS8L1]] | B | TMEM45B activity raises EPS8L1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 4.37× lower at baseline in the lines without TMEM45B | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[TMEM184A]] | B | TMEM45B activity raises TMEM184A's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.01× lower at baseline in the lines without TMEM45B | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[ZNF703]] | B | TMEM45B activity raises ZNF703's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without TMEM45B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[ZNF25]] | B | TMEM45B activity lowers ZNF25's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.01× higher at baseline in the lines without TMEM45B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[MROH7]] | B | TMEM45B activity raises MROH7's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.53× lower at baseline in the lines without TMEM45B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[TNFRSF21]] | B | TMEM45B activity raises TNFRSF21's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 4.90× lower at baseline in the lines without TMEM45B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[USP6NL]] | B | TMEM45B activity raises USP6NL's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[ELMO3]] | B | TMEM45B activity raises ELMO3's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.66× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[MYO1D]] | B | TMEM45B activity raises MYO1D's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.65× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[KIF13B]] | B | TMEM45B activity raises KIF13B's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.55× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.2, 55.9); signed map (59.3, 7.4). **Vector** length 105, 45.8% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -0.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +4.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -5.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -3.5 |
|  | [[Encorafenib (drug)]] 5 µM |  | -2.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 45B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:129,815,848-129,860,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BC016153, FLJ40787 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B21](https://www.uniprot.org/uniprotkb/Q96B21) (Transmembrane protein 45B):

> Plays a role in innate immunity. Mechanistically, promotes alphaviruses RNA degradation by interacting with the viral polymerase nsP4 and the mRNA-capping enzyme nsP1 and thereby interfering with the interaction between viral RNA and nsP1. Essential for inflammation- and tissue injury-induced mechanical pain hypersensitivity (By similarity).

**Summary**, from NCBI Gene [120224](https://www.ncbi.nlm.nih.gov/gene/120224):

> Predicted to be involved in response to pain. Predicted to be located in trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25194) · Entrez [120224](https://www.ncbi.nlm.nih.gov/gene/120224) · UniProt [Q96B21](https://www.uniprot.org/uniprotkb/Q96B21) · Ensembl [ENSG00000151715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151715)

## Data

Gene col 7556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7556); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7556]; `tensor/DDL_lfc|DDL_z.npy` [7556]; `embed/gene_vectors.npy` [7556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7556 or target_col == 7556). Every well: [[TMEM45B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM45B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
