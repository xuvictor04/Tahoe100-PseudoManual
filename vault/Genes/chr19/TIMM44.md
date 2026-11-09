---
symbol: "TIMM44"
type: "gene"
col: 2537
ensembl_id: "ENSG00000104980"
name: "translocase of inner mitochondrial membrane 44"
location: "19p13.2"
module: 133
arm: "+"
pooled_cpm: 32.32
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# TIMM44

*translocase of inner mitochondrial membrane 44* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +12.0, q 1e-30, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.708× (z -4.6, q 0.003, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.0709×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.210×; ⚠ cell-cycle shift, explains ~18% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTO1]] (+0.67, fdr 7e-06), [[N4BP2L2]] (+0.61, fdr 2e-05), [[ATF4]] (+0.60, fdr 3e-05); moves opposite to [[ITM2C]] (-0.59, fdr 1e-05), [[PKM]] (-0.59, fdr 1e-05), [[HSBP1]] (-0.54, fdr 2e-05).
> It is in [[Module 133]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +12.0 | 1e-30 | 45/47 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +11.3 | 3e-27 | 45/47 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +9.1 | 3e-17 | 43/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.7 | 2e-12 | 36/45 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +7.6 | 4e-12 | 38/47 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.4 | 2e-11 | 38/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +7.0 | 2e-10 | 41/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.9 | 3e-10 | 26/38 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +6.4 | 1e-08 | 41/47 (SNU-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +6.2 | 3e-08 | 40/46 (SW 900, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.30×** | +5.7 | 6e-07 | 38/48 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +5.7 | 6e-07 | 27/43 (HS-578T, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.3 | 4e-06 | 31/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.50×** | +5.1 | 1e-05 | 31/48 (AsPC-1, A-172, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 2e-05 | 33/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[EX229 (drug)]] 5 µM |  | **1.94×** | +4.5 | 2e-04 | 31/47 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +4.4 | 3e-04 | 27/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.81×** | +4.1 | 0.001 | 32/47 (NCI-H2030, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.81×** | +4.1 | 0.001 | 30/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.001 | 28/48 (SW48, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.74×** | +3.8 | 0.004 | 25/47 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.009 | 23/48 (LoVo, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.011 | 19/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2537.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.0709×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.210×; ⚠ cell-cycle shift, explains ~18% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.708×** | -4.6 | 0.003 | 23/48 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -4.3 | 0.005 | 28/48 (A498, COLO 205, …) | rises with dose |  |
| [[Folic acid (drug)]] 5 µM |  | 0.846× | -3.1 | 0.33 | 17/48 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.850× | -3.0 | 0.33 | 20/48 (SNU-423, CHP-212, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +10.8) | — |
| [[LoVo (line)]] | wt | 37.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 24.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.4) | — |
| [[A-427 (line)]] | wt | 49.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.4) | — |
| [[H4 (line)]] | wt | 45.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.66× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 43.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0709× (z -16.2) |
| [[HOP62 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.7) | — |
| [[J82 (line)]] | alt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -9.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW 900 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.5) | — |
| [[A498 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTO1]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[N4BP2L2]] | +0.61 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[ATF4]] | +0.60 | +0.79 / +0.46 | both halves | 3e-05 |  |
| [[DNAJC2]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[YARS1]] | +0.60 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[CEBPG]] | +0.59 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[LMO4]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[EIF2S2]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[SLC3A2]] | +0.57 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[FNBP4]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ADM2]] | +0.56 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CPT1B]] | +0.55 | +0.62 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2C]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[PKM]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[HSBP1]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MED14]] | -0.52 | -0.63 / -0.39 | both halves | 6e-05 |  |
| [[EPB41L2]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CD59]] | -0.51 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[GALNT4]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PGAM1]] | -0.50 | -0.71 / -0.31 | both halves | 2e-04 |  |
| [[HPSE]] | -0.49 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[ATP5MC3]] ⚠ | -0.49 | -0.56 / -0.36 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RIPK4]] | -0.49 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[BANF1]] | -0.48 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[FKBP1A]] | -0.48 | -0.58 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-24.6, 21.7); signed map (-5.8, -8.2). **Vector** length 91.2, 23.1% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +11.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.1 | +4.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +5.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -1.3 |
|  | [[Adenine (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,926,718-7,943,667 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIM44 |
| Gene groups (HGNC) | TIM23 complex |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43615](https://www.uniprot.org/uniprotkb/O43615) (Mitochondrial import inner membrane translocase subunit TIM44):

> Essential component of the PAM complex, a complex required for the translocation of transit peptide-containing proteins from the inner membrane into the mitochondrial matrix in an ATP-dependent manner (By similarity). Recruits mitochondrial HSP70 to drive protein translocation into the matrix using ATP as an energy source (By similarity).

**Summary**, from NCBI Gene [10469](https://www.ncbi.nlm.nih.gov/gene/10469):

> This gene encodes a peripheral membrane protein associated with the mitochondrial inner membrane translocase, which functions in the import of proteins across the mitochondrial inner membrane and into the mitochondrial matrix. The encoded protein mediates binding of mitochondrial heat shock protein 70 to the translocase of inner mitochondrial membrane 23 (TIM23) complex. Expression of this gene is upregulated in kidney in a mouse model of diabetes. A mutation in this gene is associated with …

**Accessions** — [HGNC:17316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17316) · Entrez [10469](https://www.ncbi.nlm.nih.gov/gene/10469) · UniProt [O43615](https://www.uniprot.org/uniprotkb/O43615) · Ensembl [ENSG00000104980](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104980)

## Data

Gene col 2537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2537); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2537]; `tensor/DDL_lfc|DDL_z.npy` [2537]; `embed/gene_vectors.npy` [2537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2537 or target_col == 2537). Every well: [[TIMM44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
