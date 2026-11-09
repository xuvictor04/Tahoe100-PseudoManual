---
symbol: "INPPL1"
type: "gene"
col: 9123
ensembl_id: "ENSG00000165458"
name: "inositol polyphosphate phosphatase like 1"
location: "11q13.4"
module: 126
arm: "+"
pooled_cpm: 26.84
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# INPPL1

*inositol polyphosphate phosphatase like 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.83× (z +8.3, q 5e-14, up in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +6.5, q 1e-08, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 3.59×, J82 3.35×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.313× (z -16.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAN2A2]] (+0.70, fdr 1e-05), [[LDB1]] (+0.70, fdr 1e-05), [[ATN1]] (+0.69, fdr 7e-06); moves opposite to [[SMIM30]] (-0.56, fdr 3e-05), [[PIBF1]] (-0.54, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9123.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 3.59×, J82 3.35×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +8.3 | 5e-14 | 25/35 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +7.6 | 1e-11 | 32/43 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.5 | 1e-08 | 31/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.6 | 0.040 | 18/46 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.28× | +3.3 | 0.12 | 18/39 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.313×** | -16.6 | 0e+00 | 47/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.333×** | -15.7 | 0e+00 | 47/48 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.375×** | -14.0 | 3e-42 | 45/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.655×** | -8.5 | 2e-15 | 31/47 (AsPC-1, COLO 205, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -8.2 | 3e-14 | 32/47 (COLO 205, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.609×** | -7.1 | 1e-10 | 32/47 (hTERT-HPNE, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -6.7 | 1e-09 | 31/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.687×** | -5.4 | 6e-06 | 26/47 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.703×** | -5.0 | 3e-05 | 24/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -4.7 | 1e-04 | 25/48 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.731×** | -4.5 | 4e-04 | 22/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.551×** | -4.4 | 4e-04 | 27/48 (CFPAC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.559×** | -4.3 | 6e-04 | 23/48 (SK-MEL-2, NCI-H661, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.745×** | -4.0 | 0.002 | 21/47 (COLO 205, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.765×** | -3.8 | 0.005 | 23/48 (A-427, SW1417, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.744×** | -3.7 | 0.007 | 14/48 (C-33 A, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.613×** | -3.7 | 0.008 | 15/47 (Hs 766T, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.010 | 19/47 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.803×** | -3.1 | 0.049 | 14/48 (SHP-77, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 27.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.171× (z -11.6) |
| [[J82 (line)]] | alt | 37.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 18.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.251× (z -10.3) |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -11.4) |
| [[SW480 (line)]] | alt | 22.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -15.0) |
| [[KATO III (line)]] | alt | 22.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 42.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -12.1) |
| [[SW 900 (line)]] | alt | 29.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.227× (z -9.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.259× (z -8.9) |
| [[A-427 (line)]] | wt | 48.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.325× (z -9.5) |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 32.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.382× (z -8.8) |
| [[HOP62 (line)]] | alt | 17.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.280× (z -9.0) |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -11.2) |
| [[LoVo (line)]] | wt | 24.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 28.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.400× (z -8.5) |
| [[RKO (line)]] | wt | 32.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -11.1) |
| [[SW48 (line)]] | wt | 25.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -10.1) |
| [[A-172 (line)]] | wt | 45.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.4) |
| [[A549 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 54.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -13.8) |
| [[HCT15 (line)]] | alt | 42.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -8.5) |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -8.5) |
| [[LS 180 (line)]] | wt | 20.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -11.4) |
| [[A498 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAN2A2]] | +0.70 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[LDB1]] | +0.70 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ATN1]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[MTA2]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[DVL3]] | +0.67 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[SEPTIN8]] | +0.67 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[FBRS]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.66 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SORBS3]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 491 |
| [[STRN4]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[NCSTN]] | +0.64 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[VPS52]] | +0.64 | +0.28 / +0.56 | both halves | 3e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM30]] | -0.56 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PIBF1]] | -0.54 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.1, -22.6); signed map (-11.4, -34.7). **Vector** length 98.4, 24.6% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +1.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -15.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -14.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | -16.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -6.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate phosphatase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,223,701-72,239,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SHIP2 |
| Gene groups (HGNC) | SH2 domain containing; Sterile alpha motif domain containing; Phosphoinositide phosphatases |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 12 pathways, smallest: Interleukin receptor SHC signaling; Synthesis of IP3 and IP4 in the cytosol; Signaling by CSF1 (M-CSF) in myeloid cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O15357](https://www.uniprot.org/uniprotkb/O15357) (Phosphatidylinositol 3,4,5-trisphosphate 5-phosphatase 2):

> Phosphatidylinositol (PtdIns) phosphatase that specifically hydrolyzes the 5-phosphate of phosphatidylinositol-3,4,5-trisphosphate (PtdIns(3,4,5)P3) to produce PtdIns(3,4)P2, thereby negatively regulating the PI3K (phosphoinositide 3-kinase) pathways. Required for correct mitotic spindle orientation and therefore progression of mitosis (By similarity). Plays a central role in regulation of PI3K-dependent insulin signaling, although the precise molecular mechanisms and signaling pathways remain …

**Summary**, from NCBI Gene [3636](https://www.ncbi.nlm.nih.gov/gene/3636):

> The protein encoded by this gene is an SH2-containing 5'-inositol phosphatase that is involved in the regulation of insulin function. The encoded protein also plays a role in the regulation of epidermal growth factor receptor turnover and actin remodelling. Additionally, this gene supports metastatic growth in breast cancer and is a valuable biomarker for breast cancer. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:6080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6080) · Entrez [3636](https://www.ncbi.nlm.nih.gov/gene/3636) · UniProt [O15357](https://www.uniprot.org/uniprotkb/O15357) · Ensembl [ENSG00000165458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165458)

## Data

Gene col 9123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9123); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9123]; `tensor/DDL_lfc|DDL_z.npy` [9123]; `embed/gene_vectors.npy` [9123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9123 or target_col == 9123). Every well: [[INPPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INPPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
