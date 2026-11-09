---
symbol: "VILL"
type: "gene"
col: 5808
ensembl_id: "ENSG00000136059"
name: "villin like"
location: "3p22.2"
module: 55
arm: "+"
pooled_cpm: 2.99
n_lines_expressing: 34
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 82
direction_downstream: 13
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# VILL

*villin like* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.76× (z +8.9, q 2e-16, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.53× (z +3.9, q 0.011, up in 5 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.451× (z -7.3, q 2e-10, down in 19 of 30 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.604× (z -4.6, q 4e-04, down in 13 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01819]] (+0.79, fdr 7e-06), [[HNF4A]] (+0.75, fdr 7e-06), [[LINC02474]] (+0.74, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 82 arrows point to it, the strongest [[LINC02474]] → it (grade B ⚠); 13 go from it, the strongest it → [[BMP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +8.9 | 2e-16 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +7.9 | 1e-12 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.3 | 0.003 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.36×** | +4.0 | 0.011 | 2/30 (NCI-H23, PANC-1) | top dose only | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.011 | 5/30 (SW480, SW48, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.4 | 0.054 | 0/7 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.68×** | +3.4 | 0.054 | 1/9 (LS 180) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.62× | +3.2 | 0.11 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.44× | +3.1 | 0.12 | 0/15 | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | 1.45× | +3.0 | 0.14 | 0/22 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.451×** | -7.3 | 2e-10 | 19/30 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.474×** | -6.8 | 2e-09 | 14/29 (LoVo, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.551×** | -5.2 | 3e-05 | 12/26 (LoVo, KATO III, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.551×** | -4.9 | 2e-04 | 12/27 (LS 180, LoVo, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.594×** | -4.8 | 2e-04 | 17/30 (LoVo, KATO III, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.604×** | -4.6 | 4e-04 | 13/28 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.599×** | -4.2 | 0.002 | 15/28 (LoVo, KATO III, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.654×** | -3.9 | 0.007 | 8/30 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.655×** | -3.9 | 0.007 | 8/29 (SK-MEL-2, SW48, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.679×** | -3.5 | 0.022 | 2/29 (PANC-1, hTERT-HPNE) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -3.5 | 0.023 | 12/28 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Erlotinib (drug)]] 0.5 µM |  | **0.690×** | -3.4 | 0.033 | 6/29 (SW 900, HCT15, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.679×** | -3.2 | 0.070 | 14/26 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.701×** | -3.1 | 0.072 | 8/16 (HEC-1-A, KATO III, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.527×** | -3.1 | 0.081 | 7/23 (LoVo, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.720×** | -3.0 | 0.086 | 4/29 (HCT15, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.711×** | -3.0 | 0.086 | 3/29 (SW480, CFPAC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 13.8 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0311× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0836× (z -12.4) |
| [[KATO III (line)]] | alt | 18.9 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -16.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0188× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 7.66 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 6.86 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0440× (z -10.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 7.40 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0520× (z -13.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[COLO 205 (line)]] | alt | 7.38 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0497× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.500 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.796 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.943 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.889 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01819]] | +0.79 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.75 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[LINC02474]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.73 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[EDAR]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[HEPH]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.72 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SLC5A1]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 79, C 3. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02474]] | B | LINC02474 activity raises VILL's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 2.56× lower at baseline in the lines without LINC02474 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[TMEM139]] | B | TMEM139 activity raises VILL's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without TMEM139 | 0.005 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[LINC02331]] | B | LINC02331 activity raises VILL's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.17× lower at baseline in the lines without LINC02331 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[CBLC]] | B | CBLC activity raises VILL's level | lines that do not express CBLC (31) vs lines expressing it (19) | 2.28× lower at baseline in the lines without CBLC | 0.010 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[PROM1]] | B | PROM1 activity raises VILL's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.68× lower at baseline in the lines without PROM1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[EPS8L3]] | B | EPS8L3 activity raises VILL's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 2.63× lower at baseline in the lines without EPS8L3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[TJP3]] | B | TJP3 activity raises VILL's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.07× lower at baseline in the lines without TJP3 | 0.013 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[CEACAM1]] | B | CEACAM1 activity strengthens VILL's drug response | lines that do not express CEACAM1 (16) vs lines expressing it (14) | the lines without CEACAM1 respond 0.44× as strongly (z diff +1.62); strongest at Idarubicin (hydrochloride) 0.5 µM: 0.66x vs 0.35x (z diff +3.0) | 0.014 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; target measured in part of the lines; artifact flags |
| [[RAB25]] | B | RAB25 activity raises VILL's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without RAB25 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[TSPOAP1]] | B | TSPOAP1 activity raises VILL's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without TSPOAP1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[CDH1]] | B | CDH1 activity raises VILL's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without CDH1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[CLIC5]] | B | CLIC5 activity raises VILL's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.10× lower at baseline in the lines without CLIC5 | 0.020 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP4]] | B | VILL activity raises BMP4's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without VILL | 0.021 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[GPR35]] | B | VILL activity raises GPR35's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without VILL | 0.052 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[USH1C]] | B | VILL activity raises USH1C's level | lines that do not express VILL (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without VILL | 0.056 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[EPS8L3]] | B | VILL activity raises EPS8L3's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.80× lower at baseline in the lines without VILL | 0.060 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[MROH7]] | B | VILL activity raises MROH7's level | lines that do not express VILL (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without VILL | 0.064 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[ZNF860]] | B | VILL activity raises ZNF860's level | lines that do not express VILL (16) vs lines expressing it (34) | 1.76× lower at baseline in the lines without VILL | 0.069 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[LINC02331]] | B | VILL activity raises LINC02331's level | lines that do not express VILL (16) vs lines expressing it (34) | 1.90× lower at baseline in the lines without VILL | 0.072 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[MYH14]] | B | VILL activity raises MYH14's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.92× lower at baseline in the lines without VILL | 0.074 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | VILL activity raises TNFRSF14-AS1's level | lines that do not express VILL (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without VILL | 0.080 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[KLK6]] | B | VILL activity raises KLK6's level | lines that do not express VILL (16) vs lines expressing it (34) | 3.23× lower at baseline in the lines without VILL | 0.087 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[ALDH1L1]] | B | VILL activity raises ALDH1L1's level | lines that do not express VILL (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without VILL | 0.090 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[TMEM139]] | B | VILL activity raises TMEM139's level | lines that do not express VILL (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without VILL | 0.092 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.793). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.6, 50.9); signed map (62.8, 9.5). **Vector** length 53.0, 10.2% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +3.2 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.9 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.9 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.5 | -7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -4.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | villin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:37,988,059-38,007,188 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gelsolin/villins |
| Matched by | ensembl_id |

**Function**, from UniProt [O15195](https://www.uniprot.org/uniprotkb/O15195) (Villin-like protein):

> Possible tumor suppressor.

**Summary**, from NCBI Gene [50853](https://www.ncbi.nlm.nih.gov/gene/50853):

> The protein encoded by this gene belongs to the villin/gelsolin family. It contains 6 gelsolin-like repeats and a headpiece domain. It may play a role in actin-bundling. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30906) · Entrez [50853](https://www.ncbi.nlm.nih.gov/gene/50853) · UniProt [O15195](https://www.uniprot.org/uniprotkb/O15195) · Ensembl [ENSG00000136059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136059)

## Data

Gene col 5808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5808); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5808]; `tensor/DDL_lfc|DDL_z.npy` [5808]; `embed/gene_vectors.npy` [5808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5808 or target_col == 5808). Every well: [[VILL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VILL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
