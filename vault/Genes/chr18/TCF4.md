---
symbol: "TCF4"
type: "gene"
col: 12250
ensembl_id: "ENSG00000196628"
name: "transcription factor 4"
location: "18q21.2"
module: 19
arm: "+"
pooled_cpm: 75.29
n_lines_expressing: 25
n_dd_up: 4
n_dd_down: 44
n_dd_up_clean: 1
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 25
direction_downstream: 39
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TCF4

*transcription factor 4* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.74× (z +8.7, q 1e-15, up in 7 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.22× (z +4.5, q 0.001, up in 5 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.03×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.40×; ⚠ position not correctable); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 2.39×).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.578× (z -8.6, q 4e-15, down in 18 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE3A]] (+0.77, fdr 7e-06), [[FGF14]] (+0.70, fdr 7e-06), [[NALF1]] (+0.70, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[CDH13]] → it (grade C ⚠); 39 go from it, the strongest it → cells under [[Daptomycin (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.03×); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 1.40×; ⚠ position not correctable); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 2.39×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +8.7 | 1e-15 | 7/24 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.6 | 9e-12 | 6/22 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +5.2 | 4e-05 | 5/22 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.5 | 0.001 | 5/23 (NCI-H23, Panc 03.27, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.27 | 2/23 (A-172, SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.578×** | -8.6 | 4e-15 | 18/23 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.600×** | -8.0 | 3e-13 | 17/23 (SHP-77, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.615×** | -7.6 | 5e-12 | 17/23 (SHP-77, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.633×** | -7.2 | 9e-11 | 15/23 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.734×** | -6.8 | 9e-10 | 18/23 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -6.6 | 3e-09 | 13/23 (NCI-H460, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -6.0 | 1e-07 | 20/23 (SHP-77, NCI-H460, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.683×** | -6.0 | 1e-07 | 8/22 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.763×** | -6.0 | 1e-07 | 14/23 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.687×** | -5.9 | 2e-07 | 11/23 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -5.9 | 2e-07 | 10/23 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.781×** | -5.5 | 2e-06 | 12/23 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.786×** | -5.3 | 4e-06 | 11/23 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.723×** | -5.1 | 1e-05 | 6/23 (HOP62, SHP-77, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.556×** | -4.8 | 5e-05 | 12/23 (LOX-IMVI, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.560×** | -4.8 | 7e-05 | 16/24 (A-427, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 175 | 0 | 22 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -21.8) |
| [[SHP-77 (line)]] | alt | 656 | 0 | 19 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -20.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.5) |
| [[SNU-1 (line)]] | wt | 789 | 0 | 19 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0659× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.128× (z -20.0) |
| [[NCI-H1792 (line)]] | alt | 160 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -16.1) |
| [[CHP-212 (line)]] | wt | 1,548 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -20.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.109× (z -16.2) |
| [[hTERT-HPNE (line)]] | wt | 296 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 336 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -18.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.304× (z -12.9) |
| [[HOP62 (line)]] | alt | 103 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -13.3) |
| [[A-172 (line)]] | wt | 133 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.5) | [[Bortezomib (drug)]] 0.05 µM 0.353× (z -10.2) |
| [[A-427 (line)]] | wt | 165 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.117× (z -12.6) |
| [[H4 (line)]] | wt | 167 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.286× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 68.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.3) |
| [[AN3 CA (line)]] | alt | 87.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 46.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -17.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.66 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.76 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.69 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.78 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE3A]] | +0.77 | +0.68 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[FGF14]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[NALF1]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[PDE4B]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[PDE7B]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[TENM2]] | +0.66 | +0.57 / +0.66 | both halves | 9e-06 | **novel candidate** |
| [[SGIP1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CDH7]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ADGRB3]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[KCNH5]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LSAMP]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ADAMTS6]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 0, C 25. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH13]] | C | CDH13 activity raises TCF4's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 5.82× lower at baseline in the lines without CDH13 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises TCF4's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 12.22× lower at baseline in the lines without NETO1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[NDNF]] | C | NDNF activity raises TCF4's level | lines that do not express NDNF (25) vs lines expressing it (25) | 4.90× lower at baseline in the lines without NDNF | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[ACSS3]] | C | ACSS3 activity raises TCF4's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 3.74× lower at baseline in the lines without ACSS3 | 0.015 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[HGF]] | C | HGF activity raises TCF4's level | lines that do not express HGF (38) vs lines expressing it (12) | 4.12× lower at baseline in the lines without HGF | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |
| [[KCNK2]] | C | KCNK2 activity raises TCF4's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 4.49× lower at baseline in the lines without KCNK2 | 0.019 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[TMEM200A]] | C | TMEM200A activity raises TCF4's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 3.25× lower at baseline in the lines without TMEM200A | 0.024 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |
| [[ZNF804A]] | C | ZNF804A activity raises TCF4's level | lines that do not express ZNF804A (31) vs lines expressing it (19) | 5.06× lower at baseline in the lines without ZNF804A | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, CARMN, PAPPA; co-absent with the target |
| [[LINC01684]] | C | LINC01684 activity raises TCF4's level | lines that do not express LINC01684 (30) vs lines expressing it (20) | 5.23× lower at baseline in the lines without LINC01684 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IRAG2, COL3A1, LINC01592; maybe low, not absent; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises TCF4's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 5.18× lower at baseline in the lines without CDH12 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[SAMD3]] | C | SAMD3 activity raises TCF4's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.84× lower at baseline in the lines without SAMD3 | 0.046 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises TCF4's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 5.37× lower at baseline in the lines without PAPPA | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 6, C 33. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Daptomycin (drug)]] 5 µM | B | TCF4 activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express TCF4 (25) vs lines expressing it (23) | the lines without TCF4: 1.21× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; cell counts less trustworthy |
| cells under [[Ouabain (Octahydrate) (drug)]] 5 µM | B | TCF4 activity lowers the cells' numbers under Ouabain (Octahydrate) 5 µM (makes them more sensitive) | lines that do not express TCF4 (25) vs lines expressing it (23) | the lines without TCF4: 1.36× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1 |
| [[ANO3]] | B | TCF4 activity raises ANO3's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without TCF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1 |
| [[ANO3]] | B | TCF4 activity weakens ANO3's drug response | lines that do not express TCF4 (23) vs lines expressing it (20) | the lines without TCF4 respond 2.75× as strongly (z diff -1.13); strongest at Homoharringtonine 5 µM: 2.65x vs 0.67x (z diff -5.5) | 0.065 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; target measured in part of the lines; artifact flags |
| [[PDE4D]] | B | TCF4 activity raises PDE4D's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without TCF4 | 0.086 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1 |
| cells under [[Ixazomib citrate (drug)]] 5 µM | B | TCF4 activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express TCF4 (25) vs lines expressing it (23) | the lines without TCF4: 1.55× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1 |
| [[PDE7B]] | C | TCF4 activity raises PDE7B's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.62× lower at baseline in the lines without TCF4 | 0.001 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[PDCD1LG2]] | C | TCF4 activity raises PDCD1LG2's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.84× lower at baseline in the lines without TCF4 | 0.005 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[TMEM200A]] | C | TCF4 activity raises TMEM200A's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.99× lower at baseline in the lines without TCF4 | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[FAM167A]] | C | TCF4 activity raises FAM167A's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.66× lower at baseline in the lines without TCF4 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[FGF14]] | C | TCF4 activity raises FGF14's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 3.95× lower at baseline in the lines without TCF4 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[PAPPA]] | C | TCF4 activity raises PAPPA's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 5.20× lower at baseline in the lines without TCF4 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.1, 21.8); signed map (37.2, 42.9). **Vector** length 108, 36.1% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +12.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.9 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.0 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.7 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.8 | +2.8 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.8 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:55,222,185-55,664,787 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEF2-1B, ITF2, bHLHb19, E2-2 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 11 pathways, smallest: TGFBR3 expression; Myogenesis; Signaling by TGFBR3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P15884](https://www.uniprot.org/uniprotkb/P15884) (Transcription factor 4):

> Transcription factor that binds to the immunoglobulin enhancer Mu-E5/KE5-motif. Involved in the initiation of neuronal differentiation. Activates transcription by binding to the E box (5'-CANNTG-3'). Binds to the E-box present in the somatostatin receptor 2 initiator element (SSTR2-INR) to activate transcription (By similarity). Preferentially binds to either 5'-ACANNTGT-3' or 5'-CCANNTGG-3'.

**Summary**, from NCBI Gene [6925](https://www.ncbi.nlm.nih.gov/gene/6925):

> This gene encodes transcription factor 4, a basic helix-loop-helix transcription factor. The encoded protein recognizes an Ephrussi-box ('E-box') binding site ('CANNTG') - a motif first identified in immunoglobulin enhancers. This gene is broadly expressed, and may play an important role in nervous system development. Defects in this gene are a cause of Pitt-Hopkins syndrome. In addition, an intronic CTG repeat normally numbering 10-37 repeat units can expand to >50 repeat units and cause Fuchs …

**Accessions** — [HGNC:11634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11634) · Entrez [6925](https://www.ncbi.nlm.nih.gov/gene/6925) · UniProt [P15884](https://www.uniprot.org/uniprotkb/P15884) · Ensembl [ENSG00000196628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196628)

## Data

Gene col 12250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12250); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12250]; `tensor/DDL_lfc|DDL_z.npy` [12250]; `embed/gene_vectors.npy` [12250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12250 or target_col == 12250). Every well: [[TCF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
