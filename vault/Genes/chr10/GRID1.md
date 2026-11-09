---
symbol: "GRID1"
type: "gene"
col: 11324
ensembl_id: "ENSG00000182771"
name: "glutamate ionotropic receptor delta type subunit 1"
location: "10q23.1-q23.2"
module: 102
arm: "+"
pooled_cpm: 10.71
n_lines_expressing: 23
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 9
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# GRID1

*glutamate ionotropic receptor delta type subunit 1* — 10q23.1-q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.69× (z +28.9, q 0e+00, up in 10 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.717× (z -4.4, q 0.005, down in 8 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.159×, A-172 0.154×, MIA PaCa-2 0.177×, NCI-H2030 0.377×); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.119×, A-172 0.121×, Hs 766T 0.0890×, SNU-1 0.173×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.0502×, A-172 0.179×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-172 0.207×, A-427 0.266×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH23]] (+0.68, fdr 1e-05), [[GABRB3]] (+0.65, fdr 1e-05), [[SYN2]] (+0.64, fdr 7e-06).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[KIF26A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.69×** | +28.9 | 0e+00 | 10/19 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.08×** | +21.0 | 0e+00 | 13/19 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.86×** | +13.9 | 9e-42 | 12/19 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +13.6 | 6e-40 | 1/12 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +11.9 | 2e-30 | 2/16 (HEC-1-A, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +11.0 | 6e-26 | 16/20 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.20×** | +10.4 | 2e-23 | 7/19 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +9.5 | 1e-19 | 3/19 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +8.4 | 3e-15 | 2/13 (SW480, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +7.6 | 1e-12 | 7/20 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +7.0 | 2e-10 | 7/20 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +7.0 | 2e-10 | 7/20 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.8 | 4e-10 | 3/20 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.60×** | +6.6 | 1e-09 | 8/15 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +6.5 | 3e-09 | 10/20 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 2e-08 | 6/19 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +5.9 | 9e-08 | 5/19 (A549, H4, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.4 | 3e-06 | 4/18 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.002 | 2/19 (SNU-423, C-33 A) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11324.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.159×, A-172 0.154×, MIA PaCa-2 0.177×, NCI-H2030 0.377×); [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.119×, A-172 0.121×, Hs 766T 0.0890×, SNU-1 0.173×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.0502×, A-172 0.179×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A-172 0.207×, A-427 0.266×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -4.4 | 0.005 | 8/20 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 86.8 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0502× (z -25.0) |
| [[A-172 (line)]] | wt | 74.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.5) |
| [[NCI-H2030 (line)]] | alt | 37.5 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.195× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 3.71 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +15.9) | — |
| [[SNU-1 (line)]] | wt | 89.9 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0952× (z -15.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 65.4 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.106× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -13.3) |
| [[PANC-1 (line)]] | alt | 9.38 | 2 | 0 | [[Panobinostat (drug)]] 0.05 µM 5.02× (z +9.2) | — |
| [[A549 (line)]] | wt | 9.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.7) |
| [[H4 (line)]] | wt | 16.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.112× (z -8.7) |
| [[Hs 766T (line)]] | wt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 3.26 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.1× (z +11.2) | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.180× (z -10.3) ⚠ toxic |
| [[A498 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH23]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 | same gene group |
| [[GABRB3]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[SYN2]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[DOCK3]] | +0.63 | +0.56 / +0.75 | both halves | 1e-05 | same gene group |
| [[SDK2]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MSI1]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[DPYSL5]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[RASGEF1C]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MEGF11]] | +0.60 | +0.43 / +0.68 | both halves | 4e-05 |  |
| [[LRRN2]] | +0.60 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[CECR2]] | +0.59 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[BRSK2]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRID1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRDM16]] | B | PRDM16 activity raises GRID1's level | lines that do not express PRDM16 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without PRDM16 | 0.048 | ⚠ within organs, on part of the lines; also absent: FBXO2, HAS3, PTPRN2 |
| [[SEPTIN3]] | B | SEPTIN3 activity raises GRID1's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without SEPTIN3 | 0.062 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[LINC02643]] | C | LINC02643 activity raises GRID1's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 4.39× lower at baseline in the lines without LINC02643 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530; co-absent with the target |
| [[SLC47A1]] | C | SLC47A1 activity raises GRID1's level | lines that do not express SLC47A1 (20) vs lines expressing it (30) | 2.64× lower at baseline in the lines without SLC47A1 | 0.048 | ⚠ within organs, on part of the lines; also absent: DUSP9, STOX2, NOVA2; maybe low, not absent; co-absent with the target |
| [[CHD5]] | C | CHD5 activity raises GRID1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.30× lower at baseline in the lines without CHD5 | 0.054 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[LAMC3]] | C | LAMC3 activity raises GRID1's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 2.58× lower at baseline in the lines without LAMC3 | 0.060 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2; co-absent with the target |
| [[PAX2]] | C | PAX2 activity raises GRID1's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.96× lower at baseline in the lines without PAX2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises GRID1's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without DPYSL5 | 0.062 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[MSI1]] | C | MSI1 activity raises GRID1's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without MSI1 | 0.070 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; co-absent with the target |
| [[TAFA5]] | C | TAFA5 activity raises GRID1's level | lines that do not express TAFA5 (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without TAFA5 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000260958, UNC5D, EPGN; co-absent with the target |
| [[GPC3]] | C | GPC3 activity raises GRID1's level | lines that do not express GPC3 (35) vs lines expressing it (15) | 2.19× lower at baseline in the lines without GPC3 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TF, GCG, APOA2; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | GRID1 activity raises KIF26A's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without GRID1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[ADGRB1]] | B | GRID1 activity raises ADGRB1's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without GRID1 | 0.063 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[PLD5]] | B | GRID1 activity raises PLD5's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without GRID1 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[DOCK3]] | B | GRID1 activity raises DOCK3's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 2.99× lower at baseline in the lines without GRID1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[ATP6V1E2]] | B | GRID1 activity raises ATP6V1E2's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without GRID1 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[BTNL9]] | B | GRID1 activity raises BTNL9's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.41× lower at baseline in the lines without GRID1 | 0.088 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[SDK2]] | B | GRID1 activity raises SDK2's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without GRID1 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[GNAL]] | B | GRID1 activity raises GNAL's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without GRID1 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[PHF21B]] | C | GRID1 activity raises PHF21B's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 2.97× lower at baseline in the lines without GRID1 | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.828). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.8, 37.2); signed map (27.1, 25.1). **Vector** length 63.4, 17.0% of its response variance represented; |z| ≥ 3 in 544 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.54 to 8); *Transmission across Chemical Synapses* (reactome, mean cos +0.55 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +21.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +13.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +1.8 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor delta type subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.1-q23.2 — chr10:85,599,552-86,366,795 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GluD1, KIAA1220 |
| Gene groups (HGNC) | Glutamate ionotropic receptor delta type subunits; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULK0](https://www.uniprot.org/uniprotkb/Q9ULK0) (Glutamate receptor ionotropic, delta-1):

> Member of the ionotropic glutamate receptor family, which plays a crucial role in synaptic organization and signal transduction in the central nervous system. Although it shares structural features with ionotropic glutamate receptors, does not bind glutamate as a primary ligand. Instead, forms trans-synaptic adhesion complexes with presynaptic neurexins and cerebellins, regulating NMDA and AMPA receptor activity and influencing synaptic plasticity through signal transduction (By similarity). In …

**Summary**, from NCBI Gene [2894](https://www.ncbi.nlm.nih.gov/gene/2894):

> This gene encodes a subunit of glutamate receptor channels. These channels mediate most of the fast excitatory synaptic transmission in the central nervous system and play key roles in synaptic plasticity.[provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:4575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4575) · Entrez [2894](https://www.ncbi.nlm.nih.gov/gene/2894) · UniProt [Q9ULK0](https://www.uniprot.org/uniprotkb/Q9ULK0) · Ensembl [ENSG00000182771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182771)

## Data

Gene col 11324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11324); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11324]; `tensor/DDL_lfc|DDL_z.npy` [11324]; `embed/gene_vectors.npy` [11324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11324 or target_col == 11324). Every well: [[GRID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
