---
symbol: "PHACTR3"
type: "gene"
col: 1508
ensembl_id: "ENSG00000087495"
name: "phosphatase and actin regulator 3"
location: "20q13.32-q13.33"
module: 98
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 34
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# PHACTR3

*phosphatase and actin regulator 3* — 20q13.32-q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.20× (z +18.7, q 0e+00, up in 11 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (BT-474 0.0694×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.0712×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 0.207×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VSTM2L]] (+0.64, fdr 7e-06), [[F5]] (+0.62, fdr 1e-05), [[TNS4]] (+0.62, fdr 1e-05); moves opposite to [[RND1]] (-0.46, fdr 1e-04), [[CBR3-AS1]] (-0.44, fdr 1e-04), [[ATG9B]] (-0.41, fdr 6e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[ABLIM2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.20×** | +18.7 | 0e+00 | 11/16 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +11.6 | 7e-29 | 2/8 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.41×** | +11.5 | 4e-28 | 3/5 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.54×** | +10.6 | 6e-24 | 16/22 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.45×** | +9.2 | 4e-18 | 3/6 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +9.1 | 6e-18 | 7/17 (CFPAC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.21×** | +6.4 | 2e-08 | 8/19 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.0 | 1e-07 | 5/22 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +5.1 | 2e-05 | 12/19 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.34×** | +4.9 | 7e-05 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.8 | 9e-05 | 4/12 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.77×** | +4.5 | 3e-04 | 11/25 (PANC-1, C-33 A, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.83×** | +4.4 | 6e-04 | 1/2 (SW1417) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +4.1 | 0.001 | 1/13 (HEC-1-A) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.61×** | +3.8 | 0.005 | 7/21 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.009 | 5/21 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.56×** | +3.5 | 0.013 | 7/20 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.024 | 5/17 (BT-474, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.066 | 0/21 | inconsistent across doses |  |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.49×** | +3.0 | 0.071 | 0/12 | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.45×** | +2.9 | 0.071 | 5/19 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.29×** | +2.8 | 0.093 | 1/20 (Panc 03.27) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (BT-474 0.0694×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.0712×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 0.207×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 5.46 | 7 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 21.4× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 8.11 | 6 | 0 | [[Triamcinolone (drug)]] 5 µM 6.99× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 14.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.70× (z +13.9) | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0694× (z -10.7) |
| [[KATO III (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0712× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.843 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.727 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.750 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.995 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.750 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.694 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.690 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.721 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.665 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSTM2L]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[F5]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[TNS4]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[FOXQ1]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[RGCC]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[ABLIM2]] | +0.58 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TRIM29]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MAOA]] | +0.56 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[SGPP2]] | +0.54 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[RHOBTB2]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[EVA1C]] | +0.54 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[SERPINA1]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RND1]] | -0.46 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[CBR3-AS1]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ATG9B]] | -0.41 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[CYP27C1]] | -0.41 | -0.51 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PHACTR3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TMEM139]] | B | TMEM139 activity raises PHACTR3's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 1.77× lower at baseline in the lines without TMEM139 | 0.040 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[C6orf132]] | B | C6orf132 activity raises PHACTR3's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 1.81× lower at baseline in the lines without C6orf132 | 0.041 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[TRIM29]] | B | TRIM29 activity raises PHACTR3's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without TRIM29 | 0.053 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[SCNN1A]] | B | SCNN1A activity raises PHACTR3's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 1.95× lower at baseline in the lines without SCNN1A | 0.061 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[ANO4]] | B | ANO4 activity raises PHACTR3's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.01× lower at baseline in the lines without ANO4 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[GJB1]] | B | GJB1 activity raises PHACTR3's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 1.78× lower at baseline in the lines without GJB1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABLIM2]] | B | PHACTR3 activity raises ABLIM2's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without PHACTR3 | 0.045 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[SHROOM3]] | B | PHACTR3 activity raises SHROOM3's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without PHACTR3 | 0.050 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[OVOL2]] | B | PHACTR3 activity raises OVOL2's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without PHACTR3 | 0.068 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[KRT86]] | B | PHACTR3 activity raises KRT86's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without PHACTR3 | 0.075 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[ITPK1]] | B | PHACTR3 activity raises ITPK1's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without PHACTR3 | 0.089 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[TRIM29]] | B | PHACTR3 activity raises TRIM29's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 2.34× lower at baseline in the lines without PHACTR3 | 0.098 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[PDE9A]] | C | PHACTR3 activity raises PDE9A's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 3.04× lower at baseline in the lines without PHACTR3 | 0.068 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.3, 44.1); signed map (10.9, 35.0). **Vector** length 55.8, 12.9% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +18.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.0 | -0.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.0 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.0 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.1 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatase and actin regulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32-q13.33 — chr20:59,577,509-59,847,711 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PPP1R123; previously C20orf101 |
| Gene groups (HGNC) | Phosphatase and actin regulators; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

UniProt [Q96KR7](https://www.uniprot.org/uniprotkb/Q96KR7) carries no function annotation.

**Summary**, from NCBI Gene [116154](https://www.ncbi.nlm.nih.gov/gene/116154):

> This gene encodes a member of the phosphatase and actin regulator protein family. The encoded protein is associated with the nuclear scaffold in proliferating cells, and binds to actin and the catalytic subunit of protein phosphatase-1, suggesting that it functions as a regulatory subunit of protein phosphatase-1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:15833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15833) · Entrez [116154](https://www.ncbi.nlm.nih.gov/gene/116154) · UniProt [Q96KR7](https://www.uniprot.org/uniprotkb/Q96KR7) · Ensembl [ENSG00000087495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087495)

## Data

Gene col 1508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1508); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1508]; `tensor/DDL_lfc|DDL_z.npy` [1508]; `embed/gene_vectors.npy` [1508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1508 or target_col == 1508). Every well: [[PHACTR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHACTR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
