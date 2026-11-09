---
symbol: "NPTXR"
type: "gene"
col: 13315
ensembl_id: "ENSG00000221890"
name: "neuronal pentraxin receptor"
location: "22q13.1"
module: 50
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 39
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 10
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# NPTXR

*neuronal pentraxin receptor* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.95× (z +18.3, q 0e+00, up in 34 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.668× (z -4.6, q 0.003, down in 13 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 1 line (A-172 0.0719×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.219×); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0575×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OLFML2A]] (+0.56, fdr 3e-05), [[CLSTN1]] (+0.55, fdr 2e-04), [[SEPTIN3]] (+0.54, fdr 2e-05); moves opposite to [[IFT43]] (-0.48, fdr 2e-04), [[TRMT44]] (-0.48, fdr 2e-04), [[MEF2B]] (-0.48, fdr 8e-04, ⚠ not reproduced), [[SLC38A9]] (-0.48, fdr 1e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); 10 go from it, the strongest it → [[GJA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.95×** | +18.3 | 0e+00 | 34/36 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.83×** | +16.1 | 0e+00 | 19/19 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +13.2 | 1e-37 | 6/8 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.83×** | +11.5 | 2e-28 | 9/11 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.48×** | +10.9 | 2e-25 | 25/34 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +7.2 | 5e-11 | 13/19 (HepG2/C3A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +7.1 | 8e-11 | 19/36 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +6.8 | 6e-10 | 17/36 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +6.6 | 2e-09 | 10/36 (SW480, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.2 | 9e-06 | 13/36 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +4.5 | 3e-04 | 8/36 (PANC-1, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.5 | 3e-04 | 9/30 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **1.30×** | +4.4 | 4e-04 | 6/36 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 5e-04 | 7/35 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.97×** | +4.2 | 8e-04 | 5/27 (LoVo, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 5/36 (NCI-H23, PANC-1, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.007 | 10/34 (SW48, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.010 | 6/36 (A-172, BT-474, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.010 | 5/28 (PANC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.015 | 6/26 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13315.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 1 line (A-172 0.0719×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.219×); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0575×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.668×** | -4.6 | 0.003 | 13/34 (SNU-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -4.0 | 0.015 | 13/35 (A-427, SW480, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -3.7 | 0.042 | 12/37 (LoVo, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.10 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0719× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.158× (z -9.3) |
| [[H4 (line)]] | wt | 9.24 | 0 | 1 | — | [[Busulfan (drug)]] 0.5 µM 0.0824× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 2.29 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.07× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 31.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.29× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 3.69 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0575× (z -10.2) |
| [[SW480 (line)]] | alt | 6.76 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.27× (z +10.0) | — |
| [[A-427 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.828 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.821 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.904 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLFML2A]] | +0.56 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[CLSTN1]] | +0.55 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[SEPTIN3]] | +0.54 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[REEP2]] | +0.51 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[ENPP1]] | +0.51 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[CCDC69]] | +0.51 | +0.21 / +0.58 | both halves | 6e-04 |  |
| [[CELSR2]] | +0.51 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[APLP1]] | +0.51 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[CREG1]] | +0.50 | +0.47 / +0.53 | both halves | 2e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[SGCB]] | +0.50 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[CYP2U1]] | +0.50 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[TMSB4X]] | +0.50 | +0.22 / +0.48 | both halves | 6e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT43]] | -0.48 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[TRMT44]] | -0.48 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[MEF2B]] | -0.48 | -0.19 / -0.42 | ⚠ not reproduced | 8e-04 |  |
| [[SLC38A9]] | -0.48 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[DCLRE1C]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[WAPL]] | -0.46 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[C16orf91]] | -0.45 | -0.20 / -0.39 | both halves | 7e-04 |  |
| [[PHF5A]] | -0.45 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[RECQL5]] | -0.45 | -0.21 / -0.48 | both halves | 6e-04 |  |
| [[ZBTB49]] | -0.42 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[LIN52]] | -0.42 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[DHRS7B]] | -0.42 | -0.32 / -0.26 | both halves | 4e-04 |  |
| [[BFAR]] | -0.42 | -0.39 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises NPTXR's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without SEMA6B | 0.009 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[APLP1]] | B | APLP1 activity raises NPTXR's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without APLP1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[CCDC69]] | B | CCDC69 activity lowers NPTXR's level | lines that do not express CCDC69 (11) vs lines expressing it (39) | 1.23× higher at baseline in the lines without CCDC69 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises NPTXR's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GXYLT2]] | B | GXYLT2 activity raises NPTXR's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without GXYLT2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[EFR3B]] | B | EFR3B activity raises NPTXR's level | lines that do not express EFR3B (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without EFR3B | 0.062 | ⚠ within organs, on part of the lines; also absent: RTN4RL1, SEPTIN5, NT5M; maybe low, not absent |
| [[ADGRA2]] | B | ADGRA2 activity raises NPTXR's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 2.18× lower at baseline in the lines without ADGRA2 | 0.0998 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GJA3]] | B | NPTXR activity raises GJA3's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 2.07× lower at baseline in the lines without NPTXR | 0.038 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[DISP3]] | B | NPTXR activity raises DISP3's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without NPTXR | 0.040 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[CYP2U1]] | B | NPTXR activity raises CYP2U1's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without NPTXR | 0.040 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[CTSV]] | B | NPTXR activity raises CTSV's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without NPTXR | 0.042 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[GRIK4]] | B | NPTXR activity raises GRIK4's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without NPTXR | 0.051 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[SEPTIN3]] | B | NPTXR activity raises SEPTIN3's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without NPTXR | 0.060 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[LIN52]] | B | NPTXR activity raises LIN52's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without NPTXR | 0.067 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[ATP1A3]] | B | NPTXR activity raises ATP1A3's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without NPTXR | 0.068 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[REEP2]] | B | NPTXR activity raises REEP2's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without NPTXR | 0.070 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[CD83]] | B | NPTXR activity raises CD83's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.96× lower at baseline in the lines without NPTXR | 0.070 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.368). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.8, 36.0); signed map (21.7, 21.7). **Vector** length 48.3, 6.82% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +18.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.0 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.6 | -4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | -2.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | neuronal pentraxin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,818,452-38,844,028 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [O95502](https://www.uniprot.org/uniprotkb/O95502) (Neuronal pentraxin receptor):

> May be involved in mediating uptake of synaptic material during synapse remodeling or in mediating the synaptic clustering of AMPA glutamate receptors at a subset of excitatory synapses.

**Summary**, from NCBI Gene [23467](https://www.ncbi.nlm.nih.gov/gene/23467):

> This gene encodes a protein similar to the rat neuronal pentraxin receptor. The rat pentraxin receptor is an integral membrane protein that is thought to mediate neuronal uptake of the snake venom toxin, taipoxin, and its transport into the synapses. Studies in rat indicate that translation of this mRNA initiates at a non-AUG (CUG) codon. This may also be true for mouse and human, based on strong sequence conservation amongst these species. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7954) · Entrez [23467](https://www.ncbi.nlm.nih.gov/gene/23467) · UniProt [O95502](https://www.uniprot.org/uniprotkb/O95502) · Ensembl [ENSG00000221890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221890)

## Data

Gene col 13315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13315); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13315]; `tensor/DDL_lfc|DDL_z.npy` [13315]; `embed/gene_vectors.npy` [13315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13315 or target_col == 13315). Every well: [[NPTXR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPTXR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
