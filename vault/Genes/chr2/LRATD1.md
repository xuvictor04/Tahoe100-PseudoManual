---
symbol: "LRATD1"
type: "gene"
col: 8611
ensembl_id: "ENSG00000162981"
name: "LRAT domain containing 1"
location: "2p24.3"
module: 62
arm: "+"
pooled_cpm: 6.08
n_lines_expressing: 20
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# LRATD1

*LRAT domain containing 1* — 2p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.65× (z +21.6, q 0e+00, up in 12 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.655× (z -4.2, q 0.015, down in 10 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 3 lines (LoVo 0.186×, NCI-H1573 0.190×, LOX-IMVI 0.184×); [[Digitoxin (drug)]] 5 µM in 2 lines (LOX-IMVI 0.106×, SHP-77 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.362×, CHP-212 0.0784×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.305×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTCHD4]] (+0.66, fdr 1e-05), [[BTG2]] (+0.63, fdr 1e-05), [[SPATA18]] (+0.60, fdr 1e-05); moves opposite to [[ORC3]] (-0.44, fdr 9e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[RELN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.65×** | +21.6 | 0e+00 | 12/13 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +10.8 | 1e-24 | 1/12 (KATO III) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +10.0 | 4e-21 | 8/14 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +9.9 | 5e-21 | 7/16 (HOP62, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +9.8 | 1e-20 | 9/13 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +9.3 | 2e-18 | 7/14 (A498, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +9.2 | 4e-18 | 4/11 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.3 | 2e-11 | 9/17 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +7.1 | 6e-11 | 0/9 | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +7.1 | 7e-11 | 5/12 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +5.2 | 1e-05 | 9/15 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +4.7 | 1e-04 | 3/17 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 1e-04 | 3/14 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.2 | 0.001 | 1/10 (A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.007 | 2/16 (LS 180, LoVo) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.056 | 5/13 (A-427, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.070 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8611.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 3 lines (LoVo 0.186×, NCI-H1573 0.190×, LOX-IMVI 0.184×); [[Digitoxin (drug)]] 5 µM in 2 lines (LOX-IMVI 0.106×, SHP-77 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.362×, CHP-212 0.0784×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LS 180 0.305×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -4.2 | 0.015 | 10/17 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Monocrotaline (drug)]] 0.5 µM |  | **0.672×** | -3.9 | 0.023 | 1/16 (NCI-H1573) | inconsistent across doses |  |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | 0.708× | -3.4 | 0.12 | 0/16 | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.722× | -3.2 | 0.18 | 5/15 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.721× | -3.1 | 0.20 | 0/16 | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.69 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 79.7 | 1 | 3 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.175× (z -12.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -8.5) |
| [[SHP-77 (line)]] | alt | 55.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.362× (z -8.8) |
| [[LoVo (line)]] | wt | 16.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +9.1) | [[Ixazomib citrate (drug)]] 5 µM 0.186× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.184× (z -8.8) |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0784× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.51× (z +10.0) | — |
| [[KATO III (line)]] | alt | 8.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.190× (z -8.9) |
| [[A-172 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCHD4]] | +0.66 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[BTG2]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SPATA18]] | +0.60 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[PTPRO]] | +0.58 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[PINCR]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[CACNB2]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[DOCK8]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[KCND2]] | +0.55 | +0.60 / +0.31 | both halves | 2e-04 |  |
| [[GAS6-AS1]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[DIP2C-AS1]] | +0.53 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[FAS]] | +0.53 | +0.31 / +0.51 | both halves | 2e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC3]] | -0.44 | -0.37 / -0.38 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LRATD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RIT2]] | C | RIT2 activity raises LRATD1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.04× lower at baseline in the lines without RIT2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[C2CD4A]] | C | C2CD4A activity raises LRATD1's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 4.04× lower at baseline in the lines without C2CD4A | 0.013 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[GRIK1]] | C | GRIK1 activity raises LRATD1's level | lines that do not express GRIK1 (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without GRIK1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, PDE3A, ENSG00000224865; maybe low, not absent; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises LRATD1's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.09× lower at baseline in the lines without LINC01456 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises LRATD1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 3.48× lower at baseline in the lines without CALCA | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises LRATD1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.70× lower at baseline in the lines without SYT4 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[KCTD8]] | C | KCTD8 activity raises LRATD1's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without KCTD8 | 0.076 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |
| [[ASCL1]] | C | ASCL1 activity raises LRATD1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.57× lower at baseline in the lines without ASCL1 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RELN]] | B | LRATD1 activity raises RELN's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 1.44× lower at baseline in the lines without LRATD1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495 |
| [[KITLG]] | B | LRATD1 activity raises KITLG's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 1.94× lower at baseline in the lines without LRATD1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495 |
| [[LINC02268]] | B | LRATD1 activity raises LINC02268's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 1.86× lower at baseline in the lines without LRATD1 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495 |
| [[KCTD8]] | C | LRATD1 activity raises KCTD8's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without LRATD1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495; co-absent with the target |
| [[C2CD4A]] | C | LRATD1 activity raises C2CD4A's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without LRATD1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495; co-absent with the target |
| [[KCND2]] | C | LRATD1 activity raises KCND2's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without LRATD1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495; co-absent with the target |
| [[PTCHD4]] | C | LRATD1 activity raises PTCHD4's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 3.09× lower at baseline in the lines without LRATD1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.2, 37.6); signed map (43.0, -22.0). **Vector** length 46.5, 11.4% of its response variance represented; |z| ≥ 3 in 488 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +21.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.9 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.1 | +2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | LRAT domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.3 — chr2:14,632,700-14,650,814 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NSE1, FLJ35392; previously FAM84A |
| Gene groups (HGNC) | LRAT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KN4](https://www.uniprot.org/uniprotkb/Q96KN4) (Protein LRATD1):

> May play a role in cell morphology and motility.

**Summary**, from NCBI Gene [151354](https://www.ncbi.nlm.nih.gov/gene/151354):

> Involved in cell morphogenesis and cell motility. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20743) · Entrez [151354](https://www.ncbi.nlm.nih.gov/gene/151354) · UniProt [Q96KN4](https://www.uniprot.org/uniprotkb/Q96KN4) · Ensembl [ENSG00000162981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162981)

## Data

Gene col 8611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8611); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8611]; `tensor/DDL_lfc|DDL_z.npy` [8611]; `embed/gene_vectors.npy` [8611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8611 or target_col == 8611). Every well: [[LRATD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRATD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
