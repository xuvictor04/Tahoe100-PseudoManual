---
symbol: "CBR1"
type: "gene"
col: 8234
ensembl_id: "ENSG00000159228"
name: "carbonyl reductase 1"
location: "21q22.12"
module: 23
arm: "-"
pooled_cpm: 19.21
n_lines_expressing: 46
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CBR1

*carbonyl reductase 1* — 21q22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.42× (z +7.1, q 1e-09, up in 33 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.284× (z -10.0, q 7e-21, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL17]] (+0.67, fdr 4e-05), [[MRPS34]] (+0.65, fdr 2e-05), [[SLC39A3]] (+0.65, fdr 5e-05); moves opposite to [[CCNL2]] (-0.63, fdr 1e-05), [[CCDC17]] (-0.61, fdr 5e-05), [[AMY2B]] (-0.60, fdr 1e-04).
> It sits in the **-** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +7.1 | 1e-09 | 33/42 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.39×** | +7.0 | 1e-09 | 38/44 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.16×** | +6.1 | 2e-07 | 32/44 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.91×** | +5.2 | 4e-05 | 34/43 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +4.9 | 9e-05 | 34/44 (A498, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +4.8 | 1e-04 | 35/44 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.61×** | +3.8 | 0.013 | 26/41 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.058 | 17/44 (HS-578T, A-427, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.54×** | +3.3 | 0.058 | 20/40 (HS-578T, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.51×** | +3.3 | 0.058 | 21/41 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.33×** | +3.2 | 0.065 | 17/44 (HT-29, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.55×** | +3.2 | 0.065 | 18/36 (A498, A549, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.50×** | +3.1 | 0.086 | 16/28 (NCI-H460, A498, …) | rises with dose | composition shift; position effect removed |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.095 | 16/44 (HS-578T, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.284×** | -10.0 | 7e-21 | 42/44 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.415×** | -9.9 | 1e-20 | 41/43 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.479×** | -5.9 | 9e-07 | 38/42 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -5.4 | 9e-06 | 36/43 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -5.0 | 6e-05 | 38/42 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -4.9 | 8e-05 | 29/43 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.624×** | -3.8 | 0.014 | 24/43 (LOX-IMVI, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.409×** | -3.7 | 0.014 | 28/43 (MIA PaCa-2, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.442×** | -3.4 | 0.043 | 21/40 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 22.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 21.7 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.191× (z -9.0) |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.6) |
| [[A498 (line)]] | wt | 60.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.1) |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0818× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0953× (z -9.0) |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0990× (z -16.5) |
| [[A-172 (line)]] | wt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.1) |
| [[C32 (line)]] | wt | 24.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.4) |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -9.9) |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.145× (z -10.0) |
| [[HS-578T (line)]] | alt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.3) |
| [[J82 (line)]] | alt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -16.3) |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 9.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0698× (z -12.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0556× (z -12.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -8.7) |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -9.5) |
| [[A-427 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL17]] | +0.67 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[MRPS34]] | +0.65 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SLC39A3]] | +0.65 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[ULBP3]] | +0.61 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[RGS19]] | +0.60 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[CAMK2G]] | +0.60 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[UBL4A]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[RPP40]] | +0.59 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[MFSD9]] | +0.59 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[RNF216]] | +0.58 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[MRPL12]] | +0.58 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[FAM241B]] | +0.58 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNL2]] | -0.63 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[CCDC17]] | -0.61 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[AMY2B]] | -0.60 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[PPP1R3F]] | -0.60 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[LRRC37A3]] | -0.59 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[CYB5D2]] | -0.59 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[CROCC]] | -0.59 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[CHMP3]] | -0.59 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[EFCAB6]] | -0.58 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[PBLD]] | -0.58 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TTC32]] | -0.57 | -0.47 / -0.24 | both halves | 5e-04 |  |
| [[RC3H2]] | -0.57 | -0.43 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-0.6, 19.9); signed map (-20.7, -7.4). **Vector** length 87.0, 25.4% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.6 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.5 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.3 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.5 | +0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.5 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.3 | -9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.9 | +3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +3.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | carbonyl reductase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.12 — chr21:36,069,941-36,073,166 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR21C1; previously CBR |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: Synthesis of Prostaglandins (PG) and Thromboxanes (TX); Arachidonate metabolism; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P16152](https://www.uniprot.org/uniprotkb/P16152) (Carbonyl reductase):

> NADPH-dependent reductase with broad substrate specificity. Catalyzes the reduction of a wide variety of carbonyl compounds including quinones, prostaglandins, menadione, plus various xenobiotics. Catalyzes the reduction of the antitumor anthracyclines doxorubicin and daunorubicin to the cardiotoxic compounds doxorubicinol and daunorubicinol. Can convert prostaglandin E to prostaglandin F2-alpha (By similarity). Can bind glutathione, which explains its higher affinity for glutathione-conjugated …

**Summary**, from NCBI Gene [873](https://www.ncbi.nlm.nih.gov/gene/873):

> The protein encoded by this gene belongs to the short-chain dehydrogenases/reductases (SDR) family, which function as NADPH-dependent oxidoreductases having wide specificity for carbonyl compounds, such as quinones, prostaglandins, and various xenobiotics. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:1548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1548) · Entrez [873](https://www.ncbi.nlm.nih.gov/gene/873) · UniProt [P16152](https://www.uniprot.org/uniprotkb/P16152) · Ensembl [ENSG00000159228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159228)

## Data

Gene col 8234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8234); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8234]; `tensor/DDL_lfc|DDL_z.npy` [8234]; `embed/gene_vectors.npy` [8234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8234 or target_col == 8234). Every well: [[CBR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
