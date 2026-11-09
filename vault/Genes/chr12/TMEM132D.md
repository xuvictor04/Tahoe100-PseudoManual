---
symbol: "TMEM132D"
type: "gene"
col: 7583
ensembl_id: "ENSG00000151952"
name: "transmembrane protein 132D"
location: "12q24.33"
module: 13
arm: "+"
pooled_cpm: 11.38
n_lines_expressing: 21
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 14
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# TMEM132D

*transmembrane protein 132D* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.88× (z +30.1, q 0e+00, up in 13 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 0.209×, RPMI-7951 0.298×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-423 0.137×, RPMI-7951 0.201×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-423 0.142×, RPMI-7951 0.182×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.198×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.269×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSTL4]] (+0.61, fdr 7e-06), [[OR9Q1]] (+0.58, fdr 2e-05), [[RBFOX1]] (+0.57, fdr 1e-05); moves opposite to [[INPP5D]] (-0.58, fdr 2e-05), [[LINC01551]] (-0.51, fdr 2e-04), [[TANC1]] (-0.49, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CSF1R]] → it (grade C ⚠); 14 go from it, the strongest it → [[UBAC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.88×** | +30.1 | 0e+00 | 13/16 (Panc 03.27, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +16.4 | 0e+00 | 10/16 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +12.9 | 1e-35 | 3/7 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.27×** | +12.8 | 2e-35 | 14/18 (SW480, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.16×** | +12.2 | 2e-32 | 0/3 | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +12.1 | 6e-32 | 1/3 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.79×** | +11.3 | 7e-28 | 12/16 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.85×** | +11.1 | 6e-27 | 13/16 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +9.0 | 1e-17 | 13/19 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +8.2 | 1e-14 | 13/17 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +7.6 | 2e-12 | 9/17 (RPMI-7951, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +7.3 | 1e-11 | 11/18 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +6.2 | 2e-08 | 9/17 (LS 180, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.83×** | +6.0 | 8e-08 | 10/17 (HEC-1-A, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +5.8 | 3e-07 | 10/17 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.8 | 5e-05 | 1/15 (SW480) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.4 | 4e-04 | 2/17 (SW480, KATO III) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.004 | 1/11 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7583.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SNU-423 0.209×, RPMI-7951 0.298×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-423 0.137×, RPMI-7951 0.201×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-423 0.142×, RPMI-7951 0.182×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.198×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.269×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -3.8 | 0.091 | 3/19 (SW1417, SHP-77, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.737× | -3.4 | 0.14 | 4/17 (SNU-423, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.807× | -3.4 | 0.14 | 5/18 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.750× | -3.2 | 0.19 | 6/14 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Monocrotaline (drug)]] 5 µM |  | 0.749× | -3.1 | 0.19 | 3/16 (LS 180, HepG2/C3A, …) | rises with dose |  |
| [[Cilostazol (drug)]] 0.05 µM |  | 0.740× | -3.1 | 0.19 | 2/16 (COLO 205, SK-MEL-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 308 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 21.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +15.8) | — |
| [[LS 180 (line)]] | wt | 3.95 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.9× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.6) |
| [[COLO 205 (line)]] | alt | 8.24 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.2× (z +16.0) | — |
| [[KATO III (line)]] | alt | 3.28 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.6× (z +14.9) | — |
| [[SW480 (line)]] | alt | 2.89 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 11.6× (z +14.3) | — |
| [[HepG2_C3A (line)]] | wt | 3.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 75.5× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 3.49 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 14.0× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.6× (z +16.3) | — |
| [[SHP-77 (line)]] | alt | 4.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.2× (z +15.3) | — |
| [[SW1417 (line)]] | alt | 2.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +9.6) | — |
| [[A-172 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSTL4]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[OR9Q1]] | +0.58 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[RBFOX1]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ABCA1]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CSF1R]] | +0.54 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[SLC41A2]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[COL26A1]] | +0.53 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ANKRD20A9P]] | +0.52 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SPOCD1]] | +0.52 | +0.50 / +0.46 | both halves | 2e-05 | same gene group |
| [[RNF223]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[KCNMA1]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[NBPF14]] | +0.51 | +0.41 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5D]] | -0.58 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[LINC01551]] | -0.51 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[TANC1]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[B3GNT3]] | -0.49 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[EPS8L3]] | -0.48 | -0.59 / -0.26 | both halves | 3e-04 |  |
| [[ZDHHC3]] | -0.48 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[IL20RA]] | -0.48 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[USP6NL]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[EDAR]] | -0.46 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[SYK]] | -0.46 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[MST1R]] | -0.45 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[UBAC2]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSF1R]] | C | CSF1R activity raises TMEM132D's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without CSF1R | 0.095 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 7, C 7. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBAC2]] | B | TMEM132D activity raises UBAC2's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without TMEM132D | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |
| [[KCNAB1]] | B | TMEM132D activity raises KCNAB1's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.29× lower at baseline in the lines without TMEM132D | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |
| [[CCDC144NL-1]] | B | TMEM132D activity raises CCDC144NL-1's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 2.23× lower at baseline in the lines without TMEM132D | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |
| [[LENG1]] | B | TMEM132D activity raises LENG1's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.19× lower at baseline in the lines without TMEM132D | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |
| [[USP6NL]] | B | TMEM132D activity weakens USP6NL's drug response | lines that do not express TMEM132D (29) vs lines expressing it (20) | the lines without TMEM132D respond 1.29× as strongly (z diff -0.47); strongest at Harringtonine 5 µM: 1.62x vs 1.15x (z diff -2.9) | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NOTCH2NLA]] | B | TMEM132D activity lowers NOTCH2NLA's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.41× higher at baseline in the lines without TMEM132D | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |
| [[MST1R]] | B | TMEM132D activity raises MST1R's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without TMEM132D | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent |
| [[FAM83F]] | C | TMEM132D activity raises FAM83F's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 2.45× lower at baseline in the lines without TMEM132D | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[SYK]] | C | TMEM132D activity raises SYK's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 2.59× lower at baseline in the lines without TMEM132D | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[B3GNT3]] | C | TMEM132D activity raises B3GNT3's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without TMEM132D | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[C9orf152]] | C | TMEM132D activity raises C9orf152's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without TMEM132D | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[ESRP1]] | C | TMEM132D activity raises ESRP1's level | lines that do not express TMEM132D (29) vs lines expressing it (21) | 2.74× lower at baseline in the lines without TMEM132D | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000271955, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.490). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.9, 19.8); signed map (27.9, 15.1). **Vector** length 47.0, 11.0% of its response variance represented; |z| ≥ 3 in 522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.0 | +11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +0.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.3 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.1 | +4.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -0.9 | +2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -0.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 132D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:129,071,725-129,904,025 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1944, MOLT, PPP1R153 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14C87](https://www.uniprot.org/uniprotkb/Q14C87) (Transmembrane protein 132D):

> Regulate neuronals morphology via inhibition of the WAVE regulatory complex (WCR), a complex that controls F-actin cytoskeletal dynamics.

**Summary**, from NCBI Gene [121256](https://www.ncbi.nlm.nih.gov/gene/121256):

> Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29411) · Entrez [121256](https://www.ncbi.nlm.nih.gov/gene/121256) · UniProt [Q14C87](https://www.uniprot.org/uniprotkb/Q14C87) · Ensembl [ENSG00000151952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151952)

## Data

Gene col 7583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7583); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7583]; `tensor/DDL_lfc|DDL_z.npy` [7583]; `embed/gene_vectors.npy` [7583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7583 or target_col == 7583). Every well: [[TMEM132D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM132D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
