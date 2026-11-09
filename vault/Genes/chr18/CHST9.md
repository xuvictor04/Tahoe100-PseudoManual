---
symbol: "CHST9"
type: "gene"
col: 7767
ensembl_id: "ENSG00000154080"
name: "carbohydrate sulfotransferase 9"
location: "18q11.2"
module: 27
arm: "+"
pooled_cpm: 2.98
n_lines_expressing: 32
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 5
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CHST9

*carbohydrate sulfotransferase 9* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.30× (z +13.1, q 2e-36, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.79× (z +13.0, q 4e-36, up in 2 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.643× (z -3.7, q 0.081, down in 3 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.105×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.115×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.127×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.249×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN14]] (+0.57, fdr 2e-05), [[POU3F3]] (+0.52, fdr 1e-05), [[CCDC152]] (+0.51, fdr 2e-04); moves opposite to [[VPS39]] (-0.46, fdr 1e-04), [[MLYCD]] (-0.41, fdr 6e-04), [[VPS33A]] (-0.41, fdr 8e-04, ⚠ not reproduced), [[POLDIP2]] (-0.40, fdr 4e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[RHEX]] → it (grade B ⚠); 5 go from it, the strongest it → [[NME9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.30×** | +13.1 | 2e-36 | 4/9 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +13.0 | 4e-36 | 2/13 (SW 900, BT-474) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.83×** | +11.6 | 1e-28 | 3/4 (HepG2/C3A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.45×** | +11.3 | 1e-27 | 18/22 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.89×** | +8.8 | 2e-16 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.23×** | +7.2 | 6e-11 | 11/19 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +5.8 | 4e-07 | 2/15 (BT-474, A549) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.2 | 0.002 | 2/10 (A498, BT-474) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.002 | 9/25 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.33×** | +4.0 | 0.004 | 0/5 | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.9 | 0.004 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.004 | 5/15 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.80×** | +3.8 | 0.007 | 1/8 (HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.014 | 8/23 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.014 | 2/19 (BT-474, NCI-H1792) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.017 | 1/22 (NCI-H1792) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.030 | 1/11 (SNU-423) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.032 | 1/14 (HOP62) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.044 | 0/12 | top dose only | cell-cycle shift (explains ~15% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.41×** | +3.0 | 0.062 | 3/10 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7767.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.105×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.115×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HEC-1-A 0.127×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.249×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.643×** | -3.7 | 0.081 | 3/24 (COLO 205, J82, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.648×** | -3.6 | 0.081 | 4/15 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.5 µM |  | 0.690× | -3.4 | 0.14 | 2/22 (BT-474, A549) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.710× | -3.1 | 0.27 | 8/19 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 35.4 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -22.0) |
| [[CFPAC-1 (line)]] | alt | 10.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.52× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.50 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.59× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 7.14 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0827× (z -9.3) |
| [[A-172 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.750 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.935 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.768 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.939 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.625 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.659 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.749 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.786 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.807 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.752 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.639 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN14]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[POU3F3]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CCDC152]] | +0.51 | +0.29 / +0.39 | both halves | 2e-04 |  |
| [[PANTR1]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[RHEX]] | +0.51 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[LINC02999]] | +0.50 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[NCMAP]] | +0.49 | +0.27 / +0.46 | both halves | 3e-04 |  |
| [[B3GALT5]] | +0.49 | +0.39 / +0.44 | both halves | 5e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[SPTLC3]] | +0.48 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[STAC]] | +0.48 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[LINGO2]] | +0.48 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ZBED2]] | +0.47 | +0.35 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS39]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[MLYCD]] | -0.41 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[VPS33A]] | -0.41 | -0.20 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[POLDIP2]] | -0.40 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[DVL3]] | -0.39 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.39 | -0.32 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHEX]] | B | RHEX activity raises CHST9's level | lines that do not express RHEX (43) vs lines expressing it (7) | 3.19× lower at baseline in the lines without RHEX | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB |
| [[ENPP5]] | B | ENPP5 activity raises CHST9's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 1.31× lower at baseline in the lines without ENPP5 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[BSPRY]] | B | BSPRY activity raises CHST9's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 1.33× lower at baseline in the lines without BSPRY | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[GOLT1A]] | B | GOLT1A activity raises CHST9's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.56× lower at baseline in the lines without GOLT1A | 0.060 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[NCMAP]] | B | NCMAP activity raises CHST9's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.32× lower at baseline in the lines without NCMAP | 0.098 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[TIMD4]] | B | TIMD4 activity raises CHST9's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 2.31× lower at baseline in the lines without TIMD4 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NME9]] | B | CHST9 activity raises NME9's level | lines that do not express CHST9 (18) vs lines expressing it (32) | 1.19× lower at baseline in the lines without CHST9 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent |
| [[CCDC152]] | B | CHST9 activity raises CCDC152's level | lines that do not express CHST9 (18) vs lines expressing it (32) | 1.62× lower at baseline in the lines without CHST9 | 0.041 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent |
| [[CAPN14]] | B | CHST9 activity raises CAPN14's level | lines that do not express CHST9 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without CHST9 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent |
| [[VAV1]] | B | CHST9 activity raises VAV1's level | lines that do not express CHST9 (18) vs lines expressing it (32) | 1.62× lower at baseline in the lines without CHST9 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent |
| [[TMEM51-AS1]] | B | CHST9 activity strengthens TMEM51-AS1's drug response | lines that do not express CHST9 (12) vs lines expressing it (23) | the lines without CHST9 respond 0.90× as strongly (z diff +0.92); strongest at Homoharringtonine 0.5 µM: 0.41x vs 0.20x (z diff +3.6) | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.148). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.0, 41.8); signed map (50.7, 36.3). **Vector** length 37.6, 6.61% of its response variance represented; |z| ≥ 3 in 591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.6 | +2.5 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +0.6 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.6 | +1.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:26,906,481-27,185,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GALNAC4ST-2, GALNAC-4-ST2 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L1S5](https://www.uniprot.org/uniprotkb/Q7L1S5) (Carbohydrate sulfotransferase 9):

