---
symbol: "RAPGEF5"
type: "gene"
col: 5838
ensembl_id: "ENSG00000136237"
name: "Rap guanine nucleotide exchange factor 5"
location: "7p15.3"
module: 8
arm: "+"
pooled_cpm: 58.81
n_lines_expressing: 33
n_dd_up: 3
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 52
direction_downstream: 62
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RAPGEF5

*Rap guanine nucleotide exchange factor 5* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +10.9, q 1e-24, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.366× (z -20.1, q 0e+00, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAK1]] (+0.65, fdr 7e-06), [[PRSS12]] (+0.62, fdr 7e-06), [[PROM1]] (+0.62, fdr 7e-06); moves opposite to [[FAM228B]] (-0.60, fdr 7e-06), [[LRRC27]] (-0.56, fdr 1e-05), [[MCPH1-AS1]] (-0.52, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[LINC03040]] → it (grade B ⚠); 62 go from it, the strongest it → [[ACOT11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5838.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +10.9 | 1e-24 | 25/31 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +8.0 | 5e-13 | 23/32 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.9 | 2e-04 | 18/31 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | 1.52× | +3.1 | 0.27 | 10/32 (SW 900, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.366×** | -20.1 | 0e+00 | 29/31 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.410×** | -17.9 | 0e+00 | 25/32 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.334×** | -15.0 | 0e+00 | 26/31 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.440×** | -11.6 | 3e-29 | 28/31 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.465×** | -10.8 | 2e-25 | 26/31 (LoVo, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.516×** | -9.4 | 6e-19 | 24/31 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.574×** | -7.9 | 3e-13 | 25/31 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.562×** | -7.5 | 3e-12 | 24/29 (SW48, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -7.0 | 1e-10 | 26/32 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -6.4 | 1e-08 | 20/31 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.653×** | -5.8 | 3e-07 | 20/26 (SHP-77, HEC-1-A, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -5.6 | 1e-06 | 23/31 (HepG2/C3A, LoVo, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -5.3 | 4e-06 | 19/31 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.701×** | -5.0 | 2e-05 | 22/32 (HEC-1-A, LoVo, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -4.8 | 6e-05 | 19/31 (HepG2/C3A, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.548×** | -4.5 | 3e-04 | 17/31 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.753×** | -3.8 | 0.004 | 20/31 (HT-29, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -3.5 | 0.014 | 20/32 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.014 | 17/31 (RKO, SW48, …) | two highest doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 199 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -23.3) |
| [[SW48 (line)]] | wt | 202 | 0 | 16 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0342× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.148× (z -20.8) |
| [[SW1417 (line)]] | alt | 77.0 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -20.4) |
| [[RKO (line)]] | wt | 69.1 | 0 | 13 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0278× (z -25.9) |
| [[LoVo (line)]] | wt | 134 | 0 | 12 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.144× (z -19.6) |
| [[KATO III (line)]] | alt | 177 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -21.9) |
| [[HepG2_C3A (line)]] | wt | 217 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.9) |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -20.9) |
| [[SW480 (line)]] | alt | 35.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -14.6) |
| [[HT-29 (line)]] | alt | 191 | 0 | 7 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.107× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 55.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.3) |
| [[COLO 205 (line)]] | alt | 153 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.9) |
| [[HCT15 (line)]] | alt | 79.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.8) |
| [[SHP-77 (line)]] | alt | 211 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -16.9) |
| [[A-427 (line)]] | wt | 52.8 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 47.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -20.3) |
| [[LS 180 (line)]] | wt | 151 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 48.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 76.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -18.2) |
| [[J82 (line)]] | alt | 31.1 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.33× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -10.3) |
| [[A498 (line)]] | wt | 30.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.9) |
| [[A549 (line)]] | wt | 16.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.4) |
| [[BT-474 (line)]] | alt | 131 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 35.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.9) |
| [[A-172 (line)]] | wt | 20.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 70.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 34.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.239× (z -8.6) |
| [[AN3 CA (line)]] | alt | 9.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.09 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PRSS12]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[PROM1]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SPATA13]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ARHGAP8]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SKAP1]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SAMD12]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[C6orf132]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CARMIL1]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TC2N]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[OSBPL10]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM228B]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[LRRC27]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[MCPH1-AS1]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[FBXL9P]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[OTUD7B]] | -0.49 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[LMLN]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ARHGEF6]] | -0.48 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[GTF2IP14]] | -0.48 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[LINC02256]] | -0.48 | -0.59 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 33, C 19. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03040]] | B | LINC03040 activity raises RAPGEF5's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 4.14× lower at baseline in the lines without LINC03040 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[SYNPR-AS1]] | B | SYNPR-AS1 activity raises RAPGEF5's level | lines that do not express SYNPR-AS1 (33) vs lines expressing it (17) | 3.72× lower at baseline in the lines without SYNPR-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PPP1R1B, SLC6A20, FXYD3 |
| [[RNF128]] | B | RNF128 activity raises RAPGEF5's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 2.66× lower at baseline in the lines without RNF128 | 0.008 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[LINC01814]] | B | LINC01814 activity raises RAPGEF5's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 4.14× lower at baseline in the lines without LINC01814 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[CLIC5]] | B | CLIC5 activity raises RAPGEF5's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.63× lower at baseline in the lines without CLIC5 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[MPZL2]] | B | MPZL2 activity raises RAPGEF5's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.86× lower at baseline in the lines without MPZL2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[SERPINA5]] | B | SERPINA5 activity raises RAPGEF5's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 2.99× lower at baseline in the lines without SERPINA5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546 |
| [[ARHGEF6]] | B | ARHGEF6 activity lowers RAPGEF5's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 3.99× higher at baseline in the lines without ARHGEF6 | 0.019 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[ABO]] | B | ABO activity raises RAPGEF5's level | lines that do not express ABO (32) vs lines expressing it (18) | 3.73× lower at baseline in the lines without ABO | 0.026 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[MCF2L]] | B | MCF2L activity raises RAPGEF5's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 3.00× lower at baseline in the lines without MCF2L | 0.028 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RAPGEF5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[EPS8L3]] | B | EPS8L3 activity raises RAPGEF5's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 5.03× lower at baseline in the lines without EPS8L3 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |

