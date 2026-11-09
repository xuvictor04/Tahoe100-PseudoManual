---
symbol: "LPAR5"
type: "gene"
col: 11552
ensembl_id: "ENSG00000184574"
name: "lysophosphatidic acid receptor 5"
location: "12p13.31"
module: 55
arm: "+"
pooled_cpm: 3.34
n_lines_expressing: 30
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 58
direction_downstream: 50
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# LPAR5

*lysophosphatidic acid receptor 5* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.50× (z +15.2, q 0e+00, up in 7 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.559× (z -5.0, q 4e-04, down in 16 of 27 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.587× (z -4.3, q 0.004, down in 18 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 4 lines (LoVo 0.144×, LS 180 0.0982×, SW480 0.198×, Hs 766T 0.0305×); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (LS 180 0.0266×, LoVo 0.0990×, Panc 03.27 0.142×; ⚠ toxic); [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.0558×, SW480 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.108×, CFPAC-1 0.234×); [[Auranofin (drug)]] 5 µM in 2 lines (LS 180 0.109×, LoVo 0.196×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOGAT3]] (+0.68, fdr 8e-06), [[SULT1C2]] (+0.63, fdr 7e-06), [[CNKSR1]] (+0.63, fdr 2e-05); moves opposite to [[LRP11]] (-0.54, fdr 4e-05), [[R3HDM1]] (-0.48, fdr 1e-04), [[SUGP2]] (-0.47, fdr 8e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 58 arrows point to it, the strongest [[PCDH1]] → it (grade B ⚠); 50 go from it, the strongest it → [[ARHGAP27]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11552.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.50×** | +15.2 | 0e+00 | 7/19 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +8.8 | 3e-16 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +7.1 | 2e-10 | 5/20 (SW1417, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +7.0 | 5e-10 | 16/27 (KATO III, SW480, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.15×** | +6.6 | 6e-09 | 15/25 (SW480, SW1417, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +6.4 | 1e-08 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **2.01×** | +6.0 | 2e-07 | 16/27 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +5.7 | 1e-06 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.83×** | +5.2 | 2e-05 | 15/23 (KATO III, SW1417, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +4.9 | 5e-05 | 1/19 (SW1417) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.70×** | +4.3 | 9e-04 | 1/13 (KATO III) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.0 | 0.003 | 1/12 (LS 180) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.010 | 2/23 (HT-29, HEC-1-A) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.017 | 1/26 (HEC-1-A) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.4 | 0.026 | 1/18 (A-172) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.2 | 0.048 | 3/23 (HOP62, KATO III, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.068 | 1/18 (HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.071 | 4/24 (NCI-H1573, SW480, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 4 lines (LoVo 0.144×, LS 180 0.0982×, SW480 0.198×, Hs 766T 0.0305×); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (LS 180 0.0266×, LoVo 0.0990×, Panc 03.27 0.142×; ⚠ toxic); [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.0558×, SW480 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.108×, CFPAC-1 0.234×); [[Auranofin (drug)]] 5 µM in 2 lines (LS 180 0.109×, LoVo 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.559×** | -5.0 | 4e-04 | 16/27 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -4.3 | 0.004 | 18/25 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.643×** | -3.8 | 0.029 | 9/26 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.688× | -3.2 | 0.19 | 12/26 (SW480, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.685× | -3.1 | 0.24 | 12/21 (SW480, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.75 | 1 | 8 (7 ⚠) | [[Selinexor (drug)]] 5 µM 2.75× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.0918× (z -14.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.198× (z -9.4) |
| [[LoVo (line)]] | wt | 9.16 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0558× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.144× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 22.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0749× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -10.1) |
| [[LS 180 (line)]] | wt | 9.40 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0266× (z -15.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.109× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 7.16 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -8.8) |
| [[A-172 (line)]] | wt | 5.72 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[KATO III (line)]] | alt | 6.21 | 1 | 1 | [[Selinexor (drug)]] 5 µM 4.87× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.0652× (z -10.6) |
| [[SW1417 (line)]] | alt | 12.3 | 2 | 0 | [[Selinexor (drug)]] 5 µM 3.17× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 9.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -13.5) |
| [[Hs 766T (line)]] | wt | 3.05 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0305× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 6.19 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.123× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.994 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.878 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.913 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.835 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.641 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOGAT3]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[SULT1C2]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CNKSR1]] | +0.63 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[KCTD14]] | +0.62 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[TLDC2]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[AMN]] | +0.61 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ADCY4]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 | pathway: G alpha (i) signalling events |
| [[DEF6]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[FUT2]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[INAVA]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[IL17RE]] | +0.58 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[ZNF503-AS1]] | +0.57 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP11]] | -0.54 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[R3HDM1]] | -0.48 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[SUGP2]] | -0.47 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[NSD2]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ST3GAL3]] | -0.47 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 32, C 26. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PCDH1 activity raises LPAR5's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.40× lower at baseline in the lines without PCDH1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[SULT1C2]] | B | SULT1C2 activity raises LPAR5's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without SULT1C2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[C11orf52]] | B | C11orf52 activity raises LPAR5's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.09× lower at baseline in the lines without C11orf52 | 0.010 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[STYK1]] | B | STYK1 activity raises LPAR5's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without STYK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[IL2RG]] | B | IL2RG activity raises LPAR5's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without IL2RG | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[CEACAM1]] | B | CEACAM1 activity strengthens LPAR5's drug response | lines that do not express CEACAM1 (10) vs lines expressing it (17) | the lines without CEACAM1 respond 0.63× as strongly (z diff +0.50); strongest at Osimertinib (mesylate) 5 µM: 1.04x vs 2.84x (z diff +3.6) | 0.012 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; target measured in part of the lines; artifact flags |
| [[CRYBG2]] | B | CRYBG2 activity raises LPAR5's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without CRYBG2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[TMC4]] | B | TMC4 activity raises LPAR5's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.37× lower at baseline in the lines without TMC4 | 0.017 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[TMPRSS3]] | B | TMPRSS3 activity raises LPAR5's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without TMPRSS3 | 0.021 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[FXYD2]] | B | FXYD2 activity raises LPAR5's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 2.32× lower at baseline in the lines without FXYD2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA |
| [[MYO7B]] | B | MYO7B activity raises LPAR5's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.24× lower at baseline in the lines without MYO7B | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[UNC13D]] | B | UNC13D activity raises LPAR5's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without UNC13D | 0.025 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |

### Downstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 29, C 21. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP27]] | B | LPAR5 activity raises ARHGAP27's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without LPAR5 | 5e-04 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[UNC13D]] | B | LPAR5 activity raises UNC13D's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without LPAR5 | 0.001 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[ALS2CL]] | B | LPAR5 activity raises ALS2CL's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.84× lower at baseline in the lines without LPAR5 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[TLDC2]] | B | LPAR5 activity raises TLDC2's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without LPAR5 | 0.005 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[STYK1]] | B | LPAR5 activity raises STYK1's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.93× lower at baseline in the lines without LPAR5 | 0.009 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[NGEF]] | B | LPAR5 activity raises NGEF's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without LPAR5 | 0.009 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[TMC4]] | B | LPAR5 activity raises TMC4's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 3.08× lower at baseline in the lines without LPAR5 | 0.011 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[MYO7A]] | B | LPAR5 activity raises MYO7A's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without LPAR5 | 0.012 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[CRYBG2]] | B | LPAR5 activity raises CRYBG2's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 3.08× lower at baseline in the lines without LPAR5 | 0.014 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[RHBDL2]] | B | LPAR5 activity raises RHBDL2's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without LPAR5 | 0.014 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[FUT2]] | B | LPAR5 activity raises FUT2's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 1.87× lower at baseline in the lines without LPAR5 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[C11orf52]] | B | LPAR5 activity raises C11orf52's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.07× lower at baseline in the lines without LPAR5 | 0.018 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.4, 54.8); signed map (59.1, 12.0). **Vector** length 55.4, 11.8% of its response variance represented; |z| ≥ 3 in 636 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.4 | +7.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.0 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +6.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.1 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.6 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidic acid receptor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,618,835-6,635,960 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KPG_010, LPA5; previously GPR93, GPR92 |
| Gene groups (HGNC) | Lysophosphatidic acid receptors |
| Reactome | 7 pathways, smallest: Lysosphingolipid and LPA receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1C0](https://www.uniprot.org/uniprotkb/Q9H1C0) (Lysophosphatidic acid receptor 5):

> Receptor for lysophosphatidic acid (LPA), a mediator of diverse cellular activities.

**Summary**, from NCBI Gene [57121](https://www.ncbi.nlm.nih.gov/gene/57121):

> This gene encodes a member of the rhodopsin class of G protein-coupled transmembrane receptors. This protein transmits extracellular signals from lysophosphatidic acid to cells through heterotrimeric G proteins and mediates numerous cellular processes. Many G protein receptors serve as targets for pharmaceutical drugs. Transcript variants of this gene have been described.[provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:13307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13307) · Entrez [57121](https://www.ncbi.nlm.nih.gov/gene/57121) · UniProt [Q9H1C0](https://www.uniprot.org/uniprotkb/Q9H1C0) · Ensembl [ENSG00000184574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184574)

## Data

Gene col 11552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11552); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11552]; `tensor/DDL_lfc|DDL_z.npy` [11552]; `embed/gene_vectors.npy` [11552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11552 or target_col == 11552). Every well: [[LPAR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPAR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
