---
symbol: "TLCD3A"
type: "gene"
col: 9520
ensembl_id: "ENSG00000167695"
name: "TLC domain containing 3A"
location: "17p13.3"
module: 5
arm: "+"
pooled_cpm: 6.56
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# TLCD3A

*TLC domain containing 3A* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.75× (z +7.6, q 9e-12, up in 20 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.219× (z -20.8, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGW]] (+0.71, fdr 4e-05), [[TOR1A]] (+0.68, fdr 1e-05), [[CCNJ]] (+0.66, fdr 1e-05); moves opposite to [[SPAG9]] (-0.62, fdr 5e-05), [[ALAD]] (-0.61, fdr 4e-05), [[DDAH2]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +7.6 | 9e-12 | 20/45 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.6 | 9e-12 | 24/42 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.5 | 9e-06 | 4/12 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +5.1 | 5e-05 | 15/44 (NCI-H1792, SW 900, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.3 | 0.002 | 8/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +4.1 | 0.004 | 11/34 (HOP62, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **1.33×** | +3.6 | 0.028 | 8/18 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.043 | 1/42 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.043 | 4/40 (SW480, PANC-1, …) | inconsistent across doses | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.40×** | +3.3 | 0.056 | 4/24 (A-172, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.068 | 8/44 (A-427, Hs 766T, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +3.2 | 0.074 | 12/45 (SW480, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.219×** | -20.8 | 0e+00 | 43/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.252×** | -18.8 | 0e+00 | 44/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.283×** | -17.3 | 0e+00 | 42/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.513×** | -12.9 | 6e-36 | 32/41 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.439×** | -11.3 | 2e-27 | 38/47 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.654×** | -8.2 | 2e-14 | 28/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.351×** | -7.5 | 5e-12 | 28/46 (SHP-77, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.593×** | -7.2 | 6e-11 | 23/44 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.659×** | -5.0 | 3e-05 | 18/45 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.763×** | -3.7 | 0.012 | 15/42 (SHP-77, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.829×** | -3.6 | 0.015 | 11/47 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.785×** | -3.3 | 0.043 | 8/46 (NCI-H23, A498, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.764×** | -3.2 | 0.053 | 9/44 (A-427, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 9.91 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -10.6) |
| [[SW480 (line)]] | alt | 7.41 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -15.5) |
| [[A-172 (line)]] | wt | 11.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -10.9) |
| [[A498 (line)]] | wt | 8.35 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0986× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.131× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 6.95 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -11.3) |
| [[C32 (line)]] | wt | 9.10 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0244× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.133× (z -10.8) |
| [[HOP62 (line)]] | alt | 6.51 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0794× (z -12.7) |
| [[SHP-77 (line)]] | alt | 7.34 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0730× (z -10.1) |
| [[SNU-423 (line)]] | alt | 6.73 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0870× (z -10.4) |
| [[A549 (line)]] | wt | 7.49 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -8.9) |
| [[HT-29 (line)]] | alt | 3.21 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0482× (z -9.9) |
| [[KATO III (line)]] | alt | 8.14 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 3.90 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0583× (z -10.5) |
| [[LS 180 (line)]] | wt | 7.76 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 7.46 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.113× (z -9.8) |
| [[RKO (line)]] | wt | 10.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0823× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 5.93 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0698× (z -8.9) |
| [[SNU-1 (line)]] | wt | 8.47 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0646× (z -8.8) |
| [[SW1417 (line)]] | alt | 4.10 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0657× (z -9.8) |
| [[A-427 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGW]] | +0.71 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[TOR1A]] | +0.68 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CCNJ]] | +0.66 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MRM1]] | +0.66 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CUL1]] | +0.65 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SETD1B]] | +0.64 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[ALG8]] | +0.63 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[DUS2]] | +0.63 | +0.19 / +0.64 | ⚠ one half (not replicated) | 8e-04 |  |
| [[E2F3]] | +0.63 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | +0.63 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[PRDM15]] | +0.63 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SFT2D3]] | +0.62 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[DDX56]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.62 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ALAD]] | -0.61 | -0.45 / -0.43 | both halves | 4e-05 |  |
| [[DDAH2]] | -0.59 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[KIFAP3]] | -0.58 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[STAM2]] | -0.58 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPDL]] | -0.58 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[CAST]] | -0.55 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[ARL3]] | -0.54 | -0.21 / -0.40 | both halves | 6e-04 |  |
| [[HDAC5]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[OSBPL9]] | -0.53 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[TUFT1]] | -0.53 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[FCHO1]] | -0.53 | -0.21 / -0.35 | both halves | 7e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.5, 10.6); signed map (24.3, -29.5). **Vector** length 69.3, 11.4% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -18.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -20.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -17.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.4 | -7.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -7.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TLC domain containing 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:732,412-742,968 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22282, CT120; previously FAM57A |
| Gene groups (HGNC) | TLC domain containing |
| Matched by | ensembl_id |

UniProt [Q8TBR7](https://www.uniprot.org/uniprotkb/Q8TBR7) carries no function annotation.

**Summary**, from NCBI Gene [79850](https://www.ncbi.nlm.nih.gov/gene/79850):

> The protein encoded by this gene is a membrane-associated protein that promotes lung carcinogenesis. The encoded protein may be involved in amino acid transport and glutathione metabolism since it can interact with a solute carrier family member (SLC3A2) and an isoform of gamma-glutamyltranspeptidase-like 3. An alternatively spliced variant encoding a protein that lacks a 32 aa internal segment showed the opposite effect, inhibiting lung cancer cell growth. Knockdown of this gene also inhibited …

**Accessions** — [HGNC:29646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29646) · Entrez [79850](https://www.ncbi.nlm.nih.gov/gene/79850) · UniProt [Q8TBR7](https://www.uniprot.org/uniprotkb/Q8TBR7) · Ensembl [ENSG00000167695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167695)

## Data

Gene col 9520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9520); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9520]; `tensor/DDL_lfc|DDL_z.npy` [9520]; `embed/gene_vectors.npy` [9520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9520 or target_col == 9520). Every well: [[TLCD3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLCD3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
