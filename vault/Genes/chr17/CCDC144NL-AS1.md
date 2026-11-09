---
symbol: "CCDC144NL-AS1"
type: "gene"
col: 13887
ensembl_id: "ENSG00000233098"
name: "CCDC144NL antisense RNA 1"
location: "17p11.2"
module: 177
arm: "+"
pooled_cpm: 54.46
n_lines_expressing: 17
n_dd_up: 25
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 19
direction_downstream: 36
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# CCDC144NL-AS1

*CCDC144NL antisense RNA 1* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.98× (z +23.0, q 0e+00, up in 11 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.867× (z -7.5, q 4e-11, down in 1 of 17 measured lines) ⚠ position not correctable. The strongest without an alert is [[Larotrectinib (drug)]] 5 µM: 0.826× (z -4.0, q 0.017, down in 10 of 15 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBBP4-1]] (+0.70, fdr 7e-06), [[LINC02506]] (+0.68, fdr 3e-05), [[LINC01518]] (+0.67, fdr 4e-05).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[PHF2P2]] → it (grade C ⚠); 36 go from it, the strongest it → [[SYP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.98×** | +23.0 | 0e+00 | 11/15 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +13.2 | 3e-37 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.33×** | +12.2 | 9e-32 | 6/15 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +11.9 | 1e-30 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +11.1 | 1e-26 | 8/15 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +8.8 | 2e-16 | 6/14 (NCI-H1573, SNU-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +8.3 | 1e-14 | 1/15 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +8.0 | 1e-13 | 4/15 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +7.8 | 3e-13 | 1/14 (SK-MEL-2) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +7.5 | 4e-12 | 12/15 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +6.8 | 7e-10 | 11/15 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.3 | 1e-08 | 10/15 (SK-MEL-2, C-33 A, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +5.2 | 9e-06 | 0/14 | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +5.0 | 3e-05 | 7/14 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.38×** | +4.8 | 5e-05 | 0/14 | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.8 | 5e-05 | 1/17 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +4.7 | 8e-05 | 9/14 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 3e-04 | 6/15 (SNU-1, H4, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 7e-04 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.006 | 6/14 (H4, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.867× | -7.5 | 4e-11 | 1/17 (SK-MEL-2) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.826×** | -4.0 | 0.017 | 10/15 (HepG2/C3A, H4, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -3.8 | 0.031 | 5/14 (H4, SNU-423, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.773×** | -3.5 | 0.041 | 0/14 | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **0.788×** | -3.5 | 0.041 | 0/15 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.774×** | -3.5 | 0.041 | 0/15 | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.796× | -3.1 | 0.14 | 2/14 (SW1417, HS-578T) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 382 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.5) |
| [[AN3 CA (line)]] | alt | 410 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -8.7) |
| [[C-33 A (line)]] | alt | 539 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -13.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 677 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 299 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 395 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -12.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +11.4) | — |
| [[H4 (line)]] | wt | 526 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -10.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 104 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 49.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +14.7) | — |
| [[SNU-423 (line)]] | alt | 146 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -9.0) |
| [[A-427 (line)]] | wt | 7.96 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.73 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.53 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.87 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.57 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.71 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.96 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.97 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.40 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 23 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBBP4-1]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[LINC02506]] | +0.68 | +0.45 / +0.64 | both halves | 3e-05 | **novel candidate** |
| [[LINC01518]] | +0.67 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[LINC00470]] | +0.56 | +0.40 / +0.70 | both halves | 5e-05 |  |
| [[TPTE]] | +0.56 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[ANKRD20A8P]] | +0.55 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[CDH12]] | +0.55 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[LINC02484]] | +0.55 | +0.23 / +0.69 | both halves | 5e-04 |  |
| [[LINC02327]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[LINC02968]] | +0.54 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[FAM230C]] | +0.53 | +0.17 / +0.61 | ⚠ one half (not replicated) | 0.001 |  |
| [[LINC02335]] | +0.53 | +0.12 / +0.63 | ⚠ one half (not replicated) | 0.002 |  |
| [[UTY]] | +0.52 | +0.25 / +0.54 | both halves | 4e-04 |  |
| [[FBXL7]] | +0.51 | +0.20 / +0.61 | both halves | 7e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHF2P2]] | C | PHF2P2 activity raises CCDC144NL-AS1's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 9.06× lower at baseline in the lines without PHF2P2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises CCDC144NL-AS1's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 7.58× lower at baseline in the lines without LINC01518 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[UBBP4-1]] | C | UBBP4-1 activity raises CCDC144NL-AS1's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 4.43× lower at baseline in the lines without UBBP4-1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[TPTE]] | C | TPTE activity raises CCDC144NL-AS1's level | lines that do not express TPTE (35) vs lines expressing it (15) | 2.74× lower at baseline in the lines without TPTE | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises CCDC144NL-AS1's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 3.46× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[LINC02327]] | C | LINC02327 activity raises CCDC144NL-AS1's level | lines that do not express LINC02327 (41) vs lines expressing it (9) | 2.92× lower at baseline in the lines without LINC02327 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000258028, LINC02566, ENSG00000289605; co-absent with the target |
| [[LINC02484]] | C | LINC02484 activity raises CCDC144NL-AS1's level | lines that do not express LINC02484 (40) vs lines expressing it (10) | 5.77× lower at baseline in the lines without LINC02484 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000260126, LINC02566, ENSG00000289605; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises CCDC144NL-AS1's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 3.73× lower at baseline in the lines without LINC01446 | 0.032 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[POTEF]] | C | POTEF activity raises CCDC144NL-AS1's level | lines that do not express POTEF (29) vs lines expressing it (21) | 3.69× lower at baseline in the lines without POTEF | 0.033 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |
| [[GABRA3]] | C | GABRA3 activity raises CCDC144NL-AS1's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 1.68× lower at baseline in the lines without GABRA3 | 0.048 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises CCDC144NL-AS1's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.65× lower at baseline in the lines without JAKMIP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LINC02575]] | C | LINC02575 activity raises CCDC144NL-AS1's level | lines that do not express LINC02575 (32) vs lines expressing it (18) | 2.54× lower at baseline in the lines without LINC02575 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 3, C 33. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYP]] | B | CCDC144NL-AS1 activity raises SYP's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without CCDC144NL-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent |
| [[SEMA6A]] | B | CCDC144NL-AS1 activity raises SEMA6A's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.57× lower at baseline in the lines without CCDC144NL-AS1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent |
| [[LDB2]] | B | CCDC144NL-AS1 activity raises LDB2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without CCDC144NL-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent |
| [[LINC02327]] | C | CCDC144NL-AS1 activity raises LINC02327's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.62× lower at baseline in the lines without CCDC144NL-AS1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LINC01518]] | C | CCDC144NL-AS1 activity raises LINC01518's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 7.66× lower at baseline in the lines without CCDC144NL-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LINC02484]] | C | CCDC144NL-AS1 activity raises LINC02484's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 4.87× lower at baseline in the lines without CCDC144NL-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[PHF2P2]] | C | CCDC144NL-AS1 activity raises PHF2P2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 4.38× lower at baseline in the lines without CCDC144NL-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LINC02575]] | C | CCDC144NL-AS1 activity raises LINC02575's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 3.77× lower at baseline in the lines without CCDC144NL-AS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[SCG3]] | C | CCDC144NL-AS1 activity raises SCG3's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.26× lower at baseline in the lines without CCDC144NL-AS1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[UBBP4-1]] | C | CCDC144NL-AS1 activity raises UBBP4-1's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 4.26× lower at baseline in the lines without CCDC144NL-AS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LINC01446]] | C | CCDC144NL-AS1 activity raises LINC01446's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 5.11× lower at baseline in the lines without CCDC144NL-AS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[NPFFR2]] | C | CCDC144NL-AS1 activity raises NPFFR2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without CCDC144NL-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.8, 28.3); signed map (34.9, 37.0). **Vector** length 45.0, 12.6% of its response variance represented; |z| ≥ 3 in 365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.2 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | CCDC144NL antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p11.2 — chr17:20,868,433-21,002,276 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51340) · Entrez [440416](https://www.ncbi.nlm.nih.gov/gene/440416) · Ensembl [ENSG00000233098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233098)

## Data

Gene col 13887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13887); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13887]; `tensor/DDL_lfc|DDL_z.npy` [13887]; `embed/gene_vectors.npy` [13887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13887 or target_col == 13887). Every well: [[CCDC144NL-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC144NL-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
