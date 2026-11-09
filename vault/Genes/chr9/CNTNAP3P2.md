---
symbol: "CNTNAP3P2"
type: "gene"
col: 15874
ensembl_id: "ENSG00000276386"
name: "CNTNAP3 pseudogene 2"
location: "9q21.11"
module: 196
arm: "+"
pooled_cpm: 5.32
n_lines_expressing: 31
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# CNTNAP3P2

*CNTNAP3 pseudogene 2* — 9q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.39× (z +9.6, q 5e-19, up in 4 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.49× (z +4.5, q 9e-04, up in 3 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.550× (z -9.7, q 3e-19, down in 18 of 20 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.574× (z -6.3, q 6e-08, down in 15 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP3B]] (+0.86, fdr 7e-06), [[CNTNAP3C]] (+0.78, fdr 7e-06), [[CNTNAP3]] (+0.65, fdr 7e-06); moves opposite to [[CDKL5]] (-0.54, fdr 1e-05), [[TSPAN31]] (-0.48, fdr 1e-04), [[TOX4]] (-0.46, fdr 6e-05).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PTPRZ1]] → it (grade B ⚠); 5 go from it, the strongest it → [[ANKRD20A4P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +9.6 | 5e-19 | 4/12 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +8.2 | 6e-14 | 1/14 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.8 | 1e-06 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +4.5 | 9e-04 | 3/24 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.002 | 7/26 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.008 | 2/22 (A549, A498) | inconsistent across doses | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.23×** | +3.3 | 0.080 | 3/27 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.080 | 4/24 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.2 | 0.080 | 1/27 (NCI-H2030) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.550×** | -9.7 | 3e-19 | 18/20 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.574×** | -6.3 | 6e-08 | 15/26 (SNU-1, A549, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.579×** | -6.2 | 8e-08 | 15/21 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.583×** | -6.2 | 1e-07 | 15/24 (A-427, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.591×** | -5.8 | 8e-07 | 17/24 (PANC-1, SNU-423, …) | two highest doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -4.4 | 0.001 | 16/18 (Hs 766T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -4.1 | 0.003 | 12/27 (Hs 766T, HEC-1-A, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.700×** | -4.1 | 0.003 | 14/27 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.792×** | -3.8 | 0.010 | 9/26 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.4 | 0.042 | 1/28 (MIA PaCa-2) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.736×** | -3.2 | 0.062 | 1/26 (SNU-423) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.755×** | -3.2 | 0.063 | 4/27 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | **0.758×** | -3.2 | 0.067 | 4/25 (CFPAC-1, A-172, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 42.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0990× (z -17.9) |
| [[PANC-1 (line)]] | alt | 7.13 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0337× (z -14.6) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -8.8) |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -9.4) |
| [[SW480 (line)]] | alt | 6.27 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.10 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.122× (z -8.7) |
| [[A498 (line)]] | wt | 4.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0963× (z -10.9) |
| [[A549 (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -15.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 7.85 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0859× (z -8.5) |
| [[C32 (line)]] | wt | 17.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -8.7) |
| [[HS-578T (line)]] | alt | 5.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0775× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 7.38 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -13.8) |
| [[SW 900 (line)]] | alt | 6.49 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0743× (z -8.7) |
| [[A-172 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.537 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP3B]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP3C]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP3]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[AP3M2]] | +0.49 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD20A4P]] | +0.49 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[XYLB]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CHST10]] | +0.49 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[ANKRD20A1]] | +0.49 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[ANKRD29]] | +0.48 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[STAMBPL1]] | +0.47 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[LRIG3]] | +0.47 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[ALKBH8]] | +0.46 | +0.42 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL5]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TSPAN31]] | -0.48 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[TOX4]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[MIR583HG]] | -0.44 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[GCC1]] | -0.44 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[C6orf62]] | -0.43 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[MAP1LC3A]] | -0.42 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[MED29]] | -0.42 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[YIPF3]] | -0.42 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[BOLA1]] | -0.42 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[DAXX]] | -0.41 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ZKSCAN1]] | -0.40 | -0.43 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRZ1]] | B | PTPRZ1 activity raises CNTNAP3P2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.01× lower at baseline in the lines without PTPRZ1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[CNTNAP3B]] | C | CNTNAP3B activity raises CNTNAP3P2's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 3.97× lower at baseline in the lines without CNTNAP3B | 4e-04 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[CNTNAP3]] | C | CNTNAP3 activity raises CNTNAP3P2's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 3.44× lower at baseline in the lines without CNTNAP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[CNTNAP3C]] | C | CNTNAP3C activity raises CNTNAP3P2's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 3.05× lower at baseline in the lines without CNTNAP3C | 0.002 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A4P]] | B | CNTNAP3P2 activity raises ANKRD20A4P's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without CNTNAP3P2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C |
| [[ANKRD20A1]] | B | CNTNAP3P2 activity raises ANKRD20A1's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without CNTNAP3P2 | 0.091 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C |
| [[CNTNAP3B]] | C | CNTNAP3P2 activity raises CNTNAP3B's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 4.93× lower at baseline in the lines without CNTNAP3P2 | 7e-04 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[CNTNAP3]] | C | CNTNAP3P2 activity raises CNTNAP3's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 3.35× lower at baseline in the lines without CNTNAP3P2 | 0.006 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[CNTNAP3C]] | C | CNTNAP3P2 activity raises CNTNAP3C's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without CNTNAP3P2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.7, 28.7); signed map (19.8, 58.7). **Vector** length 49.2, 9.47% of its response variance represented; |z| ≥ 3 in 614 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.6 | +4.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.8 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.5 | -9.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -6.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | CNTNAP3 pseudogene 2 |
| Locus type | pseudogene |
| Location | 9q21.11 — chr9:67,059,560-67,293,468 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49589) · Entrez [643827](https://www.ncbi.nlm.nih.gov/gene/643827) · Ensembl [ENSG00000276386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276386)

## Data

Gene col 15874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15874); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15874]; `tensor/DDL_lfc|DDL_z.npy` [15874]; `embed/gene_vectors.npy` [15874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15874 or target_col == 15874). Every well: [[CNTNAP3P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTNAP3P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
