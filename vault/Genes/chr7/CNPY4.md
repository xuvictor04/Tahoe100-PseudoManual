---
symbol: "CNPY4"
type: "gene"
col: 9402
ensembl_id: "ENSG00000166997"
name: "canopy FGF signaling regulator 4"
location: "7q22.1"
module: 13
arm: "+"
pooled_cpm: 3.69
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CNPY4

*canopy FGF signaling regulator 4* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.51× (z +21.3, q 0e+00, up in 35 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.446× (z -8.1, q 4e-13, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GALNT1]] (+0.59, fdr 1e-05), [[CERCAM]] (+0.58, fdr 3e-05), [[COL1A2]] (+0.54, fdr 5e-05); moves opposite to [[WDR75]] (-0.48, fdr 9e-05), [[WDR35]] (-0.44, fdr 1e-04), [[C5orf63]] (-0.43, fdr 4e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[MAP1A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +21.3 | 0e+00 | 35/37 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +13.0 | 3e-36 | 6/6 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.20×** | +11.6 | 6e-29 | 17/20 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.82×** | +10.4 | 5e-23 | 34/46 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.62×** | +9.6 | 7e-20 | 28/43 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.26×** | +8.2 | 3e-14 | 26/46 (KATO III, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.23×** | +7.4 | 1e-11 | 7/8 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.90×** | +6.2 | 5e-08 | 18/33 (SW480, NCI-H2030, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.85×** | +5.9 | 2e-07 | 15/36 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +5.4 | 4e-06 | 4/18 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +5.0 | 3e-05 | 17/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.9 | 5e-05 | 14/47 (MIA PaCa-2, HS-578T, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +4.7 | 1e-04 | 13/40 (hTERT-HPNE, PANC-1, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.3 | 8e-04 | 9/40 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +4.2 | 9e-04 | 12/33 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.004 | 9/47 (HT-29, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.005 | 5/41 (SK-MEL-2, SW 900, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.050 | 3/42 (RKO, J82, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.076 | 5/39 (SW480, AsPC-1, …) | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.37×** | +2.9 | 0.092 | 3/30 (NCI-H2030, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -8.1 | 4e-13 | 27/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -6.8 | 3e-09 | 23/44 (NCI-H460, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.521×** | -6.5 | 1e-08 | 19/43 (LOX-IMVI, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -6.4 | 2e-08 | 19/33 (RPMI-7951, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -5.5 | 5e-06 | 21/44 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.598×** | -5.2 | 2e-05 | 13/33 (LOX-IMVI, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.604×** | -5.0 | 4e-05 | 20/47 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.672×** | -4.0 | 0.005 | 4/34 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.678×** | -3.9 | 0.006 | 17/46 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.686×** | -3.5 | 0.026 | 8/31 (LOX-IMVI, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.726×** | -3.2 | 0.068 | 13/45 (SW 900, C32, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | **0.799×** | -3.2 | 0.068 | 5/47 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.721×** | -3.2 | 0.069 | 12/38 (J82, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.653×** | -3.0 | 0.093 | 3/47 (NCI-H460, C-33 A, …) | two highest doses | noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | **0.732×** | -3.0 | 0.099 | 13/41 (H4, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.46 | 0 | 2 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0681× (z -11.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -9.2) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 2.63 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.0579× (z -8.8) |
| [[HT-29 (line)]] | alt | 2.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 3.32 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0695× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 2.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 2.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +9.4) | — |
| [[SW480 (line)]] | alt | 7.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +13.2) | — |
| [[A-427 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALNT1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CERCAM]] | +0.58 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[COL1A2]] | +0.54 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[MAP1A]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[RNF167]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ECM1]] | +0.53 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[IGFBP6]] | +0.52 | +0.41 / +0.34 | both halves | 1e-04 |  |
| [[ARHGEF6]] | +0.51 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[LOXL1]] | +0.50 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[SERPINH1]] | +0.50 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[RTL8C]] | +0.50 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[B3GNT9]] | +0.49 | +0.60 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR75]] | -0.48 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[WDR35]] | -0.44 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[C5orf63]] | -0.43 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[SFXN4]] | -0.42 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[CALML4]] | -0.41 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[NCBP2]] | -0.41 | -0.18 / -0.52 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SDHAP3]] | -0.40 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[BTNL9]] | -0.40 | -0.40 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1A]] | B | MAP1A activity raises CNPY4's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 1.89× lower at baseline in the lines without MAP1A | 0.006 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| [[SIRPA]] | B | SIRPA activity raises CNPY4's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 1.92× lower at baseline in the lines without SIRPA | 0.007 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[SYNGR1]] | B | SYNGR1 activity raises CNPY4's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 1.89× lower at baseline in the lines without SYNGR1 | 0.012 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[APLP1]] | B | APLP1 activity raises CNPY4's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.67× lower at baseline in the lines without APLP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[COL3A1]] | B | COL3A1 activity raises CNPY4's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.94× lower at baseline in the lines without COL3A1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[COL1A2]] | B | COL1A2 activity raises CNPY4's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 1.83× lower at baseline in the lines without COL1A2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[SHOX2]] | B | SHOX2 activity raises CNPY4's level | lines that do not express SHOX2 (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without SHOX2 | 0.020 | ⚠ within organs, on part of the lines; also absent: NRG2, ADAMTSL1, TTC7B |
| [[TOP2A]] | B | TOP2A activity lowers CNPY4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FBLN1]] | B | FBLN1 activity raises CNPY4's level | lines that do not express FBLN1 (20) vs lines expressing it (30) | 1.44× lower at baseline in the lines without FBLN1 | 0.037 | ⚠ within organs, on part of the lines; also absent: GJA1, PCSK1N, MLLT11 |
| [[B4GALNT1]] | B | B4GALNT1 activity raises CNPY4's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without B4GALNT1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[DZIP1L]] | B | DZIP1L activity raises CNPY4's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without DZIP1L | 0.074 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[WDR35]] | B | WDR35 activity raises CNPY4's level | lines that do not express WDR35 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without WDR35 | 0.084 | ⚠ within organs, on part of the lines; also absent: AGK, DUSP19, ENTPD1-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.327). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (56.9, 18.0); signed map (52.7, -16.8). **Vector** length 49.5, 5.94% of its response variance represented; |z| ≥ 3 in 1,189 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +21.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +2.8 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | -0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -6.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | canopy FGF signaling regulator 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,119,634-100,125,508 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40499, PRAT4B |
| Gene groups (HGNC) | Canopy FGF signaling regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N129](https://www.uniprot.org/uniprotkb/Q8N129) (Protein canopy homolog 4):

> Plays a role in the regulation of the cell surface expression of TLR4.

**Summary**, from NCBI Gene [245812](https://www.ncbi.nlm.nih.gov/gene/245812):

> Predicted to enable signaling receptor binding activity. Involved in positive regulation of protein localization to plasma membrane. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28631) · Entrez [245812](https://www.ncbi.nlm.nih.gov/gene/245812) · UniProt [Q8N129](https://www.uniprot.org/uniprotkb/Q8N129) · Ensembl [ENSG00000166997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166997)

## Data

Gene col 9402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9402); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9402]; `tensor/DDL_lfc|DDL_z.npy` [9402]; `embed/gene_vectors.npy` [9402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9402 or target_col == 9402). Every well: [[CNPY4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNPY4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
