---
symbol: "P2RX7"
type: "gene"
col: 1561
ensembl_id: "ENSG00000089041"
name: "purinergic receptor P2X 7"
location: "12q24.31"
module: 13
arm: "+"
pooled_cpm: 4.04
n_lines_expressing: 32
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 17
direction_downstream: 20
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# P2RX7

*purinergic receptor P2X 7* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +8.7, q 3e-15, up in 4 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +8.0, q 3e-13, up in 24 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.591× (z -4.4, q 0.006, down in 9 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A498 0.286×, H4 0.226×, SNU-423 0.255×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-423 0.216×, RPMI-7951 0.259×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (RPMI-7951 0.178×, H4 0.146×); [[Harringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0807×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP2]] (+0.53, fdr 5e-05), [[DCT]] (+0.52, fdr 4e-05), [[PKD1L1-AS1]] (+0.51, fdr 1e-04); moves opposite to [[E2F3]] (-0.50, fdr 3e-05), [[NHSL1]] (-0.49, fdr 3e-05), [[POC1B]] (-0.47, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[MGP]] → it (grade B ⚠); 20 go from it, the strongest it → [[IFT172]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +8.7 | 3e-15 | 4/13 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +8.3 | 4e-14 | 2/7 (HOP62, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +8.0 | 3e-13 | 24/28 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +6.4 | 2e-08 | 17/25 (HepG2/C3A, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.3 | 1e-05 | 5/25 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.3 | 0.002 | 2/15 (SK-MEL-2, C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.002 | 14/29 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.003 | 9/27 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.003 | 13/27 (SK-MEL-2, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.005 | 12/29 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +3.8 | 0.008 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.008 | 11/26 (H4, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.008 | 17/28 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.025 | 7/27 (H4, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.043 | 6/25 (RPMI-7951, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.044 | 6/29 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.053 | 11/22 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.066 | 4/29 (H4, A-172, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.63×** | +3.0 | 0.072 | 5/21 (C32, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1561.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A498 0.286×, H4 0.226×, SNU-423 0.255×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-423 0.216×, RPMI-7951 0.259×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (RPMI-7951 0.178×, H4 0.146×); [[Harringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.0807×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.591×** | -4.4 | 0.006 | 9/27 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -4.2 | 0.008 | 10/27 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.675× | -3.4 | 0.11 | 3/26 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.704× | -3.1 | 0.29 | 11/29 (H4, SNU-423, …) | top dose only | composition shift |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.688× | -3.0 | 0.29 | 6/28 (hTERT-HPNE, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 36.7 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0479× (z -13.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0807× (z -12.4) |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0922× (z -10.7) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -9.4) |
| [[A498 (line)]] | wt | 12.7 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.14× (z +8.6) | [[AZD2858 (drug)]] 0.5 µM 0.0723× (z -10.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.4) |
| [[A-172 (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.02× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 3.32 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 21.0× (z +8.8) | — |
| [[A-427 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.912 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.794 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP2]] | +0.53 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[DCT]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[PKD1L1-AS1]] | +0.51 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[ABI3BP]] | +0.50 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[SGCD]] | +0.50 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[LDB2]] | +0.50 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PTGFR]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[CA12]] | +0.49 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ARHGAP28]] | +0.49 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[GRIN2A]] | +0.49 | +0.39 / +0.47 | both halves | 5e-05 | STRING 909 |
| [[SLC17A7]] | +0.48 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[KCTD16]] | +0.48 | +0.48 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F3]] | -0.50 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[NHSL1]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[POC1B]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[NUP188]] | -0.43 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[SUV39H2]] | -0.40 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[MSANTD2]] | -0.40 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[ALG8]] | -0.40 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[UTP4]] | -0.39 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[LINC01812]] | -0.39 | -0.40 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 11, C 6. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGP]] | B | MGP activity raises P2RX7's level | lines that do not express MGP (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without MGP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1 |
| [[LINC00698]] | B | LINC00698 activity raises P2RX7's level | lines that do not express LINC00698 (30) vs lines expressing it (20) | 1.70× lower at baseline in the lines without LINC00698 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253642, HEPH, SRRM4; maybe low, not absent |
| [[RARB]] | B | RARB activity raises P2RX7's level | lines that do not express RARB (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without RARB | 0.014 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA |
| [[ARHGAP28]] | B | ARHGAP28 activity raises P2RX7's level | lines that do not express ARHGAP28 (22) vs lines expressing it (28) | 2.56× lower at baseline in the lines without ARHGAP28 | 0.030 | ⚠ within organs, on part of the lines; also absent: RORB, ENSG00000256417, TMTC1 |
| [[CNTN6]] | B | CNTN6 activity raises P2RX7's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 3.10× lower at baseline in the lines without CNTN6 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent |
| [[MAF]] | B | MAF activity raises P2RX7's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.55× lower at baseline in the lines without MAF | 0.058 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[NID2]] | B | NID2 activity raises P2RX7's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.22× lower at baseline in the lines without NID2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[PRUNE2]] | B | PRUNE2 activity raises P2RX7's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 1.93× lower at baseline in the lines without PRUNE2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[KCTD16]] | B | KCTD16 activity raises P2RX7's level | lines that do not express KCTD16 (18) vs lines expressing it (32) | 2.37× lower at baseline in the lines without KCTD16 | 0.087 | ⚠ within organs, on part of the lines; also absent: DMD, DOCK2, PRKD1; maybe low, not absent |
| [[ABI3BP]] | B | ABI3BP activity raises P2RX7's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.15× lower at baseline in the lines without ABI3BP | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[GRIN2A]] | B | GRIN2A activity raises P2RX7's level | lines that do not express GRIN2A (39) vs lines expressing it (11) | 3.47× lower at baseline in the lines without GRIN2A | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000237268, ENSG00000234426, AMPH |
| [[ENPP2]] | C | ENPP2 activity raises P2RX7's level | lines that do not express ENPP2 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without ENPP2 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 15, C 5. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFT172]] | B | P2RX7 activity strengthens IFT172's drug response | lines that do not express P2RX7 (16) vs lines expressing it (30) | the lines without P2RX7 respond 0.52× as strongly (z diff +2.84); strongest at Homoharringtonine 5 µM: 1.03x vs 0.43x (z diff +7.2) | 0.006 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFT172]] | B | P2RX7 activity raises IFT172's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 1.69× lower at baseline in the lines without P2RX7 | 0.017 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[RARB]] | B | P2RX7 activity raises RARB's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 3.09× lower at baseline in the lines without P2RX7 | 0.027 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[CA12]] | B | P2RX7 activity raises CA12's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 3.47× lower at baseline in the lines without P2RX7 | 0.039 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[KCTD16]] | B | P2RX7 activity raises KCTD16's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 3.14× lower at baseline in the lines without P2RX7 | 0.048 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[GPNMB]] | B | P2RX7 activity raises GPNMB's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without P2RX7 | 0.048 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[SEMA6D]] | B | P2RX7 activity raises SEMA6D's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.02× lower at baseline in the lines without P2RX7 | 0.056 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[PRUNE2]] | B | P2RX7 activity raises PRUNE2's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.84× lower at baseline in the lines without P2RX7 | 0.059 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[LINC02476]] | B | P2RX7 activity raises LINC02476's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 3.31× lower at baseline in the lines without P2RX7 | 0.062 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[TUBB2B]] | B | P2RX7 activity raises TUBB2B's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without P2RX7 | 0.065 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[GRIN2A]] | B | P2RX7 activity raises GRIN2A's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without P2RX7 | 0.079 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |
| [[MAF]] | B | P2RX7 activity raises MAF's level | lines that do not express P2RX7 (18) vs lines expressing it (32) | 3.16× lower at baseline in the lines without P2RX7 | 0.080 | ⚠ within organs, on part of the lines; also absent: MLLT11, IGFBP7, GPR158; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.170). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.1, 21.5); signed map (29.7, 46.7). **Vector** length 62.0, 13.5% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | purinergic receptor P2X 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,132,819-121,188,032 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P2X7, MGC20089 |
| Gene groups (HGNC) | Purinergic receptors P2X |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 15 pathways, smallest: Elevation of cytosolic Ca2+ levels; The NLRP3 inflammasome; Inflammasomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99572](https://www.uniprot.org/uniprotkb/Q99572) (P2X purinoceptor 7):

> ATP-gated nonselective transmembrane cation channel that requires high millimolar concentrations of ATP for activation. Upon ATP binding, it rapidly opens to allow the influx of small cations Na(+) and Ca(2+), and the K(+) efflux. Also has the ability to form a large pore in the cell membrane, allowing the passage of large cationic molecules. In microglia, may mediate NADPH transport across the plasma membrane. In immune cells, P2RX7 acts as a molecular sensor in pathological inflammatory …

**Summary**, from NCBI Gene [5027](https://www.ncbi.nlm.nih.gov/gene/5027):

> The product of this gene belongs to the family of purinoceptors for ATP. This receptor functions as a ligand-gated ion channel and is responsible for ATP-dependent lysis of macrophages through the formation of membrane pores permeable to large molecules. Activation of this nuclear receptor by ATP in the cytoplasm may be a mechanism by which cellular activity can be coupled to changes in gene expression. Multiple alternatively spliced variants have been identified, most of which fit …

**Accessions** — [HGNC:8537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8537) · Entrez [5027](https://www.ncbi.nlm.nih.gov/gene/5027) · UniProt [Q99572](https://www.uniprot.org/uniprotkb/Q99572) · Ensembl [ENSG00000089041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089041)

## Data

Gene col 1561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1561); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1561]; `tensor/DDL_lfc|DDL_z.npy` [1561]; `embed/gene_vectors.npy` [1561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1561 or target_col == 1561). Every well: [[P2RX7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P2RX7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
