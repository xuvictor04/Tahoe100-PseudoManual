---
symbol: "LMX1B"
type: "gene"
col: 5949
ensembl_id: "ENSG00000136944"
name: "LIM homeobox transcription factor 1 beta"
location: "9q33.3"
module: 82
arm: "+"
pooled_cpm: 5.32
n_lines_expressing: 26
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 19
direction_downstream: 23
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# LMX1B

*LIM homeobox transcription factor 1 beta* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.77× (z +17.5, q 0e+00, up in 11 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.626× (z -5.7, q 5e-06, down in 9 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.199×, BT-474 0.441×, A549 0.277×); [[Digitoxin (drug)]] 0.05 µM in 1 line (A-172 0.0473×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H460 0.0397×; ⚠ cell-cycle shift, explains ~7% of this change); [[Silodosin (drug)]] 5 µM in 1 line (NCI-H2030 0.0892×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00937]] (+0.71, fdr 7e-06), [[RIMS3]] (+0.68, fdr 1e-05), [[GNAO1]] (+0.64, fdr 7e-06); moves opposite to [[TBCK]] (-0.55, fdr 3e-05), [[CHM]] (-0.54, fdr 2e-04), [[MCPH1]] (-0.53, fdr 3e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); 23 go from it, the strongest it → [[KCNK13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +17.5 | 0e+00 | 11/22 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.85×** | +16.3 | 0e+00 | 21/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.35×** | +14.7 | 0e+00 | 21/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.15×** | +13.9 | 7e-42 | 19/24 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.16×** | +13.2 | 2e-37 | 19/24 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +12.5 | 1e-33 | 1/14 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +8.9 | 3e-17 | 21/24 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +8.5 | 2e-15 | 0/6 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +7.5 | 4e-12 | 2/9 (NCI-H460, HOP62) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +6.9 | 2e-10 | 9/22 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +6.9 | 3e-10 | 4/18 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.66×** | +6.2 | 3e-08 | 13/22 (PANC-1, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +5.7 | 4e-07 | 11/21 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +4.2 | 0.001 | 3/16 (MIA PaCa-2, AN3 CA, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 0.002 | 3/19 (HOP62, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.002 | 7/20 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.014 | 1/21 (HOP62) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.029 | 3/21 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.029 | 4/24 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.035 | 4/24 (A-427, PANC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5949.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-172 0.199×, BT-474 0.441×, A549 0.277×); [[Digitoxin (drug)]] 0.05 µM in 1 line (A-172 0.0473×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H460 0.0397×; ⚠ cell-cycle shift, explains ~7% of this change); [[Silodosin (drug)]] 5 µM in 1 line (NCI-H2030 0.0892×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -5.7 | 5e-06 | 9/24 (A549, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Captopril (drug)]] 0.5 µM |  | 0.753× | -3.5 | 0.14 | 2/24 (SK-MEL-2, C32) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.597× | -3.3 | 0.18 | 5/21 (MIA PaCa-2, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.772× | -3.2 | 0.20 | 8/21 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.777× | -3.1 | 0.21 | 10/24 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.780× | -3.1 | 0.21 | 10/23 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.90 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.0× (z +10.3) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0397× (z -13.4) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A-172 (line)]] | wt | 6.66 | 0 | 3 | — | [[Digitoxin (drug)]] 0.05 µM 0.0473× (z -13.7) |
| [[PANC-1 (line)]] | alt | 6.37 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +9.7) | — |
| [[A549 (line)]] | wt | 9.24 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 4.70 | 0 | 2 | — | [[Brimonidine (drug)]] 0.5 µM 0.0648× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 7.17 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0892× (z -11.0) |
| [[SHP-77 (line)]] | alt | 9.36 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0778× (z -10.8) |
| [[SW480 (line)]] | alt | 3.23 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.32× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 76.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0540× (z -8.6) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.623 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00937]] | +0.71 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[RIMS3]] | +0.68 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[GNAO1]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LPAR3]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.62 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TSPAN33]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CACNA2D2]] | +0.62 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[ESYT3]] | +0.61 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[FAM124A]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RET]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[RTN4R]] | +0.60 | +0.40 / +0.59 | both halves | 4e-05 |  |
| [[SEPTIN3]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CHM]] | -0.54 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[MCPH1]] | -0.53 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[RFX3-DT]] | -0.53 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[HEXIM2-AS1]] | -0.52 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[UBE3B]] | -0.52 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[USP40]] | -0.52 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[BDNF-AS]] | -0.52 | -0.31 / -0.23 | both halves | 5e-04 |  |
| [[CHD1-DT]] | -0.51 | -0.30 / -0.28 | both halves | 3e-04 |  |
| [[ANKRD17-DT]] | -0.51 | -0.33 / -0.25 | both halves | 4e-04 |  |
| [[WARS2-AS1]] | -0.51 | -0.27 / -0.37 | both halves | 3e-04 |  |
| [[CLHC1]] | -0.50 | -0.28 / -0.34 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 6, C 13. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises LMX1B's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.31× lower at baseline in the lines without TSPAN33 | 0.031 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[RIMS3]] | B | RIMS3 activity raises LMX1B's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.88× lower at baseline in the lines without RIMS3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity raises LMX1B's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 2.52× lower at baseline in the lines without ARHGAP44 | 0.060 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[MAPT]] | B | MAPT activity raises LMX1B's level | lines that do not express MAPT (10) vs lines expressing it (40) | 3.09× lower at baseline in the lines without MAPT | 0.064 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1 |
| [[MCOLN2]] | B | MCOLN2 activity raises LMX1B's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 2.13× lower at baseline in the lines without MCOLN2 | 0.086 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[RALGPS2]] | B | RALGPS2 activity lowers LMX1B's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 3.03× higher at baseline in the lines without RALGPS2 | 0.088 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[PHF21B]] | C | PHF21B activity raises LMX1B's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 3.14× lower at baseline in the lines without PHF21B | 0.008 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises LMX1B's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without DPYSL5 | 0.013 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises LMX1B's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.99× lower at baseline in the lines without KIF1A | 0.017 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[RET]] | C | RET activity raises LMX1B's level | lines that do not express RET (28) vs lines expressing it (22) | 3.36× lower at baseline in the lines without RET | 0.020 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises LMX1B's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.38× lower at baseline in the lines without NFASC | 0.028 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[FBXO27]] | C | FBXO27 activity raises LMX1B's level | lines that do not express FBXO27 (28) vs lines expressing it (22) | 3.07× lower at baseline in the lines without FBXO27 | 0.032 | ⚠ within organs, on part of the lines; also absent: SLFN13, DLL3, PAX2; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 10, C 13. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK13]] | B | LMX1B activity raises KCNK13's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.55× lower at baseline in the lines without LMX1B | 0.010 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[KIF26A]] | B | LMX1B activity raises KIF26A's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without LMX1B | 0.045 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[ATP7B]] | B | LMX1B activity raises ATP7B's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.07× lower at baseline in the lines without LMX1B | 0.047 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[STRBP]] | B | LMX1B activity raises STRBP's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.29× lower at baseline in the lines without LMX1B | 0.049 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[SEPTIN6]] | B | LMX1B activity raises SEPTIN6's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.54× lower at baseline in the lines without LMX1B | 0.054 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[SCN8A]] | B | LMX1B activity raises SCN8A's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without LMX1B | 0.069 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[HYKK]] | B | LMX1B activity raises HYKK's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.23× lower at baseline in the lines without LMX1B | 0.070 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[LRRC20]] | B | LMX1B activity raises LRRC20's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.27× lower at baseline in the lines without LMX1B | 0.075 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[MAPT]] | B | LMX1B activity raises MAPT's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without LMX1B | 0.076 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[SBK1]] | B | LMX1B activity raises SBK1's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without LMX1B | 0.082 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[KIF1A]] | C | LMX1B activity raises KIF1A's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 6.37× lower at baseline in the lines without LMX1B | 0.006 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |
| [[FBXO27]] | C | LMX1B activity raises FBXO27's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 3.14× lower at baseline in the lines without LMX1B | 0.019 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.1, 39.1); signed map (27.1, 28.2). **Vector** length 43.9, 7.85% of its response variance represented; |z| ≥ 3 in 607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +6.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | -0.3 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.1 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -1.7 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -5.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | LIM homeobox transcription factor 1 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:126,613,928-126,701,032 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously NPS1 |
| Gene groups (HGNC) | LIM class homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [O60663](https://www.uniprot.org/uniprotkb/O60663) (LIM homeobox transcription factor 1-beta):

> Transcription factor involved in the regulation of podocyte-expressed genes. Essential for the specification of dorsal limb fate at both the zeugopodal and autopodal levels.

**Summary**, from NCBI Gene [4010](https://www.ncbi.nlm.nih.gov/gene/4010):

> This gene encodes a member of LIM-homeodomain family of proteins containing two N-terminal zinc-binding LIM domains, 1 homeodomain, and a C-terminal glutamine-rich domain. It functions as a transcription factor, and is essential for the normal development of dorsal limb structures, the glomerular basement membrane, the anterior segment of the eye, and dopaminergic and serotonergic neurons. Mutations in this gene are associated with nail-patella syndrome. Alternatively spliced transcript …

**Accessions** — [HGNC:6654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6654) · Entrez [4010](https://www.ncbi.nlm.nih.gov/gene/4010) · UniProt [O60663](https://www.uniprot.org/uniprotkb/O60663) · Ensembl [ENSG00000136944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136944)

## Data

Gene col 5949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5949); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5949]; `tensor/DDL_lfc|DDL_z.npy` [5949]; `embed/gene_vectors.npy` [5949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5949 or target_col == 5949). Every well: [[LMX1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMX1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
