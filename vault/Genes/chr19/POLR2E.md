---
symbol: "POLR2E"
type: "gene"
col: 1817
ensembl_id: "ENSG00000099817"
name: "RNA polymerase II, I and III subunit E"
location: "19p13.3"
module: 15
arm: "-"
pooled_cpm: 33.94
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# POLR2E

*RNA polymerase II, I and III subunit E* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.10× (z +14.6, q 3e-45, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.52× (z +5.4, q 5e-06, up in 39 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGOLN2]] (+0.63, fdr 3e-05), [[G6PD]] (+0.63, fdr 1e-05), [[ENO1]] (+0.59, fdr 3e-05); moves opposite to [[PPP1R26-AS1]] (-0.58, fdr 3e-05), [[CARNMT1-AS1]] (-0.55, fdr 2e-04), [[CCZ1P1]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 19 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.10×** | +14.6 | 3e-45 | 45/45 (A-427, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.30×** | +14.1 | 1e-42 | 39/39 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.33×** | +10.9 | 2e-25 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.42×** | +10.5 | 8e-24 | 35/42 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.26×** | +10.5 | 1e-23 | 46/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.12×** | +9.7 | 4e-20 | 46/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 5e-06 | 39/47 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 2e-05 | 30/47 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.45×** | +4.8 | 1e-04 | 30/48 (NCI-H1792, NCI-H460, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.43×** | +4.6 | 3e-04 | 30/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.29×** | +4.6 | 3e-04 | 25/48 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.42×** | +4.5 | 4e-04 | 27/46 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.42×** | +4.5 | 4e-04 | 30/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.45×** | +4.4 | 4e-04 | 30/48 (NCI-H1792, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.4 | 4e-04 | 25/47 (HS-578T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.2 | 8e-04 | 28/48 (LoVo, SW480, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.080 | 10/48 (NCI-H1792, A498, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 36.2 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 36.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 26.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.24× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 32.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 44.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A498 (line)]] | wt | 36.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HOP62 (line)]] | alt | 21.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 31.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LS 180 (line)]] | wt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.60× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 22.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-423 (line)]] | alt | 30.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[Hs 766T (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[J82 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LOX-IMVI (line)]] | wt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1573 (line)]] | alt | 27.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Panc 03.27 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RKO (line)]] | wt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RPMI-7951 (line)]] | alt | 29.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 35.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SNU-1 (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW 900 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW1417 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGOLN2]] | +0.63 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[G6PD]] | +0.63 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ENO1]] | +0.59 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[CD151]] | +0.59 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[GALNT2]] | +0.57 | +0.37 / +0.48 | both halves | 7e-05 |  |
| [[USP9X]] | +0.56 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[ECHS1]] | +0.55 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[ALDOA]] | +0.55 | +0.23 / +0.40 | both halves | 5e-04 |  |
| [[VCL]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PPP1CA]] | +0.54 | +0.48 / +0.44 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 854 |
| [[GPS1]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 | pathway: Formation of TC-NER Pre-Incision Complex; STRING 663 |
| [[CAPZB]] | +0.53 | +0.23 / +0.38 | both halves | 5e-04 | pathway: Affinity selection of immunoglobulins |

## Genes that move opposite

*55 of its nearest partners move opposite, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R26-AS1]] | -0.58 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CARNMT1-AS1]] | -0.55 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[CCZ1P1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[MIR762HG]] | -0.55 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[RNF135]] | -0.55 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[EIF3J-DT]] | -0.54 | -0.16 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[ACTG1P17]] | -0.54 | -0.20 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[PGLS-DT]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ZNF528-AS1]] | -0.54 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[RWDD3]] | -0.53 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[TAF1D]] | -0.53 | -0.46 / -0.37 | both halves | 7e-05 | pathway: B-WICH complex positively regulates rRNA expression; STRING 590 |
| [[STARD7-AS1]] | -0.53 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[ZNF330]] | -0.53 | -0.22 / -0.42 | both halves | 6e-04 |  |
| [[ZNF785]] | -0.52 | -0.28 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.1, 22.8); signed map (-12.4, 33.3). **Vector** length 51.8, 9.48% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.7 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.7 | +10.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.6 | +9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +1.7 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +1.6 | +14.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | -0.4 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +1.2 | +1.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.2 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.1 | -0.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.3 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.3 | +4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II, I and III subunit E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,086,574-1,095,380 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPB5, RPABC1, XAP4, hRPB25, hsRPB5 |
| Gene groups (HGNC) | RNA polymerase subunits; PAQosome accessory subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 94 pathways, smallest: RNA Polymerase III Chain Elongation; Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P19388](https://www.uniprot.org/uniprotkb/P19388) (DNA-directed RNA polymerases I, II, and III subunit RPABC1):

> DNA-dependent RNA polymerase catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. Common component of RNA polymerases I, II and III which synthesize ribosomal RNA precursors, mRNA precursors and many functional non-coding RNAs, and small RNAs, such as 5S rRNA and tRNAs, respectively. Pol II is the central component of the basal RNA polymerase II transcription machinery. Pols are composed of mobile elements that move relative to each other. In …

**Summary**, from NCBI Gene [5434](https://www.ncbi.nlm.nih.gov/gene/5434):

> This gene encodes the fifth largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. This subunit is shared by the other two DNA-directed RNA polymerases and is present in two-fold molar excess over the other polymerase subunits. An interaction between this subunit and a hepatitis virus transactivating protein has been demonstrated, suggesting that interaction between transcriptional activators and the polymerase can occur through this …

**Accessions** — [HGNC:9192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9192) · Entrez [5434](https://www.ncbi.nlm.nih.gov/gene/5434) · UniProt [P19388](https://www.uniprot.org/uniprotkb/P19388) · Ensembl [ENSG00000099817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099817)

## Data

Gene col 1817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1817); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1817]; `tensor/DDL_lfc|DDL_z.npy` [1817]; `embed/gene_vectors.npy` [1817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1817 or target_col == 1817). Every well: [[POLR2E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
