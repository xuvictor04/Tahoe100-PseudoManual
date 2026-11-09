---
symbol: "NLGN2"
type: "gene"
col: 9889
ensembl_id: "ENSG00000169992"
name: "neuroligin 2"
location: "17p13.1"
module: 1
arm: "-"
pooled_cpm: 22.35
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NLGN2

*neuroligin 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +14.7, q 1e-45, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.463× (z -10.7, q 4e-24, down in 35 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD81]] (+0.65, fdr 7e-06), [[SH3D21]] (+0.62, fdr 8e-06), [[RAB5B]] (+0.61, fdr 1e-05); moves opposite to [[MRPL15]] (-0.57, fdr 2e-05), [[TMA16]] (-0.57, fdr 3e-05), [[ATIC]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CERCAM]] → it (grade B ⚠); 7 go from it, the strongest it → [[CERCAM]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +14.7 | 1e-45 | 41/43 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +7.5 | 1e-11 | 30/44 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +6.8 | 2e-09 | 27/44 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.4 | 8e-06 | 23/43 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.6 | 5e-04 | 4/44 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 9e-04 | 18/44 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.004 | 19/44 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.006 | 19/44 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.042 | 17/43 (HOP62, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.042 | 12/43 (HS-578T, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.042 | 13/43 (NCI-H2030, HEC-1-A, …) | two highest doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.070 | 15/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9889.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.463×** | -10.7 | 4e-24 | 35/44 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.490×** | -9.5 | 4e-19 | 37/44 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.639×** | -8.8 | 3e-16 | 30/44 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.556×** | -8.2 | 4e-14 | 34/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.708×** | -4.8 | 2e-04 | 23/44 (RPMI-7951, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -4.7 | 3e-04 | 24/42 (HepG2/C3A, CHP-212, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -4.4 | 9e-04 | 21/44 (Panc 03.27, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.735×** | -4.3 | 0.001 | 21/44 (HS-578T, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.736×** | -4.1 | 0.003 | 24/44 (hTERT-HPNE, LOX-IMVI, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.753×** | -3.7 | 0.011 | 17/44 (LOX-IMVI, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.771×** | -3.6 | 0.017 | 19/44 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.773×** | -3.6 | 0.017 | 18/43 (SW 900, hTERT-HPNE, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.778×** | -3.5 | 0.022 | 15/44 (A549, SW 900, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.627×** | -3.4 | 0.028 | 18/43 (SK-MEL-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -3.2 | 0.047 | 16/44 (HS-578T, SW 1088, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.294× (z -9.9) |
| [[PANC-1 (line)]] | alt | 20.9 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -9.6) |
| [[SW480 (line)]] | alt | 18.1 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.2) | [[Harringtonine (drug)]] 0.5 µM 0.324× (z -8.9) |
| [[A-172 (line)]] | wt | 59.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -18.7) |
| [[LOX-IMVI (line)]] | wt | 26.1 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.274× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 23.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +11.8) | — |
| [[RKO (line)]] | wt | 38.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -8.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 25.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.4) | — |
| [[A549 (line)]] | wt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +14.5) | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.8) |
| [[Hs 766T (line)]] | wt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +11.3) | — |
| [[LoVo (line)]] | wt | 24.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 26.3 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0573× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.295× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -8.8) |
| [[AN3 CA (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD81]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SH3D21]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[RAB5B]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MTCH1]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ATG9A]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[AP2A1]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 | pathway: Neuronal System |
| [[PRSS53]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SBF1]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SEZ6L2]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[LRPAP1]] | +0.55 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[KIFC2]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[HLA-C]] | +0.54 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL15]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[TMA16]] | -0.57 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ATIC]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[DIS3L]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CRADD]] | -0.56 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[SLX4IP]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[PEX1]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PAK1IP1]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.55 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[N6AMT1]] | -0.54 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[DPH5]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[NBN]] | -0.53 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | B | CERCAM activity raises NLGN2's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 3.40× lower at baseline in the lines without CERCAM | 5e-04 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[APLP1]] | B | APLP1 activity raises NLGN2's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.30× lower at baseline in the lines without APLP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[MEIS3]] | B | MEIS3 activity raises NLGN2's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 2.41× lower at baseline in the lines without MEIS3 | 0.008 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NLGN2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers NLGN2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | C | NLGN2 activity raises CERCAM's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 5.47× lower at baseline in the lines without NLGN2 | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |
| [[APLP1]] | C | NLGN2 activity raises APLP1's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 3.94× lower at baseline in the lines without NLGN2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |
| [[GUCD1]] | C | NLGN2 activity lowers GUCD1's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 1.57× higher at baseline in the lines without NLGN2 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |
| [[C12orf29]] | C | NLGN2 activity raises C12orf29's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 1.51× lower at baseline in the lines without NLGN2 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |
| [[BSG]] | C | NLGN2 activity raises BSG's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without NLGN2 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |
| [[MEIS3]] | C | NLGN2 activity raises MEIS3's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 4.53× lower at baseline in the lines without NLGN2 | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |
| [[PTMS]] | C | NLGN2 activity raises PTMS's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without NLGN2 | 0.0997 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.7, -36.6); signed map (-33.9, 29.7). **Vector** length 87.0, 18.3% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +14.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -2.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.5 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | neuroligin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,404,874-7,419,860 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1366 |
| Gene groups (HGNC) | Neuroligins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFZ4](https://www.uniprot.org/uniprotkb/Q8NFZ4) (Neuroligin-2):

> Transmembrane scaffolding protein involved in cell-cell interactions via its interactions with neurexin family members. Mediates cell-cell interactions both in neurons and in other types of cells, such as Langerhans beta cells. Plays a role in synapse function and synaptic signal transmission, especially via gamma-aminobutyric acid receptors (GABA(A) receptors). Functions by recruiting and clustering synaptic proteins. Promotes clustering of postsynaptic GABRG2 and GPHN. Promotes clustering of …

**Summary**, from NCBI Gene [57555](https://www.ncbi.nlm.nih.gov/gene/57555):

> This gene encodes a member of a family of neuronal cell surface proteins. Members of this family may act as splice site-specific ligands for beta-neurexins and may be involved in the formation and remodeling of central nervous system synapses. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14290) · Entrez [57555](https://www.ncbi.nlm.nih.gov/gene/57555) · UniProt [Q8NFZ4](https://www.uniprot.org/uniprotkb/Q8NFZ4) · Ensembl [ENSG00000169992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169992)

## Data

Gene col 9889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9889); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9889]; `tensor/DDL_lfc|DDL_z.npy` [9889]; `embed/gene_vectors.npy` [9889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9889 or target_col == 9889). Every well: [[NLGN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLGN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
