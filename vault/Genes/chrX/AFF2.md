---
symbol: "AFF2"
type: "gene"
col: 7934
ensembl_id: "ENSG00000155966"
name: "ALF transcription elongation factor 2"
location: "Xq28"
module: 61
arm: "+"
pooled_cpm: 4.23
n_lines_expressing: 25
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# AFF2

*ALF transcription elongation factor 2* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.66× (z +17.9, q 0e+00, up in 18 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.253×, SW 900 0.250×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.119×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1792 0.194×; ⚠ toxic; transcription drop); [[Oxaprozin (drug)]] 0.5 µM in 1 line (CHP-212 0.0692×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS6ST3]] (+0.67, fdr 1e-05), [[ASXL3]] (+0.61, fdr 2e-05), [[MTUS2]] (+0.58, fdr 2e-05); moves opposite to [[EFCAB11]] (-0.46, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GRIK2]] → it (grade B ⚠); 9 go from it, the strongest it → [[FAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.66×** | +17.9 | 0e+00 | 18/22 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.99×** | +12.9 | 7e-36 | 1/6 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +11.1 | 2e-26 | 2/12 (SNU-423, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +11.0 | 5e-26 | 5/18 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +10.2 | 2e-22 | 6/19 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.70×** | +9.4 | 5e-19 | 15/20 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +9.3 | 8e-19 | 3/7 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +7.6 | 2e-12 | 9/20 (A-172, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +5.2 | 1e-05 | 15/22 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +4.7 | 1e-04 | 14/21 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +4.4 | 6e-04 | 12/22 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.86×** | +4.3 | 8e-04 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.1 | 0.002 | 0/12 | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.002 | 10/21 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.005 | 0/12 | inconsistent across doses | low cells (technical?) |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.013 | 1/20 (HT-29) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.017 | 4/21 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.022 | 5/20 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.027 | 6/22 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.030 | 2/16 (A498, A549) | top dose only | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7934.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1792 0.253×, SW 900 0.250×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.119×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1792 0.194×; ⚠ toxic; transcription drop); [[Oxaprozin (drug)]] 0.5 µM in 1 line (CHP-212 0.0692×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.709× | -3.3 | 0.61 | 3/19 (NCI-H1573, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.2 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.03× (z +10.6) | — |
| [[SW480 (line)]] | alt | 5.63 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 9.92× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 62.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -13.0) |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0692× (z -9.0) |
| [[PANC-1 (line)]] | alt | 4.70 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.83× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -9.8) |
| [[SW1417 (line)]] | alt | 4.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.2× (z +11.7) | — |
| [[A-172 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.813 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.928 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.569 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.946 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.793 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS6ST3]] | +0.67 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ASXL3]] | +0.61 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[MTUS2]] | +0.58 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ZNF385D]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ZMAT4]] | +0.57 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[SUSD4]] | +0.56 | +0.38 / +0.65 | both halves | 7e-05 |  |
| [[SEMA6D]] | +0.56 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[KCNJ6]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[GRIK2]] | +0.56 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[SYN1]] | +0.55 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[SNAP91]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[PLXNA4]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB11]] | -0.46 | -0.35 / -0.57 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIK2]] | B | GRIK2 activity raises AFF2's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 2.23× lower at baseline in the lines without GRIK2 | 0.050 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[P2RY1]] | B | P2RY1 activity lowers AFF2's level | lines that do not express P2RY1 (21) vs lines expressing it (29) | 1.10× higher at baseline in the lines without P2RY1 | 0.066 | ⚠ within organs, on part of the lines; also absent: RGS2, FGF14, BASP1-AS1 |
| [[ZNF385D]] | C | ZNF385D activity raises AFF2's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.42× lower at baseline in the lines without ZNF385D | 0.043 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[TMEM163]] | C | TMEM163 activity raises AFF2's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.03× lower at baseline in the lines without TMEM163 | 0.057 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[SNAP91]] | C | SNAP91 activity raises AFF2's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without SNAP91 | 0.080 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAT3]] | B | AFF2 activity raises FAT3's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.79× lower at baseline in the lines without AFF2 | 0.012 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent |
| [[COL26A1]] | B | AFF2 activity raises COL26A1's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.70× lower at baseline in the lines without AFF2 | 0.037 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent |
| [[ADAMTS15]] | B | AFF2 activity raises ADAMTS15's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without AFF2 | 0.053 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent |
| [[MIR325HG]] | B | AFF2 activity raises MIR325HG's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.56× lower at baseline in the lines without AFF2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent |
| [[TMEM163]] | C | AFF2 activity raises TMEM163's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 2.96× lower at baseline in the lines without AFF2 | 0.004 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |
| [[CHGB]] | C | AFF2 activity raises CHGB's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 2.40× lower at baseline in the lines without AFF2 | 0.029 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |
| [[LINC01194]] | C | AFF2 activity raises LINC01194's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 2.54× lower at baseline in the lines without AFF2 | 0.031 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |
| [[JAKMIP1]] | C | AFF2 activity raises JAKMIP1's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without AFF2 | 0.069 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |
| [[XKR7]] | C | AFF2 activity raises XKR7's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without AFF2 | 0.084 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, 33.5); signed map (32.5, 31.9). **Vector** length 39.5, 7.31% of its response variance represented; |z| ≥ 3 in 520 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +17.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +7.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +0.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.8 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ALF transcription elongation factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:148,500,617-149,000,663 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FRAXE; previously FMR2 |
| Gene groups (HGNC) | AF4/FMR2 family; Super elongation complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P51816](https://www.uniprot.org/uniprotkb/P51816) (AF4/FMR2 family member 2):

> RNA-binding protein. Might be involved in alternative splicing regulation through an interaction with G-quartet RNA structure.

**Summary**, from NCBI Gene [2334](https://www.ncbi.nlm.nih.gov/gene/2334):

> This gene encodes a putative transcriptional activator that is a member of the AF4\FMR2 gene family. This gene is associated with the folate-sensitive fragile X E locus on chromosome X. A repeat polymorphism in the fragile X E locus results in silencing of this gene causing Fragile X E syndrome. Fragile X E syndrome is a form of nonsyndromic X-linked cognitive disability. In addition, this gene contains 6-25 GCC repeats that are expanded to >200 repeats in the disease state. Alternate splicing …

**Accessions** — [HGNC:3776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3776) · Entrez [2334](https://www.ncbi.nlm.nih.gov/gene/2334) · UniProt [P51816](https://www.uniprot.org/uniprotkb/P51816) · Ensembl [ENSG00000155966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155966)

## Data

Gene col 7934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7934); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7934]; `tensor/DDL_lfc|DDL_z.npy` [7934]; `embed/gene_vectors.npy` [7934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7934 or target_col == 7934). Every well: [[AFF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
