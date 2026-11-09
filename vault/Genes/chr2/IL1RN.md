---
symbol: "IL1RN"
type: "gene"
col: 5888
ensembl_id: "ENSG00000136689"
name: "interleukin 1 receptor antagonist"
location: "2q14.1"
module: 31
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 23
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 56
direction_downstream: 80
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# IL1RN

*interleukin 1 receptor antagonist* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.85× (z +11.0, q 2e-25, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.50× (z +9.4, q 2e-18, up in 3 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.112×, LS 180 0.145×); [[Panobinostat (drug)]] 5 µM in 2 lines (HT-29 0.0659×, HepG2/C3A 0.128×); [[Belinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.0848×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM5]] (+0.68, fdr 7e-06), [[SLC28A3]] (+0.63, fdr 7e-06), [[CEACAM6]] (+0.62, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[LAMA3]] → it (grade B ⚠); 80 go from it, the strongest it → [[KPNA7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.85×** | +11.0 | 2e-25 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +9.4 | 2e-18 | 3/14 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +7.4 | 2e-11 | 2/6 (LS 180, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +7.4 | 2e-11 | 3/9 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +5.4 | 6e-06 | 2/12 (COLO 205, LoVo) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.10×** | +5.3 | 8e-06 | 10/19 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.07×** | +5.3 | 1e-05 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +5.0 | 4e-05 | 3/16 (A-172, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +4.8 | 1e-04 | 6/15 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.52×** | +4.6 | 2e-04 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.001 | 2/20 (KATO III, COLO 205) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.1 | 0.002 | 3/9 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.74×** | +4.0 | 0.003 | 9/17 (KATO III, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.004 | 6/16 (LS 180, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.70×** | +3.8 | 0.005 | 1/11 (NCI-H2347) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +3.7 | 0.007 | 3/15 (NCI-H2347, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.008 | 8/20 (LS 180, BT-474, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.016 | 4/17 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.019 | 1/19 (HS-578T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.030 | 4/18 (A-172, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.037 | 4/13 (HS-578T, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5888.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.112×, LS 180 0.145×); [[Panobinostat (drug)]] 5 µM in 2 lines (HT-29 0.0659×, HepG2/C3A 0.128×); [[Belinostat (drug)]] 5 µM in 1 line (HepG2/C3A 0.0848×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.600× | -3.4 | 0.27 | 4/19 (BT-474, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.636× | -3.3 | 0.27 | 6/17 (BT-474, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.655× | -3.1 | 0.31 | 8/20 (HepG2/C3A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.663× | -3.0 | 0.31 | 3/20 (HT-29, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0848× (z -10.3) |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -12.5) |
| [[BT-474 (line)]] | alt | 7.86 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0672× (z -9.1) |
| [[LS 180 (line)]] | wt | 9.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -10.6) |
| [[A-172 (line)]] | wt | 0.907 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.802 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.788 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.503 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM5]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SLC28A3]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CEACAM6]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[FLRT3]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TACSTD2]] | +0.61 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[ABHD11]] | +0.61 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[KRT23]] | +0.61 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[LINC01559]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CAPN8]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[C1orf116]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[TSPAN1]] | +0.59 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TNNT2]] | +0.59 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 3, C 53. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | LAMA3 activity raises IL1RN's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.36× lower at baseline in the lines without LAMA3 | 0.021 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[TOP2A]] | B | TOP2A activity lowers IL1RN's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DSC2]] | B | DSC2 activity raises IL1RN's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 2.26× lower at baseline in the lines without DSC2 | 0.096 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[SLC6A14]] | C | SLC6A14 activity raises IL1RN's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 6.70× lower at baseline in the lines without SLC6A14 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[MUC5AC]] | C | MUC5AC activity raises IL1RN's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 5.21× lower at baseline in the lines without MUC5AC | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |
| [[DAPP1]] | C | DAPP1 activity raises IL1RN's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 4.86× lower at baseline in the lines without DAPP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises IL1RN's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 4.04× lower at baseline in the lines without TMEM30B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises IL1RN's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.52× lower at baseline in the lines without LAD1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises IL1RN's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.43× lower at baseline in the lines without TMPRSS4 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises IL1RN's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 5.01× lower at baseline in the lines without MUC2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[TNNT2]] | C | TNNT2 activity raises IL1RN's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 3.42× lower at baseline in the lines without TNNT2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises IL1RN's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.43× lower at baseline in the lines without MPZL2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |

