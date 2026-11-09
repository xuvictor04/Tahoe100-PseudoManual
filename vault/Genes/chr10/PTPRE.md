---
symbol: "PTPRE"
type: "gene"
col: 5302
ensembl_id: "ENSG00000132334"
name: "protein tyrosine phosphatase receptor type E"
location: "10q26.2"
module: 34
arm: "+"
pooled_cpm: 62.83
n_lines_expressing: 37
n_dd_up: 2
n_dd_down: 53
n_dd_up_clean: 1
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 38
direction_downstream: 34
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PTPRE

*protein tyrosine phosphatase receptor type E* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Sapanisertib (drug)]] 0.05 µM: 1.32× (z +4.2, q 0.009, up in 18 of 35 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 1.20× (z +4.1, q 0.009, up in 9 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 4.36×).
> Pooled over the cell lines (median), lowered significantly by 53 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.270× (z -30.0, q 0e+00, down in 34 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGFA]] (+0.65, fdr 7e-06), [[EPHB6]] (+0.64, fdr 7e-06), [[ABTB3]] (+0.61, fdr 7e-06); moves opposite to [[PUS10]] (-0.55, fdr 6e-05), [[DCLK2]] (-0.54, fdr 3e-05), [[CNTNAP1]] (-0.53, fdr 2e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); 34 go from it, the strongest it → [[RAC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5302.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 4.36×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +4.2 | 0.009 | 18/35 (Hs 766T, J82, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +4.1 | 0.009 | 9/35 (Hs 766T, J82, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.58×** | +3.9 | 0.021 | 18/35 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.24× | +3.4 | 0.11 | 12/35 (SW480, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 53 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5302.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.270×** | -30.0 | 0e+00 | 34/35 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.394×** | -21.3 | 0e+00 | 33/36 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.468×** | -12.3 | 2e-32 | 24/35 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.483×** | -11.3 | 1e-27 | 25/35 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.491×** | -11.1 | 1e-26 | 28/34 (SW480, COLO 205, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.565×** | -9.2 | 2e-18 | 25/35 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -9.2 | 3e-18 | 25/35 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.554×** | -8.8 | 6e-17 | 21/29 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.573×** | -8.7 | 3e-16 | 19/28 (Hs 766T, LS 180, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -8.2 | 1e-14 | 23/37 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.384×** | -8.1 | 3e-14 | 26/35 (SK-MEL-2, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.610×** | -8.0 | 7e-14 | 24/35 (LS 180, SW48, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -7.9 | 9e-14 | 23/36 (SW 900, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.640×** | -7.2 | 2e-11 | 25/35 (LoVo, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.665×** | -7.2 | 2e-11 | 20/37 (HOP62, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.643×** | -7.1 | 3e-11 | 20/35 (LoVo, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.645×** | -7.1 | 4e-11 | 23/35 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.673×** | -6.2 | 2e-08 | 20/36 (HOP62, CHP-212, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.487×** | -6.1 | 3e-08 | 26/35 (AsPC-1, CHP-212, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.523×** | -5.5 | 1e-06 | 21/35 (LoVo, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.714×** | -5.4 | 1e-06 | 19/35 (LS 180, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 118 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -36.3) |
| [[LS 180 (line)]] | wt | 256 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -25.6) |
| [[HOP62 (line)]] | alt | 86.0 | 0 | 13 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -21.9) |
| [[CHP-212 (line)]] | wt | 328 | 0 | 11 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 191 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -21.7) |
| [[SW480 (line)]] | alt | 144 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -19.2) |
| [[NCI-H1792 (line)]] | alt | 106 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -22.4) |
| [[SW 900 (line)]] | alt | 168 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -20.6) |
| [[CFPAC-1 (line)]] | alt | 168 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -27.8) |
| [[J82 (line)]] | alt | 53.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.6) |
| [[SW48 (line)]] | wt | 59.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.3) |
| [[A-427 (line)]] | wt | 30.2 | 0 | 5 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0622× (z -19.2) |
| [[A498 (line)]] | wt | 72.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -18.0) |
| [[COLO 205 (line)]] | alt | 53.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -19.6) |
| [[HEC-1-A (line)]] | alt | 28.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.0) |
| [[Hs 766T (line)]] | wt | 81.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0392× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -20.2) |
| [[KATO III (line)]] | alt | 102 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 157 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -19.0) |
| [[AsPC-1 (line)]] | alt | 63.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -17.1) |
| [[HT-29 (line)]] | alt | 42.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 46.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.9) |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 69.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -13.2) |
| [[NCI-H596 (line)]] | alt | 64.2 | 1 | 1 (1 ⚠) | [[Trametinib (drug)]] 5 µM 4.36× (z +12.1) | [[Pentoxifylline (drug)]] 0.05 µM 0.293× (z -9.7) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -16.1) |
| [[SNU-423 (line)]] | alt | 63.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -14.1) |
| [[SW1417 (line)]] | alt | 73.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -12.2) |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -11.7) |
| [[A-172 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFA]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[EPHB6]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ABTB3]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[RAC2]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ST3GAL1]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[LINC02813]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CD44]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MYEOV]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SIGLEC15]] | +0.56 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[PODXL]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ADGRE2]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS10]] | -0.55 | -0.61 / -0.39 | both halves | 6e-05 |  |
| [[DCLK2]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[CNTNAP1]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 35, C 3. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity raises PTPRE's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without TINAGL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[TMCC3]] | B | TMCC3 activity raises PTPRE's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 2.76× lower at baseline in the lines without TMCC3 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[CARD11]] | B | CARD11 activity raises PTPRE's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without CARD11 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[WNT7B]] | B | WNT7B activity raises PTPRE's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.73× lower at baseline in the lines without WNT7B | 0.008 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[EVA1A]] | B | EVA1A activity raises PTPRE's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without EVA1A | 0.010 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[ITGA3]] | B | ITGA3 activity raises PTPRE's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.52× lower at baseline in the lines without ITGA3 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[LINC02725]] | B | LINC02725 activity raises PTPRE's level | lines that do not express LINC02725 (35) vs lines expressing it (15) | 2.18× lower at baseline in the lines without LINC02725 | 0.013 | ⚠ within organs, on part of the lines; also absent: DHRS9, ENSG00000203434, LINC01425 |
| [[ADAM8]] | B | ADAM8 activity raises PTPRE's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.58× lower at baseline in the lines without ADAM8 | 0.015 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[EMP1]] | B | EMP1 activity raises PTPRE's level | lines that do not express EMP1 (10) vs lines expressing it (40) | 3.03× lower at baseline in the lines without EMP1 | 0.017 | ⚠ within organs, on part of the lines |
| [[LYPD6B]] | B | LYPD6B activity raises PTPRE's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without LYPD6B | 0.019 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[EPHB6]] | B | EPHB6 activity raises PTPRE's level | lines that do not express EPHB6 (27) vs lines expressing it (23) | 2.76× lower at baseline in the lines without EPHB6 | 0.019 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000213981, ARHGEF38 |
| [[RAC2]] | B | RAC2 activity raises PTPRE's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without RAC2 | 0.020 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 33, C 1. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC2]] | B | PTPRE activity raises RAC2's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 3.37× lower at baseline in the lines without PTPRE | 0.006 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[TMCC3]] | B | PTPRE activity raises TMCC3's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.80× lower at baseline in the lines without PTPRE | 0.008 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[TINAGL1]] | B | PTPRE activity raises TINAGL1's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 4.88× lower at baseline in the lines without PTPRE | 0.008 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | B | PTPRE activity raises ARHGAP27P1-BPTFP1-KPNA2P3's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without PTPRE | 0.011 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[CARD11]] | B | PTPRE activity raises CARD11's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 3.71× lower at baseline in the lines without PTPRE | 0.017 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[EMP1]] | B | PTPRE activity raises EMP1's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without PTPRE | 0.020 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[S100A16]] | B | PTPRE activity raises S100A16's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 3.00× lower at baseline in the lines without PTPRE | 0.024 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[CD82]] | B | PTPRE activity raises CD82's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without PTPRE | 0.028 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[ADAM8]] | B | PTPRE activity raises ADAM8's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.41× lower at baseline in the lines without PTPRE | 0.034 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[RPSAP52]] | B | PTPRE activity raises RPSAP52's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.01× lower at baseline in the lines without PTPRE | 0.041 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[PRSS3]] | B | PTPRE activity raises PRSS3's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 3.61× lower at baseline in the lines without PTPRE | 0.042 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[TMEM171]] | B | PTPRE activity raises TMEM171's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without PTPRE | 0.044 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.5, 7.4); signed map (10.4, 51.9). **Vector** length 104, 28.0% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.8 | +0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | -7.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.8 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | -1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.8 | +2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.6 | +3.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.6 | -7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.7 | -6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.3 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:127,907,103-128,085,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTPE |
| Gene groups (HGNC) | Protein tyrosine phosphatases receptor type |
| Hallmark sets | INFLAMMATORY_RESPONSE, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [P23469](https://www.uniprot.org/uniprotkb/P23469) (Receptor-type tyrosine-protein phosphatase epsilon):

> Isoform 1 plays a critical role in signaling transduction pathways and phosphoprotein network topology in red blood cells. May play a role in osteoclast formation and function (By similarity).; Isoform 2 acts as a negative regulator of insulin receptor (IR) signaling in skeletal muscle. Regulates insulin-induced tyrosine phosphorylation of insulin receptor (IR) and insulin receptor substrate 1 (IRS-1), phosphorylation of protein kinase B and glycogen synthase kinase-3 and insulin induced …

**Summary**, from NCBI Gene [5791](https://www.ncbi.nlm.nih.gov/gene/5791):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. Several alternatively spliced transcript variants of this gene have been reported, at least two of which encode a receptor-type PTP that possesses a short extracellular domain, a single transmembrane region, and two tandem …

**Accessions** — [HGNC:9669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9669) · Entrez [5791](https://www.ncbi.nlm.nih.gov/gene/5791) · UniProt [P23469](https://www.uniprot.org/uniprotkb/P23469) · Ensembl [ENSG00000132334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132334)

## Data

Gene col 5302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5302); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5302]; `tensor/DDL_lfc|DDL_z.npy` [5302]; `embed/gene_vectors.npy` [5302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5302 or target_col == 5302). Every well: [[PTPRE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
