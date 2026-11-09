---
symbol: "PINLYP"
type: "gene"
col: 13962
ensembl_id: "ENSG00000234465"
name: "phospholipase A2 inhibitor and LY6/PLAUR domain containing"
location: "19q13.31"
module: 112
arm: "+"
pooled_cpm: 2.4
n_lines_expressing: 33
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# PINLYP

*phospholipase A2 inhibitor and LY6/PLAUR domain containing* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.14× (z +14.6, q 3e-45, up in 11 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.559× (z -3.9, q 0.047, down in 8 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Raltitrexed (drug)]] 5 µM in 1 line (AN3 CA 0.233×; ⚠ cell-cycle shift, explains ~95% of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (A-172 0.0794×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.111×; ⚠ toxic; cell-cycle shift, explains ~42% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL11]] (+0.66, fdr 7e-06), [[CD82]] (+0.64, fdr 7e-06), [[LINC00973]] (+0.62, fdr 1e-05); moves opposite to [[NCKAP1]] (-0.54, fdr 3e-05), [[CLASP1]] (-0.49, fdr 4e-05), [[PPP4R1]] (-0.49, fdr 5e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IL11]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLC37A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.14×** | +14.6 | 3e-45 | 11/16 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.76×** | +13.6 | 2e-39 | 8/14 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +8.1 | 1e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +6.5 | 1e-08 | 7/16 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.55×** | +6.2 | 5e-08 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.39×** | +6.1 | 1e-07 | 13/23 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.98×** | +4.9 | 6e-05 | 1/6 (A-172) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.4 | 6e-04 | 2/26 (HEC-1-A, NCI-H2030) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +4.4 | 6e-04 | 2/9 (A-172, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.85×** | +4.3 | 0.001 | 2/9 (J82, A-172) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.78×** | +4.0 | 0.003 | 3/18 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.7 | 0.010 | 0/12 | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.015 | 4/20 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.016 | 1/25 (C-33 A) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.39×** | +3.3 | 0.036 | 0/3 | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.048 | 1/11 (SK-MEL-2) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.074 | 3/24 (HOP62, H4, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13962.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Raltitrexed (drug)]] 5 µM in 1 line (AN3 CA 0.233×; ⚠ cell-cycle shift, explains ~95% of this change); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (A-172 0.0794×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW 900 0.111×; ⚠ toxic; cell-cycle shift, explains ~42% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.559×** | -3.9 | 0.047 | 8/25 (SK-MEL-2, SW 900, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.587×** | -3.6 | 0.076 | 11/27 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | 0.639× | -3.3 | 0.14 | 8/23 (SW 900, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.629× | -3.3 | 0.14 | 5/18 (A-172, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.652× | -3.1 | 0.14 | 8/18 (SW 900, HCT15, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.656× | -3.1 | 0.14 | 8/26 (A-172, SK-MEL-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.656× | -3.1 | 0.14 | 8/18 (SK-MEL-2, RKO, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.744× | -3.1 | 0.14 | 6/27 (hTERT-HPNE, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.15 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +14.2) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0794× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +8.5) | — |
| [[A549 (line)]] | wt | 0.904 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 0.713 | 0 | 1 (1 ⚠) | — | [[Raltitrexed (drug)]] 5 µM 0.233× (z -11.9) ⚠ cell-cycle shift, explains ~95% of this change |
| [[hTERT-HPNE (line)]] | wt | 3.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +9.2) | — |
| [[J82 (line)]] | alt | 1.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 0.705 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.3× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.111× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.717 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.754 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.682 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.511 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.684 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.670 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.549 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL11]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[CD82]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LINC00973]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[IL1B]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LIF]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[POU2F2]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[NTNG2]] | +0.57 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CSF2]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[GPR68]] | +0.57 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[DPF3]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[BCL2A1]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[RDUR]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP1]] | -0.54 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[CLASP1]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PPP4R1]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ATL3]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[NCOA6]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[DUBR]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[MGP]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[PDLIM1]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[CHPT1]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[MGST1]] | -0.46 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL11]] | B | IL11 activity raises PINLYP's level | lines that do not express IL11 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without IL11 | 0.024 | ⚠ within organs, on part of the lines; also absent: EDNRA, LINC00973, LINC01583 |
| [[SPOCD1]] | B | SPOCD1 activity raises PINLYP's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without SPOCD1 | 0.076 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[ICAM1]] | C | ICAM1 activity raises PINLYP's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without ICAM1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC37A2]] | B | PINLYP activity raises SLC37A2's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without PINLYP | 0.038 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[FAM110A]] | B | PINLYP activity raises FAM110A's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.30× lower at baseline in the lines without PINLYP | 0.058 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[PRDM8]] | B | PINLYP activity weakens PRDM8's drug response | lines that do not express PINLYP (10) vs lines expressing it (21) | the lines without PINLYP respond 1.92× as strongly (z diff -1.83); strongest at Trametinib (DMSO_TF solvate) 5 µM: 0.30x vs 0.53x (z diff -2.8) | 0.069 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent; target measured in part of the lines; the reference differs |
| [[RAC2]] | B | PINLYP activity raises RAC2's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 2.01× lower at baseline in the lines without PINLYP | 0.088 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[NFKBIE]] | B | PINLYP activity raises NFKBIE's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.50× lower at baseline in the lines without PINLYP | 0.090 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[EVA1A]] | B | PINLYP activity raises EVA1A's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 3.10× lower at baseline in the lines without PINLYP | 0.093 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[DPF3]] | B | PINLYP activity raises DPF3's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without PINLYP | 0.0997 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[SPRED3]] | B | PINLYP activity raises SPRED3's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without PINLYP | 0.0997 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |
| [[ICAM1]] | C | PINLYP activity raises ICAM1's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 2.87× lower at baseline in the lines without PINLYP | 0.063 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.9, 0.8); signed map (16.6, 48.1). **Vector** length 47.6, 10.1% of its response variance represented; |z| ≥ 3 in 633 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.54 to 5); *inflammatory response* (hallmark, mean cos +0.52 to 6); *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +14.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.9 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +13.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.1 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +0.8 | +3.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +0.8 | +1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +0.8 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.7 | +1.8 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 inhibitor and LY6/PLAUR domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,575,801-43,583,964 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Matched by | ensembl_id |

UniProt [A6NC86](https://www.uniprot.org/uniprotkb/A6NC86) carries no function annotation.

**Summary**, from NCBI Gene [390940](https://www.ncbi.nlm.nih.gov/gene/390940):

> Predicted to enable phospholipase inhibitor activity. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:44206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44206) · Entrez [390940](https://www.ncbi.nlm.nih.gov/gene/390940) · UniProt [A6NC86](https://www.uniprot.org/uniprotkb/A6NC86) · Ensembl [ENSG00000234465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234465)

## Data

Gene col 13962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13962); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13962]; `tensor/DDL_lfc|DDL_z.npy` [13962]; `embed/gene_vectors.npy` [13962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13962 or target_col == 13962). Every well: [[PINLYP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PINLYP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
