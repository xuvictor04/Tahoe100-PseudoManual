---
symbol: "ANKRD20A8P"
type: "gene"
col: 13690
ensembl_id: "ENSG00000229089"
name: "ankyrin repeat domain 20 family member A8, pseudogene"
location: "2q11.1"
module: 177
arm: "+"
pooled_cpm: 8.69
n_lines_expressing: 12
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 15
direction_downstream: 27
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# ANKRD20A8P

*ankyrin repeat domain 20 family member A8, pseudogene* — 2q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.73× (z +14.4, q 2e-44, up in 7 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.848× (z -4.5, q 0.004, down in 6 of 10 measured lines) ⚠ position not correctable. The strongest without an alert is [[Diphenhydramine (drug)]] 0.05 µM: 0.597× (z -3.7, q 0.055, down in 1 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.156×, KATO III 0.188×, H4 0.299×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.214×, H4 0.290×, A-172 0.123×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.118×, H4 0.298×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0497×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM95A]] (+0.81, fdr 7e-06, ⚠ same locus), [[UBBP4-1]] (+0.65, fdr 3e-05), [[PHF2P2]] (+0.64, fdr 1e-05), [[LINC02506]] (+0.59, fdr 1e-04); moves opposite to [[NAXD]] (-0.49, fdr 1e-04), [[C1orf216]] (-0.48, fdr 1e-04), [[POMGNT1]] (-0.45, fdr 7e-05).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LINC01205]] → it (grade C ⚠); 27 go from it, the strongest it → [[CEP63]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.73×** | +14.4 | 2e-44 | 7/8 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +11.3 | 4e-27 | 1/8 (KATO III) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.44×** | +11.2 | 5e-27 | 1/4 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.62×** | +10.1 | 1e-21 | 1/6 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +7.2 | 9e-11 | 6/8 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.41×** | +6.9 | 5e-10 | 9/10 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +6.4 | 2e-08 | 7/9 (KATO III, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +5.6 | 1e-06 | 7/10 (KATO III, H4, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +5.4 | 3e-06 | 8/9 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +4.9 | 5e-05 | 4/9 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +4.5 | 3e-04 | 0/9 | top dose only | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +3.9 | 0.004 | 1/5 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.99×** | +3.8 | 0.005 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +3.8 | 0.006 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +3.7 | 0.009 | 0/9 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +3.6 | 0.010 | 7/9 (KATO III, H4, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.4 | 0.021 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.1 | 0.051 | 3/9 (NCI-H1573, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.48×** | +3.1 | 0.054 | 3/9 (A-427, NCI-H1573, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.058 | 3/9 (HS-578T, SW1417, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.156×, KATO III 0.188×, H4 0.299×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.214×, H4 0.290×, A-172 0.123×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.118×, H4 0.298×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H23 0.0497×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.848× | -4.5 | 0.004 | 6/10 (KATO III, H4, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.597×** | -3.7 | 0.055 | 1/10 (NCI-H661) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.631×** | -3.6 | 0.062 | 1/9 (H4) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.659× | -3.0 | 0.27 | 1/10 (HS-578T) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.681× | -3.0 | 0.27 | 2/10 (SW1417, NCI-H661) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 418 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.299× (z -9.0) |
| [[KATO III (line)]] | alt | 62.1 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.188× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 120 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.156× (z -12.2) |
| [[A-172 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 3.67 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0497× (z -8.9) |
| [[A-427 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.986 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.898 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.909 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM95A]] | +0.81 | +0.76 / +0.85 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UBBP4-1]] | +0.65 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[PHF2P2]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[LINC02506]] | +0.59 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[LINC02335]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[TPTE]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LINC01205]] | +0.58 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[GRIA2]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[AACSP1]] | +0.56 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ANKRD20A9P]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CCDC144NL-AS1]] | +0.55 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[LINC02484]] | +0.55 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[NCAM2]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAXD]] | -0.49 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[C1orf216]] | -0.48 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[POMGNT1]] | -0.45 | -0.38 / -0.41 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01205]] | C | LINC01205 activity raises ANKRD20A8P's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 3.96× lower at baseline in the lines without LINC01205 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent; co-absent with the target |
| [[TPTE]] | C | TPTE activity raises ANKRD20A8P's level | lines that do not express TPTE (35) vs lines expressing it (15) | 4.64× lower at baseline in the lines without TPTE | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises ANKRD20A8P's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 4.59× lower at baseline in the lines without LINC01242 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |
| [[GABRA3]] | C | GABRA3 activity raises ANKRD20A8P's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without GABRA3 | 0.047 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[ANKRD20A9P]] | C | ANKRD20A9P activity raises ANKRD20A8P's level | lines that do not express ANKRD20A9P (40) vs lines expressing it (10) | 3.86× lower at baseline in the lines without ANKRD20A9P | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MTND1P23, ENSG00000291025, LINC00408; co-absent with the target |
| [[PHF2P2]] | C | PHF2P2 activity raises ANKRD20A8P's level | lines that do not express PHF2P2 (38) vs lines expressing it (12) | 3.78× lower at baseline in the lines without PHF2P2 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287861, ENSG00000291025, LINC00408; co-absent with the target |
| [[UBBP4-1]] | C | UBBP4-1 activity raises ANKRD20A8P's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 3.75× lower at baseline in the lines without UBBP4-1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[LINC00879]] | C | LINC00879 activity raises ANKRD20A8P's level | lines that do not express LINC00879 (46) vs lines expressing it (4) | 5.98× lower at baseline in the lines without LINC00879 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, ENSG00000234426, APOB; co-absent with the target; its own permutation p |
| [[LINC02484]] | C | LINC02484 activity raises ANKRD20A8P's level | lines that do not express LINC02484 (40) vs lines expressing it (10) | 2.12× lower at baseline in the lines without LINC02484 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000260126, LINC02566, ENSG00000289605; co-absent with the target |
| [[NRG3]] | C | NRG3 activity raises ANKRD20A8P's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 1.92× lower at baseline in the lines without NRG3 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[NLGN4X]] | C | NLGN4X activity raises ANKRD20A8P's level | lines that do not express NLGN4X (37) vs lines expressing it (13) | 3.56× lower at baseline in the lines without NLGN4X | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises ANKRD20A8P's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 3.90× lower at baseline in the lines without LINC01446 | 0.073 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 4, C 23. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP63]] | B | ANKRD20A8P activity raises CEP63's level | lines that do not express ANKRD20A8P (38) vs lines expressing it (12) | 1.51× lower at baseline in the lines without ANKRD20A8P | 0.032 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE |
| [[SPAG17]] | B | ANKRD20A8P, [[FAM95A]] activity raises SPAG17's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.40× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent genes |
| [[CHRM3]] | B | ANKRD20A8P, [[FAM95A]] activity raises CHRM3's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.76× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent genes |
| [[ARL4A]] | B | ANKRD20A8P activity raises ARL4A's level | lines that do not express ANKRD20A8P (38) vs lines expressing it (12) | 1.47× lower at baseline in the lines without ANKRD20A8P | 0.094 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE |
| [[TPTE]] | C | ANKRD20A8P, [[FAM95A]] activity raises TPTE's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 9.26× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[GABRA3]] | C | ANKRD20A8P, [[FAM95A]] activity raises GABRA3's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.93× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[PHF2P2]] | C | ANKRD20A8P, [[FAM95A]] activity raises PHF2P2's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.50× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[NLGN4X]] | C | ANKRD20A8P, [[FAM95A]] activity raises NLGN4X's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.16× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[ANKRD20A9P]] | C | ANKRD20A8P activity raises ANKRD20A9P's level | lines that do not express ANKRD20A8P (38) vs lines expressing it (12) | 4.01× lower at baseline in the lines without ANKRD20A8P | 0.011 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |
| [[LINC01205]] | C | ANKRD20A8P, [[FAM95A]] activity raises LINC01205's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 3.02× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[AACSP1]] | C | ANKRD20A8P, [[FAM95A]] activity raises AACSP1's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.10× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[LINC01194]] | C | ANKRD20A8P activity raises LINC01194's level | lines that do not express ANKRD20A8P (38) vs lines expressing it (12) | 4.34× lower at baseline in the lines without ANKRD20A8P | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.8, 28.4); signed map (34.0, 36.7). **Vector** length 25.3, 6.14% of its response variance represented; |z| ≥ 3 in 232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.8 | +1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.4 | -1.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | +0.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -4.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -3.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -3.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 20 family member A8, pseudogene |
| Locus type | pseudogene |
| Location | 2q11.1 — chr2:94,791,103-94,857,282 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously ANKRD20B |
| Matched by | ensembl_id |

UniProt [Q5CZ79](https://www.uniprot.org/uniprotkb/Q5CZ79) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23666) · Entrez [729171](https://www.ncbi.nlm.nih.gov/gene/729171) · UniProt [Q5CZ79](https://www.uniprot.org/uniprotkb/Q5CZ79) · Ensembl [ENSG00000229089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229089)

## Data

Gene col 13690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13690); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13690]; `tensor/DDL_lfc|DDL_z.npy` [13690]; `embed/gene_vectors.npy` [13690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13690 or target_col == 13690). Every well: [[ANKRD20A8P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD20A8P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
