---
symbol: "BAIAP2-DT"
type: "gene"
col: 13513
ensembl_id: "ENSG00000226137"
name: "BAIAP2 divergent transcript"
location: "17q25.3"
module: 28
arm: "-"
pooled_cpm: 4.86
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# BAIAP2-DT

*BAIAP2 divergent transcript* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.58× (z +10.2, q 9e-22, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.322× (z -12.8, q 6e-35, down in 31 of 39 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRD3OS]] (+0.62, fdr 2e-05), [[RPUSD1]] (+0.61, fdr 4e-05), [[ROGDI]] (+0.59, fdr 4e-05); moves opposite to [[RPAP2]] (-0.57, fdr 4e-05), [[DDX59]] (-0.55, fdr 2e-04), [[ZBTB8A]] (-0.54, fdr 4e-04).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC16A9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.58×** | +10.2 | 9e-22 | 42/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.89×** | +8.5 | 4e-15 | 39/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +8.3 | 2e-14 | 7/7 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +8.1 | 7e-14 | 16/20 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.63×** | +7.7 | 1e-12 | 33/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +5.4 | 5e-06 | 8/15 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +4.5 | 6e-04 | 16/38 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +3.3 | 0.066 | 11/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.066 | 15/42 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.076 | 11/41 (HEC-1-A, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.322×** | -12.8 | 6e-35 | 31/39 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.330×** | -8.9 | 2e-16 | 30/36 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -8.1 | 8e-14 | 33/46 (SW 900, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.397×** | -7.4 | 2e-11 | 31/44 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.408×** | -6.9 | 6e-10 | 27/41 (J82, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -5.9 | 4e-07 | 22/36 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.501×** | -5.5 | 2e-06 | 26/45 (LS 180, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.510×** | -5.4 | 5e-06 | 25/44 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.526×** | -5.1 | 2e-05 | 23/46 (H4, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.518×** | -5.0 | 4e-05 | 19/40 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.632×** | -3.7 | 0.012 | 22/46 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.641×** | -3.6 | 0.017 | 15/42 (A-427, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -3.5 | 0.019 | 18/35 (SW 900, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.649×** | -3.5 | 0.021 | 15/43 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.652×** | -3.4 | 0.023 | 19/46 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -3.4 | 0.028 | 14/37 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.541×** | -3.2 | 0.049 | 3/46 (NCI-H23, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 8.38 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.0472× (z -11.6) |
| [[SW480 (line)]] | alt | 4.73 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 7.39× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -10.0) |
| [[COLO 205 (line)]] | alt | 9.27 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0459× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 8.99 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -12.1) |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0815× (z -15.7) |
| [[J82 (line)]] | alt | 3.96 | 0 | 3 | — | [[Furosemide (drug)]] 0.05 µM 0.0343× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 6.33 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0452× (z -10.9) |
| [[PANC-1 (line)]] | alt | 4.81 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.29× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.8) |
| [[KATO III (line)]] | alt | 11.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 5.48 | 0 | 2 | — | [[Talc (drug)]] 0.05 µM 0.0512× (z -10.2) |
| [[LS 180 (line)]] | wt | 5.67 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -11.2) |
| [[SHP-77 (line)]] | alt | 6.92 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0612× (z -10.1) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0898× (z -9.0) |
| [[A-427 (line)]] | wt | 5.74 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0684× (z -9.2) |
| [[HOP62 (line)]] | alt | 7.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 4.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0632× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 8.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0544× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 5.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0993× (z -8.5) |
| [[A-172 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD3OS]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RPUSD1]] | +0.61 | +0.49 / +0.40 | both halves | 4e-05 |  |
| [[ROGDI]] | +0.59 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[CDK5]] | +0.58 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[USP9X]] | +0.57 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[LINC00205]] | +0.57 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[RAB5C]] | +0.55 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[ILRUN]] | +0.55 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[LRFN3]] | +0.54 | +0.48 / +0.23 | both halves | 5e-04 |  |
| [[HDAC1]] | +0.54 | +0.52 / +0.21 | both halves | 7e-04 |  |
| [[KCTD17]] | +0.54 | +0.45 / +0.22 | both halves | 6e-04 |  |
| [[BCKDK]] | +0.54 | +0.45 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP2]] | -0.57 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[DDX59]] | -0.55 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[ZBTB8A]] | -0.54 | -0.35 / -0.26 | both halves | 4e-04 |  |
| [[ZC3H8]] | -0.54 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[TAF15]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[KRBOX5]] | -0.54 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[RRP8]] | -0.52 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[CSTF3]] | -0.52 | -0.42 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[NDUFA6]] | -0.52 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[ANKRD18A]] | -0.51 | -0.31 / -0.29 | both halves | 3e-04 |  |
| [[CYP20A1]] | -0.51 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[PPP1R8]] | -0.51 | -0.48 / -0.24 | both halves | 4e-04 |  |
| [[MTG2]] | -0.50 | -0.37 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A9]] | B | SLC16A9 activity lowers BAIAP2-DT's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.37× higher at baseline in the lines without SLC16A9 | 0.020 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers BAIAP2-DT's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.290). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-2.0, 13.6); signed map (-52.3, -10.2). **Vector** length 67.9, 11.6% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -1.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | BAIAP2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q25.3 — chr17:81,029,130-81,034,881 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lnc-BAIAP2; previously BAIAP2-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44342](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44342) · Entrez [440465](https://www.ncbi.nlm.nih.gov/gene/440465) · Ensembl [ENSG00000226137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226137)

## Data

Gene col 13513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13513); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13513]; `tensor/DDL_lfc|DDL_z.npy` [13513]; `embed/gene_vectors.npy` [13513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13513 or target_col == 13513). Every well: [[BAIAP2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAIAP2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
