---
symbol: "ENPEP"
type: "gene"
col: 6240
ensembl_id: "ENSG00000138792"
name: "glutamyl aminopeptidase"
location: "4q25"
module: 19
arm: "+"
pooled_cpm: 5.93
n_lines_expressing: 25
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ENPEP

*glutamyl aminopeptidase* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.99× (z +13.6, q 1e-39, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +11.0, q 1e-25, up in 5 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.560× (z -5.9, q 2e-06, down in 14 of 21 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.660× (z -4.2, q 0.003, down in 12 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 12 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 4 lines (HCT15 0.00897×, NCI-H1792 0.0183×, COLO 205 0.0539×, hTERT-HPNE 0.210×; ⚠ cell-cycle shift, explains ~27% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (NCI-H460 0.177×, HT-29 0.0820×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0481×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.110×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXPH1]] (+0.71, fdr 1e-05), [[GAS2]] (+0.64, fdr 1e-05), [[WDR72]] (+0.61, fdr 1e-05); moves opposite to [[TNK2]] (-0.52, fdr 3e-04), [[EHD4]] (-0.51, fdr 3e-04), [[GNAI2]] (-0.51, fdr 7e-04, ⚠ not reproduced), [[EHBP1L1]] (-0.51, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[FLNB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.99×** | +13.6 | 1e-39 | 2/7 (A498, NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +11.0 | 1e-25 | 5/17 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.68×** | +10.1 | 9e-22 | 2/12 (NCI-H2347, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +8.9 | 5e-17 | 1/8 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.6 | 5e-09 | 8/21 (A498, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.9 | 3e-07 | 7/20 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +5.5 | 3e-06 | 10/21 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.1 | 2e-05 | 6/16 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +4.7 | 2e-04 | 5/19 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +4.5 | 4e-04 | 10/21 (A498, HT-29, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +4.5 | 4e-04 | 8/18 (NCI-H460, HCT15, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.4 | 5e-04 | 4/16 (SW480, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 8e-04 | 3/20 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 0.001 | 10/20 (LS 180, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.002 | 7/20 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.015 | 4/21 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM |  | **1.34×** | +3.0 | 0.081 | 0/20 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6240.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 12 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 4 lines (HCT15 0.00897×, NCI-H1792 0.0183×, COLO 205 0.0539×, hTERT-HPNE 0.210×; ⚠ cell-cycle shift, explains ~27% of this change); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (NCI-H460 0.177×, HT-29 0.0820×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0481×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.560×** | -5.9 | 2e-06 | 14/21 (HCT15, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.618×** | -4.9 | 3e-04 | 14/20 (COLO 205, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.631×** | -4.7 | 5e-04 | 15/21 (hTERT-HPNE, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -4.2 | 0.003 | 12/20 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.692×** | -3.8 | 0.019 | 13/21 (COLO 205, HCT15, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.694×** | -3.7 | 0.019 | 13/20 (NCI-H460, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.700×** | -3.6 | 0.022 | 14/22 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.718×** | -3.2 | 0.086 | 7/20 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.739× | -3.1 | 0.13 | 10/21 (HT-29, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.810× | -3.0 | 0.14 | 7/20 (HT-29, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0481× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.177× (z -8.8) |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0539× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.110× (z -8.6) |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.00897× (z -18.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 5.52 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0820× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0183× (z -16.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.991 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.876 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXPH1]] | +0.71 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[GAS2]] | +0.64 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[WDR72]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CASC9]] | +0.60 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TARID]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.59 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[LINC01508]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[GUCY1B2]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ATP8B4]] | +0.57 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[ASB4]] | +0.57 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[TPRG1]] | +0.57 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[ZBED5-AS1]] | +0.56 | +0.48 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNK2]] | -0.52 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[EHD4]] | -0.51 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[GNAI2]] | -0.51 | -0.40 / -0.20 | ⚠ not reproduced | 7e-04 |  |
| [[FLNB]] | -0.51 | -0.51 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[EHBP1L1]] | -0.51 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[LMBR1]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[HDAC11]] | -0.50 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[CTNNBIP1]] | -0.49 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[SH2B2]] | -0.49 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[TSPAN9]] | -0.49 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[EIF4EBP1]] | -0.49 | -0.45 / -0.21 | both halves | 6e-04 |  |
| [[INPP5F]] | -0.49 | -0.45 / -0.21 | both halves | 6e-04 |  |
| [[CORO7]] | -0.49 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[PKD1]] | -0.48 | -0.39 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ENPEP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NXPH1]] | B | NXPH1 activity strengthens ENPEP's drug response | lines that do not express NXPH1 (7) vs lines expressing it (15) | the lines without NXPH1 respond 1.13× as strongly (z diff +0.17); strongest at Belinostat 5 µM: 0.56x vs 0.18x (z diff +4.4) | 0.045 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[LYPLAL1-DT]] | B | LYPLAL1-DT activity raises ENPEP's level | lines that do not express LYPLAL1-DT (32) vs lines expressing it (18) | 1.59× lower at baseline in the lines without LYPLAL1-DT | 0.057 | ⚠ within organs, on part of the lines; also absent: EBF1, ANXA10, IRF4; maybe low, not absent |
| [[KCNMB2]] | B | KCNMB2 activity raises ENPEP's level | lines that do not express KCNMB2 (18) vs lines expressing it (32) | 2.17× lower at baseline in the lines without KCNMB2 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01980, LINC02398, LINC02306; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ENPEP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDE1A]] | C | PDE1A activity raises ENPEP's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.37× lower at baseline in the lines without PDE1A | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[LINC01967]] | C | LINC01967 activity raises ENPEP's level | lines that do not express LINC01967 (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without LINC01967 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1; co-absent with the target |
| [[LINC00824]] | C | LINC00824 activity raises ENPEP's level | lines that do not express LINC00824 (46) vs lines expressing it (4) | 3.91× lower at baseline in the lines without LINC00824 | 0.072 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SUCNR1, ENSG00000289530; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLNB]] | B | ENPEP activity lowers FLNB's level | lines that do not express ENPEP (25) vs lines expressing it (25) | 1.77× higher at baseline in the lines without ENPEP | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02253, KCNE3, ENSG00000265554; maybe low, not absent |
| [[KCNMB2]] | B | ENPEP activity raises KCNMB2's level | lines that do not express ENPEP (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without ENPEP | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02253, KCNE3, ENSG00000265554; maybe low, not absent |
| [[KCNMB2-AS1]] | B | ENPEP activity raises KCNMB2-AS1's level | lines that do not express ENPEP (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without ENPEP | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02253, KCNE3, ENSG00000265554; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.3, 42.8); signed map (46.5, 42.5). **Vector** length 47.7, 10.6% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +11.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.1 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.5 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.4 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.3 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -0.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | glutamyl aminopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:110,365,733-110,565,285 (+) |
| Ensembl biotype | protein_coding |
| Also known as | gp160, CD249 |
| Gene groups (HGNC) | Aminopeptidases; CD molecules; M1 metallopeptidases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Metabolism of Angiotensinogen to Angiotensins; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07075](https://www.uniprot.org/uniprotkb/Q07075) (Glutamyl aminopeptidase):

> Regulates central hypertension through its calcium-modulated preference to cleave N-terminal acidic residues from peptides such as angiotensin II.

**Summary**, from NCBI Gene [2028](https://www.ncbi.nlm.nih.gov/gene/2028):

> The ENPEP gene encodes glutamyl aminopeptidase, a type II integral membrane protein with an extracellular zinc-binding domain. This protein can upregulate blood pressure by cleaving the N-terminal aspartate from angiotensin II, and can regulate blood vessel formation and enhance tumorigenesis in some tissues. Along with ANPEP and DPP4, ENPEP was found to be a candidate co-receptor for the coronavirus SARS-CoV-2, which causes COVID-19. [provided by RefSeq, Apr 2020]

**Accessions** — [HGNC:3355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3355) · Entrez [2028](https://www.ncbi.nlm.nih.gov/gene/2028) · UniProt [Q07075](https://www.uniprot.org/uniprotkb/Q07075) · Ensembl [ENSG00000138792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138792)

## Data

Gene col 6240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6240); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6240]; `tensor/DDL_lfc|DDL_z.npy` [6240]; `embed/gene_vectors.npy` [6240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6240 or target_col == 6240). Every well: [[ENPEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENPEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
