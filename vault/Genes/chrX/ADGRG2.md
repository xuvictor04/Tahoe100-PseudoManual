---
symbol: "ADGRG2"
type: "gene"
col: 10418
ensembl_id: "ENSG00000173698"
name: "adhesion G protein-coupled receptor G2"
location: "Xp22.13"
module: 98
arm: "+"
pooled_cpm: 4.57
n_lines_expressing: 40
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# ADGRG2

*adhesion G protein-coupled receptor G2* — Xp22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.41× (z +13.5, q 5e-39, up in 7 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 2.51× (z +8.4, q 6e-15, up in 18 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.108×, NCI-H460 0.305×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.111×; ⚠ cell-cycle shift, explains ~17% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0540×); [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0723×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAOA]] (+0.68, fdr 7e-06), [[VSTM2L]] (+0.67, fdr 7e-06), [[FKBP5]] (+0.67, fdr 7e-06); moves opposite to [[NPTX1]] (-0.63, fdr 1e-05), [[PKIA]] (-0.58, fdr 3e-05), [[SYNJ2]] (-0.56, fdr 1e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NRCAM]] → it (grade B ⚠); 10 go from it, the strongest it → [[KCNMA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.41×** | +13.5 | 5e-39 | 7/9 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.47×** | +13.1 | 6e-37 | 2/3 (C32, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +10.3 | 9e-23 | 2/6 (PANC-1, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.51×** | +8.4 | 6e-15 | 18/26 (NCI-H460, A498, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.9 | 2e-13 | 8/20 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.93×** | +6.0 | 2e-07 | 14/26 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.99×** | +5.8 | 6e-07 | 11/18 (NCI-H460, A498, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +5.5 | 2e-06 | 15/33 (SW480, A-427, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.84×** | +5.3 | 7e-06 | 9/28 (Hs 766T, A549, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.78×** | +5.3 | 8e-06 | 9/28 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +5.2 | 1e-05 | 6/25 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.65×** | +4.6 | 2e-04 | 11/26 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.63×** | +4.5 | 3e-04 | 9/26 (A498, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.62×** | +4.4 | 5e-04 | 10/28 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.004 | 6/18 (A498, A549, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.006 | 8/33 (Hs 766T, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.49×** | +3.6 | 0.011 | 10/31 (A498, NCI-H460, …) | all doses, flat |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.011 | 2/16 (NCI-H1573, HOP62) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10418.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.108×, NCI-H460 0.305×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.111×; ⚠ cell-cycle shift, explains ~17% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0540×); [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0723×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pimozide (drug)]] 5 µM |  | 0.685× | -3.5 | 0.15 | 8/34 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | 0.686× | -3.5 | 0.15 | 6/31 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.690× | -3.2 | 0.24 | 5/33 (COLO 205, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | 0.786× | -3.1 | 0.24 | 6/35 (SW48, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.7 | 2 | 2 (2 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 6.62× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 43.9 | 1 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 4.86× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 5.61 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 12.0× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 4.35 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0723× (z -9.0) |
| [[PANC-1 (line)]] | alt | 1.81 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0540× (z -10.1) |
| [[A-172 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAOA]] | +0.68 | +0.59 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[VSTM2L]] | +0.67 | +0.61 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[FKBP5]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[RIPOR2]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[JPH2]] | +0.64 | +0.53 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[STXBP5-AS1]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MAPK4]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[TLR2]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[KLF9]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CAVIN2]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[KCNG2]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ACSL1]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTX1]] | -0.63 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[PKIA]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[SYNJ2]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[WNT7B]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PTHLH]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[KCNMA1]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FAM107B]] | -0.50 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[C15orf48]] | -0.49 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[LIF]] | -0.49 | -0.49 / -0.51 | both halves | 2e-05 |  |
| [[GJA1]] | -0.48 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[PLAU]] | -0.48 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ADAMTS16]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRCAM]] | B | NRCAM activity raises ADGRG2's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without NRCAM | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[MAPK4]] | B | MAPK4 activity raises ADGRG2's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 1.72× lower at baseline in the lines without MAPK4 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1 |
| [[NR3C1]] | B | NR3C1 activity raises ADGRG2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[SLPI]] | B | SLPI activity raises ADGRG2's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.44× lower at baseline in the lines without SLPI | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[CAVIN2]] | B | CAVIN2 activity raises ADGRG2's level | lines that do not express CAVIN2 (32) vs lines expressing it (18) | 1.46× lower at baseline in the lines without CAVIN2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CAVIN2-AS1, NLGN4Y, PSG9 |
| [[S100P]] | B | S100P activity raises ADGRG2's level | lines that do not express S100P (34) vs lines expressing it (16) | 1.27× lower at baseline in the lines without S100P | 0.068 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMA1]] | B | ADGRG2 activity raises KCNMA1's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 4.40× lower at baseline in the lines without ADGRG2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[PRDX6-AS1]] | B | ADGRG2 activity raises PRDX6-AS1's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.52× lower at baseline in the lines without ADGRG2 | 0.026 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[SLC19A2]] | B | ADGRG2 activity lowers SLC19A2's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without ADGRG2 | 0.036 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[GJA1]] | B | ADGRG2 activity raises GJA1's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 3.53× lower at baseline in the lines without ADGRG2 | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| cells under [[Naproxen (drug)]] 5 µM | B | ADGRG2 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ADGRG2 (10) vs lines expressing it (38) | the lines without ADGRG2: 0.85× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[ADAMTSL4]] | B | ADGRG2 activity raises ADAMTSL4's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.28× lower at baseline in the lines without ADGRG2 | 0.053 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[B3GNT5]] | B | ADGRG2 activity lowers B3GNT5's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 2.19× higher at baseline in the lines without ADGRG2 | 0.065 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[CPD]] | B | ADGRG2 activity lowers CPD's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.21× higher at baseline in the lines without ADGRG2 | 0.071 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[ITGA10]] | B | ADGRG2 activity raises ITGA10's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 2.04× lower at baseline in the lines without ADGRG2 | 0.073 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[GAB3]] | B | ADGRG2 activity raises GAB3's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without ADGRG2 | 0.095 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.7, 16.5); signed map (18.0, 31.1). **Vector** length 61.3, 11.7% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +13.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +10.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.5 | +6.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.3 | +4.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.3 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +5.5 |
| fall | [[Artesunate (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.7 |
|  | [[Hexylresorcinol (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Pimozide (drug)]] 5 µM |  | -0.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor G2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.13 — chrX:18,989,307-19,122,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HE6, TM7LN2, EDDM6; previously GPR64 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily G |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZP9](https://www.uniprot.org/uniprotkb/Q8IZP9) (Adhesion G protein-coupled receptor G2):

> Adhesion G protein-coupled receptor (aGPCR) for steroid hormones, such as dehydroepiandrosterone (DHEA; also named 3beta-hydroxyandrost-5-en-17-one) and androstenedione. Involved in a signal transduction pathway controlling epididymal function and male fertility. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase. ADGRG2 is coupled to G(s) G …

**Summary**, from NCBI Gene [10149](https://www.ncbi.nlm.nih.gov/gene/10149):

> This gene encodes a member of the G protein-coupled receptor family described as an epididymis-specific transmembrane protein. The encoded protein may be proteolytically processed as it contains a motif shown to be a protein scission motif in some members of this family (PMID: 11973329). Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:4516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4516) · Entrez [10149](https://www.ncbi.nlm.nih.gov/gene/10149) · UniProt [Q8IZP9](https://www.uniprot.org/uniprotkb/Q8IZP9) · Ensembl [ENSG00000173698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173698)

## Data

Gene col 10418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10418); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10418]; `tensor/DDL_lfc|DDL_z.npy` [10418]; `embed/gene_vectors.npy` [10418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10418 or target_col == 10418). Every well: [[ADGRG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
