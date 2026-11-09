---
symbol: "TUB"
type: "gene"
col: 9299
ensembl_id: "ENSG00000166402"
name: "TUB bipartite transcription factor"
location: "11p15.4"
module: 176
arm: "+"
pooled_cpm: 2.79
n_lines_expressing: 32
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 13
direction_downstream: 8
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# TUB

*TUB bipartite transcription factor* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +9.8, q 6e-20, up in 13 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.414× (z -8.2, q 1e-13, down in 15 of 25 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.446× (z -7.8, q 1e-12, down in 15 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAGLR]] (+0.60, fdr 7e-06), [[MSI1]] (+0.59, fdr 1e-05), [[PAX2]] (+0.59, fdr 4e-05); moves opposite to [[SPG11]] (-0.52, fdr 6e-05), [[H3-3B]] (-0.51, fdr 8e-05), [[DNAL4]] (-0.50, fdr 3e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 8 go from it, the strongest it → [[SMO]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +9.8 | 6e-20 | 13/20 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.93×** | +9.0 | 5e-17 | 16/28 (HOP62, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +8.1 | 8e-14 | 14/25 (HOP62, SK-MEL-2, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +8.0 | 2e-13 | 15/28 (PANC-1, NCI-H1792, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +7.9 | 4e-13 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.3 | 0.002 | 3/13 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 0.003 | 11/24 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.50×** | +3.9 | 0.006 | 6/24 (C-33 A, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.007 | 9/29 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.5 | 0.023 | 2/30 (NCI-H23, A549) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +3.2 | 0.061 | 2/8 (MIA PaCa-2, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Trifluridine (drug)]] 0.5 µM |  | 1.37× | +3.0 | 0.11 | 3/24 (A-427, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.414×** | -8.2 | 1e-13 | 15/25 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.446×** | -7.8 | 1e-12 | 15/28 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.602×** | -4.9 | 2e-04 | 9/20 (A498, A549, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.614×** | -4.7 | 3e-04 | 13/26 (A-172, C32, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.714×** | -4.6 | 5e-04 | 11/20 (A-427, A549, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.639×** | -4.3 | 0.001 | 9/29 (A498, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Artesunate (drug)]] 5 µM |  | **0.765×** | -3.7 | 0.020 | 6/29 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.679×** | -3.6 | 0.022 | 8/23 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **0.712×** | -3.2 | 0.096 | 5/22 (A-172, A549, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.710× | -3.1 | 0.12 | 3/20 (A-172, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 11.8 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.153× (z -9.9) |
| [[A549 (line)]] | wt | 5.88 | 0 | 2 (1 ⚠) | — | [[Isocorydine (drug)]] 0.5 µM 0.0755× (z -9.9) |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0697× (z -12.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.61 | 0 | 2 | — | [[Sulfisoxazole (drug)]] 0.05 µM 0.0586× (z -10.8) |
| [[A498 (line)]] | wt | 8.47 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -11.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 5.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.226 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.900 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.320 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAGLR]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[MSI1]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PAX2]] | +0.59 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[CGREF1]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ASIC1]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[SMO]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SEPTIN3]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GRID1]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[KBTBD11]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[FGD1]] | +0.53 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LINC00937]] | +0.53 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[MCOLN2]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPG11]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[H3-3B]] | -0.51 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[DNAL4]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[WASHC3]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[CHMP4A]] | -0.48 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[LRRC37A2]] | -0.46 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[STYXL1]] | -0.46 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[RSPH3]] | -0.45 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[CLEC16A]] | -0.45 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[R3HDM2]] | -0.44 | -0.24 / -0.58 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises TUB's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without MSI1 | 0.039 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[LRRC4B]] | B | LRRC4B activity raises TUB's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without LRRC4B | 0.043 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[LINC00937]] | B | LINC00937 activity raises TUB's level | lines that do not express LINC00937 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without LINC00937 | 0.085 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000255367, MRAS; maybe low, not absent |
| [[SCD5]] | B | SCD5 activity raises TUB's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 2.02× lower at baseline in the lines without SCD5 | 0.097 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[SLC22A17]] | C | SLC22A17 activity raises TUB's level | lines that do not express SLC22A17 (21) vs lines expressing it (29) | 3.15× lower at baseline in the lines without SLC22A17 | 0.004 | ⚠ within organs, on part of the lines; also absent: APBA2, TUB, COLEC12; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises TUB's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.77× lower at baseline in the lines without PDZD4 | 0.007 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |
| [[MCOLN2]] | C | MCOLN2 activity raises TUB's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.14× lower at baseline in the lines without MCOLN2 | 0.031 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG; co-absent with the target |
| [[VASH1]] | C | VASH1 activity raises TUB's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.33× lower at baseline in the lines without VASH1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |
| [[FAM124A]] | C | FAM124A activity raises TUB's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without FAM124A | 0.046 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[MGAT5B]] | C | MGAT5B activity raises TUB's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 2.95× lower at baseline in the lines without MGAT5B | 0.066 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |
| [[MED12L]] | C | MED12L activity raises TUB's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without MED12L | 0.074 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2; co-absent with the target |
| [[RAB6B]] | C | RAB6B activity raises TUB's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.46× lower at baseline in the lines without RAB6B | 0.074 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMO]] | B | TUB activity raises SMO's level | lines that do not express TUB (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without TUB | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82 |
| [[LINC00937]] | B | TUB activity raises LINC00937's level | lines that do not express TUB (18) vs lines expressing it (32) | 1.53× lower at baseline in the lines without TUB | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82 |
| [[FAM124A]] | C | TUB activity raises FAM124A's level | lines that do not express TUB (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without TUB | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82; co-absent with the target |
| [[PDZD4]] | C | TUB activity raises PDZD4's level | lines that do not express TUB (18) vs lines expressing it (32) | 3.35× lower at baseline in the lines without TUB | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82; co-absent with the target |
| [[SLC22A17]] | C | TUB activity raises SLC22A17's level | lines that do not express TUB (18) vs lines expressing it (32) | 3.15× lower at baseline in the lines without TUB | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82; co-absent with the target |
| [[RAB6B]] | C | TUB activity raises RAB6B's level | lines that do not express TUB (18) vs lines expressing it (32) | 2.60× lower at baseline in the lines without TUB | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82; co-absent with the target |
| [[VASH1]] | C | TUB activity raises VASH1's level | lines that do not express TUB (18) vs lines expressing it (32) | 2.34× lower at baseline in the lines without TUB | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82; co-absent with the target |
| [[MCOLN2]] | C | TUB activity raises MCOLN2's level | lines that do not express TUB (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without TUB | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82; co-absent with the target |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.3, 41.5); signed map (24.2, 28.5). **Vector** length 45.5, 7.74% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.5 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.1 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -7.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | TUB bipartite transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:8,019,244-8,106,243 (+) |
| Ensembl biotype | protein_coding |
| Also known as | rd5 |
| Matched by | ensembl_id |

**Function**, from UniProt [P50607](https://www.uniprot.org/uniprotkb/P50607) (Tubby protein homolog):

> Functions in signal transduction from heterotrimeric G protein-coupled receptors. Binds to membranes containing phosphatidylinositol 4,5-bisphosphate. Can bind DNA (in vitro). May contribute to the regulation of transcription in the nucleus. Could be involved in the hypothalamic regulation of body weight (By similarity). Contribute to stimulation of phagocytosis of apoptotic retinal pigment epithelium (RPE) cells and macrophages.

**Summary**, from NCBI Gene [7275](https://www.ncbi.nlm.nih.gov/gene/7275):

> This gene encodes a member of the Tubby family of bipartite transcription factors. The encoded protein may play a role in obesity and sensorineural degradation. The crystal structure has been determined for a similar protein in mouse, and it functions as a membrane-bound transcription regulator that translocates to the nucleus in response to phosphoinositide hydrolysis. Two transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12406) · Entrez [7275](https://www.ncbi.nlm.nih.gov/gene/7275) · UniProt [P50607](https://www.uniprot.org/uniprotkb/P50607) · Ensembl [ENSG00000166402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166402)

## Data

Gene col 9299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9299); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9299]; `tensor/DDL_lfc|DDL_z.npy` [9299]; `embed/gene_vectors.npy` [9299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9299 or target_col == 9299). Every well: [[TUB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
