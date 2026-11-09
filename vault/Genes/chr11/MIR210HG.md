---
symbol: "MIR210HG"
type: "gene"
col: 14481
ensembl_id: "ENSG00000247095"
name: "MIR210 host gene"
location: "11p15.5"
module: 48
arm: "+"
pooled_cpm: 5.7
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# MIR210HG

*MIR210 host gene* — 11p15.5

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.148× (z -20.2, q 0e+00, down in 36 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM162A]] (+0.64, fdr 1e-05), [[MINCR]] (+0.62, fdr 4e-05), [[TMEM276]] (+0.62, fdr 1e-05); moves opposite to [[ADSS2]] (-0.68, fdr 7e-06), [[OXCT1]] (-0.61, fdr 3e-05), [[SNX5]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.55× | +3.3 | 0.29 | 12/40 (LS 180, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 1.52× | +3.1 | 0.29 | 14/44 (HT-29, SW1417, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.51× | +3.1 | 0.29 | 7/44 (LS 180, KATO III, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.50× | +3.1 | 0.29 | 9/30 (A-172, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.148×** | -20.2 | 0e+00 | 36/36 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.168×** | -13.3 | 8e-38 | 37/38 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.237×** | -10.3 | 1e-22 | 40/43 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.335×** | -7.8 | 7e-13 | 28/34 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.383×** | -7.1 | 1e-10 | 29/46 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.400×** | -6.8 | 8e-10 | 31/43 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -6.1 | 1e-07 | 29/40 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.469×** | -5.6 | 1e-06 | 28/44 (HCT15, J82, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.532×** | -4.7 | 2e-04 | 25/44 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.517×** | -4.6 | 2e-04 | 23/43 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -4.2 | 0.001 | 23/38 (BT-474, LS 180, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -3.9 | 0.004 | 20/44 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.344×** | -3.4 | 0.026 | 16/40 (COLO 205, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.636×** | -3.4 | 0.031 | 16/43 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.379×** | -3.1 | 0.068 | 16/40 (J82, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.639×** | -3.1 | 0.075 | 13/44 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.664×** | -3.0 | 0.076 | 13/45 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 10.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0317× (z -22.2) |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0728× (z -13.2) |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0298× (z -21.5) |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0409× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 9.16 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0163× (z -25.7) |
| [[KATO III (line)]] | alt | 10.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0220× (z -16.2) |
| [[LoVo (line)]] | wt | 7.42 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0237× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 5.98 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0460× (z -18.6) |
| [[PANC-1 (line)]] | alt | 6.56 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0359× (z -22.4) |
| [[RPMI-7951 (line)]] | alt | 10.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -11.2) |
| [[SW1417 (line)]] | alt | 5.65 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -14.0) |
| [[SW480 (line)]] | alt | 4.70 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0720× (z -16.2) |
| [[HOP62 (line)]] | alt | 5.85 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.5) |
| [[J82 (line)]] | alt | 14.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -15.8) |
| [[A-172 (line)]] | wt | 4.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0373× (z -16.0) |
| [[A549 (line)]] | wt | 3.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0412× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 3.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0544× (z -11.7) |
| [[C32 (line)]] | wt | 4.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -9.3) |
| [[Hs 766T (line)]] | wt | 7.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -11.4) |
| [[HS-578T (line)]] | alt | 4.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 4.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0771× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 3.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 1.71 | 0 | 1 | — | [[Uridine (drug)]] 5 µM 0.217× (z -18.5) |
| [[SHP-77 (line)]] | alt | 3.00 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0283× (z -8.6) |
| [[SNU-423 (line)]] | alt | 7.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -11.8) |
| [[SW48 (line)]] | wt | 6.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0625× (z -9.6) |
| [[A-427 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM162A]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[MINCR]] | +0.62 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[TMEM276]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RNF114]] | +0.61 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[ATP5MJ]] | +0.59 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[RPS26]] | +0.58 | +0.23 / +0.59 | both halves | 5e-04 |  |
| [[PCSK1N]] | +0.58 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[SEC61G]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[NDUFA3]] | +0.57 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[WDR45B]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[COX6A1]] | +0.57 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[COMMD6]] | +0.57 | +0.41 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADSS2]] | -0.68 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[OXCT1]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SNX5]] | -0.58 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SEPTIN11]] | -0.57 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[ZMPSTE24]] | -0.55 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[EIF4G2]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MCCC2]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ELK4]] | -0.53 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[N4BP2]] | -0.53 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[SLC25A21]] | -0.53 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[STK26]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SCRN1]] | -0.53 | -0.29 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-43.9, -18.7); signed map (-31.2, 7.1). **Vector** length 64.7, 11.6% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +2.3 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.1 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -20.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MIR210 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.5 — chr11:565,657-568,457 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39524) · Entrez [100506211](https://www.ncbi.nlm.nih.gov/gene/100506211) · Ensembl [ENSG00000247095](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247095)

## Data

Gene col 14481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14481); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14481]; `tensor/DDL_lfc|DDL_z.npy` [14481]; `embed/gene_vectors.npy` [14481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14481 or target_col == 14481). Every well: [[MIR210HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR210HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
