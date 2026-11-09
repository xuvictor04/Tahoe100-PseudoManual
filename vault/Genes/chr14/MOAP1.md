---
symbol: "MOAP1"
type: "gene"
col: 9213
ensembl_id: "ENSG00000165943"
name: "modulator of apoptosis 1"
location: "14q32.12"
module: 0
arm: null
pooled_cpm: 11.78
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene"]
generated_by: "tahoemap"
---

# MOAP1

*modulator of apoptosis 1* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (18 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.77× (z +14.2, q 3e-43, up in 34 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.60× (z +13.9, q 1e-41, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 0.05 µM: 0.832× (z -3.6, q 0.070, down in 10 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS37B]] (+0.54, fdr 2e-05), [[SFT2D1]] (+0.53, fdr 2e-05), [[RAB3B]] (+0.52, fdr 1e-05); moves opposite to [[SRRM1]] (-0.49, fdr 5e-05), [[LRRC37A2]] (-0.48, fdr 4e-05), [[SMC6]] (-0.41, fdr 2e-04).
> Its neighbourhood forms no module of 5 or more genes (module 0, unassigned).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.77×** | +14.2 | 3e-43 | 34/39 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.60×** | +13.9 | 1e-41 | 44/47 (HEC-1-A, SK-MEL-2, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +10.0 | 3e-21 | 25/33 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +9.5 | 3e-19 | 30/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.72×** | +7.9 | 3e-13 | 26/38 (MIA PaCa-2, C32, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.69×** | +7.7 | 1e-12 | 30/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +7.7 | 1e-12 | 31/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.62×** | +6.8 | 1e-09 | 10/22 (HEC-1-A, SW 900, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.50×** | +5.9 | 2e-07 | 20/46 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.50×** | +5.9 | 2e-07 | 20/45 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +5.8 | 4e-07 | 24/45 (A498, LS 180, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.41×** | +5.0 | 3e-05 | 18/47 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 9e-05 | 14/47 (KATO III, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.36×** | +4.5 | 2e-04 | 14/47 (SK-MEL-2, SW480, …) | rises with dose | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +4.2 | 8e-04 | 14/47 (BT-474, C-33 A, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.003 | 11/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.049 | 5/46 (A498, SW1417, …) | inconsistent across doses | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.068 | 2/47 (NCI-H460, NCI-H2030) | top dose only | plate-row cell shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.31×** | +2.9 | 0.090 | 5/44 (J82, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +2.8 | 0.090 | 8/46 (HCT15, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +2.8 | 0.096 | 3/42 (AsPC-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.05 µM |  | **0.832×** | -3.6 | 0.070 | 10/47 (NCI-H460, RKO, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.774×** | -3.5 | 0.070 | 10/47 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.820×** | -3.4 | 0.070 | 9/48 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.782×** | -3.4 | 0.070 | 14/45 (NCI-H460, NCI-H2347, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.070 | 12/48 (NCI-H460, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.844× | -3.3 | 0.070 | 13/47 (NCI-H460, HOP62, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.070 | 10/47 (AsPC-1, J82, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.794×** | -3.3 | 0.070 | 9/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.2 | 5 (5 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.05× (z +10.0) ⚠ cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.251× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 11.7 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.54× (z +10.3) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.79× (z +10.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.65× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.80× (z +10.4) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 2.94× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.199× (z -8.7) |
| [[C-33 A (line)]] | alt | 7.48 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0716× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 15.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.05× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.102× (z -10.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.69× (z +9.2) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.643× (z -9.5) ⚠ position not correctable |
| [[RKO (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.64× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.210× (z -8.6) |
| [[SW480 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.90× (z +8.6) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37B]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SFT2D1]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RAB3B]] | +0.52 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ITM2C]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[GPR137B]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[ANO7]] | +0.49 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[WDR26]] | +0.48 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[SDAD1P1]] | +0.47 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[SGIP1]] | +0.47 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[GABRE]] | +0.47 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[PLAC4]] | +0.47 | +0.36 / +0.53 | both halves | 9e-05 |  |
| [[LINC-PINT]] | +0.46 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRM1]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[LRRC37A2]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SMC6]] | -0.41 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[DHX29]] | -0.41 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[ARMC8]] | -0.41 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[HMGXB4]] | -0.41 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[SHPRH]] | -0.41 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[BAZ1B]] | -0.40 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[TADA2A]] | -0.40 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[CEP63]] | -0.40 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[LARP1B]] | -0.40 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[SUCLG1]] | -0.40 | -0.43 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MOAP1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises MOAP1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: none (module 0: its neighbourhood formed no community of ≥ 5 genes).
- **Nodal map** (x, y) = (23.7, 20.1); signed map (0.4, 27.3). **Vector** length 78.9, 14.7% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.4 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +13.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +14.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -0.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | modulator of apoptosis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:93,182,199-93,184,923 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAP-1, PNMA4 |
| Gene groups (HGNC) | Paraneoplastic Ma antigens |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BY2](https://www.uniprot.org/uniprotkb/Q96BY2) (Modulator of apoptosis 1):

> Retrotransposon-derived protein that forms virion-like capsids (By similarity). Acts as an effector of BAX during apoptosis: enriched at outer mitochondria membrane and associates with BAX upon induction of apoptosis, facilitating BAX-dependent mitochondrial outer membrane permeabilization and apoptosis. Required for death receptor-dependent apoptosis. When associated with RASSF1, promotes BAX conformational change and translocation to mitochondrial membranes in response to TNF and TNFSF10 …

**Summary**, from NCBI Gene [64112](https://www.ncbi.nlm.nih.gov/gene/64112):

> The protein encoded by this gene was identified by its interaction with apoptosis regulator BAX protein. This protein contains a Bcl-2 homology 3 (BH3)-like motif, which is required for the association with BAX. When overexpressed, this gene has been shown to mediate caspase-dependent apoptosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16658) · Entrez [64112](https://www.ncbi.nlm.nih.gov/gene/64112) · UniProt [Q96BY2](https://www.uniprot.org/uniprotkb/Q96BY2) · Ensembl [ENSG00000165943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165943)

## Data

Gene col 9213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9213); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9213]; `tensor/DDL_lfc|DDL_z.npy` [9213]; `embed/gene_vectors.npy` [9213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9213 or target_col == 9213). Every well: [[MOAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
