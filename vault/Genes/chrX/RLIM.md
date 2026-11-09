---
symbol: "RLIM"
type: "gene"
col: 5190
ensembl_id: "ENSG00000131263"
name: "ring finger protein, LIM domain interacting"
location: "Xq13.2"
module: 54
arm: "-"
pooled_cpm: 145.43
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# RLIM

*ring finger protein, LIM domain interacting* — Xq13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.19× (z +8.4, q 4e-14, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.582× (z -7.2, q 4e-10, down in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.794× (z -4.5, q 7e-04, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF460]] (+0.69, fdr 7e-06), [[CYB5D1]] (+0.65, fdr 1e-05), [[ZNF548]] (+0.64, fdr 1e-05); moves opposite to [[SNHG25]] (-0.57, fdr 7e-05), [[STK38]] (-0.56, fdr 2e-05), [[MZT2A]] (-0.55, fdr 3e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.19×** | +8.4 | 4e-14 | 48/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +8.1 | 2e-13 | 39/48 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +6.6 | 8e-09 | 40/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +6.5 | 1e-08 | 41/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.45×** | +6.5 | 1e-08 | 40/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +5.7 | 1e-06 | 40/48 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.6 | 1e-06 | 1/50 (CHP-212) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.003 | 30/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.009 | 32/48 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.009 | 33/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.018 | 32/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.10 | 25/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.12 | 24/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.582×** | -7.2 | 4e-10 | 44/47 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.667×** | -5.4 | 2e-05 | 35/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.705×** | -4.8 | 3e-04 | 34/48 (SW 900, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.704×** | -4.6 | 4e-04 | 34/48 (CFPAC-1, A498, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.789×** | -4.6 | 4e-04 | 29/49 (A498, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -4.5 | 7e-04 | 31/48 (CFPAC-1, HOP62, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.721×** | -4.3 | 0.001 | 30/44 (NCI-H23, C-33 A, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.743×** | -4.1 | 0.003 | 38/48 (A-427, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.753×** | -3.8 | 0.011 | 33/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.040 | 33/49 (NCI-H2122, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.782×** | -3.3 | 0.058 | 25/48 (H4, A498, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.853× | -3.1 | 0.091 | 15/48 (LoVo, A549, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 185 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 210 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[AsPC-1 (line)]] | alt | 210 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +10.8) | — |
| [[SW480 (line)]] | alt | 185 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.43× (z +10.3) | — |
| [[A-172 (line)]] | wt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.2) | — |
| [[A-427 (line)]] | wt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.2) | — |
| [[A498 (line)]] | wt | 185 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -12.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[C-33 A (line)]] | alt | 84.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 82.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 140 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.71× (z +8.9) | — |
| [[H4 (line)]] | wt | 206 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0948× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 84.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 213 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 151 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 78.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 144 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 172 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 99.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0957× (z -10.5) |
| [[SW1417 (line)]] | alt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.0) | — |
| [[SW48 (line)]] | wt | 99.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.4) | — |
| [[A549 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 108 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 153 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 128 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 81.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 141 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF460]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[CYB5D1]] | +0.65 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ZNF548]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SMU1]] | +0.62 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[PEX19]] | +0.62 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ARCN1]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SF3B1]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ZNF543]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZBTB37]] | +0.58 | +0.32 / +0.68 | both halves | 2e-04 |  |
| [[NELFE]] | +0.57 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ZNF816]] | +0.57 | +0.43 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG25]] | -0.57 | -0.37 / -0.66 | both halves | 7e-05 |  |
| [[STK38]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MZT2A]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[BTBD7]] | -0.55 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[ILKAP]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TBC1D12]] | -0.54 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[UBE2G1]] | -0.54 | -0.31 / -0.50 | both halves | 2e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SNHG19]] | -0.54 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[SEC24B]] | -0.54 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[MFSD14CP]] | -0.54 | -0.26 / -0.57 | both halves | 3e-04 |  |
| [[MEMO1]] | -0.53 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[MZT2B]] | -0.53 | -0.39 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.7, -16.7); signed map (-2.8, -32.5). **Vector** length 89.7, 29.9% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +3.7 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.7 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +1.7 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.6 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.9 | -0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.8 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein, LIM domain interacting |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.2 — chrX:74,582,976-74,614,624 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-43, MGC15161; previously RNF12 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVW2](https://www.uniprot.org/uniprotkb/Q9NVW2) (E3 ubiquitin-protein ligase RLIM):

> E3 ubiquitin-protein ligase that acts as a negative coregulator for LIM homeodomain transcription factors by mediating the ubiquitination and subsequent degradation of LIM cofactors LDB1 and LDB2 and by mediating the recruitment the SIN3a/histone deacetylase corepressor complex. Ubiquitination and degradation of LIM cofactors LDB1 and LDB2 allows DNA-bound LIM homeodomain transcription factors to interact with other protein partners such as RLIM. Plays a role in telomere length-mediated growth …

**Summary**, from NCBI Gene [51132](https://www.ncbi.nlm.nih.gov/gene/51132):

> The protein encoded by this gene is a RING-H2 zinc finger protein. It has been shown to be an E3 ubiquitin protein ligase that targets LIM domain binding 1 (LDB1/CLIM), and causes proteasome-dependent degradation of LDB1. This protein and LDB1 are co-repressors of LHX1/LIM-1, a homeodomain transcription factor. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:13429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13429) · Entrez [51132](https://www.ncbi.nlm.nih.gov/gene/51132) · UniProt [Q9NVW2](https://www.uniprot.org/uniprotkb/Q9NVW2) · Ensembl [ENSG00000131263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131263)

## Data

Gene col 5190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5190); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5190]; `tensor/DDL_lfc|DDL_z.npy` [5190]; `embed/gene_vectors.npy` [5190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5190 or target_col == 5190). Every well: [[RLIM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RLIM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
