---
symbol: "FBXO44"
type: "gene"
col: 5388
ensembl_id: "ENSG00000132879"
name: "F-box protein 44"
location: "1p36.22"
module: 221
arm: "+"
pooled_cpm: 6.91
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# FBXO44

*F-box protein 44* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.91× (z +11.5, q 6e-28, up in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.30× (z +4.7, q 6e-04, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.381× (z -17.1, q 0e+00, down in 37 of 42 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.382× (z -12.1, q 5e-31, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC45A]] (+0.75, fdr 7e-06), [[CDS2]] (+0.69, fdr 1e-05), [[PLD2]] (+0.67, fdr 7e-06); moves opposite to [[R3HDM2]] (-0.63, fdr 1e-05), [[GEN1]] (-0.62, fdr 8e-06), [[ERCC6L2]] (-0.61, fdr 1e-05).
> It is in [[Module 221]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FBXO2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5388.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.91×** | +11.5 | 6e-28 | 33/46 (LOX-IMVI, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.45×** | +4.7 | 6e-04 | 12/42 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.7 | 6e-04 | 12/46 (HT-29, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.5 | 0.001 | 11/31 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 0.001 | 17/46 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.001 | 15/46 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +4.0 | 0.005 | 8/37 (NCI-H460, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.012 | 6/39 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.013 | 12/43 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.6 | 0.016 | 4/12 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.018 | 8/41 (MIA PaCa-2, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.019 | 11/46 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.026 | 11/46 (PANC-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.028 | 13/46 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.028 | 10/39 (RKO, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.044 | 4/45 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.071 | 6/41 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5388.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.381×** | -17.1 | 0e+00 | 37/42 (NCI-H1573, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.382×** | -12.1 | 5e-31 | 32/42 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.483×** | -8.8 | 3e-16 | 31/44 (HOP62, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.564×** | -7.2 | 9e-11 | 23/46 (H4, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.590×** | -6.6 | 4e-09 | 28/45 (SW 900, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.427×** | -5.6 | 2e-06 | 19/43 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -5.1 | 3e-05 | 16/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.678×** | -4.9 | 8e-05 | 19/39 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -4.3 | 1e-03 | 13/40 (Hs 766T, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.719×** | -4.1 | 0.002 | 18/44 (LOX-IMVI, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5388. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 8.16 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Bentamapimod (drug)]] 0.05 µM 0.0881× (z -9.8) |
| [[HOP62 (line)]] | alt | 5.94 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.2) |
| [[A498 (line)]] | wt | 4.16 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +8.9) ⚠ cell-cycle shift, explains ~4% of this change | — |
| [[CFPAC-1 (line)]] | alt | 5.60 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.116× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 5.64 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 5.21 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0568× (z -16.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 6.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 9.44 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 6.88 | 0 | 1 | — | [[Thymol (drug)]] 5 µM 0.185× (z -8.9) |
| [[SNU-423 (line)]] | alt | 7.13 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 9.99 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0727× (z -8.5) |
| [[SW480 (line)]] | alt | 6.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5388), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC45A]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[CDS2]] | +0.69 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[PLD2]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[ATPAF2]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[C20orf96]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[VPS37D]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[UNC119]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[NTAN1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.65 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.64 | +0.71 / +0.48 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[RTCA]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM2]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GEN1]] | -0.62 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[ERCC6L2]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[TASOR]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[MIS12]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ST7L]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[CYREN]] | -0.59 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ZBTB38]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[WARS2-AS1]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MYH15]] | -0.55 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[PHF19]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | -0.55 | -0.62 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO2]] | B | FBXO2 activity raises FBXO44's level | lines that do not express FBXO2 (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without FBXO2 | 0.005 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, LAMP3 |
| [[PARD6G]] | B | PARD6G activity raises FBXO44's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.00× lower at baseline in the lines without PARD6G | 0.020 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[LRP3]] | B | LRP3 activity raises FBXO44's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without LRP3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.4, -8.5); signed map (-31.6, -5.8). **Vector** length 74.1, 13.0% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.4 | +11.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.5 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.7 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.3 | -17.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -12.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.8 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -5.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -0.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,654,375-11,663,327 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBX30, FBG3, MGC14140, Fbxo6a, Fbx44 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4M3](https://www.uniprot.org/uniprotkb/Q9H4M3) (F-box only protein 44):

> Substrate-recognition component of two distinct E3 ligase complexes, the SKP1-CUL1-FBXO44 complex and the CUL4B-DDB1-FBXO44 complex. The complex SCF(FBXO44) complex ubiquitinates and mediates BRCA1 degradation. In association with cullin 4B/CUL4B and DDB1, mediates the ubiquitination of RGS2 leading to its degradation. Additionally, regulates the pregnane X receptor/NR1I2 protein level by ubiquitination and degradation.

**Summary**, from NCBI Gene [93611](https://www.ncbi.nlm.nih.gov/gene/93611):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:24847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24847) · Entrez [93611](https://www.ncbi.nlm.nih.gov/gene/93611) · UniProt [Q9H4M3](https://www.uniprot.org/uniprotkb/Q9H4M3) · Ensembl [ENSG00000132879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132879)

## Data

Gene col 5388: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5388); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5388, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5388]; `tensor/DDL_lfc|DDL_z.npy` [5388]; `embed/gene_vectors.npy` [5388]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5388 or target_col == 5388). Every well: [[FBXO44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
