---
symbol: "NEIL3"
type: "gene"
col: 3070
ensembl_id: "ENSG00000109674"
name: "nei like DNA glycosylase 3"
location: "4q34.3"
module: 67
arm: "+"
pooled_cpm: 22.09
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# NEIL3

*nei like DNA glycosylase 3* — 4q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Darinaparsin (drug)]] 5 µM: 1.40× (z +6.3, q 2e-07, up in 27 of 46 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +4.1, q 0.009, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.612× (z -9.2, q 2e-17, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBK]] (+0.90, fdr 7e-06), [[UBE2T]] (+0.89, fdr 7e-06), [[CIT]] (+0.89, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.40×** | +6.3 | 2e-07 | 27/46 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.38×** | +4.3 | 0.005 | 13/45 (A549, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.009 | 22/46 (NCI-H2347, RKO, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.75×** | +3.9 | 0.011 | 15/42 (J82, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.018 | 14/46 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.034 | 16/46 (NCI-H23, J82, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.3 | 0.083 | 11/46 (KATO III, hTERT-HPNE, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.28× | +3.2 | 0.10 | 8/45 (NCI-H2347, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | 1.25× | +3.1 | 0.10 | 16/41 (SHP-77, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.10 | 9/45 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.25× | +3.1 | 0.10 | 11/46 (KATO III, A549, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.25× | +3.1 | 0.10 | 11/46 (KATO III, A549, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.25× | +3.0 | 0.11 | 8/46 (A498, KATO III, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.612×** | -9.2 | 2e-17 | 29/44 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.544×** | -8.2 | 8e-14 | 28/45 (HOP62, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.494×** | -7.7 | 3e-12 | 30/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.506×** | -7.4 | 2e-11 | 33/45 (A498, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -7.1 | 1e-10 | 23/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -7.0 | 3e-10 | 26/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.719×** | -6.2 | 6e-08 | 27/46 (A498, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.636×** | -6.1 | 9e-08 | 22/45 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.580×** | -5.8 | 3e-07 | 24/45 (HCT15, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.662×** | -5.5 | 2e-06 | 22/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -5.2 | 9e-06 | 20/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.623×** | -5.2 | 1e-05 | 19/44 (MIA PaCa-2, HCT15, …) | two highest doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.615×** | -4.7 | 1e-04 | 21/46 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.790×** | -4.4 | 4e-04 | 18/46 (HCT15, RKO, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.732×** | -4.2 | 0.001 | 19/46 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.804×** | -4.1 | 0.002 | 18/46 (NCI-H1573, A-427, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.571×** | -3.9 | 0.003 | 19/44 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.705×** | -3.7 | 0.006 | 17/45 (HCT15, SW 1088, …) | all doses, flat | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.622×** | -3.3 | 0.024 | 14/41 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -3.3 | 0.027 | 20/46 (A-427, A498, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.745×** | -3.2 | 0.034 | 11/45 (SW480, A549, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 62.0 | 0 | 7 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0765× (z -23.2) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.173× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 60.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -13.8) |
| [[H4 (line)]] | wt | 35.4 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0966× (z -14.1) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.161× (z -11.0) |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.182× (z -11.6) |
| [[SW480 (line)]] | alt | 21.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.0) |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.162× (z -11.9) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.8) |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.3) |
| [[A-172 (line)]] | wt | 18.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0760× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.7) |
| [[A549 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.132× (z -17.0) ⚠ cell-cycle shift, explains ~87% of this change |
| [[LoVo (line)]] | wt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.236× (z -9.2) ⚠ cell-cycle shift, explains ~87% of this change |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0956× (z -17.0) |
| [[SW48 (line)]] | wt | 27.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.155× (z -8.6) |
| [[A-427 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBK]] | +0.90 | +0.89 / +0.87 | both halves | 7e-06 | STRING 557 |
| [[UBE2T]] | +0.89 | +0.89 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[CIT]] | +0.89 | +0.88 / +0.84 | both halves | 7e-06 |  |
| [[KIF15]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | STRING 650 |
| [[PARPBP]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | STRING 491 |
| [[NCAPH]] | +0.86 | +0.82 / +0.84 | both halves | 7e-06 | STRING 483 |
| [[CENPI]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | STRING 486 |
| [[AURKB]] | +0.86 | +0.84 / +0.82 | both halves | 7e-06 | STRING 413 |
| [[BUB1B]] | +0.85 | +0.87 / +0.80 | both halves | 7e-06 | STRING 637 |
| [[TTK]] | +0.84 | +0.79 / +0.85 | both halves | 7e-06 | STRING 630 |
| [[SKA3]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | STRING 503 |
| [[NUF2]] | +0.84 | +0.83 / +0.80 | both halves | 7e-06 | STRING 549 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises NEIL3's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without E2F8 | 0.022 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[PIMREG]] | B | PIMREG activity raises NEIL3's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without PIMREG | 0.039 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises NEIL3's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without NEURL1B | 0.040 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[ABL1]] | B | ABL1 activity lowers NEIL3's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.0% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NDC80]] | C | NDC80 activity raises NEIL3's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.09× lower at baseline in the lines without NDC80 | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises NEIL3's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.51× lower at baseline in the lines without C21orf58, SKA3 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |
| [[SHMT1]] | C | SHMT1 activity raises NEIL3's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.53× lower at baseline in the lines without SHMT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.902). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.3, -53.2); signed map (-46.0, -40.8). **Vector** length 130, 37.4% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.80 to 12); *G2/M checkpoint* (hallmark, mean cos +0.78 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.77 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | +4.0 | +4.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.9 | +6.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.5 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +2.2 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.9 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -5.2 | -6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | nei like DNA glycosylase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.3 — chr4:177,309,874-177,362,936 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10858, hFPG2, FPG2, hNEI3, ZGRF3 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; Zinc fingers GRF-type; DNA glycosylases; DNA-(apurinic or apyrimidinic site) lyases |
| Reactome | 11 pathways, smallest: Diseases of Base Excision Repair; Cleavage of the damaged purine; Depurination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAT5](https://www.uniprot.org/uniprotkb/Q8TAT5) (Endonuclease 8-like 3):

> DNA glycosylase which prefers single-stranded DNA (ssDNA), or partially ssDNA structures such as bubble and fork structures, to double-stranded DNA (dsDNA). Mediates interstrand cross-link repair in response to replication stress: acts by mediating DNA glycosylase activity, cleaving one of the two N-glycosyl bonds comprising the interstrand cross-link, which avoids the formation of a double-strand break but generates an abasic site that is bypassed by translesion synthesis polymerases (By …

**Summary**, from NCBI Gene [55247](https://www.ncbi.nlm.nih.gov/gene/55247):

> NEIL3 belongs to a class of DNA glycosylases homologous to the bacterial Fpg/Nei family. These glycosylases initiate the first step in base excision repair by cleaving bases damaged by reactive oxygen species and introducing a DNA strand break via the associated lyase reaction (Bandaru et al., 2002 [PubMed 12509226]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24573) · Entrez [55247](https://www.ncbi.nlm.nih.gov/gene/55247) · UniProt [Q8TAT5](https://www.uniprot.org/uniprotkb/Q8TAT5) · Ensembl [ENSG00000109674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109674)

## Data

Gene col 3070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3070); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3070]; `tensor/DDL_lfc|DDL_z.npy` [3070]; `embed/gene_vectors.npy` [3070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3070 or target_col == 3070). Every well: [[NEIL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEIL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
