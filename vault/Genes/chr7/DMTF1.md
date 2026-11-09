---
symbol: "DMTF1"
type: "gene"
col: 5662
ensembl_id: "ENSG00000135164"
name: "cyclin D binding myb like transcription factor 1"
location: "7q21.12"
module: 11
arm: "+"
pooled_cpm: 107.67
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# DMTF1

*cyclin D binding myb like transcription factor 1* — 7q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.28× (z +4.8, q 0.001, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.579× (z -7.4, q 6e-11, down in 38 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.575× (z -3.9, q 0.007, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.110×, NCI-H23 0.207×, H4 0.327×, SW48 0.309×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-1 0.199×, NCI-H23 0.331×, C-33 A 0.370×, Hs 766T 0.333×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (C32 0.274×, A-172 0.345×; ⚠ toxic; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.352×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC4]] (+0.61, fdr 9e-06), [[ZNF160]] (+0.60, fdr 1e-05), [[POLI]] (+0.59, fdr 2e-05); moves opposite to [[CMTM8]] (-0.51, fdr 1e-04), [[NFATC3]] (-0.50, fdr 1e-04), [[MRPS28]] (-0.49, fdr 6e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +4.8 | 0.001 | 25/48 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 0.003 | 28/48 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.003 | 29/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.013 | 31/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5662.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.110×, NCI-H23 0.207×, H4 0.327×, SW48 0.309×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (SNU-1 0.199×, NCI-H23 0.331×, C-33 A 0.370×, Hs 766T 0.333×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (C32 0.274×, A-172 0.345×; ⚠ toxic; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.352×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.579×** | -7.4 | 6e-11 | 38/49 (SK-MEL-2, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.602×** | -6.4 | 5e-08 | 33/45 (NCI-H460, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.683×** | -5.0 | 1e-04 | 32/44 (SNU-1, NCI-H23, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.710×** | -4.7 | 4e-04 | 34/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.734×** | -4.2 | 0.003 | 30/48 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.731×** | -4.1 | 0.004 | 30/47 (C32, A-172, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.575×** | -3.9 | 0.007 | 33/49 (RPMI-7951, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.823×** | -3.8 | 0.012 | 24/48 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.039 | 25/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.621×** | -3.4 | 0.039 | 28/45 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.850× | -3.1 | 0.086 | 26/49 (HEC-1-A, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[RKO (line)]] | wt | 86.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 74.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SW48 (line)]] | wt | 97.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.345× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[C32 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.274× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[H4 (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[Hs 766T (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HT-29 (line)]] | alt | 87.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.4) | — |
| [[LoVo (line)]] | wt | 74.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 64.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 126 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SW1417 (line)]] | alt | 99.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.7) | — |
| [[SW480 (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.1) | — |
| [[A-427 (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 86.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 149 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 126 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 97.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 117 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC4]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[ZNF160]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[POLI]] | +0.59 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MTR]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[RMDN1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[RO60]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SEPSECS]] | +0.56 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[FNTA]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ERMARD]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[HMGCL]] | +0.55 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[PHF20L1]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ZNG1B]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTM8]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[NFATC3]] | -0.50 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[MRPS28]] | -0.49 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[TUBA8]] | -0.49 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[C16orf95]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[POLR3B]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[LMTK2]] | -0.48 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[CCDC12]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[FTO]] | -0.48 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[ZNF787]] | -0.47 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[CHST12]] | -0.47 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[COP1]] | -0.47 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.219). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-22.6, 19.6); signed map (9.8, -15.2). **Vector** length 89.4, 26.8% of its response variance represented; |z| ≥ 3 in 733 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +0.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.7 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.6 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -0.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | -3.5 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin D binding myb like transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.12 — chr7:87,152,409-87,196,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DMP1, DMTF, hDMP1, MRUL |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y222](https://www.uniprot.org/uniprotkb/Q9Y222) (Cyclin-D-binding Myb-like transcription factor 1):

> Transcriptional activator which activates the CDKN2A/ARF locus in response to Ras-Raf signaling, thereby promoting p53/TP53-dependent growth arrest (By similarity). Binds to the consensus sequence 5'-CCCG[GT]ATGT-3' (By similarity). Isoform 1 may cooperate with MYB to activate transcription of the ANPEP gene. Isoform 2 may antagonize transcriptional activation by isoform 1.

**Summary**, from NCBI Gene [9988](https://www.ncbi.nlm.nih.gov/gene/9988):

> This gene encodes a transcription factor that contains a cyclin D-binding domain, three central Myb-like repeats, and two flanking acidic transactivation domains at the N- and C-termini. The encoded protein is induced by the oncogenic Ras signaling pathway and functions as a tumor suppressor by activating the transcription of ARF and thus the ARF-p53 pathway to arrest cell growth or induce apoptosis. It also activates the transcription of aminopeptidase N and may play a role in hematopoietic …

**Accessions** — [HGNC:14603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14603) · Entrez [9988](https://www.ncbi.nlm.nih.gov/gene/9988) · UniProt [Q9Y222](https://www.uniprot.org/uniprotkb/Q9Y222) · Ensembl [ENSG00000135164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135164)

## Data

Gene col 5662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5662); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5662]; `tensor/DDL_lfc|DDL_z.npy` [5662]; `embed/gene_vectors.npy` [5662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5662 or target_col == 5662). Every well: [[DMTF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMTF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
