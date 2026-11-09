---
symbol: "PLCD3"
type: "gene"
col: 8451
ensembl_id: "ENSG00000161714"
name: "phospholipase C delta 3"
location: "17q21.31"
module: 31
arm: "+"
pooled_cpm: 20.74
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PLCD3

*phospholipase C delta 3* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +18.5, q 0e+00, up in 31 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +14.8, q 0e+00, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Acetohexamide (drug)]] 5 µM: 0.870× (z -3.6, q 0.097, down in 8 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.384×); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (SNU-1 0.0690×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0976×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MISP]] (+0.65, fdr 7e-06), [[JUP]] (+0.64, fdr 1e-05), [[AFAP1L2]] (+0.58, fdr 1e-05); moves opposite to [[COA6]] (-0.50, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[MISP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +18.5 | 0e+00 | 31/34 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +14.8 | 0e+00 | 28/45 (A498, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +14.4 | 6e-45 | 22/28 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.86×** | +11.4 | 8e-28 | 35/47 (LOX-IMVI, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +11.4 | 8e-28 | 32/47 (HOP62, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +11.2 | 6e-27 | 30/43 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +11.0 | 4e-26 | 35/47 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +10.7 | 9e-25 | 34/46 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +10.0 | 1e-21 | 20/28 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.8 | 1e-16 | 27/43 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +7.8 | 2e-13 | 25/47 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +7.2 | 2e-11 | 27/46 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +7.0 | 8e-11 | 21/43 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +6.8 | 4e-10 | 20/45 (HepG2/C3A, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +5.0 | 2e-05 | 11/47 (HOP62, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.002 | 11/41 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.010 | 1/42 (HEC-1-A) | rises with dose | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.010 | 6/47 (LoVo, Panc 03.27, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8451.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 0.384×); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (SNU-1 0.0690×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.0976×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Acetohexamide (drug)]] 5 µM |  | 0.870× | -3.6 | 0.097 | 8/47 (HOP62, SNU-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.823×** | -3.6 | 0.097 | 11/46 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.828×** | -3.5 | 0.097 | 13/45 (H4, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.2 | 0.17 | 14/46 (LoVo, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 41.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.9) | — |
| [[A498 (line)]] | wt | 20.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.9) | — |
| [[A549 (line)]] | wt | 26.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.4) | — |
| [[KATO III (line)]] | alt | 46.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.38× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 9.40 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.74× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 8.16 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0976× (z -9.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 38.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.6) |
| [[HT-29 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.442× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 9.19 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0690× (z -9.5) |
| [[SW480 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MISP]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[JUP]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ZMIZ2]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SEMA3B]] | +0.58 | +0.43 / +0.53 | both halves | 3e-05 | same gene group |
| [[MYO1C]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[DDR1]] | +0.57 | +0.60 / +0.50 | both halves | 1e-05 | same gene group |
| [[LMNA]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[KLF3]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[ADAP1]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.55 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[INPP1]] | +0.55 | +0.61 / +0.47 | both halves | 2e-05 | pathway: Inositol phosphate metabolism; STRING 901 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA6]] | -0.50 | -0.40 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MISP]] | B | MISP activity raises PLCD3's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without MISP | 0.003 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[IL2RG]] | B | IL2RG activity raises PLCD3's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without IL2RG | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[ITGB4]] | B | ITGB4 activity raises PLCD3's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.03× lower at baseline in the lines without ITGB4 | 0.016 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[SULF2]] | B | SULF2 activity raises PLCD3's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without SULF2 | 0.018 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[DENND2C]] | B | DENND2C activity raises PLCD3's level | lines that do not express DENND2C (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without DENND2C | 0.019 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| [[HR]] | B | HR activity raises PLCD3's level | lines that do not express HR (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without HR | 0.021 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |
| [[A4GALT]] | B | A4GALT activity raises PLCD3's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.22× lower at baseline in the lines without A4GALT | 0.022 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[PCDH1]] | B | PCDH1 activity raises PLCD3's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.80× lower at baseline in the lines without PCDH1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[SH2D3A]] | B | SH2D3A activity raises PLCD3's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.81× lower at baseline in the lines without SH2D3A | 0.025 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[COL16A1]] | B | COL16A1 activity raises PLCD3's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without COL16A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |
| [[TINAGL1]] | B | TINAGL1 activity raises PLCD3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without TINAGL1 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[CYP3A5]] | B | CYP3A5 activity raises PLCD3's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.06× lower at baseline in the lines without CYP3A5 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.8, 56.9); signed map (-1.6, 36.5). **Vector** length 86.6, 17.1% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +14.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C delta 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,108,959-45,133,354 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3E9](https://www.uniprot.org/uniprotkb/Q8N3E9) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase delta-3):

> Hydrolyzes the phosphatidylinositol 4,5-bisphosphate (PIP2) to generate 2 second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3). DAG mediates the activation of protein kinase C (PKC), while IP3 releases Ca(2+) from intracellular stores. Essential for trophoblast and placental development. May participate in cytokinesis by hydrolyzing PIP2 at the cleavage furrow. Regulates neurite outgrowth through the inhibition of RhoA/Rho kinase signaling (By similarity).

**Summary**, from NCBI Gene [113026](https://www.ncbi.nlm.nih.gov/gene/113026):

> This gene encodes a member of the phospholipase C family, which catalyze the hydrolysis of phosphatidylinositol 4,5-bisphosphate to generate the second messengers diacylglycerol and inositol 1,4,5-trisphosphate (IP3). Diacylglycerol and IP3 mediate a variety of cellular responses to extracellular stimuli by inducing protein kinase C and increasing cytosolic Ca(2+) concentrations. This enzyme localizes to the plasma membrane and requires calcium for activation. Its activity is inhibited by …

**Accessions** — [HGNC:9061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9061) · Entrez [113026](https://www.ncbi.nlm.nih.gov/gene/113026) · UniProt [Q8N3E9](https://www.uniprot.org/uniprotkb/Q8N3E9) · Ensembl [ENSG00000161714](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161714)

## Data

Gene col 8451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8451); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8451]; `tensor/DDL_lfc|DDL_z.npy` [8451]; `embed/gene_vectors.npy` [8451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8451 or target_col == 8451). Every well: [[PLCD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
