---
symbol: "ALMS1"
type: "gene"
col: 3762
ensembl_id: "ENSG00000116127"
name: "ALMS1 centrosome and basal body associated protein"
location: "2p13.1"
module: 6
arm: "+"
pooled_cpm: 95.53
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ALMS1

*ALMS1 centrosome and basal body associated protein* — 2p13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.585× (z -8.6, q 7e-15, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.625× (z -7.5, q 1e-11, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XRCC5]] (+0.60, fdr 9e-06), [[COPS3]] (+0.60, fdr 2e-05), [[SMC1A]] (+0.59, fdr 2e-05); moves opposite to [[KBTBD3]] (-0.54, fdr 1e-05), [[IL17RE]] (-0.53, fdr 2e-05), [[MITD1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC171]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.3 | 0.58 | 13/48 (NCI-H460, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -8.6 | 7e-15 | 42/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.698×** | -8.1 | 1e-13 | 30/48 (NCI-H1792, HS-578T, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.625×** | -7.5 | 1e-11 | 33/48 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -5.8 | 8e-07 | 33/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.721×** | -5.2 | 2e-05 | 27/48 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.735×** | -4.7 | 2e-04 | 30/47 (C-33 A, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -4.6 | 4e-04 | 24/49 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.742×** | -4.4 | 8e-04 | 25/45 (C-33 A, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.767×** | -4.2 | 0.001 | 27/48 (NCI-H1573, SW 1088, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.832×** | -4.1 | 0.002 | 23/49 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -4.1 | 0.002 | 26/48 (C32, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.769×** | -4.0 | 0.003 | 28/47 (C-33 A, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -3.9 | 0.005 | 29/49 (SW 1088, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.665×** | -3.4 | 0.027 | 25/47 (A549, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.039 | 21/49 (HepG2/C3A, A-172, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.042 | 22/48 (KATO III, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.821×** | -3.1 | 0.055 | 23/48 (LOX-IMVI, SNU-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.873× | -3.1 | 0.070 | 15/48 (HepG2/C3A, AsPC-1, …) | all doses, flat |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.703×** | -2.9 | 0.090 | 20/48 (AsPC-1, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 217 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0499× (z -31.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 97.5 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.378× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.419× (z -9.5) |
| [[C32 (line)]] | wt | 145 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -14.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 153 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.412× (z -10.2) |
| [[HS-578T (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -18.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 75.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -11.0) |
| [[LoVo (line)]] | wt | 89.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.454× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -19.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 78.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.9) |
| [[A-427 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.467× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 76.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -9.6) |
| [[A549 (line)]] | wt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -9.3) |
| [[AN3 CA (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[CHP-212 (line)]] | wt | 68.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[HepG2_C3A (line)]] | wt | 82.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.321× (z -9.6) |
| [[HOP62 (line)]] | alt | 94.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -9.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[J82 (line)]] | alt | 91.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H23 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -9.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H460 (line)]] | wt | 126 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.341× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 74.2 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.132× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -13.4) |
| [[SNU-423 (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW48 (line)]] | wt | 94.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 86.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC5]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[COPS3]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[SMC1A]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[MCM7]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PRKDC]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MCM3]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MCM4]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[XRCC3]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MTOR]] | +0.56 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[NCAPH2]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[VRK1]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RANBP1]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[IL17RE]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[MITD1]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[SNHG8]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[MRPL33]] | -0.51 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[NDUFB4]] | -0.50 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[SAT2]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZFAND2A-DT]] | -0.50 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[HOTAIRM1]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[PKD1L2]] | -0.49 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC171]] | C | CCDC171 activity raises ALMS1's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without CCDC171 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.3, -41.9); signed map (-35.9, -47.7). **Vector** length 106, 29.9% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.9 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +1.9 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Larotrectinib (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.6 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -6.0 | -8.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ALMS1 centrosome and basal body associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:73,385,758-73,625,166 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0328 |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCU4](https://www.uniprot.org/uniprotkb/Q8TCU4) (Centrosome-associated protein ALMS1):

> Involved in PCM1-dependent intracellular transport. Required, directly or indirectly, for the localization of NCAPD2 to the proximal ends of centrioles. Required for proper formation and/or maintenance of primary cilia (PC), microtubule-based structures that protrude from the surface of epithelial cells.

**Summary**, from NCBI Gene [7840](https://www.ncbi.nlm.nih.gov/gene/7840):

> This gene encodes a protein containing a large tandem-repeat domain as well as additional low complexity regions. The encoded protein functions in microtubule organization, particularly in the formation and maintanance of cilia. Mutations in this gene cause Alstrom syndrome. There is a pseudogene for this gene located adjacent in the same region of chromosome 2. Alternative splice variants have been described but their full length nature has not been determined. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:428) · Entrez [7840](https://www.ncbi.nlm.nih.gov/gene/7840) · UniProt [Q8TCU4](https://www.uniprot.org/uniprotkb/Q8TCU4) · Ensembl [ENSG00000116127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116127)

## Data

Gene col 3762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3762); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3762]; `tensor/DDL_lfc|DDL_z.npy` [3762]; `embed/gene_vectors.npy` [3762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3762 or target_col == 3762). Every well: [[ALMS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALMS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
