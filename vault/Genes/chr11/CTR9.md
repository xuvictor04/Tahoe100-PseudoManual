---
symbol: "CTR9"
type: "gene"
col: 12658
ensembl_id: "ENSG00000198730"
name: "CTR9 component of Paf1/RNA polymerase II complex"
location: "11p15.4"
module: 126
arm: "+"
pooled_cpm: 90.95
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# CTR9

*CTR9 component of Paf1/RNA polymerase II complex* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.40× (z +16.5, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.76× (z +9.2, q 1e-17, up in 48 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.286×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADM]] (+0.73, fdr 7e-06), [[ZNF10]] (+0.67, fdr 1e-05), [[SUGP1]] (+0.67, fdr 7e-06); moves opposite to [[RCC2]] (-0.67, fdr 9e-06), [[PSME3]] (-0.66, fdr 1e-05), [[UBQLN4]] (-0.65, fdr 1e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARL4D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.40×** | +16.5 | 0e+00 | 46/48 (A498, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.76×** | +9.2 | 1e-17 | 48/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.95×** | +8.9 | 1e-16 | 45/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +8.6 | 8e-16 | 42/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.80×** | +7.8 | 6e-13 | 44/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.73×** | +7.3 | 2e-11 | 43/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.80×** | +7.2 | 5e-11 | 40/48 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.68×** | +6.9 | 3e-10 | 42/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.52×** | +6.4 | 9e-09 | 39/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.59×** | +6.2 | 3e-08 | 36/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.5 | 3e-04 | 33/47 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.3 | 9e-04 | 29/48 (HepG2/C3A, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.37×** | +4.2 | 0.001 | 31/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.008 | 26/48 (SNU-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.021 | 23/48 (HT-29, PANC-1, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.077 | 24/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.079 | 25/48 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.079 | 22/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C-33 A 0.286×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.8 | 8 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +17.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 74.9 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +20.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 140 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.13× (z +12.3) | — |
| [[SW480 (line)]] | alt | 119 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +19.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 96.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.59× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 96.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.64× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 112 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 137 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +20.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +10.5) | — |
| [[A498 (line)]] | wt | 81.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +23.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.27× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 81.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 74.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.28× (z +9.1) | — |
| [[RKO (line)]] | wt | 82.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +10.3) | — |
| [[C32 (line)]] | wt | 93.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 101 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.88× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 94.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 83.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +16.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 102 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +20.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 98.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.286× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 91.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 85.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.8) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 73.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HepG2_C3A (line)]] | wt | 74.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 68.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 153 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[RPMI-7951 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 55.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 82.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +17.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW48 (line)]] | wt | 79.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADM]] | +0.73 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ZNF10]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[SUGP1]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions |
| [[SAP18]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[NOSIP]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SNRPB2]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[SUMO4]] | +0.64 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[CNNM4]] | +0.64 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[BTG1]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[RLF]] | +0.63 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[RIOK3]] | +0.63 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[RNF113A]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCC2]] | -0.67 | -0.66 / -0.57 | both halves | 9e-06 |  |
| [[PSME3]] | -0.66 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[UBQLN4]] | -0.65 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[NUP188]] | -0.64 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[MACROH2A1]] | -0.64 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[CERS2]] | -0.63 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[TTF2]] | -0.63 | -0.54 / -0.58 | both halves | 1e-05 | STRING 750 |
| [[LIG3]] | -0.62 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[GMPS]] | -0.62 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[UBE2G2]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 | pathway: Protein ubiquitination |
| [[HCFC1]] | -0.62 | -0.57 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL4D]] | B | ARL4D activity raises CTR9's level | lines that do not express ARL4D (5) vs lines expressing it (45) | 1.29× lower at baseline in the lines without ARL4D | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, SOGA1, ELOVL5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction -0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-26.0, -28.6); signed map (-26.5, 13.2). **Vector** length 94.5, 31.3% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +0.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.9 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | -0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | CTR9 component of Paf1/RNA polymerase II complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:10,751,018-10,801,625 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0155, TSBP, p150TSP; previously SH2BP1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Paf1/RNA polymerase II complex |
| Reactome | 17 pathways, smallest: Dengue virus activates/modulates innate and adaptive immune responses; E3 ubiquitin ligases ubiquitinate target proteins; CHD1 and CHD2 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PD62](https://www.uniprot.org/uniprotkb/Q6PD62) (RNA polymerase-associated protein CTR9 homolog):

> Component of the PAF1 complex (PAF1C) which has multiple functions during transcription by RNA polymerase II and is implicated in regulation of development and maintenance of embryonic stem cell pluripotency. PAF1C associates with RNA polymerase II through interaction with POLR2A CTD non-phosphorylated and 'Ser-2'- and 'Ser-5'-phosphorylated forms and is involved in transcriptional elongation, acting both independently and synergistically with TCEA1 and in cooperation with the DSIF complex and …

**Summary**, from NCBI Gene [9646](https://www.ncbi.nlm.nih.gov/gene/9646):

> The protein encoded by this gene is a component of the PAF1 complex, which associates with RNA polymerase II and functions in transcriptional regulation and elongation. This complex also plays a role in the modification of histones. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:16850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16850) · Entrez [9646](https://www.ncbi.nlm.nih.gov/gene/9646) · UniProt [Q6PD62](https://www.uniprot.org/uniprotkb/Q6PD62) · Ensembl [ENSG00000198730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198730)

## Data

Gene col 12658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12658); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12658]; `tensor/DDL_lfc|DDL_z.npy` [12658]; `embed/gene_vectors.npy` [12658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12658 or target_col == 12658). Every well: [[CTR9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTR9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
