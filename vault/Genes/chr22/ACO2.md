---
symbol: "ACO2"
type: "gene"
col: 1953
ensembl_id: "ENSG00000100412"
name: "aconitase 2"
location: "22q13.2"
module: 210
arm: "+"
pooled_cpm: 59.46
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# ACO2

*aconitase 2* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.30× (z +20.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.698× (z -12.5, q 2e-33, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD8]] (+0.64, fdr 7e-06), [[VPS51]] (+0.63, fdr 7e-06), [[RTF2]] (+0.62, fdr 7e-06); moves opposite to [[UGCG]] (-0.59, fdr 1e-05), [[PPP2R2A]] (-0.54, fdr 3e-04), [[PIM3]] (-0.52, fdr 4e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.30×** | +20.4 | 0e+00 | 47/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.21×** | +18.4 | 0e+00 | 47/48 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.92×** | +16.0 | 0e+00 | 44/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +13.0 | 1e-36 | 37/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +10.5 | 9e-24 | 39/49 (NCI-H460, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +9.2 | 5e-18 | 38/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.60×** | +8.3 | 1e-14 | 39/49 (NCI-H1792, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +8.0 | 7e-14 | 27/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +7.5 | 4e-12 | 21/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +7.5 | 4e-12 | 29/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +6.9 | 3e-10 | 27/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.32×** | +6.9 | 3e-10 | 29/48 (LoVo, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.2 | 8e-06 | 19/35 (PANC-1, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.23×** | +5.1 | 1e-05 | 24/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.25×** | +5.1 | 2e-05 | 22/45 (HEC-1-A, PANC-1, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.008 | 15/48 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.018 | 12/48 (NCI-H2030, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.019 | 13/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.025 | 13/48 (SNU-423, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.049 | 12/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.698×** | -12.5 | 2e-33 | 45/48 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.727×** | -7.9 | 9e-13 | 39/48 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.5 | 0.002 | 19/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.901× | -3.7 | 0.034 | 11/48 (A498, KATO III, …) | top dose only | low cells (technical?) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.902× | -3.6 | 0.034 | 8/49 (AsPC-1, A498, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.039 | 12/49 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.868× | -3.5 | 0.039 | 15/48 (CHP-212, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 73.0 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +11.9) | — |
| [[LoVo (line)]] | wt | 65.3 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 51.4 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 74.6 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.72× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 51.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.16× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 56.0 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.56× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 41.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.26× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 58.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.19× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 87.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 157 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 52.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.1) | — |
| [[SW480 (line)]] | alt | 57.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.40× (z +12.9) | — |
| [[A549 (line)]] | wt | 40.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 47.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.63× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 82.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.20× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.92× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 65.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 94.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.590× (z -9.0) |
| [[A-172 (line)]] | wt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.3) | — |
| [[A498 (line)]] | wt | 69.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.91× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 49.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.56× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 66.0 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.207× (z -8.9) |
| [[H4 (line)]] | wt | 75.1 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.46× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 90.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 80.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 50.6 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 53.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +8.9) | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 37.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[A-427 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD8]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[VPS51]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[RTF2]] | +0.62 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[PSMC4]] | +0.61 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[LMAN2]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[DDX49]] | +0.60 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[NDUFA10]] | +0.60 | +0.47 / +0.66 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 747 |
| [[NUP214]] | +0.58 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TM9SF4]] | +0.58 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[LRRC41]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MFN2]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 649 |
| [[ACAD9]] | +0.57 | +0.38 / +0.61 | both halves | 6e-05 | pathway: Aerobic respiration and respiratory electron transport |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGCG]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[PPP2R2A]] | -0.54 | -0.28 / -0.62 | both halves | 3e-04 |  |
| [[PIM3]] | -0.52 | -0.40 / -0.54 | both halves | 4e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[MIER1]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PICALM]] | -0.49 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[ZNF706]] | -0.49 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[GPR37]] | -0.49 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[TIGD2]] | -0.47 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[ELOVL4]] | -0.47 | -0.32 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.5, -11.9); signed map (-31.9, -29.1). **Vector** length 106, 28.0% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.9 | +18.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.1 | +20.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +13.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +6.9 | +6.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.2 | -12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.7 | -7.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.7 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | aconitase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,447,830-41,529,273 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACONM |
| Gene groups (HGNC) | Aconitases |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Maturation of TCA enzymes and regulation of TCA cycle; Citric acid cycle (TCA cycle); Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99798](https://www.uniprot.org/uniprotkb/Q99798) (Aconitate hydratase, mitochondrial):

> Mitochondrial aconitate hydratase that converts citrate to isocitrate via cis-aconitate in the tricarboxylic (TCA) cycle. Mainly required to clear excess citrate; citrate accumulation activating the integrated stress response (ISR) and impairing cell fitness.

**Summary**, from NCBI Gene [50](https://www.ncbi.nlm.nih.gov/gene/50):

> The protein encoded by this gene belongs to the aconitase/IPM isomerase family. It is an enzyme that catalyzes the interconversion of citrate to isocitrate via cis-aconitate in the second step of the TCA cycle. This protein is encoded in the nucleus and functions in the mitochondrion. It was found to be one of the mitochondrial matrix proteins that are preferentially degraded by the serine protease 15(PRSS15), also known as Lon protease, after oxidative modification. [provided by RefSeq, Jul …

**Accessions** — [HGNC:118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:118) · Entrez [50](https://www.ncbi.nlm.nih.gov/gene/50) · UniProt [Q99798](https://www.uniprot.org/uniprotkb/Q99798) · Ensembl [ENSG00000100412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100412)

## Data

Gene col 1953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1953); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1953]; `tensor/DDL_lfc|DDL_z.npy` [1953]; `embed/gene_vectors.npy` [1953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1953 or target_col == 1953). Every well: [[ACO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
