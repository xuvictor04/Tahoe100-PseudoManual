---
symbol: "SMG1P2"
type: "gene"
col: 12985
ensembl_id: "ENSG00000205534"
name: "SMG1 pseudogene 2"
location: "16p11.2"
module: 77
arm: "+"
pooled_cpm: 33.52
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# SMG1P2

*SMG1 pseudogene 2* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +8.9, q 3e-16, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.396× (z -11.4, q 3e-27, down in 39 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.640× (z -5.5, q 6e-06, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GFOD2]] (+0.67, fdr 7e-06), [[SMG1P5]] (+0.64, fdr 7e-06), [[TPST2]] (+0.62, fdr 1e-05); moves opposite to [[C11orf58]] (-0.70, fdr 7e-06), [[CHURC1]] (-0.70, fdr 7e-06), [[OCIAD1]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 077]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +8.9 | 3e-16 | 42/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +8.3 | 3e-14 | 39/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +7.7 | 4e-12 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +6.9 | 7e-10 | 40/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +6.3 | 4e-08 | 32/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.29×** | +5.9 | 4e-07 | 36/48 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +5.4 | 4e-06 | 35/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +5.1 | 2e-05 | 34/48 (NCI-H460, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.9 | 6e-05 | 27/47 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +4.2 | 0.001 | 26/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.025 | 14/48 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.025 | 22/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.4 | 0.025 | 21/47 (NCI-H460, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.025 | 16/48 (KATO III, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +3.2 | 0.055 | 17/49 (AsPC-1, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12985.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.396×** | -11.4 | 3e-27 | 39/45 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.400×** | -10.8 | 9e-25 | 30/36 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.566×** | -6.5 | 2e-08 | 24/40 (LoVo, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -5.5 | 6e-06 | 29/48 (A-427, A-172, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.696×** | -4.5 | 9e-04 | 22/46 (HepG2/C3A, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.742×** | -3.7 | 0.020 | 24/48 (HT-29, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.743×** | -3.7 | 0.020 | 24/47 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.050 | 22/48 (A-427, HS-578T, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.840× | -3.1 | 0.13 | 19/48 (KATO III, Hs 766T, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.638× | -3.1 | 0.13 | 14/48 (A549, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.3 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.82× (z +10.7) | — |
| [[A-427 (line)]] | wt | 29.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.246× (z -9.4) |
| [[A498 (line)]] | wt | 44.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 39.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0933× (z -17.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 92.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0564× (z -16.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 32.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 23.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0674× (z -17.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0952× (z -12.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.170× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -9.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -10.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +8.6) | — |
| [[LoVo (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -10.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.307× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -11.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.1000× (z -14.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFOD2]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SMG1P5]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TPST2]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NT5DC3]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[TAF5L]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[BUD23]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MED26]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[GRB2]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ST6GALNAC4]] | +0.60 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[SPTLC2]] | +0.60 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[FARP2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GARNL3]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | -0.70 | -0.69 / -0.59 | both halves | 7e-06 |  |
| [[CHURC1]] | -0.70 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[OCIAD1]] | -0.70 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[RC3H2]] | -0.67 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[CLK4]] | -0.66 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.66 | -0.71 / -0.60 | both halves | 7e-06 |  |
| [[FAM200A]] | -0.64 | -0.71 / -0.50 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.63 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[PHC3]] | -0.63 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[TIA1]] | -0.63 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.62 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-27.1, 7.8); signed map (-47.3, 23.5). **Vector** length 96.0, 25.7% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | -0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Auranofin (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -8.8 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.2 | +0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | SMG1 pseudogene 2 |
| Locus type | pseudogene |
| Location | 16p11.2 — chr16:29,527,568-29,594,966 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49859) · Entrez [440354](https://www.ncbi.nlm.nih.gov/gene/440354) · Ensembl [ENSG00000205534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205534)

## Data

Gene col 12985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12985); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12985]; `tensor/DDL_lfc|DDL_z.npy` [12985]; `embed/gene_vectors.npy` [12985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12985 or target_col == 12985). Every well: [[SMG1P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG1P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
