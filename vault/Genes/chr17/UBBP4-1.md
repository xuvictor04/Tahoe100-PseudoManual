---
symbol: "UBBP4-1"
type: "gene"
col: 16527
ensembl_id: "ENSG00000290919"
name: ""
location: ""
module: 9
arm: "+"
pooled_cpm: 16.61
n_lines_expressing: 16
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 16
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# UBBP4-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.62× (z +22.0, q 0e+00, up in 11 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Diphenhydramine (drug)]] 0.05 µM: 0.671× (z -3.8, q 0.090, down in 0 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LOX-IMVI 0.0833×, H4 0.108×, SNU-423 0.259×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.0929×, H4 0.179×, SNU-423 0.197×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (H4 0.149×, LOX-IMVI 0.157×, SNU-423 0.245×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.425×).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02506]] (+0.71, fdr 7e-06), [[CCDC144NL-AS1]] (+0.70, fdr 7e-06), [[ANKRD20A8P]] (+0.65, fdr 3e-05); moves opposite to [[TXNDC15]] (-0.50, fdr 3e-04), [[CLCC1]] (-0.49, fdr 4e-04), [[TMPRSS5]] (-0.48, fdr 4e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC01518]] → it (grade C ⚠); 16 go from it, the strongest it → [[CCDC144NL-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.62×** | +22.0 | 0e+00 | 11/12 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.43×** | +12.0 | 7e-31 | 12/12 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.23×** | +11.9 | 2e-30 | 10/12 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +9.9 | 7e-21 | 1/10 (KATO III) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +9.3 | 2e-18 | 3/14 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +8.9 | 6e-17 | 12/13 (SNU-423, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.7 | 3e-16 | 0/8 | two highest doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +8.2 | 1e-14 | 12/13 (SNU-423, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +8.1 | 4e-14 | 9/13 (SNU-423, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +6.6 | 3e-09 | 8/12 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +6.0 | 9e-08 | 10/13 (SNU-423, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +5.4 | 4e-06 | 4/13 (HS-578T, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.64×** | +5.0 | 3e-05 | 5/13 (H4, KATO III, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.8 | 7e-05 | 8/13 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.51×** | +4.2 | 0.001 | 0/13 | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 2/13 (KATO III, HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +4.0 | 0.002 | 13/13 (SNU-423, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.004 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.029 | 0/12 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16527.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LOX-IMVI 0.0833×, H4 0.108×, SNU-423 0.259×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.0929×, H4 0.179×, SNU-423 0.197×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (H4 0.149×, LOX-IMVI 0.157×, SNU-423 0.245×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.425×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.671×** | -3.8 | 0.090 | 0/13 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.712× | -3.5 | 0.11 | 8/13 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.714× | -3.4 | 0.11 | 2/13 (SNU-423, NCI-H1573) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.737× | -3.0 | 0.38 | 4/13 (KATO III, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 424 | 10 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -16.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 104 | 5 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 7.07× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 291 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.0833× (z -18.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.70× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +10.0) | — |
| [[KATO III (line)]] | alt | 9.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +14.9) | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.2× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +12.5) | — |
| [[A-427 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 16 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02506]] | +0.71 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CCDC144NL-AS1]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ANKRD20A8P]] | +0.65 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[DHRS2]] | +0.64 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LINC02484]] | +0.59 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[ANKRD12]] | +0.58 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[MARCHF1]] | +0.54 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[TXNIP]] | +0.53 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[MSR1]] | +0.53 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[COX7B2]] | +0.53 | +0.24 / +0.56 | both halves | 5e-04 |  |
| [[BTG1]] | +0.53 | +0.25 / +0.48 | both halves | 4e-04 |  |
| [[GAS2L3]] | +0.52 | +0.33 / +0.45 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC15]] | -0.50 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[CLCC1]] | -0.49 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[TMPRSS5]] | -0.48 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[RPN1]] | -0.48 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[ZW10]] | -0.48 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[STT3A]] | -0.47 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[SELENOF]] | -0.47 | -0.30 / -0.30 | both halves | 2e-04 |  |
| [[NAXD]] | -0.47 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[LIG3]] | -0.47 | -0.18 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[MCM9]] | -0.47 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[TMEM248]] | -0.47 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[THOC5]] | -0.47 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[GDAP2]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ADPGK]] | -0.46 | -0.30 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01518]] | C | LINC01518 activity raises UBBP4-1's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 3.92× lower at baseline in the lines without LINC01518 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises UBBP4-1's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 4.26× lower at baseline in the lines without CCDC144NL-AS1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises UBBP4-1's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 5.23× lower at baseline in the lines without LINC01885 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[DDX43]] | C | DDX43 activity raises UBBP4-1's level | lines that do not express DDX43 (34) vs lines expressing it (16) | 2.88× lower at baseline in the lines without DDX43 | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC34A2, LINC02377, RNF17; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises UBBP4-1's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.53× lower at baseline in the lines without LINC02506 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises UBBP4-1's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 4.33× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[LINC02484]] | C | LINC02484 activity raises UBBP4-1's level | lines that do not express LINC02484 (40) vs lines expressing it (10) | 3.51× lower at baseline in the lines without LINC02484 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000260126, LINC02566, ENSG00000289605; co-absent with the target |
| [[CCNYL2]] | C | CCNYL2 activity raises UBBP4-1's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 3.13× lower at baseline in the lines without CCNYL2 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[NCAM2]] | C | NCAM2 activity raises UBBP4-1's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 2.79× lower at baseline in the lines without NCAM2 | 0.094 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144NL-1]] | B | UBBP4-1 activity raises CCDC144NL-1's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without UBBP4-1 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025 |
| [[LINC02506]] | C | UBBP4-1 activity raises LINC02506's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 4.85× lower at baseline in the lines without UBBP4-1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[CCDC144NL-AS1]] | C | UBBP4-1 activity raises CCDC144NL-AS1's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 4.43× lower at baseline in the lines without UBBP4-1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[LINC01885]] | C | UBBP4-1 activity raises LINC01885's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 4.99× lower at baseline in the lines without UBBP4-1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[SCG3]] | C | UBBP4-1 activity raises SCG3's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without UBBP4-1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[TENM1]] | C | UBBP4-1 activity raises TENM1's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 3.75× lower at baseline in the lines without UBBP4-1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[LINC02484]] | C | UBBP4-1 activity raises LINC02484's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without UBBP4-1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[LINC01518]] | C | UBBP4-1 activity raises LINC01518's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 4.04× lower at baseline in the lines without UBBP4-1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[DDX43]] | C | UBBP4-1 activity raises DDX43's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 2.65× lower at baseline in the lines without UBBP4-1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[LINC02575]] | C | UBBP4-1 activity raises LINC02575's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without UBBP4-1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[LINC01320]] | C | UBBP4-1 activity raises LINC01320's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 3.16× lower at baseline in the lines without UBBP4-1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[ANKRD20A8P]] | C | UBBP4-1 activity raises ANKRD20A8P's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 3.75× lower at baseline in the lines without UBBP4-1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.416). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.8, 28.5); signed map (34.4, 36.7). **Vector** length 33.5, 7.20% of its response variance represented; |z| ≥ 3 in 369 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +1.6 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.5 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.5 | +22.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.5 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +5.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.7 | +0.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.8 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.1 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.0 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.9 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -0.7 | -1.5 |

## What is on record

> [!warning] No registry record
> UBBP4-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16527); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16527]; `tensor/DDL_lfc|DDL_z.npy` [16527]; `embed/gene_vectors.npy` [16527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16527 or target_col == 16527). Every well: [[UBBP4-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBBP4-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