### Downstream of this gene

*80 arrows, 80 of them with an alert ⚠; grade A 0, B 31, C 49. Shown: the 12 strongest; 68 more arrows (68 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA7]] | B | IL1RN activity raises KPNA7's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.93× lower at baseline in the lines without IL1RN | 6e-04 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[FAM83E]] | B | IL1RN activity raises FAM83E's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.71× lower at baseline in the lines without IL1RN | 0.003 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[LAMA3]] | B | IL1RN activity raises LAMA3's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 3.11× lower at baseline in the lines without IL1RN | 0.010 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[DSC2]] | B | IL1RN activity raises DSC2's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 3.29× lower at baseline in the lines without IL1RN | 0.011 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[SRMS]] | B | IL1RN activity raises SRMS's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without IL1RN | 0.015 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[KRT86]] | B | IL1RN activity raises KRT86's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without IL1RN | 0.020 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[ARHGAP27]] | B | IL1RN activity raises ARHGAP27's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 1.89× lower at baseline in the lines without IL1RN | 0.021 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[XDH]] | B | IL1RN activity raises XDH's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.93× lower at baseline in the lines without IL1RN | 0.022 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[LGALS9]] | B | IL1RN activity raises LGALS9's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.51× lower at baseline in the lines without IL1RN | 0.023 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[TNFAIP8]] | B | IL1RN activity raises TNFAIP8's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 1.55× lower at baseline in the lines without IL1RN | 0.028 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[FUT2]] | B | IL1RN activity raises FUT2's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.04× lower at baseline in the lines without IL1RN | 0.028 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[TNFRSF21]] | B | IL1RN activity raises TNFRSF21's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.77× lower at baseline in the lines without IL1RN | 0.030 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.8, 57.3); signed map (59.3, 8.3). **Vector** length 44.3, 10.6% of its response variance represented; |z| ≥ 3 in 479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor antagonist |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:113,099,315-113,134,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL1RA, ICIL-1RA, IL1F3, IRAP, IL-1RN, MGC10430 |
| Gene groups (HGNC) | Interleukins; Interleukin 1 family |
| Reactome | 5 pathways, smallest: Interleukin-10 signaling; Interleukin-1 signaling; Interleukin-1 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P18510](https://www.uniprot.org/uniprotkb/P18510) (Interleukin-1 receptor antagonist protein):

> Anti-inflammatory antagonist of interleukin-1 family of pro-inflammatory cytokines such as interleukin-1beta/IL1B and interleukin-1alpha/IL1A. Protects from immune dysregulation and uncontrolled systemic inflammation triggered by IL1 for a range of innate stimulatory agents such as pathogens.

**Summary**, from NCBI Gene [3557](https://www.ncbi.nlm.nih.gov/gene/3557):

> The protein encoded by this gene is a member of the interleukin 1 cytokine family. This protein inhibits the activities of interleukin 1, alpha (IL1A) and interleukin 1, beta (IL1B), and modulates a variety of interleukin 1 related immune and inflammatory responses, particularly in the acute phase of infection and inflammation. This gene and five other closely related cytokine genes form a gene cluster spanning approximately 400 kb on chromosome 2. A polymorphism of this gene is reported to be …

**Accessions** — [HGNC:6000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6000) · Entrez [3557](https://www.ncbi.nlm.nih.gov/gene/3557) · UniProt [P18510](https://www.uniprot.org/uniprotkb/P18510) · Ensembl [ENSG00000136689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136689)

## Data

Gene col 5888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5888); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5888]; `tensor/DDL_lfc|DDL_z.npy` [5888]; `embed/gene_vectors.npy` [5888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5888 or target_col == 5888). Every well: [[IL1RN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1RN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