> Catalyzes the transfer of sulfate from 3'-phosphoadenylyl sulfate (PAPS) to position 4 of non-reducing N-acetylgalactosamine (GalNAc) residues in both N-glycans and O-glycans. Transfers sulfate to the C-4 hydroxyl of terminal beta-1,4-linked GalNAc in the sequence GalNAc-beta-1,4GlcNAcbeta-R found on N-linked oligosaccharides and to the nonterminal beta-1,4-linked GalNAc in chondroitin and dermatan. Required for biosynthesis of glycoprotein hormones lutropin and thyrotropin, by mediating …

**Summary**, from NCBI Gene [83539](https://www.ncbi.nlm.nih.gov/gene/83539):

> The protein encoded by this gene belongs to the sulfotransferase 2 family. It is localized to the golgi membrane, and catalyzes the transfer of sulfate to position 4 of non-reducing N-acetylgalactosamine (GalNAc) residues in both N-glycans and O-glycans. Sulfate groups on carbohydrates confer highly specific functions to glycoproteins, glycolipids, and proteoglycans, and are critical for cell-cell interaction, signal transduction, and embryonic development. Alternatively spliced transcript …

**Accessions** — [HGNC:19898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19898) · Entrez [83539](https://www.ncbi.nlm.nih.gov/gene/83539) · UniProt [Q7L1S5](https://www.uniprot.org/uniprotkb/Q7L1S5) · Ensembl [ENSG00000154080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154080)

## Data

Gene col 7767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7767); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7767]; `tensor/DDL_lfc|DDL_z.npy` [7767]; `embed/gene_vectors.npy` [7767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7767 or target_col == 7767). Every well: [[CHST9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
