---
symbol: "CACNG7"
type: "gene"
col: 2624
ensembl_id: "ENSG00000105605"
name: "calcium voltage-gated channel auxiliary subunit gamma 7"
location: "19q13.42"
module: 82
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 29
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 18
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# CACNG7

*calcium voltage-gated channel auxiliary subunit gamma 7* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.07× (z +13.5, q 1e-38, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 3.00× (z +12.1, q 4e-31, up in 19 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.543× (z -4.8, q 0.001, down in 13 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.316×, PANC-1 0.425×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.243×; ⚠ cell-cycle shift, explains ~2% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (NCI-H23 0.0685×); [[ETC-206 (drug)]] 0.05 µM in 1 line (HOP62 0.0625×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOVA2]] (+0.70, fdr 7e-06), [[EBF2]] (+0.67, fdr 2e-05), [[BMERB1]] (+0.64, fdr 1e-05); moves opposite to [[RNF146]] (-0.53, fdr 6e-05), [[FBXW4]] (-0.52, fdr 2e-04), [[NNT]] (-0.51, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PPP1R14A]] → it (grade B ⚠); 18 go from it, the strongest it → [[EML2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.07×** | +13.5 | 1e-38 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.00×** | +12.1 | 4e-31 | 19/23 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.97×** | +10.7 | 2e-24 | 1/9 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.65×** | +9.3 | 2e-18 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.87×** | +8.2 | 3e-14 | 16/20 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +7.5 | 7e-12 | 3/17 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +7.2 | 7e-11 | 13/24 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +7.0 | 2e-10 | 12/23 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.34×** | +6.6 | 3e-09 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.22×** | +6.2 | 3e-08 | 3/19 (A-427, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **2.17×** | +6.0 | 1e-07 | 12/24 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +5.9 | 1e-07 | 16/24 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +5.9 | 2e-07 | 4/16 (RPMI-7951, C32, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.91×** | +5.0 | 2e-05 | 7/13 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.44×** | +4.9 | 3e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.004 | 2/23 (NCI-H1792, NCI-H2030) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.60×** | +3.6 | 0.009 | 6/23 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.52×** | +3.0 | 0.061 | 1/11 (HS-578T) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.061 | 0/12 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.061 | 0/14 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2624.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.316×, PANC-1 0.425×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.243×; ⚠ cell-cycle shift, explains ~2% of this change); [[Hesperidin (drug)]] 5 µM in 1 line (NCI-H23 0.0685×); [[ETC-206 (drug)]] 0.05 µM in 1 line (HOP62 0.0625×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.543×** | -4.8 | 0.001 | 13/23 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.660× | -3.3 | 0.32 | 10/22 (NCI-H23, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.1 | 2 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.46× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -10.1) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.425× (z -8.7) |
| [[A549 (line)]] | wt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -8.9) |
| [[HOP62 (line)]] | alt | 2.82 | 0 | 1 | — | [[ETC-206 (drug)]] 0.05 µM 0.0625× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 5.30 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0685× (z -9.6) |
| [[A-172 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.658 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.670 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.678 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.948 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.756 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.719 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.783 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.344 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOVA2]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[EBF2]] | +0.67 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[BMERB1]] | +0.64 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[JAKMIP1]] | +0.64 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[VAT1L]] | +0.63 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[PTPRS]] | +0.63 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[CELF5]] | +0.62 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[KIF5C]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[LPAR3]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SYN1]] | +0.61 | +0.34 / +0.69 | both halves | 1e-04 |  |
| [[ARID3B]] | +0.60 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[PDZD4]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF146]] | -0.53 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[FBXW4]] | -0.52 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[NNT]] | -0.51 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ARFGAP2]] | -0.51 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[DECR1]] | -0.51 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[PSME3IP1]] | -0.51 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[PPP1R7]] | -0.50 | -0.37 / -0.50 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R14A]] | B | PPP1R14A activity raises CACNG7's level | lines that do not express PPP1R14A (39) vs lines expressing it (11) | 2.36× lower at baseline in the lines without PPP1R14A | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, SFTPA2 |
| [[RET]] | B | RET activity raises CACNG7's level | lines that do not express RET (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without RET | 0.070 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[FSD1]] | C | FSD1 activity raises CACNG7's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.88× lower at baseline in the lines without FSD1 | 0.034 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2; co-absent with the target |
| [[MIR493HG]] | C | MIR493HG activity raises CACNG7's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 1.80× lower at baseline in the lines without MIR493HG | 0.040 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 14, C 4. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EML2]] | B | CACNG7 activity raises EML2's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.28× lower at baseline in the lines without CACNG7 | 0.038 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[EFEMP2]] | B | CACNG7 activity raises EFEMP2's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without CACNG7 | 0.048 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[MEG3]] | B | CACNG7 activity raises MEG3's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 2.60× lower at baseline in the lines without CACNG7 | 0.061 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[BCORL1]] | B | CACNG7 activity raises BCORL1's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without CACNG7 | 0.062 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[SPANXA2-OT1]] | B | CACNG7 activity raises SPANXA2-OT1's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without CACNG7 | 0.076 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | CACNG7 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.24× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | B | CACNG7 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.21× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[CYS1]] | B | CACNG7 activity raises CYS1's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.55× lower at baseline in the lines without CACNG7 | 0.089 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| cells under [[AZD2858 (drug)]] 5 µM | B | CACNG7 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.30× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| cells under [[Penfluridol (drug)]] 5 µM | B | CACNG7 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.16× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| cells under [[Clotrimazole (drug)]] 0.5 µM | B | CACNG7 activity lowers the cells' numbers under Clotrimazole 0.5 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.18× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| cells under [[Pimozide (drug)]] 0.05 µM | B | CACNG7 activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.17× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.7, 39.1); signed map (27.4, 29.0). **Vector** length 36.9, 6.41% of its response variance represented; |z| ≥ 3 in 547 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +12.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +13.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Encorafenib (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit gamma 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:53,909,278-53,943,950 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Calcium channel auxiliary gamma subunits |
| Reactome | 7 pathways, smallest: Phase 2 - plateau phase; Mechanical load activates signaling by PIEZO1 and integrins in osteocytes; Phase 0 - rapid depolarisation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62955](https://www.uniprot.org/uniprotkb/P62955) (Voltage-dependent calcium channel gamma-7 subunit):

> Regulates the activity of L-type calcium channels that contain CACNA1C as pore-forming subunit. Regulates the trafficking and gating properties of AMPA-selective glutamate receptors (AMPARs). Promotes their targeting to the cell membrane and synapses and modulates their gating properties by slowing their rates of activation, deactivation and desensitization and by mediating their resensitization. Displays subunit-specific AMPA receptor regulation. Shows specificity only for GRIA1 and GRIA2.

**Summary**, from NCBI Gene [59284](https://www.ncbi.nlm.nih.gov/gene/59284):

> The protein encoded by this gene is a type II transmembrane AMPA receptor regulatory protein (TARP). TARPs regulate both trafficking and channel gating of the AMPA receptors. This gene is part of a functionally diverse eight-member protein subfamily of the PMP-22/EMP/MP20 family and is located in a cluster with two family members, a type I TARP and a calcium channel gamma subunit. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:13626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13626) · Entrez [59284](https://www.ncbi.nlm.nih.gov/gene/59284) · UniProt [P62955](https://www.uniprot.org/uniprotkb/P62955) · Ensembl [ENSG00000105605](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105605)

## Data

Gene col 2624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2624); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2624]; `tensor/DDL_lfc|DDL_z.npy` [2624]; `embed/gene_vectors.npy` [2624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2624 or target_col == 2624). Every well: [[CACNG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
