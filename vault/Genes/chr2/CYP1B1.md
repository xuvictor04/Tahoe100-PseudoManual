---
symbol: "CYP1B1"
type: "gene"
col: 6115
ensembl_id: "ENSG00000138061"
name: "cytochrome P450 family 1 subfamily B member 1"
location: "2p22.2"
module: 19
arm: "+"
pooled_cpm: 93.14
n_lines_expressing: 21
n_dd_up: 42
n_dd_down: 1
n_dd_up_clean: 30
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 11
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CYP1B1

*cytochrome P450 family 1 subfamily B member 1* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.98× (z +11.0, q 1e-25, up in 14 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Gemcitabine (drug)]] 0.05 µM: 2.07× (z +6.7, q 4e-09, up in 19 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.431× (z -5.8, q 3e-06, down in 15 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (SW 900 0.0541×, NCI-H460 0.109×; ⚠ cell-cycle shift, explains ~71% of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (SW 900 0.0475×, NCI-H460 0.155×; ⚠ cell-cycle shift, explains ~37% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SW 900 0.0785×, NCI-H460 0.114×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW 900 0.196×, NCI-H460 0.239×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.132×, SW 900 0.195×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMDN2-AS1]] (+0.78, fdr 7e-06, ⚠ read-through risk), [[CYP1B1-AS1]] (+0.74, fdr 7e-06, ⚠ same locus), [[NOVA1]] (+0.67, fdr 7e-06), [[BCL3]] (+0.65, fdr 7e-06), [[IL6]] (+0.63, fdr 1e-05); moves opposite to [[NBPF15]] (-0.47, fdr 5e-05), [[GPR89A]] (-0.46, fdr 4e-05), [[ZNF749]] (-0.46, fdr 5e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[RMDN2-AS1]] → it (grade B ⚠); 11 go from it, the strongest it → [[CYP1B1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.98×** | +11.0 | 1e-25 | 14/19 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +7.9 | 6e-13 | 10/15 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +7.2 | 9e-11 | 11/16 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Gemcitabine (drug)]] 0.05 µM |  | **2.07×** | +6.7 | 4e-09 | 19/19 (A498, CFPAC-1, …) | all doses, flat |  |
| [[AZD-7648 (drug)]] 5 µM |  | **6.48×** | +6.4 | 2e-08 | 17/18 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Menadione (drug)]] 5 µM |  | **2.44×** | +5.9 | 4e-07 | 18/18 (A498, PANC-1, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 5 µM |  | **2.90×** | +5.1 | 2e-05 | 17/19 (A498, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **4.50×** | +5.1 | 2e-05 | 15/17 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +5.1 | 2e-05 | 16/19 (PANC-1, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.9 | 4e-05 | 6/20 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.62×** | +4.7 | 1e-04 | 11/19 (HS-578T, NCI-H23, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.01×** | +4.6 | 2e-04 | 13/19 (PANC-1, HS-578T, …) | top dose only | composition shift |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.85×** | +4.2 | 0.001 | 16/19 (A498, NCI-H1792, …) | top dose only |  |
| [[LY2090314 (drug)]] 0.05 µM |  | **1.88×** | +4.1 | 0.002 | 18/19 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.1 | 0.002 | 12/18 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Anastrozole (drug)]] 5 µM |  | **3.07×** | +3.8 | 0.005 | 17/19 (A498, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **3.22×** | +3.8 | 0.005 | 14/19 (A498, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Resveratrol (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.005 | 19/20 (A498, NCI-H1792, …) | top dose only |  |
| [[DT-061 (drug)]] 5 µM |  | **2.99×** | +3.7 | 0.006 | 15/18 (A498, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | **1.77×** | +3.7 | 0.006 | 17/19 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **2.22×** | +3.7 | 0.007 | 13/19 (CFPAC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **2.96×** | +3.5 | 0.011 | 11/19 (PANC-1, NCI-H23, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 5 µM |  | **1.67×** | +3.5 | 0.011 | 10/19 (A498, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6115.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (SW 900 0.0541×, NCI-H460 0.109×; ⚠ cell-cycle shift, explains ~71% of this change); [[Bortezomib (drug)]] 0.05 µM in 2 lines (SW 900 0.0475×, NCI-H460 0.155×; ⚠ cell-cycle shift, explains ~37% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SW 900 0.0785×, NCI-H460 0.114×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW 900 0.196×, NCI-H460 0.239×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.132×, SW 900 0.195×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.431×** | -5.8 | 3e-06 | 15/19 (SW 900, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.700× | -3.5 | 0.13 | 14/19 (NCI-H1792, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.639× | -3.1 | 0.30 | 9/18 (HT-29, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.646× | -3.0 | 0.30 | 7/19 (NCI-H1792, A498, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 1,364 | 0 | 9 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0541× (z -16.4) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0785× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 698 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.109× (z -11.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.114× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 179 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 30.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +13.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[PANC-1 (line)]] | alt | 82.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 41.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +16.5) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[A498 (line)]] | wt | 51.7 | 1 | 0 | [[Menadione (drug)]] 5 µM 6.76× (z +8.9) | — |
| [[H4 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +12.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[LoVo (line)]] | wt | 32.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +8.8) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H2030 (line)]] | alt | 288 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.70× (z +8.5) ⚠ position not correctable | — |
| [[A-172 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.73 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.29 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 22.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.91 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.51 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMDN2-AS1]] | +0.78 | +0.84 / +0.73 | both halves | 7e-06 | ⚠ **readthrough risk**: RMDN2-AS1 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[CYP1B1-AS1]] | +0.74 | +0.72 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NOVA1]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[BCL3]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[IL6]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 | STRING 448 |
| [[KYNU]] | +0.62 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[AHR]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 | pathway: Biological oxidations; STRING 763 |
| [[CFH]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[NR3C1]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TCIM]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[LINC02015]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[PLD1]] | +0.58 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[EBF1]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PDE7B]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF15]] | -0.47 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[GPR89A]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ZNF749]] | -0.46 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[FXYD5]] | -0.46 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[TPD52L2]] | -0.45 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RMDN2-AS1]] | B | RMDN2-AS1 activity raises CYP1B1's level | lines that do not express RMDN2-AS1 (14) vs lines expressing it (36) | 4.12× lower at baseline in the lines without RMDN2-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: EHD3, PLOD2, ZNF43; maybe low, not absent |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises CYP1B1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 3.77× lower at baseline in the lines without CYP1B1-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[STEAP1B-AS1]] | C | STEAP1B-AS1 activity raises CYP1B1's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 3.77× lower at baseline in the lines without STEAP1B-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[NOVA1]] | C | NOVA1 activity raises CYP1B1's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 4.13× lower at baseline in the lines without NOVA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[IL6]] | C | IL6 activity raises CYP1B1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 3.80× lower at baseline in the lines without IL6 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[TYMP]] | C | TYMP activity raises CYP1B1's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without TYMP | 0.086 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20; co-absent with the target |
| [[EBF1]] | C | EBF1 activity raises CYP1B1's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.87× lower at baseline in the lines without EBF1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[EYA4]] | C | EYA4 activity raises CYP1B1's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 3.38× lower at baseline in the lines without EYA4 | 0.099 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1-AS1]] | B | CYP1B1 activity raises CYP1B1-AS1's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 3.42× lower at baseline in the lines without CYP1B1 | 4e-05 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[RMDN2-AS1]] | B | CYP1B1 activity raises RMDN2-AS1's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without CYP1B1 | 0.001 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[SYNPO]] | B | CYP1B1 activity raises SYNPO's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without CYP1B1 | 0.025 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[NCOA7]] | B | CYP1B1 activity raises NCOA7's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 1.56× lower at baseline in the lines without CYP1B1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[CFAP300]] | B | CYP1B1 activity raises CFAP300's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without CYP1B1 | 0.060 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[DPYD]] | B | CYP1B1 activity strengthens DPYD's drug response | lines that do not express CYP1B1 (19) vs lines expressing it (18) | the lines without CYP1B1 respond 0.79× as strongly (z diff +1.21); strongest at Bortezomib 0.05 µM: 0.68x vs 0.46x (z diff +2.9) | 0.063 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849; target measured in part of the lines; artifact flags |
| [[AHR]] | B | CYP1B1 activity raises AHR's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without CYP1B1 | 0.081 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[DPYD]] | B | CYP1B1 activity raises DPYD's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.67× lower at baseline in the lines without CYP1B1 | 0.097 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[EYA4]] | C | CYP1B1 activity raises EYA4's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 3.48× lower at baseline in the lines without CYP1B1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849; co-absent with the target |
| [[NTN4]] | C | CYP1B1 activity raises NTN4's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 3.78× lower at baseline in the lines without CYP1B1 | 0.043 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849; co-absent with the target |
| [[BASP1]] | C | CYP1B1 activity raises BASP1's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 4.25× lower at baseline in the lines without CYP1B1 | 0.087 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.446). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.4, 23.0); signed map (48.5, 24.2). **Vector** length 71.4, 21.4% of its response variance represented; |z| ≥ 3 in 709 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.1 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -2.9 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.5 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -2.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.4 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 1 subfamily B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:38,066,973-38,109,902 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CP1B; previously GLC3A |
| Gene groups (HGNC) | Cytochrome P450 family 1; Hydroperoxy icosatetraenoate dehydratases |
| Reactome | 10 pathways, smallest: Synthesis of epoxy (EET) and dihydroxyeicosatrienoic acids (DHET); Endogenous sterols; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16678](https://www.uniprot.org/uniprotkb/Q16678) (Cytochrome P450 1B1):

> A cytochrome P450 monooxygenase involved in the metabolism of various endogenous substrates, including fatty acids, steroid hormones and vitamins. Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (NADPH--hemoprotein reductase). Exhibits catalytic activity for the formation of hydroxyestrogens from estrone (E1) and 17beta-estradiol (E2), namely 2- …

**Summary**, from NCBI Gene [1545](https://www.ncbi.nlm.nih.gov/gene/1545):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. The enzyme encoded by this gene localizes to the endoplasmic reticulum and metabolizes procarcinogens such as polycyclic aromatic hydrocarbons and 17beta-estradiol. Mutations in this gene have been associated with primary congenital glaucoma; therefore it is …

**Accessions** — [HGNC:2597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2597) · Entrez [1545](https://www.ncbi.nlm.nih.gov/gene/1545) · UniProt [Q16678](https://www.uniprot.org/uniprotkb/Q16678) · Ensembl [ENSG00000138061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138061)

## Data

Gene col 6115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6115); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6115]; `tensor/DDL_lfc|DDL_z.npy` [6115]; `embed/gene_vectors.npy` [6115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6115 or target_col == 6115). Every well: [[CYP1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
