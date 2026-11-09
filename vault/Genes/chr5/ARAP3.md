---
symbol: "ARAP3"
type: "gene"
col: 4177
ensembl_id: "ENSG00000120318"
name: "ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 3"
location: "5q31.3"
module: 36
arm: "+"
pooled_cpm: 9.77
n_lines_expressing: 41
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ARAP3

*ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 3* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.62× (z +10.1, q 3e-21, up in 25 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.475× (z -15.5, q 0e+00, down in 30 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF7]] (+0.60, fdr 1e-05), [[NBPF9]] (+0.56, fdr 1e-05), [[KIF21B]] (+0.55, fdr 1e-05); moves opposite to [[CDKN1B]] (-0.58, fdr 1e-05), [[ATRAID]] (-0.54, fdr 3e-05), [[NCOA2]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PLPP4]] → it (grade B ⚠); 6 go from it, the strongest it → [[TM4SF19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4177.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +10.1 | 3e-21 | 25/39 (LoVo, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +9.7 | 1e-19 | 24/35 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +7.5 | 8e-12 | 19/38 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 2e-07 | 19/38 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +5.3 | 1e-05 | 15/37 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.3 | 0.002 | 2/16 (NCI-H1792, C32) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +3.8 | 0.013 | 8/38 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.021 | 10/39 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.022 | 3/32 (SW1417, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.23× | +3.1 | 0.11 | 8/38 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.13 | 3/39 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.475×** | -15.5 | 0e+00 | 30/37 (MIA PaCa-2, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.572×** | -11.6 | 1e-28 | 25/39 (SK-MEL-2, Hs 766T, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.504×** | -9.7 | 7e-20 | 26/37 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -8.5 | 3e-15 | 23/35 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.639×** | -6.6 | 5e-09 | 19/39 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -6.4 | 2e-08 | 19/37 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.679×** | -5.7 | 1e-06 | 18/39 (LoVo, hTERT-HPNE, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.699×** | -5.1 | 3e-05 | 13/38 (SW48, HEC-1-A, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -4.6 | 3e-04 | 15/39 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.723×** | -4.6 | 3e-04 | 14/33 (A549, J82, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.584×** | -4.1 | 0.002 | 10/33 (RKO, H4, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.766×** | -3.9 | 0.004 | 10/33 (RKO, COLO 205, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.828×** | -3.5 | 0.021 | 13/39 (MIA PaCa-2, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Bexarotene (drug)]] 0.5 µM |  | **0.791×** | -3.4 | 0.024 | 6/39 (SW 1271, CFPAC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.853× | -3.3 | 0.038 | 7/39 (A498, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.805×** | -3.2 | 0.049 | 12/38 (HOP62, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 23.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -14.4) |
| [[C32 (line)]] | wt | 24.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -8.8) |
| [[RKO (line)]] | wt | 23.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 13.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.9) |
| [[A549 (line)]] | wt | 6.02 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0676× (z -11.2) |
| [[Hs 766T (line)]] | wt | 50.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -14.9) |
| [[J82 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0781× (z -19.5) |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 8.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HS-578T (line)]] | alt | 6.17 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0846× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -8.6) |
| [[KATO III (line)]] | alt | 4.70 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 9.38 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 25.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.6) |
| [[SNU-423 (line)]] | alt | 7.58 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0942× (z -9.8) |
| [[SW1417 (line)]] | alt | 4.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0892× (z -9.2) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF7]] | +0.60 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[NBPF9]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[KIF21B]] | +0.55 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZDHHC18]] | +0.55 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ZNF473]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[CPNE2]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[GPSM1]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MPP3]] | +0.53 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[ANKS6]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 | same gene group |
| [[RUBCNL]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[DFFA]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[NBPF20]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN1B]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ATRAID]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[NCOA2]] | -0.52 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[BBX]] | -0.51 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[FBXO8]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[TBCK]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PUS10]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ALDH6A1]] | -0.48 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[CDK19]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ACBD5]] | -0.47 | -0.41 / -0.48 | both halves | 4e-05 | pathway: RHOA GTPase cycle |
| [[SMIM14]] | -0.47 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[CMC4]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLPP4]] | B | PLPP4 activity raises ARAP3's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without PLPP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[TOP2A]] | B | TOP2A activity raises ARAP3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C13orf46]] | B | C13orf46 activity raises ARAP3's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 2.62× lower at baseline in the lines without C13orf46 | 0.040 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[EFCAB6]] | B | EFCAB6 activity raises ARAP3's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without EFCAB6 | 0.052 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers ARAP3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF19]] | B | ARAP3 activity raises TM4SF19's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 4.12× lower at baseline in the lines without ARAP3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[TM4SF19-DYNLT2B]] | B | ARAP3 activity raises TM4SF19-DYNLT2B's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without ARAP3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[LIMK1]] | B | ARAP3 activity raises LIMK1's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without ARAP3 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[ACBD5]] | B | ARAP3 activity lowers ACBD5's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 1.25× higher at baseline in the lines without ARAP3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[EFCAB6]] | B | ARAP3 activity raises EFCAB6's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 1.22× lower at baseline in the lines without ARAP3 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[NCOA2]] | B | ARAP3 activity lowers NCOA2's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without ARAP3 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.318). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (4.3, -27.4); signed map (-16.2, 47.7). **Vector** length 78.4, 16.5% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.0 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -9.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -8.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -15.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:141,653,401-141,682,230 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21065, DRAG1; previously CENTD3 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; Pleckstrin homology domain containing; Sterile alpha motif domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: RAC3 GTPase cycle; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWN8](https://www.uniprot.org/uniprotkb/Q8WWN8) (Arf-GAP with Rho-GAP domain, ANK repeat and PH domain-containing protein 3):

> Phosphatidylinositol 3,4,5-trisphosphate-dependent GTPase-activating protein that modulates actin cytoskeleton remodeling by regulating ARF and RHO family members. Is activated by phosphatidylinositol 3,4,5-trisphosphate (PtdIns(3,4,5)P3) binding. Can be activated by phosphatidylinositol 3,4-bisphosphate (PtdIns(3,4,5)P2) binding, albeit with lower efficiency. Acts on ARF6, RAC1, RHOA and CDC42. Plays a role in the internalization of anthrax toxin.

**Summary**, from NCBI Gene [64411](https://www.ncbi.nlm.nih.gov/gene/64411):

> This gene encodes a phosphoinositide binding protein containing ARF-GAP, RHO-GAP, RAS-associating, and pleckstrin homology domains. The ARF-GAP and RHO-GAP domains cooperate in mediating rearrangements in the cell cytoskeleton and cell shape. It is a specific PtdIns(3,4,5)P3/PtdIns(3,4)P2-stimulated Arf6-GAP protein. An alternatively spliced transcript has been found for this gene, but its biological validity has not been determined. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:24097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24097) · Entrez [64411](https://www.ncbi.nlm.nih.gov/gene/64411) · UniProt [Q8WWN8](https://www.uniprot.org/uniprotkb/Q8WWN8) · Ensembl [ENSG00000120318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120318)

## Data

Gene col 4177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4177); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4177]; `tensor/DDL_lfc|DDL_z.npy` [4177]; `embed/gene_vectors.npy` [4177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4177 or target_col == 4177). Every well: [[ARAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
