---
symbol: "STX11"
type: "gene"
col: 5728
ensembl_id: "ENSG00000135604"
name: "syntaxin 11"
location: "6q24.2"
module: 14
arm: "+"
pooled_cpm: 4.03
n_lines_expressing: 42
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# STX11

*syntaxin 11* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.99× (z +25.3, q 0e+00, up in 27 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.0502×, J82 0.174×, Hs 766T 0.0963×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0600×); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-423 0.0918×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Busulfan (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0696×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOVL7]] (+0.67, fdr 1e-05), [[SLC35F1]] (+0.66, fdr 7e-06), [[NKX3-1]] (+0.65, fdr 7e-06); moves opposite to [[TYW1]] (-0.55, fdr 1e-05), [[ANAPC10]] (-0.53, fdr 3e-05), [[IPO11]] (-0.50, fdr 8e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NKX3-1]] → it (grade B ⚠); 4 go from it, the strongest it → [[XKR4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.99×** | +25.3 | 0e+00 | 27/30 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.21×** | +15.8 | 0e+00 | 32/34 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.51×** | +13.0 | 3e-36 | 34/38 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.52×** | +12.6 | 5e-34 | 25/29 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +10.3 | 6e-23 | 23/29 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.77×** | +10.2 | 3e-22 | 28/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.54×** | +8.9 | 3e-17 | 13/20 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.51×** | +7.9 | 2e-13 | 22/33 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.03×** | +7.1 | 1e-10 | 19/38 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.92×** | +6.5 | 4e-09 | 17/37 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.6 | 1e-06 | 7/19 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.5 | 1e-06 | 14/38 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.46×** | +5.4 | 3e-06 | 9/37 (LOX-IMVI, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +5.2 | 6e-06 | 11/38 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +5.0 | 2e-05 | 8/27 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +4.9 | 3e-05 | 13/38 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +4.9 | 4e-05 | 15/39 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5728.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.0502×, J82 0.174×, Hs 766T 0.0963×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Azithromycin (hydrate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0600×); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-423 0.0918×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Busulfan (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0696×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.5 | 0.15 | 7/40 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.709× | -3.5 | 0.15 | 10/38 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.716× | -3.4 | 0.15 | 7/37 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.730× | -3.2 | 0.22 | 6/38 (COLO 205, AsPC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.560× | -3.0 | 0.27 | 3/26 (A549, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.9 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.12× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0502× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 7.27 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0963× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 11.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 4.78 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +10.0) | [[Busulfan (drug)]] 0.5 µM 0.0696× (z -8.6) |
| [[PANC-1 (line)]] | alt | 3.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +15.4) | — |
| [[SNU-423 (line)]] | alt | 7.99 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 7.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +10.8) | — |
| [[A549 (line)]] | wt | 5.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 1.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 1.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.3× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 1.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 1.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 2.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 5.37 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0600× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 3.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 3.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOVL7]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SLC35F1]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[NKX3-1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[EBI3]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CPAMD8]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[C11orf96]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RASGRP1]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[IL1A]] | +0.61 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[SH3GL2]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[XKR4]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW1]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ANAPC10]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[IPO11]] | -0.50 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[TCTN3]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[LONP2]] | -0.49 | -0.36 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NKX3-1]] | B | NKX3-1 activity raises STX11's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without NKX3-1 | 0.010 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[HLA-L-1]] | B | HLA-L-1 activity raises STX11's level | lines that do not express HLA-L-1 (10) vs lines expressing it (40) | 2.25× lower at baseline in the lines without HLA-L-1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, SETD1B; also absent: DNAAF9, NR3C1, RIMKLB; maybe low, not absent |
| [[C12orf50]] | B | C12orf50 activity raises STX11's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without C12orf50 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[ANKRD33B]] | B | ANKRD33B activity raises STX11's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 1.99× lower at baseline in the lines without ANKRD33B | 0.062 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22 |
| [[GLIPR2]] | B | GLIPR2 activity raises STX11's level | lines that do not express GLIPR2 (9) vs lines expressing it (41) | 1.72× lower at baseline in the lines without GLIPR2 | 0.066 | ⚠ within organs, on part of the lines; also absent: OSBPL6, HAPLN3, LHFPL6 |
| [[ARHGAP40]] | B | ARHGAP40 activity raises STX11's level | lines that do not express ARHGAP40 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without ARHGAP40 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000225096, ENSG00000239462; maybe low, not absent |
| [[EBI3]] | B | EBI3 activity raises STX11's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 2.20× lower at baseline in the lines without EBI3 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR4]] | B | STX11 activity lowers XKR4's level | lines that do not express STX11 (8) vs lines expressing it (42) | 1.75× higher at baseline in the lines without STX11 | 0.005 | ⚠ within organs, on part of the lines; also absent: TSPAN4 |
| [[EBI3]] | B | STX11 activity raises EBI3's level | lines that do not express STX11 (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without STX11 | 0.049 | ⚠ within organs, on part of the lines; also absent: TSPAN4 |
| [[PTPN14]] | B | STX11 activity raises PTPN14's level | lines that do not express STX11 (8) vs lines expressing it (42) | 1.46× lower at baseline in the lines without STX11 | 0.055 | ⚠ within organs, on part of the lines; also absent: TSPAN4 |
| [[NKX3-1]] | B | STX11 activity raises NKX3-1's level | lines that do not express STX11 (8) vs lines expressing it (42) | 2.84× lower at baseline in the lines without STX11 | 0.096 | ⚠ within organs, on part of the lines; also absent: TSPAN4 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, 3.1); signed map (40.6, 10.5). **Vector** length 60.2, 10.3% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +25.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +15.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +4.4 |
| fall | [[NG25 (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:144,150,487-144,191,939 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Syntaxins |
| Matched by | ensembl_id |

**Function**, from UniProt [O75558](https://www.uniprot.org/uniprotkb/O75558) (Syntaxin-11):

> SNAREs (soluble N-ethylmaleimide-sensitive factor-attachment protein receptors) are essential proteins for intracellular membrane fusion. SNAREs localized on opposing membranes assemble to form a trans-SNARE complex, an extended, parallel four-helix bundle whose assembly releases energy that drives membrane fusion. The core SNARE complex typically consists of four alpha-helical domains, three from target membrane SNAREs (t-SNAREs) and one from a vesicle SNARE (v-SNARE). Syntaxin-11/STX11 is an …

**Summary**, from NCBI Gene [8676](https://www.ncbi.nlm.nih.gov/gene/8676):

> This gene encodes a member of the syntaxin family. Syntaxins have been implicated in the targeting and fusion of intracellular transport vesicles. This family member may regulate protein transport among late endosomes and the trans-Golgi network. Mutations in this gene have been associated with familial hemophagocytic lymphohistiocytosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11429) · Entrez [8676](https://www.ncbi.nlm.nih.gov/gene/8676) · UniProt [O75558](https://www.uniprot.org/uniprotkb/O75558) · Ensembl [ENSG00000135604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135604)

## Data

Gene col 5728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5728); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5728]; `tensor/DDL_lfc|DDL_z.npy` [5728]; `embed/gene_vectors.npy` [5728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5728 or target_col == 5728). Every well: [[STX11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
