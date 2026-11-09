---
symbol: "ANO1"
type: "gene"
col: 5226
ensembl_id: "ENSG00000131620"
name: "anoctamin 1"
location: "11q13.3"
module: 31
arm: "+"
pooled_cpm: 47.21
n_lines_expressing: 20
n_dd_up: 17
n_dd_down: 24
n_dd_up_clean: 13
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 58
direction_downstream: 61
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ANO1

*anoctamin 1* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.97× (z +12.6, q 7e-34, up in 5 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +6.7, q 3e-09, up in 5 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.626× (z -8.1, q 5e-13, down in 16 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB5]] (+0.77, fdr 7e-06), [[PIWIL1]] (+0.74, fdr 7e-06), [[FERMT1]] (+0.73, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 58 arrows point to it, the strongest [[LINC02320]] → it (grade B ⚠); 61 go from it, the strongest it → [[SEMA3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.97×** | +12.6 | 7e-34 | 5/14 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.6 | 9e-29 | 8/18 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +7.7 | 4e-12 | 7/15 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +6.7 | 3e-09 | 5/18 (SW480, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.0 | 6e-05 | 4/17 (SW1417, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.9 | 9e-05 | 0/18 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 4e-04 | 11/18 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.5 | 6e-04 | 4/18 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +4.3 | 0.001 | 4/18 (COLO 205, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +4.2 | 0.001 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.007 | 4/18 (COLO 205, KATO III, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.011 | 7/18 (HT-29, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.016 | 0/18 | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.021 | 3/18 (LoVo, KATO III, …) | two highest doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.039 | 5/18 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.89×** | +3.2 | 0.043 | 10/18 (COLO 205, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.067 | 0/18 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, none with an alert; shown: the 15 strongest. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.626×** | -8.1 | 5e-13 | 16/17 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.557×** | -6.6 | 1e-08 | 10/18 (SW480, LoVo, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.705×** | -6.0 | 3e-07 | 14/18 (Panc 03.27, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.633×** | -5.6 | 4e-06 | 13/18 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.673×** | -4.6 | 4e-04 | 11/18 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -4.2 | 0.002 | 11/17 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.781×** | -4.2 | 0.002 | 8/18 (SW480, HOP62, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.717×** | -4.0 | 0.004 | 15/18 (Hs 766T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.791×** | -4.0 | 0.004 | 6/18 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.685×** | -4.0 | 0.004 | 11/18 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.724×** | -3.9 | 0.004 | 17/18 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.726×** | -3.8 | 0.008 | 13/17 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.777×** | -3.7 | 0.010 | 11/18 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.725×** | -3.6 | 0.012 | 8/18 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.013 | 11/18 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 278 | 0 | 25 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -24.8) |
| [[LoVo (line)]] | wt | 58.3 | 0 | 10 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -13.2) |
| [[SNU-1 (line)]] | wt | 61.2 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.8) |
| [[Hs 766T (line)]] | wt | 279 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -18.9) |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -16.4) |
| [[COLO 205 (line)]] | alt | 83.5 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 6.97× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -14.1) |
| [[LS 180 (line)]] | wt | 92.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0823× (z -23.9) |
| [[AsPC-1 (line)]] | alt | 91.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.305× (z -8.7) |
| [[BT-474 (line)]] | alt | 41.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.6) |
| [[KATO III (line)]] | alt | 240 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -17.8) |
| [[Panc 03.27 (line)]] | alt | 79.1 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.252× (z -12.0) |
| [[SW1417 (line)]] | alt | 167 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.6) |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -13.4) |
| [[A-172 (line)]] | wt | 5.95 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.63 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.82 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.35 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.54 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.41 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB5]] | +0.77 | +0.73 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[PIWIL1]] | +0.74 | +0.67 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[FERMT1]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LCK]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[GJB3]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[TMC7]] | +0.66 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[TNS4]] | +0.66 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[ITGB4]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CALB1]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[KLK10]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MPRIP]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[MALL]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 14, C 44. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | LINC02320 activity raises ANO1's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 3.04× lower at baseline in the lines without LINC02320 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[SEMA3B]] | B | SEMA3B activity raises ANO1's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.19× lower at baseline in the lines without SEMA3B | 0.022 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[EFNB2]] | B | EFNB2 activity raises ANO1's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without EFNB2 | 0.026 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[PTK2B]] | B | PTK2B activity raises ANO1's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.16× lower at baseline in the lines without PTK2B | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TGFA]] | B | TGFA activity raises ANO1's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.74× lower at baseline in the lines without TGFA | 0.041 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[SYNE3]] | B | SYNE3 activity raises ANO1's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without SYNE3 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IGSF9]] | B | IGSF9 activity raises ANO1's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.45× lower at baseline in the lines without IGSF9 | 0.075 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[LSMEM2]] | B | LSMEM2 activity raises ANO1's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without LSMEM2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ANO1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[KRT15]] | B | KRT15 activity raises ANO1's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.67× lower at baseline in the lines without KRT15 | 0.088 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[PPARG]] | B | PPARG activity raises ANO1's level | lines that do not express PPARG (20) vs lines expressing it (30) | 2.24× lower at baseline in the lines without PPARG | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |
| [[STON2]] | B | STON2 activity raises ANO1's level | lines that do not express STON2 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without STON2 | 0.093 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |

### Downstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 23, C 38. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | ANO1 activity raises SEMA3B's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.49× lower at baseline in the lines without ANO1 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[DEF6]] | B | ANO1 activity raises DEF6's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without ANO1 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[PPARD]] | B | ANO1 activity raises PPARD's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without ANO1 | 0.003 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[TMC6]] | B | ANO1 activity raises TMC6's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.97× lower at baseline in the lines without ANO1 | 0.006 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[PTK2B]] | B | ANO1 activity raises PTK2B's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.02× lower at baseline in the lines without ANO1 | 0.007 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[MYO18A]] | B | ANO1 activity raises MYO18A's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 1.93× lower at baseline in the lines without ANO1 | 0.010 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[EFNB2]] | B | ANO1 activity raises EFNB2's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.44× lower at baseline in the lines without ANO1 | 0.012 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[NECTIN1]] | B | ANO1 activity raises NECTIN1's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.66× lower at baseline in the lines without ANO1 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[LSMEM2]] | B | ANO1 activity raises LSMEM2's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without ANO1 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[IGSF9]] | B | ANO1 activity raises IGSF9's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without ANO1 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[BLACAT1]] | B | ANO1 activity raises BLACAT1's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 2.42× lower at baseline in the lines without ANO1 | 0.019 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |
| [[LEMD1]] | B | ANO1 activity raises LEMD1's level | lines that do not express ANO1 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without ANO1 | 0.023 | ⚠ within organs, on part of the lines; also absent: COL17A1, CLIC5, TMPRSS2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, 52.8); signed map (2.7, 38.7). **Vector** length 86.5, 31.0% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +3.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.1 | -4.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -6.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:69,985,907-70,189,530 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAOS2, FLJ10261, DOG1; previously ORAOV2, TMEM16A |
| Gene groups (HGNC) | Anoctamins |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 8 pathways, smallest: Induction of Cell-Cell Fusion; Late SARS-CoV-2 Infection Events; Stimuli-sensing channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5XXA6](https://www.uniprot.org/uniprotkb/Q5XXA6) (Anoctamin-1):

> Calcium-activated chloride channel (CaCC). Plays a role in transepithelial anion transport and smooth muscle contraction. Required for the normal functioning of the interstitial cells of Cajal (ICCs) which generate electrical pacemaker activity in gastrointestinal smooth muscles. Acts as a major contributor to basal and stimulated chloride conductance in airway epithelial cells and plays an important role in tracheal cartilage development. Required for CFTR activation by enhancing endoplasmic …

**Summary**, from NCBI Gene [55107](https://www.ncbi.nlm.nih.gov/gene/55107):

> Enables identical protein binding activity and monoatomic ion transmembrane transporter activity. Involved in monoatomic anion transport; mucus secretion; and protein localization to membrane. Located in apical plasma membrane. Implicated in Moyamoya disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21625) · Entrez [55107](https://www.ncbi.nlm.nih.gov/gene/55107) · UniProt [Q5XXA6](https://www.uniprot.org/uniprotkb/Q5XXA6) · Ensembl [ENSG00000131620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131620)

## Data

Gene col 5226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5226); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5226]; `tensor/DDL_lfc|DDL_z.npy` [5226]; `embed/gene_vectors.npy` [5226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5226 or target_col == 5226). Every well: [[ANO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
