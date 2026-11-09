---
symbol: "TRAPPC13"
type: "gene"
col: 3481
ensembl_id: "ENSG00000113597"
name: "trafficking protein particle complex subunit 13"
location: "5q12.3"
module: 15
arm: "+"
pooled_cpm: 27.47
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TRAPPC13

*trafficking protein particle complex subunit 13* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +13.5, q 6e-39, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.708× (z -9.7, q 3e-19, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf42]] (+0.75, fdr 7e-06), [[DHX35]] (+0.74, fdr 7e-06), [[TMEM267]] (+0.71, fdr 9e-06); moves opposite to [[GDF11]] (-0.65, fdr 1e-05), [[ATP1A3]] (-0.63, fdr 3e-05), [[JUNB]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +13.5 | 6e-39 | 32/47 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +13.0 | 7e-36 | 38/47 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +11.3 | 3e-27 | 38/45 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +8.2 | 3e-14 | 31/48 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +6.7 | 3e-09 | 30/48 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.6 | 3e-09 | 24/48 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.3 | 2e-08 | 26/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +6.3 | 3e-08 | 25/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +6.0 | 1e-07 | 24/48 (RKO, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.8 | 3e-07 | 21/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 1e-04 | 16/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.7 | 1e-04 | 20/47 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.6 | 2e-04 | 20/48 (RKO, LS 180, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.3 | 8e-04 | 14/48 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 9e-04 | 21/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.708×** | -9.7 | 3e-19 | 42/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -9.2 | 7e-18 | 29/43 (SHP-77, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -7.6 | 7e-12 | 21/35 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -5.8 | 9e-07 | 24/48 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.775×** | -5.0 | 6e-05 | 20/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.791×** | -4.6 | 4e-04 | 16/48 (HEC-1-A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.807×** | -4.2 | 0.002 | 16/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.799×** | -4.1 | 0.003 | 18/41 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.1 | 0.11 | 10/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.896× | -3.1 | 0.12 | 5/48 (NCI-H2030, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 39.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.457× (z -8.9) |
| [[LoVo (line)]] | wt | 29.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 21.0 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.0) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.261× (z -9.2) |
| [[A498 (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 23.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 26.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.23× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 49.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 35.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0796× (z -20.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.7) | — |
| [[A-172 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf42]] | +0.75 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[DHX35]] | +0.74 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[TMEM267]] | +0.71 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[LSM8]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MTG2]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.68 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MFSD8]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ELMOD3]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[C8orf76]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[BMS1P4-1]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[QRSL1]] | +0.65 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ANGEL2]] | +0.64 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDF11]] | -0.65 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ATP1A3]] | -0.63 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[JUNB]] | -0.60 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ZDHHC11B]] | -0.60 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[OSBPL8]] | -0.59 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.57 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[USP9X]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[NR4A1]] | -0.56 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[EZR]] | -0.56 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[FOS]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[PADI2]] | -0.55 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ARC]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRAPPC13's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TRAPPC13's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ZDHHC11B]] | B | ZDHHC11B activity raises TRAPPC13's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without ZDHHC11B | 0.067 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens TRAPPC13's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.09× as strongly (z diff -0.34); strongest at Idarubicin (hydrochloride) 5 µM: 1.70x vs 1.22x (z diff -3.7) | 0.857 over the table, 0.068 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.2, 21.2); signed map (-0.6, 0.4). **Vector** length 105, 24.5% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +13.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.3 | -9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.4 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -5.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:65,625,004-65,666,233 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13611, MGC48585; previously C5orf44 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [A5PLN9](https://www.uniprot.org/uniprotkb/A5PLN9) (Trafficking protein particle complex subunit 13):

> Component of the multisubunit TRAPP (transport protein particle) III complex. As a component of TRAPPIII complex, participates in the activation of RAB1 and RAB43, but not RAB11A, RAB11B, nor RAB19.

**Summary**, from NCBI Gene [80006](https://www.ncbi.nlm.nih.gov/gene/80006):

> Predicted to be involved in endoplasmic reticulum to Golgi vesicle-mediated transport; vesicle coating; and vesicle tethering. Predicted to be located in cytosol. Predicted to be part of TRAPPIII protein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25828](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25828) · Entrez [80006](https://www.ncbi.nlm.nih.gov/gene/80006) · UniProt [A5PLN9](https://www.uniprot.org/uniprotkb/A5PLN9) · Ensembl [ENSG00000113597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113597)

## Data

Gene col 3481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3481); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3481]; `tensor/DDL_lfc|DDL_z.npy` [3481]; `embed/gene_vectors.npy` [3481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3481 or target_col == 3481). Every well: [[TRAPPC13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
