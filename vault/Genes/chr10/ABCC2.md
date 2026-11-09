---
symbol: "ABCC2"
type: "gene"
col: 351
ensembl_id: "ENSG00000023839"
name: "ATP binding cassette subfamily C member 2"
location: "10q24.2"
module: 117
arm: "+"
pooled_cpm: 35.09
n_lines_expressing: 28
n_dd_up: 44
n_dd_down: 1
n_dd_up_clean: 36
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 7
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# ABCC2

*ATP binding cassette subfamily C member 2* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.71× (z +15.9, q 0e+00, up in 22 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.702× (z -4.3, q 0.009, down in 12 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (COLO 205 0.121×, NCI-H460 0.160×, HepG2/C3A 0.254×, NCI-H1573 0.182×, …); [[Belinostat (drug)]] 5 µM in 4 lines (COLO 205 0.225×, SW480 0.308×, HepG2/C3A 0.303×, NCI-H460 0.293×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.197×, HepG2/C3A 0.234×; ⚠ cell-cycle shift, explains ~5% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 2 lines (NCI-H23 0.0739×, SW 900 0.0865×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM16L]] (+0.74, fdr 7e-06), [[ALOX12P2-1]] (+0.68, fdr 1e-05), [[NMRAL2P-1]] (+0.67, fdr 7e-06); moves opposite to [[MTMR14]] (-0.60, fdr 3e-05), [[TRPT1]] (-0.57, fdr 5e-05), [[UHRF2]] (-0.55, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[AKR1C3]] → it (grade B ⚠); 7 go from it, the strongest it → [[JAKMIP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.71×** | +15.9 | 0e+00 | 22/25 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +13.9 | 1e-41 | 19/22 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +12.8 | 6e-35 | 17/20 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +11.9 | 1e-30 | 13/25 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.54×** | +11.3 | 2e-27 | 22/26 (SW480, COLO 205, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +9.9 | 5e-21 | 18/25 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.21×** | +9.6 | 5e-20 | 21/25 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +9.3 | 1e-18 | 12/25 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +9.1 | 8e-18 | 14/20 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.05×** | +8.2 | 1e-14 | 19/26 (SW480, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +6.9 | 3e-10 | 9/23 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +5.7 | 5e-07 | 12/26 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.7 | 7e-07 | 14/24 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +5.6 | 1e-06 | 16/25 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.2 | 6e-06 | 13/26 (A549, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +5.2 | 6e-06 | 13/25 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.9 | 3e-05 | 9/26 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +4.4 | 3e-04 | 12/25 (A549, NCI-H1573, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +4.3 | 5e-04 | 14/26 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 351.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (COLO 205 0.121×, NCI-H460 0.160×, HepG2/C3A 0.254×, NCI-H1573 0.182×, …); [[Belinostat (drug)]] 5 µM in 4 lines (COLO 205 0.225×, SW480 0.308×, HepG2/C3A 0.303×, NCI-H460 0.293×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (COLO 205 0.197×, HepG2/C3A 0.234×; ⚠ cell-cycle shift, explains ~5% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 2 lines (NCI-H23 0.0739×, SW 900 0.0865×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.702×** | -4.3 | 0.009 | 12/25 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.773× | -3.1 | 0.48 | 15/25 (SNU-423, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 116 | 4 | 6 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 12.6× (z +19.3) | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -18.0) |
| [[HepG2_C3A (line)]] | wt | 205 | 2 | 6 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.00× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -12.1) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -11.5) |
| [[SW480 (line)]] | alt | 33.7 | 3 | 5 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 10.5× (z +20.0) | [[Digitoxin (drug)]] 5 µM 0.223× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.295× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 4 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.75× (z +16.3) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 8.65× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 158 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.09× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.182× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 183 | 1 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.54× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.160× (z -13.4) |
| [[C32 (line)]] | wt | 48.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.76× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 9.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +13.6) | — |
| [[LoVo (line)]] | wt | 22.9 | 2 | 0 | [[Auranofin (drug)]] 0.5 µM 3.95× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 11.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +12.9) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.112× (z -10.2) |
| [[A549 (line)]] | wt | 117 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 9.83 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.5× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.16× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 8.78 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0739× (z -11.4) |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0865× (z -9.2) |
| [[A-172 (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.07 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.48 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.60 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.62 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.70 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.65 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.09 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.66 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM16L]] | +0.74 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.68 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[NMRAL2P-1]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CAPS2]] | +0.67 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[AKR1C1]] | +0.64 | +0.64 / +0.70 | both halves | 7e-06 | pathway: Drug ADME |
| [[NMRAL2P]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[JAKMIP3]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CYP4F3]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[AKR1C3]] | +0.63 | +0.69 / +0.57 | both halves | 8e-06 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[HTATIP2]] | +0.63 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[MGST1]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ME1]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR14]] | -0.60 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[TRPT1]] | -0.57 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[UHRF2]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[RASA2]] | -0.55 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SPATA33]] | -0.54 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[CDKN2D]] | -0.53 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[INPP5F]] | -0.52 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[TXNDC17]] | -0.52 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[STC1]] | -0.52 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[B3GAT3]] | -0.52 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[MAD2L2]] | -0.51 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[TMEM158]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C3]] | B | AKR1C3 activity raises ABCC2's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.52× lower at baseline in the lines without AKR1C3 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[NMRAL2P]] | B | NMRAL2P activity raises ABCC2's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without NMRAL2P | 0.046 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[TOP2A]] | B | TOP2A activity lowers ABCC2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00278]] | B | LINC00278 activity raises ABCC2's level | lines that do not express LINC00278 (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without LINC00278 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, PRKY, RPS4Y1 |
| [[CYP4F11]] | B | CYP4F11 activity raises ABCC2's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.33× lower at baseline in the lines without CYP4F11 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[CYP4F3]] | B | CYP4F3 activity raises ABCC2's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 1.87× lower at baseline in the lines without CYP4F3 | 0.086 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[AKR1C2]] | C | AKR1C2 activity raises ABCC2's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 3.97× lower at baseline in the lines without AKR1C2 | 0.001 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[AKR1C1]] | C | AKR1C1 activity raises ABCC2's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 2.61× lower at baseline in the lines without AKR1C1 | 0.055 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAKMIP3]] | B | ABCC2 activity raises JAKMIP3's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without ABCC2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |
| [[CDKN2D]] | B | ABCC2 activity lowers CDKN2D's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 1.29× higher at baseline in the lines without ABCC2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |
| [[INPP5F]] | B | ABCC2 activity lowers INPP5F's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 1.33× higher at baseline in the lines without ABCC2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |
| [[HSPB1]] | B | ABCC2 activity weakens HSPB1's drug response | lines that do not express ABCC2 (22) vs lines expressing it (25) | the lines without ABCC2 respond 1.06× as strongly (z diff -0.19); strongest at Bortezomib 0.05 µM: 6.10x vs 4.63x (z diff -1.4) | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[B3GAT3]] | B | ABCC2 activity lowers B3GAT3's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 1.23× higher at baseline in the lines without ABCC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |
| [[MGST1]] | B | ABCC2 activity raises MGST1's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without ABCC2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |
| cells under [[Ipatasertib (drug)]] 5 µM | B | ABCC2 activity raises the cells' numbers under Ipatasertib 5 µM (protects the cells) | lines that do not express ABCC2 (22) vs lines expressing it (26) | the lines without ABCC2: 0.89× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.5, 48.1); signed map (51.0, -9.3). **Vector** length 86.7, 23.0% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.55 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.55 to 7); *NFE2L2 regulating anti-oxidant/detoxification enzymes* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.4 | +8.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +15.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -5.0 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Pemetrexed (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:99,782,640-99,852,594 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DJS, MRP2, cMRP; previously CMOAT |
| Gene groups (HGNC) | ATP binding cassette subfamily C |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 10 pathways, smallest: Atorvastatin ADME; Heme degradation; Aspirin ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92887](https://www.uniprot.org/uniprotkb/Q92887) (ATP-binding cassette sub-family C member 2):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family that hydrolyzes ATP to enable active transport of substrates conjugated with glucuronate, glutathione or sulfate. Operates at apical membranes of polarized cells such as hepatocytes, renal and intestinal epithelial cells where it mediates hepatobiliary and renal excretion of conjugated substrates. Involved in canalicular bile production. Mediates hepatobiliary excretion of mono- and bis-glucuronidated bilirubin, enabling …

**Summary**, from NCBI Gene [1244](https://www.ncbi.nlm.nih.gov/gene/1244):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MRP subfamily which is involved in multi-drug resistance. This protein is expressed in the canalicular (apical) part of the hepatocyte and functions in biliary transport. …

**Accessions** — [HGNC:53](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53) · Entrez [1244](https://www.ncbi.nlm.nih.gov/gene/1244) · UniProt [Q92887](https://www.uniprot.org/uniprotkb/Q92887) · Ensembl [ENSG00000023839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023839)

## Data

Gene col 351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 351); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 351]; `tensor/DDL_lfc|DDL_z.npy` [351]; `embed/gene_vectors.npy` [351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 351 or target_col == 351). Every well: [[ABCC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
