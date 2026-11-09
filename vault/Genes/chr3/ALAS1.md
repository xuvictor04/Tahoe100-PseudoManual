---
symbol: "ALAS1"
type: "gene"
col: 344
ensembl_id: "ENSG00000023330"
name: "5'-aminolevulinate synthase 1"
location: "3p21.2"
module: 15
arm: "-"
pooled_cpm: 32.55
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ALAS1

*5'-aminolevulinate synthase 1* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.43× (z +24.9, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.671× (z -8.0, q 1e-12, down in 29 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.729× (z -6.3, q 7e-08, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAPIN]] (+0.66, fdr 4e-05), [[CREB3]] (+0.64, fdr 1e-05), [[MOCS2]] (+0.64, fdr 1e-05); moves opposite to [[GATD1-DT]] (-0.65, fdr 2e-05), [[NDUFAF6]] (-0.64, fdr 3e-05), [[WDR20]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPPK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +24.9 | 0e+00 | 44/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.28×** | +23.6 | 0e+00 | 48/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.21×** | +23.2 | 0e+00 | 46/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +15.6 | 0e+00 | 46/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +14.3 | 2e-44 | 46/48 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +12.9 | 7e-36 | 39/47 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +10.9 | 1e-25 | 38/47 (LOX-IMVI, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +10.1 | 6e-22 | 40/48 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +9.0 | 1e-17 | 30/48 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.51×** | +7.8 | 4e-13 | 24/37 (NCI-H1792, J82, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +7.1 | 8e-11 | 29/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +6.0 | 1e-07 | 26/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.8 | 3e-07 | 27/48 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +5.7 | 4e-07 | 22/47 (HEC-1-A, J82, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.7 | 4e-07 | 24/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +5.1 | 1e-05 | 23/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -8.0 | 1e-12 | 29/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.729×** | -6.3 | 7e-08 | 30/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.738×** | -6.1 | 3e-07 | 25/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.824×** | -3.9 | 0.014 | 19/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.4 | 0.068 | 16/47 (SNU-1, AsPC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.0 | 0.24 | 13/47 (SW 900, SNU-423, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 42.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.82× (z +23.8) | — |
| [[HOP62 (line)]] | alt | 18.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 39.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +16.2) | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 5 | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 24.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +17.2) | — |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 49.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +14.5) | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.4× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[J82 (line)]] | alt | 32.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +14.1) | — |
| [[LoVo (line)]] | wt | 35.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +19.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.3 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.06× (z +13.8) | — |
| [[Panc 03.27 (line)]] | alt | 37.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.8) | — |
| [[RPMI-7951 (line)]] | alt | 21.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.60× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 32.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +16.4) | — |
| [[SW480 (line)]] | alt | 47.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +14.2) | — |
| [[A-172 (line)]] | wt | 22.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +10.6) | — |
| [[A549 (line)]] | wt | 19.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +11.4) | — |
| [[C32 (line)]] | wt | 25.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 26.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.29× (z +14.3) | — |
| [[HT-29 (line)]] | alt | 31.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +14.9) | — |
| [[NCI-H2030 (line)]] | alt | 41.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.198× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 23.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 32.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.96× (z +10.3) | — |
| [[SW48 (line)]] | wt | 34.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 43.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 28.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.58× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 45.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +9.0) | — |
| [[KATO III (line)]] | alt | 58.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.72× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 41.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 25.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 24.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.55× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -14.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 25.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.24× (z +9.1) | — |
| [[A-427 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPIN]] | +0.66 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[CREB3]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MOCS2]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[RPAP3]] | +0.60 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ULBP3]] | +0.58 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[FIBP]] | +0.58 | +0.65 / +0.26 | both halves | 3e-04 |  |
| [[CSRP1]] | +0.58 | +0.57 / +0.40 | both halves | 4e-05 |  |
| [[EIF4A2]] | +0.57 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[ZNF510]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF184]] | +0.56 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[BCL10]] | +0.56 | +0.59 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATD1-DT]] | -0.65 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[NDUFAF6]] | -0.64 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[WDR20]] | -0.60 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NAF1]] | -0.60 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[LAMTOR5-AS1]] | -0.59 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TCTN3]] | -0.59 | -0.66 / -0.56 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[CRNDE]] | -0.58 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[NR2C2]] | -0.57 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MZT2A]] | -0.57 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[ZNF460-AS1]] | -0.57 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ANXA2R-OT1]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[LEMD3]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPPK1]] | B | EPPK1 activity raises ALAS1's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without EPPK1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.1, 20.9); signed map (-23.2, -20.1). **Vector** length 95.0, 22.6% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +14.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +24.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.9 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.5 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -7.2 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.6 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +1.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.1 | -1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | 5'-aminolevulinate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:52,198,086-52,214,327 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALAS-H; previously ALAS3, ALAS |
| Gene groups (HGNC) | 5'-aminolevulinate synthase family |
| Hallmark sets | UV_RESPONSE_UP, XENOBIOTIC_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins; Transcriptional activation of mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P13196](https://www.uniprot.org/uniprotkb/P13196) (5-aminolevulinate synthase, non-specific, mitochondrial):

> Catalyzes the pyridoxal 5'-phosphate (PLP)-dependent condensation of succinyl-CoA and glycine to form aminolevulinic acid (ALA), with CoA and CO2 as by-products.

**Summary**, from NCBI Gene [211](https://www.ncbi.nlm.nih.gov/gene/211):

> This gene encodes the mitochondrial enzyme which is catalyzes the rate-limiting step in heme (iron-protoporphyrin) biosynthesis. The enzyme encoded by this gene is the housekeeping enzyme; a separate gene encodes a form of the enzyme that is specific for erythroid tissue. The level of the mature encoded protein is regulated by heme: high levels of heme down-regulate the mature enzyme in mitochondria while low heme levels up-regulate. A pseudogene of this gene is located on chromosome 12. …

**Accessions** — [HGNC:396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:396) · Entrez [211](https://www.ncbi.nlm.nih.gov/gene/211) · UniProt [P13196](https://www.uniprot.org/uniprotkb/P13196) · Ensembl [ENSG00000023330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023330)

## Data

Gene col 344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 344); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 344]; `tensor/DDL_lfc|DDL_z.npy` [344]; `embed/gene_vectors.npy` [344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 344 or target_col == 344). Every well: [[ALAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
