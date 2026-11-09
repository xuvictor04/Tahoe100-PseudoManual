---
symbol: "LTBP3"
type: "gene"
col: 9588
ensembl_id: "ENSG00000168056"
name: "latent transforming growth factor beta binding protein 3"
location: "11q13.1"
module: 78
arm: "+"
pooled_cpm: 38.1
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 47
n_dd_up_clean: 2
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# LTBP3

*latent transforming growth factor beta binding protein 3* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Retinoic acid (drug)]] 0.5 µM: 1.30× (z +4.0, q 0.032, up in 20 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.431× (z -12.7, q 5e-34, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA3]] (+0.69, fdr 7e-06), [[COL13A1]] (+0.61, fdr 7e-06), [[ITGB3]] (+0.60, fdr 1e-05); moves opposite to [[MIR4307HG]] (-0.50, fdr 6e-05), [[MYO16-AS1]] (-0.49, fdr 6e-05), [[SPINK13]] (-0.48, fdr 5e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LOXL2]] → it (grade B ⚠); 10 go from it, the strongest it → [[PLP2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.032 | 20/43 (LOX-IMVI, SK-MEL-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.7 | 0.040 | 18/40 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Retinoic acid (drug)]] 5 µM |  | 1.19× | +3.7 | 0.040 | 17/44 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.053 | 18/44 (LOX-IMVI, A-172, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.25× | +3.1 | 0.21 | 14/37 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Apalutamide (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.21 | 11/44 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Tazarotene (drug)]] 5 µM |  | 1.22× | +3.0 | 0.22 | 15/44 (A549, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.431×** | -12.7 | 5e-34 | 36/44 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.594×** | -11.1 | 5e-26 | 30/44 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.553×** | -8.9 | 1e-16 | 26/43 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.577×** | -8.3 | 2e-14 | 28/44 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -7.8 | 6e-13 | 32/43 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.610×** | -7.4 | 1e-11 | 26/44 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -7.4 | 1e-11 | 28/44 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.604×** | -7.1 | 6e-11 | 31/43 (HOP62, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -6.7 | 2e-09 | 23/44 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.650×** | -6.5 | 6e-09 | 25/42 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.661×** | -6.2 | 2e-08 | 25/44 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -6.2 | 3e-08 | 27/42 (HT-29, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -5.9 | 1e-07 | 24/42 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.760×** | -5.8 | 3e-07 | 23/44 (HEC-1-A, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.694×** | -5.5 | 2e-06 | 25/44 (PANC-1, J82, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.719×** | -5.4 | 2e-06 | 21/44 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 43.5 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -13.5) |
| [[HOP62 (line)]] | alt | 78.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.8) |
| [[J82 (line)]] | alt | 27.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -16.8) |
| [[PANC-1 (line)]] | alt | 33.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.7) |
| [[RPMI-7951 (line)]] | alt | 66.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -11.6) |
| [[A-172 (line)]] | wt | 63.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.4) |
| [[C32 (line)]] | wt | 90.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 67.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -13.1) |
| [[SNU-423 (line)]] | alt | 53.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -12.9) |
| [[Hs 766T (line)]] | wt | 81.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -17.9) |
| [[HS-578T (line)]] | alt | 71.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 32.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0787× (z -16.0) |
| [[SW 900 (line)]] | alt | 123 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.0) |
| [[A-427 (line)]] | wt | 33.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -9.0) |
| [[A549 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0805× (z -10.1) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 66.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.131× (z -8.7) |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0835× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 45.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.463× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 63.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 60.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.275× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -11.5) |
| [[A498 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 47.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA3]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[COL13A1]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[ITGB3]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 | pathway: Elastic fibre formation; STRING 552 |
| [[STMN3]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ECE1]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[LINC02813]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[WWTR1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 | pathway: Signaling by TGF-beta Receptor Complex |
| [[ETV1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[STX1A]] | +0.56 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[EHBP1L1]] | +0.56 | +0.62 / +0.52 | both halves | 1e-05 | ⚠ same locus (17.1 kb: neighbours can correlate without regulation) |
| [[SHC4]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 | pathway: Elastic fibre formation; STRING 617 |
| [[SH2B3]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4307HG]] | -0.50 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[MYO16-AS1]] | -0.49 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[SPINK13]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ANKRD30B]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[MARCOL]] | -0.46 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PAX8-AS1]] | -0.45 | -0.47 / -0.24 | both halves | 4e-04 |  |
| [[ROS1]] | -0.45 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[PLCH1]] | -0.43 | -0.50 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOXL2]] | B | LOXL2 activity raises LTBP3's level | lines that do not express LOXL2 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without LOXL2 | 0.028 | ⚠ within organs, on part of the lines; also absent: GNG11, VIM, ARMCX1 |
| [[MAP2K1]] | B | MAP2K1 activity raises LTBP3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.3% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ELFN2]] | B | ELFN2 activity raises LTBP3's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without ELFN2 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92 |
| [[FN1]] | B | FN1 activity raises LTBP3's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without FN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[MTSS1]] | B | MTSS1 activity raises LTBP3's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without MTSS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[ADAM8]] | B | ADAM8 activity raises LTBP3's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without ADAM8 | 0.097 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLP2]] | C | LTBP3 activity raises PLP2's level | lines that do not express LTBP3 (4) vs lines expressing it (46) | 3.29× lower at baseline in the lines without LTBP3 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| [[PPFIBP1]] | C | LTBP3 activity strengthens PPFIBP1's drug response | lines that do not express LTBP3 (4) vs lines expressing it (45) | the lines without LTBP3 respond 0.00× as strongly (z diff +4.85); strongest at Homoharringtonine 5 µM: 1.59x vs 0.66x (z diff +10.8) | 0.005 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PHLDB1]] | C | LTBP3 activity raises PHLDB1's level | lines that do not express LTBP3 (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without LTBP3 | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| cells under [[AZD2858 (drug)]] 5 µM | C | LTBP3 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express LTBP3 (4) vs lines expressing it (44) | the lines without LTBP3: 1.49× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | LTBP3 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express LTBP3 (4) vs lines expressing it (44) | the lines without LTBP3: 1.31× the cells of the other lines | 0.051 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | LTBP3 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LTBP3 (4) vs lines expressing it (44) | the lines without LTBP3: 0.79× the cells of the other lines | 0.063 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| cells under [[Hydroxyfasudil (drug)]] 5 µM | C | LTBP3 activity lowers the cells' numbers under Hydroxyfasudil 5 µM (makes them more sensitive) | lines that do not express LTBP3 (4) vs lines expressing it (44) | the lines without LTBP3: 1.25× the cells of the other lines | 0.071 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| [[STX1A]] | C | LTBP3 activity raises STX1A's level | lines that do not express LTBP3 (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without LTBP3 | 0.093 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| [[TGFB1]] | C | LTBP3 activity raises TGFB1's level | lines that do not express LTBP3 (4) vs lines expressing it (46) | 3.42× lower at baseline in the lines without LTBP3 | 0.094 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| [[ITGB5]] | C | LTBP3 activity raises ITGB5's level | lines that do not express LTBP3 (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without LTBP3 | 0.094 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.8, 6.1); signed map (6.2, 50.9). **Vector** length 102, 26.8% of its response variance represented; |z| ≥ 3 in 1,244 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.4 | -6.2 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.0 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.0 | -8.9 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +0.8 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.9 | +1.7 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.9 | +0.7 |
|  | [[DTP3 (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.5 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.4 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | latent transforming growth factor beta binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,538,559-65,558,930 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LTBP2 |
| Gene groups (HGNC) | Latent transforming growth factor beta binding proteins |
| Reactome | 6 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS15](https://www.uniprot.org/uniprotkb/Q9NS15) (Latent-transforming growth factor beta-binding protein 3):

> Key regulator of transforming growth factor beta (TGFB1, TGFB2 and TGFB3) that controls TGF-beta activation by maintaining it in a latent state during storage in extracellular space. Associates specifically via disulfide bonds with the Latency-associated peptide (LAP), which is the regulatory chain of TGF-beta, and regulates integrin-dependent activation of TGF-beta.

**Summary**, from NCBI Gene [4054](https://www.ncbi.nlm.nih.gov/gene/4054):

> The protein encoded by this gene forms a complex with transforming growth factor beta (TGF-beta) proteins and may be involved in their subcellular localization. Activation of this complex requires removal of the encoded binding protein. This protein also may play a structural role in the extracellular matrix. Three transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:6716](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6716) · Entrez [4054](https://www.ncbi.nlm.nih.gov/gene/4054) · UniProt [Q9NS15](https://www.uniprot.org/uniprotkb/Q9NS15) · Ensembl [ENSG00000168056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168056)

## Data

Gene col 9588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9588); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9588]; `tensor/DDL_lfc|DDL_z.npy` [9588]; `embed/gene_vectors.npy` [9588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9588 or target_col == 9588). Every well: [[LTBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
