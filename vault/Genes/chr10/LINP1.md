---
symbol: "LINP1"
type: "gene"
col: 13363
ensembl_id: "ENSG00000223784"
name: "lncRNA in non-homologous end joining pathway 1"
location: "10p14"
module: 34
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 21
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 26
direction_downstream: 21
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# LINP1

*lncRNA in non-homologous end joining pathway 1* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 11.0× (z +16.2, q 0e+00, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.34× (z +6.0, q 4e-07, up in 7 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.105×, NCI-H1573 0.0972×, NCI-H460 0.115×, A549 0.159×; ⚠ cell-cycle shift, explains ~81% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.309×, KATO III 0.216×); [[Panobinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.0561×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0590×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (A-172 0.0978×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01589]] (+0.58, fdr 1e-05), [[TMEM154]] (+0.54, fdr 2e-05), [[SCEL]] (+0.54, fdr 2e-05); moves opposite to [[ALDH6A1]] (-0.42, fdr 6e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[LAMA3]] → it (grade B ⚠); 21 go from it, the strongest it → [[CCDC9B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.0×** | +16.2 | 0e+00 | 5/5 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.05×** | +13.7 | 2e-40 | 12/13 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.51×** | +12.2 | 1e-31 | 7/7 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.34×** | +6.0 | 4e-07 | 7/16 (KATO III, A-172, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.39×** | +5.9 | 5e-07 | 7/14 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.15×** | +5.4 | 8e-06 | 4/12 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.99×** | +5.3 | 1e-05 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.6 | 3e-04 | 1/15 (A498) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.87×** | +4.4 | 8e-04 | 2/15 (A498, Hs 766T) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.4 | 8e-04 | 3/17 (A-172, NCI-H1792, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.22×** | +3.8 | 0.006 | 2/13 (NCI-H1573, CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +3.6 | 0.013 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.6 | 0.013 | 1/15 (Panc 03.27) | top dose only | cell-cycle shift (explains ~24% here) |
| [[vincristine (drug)]] 0.5 µM |  | **2.01×** | +3.4 | 0.032 | 4/15 (LS 180, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.87×** | +3.0 | 0.099 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13363.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (KATO III 0.105×, NCI-H1573 0.0972×, NCI-H460 0.115×, A549 0.159×; ⚠ cell-cycle shift, explains ~81% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.309×, KATO III 0.216×); [[Panobinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.0561×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0590×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (A-172 0.0978×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.386× | -3.5 | 0.24 | 9/16 (NCI-H1792, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 13.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0561× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0590× (z -14.8) |
| [[KATO III (line)]] | alt | 6.87 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -12.7) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -8.6) |
| [[A-172 (line)]] | wt | 5.66 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0978× (z -8.7) |
| [[A549 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -12.0) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H1573 (line)]] | alt | 5.35 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -12.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H460 (line)]] | wt | 3.50 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -12.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-427 (line)]] | wt | 0.204 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.795 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.334 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01589]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TMEM154]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SCEL]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[LINC01322]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[LINC00707]] | +0.52 | +0.53 / +0.49 | both halves | 2e-05 | ⚠ same locus (39.0 kb, same strand: neighbours can correlate without regulation) |
| [[PLCXD2]] | +0.50 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[CHST9]] | +0.47 | +0.52 / +0.32 | both halves | 2e-04 |  |
| [[CHMP1B-AS1]] | +0.46 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[LAMC2]] | +0.45 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[ZBED2]] | +0.45 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[OSBPL10]] | +0.45 | +0.37 / +0.46 | both halves | 9e-05 |  |
| [[COL4A5]] | +0.44 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[GPR39]] | +0.44 | +0.41 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH6A1]] | -0.42 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 8, C 18. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | LAMA3 activity raises LINP1's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without LAMA3 | 0.023 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[PLEKHA6]] | B | PLEKHA6 activity raises LINP1's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.73× lower at baseline in the lines without PLEKHA6 | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[GALNT14]] | B | GALNT14 activity raises LINP1's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.68× lower at baseline in the lines without GALNT14 | 0.040 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[PLCXD2]] | B | PLCXD2 activity raises LINP1's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 1.94× lower at baseline in the lines without PLCXD2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |
| [[CCDC9B]] | B | CCDC9B activity raises LINP1's level | lines that do not express CCDC9B (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without CCDC9B | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC02220, COL16A1, CD22 |
| [[PCED1B]] | B | PCED1B activity raises LINP1's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.16× lower at baseline in the lines without PCED1B | 0.077 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[SH2D3A]] | B | SH2D3A activity raises LINP1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.60× lower at baseline in the lines without SH2D3A | 0.082 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[IL1RN]] | B | IL1RN activity raises LINP1's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 1.54× lower at baseline in the lines without IL1RN | 0.092 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[LINC00707]] | C | LINC00707 activity raises LINP1's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 2.90× lower at baseline in the lines without LINC00707 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises LINP1's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.20× lower at baseline in the lines without CYP4F11 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[LASTR]] | C | LASTR activity raises LINP1's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without LASTR | 0.018 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent; co-absent with the target |
| [[LINC01589]] | C | LINC01589 activity raises LINP1's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 2.09× lower at baseline in the lines without LINC01589 | 0.020 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 7, C 14. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC9B]] | B | LINP1 activity raises CCDC9B's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without LINP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[ITGA6]] | B | LINP1 activity raises ITGA6's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without LINP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[BACH1]] | B | LINP1 activity raises BACH1's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without LINP1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[PLCXD2]] | B | LINP1 activity raises PLCXD2's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 1.80× lower at baseline in the lines without LINP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[LINC00887]] | B | LINP1 activity raises LINC00887's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.07× lower at baseline in the lines without LINP1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[LAMA3]] | B | LINP1 activity raises LAMA3's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without LINP1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[PCED1B]] | B | LINP1 activity raises PCED1B's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without LINP1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[LINC00707]] | C | LINP1 activity raises LINC00707's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 4.63× lower at baseline in the lines without LINP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |
| [[FGFBP1]] | C | LINP1 activity raises FGFBP1's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.45× lower at baseline in the lines without LINP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |
| [[LINC01589]] | C | LINP1 activity raises LINC01589's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.34× lower at baseline in the lines without LINP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |
| [[LINC02742]] | C | LINP1 activity raises LINC02742's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.90× lower at baseline in the lines without LINP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |
| [[CYP4F11]] | C | LINP1 activity raises CYP4F11's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.80× lower at baseline in the lines without LINP1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.0, 14.9); signed map (10.1, 39.6). **Vector** length 37.7, 8.61% of its response variance represented; |z| ≥ 3 in 358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +16.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | lncRNA in non-homologous end joining pathway 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p14 — chr10:6,709,530-6,740,532 (+) |
| Ensembl biotype | lncRNA |
| Also known as | PARROT; previously LINC00707 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53170) · Entrez [108570035](https://www.ncbi.nlm.nih.gov/gene/108570035) · Ensembl [ENSG00000223784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223784)

## Data

Gene col 13363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13363); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13363]; `tensor/DDL_lfc|DDL_z.npy` [13363]; `embed/gene_vectors.npy` [13363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13363 or target_col == 13363). Every well: [[LINP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LINP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
