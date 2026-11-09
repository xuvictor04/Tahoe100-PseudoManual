---
symbol: "FAM95A"
type: "gene"
col: 16443
ensembl_id: "ENSG00000289811"
name: "family with sequence similarity 95 member A"
location: "2q11.1"
module: 177
arm: "+"
pooled_cpm: 3.9
n_lines_expressing: 12
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 28
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# FAM95A

*family with sequence similarity 95 member A* — 2q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.27× (z +11.3, q 6e-27, up in 4 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[(S)-Crizotinib (drug)]] 0.05 µM: 0.517× (z -4.1, q 0.020, down in 2 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (KATO III 0.119×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD20A8P]] (+0.81, fdr 7e-06, ⚠ same locus), [[PHF2P2]] (+0.61, fdr 7e-06), [[GRIA2]] (+0.55, fdr 5e-05), [[TPTE]] (+0.54, fdr 1e-05); moves opposite to [[FBXW11]] (-0.42, fdr 1e-04), [[SLC38A9]] (-0.41, fdr 2e-04), [[SRP14]] (-0.40, fdr 5e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC01205]] → it (grade C ⚠); 28 go from it, the strongest it → [[SPAG17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.27×** | +11.3 | 6e-27 | 4/7 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.51×** | +11.1 | 5e-26 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.43×** | +10.0 | 2e-21 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.78×** | +8.3 | 1e-14 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.28×** | +5.6 | 3e-06 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.75×** | +4.9 | 1e-04 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.73×** | +4.8 | 1e-04 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +4.7 | 2e-04 | 3/8 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.90×** | +4.3 | 9e-04 | 1/5 (A-172) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.89×** | +4.3 | 0.001 | 0/8 | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.001 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.002 | 3/9 (NCI-H23, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +4.1 | 0.002 | 8/9 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.9 | 0.004 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.98×** | +3.8 | 0.004 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.008 | 0/8 | inconsistent across doses | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.74×** | +3.5 | 0.017 | 0/7 | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.019 | 2/5 (H4, HS-578T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trimetrexate (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.021 | 0/9 | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.98×** | +3.3 | 0.027 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.59×** | +2.9 | 0.092 | 0/7 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16443.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (KATO III 0.119×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.517×** | -4.1 | 0.020 | 2/9 (HS-578T, NCI-H23) | inconsistent across doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.594× | -3.3 | 0.26 | 0/9 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.624× | -3.2 | 0.26 | 0/9 | two highest doses |  |
| [[Sildenafil (drug)]] 0.05 µM |  | 0.617× | -3.0 | 0.30 | 1/9 (A-427) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | 0.642× | -3.0 | 0.30 | 0/9 | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 35.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.119× (z -8.9) |
| [[A-172 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.380 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD20A8P]] | +0.81 | +0.76 / +0.85 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PHF2P2]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[GRIA2]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[TPTE]] | +0.54 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[AACSP1]] | +0.54 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LINC01205]] | +0.54 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[FAR2P1]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[GABRA3]] | +0.53 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[MIR3667HG]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CSMD3]] | +0.50 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[LINC01446]] | +0.50 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CDH12]] | +0.50 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[LINC02335]] | +0.49 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW11]] | -0.42 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[SLC38A9]] | -0.41 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[SRP14]] | -0.40 | -0.23 / -0.31 | both halves | 5e-04 |  |
| [[GLUD1P3]] | -0.40 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[NFATC3]] | -0.39 | -0.41 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01205]] | C | LINC01205 activity raises FAM95A's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 2.69× lower at baseline in the lines without LINC01205 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent; co-absent with the target |
| [[LINC00648]] | C | LINC00648 activity raises FAM95A's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 2.48× lower at baseline in the lines without LINC00648 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises FAM95A's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 3.52× lower at baseline in the lines without LINC01242 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises FAM95A's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 2.53× lower at baseline in the lines without LINC01687 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[LINC00879]] | C | LINC00879 activity raises FAM95A's level | lines that do not express LINC00879 (46) vs lines expressing it (4) | 3.86× lower at baseline in the lines without LINC00879 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, ENSG00000234426, APOB; co-absent with the target; its own permutation p |
| [[TPTE]] | C | TPTE activity raises FAM95A's level | lines that do not express TPTE (35) vs lines expressing it (15) | 3.40× lower at baseline in the lines without TPTE | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P; co-absent with the target |
| [[LINC02484]] | C | LINC02484 activity raises FAM95A's level | lines that do not express LINC02484 (40) vs lines expressing it (10) | 1.69× lower at baseline in the lines without LINC02484 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000260126, LINC02566, ENSG00000289605; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises FAM95A's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 3.67× lower at baseline in the lines without LINC02616 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |
| [[UBBP4-1]] | C | UBBP4-1 activity raises FAM95A's level | lines that do not express UBBP4-1 (34) vs lines expressing it (16) | 2.95× lower at baseline in the lines without UBBP4-1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253363, MIR548XHG, ENSG00000291025; co-absent with the target |
| [[GABRA3]] | C | GABRA3 activity raises FAM95A's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without GABRA3 | 0.095 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 3, C 25. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPAG17]] | B | [[ANKRD20A8P]], FAM95A activity raises SPAG17's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.40× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent genes |
| [[CHRM3]] | B | [[ANKRD20A8P]], FAM95A activity raises CHRM3's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.76× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent genes |
| [[LDB2]] | B | FAM95A activity raises LDB2's level | lines that do not express FAM95A (38) vs lines expressing it (12) | 2.08× lower at baseline in the lines without FAM95A | 0.070 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE |
| [[TPTE]] | C | [[ANKRD20A8P]], FAM95A activity raises TPTE's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 9.26× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[GABRA3]] | C | [[ANKRD20A8P]], FAM95A activity raises GABRA3's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.93× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[MIR548XHG]] | C | FAM95A activity raises MIR548XHG's level | lines that do not express FAM95A (38) vs lines expressing it (12) | 5.39× lower at baseline in the lines without FAM95A | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |
| [[PHF2P2]] | C | [[ANKRD20A8P]], FAM95A activity raises PHF2P2's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.50× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[LINC02616]] | C | FAM95A activity raises LINC02616's level | lines that do not express FAM95A (38) vs lines expressing it (12) | 4.53× lower at baseline in the lines without FAM95A | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |
| [[NLGN4X]] | C | [[ANKRD20A8P]], FAM95A activity raises NLGN4X's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 5.16× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[BAGE2]] | C | FAM95A activity raises BAGE2's level | lines that do not express FAM95A (38) vs lines expressing it (12) | 5.13× lower at baseline in the lines without FAM95A | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |
| [[LINC01205]] | C | [[ANKRD20A8P]], FAM95A activity raises LINC01205's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 3.02× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |
| [[AACSP1]] | C | [[ANKRD20A8P]], FAM95A activity raises AACSP1's level | lines that do not express ANKRD20A8P, FAM95A (38) vs lines expressing them (12) | 2.10× lower at baseline in the lines without ANKRD20A8P, FAM95A | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.8, 31.6); signed map (33.6, 36.4). **Vector** length 17.6, 3.35% of its response variance represented; |z| ≥ 3 in 244 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.6 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.6 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.6 | +1.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -3.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.5 | -3.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.5 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 95 member A |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q11.1 — chr2:94,755,326-94,798,875 (-) |
| Ensembl biotype | lncRNA |
| Also known as | DKFZp434H0923 |
| Gene groups (HGNC) | Long non-coding RNAs with FAM root symbol |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28069) · Entrez [90499](https://www.ncbi.nlm.nih.gov/gene/90499) · Ensembl [ENSG00000289811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000289811)

## Data

Gene col 16443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16443); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16443]; `tensor/DDL_lfc|DDL_z.npy` [16443]; `embed/gene_vectors.npy` [16443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16443 or target_col == 16443). Every well: [[FAM95A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM95A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
