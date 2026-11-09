---
symbol: "EFHD1"
type: "gene"
col: 3681
ensembl_id: "ENSG00000115468"
name: "EF-hand domain family member D1"
location: "2q37.1"
module: 100
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 47
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# EFHD1

*EF-hand domain family member D1* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.18× (z +17.0, q 0e+00, up in 23 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.163×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (C-33 A 0.0895×); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.0576×; ⚠ cell-cycle shift, explains ~52% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0964×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH23]] (+0.68, fdr 7e-06), [[CELF5]] (+0.66, fdr 7e-06), [[TMEM266]] (+0.66, fdr 7e-06).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[HHIPL2]] → it (grade B ⚠); 8 go from it, the strongest it → cells under [[EX229 (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.18×** | +17.0 | 0e+00 | 23/28 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.07×** | +16.3 | 0e+00 | 3/4 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.43×** | +13.1 | 1e-36 | 31/43 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +12.4 | 4e-33 | 7/11 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.83×** | +10.8 | 3e-25 | 25/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.64×** | +10.1 | 4e-22 | 21/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +9.8 | 7e-21 | 16/30 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +8.7 | 2e-16 | 3/5 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.04×** | +7.4 | 8e-12 | 16/32 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +6.8 | 6e-10 | 20/43 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +6.2 | 4e-08 | 17/42 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +6.0 | 9e-08 | 12/37 (NCI-H23, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.1 | 1e-05 | 6/43 (NCI-H460, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.4 | 5e-04 | 4/38 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.2 | 9e-04 | 5/17 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.003 | 9/42 (BT-474, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.7 | 0.006 | 5/35 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +3.4 | 0.016 | 1/32 (NCI-H460) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.017 | 6/38 (BT-474, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3681.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.163×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (C-33 A 0.0895×); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.0576×; ⚠ cell-cycle shift, explains ~52% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0964×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.701× | -3.7 | 0.10 | 12/38 (NCI-H661, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.710× | -3.6 | 0.10 | 10/37 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.724× | -3.4 | 0.14 | 8/43 (BT-474, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.730× | -3.3 | 0.15 | 12/42 (A549, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.736× | -3.2 | 0.16 | 12/43 (HCT15, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.84 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +10.4) | — |
| [[A-172 (line)]] | wt | 4.42 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0576× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-427 (line)]] | wt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -9.9) |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0895× (z -9.2) |
| [[LoVo (line)]] | wt | 2.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 5.33 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0964× (z -8.5) |
| [[PANC-1 (line)]] | alt | 8.19 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.36× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.984 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH23]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[CELF5]] | +0.66 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[TMEM266]] | +0.66 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[KCNB1]] | +0.66 | +0.61 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MEIOC]] | +0.62 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MYO1F]] | +0.59 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[DPYSL5]] | +0.58 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[SPTBN4]] | +0.58 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[NME9]] | +0.58 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ARHGEF26-AS1]] | +0.58 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ITGA7]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HHIPL2]] | B | HHIPL2 activity raises EFHD1's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without HHIPL2 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent |
| [[ZNF536]] | B | ZNF536 activity raises EFHD1's level | lines that do not express ZNF536 (24) vs lines expressing it (26) | 1.59× lower at baseline in the lines without ZNF536 | 0.043 | ⚠ within organs, on part of the lines; also absent: PDZD4, NPTX1, RET; maybe low, not absent |
| [[CACNA1B]] | B | CACNA1B activity raises EFHD1's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without CACNA1B | 0.047 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[KCNQ2]] | B | KCNQ2 activity raises EFHD1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without KCNQ2 | 0.058 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[SRRM3]] | B | SRRM3 activity raises EFHD1's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without SRRM3 | 0.069 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[MYT1]] | B | MYT1 activity raises EFHD1's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.66× lower at baseline in the lines without MYT1 | 0.075 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[RTN4RL1]] | B | RTN4RL1 activity raises EFHD1's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 1.81× lower at baseline in the lines without RTN4RL1 | 0.077 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[EX229 (drug)]] 0.05 µM | C | EFHD1 activity raises the cells' numbers under EX229 0.05 µM (protects the cells) | lines that do not express EFHD1 (3) vs lines expressing it (45) | the lines without EFHD1: 0.73× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 0.5 µM | C | EFHD1 activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express EFHD1 (3) vs lines expressing it (45) | the lines without EFHD1: 0.68× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; maybe low, not absent |
| cells under [[MK-3903 (drug)]] 0.05 µM | C | EFHD1 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express EFHD1 (3) vs lines expressing it (45) | the lines without EFHD1: 0.76× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; maybe low, not absent |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | C | EFHD1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express EFHD1 (3) vs lines expressing it (45) | the lines without EFHD1: 1.27× the cells of the other lines | 0.064 | ⚠ few lines (3 vs 47); across organs; maybe low, not absent |
| cells under [[Aliskiren (drug)]] 0.5 µM | C | EFHD1 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express EFHD1 (3) vs lines expressing it (45) | the lines without EFHD1: 0.67× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; maybe low, not absent |
| cells under [[Celecoxib (drug)]] 0.05 µM | C | EFHD1 activity raises the cells' numbers under Celecoxib 0.05 µM (protects the cells) | lines that do not express EFHD1 (3) vs lines expressing it (45) | the lines without EFHD1: 0.71× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; maybe low, not absent |
| cells under [[Glycyrrhizic acid (drug)]] 0.5 µM | C | EFHD1 activity raises the cells' numbers under Glycyrrhizic acid 0.5 µM (protects the cells) | lines that do not express EFHD1 (3) vs lines expressing it (45) | the lines without EFHD1: 0.72× the cells of the other lines | 0.089 | ⚠ few lines (3 vs 47); across organs; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | C | EFHD1 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express EFHD1 (3) vs lines expressing it (45) | the lines without EFHD1: 0.78× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); across organs; maybe low, not absent |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.4, 34.8); signed map (27.2, 20.3). **Vector** length 46.7, 5.91% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.7 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand domain family member D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:232,606,057-232,682,776 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13612 |
| Gene groups (HGNC) | EF-hand domain containing |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUP0](https://www.uniprot.org/uniprotkb/Q9BUP0) (EF-hand domain-containing protein D1):

> Acts as a calcium sensor for mitochondrial flash (mitoflash) activation, an event characterized by stochastic bursts of superoxide production. May play a role in neuronal differentiation (By similarity).

**Summary**, from NCBI Gene [80303](https://www.ncbi.nlm.nih.gov/gene/80303):

> This gene encodes a member of the EF-hand super family of calcium binding proteins, which are involved in a variety of cellular processes including mitosis, synaptic transmission, and cytoskeletal rearrangement. The protein encoded by this gene is composed of an N-terminal disordered region, proline-rich elements, two EF-hands, and a C-terminal coiled-coil domain. This protein has been shown to associate with the mitochondrial inner membrane, and in HeLa cells, acts as a novel mitochondrial …

**Accessions** — [HGNC:29556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29556) · Entrez [80303](https://www.ncbi.nlm.nih.gov/gene/80303) · UniProt [Q9BUP0](https://www.uniprot.org/uniprotkb/Q9BUP0) · Ensembl [ENSG00000115468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115468)

## Data

Gene col 3681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3681); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3681]; `tensor/DDL_lfc|DDL_z.npy` [3681]; `embed/gene_vectors.npy` [3681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3681 or target_col == 3681). Every well: [[EFHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
