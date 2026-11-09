---
symbol: "GDNF-AS1"
type: "gene"
col: 14552
ensembl_id: "ENSG00000248587"
name: "GDNF antisense RNA 1"
location: "5p13.2"
module: 13
arm: "+"
pooled_cpm: 2.91
n_lines_expressing: 27
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 27
direction_downstream: 22
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# GDNF-AS1

*GDNF antisense RNA 1* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.12× (z +22.3, q 0e+00, up in 10 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.612× (z -4.3, q 0.012, down in 0 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0825×, RPMI-7951 0.0877×; ⚠ cell-cycle shift, explains ~91% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0883×, C32 0.160×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.163×, HS-578T 0.105×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HS-578T 0.0506×); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (HOP62 0.0536×); [[Dexamethasone (drug)]] 0.5 µM in 1 line (HOP62 0.0922×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDNF]] (+0.82, fdr 7e-06, ⚠ same locus), [[SYNDIG1]] (+0.78, fdr 7e-06), [[APCDD1L]] (+0.69, fdr 7e-06), [[NTNG2]] (+0.68, fdr 1e-05); moves opposite to [[SRGN]] (-0.49, fdr 3e-05), [[KIF13B]] (-0.49, fdr 6e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[DIRAS3]] → it (grade B ⚠); 22 go from it, the strongest it → [[SLCO1C1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14552.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.12×** | +22.3 | 0e+00 | 10/11 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.70×** | +14.6 | 1e-45 | 1/6 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +10.6 | 9e-24 | 3/13 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.39×** | +9.8 | 1e-20 | 1/5 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +9.8 | 2e-20 | 1/7 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +6.5 | 7e-09 | 4/10 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +6.3 | 2e-08 | 4/11 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.0 | 5e-05 | 2/18 (NCI-H460, C32) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.18×** | +4.8 | 8e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.4 | 8e-04 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.002 | 3/13 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.87×** | +3.9 | 0.005 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +3.6 | 0.016 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.024 | 2/15 (SK-MEL-2, A-172) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +3.3 | 0.032 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.032 | 6/16 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.069 | 0/10 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0825×, RPMI-7951 0.0877×; ⚠ cell-cycle shift, explains ~91% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0883×, C32 0.160×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 0.163×, HS-578T 0.105×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HS-578T 0.0506×); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (HOP62 0.0536×); [[Dexamethasone (drug)]] 0.5 µM in 1 line (HOP62 0.0922×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.612×** | -4.3 | 0.012 | 0/18 | inconsistent across doses |  |
| [[Captopril (drug)]] 0.5 µM |  | 0.682× | -3.3 | 0.26 | 3/17 (SW 900, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.693× | -3.2 | 0.27 | 8/20 (HS-578T, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.689× | -3.1 | 0.27 | 2/18 (H4, J82) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 29.4 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0415× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0506× (z -12.7) |
| [[C32 (line)]] | wt | 48.9 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0877× (z -9.9) ⚠ cell-cycle shift, explains ~91% of this change |
| [[HOP62 (line)]] | alt | 5.53 | 0 | 2 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0536× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 0.967 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.7× (z +10.3) | — |
| [[A-172 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.774 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.908 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.768 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.770 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.625 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.510 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDNF]] | +0.82 | +0.84 / +0.84 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SYNDIG1]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[NTNG2]] | +0.68 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[BAALC]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[GPR68]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SAMD3]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[RFX8]] | +0.64 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[TSHZ3-AS1]] | +0.63 | +0.62 / +0.57 | both halves | 8e-06 | same gene group |
| [[SLC14A2]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[KIF13B]] | -0.49 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 8, C 19. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRAS3]] | B | DIRAS3 activity raises GDNF-AS1's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 1.60× lower at baseline in the lines without DIRAS3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB |
| [[VEPH1]] | B | VEPH1 activity raises GDNF-AS1's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without VEPH1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[TOP2A]] | B | TOP2A activity lowers GDNF-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COL5A3]] | B | COL5A3 activity raises GDNF-AS1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 1.88× lower at baseline in the lines without COL5A3 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[CSF1R]] | B | CSF1R activity raises GDNF-AS1's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without CSF1R | 0.070 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[SPOCD1]] | B | SPOCD1 activity raises GDNF-AS1's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without SPOCD1 | 0.082 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[LINC02813]] | B | LINC02813 activity raises GDNF-AS1's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without LINC02813 | 0.085 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[ANXA10]] | B | ANXA10 activity raises GDNF-AS1's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 1.63× lower at baseline in the lines without ANXA10 | 0.099 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[GDNF]] | C | GDNF activity raises GDNF-AS1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 4.60× lower at baseline in the lines without GDNF | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises GDNF-AS1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 2.51× lower at baseline in the lines without COL15A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[DENND2A]] | C | DENND2A activity raises GDNF-AS1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.07× lower at baseline in the lines without DENND2A | 0.008 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises GDNF-AS1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.59× lower at baseline in the lines without PDGFRB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 7, C 15. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO1C1]] | B | GDNF-AS1 activity raises SLCO1C1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without GDNF-AS1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[THBS2-AS1]] | B | GDNF-AS1 activity raises THBS2-AS1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without GDNF-AS1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[LINC01119]] | B | GDNF-AS1 activity raises LINC01119's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 1.74× lower at baseline in the lines without GDNF-AS1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[VEPH1]] | B | GDNF-AS1 activity raises VEPH1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without GDNF-AS1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[C2orf92]] | B | GDNF-AS1 activity raises C2orf92's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without GDNF-AS1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | GDNF-AS1 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express GDNF-AS1 (23) vs lines expressing it (25) | the lines without GDNF-AS1: 1.33× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[RFX8]] | B | GDNF-AS1 activity raises RFX8's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.70× lower at baseline in the lines without GDNF-AS1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[COL15A1]] | C | GDNF-AS1 activity raises COL15A1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.84× lower at baseline in the lines without GDNF-AS1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[MEG3]] | C | GDNF-AS1 activity raises MEG3's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 3.02× lower at baseline in the lines without GDNF-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[HS3ST3A1]] | C | GDNF-AS1 activity raises HS3ST3A1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 5.27× lower at baseline in the lines without GDNF-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[CARMN]] | C | GDNF-AS1 activity raises CARMN's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.56× lower at baseline in the lines without GDNF-AS1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[TWIST2]] | C | GDNF-AS1 activity raises TWIST2's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 4.28× lower at baseline in the lines without GDNF-AS1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.4, 16.0); signed map (23.5, 47.1). **Vector** length 49.1, 13.0% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NCAM1 interactions* (reactome, mean cos +0.53 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +22.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.8 | +2.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | GDNF antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p13.2 — chr5:37,811,589-37,953,827 (+) |
| Ensembl biotype | lncRNA |
| Also known as | GDNFOS; previously LINC02110 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43592) · Entrez [100861519](https://www.ncbi.nlm.nih.gov/gene/100861519) · Ensembl [ENSG00000248587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248587)

## Data

Gene col 14552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14552); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14552]; `tensor/DDL_lfc|DDL_z.npy` [14552]; `embed/gene_vectors.npy` [14552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14552 or target_col == 14552). Every well: [[GDNF-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDNF-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
