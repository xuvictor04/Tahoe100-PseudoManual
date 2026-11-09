---
symbol: "INPP1"
type: "gene"
col: 7550
ensembl_id: "ENSG00000151689"
name: "inositol polyphosphate-1-phosphatase"
location: "2q32.2"
module: 73
arm: "+"
pooled_cpm: 20.08
n_lines_expressing: 38
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 20
direction_downstream: 5
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# INPP1

*inositol polyphosphate-1-phosphatase* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.49× (z +16.9, q 0e+00, up in 26 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.910× (z -6.2, q 2e-07, down in 6 of 36 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.764× (z -6.2, q 2e-07, down in 18 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SULF2]] (+0.72, fdr 7e-06), [[EPHA2]] (+0.67, fdr 7e-06), [[COL17A1]] (+0.66, fdr 1e-05); moves opposite to [[ATF2]] (-0.46, fdr 7e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[C4BPB]] → it (grade B ⚠); 5 go from it, the strongest it → [[PLK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +16.9 | 0e+00 | 26/34 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +13.3 | 9e-38 | 20/35 (AsPC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +12.0 | 8e-31 | 26/35 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +11.6 | 9e-29 | 21/32 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +10.8 | 4e-25 | 26/35 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +10.2 | 1e-22 | 22/35 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +9.6 | 9e-20 | 19/34 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +9.4 | 5e-19 | 18/31 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +7.3 | 1e-11 | 14/35 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +7.1 | 8e-11 | 14/28 (SW1417, A549, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.4 | 7e-09 | 16/35 (HepG2/C3A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.35×** | +5.4 | 3e-06 | 8/24 (SW1417, SW 900, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.5 | 3e-04 | 4/18 (SW480, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 6e-04 | 10/35 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.3 | 6e-04 | 8/36 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.100 | 7/35 (NCI-H460, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -6.2 | 2e-07 | 6/36 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.764×** | -6.2 | 2e-07 | 18/36 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.747×** | -5.0 | 1e-04 | 16/33 (AsPC-1, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.803×** | -4.9 | 1e-04 | 17/36 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.786×** | -4.1 | 0.004 | 14/34 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.804×** | -4.1 | 0.004 | 14/35 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.853× | -4.0 | 0.004 | 10/36 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.824×** | -4.0 | 0.004 | 15/36 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.812×** | -3.9 | 0.007 | 11/35 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.831×** | -3.6 | 0.020 | 12/36 (CFPAC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.05 µM |  | **0.830×** | -3.2 | 0.077 | 10/36 (COLO 205, SW48, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.888× | -3.1 | 0.078 | 11/36 (LS 180, LoVo, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **0.828×** | -3.0 | 0.099 | 10/36 (LoVo, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.844× | -3.0 | 0.099 | 12/35 (AsPC-1, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 135 | 3 (1 ⚠) | 11 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +12.2) | [[Trametinib (drug)]] 0.5 µM 0.384× (z -12.5) |
| [[HOP62 (line)]] | alt | 11.0 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 59.7 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 36.9 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 56.7 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.270× (z -13.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 94.0 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.235× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.81× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 63.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 7.72 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 4.28× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.1) | — |
| [[A-172 (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.45× (z +8.6) ⚠ toxic | — |
| [[RKO (line)]] | wt | 16.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 7.89 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0733× (z -10.6) |
| [[SW48 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SULF2]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[EPHA2]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[COL17A1]] | +0.66 | +0.54 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[ACSL5]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TMC7]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[BAIAP2L2]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[KIAA0040]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[SLC22A3]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[MST1R]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[EPHA2-AS1]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NAB1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF2]] | -0.46 | -0.50 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4BPB]] | B | C4BPB activity raises INPP1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 3.63× lower at baseline in the lines without C4BPB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[LINC02582]] | B | LINC02582 activity raises INPP1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.38× lower at baseline in the lines without LINC02582 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[TINAGL1]] | B | TINAGL1 activity raises INPP1's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without TINAGL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[HS3ST1]] | B | HS3ST1 activity raises INPP1's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.95× lower at baseline in the lines without HS3ST1 | 0.021 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[NPSR1]] | B | NPSR1 activity raises INPP1's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.08× lower at baseline in the lines without NPSR1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[SPON1]] | B | SPON1 activity raises INPP1's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.82× lower at baseline in the lines without SPON1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[MAP2K1]] | B | MAP2K1 activity raises INPP1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[TGFA]] | B | TGFA activity raises INPP1's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.24× lower at baseline in the lines without TGFA | 0.033 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[CYP3A5]] | B | CYP3A5 activity raises INPP1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.78× lower at baseline in the lines without CYP3A5 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[IGFL2]] | B | IGFL2 activity raises INPP1's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.25× lower at baseline in the lines without IGFL2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[TFF2]] | B | TFF2 activity raises INPP1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.33× lower at baseline in the lines without TFF2 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[PRSS3]] | B | PRSS3 activity raises INPP1's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without PRSS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLK3]] | B | INPP1 activity raises PLK3's level | lines that do not express INPP1 (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without INPP1 | 0.019 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TGFA]] | B | INPP1 activity raises TGFA's level | lines that do not express INPP1 (12) vs lines expressing it (38) | 3.79× lower at baseline in the lines without INPP1 | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BTBD19]] | B | INPP1 activity raises BTBD19's level | lines that do not express INPP1 (12) vs lines expressing it (38) | 1.46× lower at baseline in the lines without INPP1 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TINAGL1]] | B | INPP1 activity raises TINAGL1's level | lines that do not express INPP1 (12) vs lines expressing it (38) | 4.92× lower at baseline in the lines without INPP1 | 0.056 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ACSL5]] | B | INPP1 activity raises ACSL5's level | lines that do not express INPP1 (12) vs lines expressing it (38) | 3.95× lower at baseline in the lines without INPP1 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.2, 48.9); signed map (5.1, 35.9). **Vector** length 103, 27.6% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.3 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +16.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.8 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -6.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate-1-phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:190,343,570-190,371,665 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 2 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P49441](https://www.uniprot.org/uniprotkb/P49441) (Inositol polyphosphate 1-phosphatase):

> Mg(2+)-dependent phosphatase that catalyzes the hydrolysis of the 1-position phosphate from inositol 1,4-bisphosphate and inositol 1,3,4-trisphosphate and participates in inositol phosphate metabolism.

**Summary**, from NCBI Gene [3628](https://www.ncbi.nlm.nih.gov/gene/3628):

> This gene encodes the enzyme inositol polyphosphate-1-phosphatase, one of the enzymes involved in phosphatidylinositol signaling pathways. This enzyme removes the phosphate group at position 1 of the inositol ring from the polyphosphates inositol 1,4-bisphosphate and inositol 1,3,4-trisphophosphate. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6071) · Entrez [3628](https://www.ncbi.nlm.nih.gov/gene/3628) · UniProt [P49441](https://www.uniprot.org/uniprotkb/P49441) · Ensembl [ENSG00000151689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151689)

## Data

Gene col 7550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7550); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7550]; `tensor/DDL_lfc|DDL_z.npy` [7550]; `embed/gene_vectors.npy` [7550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7550 or target_col == 7550). Every well: [[INPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
