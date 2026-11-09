---
symbol: "MSX2"
type: "gene"
col: 4161
ensembl_id: "ENSG00000120149"
name: "msh homeobox 2"
location: "5q35.2"
module: 20
arm: "-"
pooled_cpm: 5.92
n_lines_expressing: 39
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MSX2

*msh homeobox 2* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.65× (z +12.9, q 5e-35, up in 22 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.201×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Oxaprozin (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0693×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX4]] (+0.68, fdr 1e-05), [[MED19]] (+0.64, fdr 1e-05), [[CDKN2B]] (+0.64, fdr 7e-06); moves opposite to [[CMPK1]] (-0.60, fdr 1e-05), [[TXNDC5]] (-0.55, fdr 4e-05), [[HNRNPA3]] (-0.55, fdr 6e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ARRDC4]] → it (grade B ⚠); 7 go from it, the strongest it → [[POLD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4161.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +12.9 | 5e-35 | 22/31 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.02×** | +10.3 | 2e-22 | 31/36 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +10.1 | 7e-22 | 22/30 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.88×** | +9.5 | 3e-19 | 27/33 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.51×** | +8.6 | 1e-15 | 24/31 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.44×** | +8.3 | 7e-15 | 28/36 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +8.2 | 1e-14 | 18/23 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.39×** | +8.1 | 4e-14 | 28/36 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +8.1 | 4e-14 | 27/36 (SW480, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.17×** | +7.2 | 3e-11 | 25/36 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +6.2 | 2e-08 | 23/35 (SW48, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +5.1 | 2e-05 | 19/36 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +5.0 | 2e-05 | 17/32 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.67×** | +4.6 | 2e-04 | 13/30 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.4 | 5e-04 | 10/36 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.3 | 7e-04 | 7/36 (CFPAC-1, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.018 | 5/36 (PANC-1, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.090 | 8/35 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.097 | 6/36 (SW48, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4161.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.201×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Oxaprozin (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0693×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.672× | -3.4 | 0.33 | 10/15 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4161. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 26.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[J82 (line)]] | alt | 2.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.80× (z +8.7) | — |
| [[KATO III (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 7.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 7.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 2.95 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0693× (z -9.5) |
| [[SW48 (line)]] | wt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 8.73 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4161), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX4]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[MED19]] | +0.64 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[CDKN2B]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ACAP1]] | +0.63 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[ARL14]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[EID2]] | +0.61 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[BTG1]] | +0.60 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[MARCKS]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[FOXA2]] | +0.58 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[SCAND1]] | +0.58 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[RPP25L]] | +0.57 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[LENG1]] | +0.56 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK1]] | -0.60 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.55 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[HNRNPA3]] | -0.55 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[RBBP4]] | -0.55 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[IPO5]] | -0.55 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[RPN1]] | -0.54 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[FKBP9]] | -0.54 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[EIF3F]] | -0.53 | -0.24 / -0.67 | both halves | 5e-04 |  |
| [[CRTAP]] | -0.53 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[MRE11]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.53 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[DHFR]] | -0.52 | -0.39 / -0.58 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARRDC4]] | B | ARRDC4 activity raises MSX2's level | lines that do not express ARRDC4 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without ARRDC4 | 0.012 | ⚠ within organs, on part of the lines; also absent: C2orf72, ADAP1, BACH2; maybe low, not absent |
| [[SOX4]] | B | SOX4 activity raises MSX2's level | lines that do not express SOX4 (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without SOX4 | 0.042 | ⚠ within organs, on part of the lines; also absent: B3GNT5, PLCXD2, PMEPA1; maybe low, not absent |
| [[H2AJ]] | B | H2AJ activity raises MSX2's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without H2AJ | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[ARL14]] | B | ARL14 activity raises MSX2's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without ARL14 | 0.085 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[MAF]] | B | MAF activity raises MSX2's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.04× lower at baseline in the lines without MAF | 0.086 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[FGF9]] | B | FGF9 activity strengthens MSX2's drug response | lines that do not express FGF9 (23) vs lines expressing it (13) | the lines without FGF9 respond 0.70× as strongly (z diff +1.13); strongest at Homoharringtonine 5 µM: 1.83x vs 2.50x (z diff +2.9) | 0.090 | ⚠ within organs, on part of the lines; also absent: VWA2, LINC02253, PRR15L; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers MSX2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLD4]] | B | MSX2 activity raises POLD4's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without MSX2 | 0.007 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[ARRDC4]] | B | MSX2 activity raises ARRDC4's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without MSX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[TUBA1A]] | B | MSX2 activity lowers TUBA1A's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 2.48× higher at baseline in the lines without MSX2 | 0.029 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[IPO5]] | B | MSX2 activity lowers IPO5's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 1.27× higher at baseline in the lines without MSX2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[IER3]] | B | MSX2 activity raises IER3's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without MSX2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[ID3]] | B | MSX2 activity lowers ID3's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 2.92× higher at baseline in the lines without MSX2 | 0.078 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[ARMCX2]] | B | MSX2 activity lowers ARMCX2's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 2.69× higher at baseline in the lines without MSX2 | 0.083 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (27.2, -34.8); signed map (-5.0, 10.6). **Vector** length 66.2, 13.4% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +12.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +9.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | msh homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:174,724,582-174,730,896 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRS2, FPP, HOX8, MSH, PFM; previously PFM1 |
| Gene groups (HGNC) | NKL subclass homeoboxes and pseudogenes |
| Reactome | 2 pathways, smallest: Regulation of RUNX2 expression and activity; Transcriptional regulation by RUNX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P35548](https://www.uniprot.org/uniprotkb/P35548) (Homeobox protein MSX-2):

> Acts as a transcriptional regulator in bone development. Represses the ALPL promoter activity and antagonizes the stimulatory effect of DLX5 on ALPL expression during osteoblast differentiation. Probable morphogenetic role. May play a role in limb-pattern formation. In osteoblasts, suppresses transcription driven by the osteocalcin FGF response element (OCFRE). Binds to the homeodomain-response element of the ALPL promoter.

**Summary**, from NCBI Gene [4488](https://www.ncbi.nlm.nih.gov/gene/4488):

> This gene encodes a member of the muscle segment homeobox gene family. The encoded protein is a transcriptional repressor whose normal activity may establish a balance between survival and apoptosis of neural crest-derived cells required for proper craniofacial morphogenesis. The encoded protein may also have a role in promoting cell growth under certain conditions and may be an important target for the RAS signaling pathways. Mutations in this gene are associated with parietal foramina 1 and …

**Accessions** — [HGNC:7392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7392) · Entrez [4488](https://www.ncbi.nlm.nih.gov/gene/4488) · UniProt [P35548](https://www.uniprot.org/uniprotkb/P35548) · Ensembl [ENSG00000120149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120149)

## Data

Gene col 4161: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4161); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4161, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4161]; `tensor/DDL_lfc|DDL_z.npy` [4161]; `embed/gene_vectors.npy` [4161]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4161 or target_col == 4161). Every well: [[MSX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
