---
symbol: "IMPA1"
type: "gene"
col: 5470
ensembl_id: "ENSG00000133731"
name: "inositol monophosphatase 1"
location: "8q21.13"
module: 5
arm: "-"
pooled_cpm: 48.26
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# IMPA1

*inositol monophosphatase 1* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +17.2, q 0e+00, up in 39 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.0956×, NCI-H2347 0.253×, NCI-H23 0.240×, SW 900 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AsPC-1 0.266×, NCI-H2347 0.428×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.323×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.233×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN5]] (+0.56, fdr 3e-05), [[SUGT1P3]] (+0.52, fdr 1e-05), [[ALDH9A1]] (+0.52, fdr 1e-05); moves opposite to [[C1orf159]] (-0.52, fdr 4e-05), [[TOMM40]] (-0.52, fdr 3e-05), [[TIMM23B-AGAP6]] (-0.51, fdr 1e-04).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +17.2 | 0e+00 | 39/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +10.9 | 3e-25 | 40/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +10.2 | 4e-22 | 38/47 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +9.2 | 6e-18 | 34/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +8.8 | 1e-16 | 34/48 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +7.7 | 1e-12 | 27/48 (SW480, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +7.5 | 8e-12 | 30/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.40×** | +7.4 | 9e-12 | 33/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 3e-06 | 21/48 (HOP62, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.24×** | +4.8 | 7e-05 | 20/48 (PANC-1, BT-474, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 7e-04 | 16/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.21×** | +4.3 | 1e-03 | 20/48 (Panc 03.27, RPMI-7951, …) | rises with dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.004 | 16/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.7 | 0.010 | 18/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Furosemide (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.029 | 9/48 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.056 | 13/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.061 | 12/48 (HCT15, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5470.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.0956×, NCI-H2347 0.253×, NCI-H23 0.240×, SW 900 0.319×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AsPC-1 0.266×, NCI-H2347 0.428×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SNU-423 0.323×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.233×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.8 | 0.046 | 10/48 (SW1417, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.8 | 0.046 | 19/47 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 66.0 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 82.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 62.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +15.6) | — |
| [[SK-MEL-2 (line)]] | alt | 46.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0956× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 52.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 56.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.5) | — |
| [[A-172 (line)]] | wt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 41.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +16.2) | — |
| [[Hs 766T (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 53.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.233× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 38.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 55.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 58.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +14.4) | — |
| [[RPMI-7951 (line)]] | alt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 36.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.323× (z -10.1) |
| [[A-427 (line)]] | wt | 49.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 121 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN5]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SUGT1P3]] | +0.52 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ALDH9A1]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SUGT1P3-1]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SP140L]] | +0.50 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[COQ10A]] | +0.49 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TEC]] | +0.49 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CYP2J2]] | +0.49 | +0.24 / +0.61 | both halves | 5e-04 |  |
| [[FIG4]] | +0.48 | +0.35 / +0.59 | both halves | 1e-04 | same gene group |
| [[RYBP]] | +0.47 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[WDR11]] | +0.47 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[GTPBP8]] | +0.47 | +0.35 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf159]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TOMM40]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[TIMM23B-AGAP6]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[FBXO36]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[NDOR1]] | -0.48 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[PRDM15]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[AGAP6]] | -0.47 | -0.19 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ELAVL1]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[PTRH1]] | -0.46 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[MBD3]] | -0.46 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[PGP]] | -0.46 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ZNF407]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.395). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.6, -29.3); signed map (7.4, -36.8). **Vector** length 87.6, 18.5% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +10.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.4 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | +0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | inositol monophosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:81,656,914-81,686,331 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously IMPA |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 2 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P29218](https://www.uniprot.org/uniprotkb/P29218) (Inositol monophosphatase 1):

> Phosphatase involved in the dephosphorylation of myo-inositol monophosphates to generate myo-inositol. Is also able to dephosphorylate scyllo-inositol-phosphate, myo-inositol 1,4-diphosphate, scyllo-inositol-1,3-diphosphate and scyllo-inositol-1,4-diphosphate. Also dephosphorylates in vitro other sugar-phosphates including D-galactose-1-phosphate, glucose-1-phosphate, glucose-6-phosphate, fructose-1-phosphate, beta-glycerophosphate and 2'-AMP. Responsible for the provision of inositol required …

**Summary**, from NCBI Gene [3612](https://www.ncbi.nlm.nih.gov/gene/3612):

> This gene encodes an enzyme that dephosphorylates myo-inositol monophosphate to generate free myo-inositol, a precursor of phosphatidylinositol, and is therefore an important modulator of intracellular signal transduction via the production of the second messengers myoinositol 1,4,5-trisphosphate and diacylglycerol. This enzyme can also use myo-inositol-1,3-diphosphate, myo-inositol-1,4-diphosphate, scyllo-inositol-phosphate, glucose-1-phosphate, glucose-6-phosphate, fructose-1-phosphate, …

**Accessions** — [HGNC:6050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6050) · Entrez [3612](https://www.ncbi.nlm.nih.gov/gene/3612) · UniProt [P29218](https://www.uniprot.org/uniprotkb/P29218) · Ensembl [ENSG00000133731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133731)

## Data

Gene col 5470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5470); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5470]; `tensor/DDL_lfc|DDL_z.npy` [5470]; `embed/gene_vectors.npy` [5470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5470 or target_col == 5470). Every well: [[IMPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
