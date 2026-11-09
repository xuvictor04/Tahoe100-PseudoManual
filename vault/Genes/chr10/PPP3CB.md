---
symbol: "PPP3CB"
type: "gene"
col: 2876
ensembl_id: "ENSG00000107758"
name: "protein phosphatase 3 catalytic subunit beta"
location: "10q22.2"
module: 209
arm: "+"
pooled_cpm: 63.84
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# PPP3CB

*protein phosphatase 3 catalytic subunit beta* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 1.38× (z +6.3, q 2e-07, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.485× (z -14.2, q 6e-43, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSS51]] (+0.75, fdr 7e-06, ⚠ read-through risk), [[TECPR2]] (+0.67, fdr 7e-06), [[HGSNAT]] (+0.57, fdr 2e-05), [[DGUOK]] (+0.56, fdr 2e-05); moves opposite to [[HSPA1B]] (-0.54, fdr 3e-05), [[CYP39A1]] (-0.52, fdr 5e-05), [[MBNL2]] (-0.51, fdr 3e-05).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[SLC12A4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +6.3 | 2e-07 | 36/48 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.006 | 22/50 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.006 | 23/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.059 | 20/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.059 | 20/48 (HEC-1-A, SNU-423, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.4 | 0.063 | 15/48 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.14 | 18/48 (A498, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.14 | 13/49 (AsPC-1, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.0 | 0.16 | 18/43 (Panc 03.27, A549, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.485×** | -14.2 | 6e-43 | 42/48 (SW480, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.593×** | -10.3 | 3e-22 | 43/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.583×** | -10.1 | 1e-21 | 36/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -8.3 | 2e-14 | 40/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.658×** | -7.7 | 1e-12 | 40/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.690×** | -7.3 | 3e-11 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.691×** | -7.3 | 3e-11 | 34/48 (SW480, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.528×** | -6.5 | 4e-09 | 31/49 (H4, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.570×** | -5.8 | 5e-07 | 29/45 (NCI-H1792, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.583×** | -5.5 | 2e-06 | 36/47 (COLO 205, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.589×** | -5.4 | 3e-06 | 31/48 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.788×** | -4.7 | 1e-04 | 25/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.805×** | -4.2 | 1e-03 | 27/47 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.818×** | -3.9 | 0.003 | 20/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.017 | 15/49 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.5 | 0 | 11 (7 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.350× (z -12.4) |
| [[SW480 (line)]] | alt | 83.4 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.319× (z -16.5) |
| [[PANC-1 (line)]] | alt | 97.8 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.423× (z -10.7) |
| [[HOP62 (line)]] | alt | 105 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.292× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 79.7 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.162× (z -11.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 84.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.424× (z -9.4) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0716× (z -16.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 59.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.476× (z -8.6) |
| [[HT-29 (line)]] | alt | 60.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.282× (z -13.3) |
| [[J82 (line)]] | alt | 38.8 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.299× (z -10.6) |
| [[LoVo (line)]] | wt | 59.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.399× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 94.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.443× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.517× (z -8.5) |
| [[SNU-1 (line)]] | wt | 72.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A498 (line)]] | wt | 23.2 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.9) | — |
| [[A549 (line)]] | wt | 70.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 67.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.398× (z -8.8) |
| [[C-33 A (line)]] | alt | 86.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.365× (z -9.4) |
| [[C32 (line)]] | wt | 40.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.264× (z -9.6) |
| [[COLO 205 (line)]] | alt | 45.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 62.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.213× (z -11.6) |
| [[HCT15 (line)]] | alt | 84.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.399× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 71.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.351× (z -8.7) |
| [[Hs 766T (line)]] | wt | 59.0 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.311× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 76.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0781× (z -10.2) ⚠ toxic |
| [[KATO III (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.404× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 73.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.286× (z -13.2) |
| [[RKO (line)]] | wt | 91.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.404× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.363× (z -8.7) |
| [[SNU-423 (line)]] | alt | 101 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.405× (z -9.2) |
| [[SW 900 (line)]] | alt | 64.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.375× (z -9.1) |
| [[SW48 (line)]] | wt | 70.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSS51]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 | ⚠ **readthrough risk**: MSS51 lies 2.9 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[TECPR2]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[HGSNAT]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[DGUOK]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PHF20L1]] | +0.55 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[PCNX4]] | +0.54 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[H6PD]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[LRCH3]] | +0.52 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[R3HDM2]] | +0.52 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[ACTR3B]] | +0.52 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[TADA3]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[PIGL]] | +0.50 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[LINC00467]] | +0.50 | +0.58 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA1B]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[CYP39A1]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MBNL2]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[TSKU]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[RAB39A]] | -0.50 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[OTX1]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ANKMY2]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[HSPB1]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[PSMA6]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 | pathway: Beta-catenin independent WNT signaling |
| [[BTN3A2]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PIK3C2B]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[SNX3]] | -0.48 | -0.54 / -0.39 | both halves | 5e-05 | pathway: Signaling by WNT |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPP3CB's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC12A4]] | C | PPP3CB's natural level strengthens SLC12A4's drug response | PPP3CB's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.16; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[GMEB1]] | C | PPP3CB's natural level strengthens GMEB1's drug response | PPP3CB's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.27; direction not clear | 0.083 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.181). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.5, 0.4); signed map (13.0, 0.1). **Vector** length 93.7, 23.5% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.3 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.1 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -14.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.0 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -10.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.2 | -7.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -8.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 3 catalytic subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,436,433-73,496,024 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CALNA2, CNA2, PP2Bbeta; previously CALNB |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits; Calcineurin subunits |
| Reactome | 22 pathways, smallest: ROBO receptors bind AKAP5; Calcineurin activates NFAT; CLEC7A (Dectin-1) induces NFAT activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P16298](https://www.uniprot.org/uniprotkb/P16298) (Serine/threonine-protein phosphatase 2B catalytic subunit beta isoform):

> Calcium-dependent, calmodulin-stimulated protein phosphatase which plays an essential role in the transduction of intracellular Ca(2+)-mediated signals. Dephosphorylates TFEB in response to lysosomal Ca(2+) release, resulting in TFEB nuclear translocation and stimulation of lysosomal biogenesis. Dephosphorylates and activates transcription factor NFATC1. Dephosphorylates and inactivates transcription factor ELK1. Dephosphorylates DARPP32. Negatively regulates MAP3K14/NIK signaling via …

**Summary**, from NCBI Gene [5532](https://www.ncbi.nlm.nih.gov/gene/5532):

> Enables several functions, including calmodulin binding activity; calmodulin-dependent protein phosphatase activity; and protein phosphatase 2B binding activity. Involved in several processes, including calcineurin-NFAT signaling cascade; positive regulation of lysosome organization; and positive regulation of protein localization to nucleus. Located in cytosol. Part of calcineurin complex. Implicated in aortic valve stenosis. Biomarker of focal segmental glomerulosclerosis and schizophrenia. …

**Accessions** — [HGNC:9315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9315) · Entrez [5532](https://www.ncbi.nlm.nih.gov/gene/5532) · UniProt [P16298](https://www.uniprot.org/uniprotkb/P16298) · Ensembl [ENSG00000107758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107758)

## Data

Gene col 2876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2876); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2876]; `tensor/DDL_lfc|DDL_z.npy` [2876]; `embed/gene_vectors.npy` [2876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2876 or target_col == 2876). Every well: [[PPP3CB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP3CB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
