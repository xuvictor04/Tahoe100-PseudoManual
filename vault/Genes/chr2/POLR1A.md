---
symbol: "POLR1A"
type: "gene"
col: 896
ensembl_id: "ENSG00000068654"
name: "RNA polymerase I subunit A"
location: "2p11.2"
module: 4
arm: "+"
pooled_cpm: 46.91
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# POLR1A

*RNA polymerase I subunit A* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.14× (z +12.8, q 1e-34, up in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.60× (z +8.4, q 4e-15, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.794× (z -3.9, q 0.052, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.832× (z -3.7, q 0.054, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.254×, NCI-H1573 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.438×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.677×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.86, fdr 7e-06), [[BYSL]] (+0.84, fdr 7e-06), [[MYBBP1A]] (+0.83, fdr 7e-06); moves opposite to [[RSRP1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FBXO32]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.14×** | +12.8 | 1e-34 | 45/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.11×** | +12.6 | 6e-34 | 41/48 (AsPC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.87×** | +10.5 | 1e-23 | 40/48 (AsPC-1, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.85×** | +10.3 | 7e-23 | 37/48 (NCI-H1792, A-172, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +8.4 | 4e-15 | 38/48 (PANC-1, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +8.2 | 2e-14 | 35/48 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.54×** | +7.3 | 3e-11 | 25/45 (Hs 766T, NCI-H1792, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.2 | 4e-11 | 26/48 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +6.7 | 1e-09 | 27/48 (NCI-H1792, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.8 | 5e-07 | 27/48 (A-172, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.40×** | +5.7 | 6e-07 | 31/47 (NCI-H460, hTERT-HPNE, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.91×** | +5.7 | 6e-07 | 30/47 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.90×** | +5.6 | 8e-07 | 36/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 9e-07 | 32/48 (LOX-IMVI, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +5.4 | 2e-06 | 28/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.81×** | +5.2 | 7e-06 | 34/48 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 8e-06 | 27/48 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +5.2 | 8e-06 | 26/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +5.1 | 8e-06 | 29/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.1 | 1e-05 | 26/48 (LS 180, H4, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 6e-04 | 22/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.254×, NCI-H1573 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.438×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.677×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.794×** | -3.9 | 0.052 | 27/48 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.832×** | -3.7 | 0.054 | 20/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.826× | -3.2 | 0.21 | 16/47 (LoVo, HOP62, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.877× | -3.2 | 0.21 | 10/48 (KATO III, LS 180, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 20.2 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.00× (z +11.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 50.6 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +9.4) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 41.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A-427 (line)]] | wt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[A549 (line)]] | wt | 51.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.87× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 31.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.14× (z +8.9) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[NCI-H23 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 59.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.57× (z +10.0) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[HS-578T (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +9.2) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[LS 180 (line)]] | wt | 38.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 66.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.70× (z +9.0) ⚠ unreliable plate only | — |
| [[PANC-1 (line)]] | alt | 63.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.11× (z +9.1) ⚠ unreliable plate only | — |
| [[RPMI-7951 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SNU-423 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +10.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW 900 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 66.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.86 | +0.83 / +0.89 | both halves | 7e-06 | STRING 475 |
| [[BYSL]] | +0.84 | +0.86 / +0.82 | both halves | 7e-06 | STRING 856 |
| [[MYBBP1A]] | +0.83 | +0.76 / +0.86 | both halves | 7e-06 | pathway: B-WICH complex positively regulates rRNA expression; STRING 964 |
| [[MRPS27]] | +0.81 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[PUM3]] | +0.81 | +0.78 / +0.82 | both halves | 7e-06 | STRING 862 |
| [[URB2]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 |  |
| [[PUS1]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 | STRING 455 |
| [[DDX10]] | +0.80 | +0.78 / +0.80 | both halves | 7e-06 | STRING 719 |
| [[MDN1]] | +0.80 | +0.73 / +0.82 | both halves | 7e-06 | STRING 486 |
| [[EFTUD2]] | +0.80 | +0.78 / +0.77 | both halves | 7e-06 | STRING 798 |
| [[LETM1]] | +0.79 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.78 | +0.78 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.68 | -0.64 / -0.71 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO32]] | B | FBXO32 activity lowers POLR1A's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.76× higher at baseline in the lines without FBXO32 | 0.004 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[MPZL3]] | B | MPZL3 activity lowers POLR1A's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.37× higher at baseline in the lines without MPZL3 | 0.079 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[LDLRAD3]] | B | LDLRAD3 activity raises POLR1A's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without LDLRAD3 | 0.096 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MTHFD1L]], [[USP31]] | C | MTHFD1L, USP31 activity raises POLR1A's level | lines that do not express MTHFD1L, USP31 (3) vs lines expressing them (47) | 2.25× lower at baseline in the lines without MTHFD1L, USP31 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.861). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.6, -35.8); signed map (-3.8, -47.7). **Vector** length 130, 39.9% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.52 to 21); *tRNA Aminoacylation* (reactome, mean cos +0.55 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.1 | +12.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +8.4 |
|  | [[EX229 (drug)]] 5 µM |  | +5.7 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.6 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.3 | +5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.0 | +5.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.5 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I subunit A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:86,020,216-86,106,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586M0122, FLJ21915, RPO1-4, RPA1, RPA190 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 9 pathways, smallest: RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression; RNA Polymerase I Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [O95602](https://www.uniprot.org/uniprotkb/O95602) (DNA-directed RNA polymerase I subunit RPA1):

> Catalytic core component of RNA polymerase I (Pol I), a DNA-dependent RNA polymerase which synthesizes ribosomal RNA precursors using the four ribonucleoside triphosphates as substrates. Transcribes 47S pre-rRNAs from multicopy rRNA gene clusters, giving rise to 5.8S, 18S and 28S ribosomal RNAs. Pol I-mediated transcription cycle proceeds through transcription initiation, transcription elongation and transcription termination stages. During transcription initiation, Pol I pre-initiation complex …

**Summary**, from NCBI Gene [25885](https://www.ncbi.nlm.nih.gov/gene/25885):

> The protein encoded by this gene is the largest subunit of the RNA polymerase I complex. The encoded protein represents the catalytic subunit of the complex, which transcribes DNA into ribosomal RNA precursors. Defects in this gene are a cause of the Cincinnati type of acrofacial dysostosis. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:17264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17264) · Entrez [25885](https://www.ncbi.nlm.nih.gov/gene/25885) · UniProt [O95602](https://www.uniprot.org/uniprotkb/O95602) · Ensembl [ENSG00000068654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068654)

## Data

Gene col 896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 896); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 896]; `tensor/DDL_lfc|DDL_z.npy` [896]; `embed/gene_vectors.npy` [896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 896 or target_col == 896). Every well: [[POLR1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