### Downstream of this gene

*62 arrows, 62 of them with an alert ⚠; grade A 0, B 42, C 20. Shown: the 12 strongest; 50 more arrows (50 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACOT11]] | B | RAPGEF5 activity raises ACOT11's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.03× lower at baseline in the lines without RAPGEF5 | 0.004 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[MTUS1]] | B | RAPGEF5 activity raises MTUS1's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.81× lower at baseline in the lines without RAPGEF5 | 0.007 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[GAREM1]] | B | RAPGEF5 activity raises GAREM1's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.58× lower at baseline in the lines without RAPGEF5 | 0.010 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[PLEKHA7]] | B | RAPGEF5 activity raises PLEKHA7's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.45× lower at baseline in the lines without RAPGEF5 | 0.010 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[OSBPL3]] | B | RAPGEF5 activity strengthens OSBPL3's drug response | lines that do not express RAPGEF5 (16) vs lines expressing it (30) | the lines without RAPGEF5 respond 1.15× as strongly (z diff -0.63); strongest at Docetaxel 0.05 µM: 0.95x vs 0.67x (z diff +3.5) | 0.012 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[COBL]] | B | RAPGEF5 activity raises COBL's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.43× lower at baseline in the lines without RAPGEF5 | 0.015 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[RFLNB]] | B | RAPGEF5 activity lowers RFLNB's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.28× higher at baseline in the lines without RAPGEF5 | 0.017 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[MGAT4A]] | B | RAPGEF5 activity raises MGAT4A's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.56× lower at baseline in the lines without RAPGEF5 | 0.020 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[TTC22]] | B | RAPGEF5 activity raises TTC22's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without RAPGEF5 | 0.020 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[LRP5]] | B | RAPGEF5 activity raises LRP5's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.99× lower at baseline in the lines without RAPGEF5 | 0.022 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[MPZL2]] | B | RAPGEF5 activity raises MPZL2's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.78× lower at baseline in the lines without RAPGEF5 | 0.028 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[EPS8L3]] | B | RAPGEF5 activity raises EPS8L3's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.79× lower at baseline in the lines without RAPGEF5 | 0.030 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, 44.1); signed map (54.7, 14.2). **Vector** length 116, 36.1% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.4 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +5.6 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.0 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | -10.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -15.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Rap guanine nucleotide exchange factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:22,118,236-22,357,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0277, GFR, MR-GEF |
| Gene groups (HGNC) | DEP domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92565](https://www.uniprot.org/uniprotkb/Q92565) (Rap guanine nucleotide exchange factor 5):

> Guanine nucleotide exchange factor (GEF) for RAP1A, RAP2A and MRAS/M-Ras-GTP. Its association with MRAS inhibits Rap1 activation.

**Summary**, from NCBI Gene [9771](https://www.ncbi.nlm.nih.gov/gene/9771):

> Members of the RAS (see HRAS; MIM 190020) subfamily of GTPases function in signal transduction as GTP/GDP-regulated switches that cycle between inactive GDP- and active GTP-bound states. Guanine nucleotide exchange factors (GEFs), such as RAPGEF5, serve as RAS activators by promoting acquisition of GTP to maintain the active GTP-bound state and are the key link between cell surface receptors and RAS activation (Rebhun et al., 2000 [PubMed 10934204]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16862) · Entrez [9771](https://www.ncbi.nlm.nih.gov/gene/9771) · UniProt [Q92565](https://www.uniprot.org/uniprotkb/Q92565) · Ensembl [ENSG00000136237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136237)

## Data

Gene col 5838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5838); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5838]; `tensor/DDL_lfc|DDL_z.npy` [5838]; `embed/gene_vectors.npy` [5838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5838 or target_col == 5838). Every well: [[RAPGEF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPGEF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
