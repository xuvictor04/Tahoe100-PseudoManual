---
symbol: "C8orf82"
type: "gene"
col: 13113
ensembl_id: "ENSG00000213563"
name: "chromosome 8 open reading frame 82"
location: "8q24.3"
module: 3
arm: "+"
pooled_cpm: 6.64
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# C8orf82

*chromosome 8 open reading frame 82* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.37× (z +8.1, q 2e-13, up in 10 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.91× (z +4.0, q 0.009, up in 14 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -14.3, q 6e-44, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSEN34]] (+0.63, fdr 1e-05), [[TMEM276]] (+0.61, fdr 1e-05), [[CBFA2T2]] (+0.61, fdr 3e-05); moves opposite to [[ADAMTS3]] (-0.55, fdr 2e-05), [[CSTF3]] (-0.53, fdr 4e-04), [[PRDM6]] (-0.52, fdr 7e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.1 | 2e-13 | 10/13 (BT-474, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +7.1 | 3e-10 | 21/28 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +5.8 | 1e-06 | 17/33 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.91×** | +4.0 | 0.009 | 14/40 (Panc 03.27, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +3.6 | 0.039 | 9/21 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.074 | 9/41 (NCI-H2030, A549, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.39× | +3.2 | 0.10 | 10/40 (J82, NCI-H1573, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.37× | +3.0 | 0.17 | 6/40 (A-172, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -14.3 | 6e-44 | 34/37 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.306×** | -11.6 | 2e-28 | 34/39 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -7.2 | 9e-11 | 26/38 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.505×** | -6.4 | 2e-08 | 25/42 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.530×** | -6.2 | 7e-08 | 26/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.534×** | -6.1 | 1e-07 | 26/46 (SW48, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.654×** | -5.8 | 4e-07 | 27/45 (RPMI-7951, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.551×** | -5.8 | 4e-07 | 25/46 (A-427, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.285×** | -5.8 | 4e-07 | 27/41 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.582×** | -5.3 | 8e-06 | 20/43 (SW48, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -4.9 | 5e-05 | 23/40 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.624×** | -4.6 | 2e-04 | 22/44 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.637×** | -4.4 | 5e-04 | 20/42 (SNU-423, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.732×** | -4.3 | 8e-04 | 18/46 (COLO 205, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.628×** | -4.1 | 0.001 | 19/41 (SW48, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 10.5 | 0 | 4 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0385× (z -10.1) |
| [[LoVo (line)]] | wt | 5.41 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -8.9) |
| [[LS 180 (line)]] | wt | 8.38 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.5) |
| [[PANC-1 (line)]] | alt | 8.86 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -10.9) |
| [[SW480 (line)]] | alt | 5.40 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -11.6) |
| [[A-427 (line)]] | wt | 6.82 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.147× (z -8.6) |
| [[A498 (line)]] | wt | 8.37 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.5) |
| [[A549 (line)]] | wt | 7.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -8.5) |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 5.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.4) |
| [[COLO 205 (line)]] | alt | 5.57 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0578× (z -8.5) |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.7) |
| [[HT-29 (line)]] | alt | 6.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 6.51 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -8.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.77 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 8.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -11.1) |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -11.0) |
| [[A-172 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 17 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSEN34]] | +0.63 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TMEM276]] | +0.61 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.61 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ZDHHC12]] | +0.61 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[PAFAH1B3]] | +0.60 | +0.56 / +0.25 | both halves | 4e-04 |  |
| [[RPUSD1]] | +0.60 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[RAB40B]] | +0.59 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[DOK4]] | +0.58 | +0.57 / +0.36 | both halves | 9e-05 |  |
| [[SNN]] | +0.57 | +0.63 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[MPST]] | +0.57 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[SLC39A4]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SLC25A1]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[MOSPD3]] | +0.56 | +0.60 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS3]] | -0.55 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[CSTF3]] | -0.53 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[PRDM6]] | -0.52 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[LINC02542]] | -0.51 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[LINC00705]] | -0.50 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[ARHGEF37]] | -0.50 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[PCBP1-AS1]] | -0.50 | -0.39 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[LINC01358]] | -0.50 | -0.29 / -0.31 | both halves | 2e-04 |  |
| [[AP5M1]] | -0.49 | -0.46 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[KRR1]] | -0.48 | -0.42 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[PCOLCE2]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TLCD4-RWDD3]] | -0.48 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[LINC01135]] | -0.48 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[MCPH1-AS1]] | -0.47 | -0.46 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.432). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.4, -15.0); signed map (-37.0, 13.1). **Vector** length 59.2, 9.72% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +7.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -4.3 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -14.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 8 open reading frame 82 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,525,733-144,529,132 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC70857 |
| Matched by | ensembl_id |

UniProt [Q6P1X6](https://www.uniprot.org/uniprotkb/Q6P1X6) carries no function annotation.

**Summary**, from NCBI Gene [414919](https://www.ncbi.nlm.nih.gov/gene/414919):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33826) · Entrez [414919](https://www.ncbi.nlm.nih.gov/gene/414919) · UniProt [Q6P1X6](https://www.uniprot.org/uniprotkb/Q6P1X6) · Ensembl [ENSG00000213563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213563)

## Data

Gene col 13113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13113); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13113]; `tensor/DDL_lfc|DDL_z.npy` [13113]; `embed/gene_vectors.npy` [13113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13113 or target_col == 13113). Every well: [[C8orf82 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C8orf82.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
