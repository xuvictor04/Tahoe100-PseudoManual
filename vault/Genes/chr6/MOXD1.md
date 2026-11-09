---
symbol: "MOXD1"
type: "gene"
col: 1268
ensembl_id: "ENSG00000079931"
name: "monooxygenase DBH like 1"
location: "6q23.2"
module: 66
arm: "+"
pooled_cpm: 8.85
n_lines_expressing: 25
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 13
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# MOXD1

*monooxygenase DBH like 1* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.95× (z +18.9, q 0e+00, up in 20 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.731× (z -3.9, q 0.056, down in 4 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (A-427 0.0524×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-423 0.308×; ⚠ cell-cycle shift, explains ~30% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (J82 0.0634×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPA4]] (+0.65, fdr 1e-05), [[PPP2R2B]] (+0.64, fdr 7e-06), [[DPYSL3]] (+0.64, fdr 1e-05); moves opposite to [[C16orf91]] (-0.47, fdr 4e-04), [[SPOUT1]] (-0.46, fdr 2e-04), [[CEP89]] (-0.45, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TRPM8]] → it (grade B ⚠); 13 go from it, the strongest it → [[CNN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1268.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.95×** | +18.9 | 0e+00 | 20/21 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +15.3 | 0e+00 | 12/14 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +15.1 | 0e+00 | 10/11 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.31×** | +13.6 | 5e-40 | 12/13 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.85×** | +12.9 | 4e-36 | 19/20 (RPMI-7951, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.7 | 2e-09 | 5/20 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +6.2 | 6e-08 | 5/21 (J82, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +5.7 | 7e-07 | 12/21 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.1 | 2e-05 | 5/18 (CFPAC-1, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.9 | 6e-05 | 3/8 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 1e-04 | 7/19 (A498, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 3e-04 | 7/21 (A-172, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +4.4 | 6e-04 | 3/18 (LoVo, Panc 03.27, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +4.2 | 0.001 | 10/21 (A498, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.002 | 9/20 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.008 | 3/21 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.009 | 6/21 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.012 | 9/20 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.020 | 2/18 (RPMI-7951, A-172) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.044 | 9/21 (C32, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.055 | 6/21 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1268.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (A-427 0.0524×; ⚠ cell-cycle shift, explains ~46% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-423 0.308×; ⚠ cell-cycle shift, explains ~30% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (J82 0.0634×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.731×** | -3.9 | 0.056 | 4/21 (A498, SHP-77, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.762× | -3.4 | 0.21 | 0/22 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1268. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0524× (z -11.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +8.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 154 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 7.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.69× (z +8.6) | — |
| [[J82 (line)]] | alt | 6.46 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0634× (z -11.1) |
| [[SHP-77 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.890 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.817 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.824 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1268), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPA4]] | +0.65 | +0.53 / +0.77 | both halves | 1e-05 | **novel candidate** |
| [[PPP2R2B]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[DPYSL3]] | +0.64 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[HMCN1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[EDIL3]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CHRDL1]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CDH6]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CDH2]] | +0.59 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[POSTN]] | +0.58 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[GUCY1B1]] | +0.58 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[CFI]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NREP]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf91]] | -0.47 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[SPOUT1]] | -0.46 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[CEP89]] | -0.45 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[GCDH]] | -0.45 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[TMEM101]] | -0.45 | -0.24 / -0.51 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 2, C 15. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPM8]] | B | TRPM8 activity raises MOXD1's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without TRPM8 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MOXD1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[FCRLA]] | C | FCRLA activity raises MOXD1's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 5.13× lower at baseline in the lines without FCRLA | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[PRUNE2]] | C | PRUNE2 activity raises MOXD1's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.83× lower at baseline in the lines without PRUNE2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises MOXD1's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 2.88× lower at baseline in the lines without TIMP3 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[PTN]] | C | PTN activity raises MOXD1's level | lines that do not express PTN (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without PTN | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises MOXD1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 4.59× lower at baseline in the lines without ITGA4 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[GPNMB]] | C | GPNMB activity raises MOXD1's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.55× lower at baseline in the lines without GPNMB | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |
| [[MYLK]] | C | MYLK activity raises MOXD1's level | lines that do not express MYLK (20) vs lines expressing it (30) | 2.91× lower at baseline in the lines without MYLK | 0.047 | ⚠ within organs, on part of the lines; also absent: ADAMTS2, COL4A1, CPEB1; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises MOXD1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 3.21× lower at baseline in the lines without IGFBP7 | 0.054 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises MOXD1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without PCDH18 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[PPP2R2B]] | C | PPP2R2B activity raises MOXD1's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without PPP2R2B | 0.076 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNN3]] | B | MOXD1 activity raises CNN3's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 2.22× lower at baseline in the lines without MOXD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1 |
| [[ATXN1-AS1]] | B | MOXD1 activity lowers ATXN1-AS1's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 1.39× higher at baseline in the lines without MOXD1 | 0.065 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1 |
| [[MATN2]] | B | MOXD1 activity raises MATN2's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without MOXD1 | 0.081 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1 |
| [[SEMA6D]] | B | MOXD1 activity raises SEMA6D's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 2.20× lower at baseline in the lines without MOXD1 | 0.0997 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1 |
| [[ANGPT1]] | C | MOXD1 activity raises ANGPT1's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 4.40× lower at baseline in the lines without MOXD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[LAYN]] | C | MOXD1 activity raises LAYN's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 3.45× lower at baseline in the lines without MOXD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[COL1A1]] | C | MOXD1 activity raises COL1A1's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 5.12× lower at baseline in the lines without MOXD1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[IGFBP7]] | C | MOXD1 activity raises IGFBP7's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 6.03× lower at baseline in the lines without MOXD1 | 0.020 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[ITGA4]] | C | MOXD1 activity raises ITGA4's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 4.90× lower at baseline in the lines without MOXD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[GLRB]] | C | MOXD1 activity raises GLRB's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 2.52× lower at baseline in the lines without MOXD1 | 0.047 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[GPNMB]] | C | MOXD1 activity raises GPNMB's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 3.40× lower at baseline in the lines without MOXD1 | 0.070 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[MYLK]] | C | MOXD1 activity raises MYLK's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 3.77× lower at baseline in the lines without MOXD1 | 0.087 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.2, 22.7); signed map (35.8, 33.4). **Vector** length 50.0, 11.4% of its response variance represented; |z| ≥ 3 in 498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +18.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +15.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +12.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | monooxygenase DBH like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:132,296,055-132,401,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564G202, MOX, dJ248E1.1 |
| Gene groups (HGNC) | Dopamine beta-hydroxylase family |
| Matched by | ensembl_id |

UniProt [Q6UVY6](https://www.uniprot.org/uniprotkb/Q6UVY6) carries no function annotation.

**Summary**, from NCBI Gene [26002](https://www.ncbi.nlm.nih.gov/gene/26002):

> Predicted to enable copper ion binding activity and dopamine beta-monooxygenase activity. Predicted to be involved in dopamine catabolic process; norepinephrine biosynthetic process; and octopamine biosynthetic process. Part of endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21063) · Entrez [26002](https://www.ncbi.nlm.nih.gov/gene/26002) · UniProt [Q6UVY6](https://www.uniprot.org/uniprotkb/Q6UVY6) · Ensembl [ENSG00000079931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079931)

## Data

Gene col 1268: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1268); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1268, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1268]; `tensor/DDL_lfc|DDL_z.npy` [1268]; `embed/gene_vectors.npy` [1268]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1268 or target_col == 1268). Every well: [[MOXD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOXD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
