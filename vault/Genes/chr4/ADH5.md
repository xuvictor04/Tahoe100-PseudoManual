---
symbol: "ADH5"
type: "gene"
col: 12484
ensembl_id: "ENSG00000197894"
name: "alcohol dehydrogenase 5 (class III), chi polypeptide"
location: "4q23"
module: 17
arm: "+"
pooled_cpm: 37.67
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ADH5

*alcohol dehydrogenase 5 (class III), chi polypeptide* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.77× (z +9.1, q 4e-17, up in 24 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.33× (z +6.7, q 3e-09, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 3.23×, A549 3.65×, PANC-1 2.45×, A-172 2.41×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.20×, SW480 2.96×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.490× (z -16.8, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNPDA2]] (+0.72, fdr 7e-06), [[MRS2]] (+0.72, fdr 7e-06), [[DLAT]] (+0.67, fdr 1e-05); moves opposite to [[CATSPERG]] (-0.60, fdr 1e-05), [[PKNOX1]] (-0.60, fdr 2e-05), [[HIVEP1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12484.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 3.23×, A549 3.65×, PANC-1 2.45×, A-172 2.41×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 3.20×, SW480 2.96×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +9.1 | 4e-17 | 24/39 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +7.8 | 2e-12 | 2/48 (AsPC-1, AN3 CA) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +7.7 | 2e-12 | 31/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +6.7 | 3e-09 | 33/48 (AsPC-1, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.004 | 19/46 (LOX-IMVI, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.490×** | -16.8 | 0e+00 | 43/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -14.2 | 4e-43 | 42/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.477×** | -12.3 | 2e-32 | 42/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -8.2 | 2e-14 | 39/48 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.609×** | -8.2 | 2e-14 | 32/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.621×** | -7.9 | 3e-13 | 36/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.744×** | -4.9 | 8e-05 | 24/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.772×** | -4.3 | 0.001 | 21/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.633×** | -4.0 | 0.005 | 20/48 (KATO III, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.006 | 22/48 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.799×** | -3.7 | 0.010 | 20/48 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -3.5 | 0.021 | 21/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.810×** | -3.4 | 0.033 | 23/48 (AN3 CA, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.058 | 14/48 (RPMI-7951, HCT15, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.077 | 7/47 (SW480, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.831×** | -3.1 | 0.077 | 12/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -22.3) |
| [[SW480 (line)]] | alt | 26.2 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.365× (z -10.1) |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 39.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.2) |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -15.0) |
| [[A498 (line)]] | wt | 71.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 39.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -10.4) |
| [[HT-29 (line)]] | alt | 35.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -14.9) |
| [[J82 (line)]] | alt | 39.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -10.3) |
| [[LoVo (line)]] | wt | 25.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.0) |
| [[LS 180 (line)]] | wt | 51.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 37.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 55.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -15.6) |
| [[PANC-1 (line)]] | alt | 34.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.3) |
| [[RKO (line)]] | wt | 47.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -15.0) |
| [[A-172 (line)]] | wt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 54.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.9) |
| [[C32 (line)]] | wt | 37.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -12.5) |
| [[H4 (line)]] | wt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -9.7) |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.8) |
| [[Hs 766T (line)]] | wt | 33.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -11.6) |
| [[KATO III (line)]] | alt | 27.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 45.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 46.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.6) |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 31.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.282× (z -9.2) |
| [[SW 1088 (line)]] | alt | 61.9 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.0695× (z -9.0) |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.4) |
| [[A-427 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNPDA2]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[MRS2]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DLAT]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PLRG1]] | +0.66 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[NDUFA12]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[THYN1]] | +0.65 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[DNAJC19]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[HSD17B4]] | +0.64 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[WDR11]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[BBS5]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[VTA1]] | +0.63 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SAAL1]] | +0.62 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERG]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.60 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[HIVEP1]] | -0.59 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[RFX1]] | -0.57 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[PSMD6-AS2]] | -0.57 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ERF]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.56 | -0.60 / -0.39 | both halves | 6e-05 |  |
| [[ANKRD17-DT]] | -0.55 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[SATB2]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[EOLA2-DT]] | -0.54 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[ZFTRAF1]] | -0.54 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[KIF27]] | -0.53 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-7.0, -10.9); signed map (-31.2, -14.8). **Vector** length 89.4, 20.2% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.4 | +6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | -1.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.1 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.9 | -14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -16.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.0 | -7.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.6 | -0.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.8 | -0.7 |
|  | [[Resveratrol (drug)]] 0.5 µM |  | -1.7 | -0.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | alcohol dehydrogenase 5 (class III), chi polypeptide |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:99,070,978-99,088,801 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADH-3, ADHX, GSNOR; previously FDH |
| Gene groups (HGNC) | Alcohol dehydrogenases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 3 pathways, smallest: Ethanol oxidation; Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P11766](https://www.uniprot.org/uniprotkb/P11766) (Alcohol dehydrogenase class-3):

> Catalyzes the oxidation of long-chain primary alcohols and the oxidation of S-(hydroxymethyl) glutathione. Also oxidizes long chain omega-hydroxy fatty acids, such as 20-HETE, producing both the intermediate aldehyde, 20-oxoarachidonate and the end product, a dicarboxylic acid, (5Z,8Z,11Z,14Z)-eicosatetraenedioate. Class-III ADH is remarkably ineffective in oxidizing ethanol. Required for clearance of cellular formaldehyde, a cytotoxic and carcinogenic metabolite that induces DNA damage. Also …

**Summary**, from NCBI Gene [128](https://www.ncbi.nlm.nih.gov/gene/128):

> This gene encodes a member of the alcohol dehydrogenase family. Members of this family metabolize a wide variety of substrates, including ethanol, retinol, other aliphatic alcohols, hydroxysteroids, and lipid peroxidation products. The encoded protein forms a homodimer. It has virtually no activity for ethanol oxidation, but exhibits high activity for oxidation of long-chain primary alcohols and for oxidation of S-hydroxymethyl-glutathione, a spontaneous adduct between formaldehyde and …

**Accessions** — [HGNC:253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:253) · Entrez [128](https://www.ncbi.nlm.nih.gov/gene/128) · UniProt [P11766](https://www.uniprot.org/uniprotkb/P11766) · Ensembl [ENSG00000197894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197894)

## Data

Gene col 12484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12484); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12484]; `tensor/DDL_lfc|DDL_z.npy` [12484]; `embed/gene_vectors.npy` [12484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12484 or target_col == 12484). Every well: [[ADH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
