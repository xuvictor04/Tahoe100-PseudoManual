---
symbol: "PHF2P2"
type: "gene"
col: 13509
ensembl_id: "ENSG00000226057"
name: "PHD finger protein 2 pseudogene 2"
location: "13q12.11"
module: 177
arm: "+"
pooled_cpm: 13.99
n_lines_expressing: 12
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 10
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# PHF2P2

*PHD finger protein 2 pseudogene 2* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.67× (z +12.0, q 2e-30, up in 4 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (H4 0.120×, SW1417 0.158×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (AN3 CA 0.0693×, SW1417 0.162×; ⚠ toxic; cell-cycle shift, explains ~33% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.234×, SW1417 0.171×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (KATO III 0.150×).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD20A8P]] (+0.64, fdr 1e-05), [[AACSP1]] (+0.63, fdr 1e-05), [[FAM95A]] (+0.61, fdr 7e-06); moves opposite to [[AHSA2P]] (-0.50, fdr 2e-04), [[HSPE1-MOB4]] (-0.42, fdr 4e-04), [[ARHGEF25]] (-0.41, fdr 6e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[CCDC144NL-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +12.0 | 2e-30 | 4/8 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.28×** | +10.1 | 2e-21 | 6/9 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +9.4 | 1e-18 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.80×** | +8.9 | 6e-17 | 7/9 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +8.4 | 4e-15 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.9 | 4e-13 | 3/8 (H4, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.19×** | +6.5 | 6e-09 | 5/10 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +6.0 | 1e-07 | 9/10 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +5.4 | 5e-06 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +5.2 | 1e-05 | 3/8 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +4.6 | 2e-04 | 2/8 (NCI-H1573, A-172) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.5 | 4e-04 | 4/8 (H4, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.005 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.7 | 0.007 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.6 | 0.010 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.017 | 7/9 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.4 | 0.022 | 7/10 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.038 | 4/10 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.042 | 5/8 (H4, KATO III, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13509.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (H4 0.120×, SW1417 0.158×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (AN3 CA 0.0693×, SW1417 0.162×; ⚠ toxic; cell-cycle shift, explains ~33% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.234×, SW1417 0.171×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (KATO III 0.150×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.675× | -3.4 | 0.23 | 6/9 (NCI-H1573, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.666× | -3.3 | 0.23 | 0/10 | inconsistent across doses | position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.771× | -3.2 | 0.23 | 5/8 (H4, NCI-H1573, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.690× | -3.0 | 0.26 | 0/9 | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.710× | -3.0 | 0.26 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 40.3 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.21× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.0908× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.150× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 237 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.71× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.234× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 166 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0929× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.120× (z -11.5) |
| [[SW1417 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.158× (z -9.1) |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0693× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +10.1) | — |
| [[A-172 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 17 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD20A8P]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[AACSP1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FAM95A]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ANKRD20A9P]] | +0.58 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[CCDC144NL-AS1]] | +0.52 | +0.17 / +0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[TPTE]] | +0.51 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[LINC00408]] | +0.49 | +0.31 / +0.61 | both halves | 2e-04 | ⚠ same locus (11.2 kb: neighbours can correlate without regulation) |
| [[POTEF]] | +0.47 | +0.08 / +0.50 | ⚠ not reproduced | 0.003 |  |
| [[FAR2P1]] | +0.47 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[CEP63]] | +0.47 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[LINC01473]] | +0.47 | +0.29 / +0.41 | both halves | 2e-04 |  |
| [[DHRS2]] | +0.45 | +0.26 / +0.40 | both halves | 4e-04 |  |
| [[NTMT1]] | +0.45 | +0.33 / +0.33 | both halves | 1e-04 |  |
| [[LRRTM4]] | +0.44 | +0.29 / +0.50 | both halves | 2e-04 |  |
| [[EMC9]] | +0.44 | +0.33 / +0.38 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA2P]] | -0.50 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[HSPE1-MOB4]] | -0.42 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[ARHGEF25]] | -0.41 | -0.22 / -0.36 | both halves | 6e-04 |  |
| [[SRP14]] | -0.40 | -0.28 / -0.28 | both halves | 3e-04 |  |
| [[TRMT2B]] | -0.40 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[HSPH1]] | -0.40 | -0.16 / -0.24 | ⚠ not reproduced | 0.001 |  |
| [[ZNF117]] | -0.39 | -0.20 / -0.31 | both halves | 7e-04 |  |
| [[BABAM1]] | -0.38 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[DNAJA4]] | -0.38 | -0.35 / -0.20 | both halves | 7e-04 |  |
| [[GLUD1P3]] | -0.38 | -0.28 / -0.28 | both halves | 3e-04 |  |
| [[HSPE1]] | -0.38 | -0.32 / -0.23 | both halves | 5e-04 |  |
| [[HEXA]] | -0.37 | -0.18 / -0.29 | ⚠ not reproduced | 9e-04 |  |
| [[IPP]] | -0.37 | -0.26 / -0.20 | both halves | 7e-04 |  |
| [[PHTF1]] | -0.37 | -0.21 / -0.29 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PHF2P2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00408]] | C | LINC00408 activity raises PHF2P2's level | lines that do not express LINC00408 (38) vs lines expressing it (12) | 7.73× lower at baseline in the lines without LINC00408 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000287861, ANKRD20A9P, PHF2P2; co-absent with the target |
| [[CCDC144NL-AS1]] | C | CCDC144NL-AS1 activity raises PHF2P2's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 4.38× lower at baseline in the lines without CCDC144NL-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent; co-absent with the target |
| [[TPTE]] | C | TPTE activity raises PHF2P2's level | lines that do not express TPTE (35) vs lines expressing it (15) | 4.64× lower at baseline in the lines without TPTE | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[ANKRD20A8P]], [[FAM95A]] | C | ANKRD20A8P, FAM95A activity raises PHF2P2's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.50× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[ANKRD20A9P]] | C | ANKRD20A9P activity raises PHF2P2's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 5.96× lower at baseline in the lines without ANKRD20A9P | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |
| [[TRIM15]] | C | TRIM15 activity raises PHF2P2's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.89× lower at baseline in the lines without TRIM15 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises PHF2P2's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 3.82× lower at baseline in the lines without LINC01518 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises PHF2P2's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without LINC01446 | 0.037 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[AACSP1]] | C | AACSP1 activity raises PHF2P2's level | lines that do not express AACSP1 (32) vs lines expressing it (18) | 4.06× lower at baseline in the lines without AACSP1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00408, ENSG00000277757, NAA11; co-absent with the target |
| [[GABRA3]] | C | GABRA3 activity raises PHF2P2's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.03× lower at baseline in the lines without GABRA3 | 0.064 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144NL-AS1]] | C | PHF2P2 activity raises CCDC144NL-AS1's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 9.06× lower at baseline in the lines without PHF2P2 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[TPTE]] | C | PHF2P2 activity raises TPTE's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 8.81× lower at baseline in the lines without PHF2P2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[AACSP1]] | C | PHF2P2 activity raises AACSP1's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.41× lower at baseline in the lines without PHF2P2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[LINC00408]] | C | PHF2P2 activity raises LINC00408's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.50× lower at baseline in the lines without PHF2P2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[LINC01446]] | C | PHF2P2 activity raises LINC01446's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 4.93× lower at baseline in the lines without PHF2P2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[ANKRD20A9P]] | C | PHF2P2 activity raises ANKRD20A9P's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.63× lower at baseline in the lines without PHF2P2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[GABRA3]] | C | PHF2P2 activity raises GABRA3's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 2.26× lower at baseline in the lines without PHF2P2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[ANKRD20A8P]] | C | PHF2P2 activity raises ANKRD20A8P's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.78× lower at baseline in the lines without PHF2P2 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[POTEF]] | C | PHF2P2 activity raises POTEF's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.39× lower at baseline in the lines without PHF2P2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[LINC01518]] | C | PHF2P2 activity raises LINC01518's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 5.74× lower at baseline in the lines without PHF2P2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.8, 31.5); signed map (33.5, 36.3). **Vector** length 24.2, 5.67% of its response variance represented; |z| ≥ 3 in 244 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +7.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.6 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -0.7 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -3.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.6 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 2 pseudogene 2 |
| Locus type | pseudogene |
| Location | 13q12.11 — chr13:18,946,755-19,062,718 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:38808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38808) · Entrez [100873793](https://www.ncbi.nlm.nih.gov/gene/100873793) · Ensembl [ENSG00000226057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226057)

## Data

Gene col 13509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13509); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13509]; `tensor/DDL_lfc|DDL_z.npy` [13509]; `embed/gene_vectors.npy` [13509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13509 or target_col == 13509). Every well: [[PHF2P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF2P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
