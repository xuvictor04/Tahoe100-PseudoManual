---
symbol: "PCDHA6"
type: "gene"
col: 1326
ensembl_id: "ENSG00000081842"
name: "protocadherin alpha 6"
location: "5q31.3"
module: 150
arm: "+"
pooled_cpm: 8.84
n_lines_expressing: 33
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# PCDHA6

*protocadherin alpha 6* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +8.4, q 3e-14, up in 17 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.366× (z -10.3, q 3e-22, down in 23 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.520× (z -6.7, q 4e-09, down in 19 of 30 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAXC]] (+0.66, fdr 1e-05), [[GPLD1]] (+0.62, fdr 7e-06), [[LINC01122]] (+0.57, fdr 2e-05); moves opposite to [[TRIOBP]] (-0.50, fdr 3e-05), [[MCRIP1]] (-0.46, fdr 2e-04).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GABRB3]] → it (grade B ⚠); 9 go from it, the strongest it → [[FRG1-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.4 | 3e-14 | 17/29 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.69×** | +7.7 | 4e-12 | 19/30 (C32, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.8 | 2e-09 | 17/30 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.9 | 5e-07 | 12/30 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +5.0 | 7e-05 | 11/27 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.8 | 2e-04 | 15/29 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.5 | 5e-04 | 11/30 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.51×** | +4.2 | 0.002 | 11/30 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.003 | 10/30 (SW48, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.32×** | +4.0 | 0.003 | 14/30 (SHP-77, NCI-H2030, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.004 | 10/30 (A498, C32, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.004 | 10/30 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.020 | 9/30 (NCI-H2030, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.055 | 11/30 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.36×** | +3.2 | 0.055 | 8/29 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.056 | 6/29 (SW48, SW 900, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.074 | 8/29 (NCI-H1573, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.366×** | -10.3 | 3e-22 | 23/28 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.434×** | -8.6 | 3e-15 | 21/30 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.520×** | -6.7 | 4e-09 | 19/30 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.557×** | -6.0 | 3e-07 | 21/30 (NCI-H23, SW 900, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.620×** | -4.7 | 3e-04 | 14/24 (A-427, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.647×** | -4.5 | 8e-04 | 14/30 (BT-474, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.005 | 15/30 (NCI-H23, H4, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.697×** | -3.7 | 0.016 | 15/30 (SW48, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.696×** | -3.6 | 0.023 | 9/30 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.735×** | -3.1 | 0.088 | 12/30 (NCI-H23, NCI-H661, …) | rises with dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | **0.805×** | -3.1 | 0.088 | 6/30 (NCI-H661, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 16.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +12.3) | [[Digitoxin (drug)]] 0.5 µM 0.152× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 5.56 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 47.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.1) |
| [[A-172 (line)]] | wt | 7.63 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.102× (z -8.6) |
| [[A-427 (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 2.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0516× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 5.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.998 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAXC]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[GPLD1]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LINC01122]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[KATNAL2]] | +0.57 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SPAG17]] | +0.56 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[ARHGEF26-AS1]] | +0.55 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[SLC9A9]] | +0.55 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[AGBL4]] | +0.55 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ANKS1B]] | +0.55 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[DUSP19]] | +0.55 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[FAM184A]] | +0.54 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[ADAMTS3]] | +0.54 | +0.56 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIOBP]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MCRIP1]] | -0.46 | -0.47 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRB3]] | B | GABRB3 activity raises PCDHA6's level | lines that do not express GABRB3 (31) vs lines expressing it (19) | 2.24× lower at baseline in the lines without GABRB3 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000244468, S100A9, FGG |
| [[RIMS2]] | B | RIMS2 activity raises PCDHA6's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without RIMS2 | 0.012 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[LINC00886]] | B | LINC00886 activity raises PCDHA6's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.95× lower at baseline in the lines without LINC00886 | 0.035 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[GPLD1]] | B | GPLD1 activity raises PCDHA6's level | lines that do not express GPLD1 (5) vs lines expressing it (45) | 3.20× lower at baseline in the lines without GPLD1 | 0.051 | ⚠ within organs, on part of the lines; also absent: PDE5A, ALDH5A1, CCDC144CP; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PCDHA6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[KATNAL2]] | B | KATNAL2 activity raises PCDHA6's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.91× lower at baseline in the lines without KATNAL2 | 0.071 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[ANKS1B]] | B | ANKS1B activity raises PCDHA6's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.81× lower at baseline in the lines without ANKS1B | 0.089 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[KLHL13]] | C | KLHL13 activity raises PCDHA6's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 3.12× lower at baseline in the lines without KLHL13 | 0.092 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRG1-DT]] | B | PCDHA6 activity raises FRG1-DT's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.27× lower at baseline in the lines without PCDHA6 | 0.021 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[LINC00886]] | B | PCDHA6 activity raises LINC00886's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without PCDHA6 | 0.026 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[CAPS2]] | B | PCDHA6 activity raises CAPS2's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.60× lower at baseline in the lines without PCDHA6 | 0.028 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[ANO5]] | B | PCDHA6 activity raises ANO5's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.58× lower at baseline in the lines without PCDHA6 | 0.032 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[LINC02026]] | B | PCDHA6 activity raises LINC02026's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 1.44× lower at baseline in the lines without PCDHA6 | 0.055 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[AGA-DT]] | B | PCDHA6 activity raises AGA-DT's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without PCDHA6 | 0.060 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[MTA3]] | B | PCDHA6 activity raises MTA3's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without PCDHA6 | 0.069 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[GABRB3]] | B | PCDHA6 activity raises GABRB3's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without PCDHA6 | 0.077 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |
| [[LINC00466]] | B | PCDHA6 activity raises LINC00466's level | lines that do not express PCDHA6 (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without PCDHA6 | 0.088 | ⚠ within organs, on part of the lines; also absent: RAB39A, PHF21B, LONRF2 |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.2, 32.8); signed map (38.9, -10.9). **Vector** length 59.9, 12.2% of its response variance represented; |z| ≥ 3 in 711 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.5 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.9 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.6 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.4 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.3 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.2 | -6.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.9 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin alpha 6 |
| Locus type | complex locus constituent (other) |
| Location | 5q31.3 — chr5:140,827,958-141,012,347 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CNR2, CRNR2, PCDH-ALPHA6; previously CNRS2 |
| Gene groups (HGNC) | Clustered protocadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN73](https://www.uniprot.org/uniprotkb/Q9UN73) (Protocadherin alpha-6):

> Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain.

**Summary**, from NCBI Gene [56142](https://www.ncbi.nlm.nih.gov/gene/56142):

> This gene is a member of the protocadherin alpha gene cluster, one of three related gene clusters tandemly linked on chromosome five that demonstrate an unusual genomic organization similar to that of B-cell and T-cell receptor gene clusters. The alpha gene cluster is composed of 15 cadherin superfamily genes related to the mouse CNR genes and consists of 13 highly similar and 2 more distantly related coding sequences. The tandem array of 15 N-terminal exons, or variable exons, are followed by …

**Accessions** — [HGNC:8672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8672) · Entrez [56142](https://www.ncbi.nlm.nih.gov/gene/56142) · UniProt [Q9UN73](https://www.uniprot.org/uniprotkb/Q9UN73) · Ensembl [ENSG00000081842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081842)

## Data

Gene col 1326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1326); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1326]; `tensor/DDL_lfc|DDL_z.npy` [1326]; `embed/gene_vectors.npy` [1326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1326 or target_col == 1326). Every well: [[PCDHA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDHA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
