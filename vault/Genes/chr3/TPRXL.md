---
symbol: "TPRXL"
type: "gene"
col: 11108
ensembl_id: "ENSG00000180438"
name: "tetrapeptide repeat homeobox like (pseudogene)"
location: "3p25.1"
module: 55
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 18
n_dd_up: 29
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 27
direction_downstream: 30
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# TPRXL

*tetrapeptide repeat homeobox like (pseudogene)* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.70× (z +14.5, q 1e-44, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 4.87× (z +13.7, q 3e-40, up in 9 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Goserelin (acetate) (drug)]] 5 µM: 0.727× (z -4.0, q 0.042, down in 3 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 4 lines (KATO III 0.0512×, LoVo 0.0754×, COLO 205 0.0701×, LS 180 0.0849×); [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.137×, KATO III 0.198×, LoVo 0.237×, LS 180 0.188×); [[Panobinostat (drug)]] 5 µM in 3 lines (COLO 205 0.0194×, LoVo 0.0393×, KATO III 0.0663×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.151×, LoVo 0.137×, COLO 205 0.230×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPSR1]] (+0.89, fdr 7e-06), [[CALB1]] (+0.85, fdr 7e-06), [[HEPH]] (+0.82, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[CALB1]] → it (grade C ⚠); 30 go from it, the strongest it → [[KCTD14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.70×** | +14.5 | 1e-44 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.87×** | +13.7 | 3e-40 | 9/13 (RPMI-7951, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.86×** | +13.7 | 3e-40 | 2/9 (SW480, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +10.6 | 4e-24 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.62×** | +10.2 | 1e-22 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +9.9 | 3e-21 | 0/12 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +4.6 | 4e-04 | 2/14 (SW480, SW1417) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.68×** | +4.5 | 5e-04 | 0/7 | inconsistent across doses | position effect removed |
| [[Valdecoxib (drug)]] 0.05 µM |  | **1.66×** | +4.3 | 9e-04 | 1/12 (SW1417) | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.99×** | +4.2 | 0.001 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +4.2 | 0.002 | 4/13 (SW1417, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.94×** | +4.1 | 0.002 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.42×** | +4.0 | 0.003 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 2/14 (Hs 766T, RPMI-7951) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.005 | 3/11 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.010 | 0/11 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.010 | 1/13 (KATO III) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.011 | 2/14 (SW480, KATO III) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.016 | 0/14 | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.022 | 1/14 (SW480) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11108.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 4 lines (KATO III 0.0512×, LoVo 0.0754×, COLO 205 0.0701×, LS 180 0.0849×); [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.137×, KATO III 0.198×, LoVo 0.237×, LS 180 0.188×); [[Panobinostat (drug)]] 5 µM in 3 lines (COLO 205 0.0194×, LoVo 0.0393×, KATO III 0.0663×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.151×, LoVo 0.137×, COLO 205 0.230×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Goserelin (acetate) (drug)]] 5 µM |  | **0.727×** | -4.0 | 0.042 | 3/14 (HT-29, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -3.7 | 0.060 | 8/14 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.678× | -3.4 | 0.13 | 7/14 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.689× | -3.1 | 0.27 | 1/14 (hTERT-HPNE) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.687× | -3.0 | 0.27 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 18.7 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0393× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -13.6) |
| [[KATO III (line)]] | alt | 33.8 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0512× (z -15.4) |
| [[COLO 205 (line)]] | alt | 48.9 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0194× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.2) |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0849× (z -9.8) |
| [[A-172 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.687 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.815 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.400 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.824 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.743 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1]] | +0.89 | +0.89 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.85 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.82 | +0.81 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TPTEP1-1]] | +0.81 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.81 | +0.85 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LINC02474]] | +0.81 | +0.78 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.81 | +0.84 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.80 | +0.82 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.80 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[MUC17]] | +0.78 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LINC01559]] | +0.77 | +0.82 / +0.53 | both halves | 1e-05 |  |
| [[HNF4A]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 0, C 27. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALB1]] | C | CALB1 activity raises TPRXL's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 3.75× lower at baseline in the lines without CALB1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[UGT1A8]], [[UGT1A9]] | C | UGT1A8, UGT1A9 activity raises TPRXL's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 2.49× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.013 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[LINC02474]] | C | LINC02474 activity raises TPRXL's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 3.13× lower at baseline in the lines without LINC02474 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |
| [[PCK1]] | C | PCK1 activity raises TPRXL's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 2.90× lower at baseline in the lines without PCK1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |
| [[GALNT5]] | C | GALNT5 activity raises TPRXL's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without GALNT5 | 0.021 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises TPRXL's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.33× lower at baseline in the lines without LGR5 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises TPRXL's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.49× lower at baseline in the lines without UGT1A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises TPRXL's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.29× lower at baseline in the lines without UGT1A6 | 0.038 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises TPRXL's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without CYP4F11 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[ATP10B]] | C | ATP10B activity raises TPRXL's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 3.43× lower at baseline in the lines without ATP10B | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises TPRXL's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.42× lower at baseline in the lines without TFF2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |
| [[INPP5D]] | C | INPP5D activity raises TPRXL's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 2.61× lower at baseline in the lines without INPP5D | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 6, C 24. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCTD14]] | B | TPRXL activity raises KCTD14's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without TPRXL | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[ZNF503-AS1]] | B | TPRXL activity raises ZNF503-AS1's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 2.45× lower at baseline in the lines without TPRXL | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[PIWIL4]] | B | TPRXL activity raises PIWIL4's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 2.60× lower at baseline in the lines without TPRXL | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[SDCBP2]] | B | TPRXL activity raises SDCBP2's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 3.38× lower at baseline in the lines without TPRXL | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[BCAR3-AS1]] | B | TPRXL activity raises BCAR3-AS1's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 1.67× lower at baseline in the lines without TPRXL | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[FKBP9P1]] | B | TPRXL activity raises FKBP9P1's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 1.94× lower at baseline in the lines without TPRXL | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent |
| [[CLRN3]] | C | TPRXL activity raises CLRN3's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 2.74× lower at baseline in the lines without TPRXL | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent; co-absent with the target |
| [[IGFL2-AS1]] | C | TPRXL activity raises IGFL2-AS1's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 3.76× lower at baseline in the lines without TPRXL | 0.017 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent; co-absent with the target |
| [[LINC01559]] | C | TPRXL activity raises LINC01559's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 2.97× lower at baseline in the lines without TPRXL | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent; co-absent with the target |
| [[GPX2]] | C | TPRXL activity raises GPX2's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 3.70× lower at baseline in the lines without TPRXL | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent; co-absent with the target |
| [[UGT1A6]] | C | TPRXL activity raises UGT1A6's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 4.46× lower at baseline in the lines without TPRXL | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent; co-absent with the target |
| [[SLC5A1]] | C | TPRXL activity raises SLC5A1's level | lines that do not express TPRXL (32) vs lines expressing it (18) | 2.96× lower at baseline in the lines without TPRXL | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC01559, LGR6, CAPN8; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.840). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.7, 50.4); signed map (64.6, 8.3). **Vector** length 46.4, 14.9% of its response variance represented; |z| ≥ 3 in 375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tetrapeptide repeat homeobox like (pseudogene) |
| Locus type | pseudogene |
| Location | 3p25.1 — chr3:14,064,203-14,065,442 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | FLJ35107, TPRX3P |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Reactome | 2 pathways, smallest: Zygotic genome activation (ZGA); Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17RH7](https://www.uniprot.org/uniprotkb/Q17RH7) (Tetra-peptide repeat homeobox-like protein):

> Transcription factor required for zygotic genome activation (ZGA), a critical event in early embryonic development during which the developmental control passes from maternally provided mRNAs to the expression of the zygotic genome after fertilization. Protein produced from maternal transcripts that binds and activates expression of key ZGA marker genes, such as NANOGNB, ZSCAN4, DUXB, KLF5 and DPPA3. Binds to regulatory DNA sequences containing a 5'-TAATCC-3' sequence motif (By similarity).

**Summary**, from NCBI Gene [348825](https://www.ncbi.nlm.nih.gov/gene/348825):

> Homeobox genes encode DNA-binding proteins, many of which are thought to be involved in early embryonic development. Homeobox genes encode a DNA-binding domain of 60 to 63 amino acids referred to as the homeodomain. This pseudogene is a member of the TPRX homeobox gene family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:32178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32178) · Entrez [348825](https://www.ncbi.nlm.nih.gov/gene/348825) · UniProt [Q17RH7](https://www.uniprot.org/uniprotkb/Q17RH7) · Ensembl [ENSG00000180438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180438)

## Data

Gene col 11108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11108); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11108]; `tensor/DDL_lfc|DDL_z.npy` [11108]; `embed/gene_vectors.npy` [11108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11108 or target_col == 11108). Every well: [[TPRXL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPRXL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
