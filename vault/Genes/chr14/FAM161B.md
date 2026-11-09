---
symbol: "FAM161B"
type: "gene"
col: 7945
ensembl_id: "ENSG00000156050"
name: "FAM161 centrosomal protein B"
location: "14q24.3"
module: 41
arm: "+"
pooled_cpm: 7.0
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# FAM161B

*FAM161 centrosomal protein B* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.83× (z +9.9, q 3e-20, up in 18 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.70× (z +8.6, q 2e-15, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.544× (z -9.9, q 2e-20, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIL4]] (+0.63, fdr 7e-06), [[MMUT]] (+0.63, fdr 1e-05), [[SENP2]] (+0.61, fdr 1e-05); moves opposite to [[TXN]] (-0.58, fdr 2e-05), [[TMEM33]] (-0.57, fdr 1e-05), [[SLC25A13]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +9.9 | 3e-20 | 18/30 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +9.0 | 8e-17 | 6/12 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +8.6 | 2e-15 | 24/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +8.4 | 9e-15 | 24/47 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +7.9 | 5e-13 | 24/42 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +6.0 | 2e-07 | 15/42 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +5.5 | 3e-06 | 20/47 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.4 | 1e-03 | 6/22 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 13/46 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.001 | 10/41 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.033 | 1/47 (NCI-H2347) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.034 | 2/45 (HEC-1-A, CFPAC-1) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.059 | 9/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.067 | 2/47 (MIA PaCa-2, SW 900) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.075 | 3/42 (SNU-423, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -9.9 | 2e-20 | 27/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -9.7 | 1e-19 | 25/42 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.558×** | -9.5 | 3e-19 | 29/47 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -7.7 | 2e-12 | 26/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -7.2 | 5e-11 | 24/47 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -6.4 | 1e-08 | 21/37 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.693×** | -6.0 | 2e-07 | 16/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.708×** | -5.3 | 6e-06 | 14/44 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.723×** | -5.3 | 7e-06 | 15/47 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.723×** | -5.1 | 2e-05 | 14/46 (NCI-H2030, NCI-H460, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.749×** | -4.7 | 1e-04 | 13/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.759×** | -4.3 | 9e-04 | 14/47 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.620×** | -4.1 | 0.002 | 15/42 (hTERT-HPNE, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.844× | -3.9 | 0.003 | 6/48 (NCI-H1573, RPMI-7951, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.787×** | -3.9 | 0.003 | 11/43 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.860× | -3.5 | 0.016 | 13/48 (H4, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.822×** | -3.2 | 0.040 | 6/47 (H4, A-427, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.689×** | -3.2 | 0.040 | 6/44 (CFPAC-1, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.692×** | -3.2 | 0.044 | 4/38 (NCI-H23, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.693×** | -3.1 | 0.045 | 6/43 (Hs 766T, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 7.83 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 6.10 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.185× (z -8.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 8.96 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 0.05 µM 0.0924× (z -8.7) |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -11.3) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 6.91 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.106× (z -9.0) |
| [[J82 (line)]] | alt | 8.44 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 9.82 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.227× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 5.08 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.16× (z +10.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 6.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +10.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0948× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 7.61 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0818× (z -9.3) |
| [[SW480 (line)]] | alt | 6.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[A-172 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL4]] | +0.63 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[MMUT]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[SENP2]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[BBOF1]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[RAB33B]] | +0.61 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[MINDY2]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ACTR1B]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MED29]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[TTC21A]] | +0.56 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[HADHB]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[BUD31]] | +0.55 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[PARP16]] | +0.55 | +0.65 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TMEM33]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[LARS2]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[UCK2]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[HSPE1]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[SLC35B4]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NME1]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SPATA5]] | -0.53 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[LARP4]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[EIF4G3]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (3.8, -34.1); signed map (-13.2, 2.5). **Vector** length 61.6, 8.46% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +4.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.1 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | +0.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +0.9 | +3.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +0.9 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -9.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -7.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.4 | -9.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | FAM161 centrosomal protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,931,501-73,950,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31697; previously C14orf44 |
| Matched by | ensembl_id |

UniProt [Q96MY7](https://www.uniprot.org/uniprotkb/Q96MY7) carries no function annotation.

**Summary**, from NCBI Gene [145483](https://www.ncbi.nlm.nih.gov/gene/145483):

> Predicted to be involved in cilium organization. Located in cytoplasmic microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19854) · Entrez [145483](https://www.ncbi.nlm.nih.gov/gene/145483) · UniProt [Q96MY7](https://www.uniprot.org/uniprotkb/Q96MY7) · Ensembl [ENSG00000156050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156050)

## Data

Gene col 7945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7945); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7945]; `tensor/DDL_lfc|DDL_z.npy` [7945]; `embed/gene_vectors.npy` [7945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7945 or target_col == 7945). Every well: [[FAM161B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM161B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
