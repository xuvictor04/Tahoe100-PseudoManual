---
symbol: "CEMIP"
type: "gene"
col: 2400
ensembl_id: "ENSG00000103888"
name: "cell migration inducing hyaluronidase 1"
location: "15q25.1"
module: 235
arm: "+"
pooled_cpm: 180.26
n_lines_expressing: 31
n_dd_up: 4
n_dd_down: 87
n_dd_up_clean: 4
n_dd_down_clean: 62
in_vector_space: true
direction_upstream: 31
direction_downstream: 41
tags: ["gene", "module/235"]
generated_by: "tahoemap"
---

# CEMIP

*cell migration inducing hyaluronidase 1* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Sapanisertib (drug)]] 5 µM: 2.13× (z +4.1, q 0.020, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 87 drug-doses (25 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.400× (z -9.6, q 3e-19, down in 26 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD17C]] (+0.72, fdr 7e-06, ⚠ same locus), [[IL33]] (+0.69, fdr 7e-06), [[DUSP4]] (+0.68, fdr 7e-06), [[EPHB6]] (+0.65, fdr 7e-06); moves opposite to [[CMKLR2]] (-0.50, fdr 3e-05), [[CHPT1]] (-0.48, fdr 4e-05).
> It is in [[Module 235]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[ABHD17C]] → it (grade B ⚠); 41 go from it, the strongest it → [[ABHD17C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2400.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | **2.13×** | +4.1 | 0.020 | 16/30 (NCI-H1573, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.01×** | +3.8 | 0.039 | 15/30 (NCI-H1573, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.94×** | +3.6 | 0.051 | 18/29 (NCI-H460, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **1.92×** | +3.6 | 0.051 | 8/29 (NCI-H1573, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.34× | +3.2 | 0.18 | 11/28 (CFPAC-1, COLO 205, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 88 in all, 25 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 87 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 25 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2400.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.400×** | -9.6 | 3e-19 | 26/29 (KATO III, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.414×** | -9.3 | 5e-18 | 22/29 (LS 180, KATO III, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.396×** | -9.0 | 4e-17 | 23/29 (BT-474, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.430×** | -8.5 | 2e-15 | 26/29 (BT-474, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM | ⚠ position correction uncertain | **0.434×** | -8.4 | 4e-15 | 22/28 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -8.1 | 6e-14 | 26/28 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.467×** | -8.0 | 1e-13 | 20/29 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.455×** | -8.0 | 1e-13 | 21/29 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.558×** | -7.9 | 3e-13 | 24/29 (BT-474, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.514×** | -7.7 | 6e-13 | 24/31 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.481×** | -7.7 | 8e-13 | 25/29 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.499×** | -7.3 | 1e-11 | 22/28 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.541×** | -7.1 | 4e-11 | 21/30 (SW480, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.507×** | -7.1 | 4e-11 | 24/30 (BT-474, SW480, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.509×** | -7.1 | 5e-11 | 20/29 (LS 180, LoVo, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.619×** | -7.1 | 5e-11 | 24/29 (C32, COLO 205, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.638×** | -6.6 | 1e-09 | 20/29 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.594×** | -6.5 | 2e-09 | 20/29 (BT-474, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.585×** | -5.6 | 5e-07 | 19/29 (LS 180, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2400. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 365 | 0 | 40 (10 ⚠) | — | [[Neratinib (drug)]] 5 µM 0.0203× (z -15.2) |
| [[KATO III (line)]] | alt | 1,184 | 0 | 30 (16 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0605× (z -26.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.0576× (z -19.2) |
| [[NCI-H1573 (line)]] | alt | 367 | 0 | 23 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0805× (z -18.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0531× (z -15.3) |
| [[LoVo (line)]] | wt | 347 | 0 | 21 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -15.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.192× (z -12.0) |
| [[LS 180 (line)]] | wt | 1,393 | 0 | 21 (16 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0632× (z -29.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0473× (z -23.3) |
| [[SW480 (line)]] | alt | 263 | 0 | 16 (8 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.199× (z -13.4) |
| [[HOP62 (line)]] | alt | 108 | 0 | 12 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0898× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 437 | 0 | 9 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0235× (z -16.2) |
| [[A549 (line)]] | wt | 328 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0355× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0359× (z -12.6) |
| [[Hs 766T (line)]] | wt | 545 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -17.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -11.1) |
| [[C32 (line)]] | wt | 131 | 0 | 5 (1 ⚠) | — | [[Radotinib (drug)]] 5 µM 0.217× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 249 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -10.7) |
| [[SW1417 (line)]] | alt | 510 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -9.8) |
| [[CHP-212 (line)]] | wt | 197 | 0 | 2 (2 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0134× (z -9.8) ⚠ position correction uncertain |
| [[COLO 205 (line)]] | alt | 173 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.210× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.120× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.149× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 62.3 | 0 | 2 (2 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.132× (z -10.1) ⚠ position correction uncertain |
| [[H4 (line)]] | wt | 158 | 0 | 1 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0572× (z -9.3) ⚠ position correction uncertain |
| [[SHP-77 (line)]] | alt | 161 | 1 | 0 | [[Budesonide (drug)]] 5 µM 4.34× (z +8.6) | — |
| [[A-172 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 28.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 183 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 463 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 30.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2400), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD17C]] | +0.72 | +0.72 / +0.73 | both halves | 7e-06 | ⚠ same locus (23.7 kb, same strand: neighbours can correlate without regulation) |
| [[IL33]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[DUSP4]] | +0.68 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[EPHB6]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ITGA2]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SHB]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SERPINE2]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[VSIG1]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ADGRE2]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.57 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[TMEM163]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMKLR2]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CHPT1]] | -0.48 | -0.40 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 22, C 9. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | ABHD17C activity raises CEMIP's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 5.17× lower at baseline in the lines without ABHD17C | 0.004 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[ST6GAL2]] | B | ST6GAL2 activity raises CEMIP's level | lines that do not express ST6GAL2 (39) vs lines expressing it (11) | 3.43× lower at baseline in the lines without ST6GAL2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC01456, MUC6 |
| [[PIWIL1]] | B | PIWIL1 activity raises CEMIP's level | lines that do not express PIWIL1 (38) vs lines expressing it (12) | 4.71× lower at baseline in the lines without PIWIL1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, CALB1, CLRN3 |
| [[CEACAM1]] | B | CEACAM1 activity raises CEMIP's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 4.09× lower at baseline in the lines without CEACAM1 | 0.013 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[CEACAM6]] | B | CEACAM6 activity raises CEMIP's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 5.26× lower at baseline in the lines without CEACAM6 | 0.023 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17 |
| [[SYT13]] | B | SYT13 activity raises CEMIP's level | lines that do not express SYT13 (33) vs lines expressing it (17) | 3.50× lower at baseline in the lines without SYT13 | 0.025 | ⚠ within organs, on part of the lines; also absent: SCEL, HS3ST1, FGFBP1 |
| [[SCAT1]] | B | SCAT1 activity raises CEMIP's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 3.43× lower at baseline in the lines without SCAT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[CAPN8]] | B | CAPN8 activity raises CEMIP's level | lines that do not express CAPN8 (35) vs lines expressing it (15) | 4.80× lower at baseline in the lines without CAPN8 | 0.035 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, ARHGEF38 |
| [[VSIG1]] | B | VSIG1 activity raises CEMIP's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 2.34× lower at baseline in the lines without VSIG1 | 0.036 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1 |
| [[PTGS2]] | B | PTGS2 activity raises CEMIP's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without PTGS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[CEACAM5]] | B | CEACAM5 activity raises CEMIP's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.75× lower at baseline in the lines without CEACAM5 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[TGFA]] | B | TGFA activity raises CEMIP's level | lines that do not express TGFA (17) vs lines expressing it (33) | 3.37× lower at baseline in the lines without TGFA | 0.073 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 33, C 8. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | CEMIP activity raises ABHD17C's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.96× lower at baseline in the lines without CEMIP | 0.001 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[LYPD3]] | B | CEMIP activity raises LYPD3's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without CEMIP | 0.011 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[ATP2B1]] | B | CEMIP activity raises ATP2B1's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without CEMIP | 0.012 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[DOCK5]] | B | CEMIP activity raises DOCK5's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without CEMIP | 0.013 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[TRIB2]] | B | CEMIP activity raises TRIB2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without CEMIP | 0.021 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[PLEKHM1P1]] | B | CEMIP activity raises PLEKHM1P1's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without CEMIP | 0.028 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[LIF]] | B | CEMIP activity raises LIF's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without CEMIP | 0.030 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[BACE2]] | B | CEMIP activity raises BACE2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.75× lower at baseline in the lines without CEMIP | 0.037 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| cells under [[Pimitespib (drug)]] 5 µM | B | CEMIP activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express CEMIP (19) vs lines expressing it (29) | the lines without CEMIP: 1.26× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[GOLGA7B]] | B | CEMIP activity raises GOLGA7B's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.08× lower at baseline in the lines without CEMIP | 0.042 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[ITPRID2]] | B | CEMIP activity raises ITPRID2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without CEMIP | 0.052 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[SMOX]] | B | CEMIP activity raises SMOX's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without CEMIP | 0.058 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |

## Where it sits

- **Module**: [[Module 235]]; 5 genes; every member is in the + arm (projection on the module's main direction 0.883). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.7, 6.5); signed map (16.4, 52.1). **Vector** length 130, 41.2% of its response variance represented; |z| ≥ 3 in 1,575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +11.4 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +10.8 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +9.3 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +7.1 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +0.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +3.2 | -2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.1 | +1.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.3 | -7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -7.8 | -9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.1 | -9.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -6.8 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.6 | -7.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -6.0 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | cell migration inducing hyaluronidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:80,779,343-80,951,776 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IR2155535, TMEM2L, HYBID, CEMIP1; previously KIAA1199 |
| Gene groups (HGNC) | Hyaluronidases |
| Reactome | 4 pathways, smallest: Hyaluronan degradation; Hyaluronan metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUJ3](https://www.uniprot.org/uniprotkb/Q8WUJ3) (Cell migration-inducing and hyaluronan-binding protein):

> Mediates depolymerization of hyaluronic acid (HA) via the cell membrane-associated clathrin-coated pit endocytic pathway. Binds to hyaluronic acid. Hydrolyzes high molecular weight hyaluronic acid to produce an intermediate-sized product, a process that may occur through rapid vesicle endocytosis and recycling without intracytoplasmic accumulation or digestion in lysosomes. Involved in hyaluronan catabolism in the dermis of the skin and arthritic synovium. Positively regulates …

**Summary**, from NCBI Gene [57214](https://www.ncbi.nlm.nih.gov/gene/57214):

> Enables several functions, including clathrin heavy chain binding activity; hyaluronic acid binding activity; and hyalurononglucosaminidase activity. Involved in several processes, including hyaluronan catabolic process; positive regulation of protein phosphorylation; and positive regulation of protein targeting to membrane. Located in several cellular components, including clathrin-coated endocytic vesicle; endoplasmic reticulum; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29213) · Entrez [57214](https://www.ncbi.nlm.nih.gov/gene/57214) · UniProt [Q8WUJ3](https://www.uniprot.org/uniprotkb/Q8WUJ3) · Ensembl [ENSG00000103888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103888)

## Data

Gene col 2400: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2400); `tables/drug_effects.parquet` (93 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2400, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2400]; `tensor/DDL_lfc|DDL_z.npy` [2400]; `embed/gene_vectors.npy` [2400]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2400 or target_col == 2400). Every well: [[CEMIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEMIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
