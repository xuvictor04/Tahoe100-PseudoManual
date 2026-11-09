---
symbol: "SIRT7"
type: "gene"
col: 11919
ensembl_id: "ENSG00000187531"
name: "sirtuin 7"
location: "17q25.3"
module: 3
arm: "+"
pooled_cpm: 21.62
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SIRT7

*sirtuin 7* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.44× (z +12.4, q 2e-32, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.695× (z -5.0, q 3e-04, down in 22 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.761× (z -3.6, q 0.092, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.182×, A549 0.216×, SW480 0.408×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 0.111×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.126×; ⚠ toxic; transcription drop); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (H4 0.100×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC34]] (+0.68, fdr 8e-05), [[TRADD]] (+0.68, fdr 1e-05), [[ARL8A]] (+0.66, fdr 1e-05); moves opposite to [[POGLUT3]] (-0.61, fdr 1e-05), [[OXCT1]] (-0.60, fdr 8e-05), [[PTGR2]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.44×** | +12.4 | 2e-32 | 46/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +11.1 | 2e-26 | 44/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.21×** | +11.1 | 4e-26 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +7.4 | 1e-11 | 31/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +6.3 | 3e-08 | 27/47 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +6.2 | 4e-08 | 32/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +6.1 | 7e-08 | 30/47 (SW480, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.7 | 7e-07 | 23/43 (KATO III, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.4 | 3e-06 | 33/46 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +5.3 | 5e-06 | 28/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.2 | 1e-05 | 21/41 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 3e-05 | 23/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.41×** | +4.8 | 6e-05 | 23/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +4.4 | 5e-04 | 23/48 (C32, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.3 | 8e-04 | 20/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.003 | 14/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.008 | 13/44 (HEC-1-A, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.010 | 17/48 (HEC-1-A, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.015 | 16/47 (SW 900, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.026 | 14/46 (HT-29, MIA PaCa-2, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11919.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.182×, A549 0.216×, SW480 0.408×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 0.111×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.126×; ⚠ toxic; transcription drop); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (H4 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.695×** | -5.0 | 3e-04 | 22/41 (SW48, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.761×** | -3.6 | 0.092 | 18/47 (HCT15, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 16.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.89× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 18.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +11.1) ⚠ cell-cycle shift, explains ~34% of this change | [[Simotinib (drug)]] 5 µM 0.194× (z -9.3) ⚠ toxic |
| [[A498 (line)]] | wt | 28.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A549 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 14.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.100× (z -8.6) |
| [[HOP62 (line)]] | alt | 13.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.91× (z +8.7) | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.6) ⚠ cell-cycle shift, explains ~6% of this change | — |
| [[NCI-H460 (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +12.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | +0.68 | +0.37 / +0.76 | both halves | 8e-05 |  |
| [[TRADD]] | +0.68 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[ARL8A]] | +0.66 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.64 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[PCGF1]] ⚠ | +0.64 | +0.44 / +0.68 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RALA]] | +0.64 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[RCE1]] | +0.63 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[C1orf35]] | +0.63 | +0.38 / +0.69 | both halves | 6e-05 |  |
| [[SELENOO]] | +0.62 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[ATOSB]] | +0.62 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[RASSF7]] | +0.62 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[PEX16]] | +0.62 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ZNF765]] | +0.61 | +0.42 / +0.65 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT3]] | -0.61 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[OXCT1]] | -0.60 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[PTGR2]] | -0.60 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SEPTIN11]] | -0.58 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[CHRAC1]] | -0.56 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SNX5]] | -0.56 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ANTXR1]] | -0.56 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ACADM]] | -0.56 | -0.20 / -0.53 | both halves | 7e-04 |  |
| [[TMX4]] | -0.56 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[IL6ST]] | -0.55 | -0.25 / -0.60 | both halves | 4e-04 |  |
| [[TMPO]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[HNRNPK]] | -0.54 | -0.36 / -0.43 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.4, -16.1); signed map (-24.0, 7.3). **Vector** length 80.7, 17.5% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +3.2 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +12.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.9 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.7 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | sirtuin 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,911,939-81,921,323 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sirtuins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRC8](https://www.uniprot.org/uniprotkb/Q9NRC8) (NAD-dependent protein deacetylase sirtuin-7):

> NAD-dependent protein-lysine deacylase that can act both as a deacetylase or deacylase (desuccinylase, depropionylase, deglutarylase and dedecanoylase), depending on the context. Specifically mediates deacetylation of histone H3 at 'Lys-18' (H3K18Ac). In contrast to other histone deacetylases, displays strong preference for a specific histone mark, H3K18Ac, directly linked to control of gene expression. H3K18Ac is mainly present around the transcription start site of genes and has been linked …

**Summary**, from NCBI Gene [51547](https://www.ncbi.nlm.nih.gov/gene/51547):

> This gene encodes a member of the sirtuin family of proteins, homologs to the yeast Sir2 protein. Members of the sirtuin family are characterized by a sirtuin core domain and grouped into four classes. The functions of human sirtuins have not yet been determined; however, yeast sirtuin proteins are known to regulate epigenetic gene silencing and suppress recombination of rDNA. Studies suggest that the human sirtuins may function as intracellular regulatory proteins with …

**Accessions** — [HGNC:14935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14935) · Entrez [51547](https://www.ncbi.nlm.nih.gov/gene/51547) · UniProt [Q9NRC8](https://www.uniprot.org/uniprotkb/Q9NRC8) · Ensembl [ENSG00000187531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187531)

## Data

Gene col 11919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11919); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11919]; `tensor/DDL_lfc|DDL_z.npy` [11919]; `embed/gene_vectors.npy` [11919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11919 or target_col == 11919). Every well: [[SIRT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIRT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
