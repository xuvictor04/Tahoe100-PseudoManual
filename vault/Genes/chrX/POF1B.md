---
symbol: "POF1B"
type: "gene"
col: 4529
ensembl_id: "ENSG00000124429"
name: "POF1B actin binding protein"
location: "Xq21.1"
module: 8
arm: "+"
pooled_cpm: 49.05
n_lines_expressing: 16
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 121
direction_downstream: 126
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# POF1B

*POF1B actin binding protein* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.84× (z +12.9, q 2e-35, up in 4 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.38× (z +4.8, q 2e-04, up in 9 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.608× (z -6.1, q 5e-07, down in 11 of 14 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.625× (z -5.8, q 2e-06, down in 13 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOX3]] (+0.84, fdr 7e-06), [[MUC13]] (+0.81, fdr 7e-06), [[ARHGEF38]] (+0.80, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 121 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 126 go from it, the strongest it → [[TOB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.84×** | +12.9 | 2e-35 | 4/14 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +11.4 | 1e-27 | 4/12 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +7.6 | 6e-12 | 2/13 (NCI-H1573, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 2e-04 | 9/14 (AsPC-1, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.011 | 11/14 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.011 | 11/14 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.023 | 0/14 | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.025 | 8/14 (AsPC-1, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.038 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.041 | 4/14 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.041 | 0/14 | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.041 | 7/14 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.068 | 1/14 (AsPC-1) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.089 | 0/14 | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.091 | 8/14 (AsPC-1, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4529.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.608×** | -6.1 | 5e-07 | 11/14 (SW480, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -5.8 | 2e-06 | 13/14 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -5.5 | 8e-06 | 10/14 (KATO III, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.645×** | -5.4 | 9e-06 | 11/14 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.668×** | -5.0 | 8e-05 | 11/14 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.461×** | -4.6 | 3e-04 | 12/14 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -4.5 | 6e-04 | 9/14 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.697×** | -4.5 | 6e-04 | 12/14 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.711×** | -4.2 | 0.002 | 0/14 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.737×** | -3.8 | 0.010 | 13/14 (SW480, AsPC-1, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.536×** | -3.7 | 0.010 | 12/15 (LS 180, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.746×** | -3.6 | 0.015 | 6/14 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.4 | 0.032 | 0/15 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -3.2 | 0.049 | 13/14 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -3.1 | 0.065 | 10/14 (HT-29, LoVo, …) | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | **0.780×** | -3.0 | 0.082 | 0/14 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 0.5 µM |  | **0.691×** | -3.0 | 0.097 | 0/14 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 215 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.234× (z -9.4) |
| [[KATO III (line)]] | alt | 370 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -25.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -11.6) |
| [[LoVo (line)]] | wt | 185 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -17.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -11.1) |
| [[SW480 (line)]] | alt | 95.1 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0793× (z -22.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.257× (z -12.1) |
| [[HT-29 (line)]] | alt | 393 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -17.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.218× (z -11.4) |
| [[LS 180 (line)]] | wt | 325 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0970× (z -19.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.107× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 87.2 | 2 | 4 (3 ⚠) | [[Trametinib (drug)]] 0.5 µM 3.13× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 22.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 46.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -17.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 38.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.49 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.06 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX3]] | +0.84 | +0.82 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.81 | +0.80 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ARHGEF38]] | +0.80 | +0.74 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PRR15]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TRIM31]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PIP5K1B]] | +0.77 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[BCL2L15]] | +0.77 | +0.79 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.75 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[RASSF6]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*121 arrows, 121 of them with an alert ⚠; grade A 0, B 3, C 118. Shown: the 12 strongest; 109 more arrows (109 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers POF1B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[MTUS1]] | B | MTUS1 activity raises POF1B's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.96× lower at baseline in the lines without MTUS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises POF1B's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.80× lower at baseline in the lines without SLC44A3-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[GCNT3]] | C | GCNT3 activity raises POF1B's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 10.95× lower at baseline in the lines without GCNT3 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises POF1B's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 10.49× lower at baseline in the lines without TMPRSS2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises POF1B's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 6.99× lower at baseline in the lines without TOX3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises POF1B's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 6.35× lower at baseline in the lines without HNF1A-AS1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises POF1B's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 14.12× lower at baseline in the lines without TRIM31 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises POF1B's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 14.68× lower at baseline in the lines without MUC13 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises POF1B's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 16.40× lower at baseline in the lines without CLRN3 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises POF1B's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 9.01× lower at baseline in the lines without GPX2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises POF1B's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 11.09× lower at baseline in the lines without LINC01559 | 0.001 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*126 arrows, 126 of them with an alert ⚠; grade A 0, B 25, C 101. Shown: the 12 strongest; 114 more arrows (114 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOB1]] | B | POF1B activity raises TOB1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without POF1B | 0.002 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[ELF3-AS1]] | B | POF1B activity raises ELF3-AS1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 3.47× lower at baseline in the lines without POF1B | 0.004 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[RSPH1]] | B | POF1B activity raises RSPH1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without POF1B | 0.009 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[PAQR7]] | B | POF1B activity lowers PAQR7's level | lines that do not express POF1B (34) vs lines expressing it (16) | 1.79× higher at baseline in the lines without POF1B | 0.011 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[SLC37A1]] | B | POF1B activity raises SLC37A1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without POF1B | 0.015 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[PLCH1]] | B | POF1B activity raises PLCH1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 3.49× lower at baseline in the lines without POF1B | 0.020 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[STS]] | B | POF1B activity raises STS's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without POF1B | 0.031 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[BCL2L15]] | B | POF1B activity raises BCL2L15's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.86× lower at baseline in the lines without POF1B | 0.033 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[PBX1]] | B | POF1B activity raises PBX1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.21× lower at baseline in the lines without POF1B | 0.037 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[GAREM1]] | B | POF1B activity raises GAREM1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.89× lower at baseline in the lines without POF1B | 0.042 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[TNFRSF14-AS1]] | B | POF1B activity raises TNFRSF14-AS1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 2.15× lower at baseline in the lines without POF1B | 0.045 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |
| [[SSH1]] | B | POF1B activity lowers SSH1's level | lines that do not express POF1B (34) vs lines expressing it (16) | 1.91× higher at baseline in the lines without POF1B | 0.050 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 52.4); signed map (60.9, 4.4). **Vector** length 86.2, 42.0% of its response variance represented; |z| ≥ 3 in 498 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.52 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -1.1 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -4.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | POF1B actin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:85,277,396-85,379,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POF, FLJ22792 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVV4](https://www.uniprot.org/uniprotkb/Q8WVV4) (Protein POF1B):

> Plays a key role in the organization of epithelial monolayers by regulating the actin cytoskeleton. May be involved in ovary development.

**Summary**, from NCBI Gene [79983](https://www.ncbi.nlm.nih.gov/gene/79983):

> Premature ovarian failure (POF) is characterized by primary or secondary amenorrhea in women less than 40 years old. Two POF susceptibility regions called "POF1" and "POF2" have been identified by breakpoint mapping of X-autosome translocations. POF1 extends from Xq21-qter while POF2 extends from Xq13.3 to Xq21.1. This gene, POF1B, resides in the POF2 region. This gene is expressed at trace levels in mouse prenatal ovary and is barely detectable or absent from adult ovary, in human and in the …

**Accessions** — [HGNC:13711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13711) · Entrez [79983](https://www.ncbi.nlm.nih.gov/gene/79983) · UniProt [Q8WVV4](https://www.uniprot.org/uniprotkb/Q8WVV4) · Ensembl [ENSG00000124429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124429)

## Data

Gene col 4529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4529); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4529]; `tensor/DDL_lfc|DDL_z.npy` [4529]; `embed/gene_vectors.npy` [4529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4529 or target_col == 4529). Every well: [[POF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
