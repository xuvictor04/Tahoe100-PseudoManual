---
symbol: "SAMD5"
type: "gene"
col: 12782
ensembl_id: "ENSG00000203727"
name: "sterile alpha motif domain containing 5"
location: "6q24.3"
module: 155
arm: "+"
pooled_cpm: 45.8
n_lines_expressing: 35
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# SAMD5

*sterile alpha motif domain containing 5* — 6q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.25× (z +19.6, q 0e+00, up in 28 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.693× (z -8.8, q 9e-16, down in 20 of 33 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 0.777× (z -4.3, q 0.003, down in 12 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.240×, NCI-H1573 0.147×, BT-474 0.0742×; ⚠ cell-cycle shift, explains ~63% of this change); [[Neratinib (drug)]] 0.05 µM in 1 line (BT-474 0.0180×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (BT-474 0.0216×); [[Gefitinib (drug)]] 5 µM in 1 line (BT-474 0.0217×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CES1]] (+0.57, fdr 2e-05), [[CEACAM5]] (+0.55, fdr 4e-05), [[MUC5AC]] (+0.54, fdr 3e-05); moves opposite to [[ZNF451]] (-0.42, fdr 9e-05), [[GANC]] (-0.41, fdr 3e-04), [[ZNF862]] (-0.41, fdr 1e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C2CD4A]] → it (grade B ⚠); 2 go from it, the strongest it → [[RGS6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.25×** | +19.6 | 0e+00 | 28/33 (KATO III, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.16×** | +13.1 | 5e-37 | 24/33 (NCI-H2030, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.16×** | +13.1 | 5e-37 | 27/33 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +12.3 | 1e-32 | 18/33 (KATO III, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +11.2 | 6e-27 | 17/32 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +10.8 | 4e-25 | 21/33 (SK-MEL-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.39×** | +7.9 | 2e-13 | 20/33 (C32, LoVo, …) | top dose only | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +6.5 | 5e-09 | 18/34 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 6e-06 | 16/32 (NCI-H2030, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +5.1 | 2e-05 | 15/32 (COLO 205, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.4 | 6e-04 | 14/32 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.3 | 8e-04 | 12/32 (HT-29, C32, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.006 | 13/34 (LoVo, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.037 | 6/33 (C32, RKO, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.052 | 9/32 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.060 | 7/32 (A-172, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.060 | 7/33 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12782.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.240×, NCI-H1573 0.147×, BT-474 0.0742×; ⚠ cell-cycle shift, explains ~63% of this change); [[Neratinib (drug)]] 0.05 µM in 1 line (BT-474 0.0180×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (BT-474 0.0216×); [[Gefitinib (drug)]] 5 µM in 1 line (BT-474 0.0217×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.693×** | -8.8 | 9e-16 | 20/33 (LoVo, NCI-H1573, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -5.3 | 4e-05 | 19/32 (CHP-212, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.736×** | -5.2 | 4e-05 | 17/30 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.777×** | -4.3 | 0.003 | 12/32 (BT-474, LS 180, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.661×** | -3.7 | 0.027 | 14/34 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 85.9 | 0 | 50 (10 ⚠) | — | [[Neratinib (drug)]] 0.05 µM 0.0180× (z -17.3) |
| [[NCI-H23 (line)]] | alt | 34.6 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 221 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HepG2_C3A (line)]] | wt | 62.7 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 83.8 | 2 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.50× (z +12.4) | [[Docetaxel (drug)]] 0.05 µM 0.310× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~49% of this change |
| [[NCI-H1573 (line)]] | alt | 59.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -17.5) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.245× (z -9.1) |
| [[LS 180 (line)]] | wt | 412 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.343× (z -10.8) |
| [[C32 (line)]] | wt | 48.8 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.14× (z +10.8) | — |
| [[LoVo (line)]] | wt | 293 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -22.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.223× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 12.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.80× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 55.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.67× (z +9.2) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.8) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.88× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.3) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A-172 (line)]] | wt | 22.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.97× (z +9.4) | — |
| [[A498 (line)]] | wt | 20.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 18.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.95× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0584× (z -11.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 21.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.24× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 57.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -8.5) ⚠ toxic |
| [[J82 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -8.6) ⚠ cell-cycle shift, explains ~97% of this change |
| [[LOX-IMVI (line)]] | wt | 17.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.97× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 28.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.85× (z +9.3) | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0294× (z -10.6) ⚠ cell-cycle shift, explains ~97% of this change |
| [[A-427 (line)]] | wt | 7.40 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.99 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CES1]] | +0.57 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[CEACAM5]] | +0.55 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[MUC5AC]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[CAPN8]] | +0.53 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[CEACAM6]] | +0.53 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[IL1RN]] | +0.52 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[SPTSSB]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[LPAR3]] | +0.50 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[LINC01440]] | +0.49 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[KRT18]] | +0.49 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[HS6ST3]] | +0.49 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[RGS6]] | +0.49 | +0.40 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF451]] | -0.42 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[GANC]] | -0.41 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[ZNF862]] | -0.41 | -0.32 / -0.36 | both halves | 1e-04 |  |
| [[WHAMMP3]] | -0.40 | -0.40 / -0.24 | both halves | 4e-04 |  |
| [[RBKS]] | -0.40 | -0.32 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2CD4A]] | B | C2CD4A activity raises SAMD5's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 3.39× lower at baseline in the lines without C2CD4A | 0.038 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[IL1RN]] | B | IL1RN activity raises SAMD5's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.42× lower at baseline in the lines without IL1RN | 0.052 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[CEACAM5]] | B | CEACAM5 activity raises SAMD5's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 3.43× lower at baseline in the lines without CEACAM5 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS6]] | B | SAMD5 activity raises RGS6's level | lines that do not express SAMD5 (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without SAMD5 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000287976, ENSG00000227681, TSPAN7 |
| [[EIF5A2]] | B | SAMD5 activity lowers EIF5A2's level | lines that do not express SAMD5 (15) vs lines expressing it (35) | 1.46× higher at baseline in the lines without SAMD5 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000287976, ENSG00000227681, TSPAN7 |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.2, 57.9); signed map (56.5, 22.4). **Vector** length 98.9, 23.0% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +19.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +13.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | +4.3 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | -0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.3 — chr6:147,508,690-147,737,547 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ875H10.1 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Matched by | ensembl_id |

UniProt [Q5TGI4](https://www.uniprot.org/uniprotkb/Q5TGI4) carries no function annotation.

**Summary**, from NCBI Gene [389432](https://www.ncbi.nlm.nih.gov/gene/389432):

> Predicted to be involved in regulation of intracellular signal transduction. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21180) · Entrez [389432](https://www.ncbi.nlm.nih.gov/gene/389432) · UniProt [Q5TGI4](https://www.uniprot.org/uniprotkb/Q5TGI4) · Ensembl [ENSG00000203727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203727)

## Data

Gene col 12782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12782); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12782]; `tensor/DDL_lfc|DDL_z.npy` [12782]; `embed/gene_vectors.npy` [12782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12782 or target_col == 12782). Every well: [[SAMD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
