---
symbol: "PI3"
type: "gene"
col: 4477
ensembl_id: "ENSG00000124102"
name: "peptidase inhibitor 3"
location: "20q13.12"
module: 155
arm: "+"
pooled_cpm: 4.14
n_lines_expressing: 23
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 26
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# PI3

*peptidase inhibitor 3* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.82× (z +7.5, q 2e-11, up in 13 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.0357×, HT-29 0.155×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLPI]] (+0.68, fdr 7e-06), [[CES1]] (+0.64, fdr 1e-05), [[S100A9]] (+0.64, fdr 1e-05); moves opposite to [[SEC22C]] (-0.43, fdr 2e-04), [[SFT2D2]] (-0.43, fdr 7e-05), [[EXOSC8]] (-0.40, fdr 1e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 26 go from it, the strongest it → [[MLKL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.82×** | +7.5 | 2e-11 | 13/20 (BT-474, J82, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +7.5 | 2e-11 | 12/17 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **4.26×** | +7.0 | 5e-10 | 8/12 (BT-474, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.09×** | +6.8 | 2e-09 | 1/4 (J82) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.10×** | +5.8 | 8e-07 | 7/16 (LoVo, NCI-H460, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.05×** | +5.7 | 1e-06 | 3/9 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **6.90×** | +5.1 | 4e-05 | 5/9 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.76×** | +4.8 | 1e-04 | 2/6 (NCI-H460, J82) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.53×** | +4.8 | 1e-04 | 13/20 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.29×** | +4.2 | 0.001 | 11/19 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +3.9 | 0.006 | 7/19 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.12×** | +3.6 | 0.013 | 4/18 (LS 180, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.03×** | +3.6 | 0.013 | 5/18 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.11×** | +3.6 | 0.014 | 6/19 (NCI-H1792, H4, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.015 | 6/20 (SW 1088, NCI-H460, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.85×** | +3.1 | 0.057 | 1/17 (J82) | inconsistent across doses | low cells (technical?); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.44×** | +3.1 | 0.057 | 3/16 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **2.43×** | +3.1 | 0.057 | 2/18 (J82, NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.80×** | +3.0 | 0.075 | 10/20 (SW48, H4, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.51×** | +2.9 | 0.086 | 7/20 (BT-474, HS-578T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4477.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2030 0.0357×, HT-29 0.155×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.475× | -3.6 | 0.16 | 6/20 (NCI-H2030, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.518× | -3.4 | 0.16 | 9/20 (A549, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | 0.287× | -3.3 | 0.19 | 5/20 (NCI-H1573, SW 1088, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0357× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.568 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.358 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLPI]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 | same gene group; STRING 700 |
| [[CES1]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[S100A9]] | +0.64 | +0.54 / +0.67 | both halves | 1e-05 | pathway: Antimicrobial peptides |
| [[SERPINA1]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 | STRING 498 |
| [[ADGRE2]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[GSDMC]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TCIM]] | +0.56 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[SERPINB3]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 | STRING 458 |
| [[S100P]] | +0.53 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[S100A8]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 | pathway: Antimicrobial peptides |
| [[FAM83A]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SERPINB4]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 | STRING 508 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC22C]] | -0.43 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[SFT2D2]] | -0.43 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[EXOSC8]] | -0.40 | -0.34 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PI3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[XDH]] | B | XDH activity raises PI3's level | lines that do not express XDH (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without XDH | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, SYT13, LINC01564 |
| [[SLPI]] | C | SLPI activity raises PI3's level | lines that do not express SLPI (25) vs lines expressing it (25) | 3.13× lower at baseline in the lines without SLPI | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2; co-absent with the target |
| [[FOXQ1]] | C | FOXQ1 activity raises PI3's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 1.93× lower at baseline in the lines without FOXQ1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; co-absent with the target |
| [[MUC5AC]] | C | MUC5AC activity raises PI3's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 1.97× lower at baseline in the lines without MUC5AC | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |
| [[SERPINB3]] | C | SERPINB3 activity raises PI3's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.17× lower at baseline in the lines without SERPINB3 | 0.076 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[GPR141]] | C | GPR141 activity raises PI3's level | lines that do not express GPR141 (39) vs lines expressing it (11) | 1.89× lower at baseline in the lines without GPR141 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, S100A8, LINC00879; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 20, C 6. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLKL]] | B | PI3 activity raises MLKL's level | lines that do not express PI3 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without PI3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[KLF5]] | B | PI3 activity raises KLF5's level | lines that do not express PI3 (27) vs lines expressing it (23) | 2.38× lower at baseline in the lines without PI3 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[TNFAIP8]] | B | PI3 activity raises TNFAIP8's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without PI3 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[DOCK5]] | B | PI3 activity raises DOCK5's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without PI3 | 0.024 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[C19orf33]] | B | PI3 activity raises C19orf33's level | lines that do not express PI3 (27) vs lines expressing it (23) | 2.01× lower at baseline in the lines without PI3 | 0.033 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[IL4R]] | B | PI3 activity raises IL4R's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without PI3 | 0.033 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[C11orf91]] | B | PI3 activity raises C11orf91's level | lines that do not express PI3 (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without PI3 | 0.035 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[SLC22A23]] | B | PI3 activity raises SLC22A23's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without PI3 | 0.042 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[MARCHF3]] | B | PI3 activity raises MARCHF3's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.69× lower at baseline in the lines without PI3 | 0.049 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[TANK]] | B | PI3 activity raises TANK's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.24× lower at baseline in the lines without PI3 | 0.051 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[ST3GAL1]] | B | PI3 activity raises ST3GAL1's level | lines that do not express PI3 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without PI3 | 0.061 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[AQP3]] | B | PI3 activity raises AQP3's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without PI3 | 0.064 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.6, 48.8); signed map (55.2, 24.1). **Vector** length 51.2, 13.6% of its response variance represented; |z| ≥ 3 in 474 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +1.7 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | peptidase inhibitor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,174,902-45,176,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ESI, SKALP, ELAFIN, WAP3, WFDC14, cementoin |
| Gene groups (HGNC) | WAP four-disulfide core domain containing |
| Reactome | 4 pathways, smallest: Antimicrobial peptides; Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P19957](https://www.uniprot.org/uniprotkb/P19957) (Elafin):

> Neutrophil and pancreatic elastase-specific inhibitor of skin. It may prevent elastase-mediated tissue proteolysis. Has been shown to inhibit the alpha-4-beta-2/CHRNA2-CHRNB2 nicotinic acetylcholine receptor and to produce a weak inhibition on Kv11.1/KCNH2/ERG1 and on the transient receptor potential cation channel subfamily V member 1 (TRPV1).

**Summary**, from NCBI Gene [5266](https://www.ncbi.nlm.nih.gov/gene/5266):

> This gene encodes an elastase-specific inhibitor that functions as an antimicrobial peptide against Gram-positive and Gram-negative bacteria, and fungal pathogens. The protein contains a WAP-type four-disulfide core (WFDC) domain, and is thus a member of the WFDC domain family. Most WFDC gene members are localized to chromosome 20q12-q13 in two clusters: centromeric and telomeric. This gene belongs to the centromeric cluster. Expression of this gene is upgulated by bacterial lipopolysaccharides …

**Accessions** — [HGNC:8947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8947) · Entrez [5266](https://www.ncbi.nlm.nih.gov/gene/5266) · UniProt [P19957](https://www.uniprot.org/uniprotkb/P19957) · Ensembl [ENSG00000124102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124102)

## Data

Gene col 4477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4477); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4477]; `tensor/DDL_lfc|DDL_z.npy` [4477]; `embed/gene_vectors.npy` [4477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4477 or target_col == 4477). Every well: [[PI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
