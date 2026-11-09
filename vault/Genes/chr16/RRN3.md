---
symbol: "RRN3"
type: "gene"
col: 1437
ensembl_id: "ENSG00000085721"
name: "RNA polymerase I transcription factor RRN3"
location: "16p13.11"
module: 7
arm: "+"
pooled_cpm: 38.51
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 4
n_dd_up_clean: 26
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RRN3

*RNA polymerase I transcription factor RRN3* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (14 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 11.2× (z +25.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.784× (z -4.8, q 6e-04, down in 19 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 0.5 µM: 0.826× (z -3.9, q 0.014, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.324×, Hs 766T 0.286×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.335×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.156×); [[Orlistat (drug)]] 0.05 µM in 1 line (BT-474 0.290×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX28]] (+0.73, fdr 7e-06), [[REXO4]] (+0.72, fdr 7e-06), [[PES1]] (+0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RALGPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **11.2×** | +25.7 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +21.8 | 0e+00 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **5.85×** | +18.7 | 0e+00 | 46/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +17.1 | 0e+00 | 42/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +12.4 | 5e-33 | 41/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +11.7 | 2e-29 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +10.0 | 8e-22 | 36/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +8.1 | 4e-14 | 33/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +7.8 | 4e-13 | 37/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.46×** | +7.6 | 1e-12 | 37/48 (SW480, AsPC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +7.6 | 2e-12 | 35/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.45×** | +7.5 | 4e-12 | 29/48 (SW480, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.3 | 1e-11 | 24/48 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +7.2 | 3e-11 | 32/48 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +6.8 | 4e-10 | 29/47 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +5.4 | 2e-06 | 17/48 (SNU-423, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 1e-05 | 19/48 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.8 | 5e-05 | 23/48 (A-172, SW480, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.7 | 7e-05 | 20/48 (SW480, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1437.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.324×, Hs 766T 0.286×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.335×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.156×); [[Orlistat (drug)]] 0.05 µM in 1 line (BT-474 0.290×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.784×** | -4.8 | 6e-04 | 19/39 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.793×** | -4.7 | 6e-04 | 17/46 (NCI-H2030, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.816×** | -4.2 | 0.006 | 18/48 (RKO, HEC-1-A, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.826×** | -3.9 | 0.014 | 15/47 (NCI-H23, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.837× | -3.6 | 0.032 | 11/48 (NCI-H23, AN3 CA, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.837× | -3.5 | 0.044 | 18/47 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.896× | -3.2 | 0.11 | 13/48 (RKO, AsPC-1, …) | two highest doses |  |
| [[Afatinib (drug)]] 5 µM |  | 0.857× | -3.0 | 0.16 | 11/48 (NCI-H23, C-33 A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 34.6 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.2× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 29.0 | 6 | 0 | [[TAK-901 (drug)]] 5 µM 19.2× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 36.9 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 13.2× (z +11.0) | [[Orlistat (drug)]] 0.05 µM 0.290× (z -9.3) |
| [[HOP62 (line)]] | alt | 22.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.7) | — |
| [[KATO III (line)]] | alt | 39.1 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 14.8× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 65.2 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 8.90× (z +15.0) | — |
| [[SW1417 (line)]] | alt | 49.7 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 9.50× (z +11.3) | — |
| [[A-427 (line)]] | wt | 40.4 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A549 (line)]] | wt | 43.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 45.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 40.5 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.19× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 30.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.8× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -8.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 34.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.64× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 31.6 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 16.9× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 28.3 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 13.4× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 46.4 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 28.3 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +11.5) | — |
| [[SW480 (line)]] | alt | 41.3 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 14.5× (z +17.5) | — |
| [[A-172 (line)]] | wt | 32.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.8) | — |
| [[A498 (line)]] | wt | 48.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.3) | — |
| [[C-33 A (line)]] | alt | 72.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.4× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.6× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 24.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 58.1× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 23.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 18.1× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 48.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.30× (z +9.7) | — |
| [[RKO (line)]] | wt | 70.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.1× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 59.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.156× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 55.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.00× (z +8.8) | — |
| [[J82 (line)]] | alt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.74× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 25.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.4× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 55.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.96× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 52.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 19.1× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX28]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[REXO4]] | +0.72 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[PES1]] | +0.72 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[ZNF777]] | +0.72 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[KTI12]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[NOL8]] | +0.70 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[SURF6]] | +0.69 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.69 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[PHAX]] | +0.67 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[ZNF691]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGPS2]] | B | RALGPS2 activity lowers RRN3's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.42× higher at baseline in the lines without RALGPS2 | 0.033 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-40.8, 0.8); signed map (-2.6, -22.5). **Vector** length 82.2, 19.3% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +25.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +17.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +18.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +10.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +4.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +3.0 | +2.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.7 | +7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | -4.5 | +4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.3 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.6 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I transcription factor RRN3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,060,033-15,094,311 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp566E104, TIF-IA |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 3 pathways, smallest: RNA Polymerase I Promoter Escape; RNA Polymerase I Transcription Initiation; RNA Polymerase I Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYV6](https://www.uniprot.org/uniprotkb/Q9NYV6) (RNA polymerase I-specific transcription initiation factor RRN3):

> Required for efficient transcription initiation by RNA polymerase I (Pol I). Required for the formation of the competent pre-initiation complex (PIC).

**Summary**, from NCBI Gene [54700](https://www.ncbi.nlm.nih.gov/gene/54700):

> Enables RNA polymerase I core promoter sequence-specific DNA binding activity and RNA polymerase I general transcription initiation factor activity. Involved in transcription initiation at RNA polymerase I promoter. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30346](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30346) · Entrez [54700](https://www.ncbi.nlm.nih.gov/gene/54700) · UniProt [Q9NYV6](https://www.uniprot.org/uniprotkb/Q9NYV6) · Ensembl [ENSG00000085721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085721)

## Data

Gene col 1437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1437); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1437]; `tensor/DDL_lfc|DDL_z.npy` [1437]; `embed/gene_vectors.npy` [1437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1437 or target_col == 1437). Every well: [[RRN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
