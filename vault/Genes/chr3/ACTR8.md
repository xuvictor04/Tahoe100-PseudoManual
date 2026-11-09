---
symbol: "ACTR8"
type: "gene"
col: 3506
ensembl_id: "ENSG00000113812"
name: "actin related protein 8"
location: "3p21.1"
module: 7
arm: "+"
pooled_cpm: 10.23
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ACTR8

*actin related protein 8* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.39× (z +7.8, q 4e-12, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.686× (z -6.2, q 3e-07, down in 21 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.834× (z -4.2, q 0.007, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.114×, hTERT-HPNE 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HCT15 0.0712×); [[Pimozide (drug)]] 0.5 µM in 1 line (RKO 0.0970×; ⚠ transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (A549 0.0880×); [[crizotinib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0916×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL9]] (+0.74, fdr 7e-06), [[ERAL1]] (+0.70, fdr 7e-06), [[ZXDB]] (+0.70, fdr 7e-06); moves opposite to [[SLC25A5]] (-0.63, fdr 1e-05), [[PTMA]] (-0.59, fdr 1e-05), [[UBL5]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +7.8 | 4e-12 | 20/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +6.9 | 1e-09 | 21/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 3e-08 | 20/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +6.3 | 4e-08 | 17/46 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.8 | 9e-07 | 18/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.6 | 4e-04 | 11/38 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.26×** | +3.8 | 0.011 | 11/45 (SW480, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3506.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.114×, hTERT-HPNE 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HCT15 0.0712×); [[Pimozide (drug)]] 0.5 µM in 1 line (RKO 0.0970×; ⚠ transcription drop); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (A549 0.0880×); [[crizotinib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0916×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -6.2 | 3e-07 | 21/46 (C-33 A, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -4.2 | 0.007 | 16/48 (KATO III, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.783×** | -4.0 | 0.010 | 12/45 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.789×** | -3.9 | 0.010 | 10/48 (NCI-H1573, AsPC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.789×** | -3.9 | 0.010 | 12/46 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.863× | -3.4 | 0.054 | 17/43 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.831× | -3.1 | 0.15 | 6/46 (AN3 CA, NCI-H2030, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.15 | 6/44 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 6.63 | 0 | 2 | — | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.0722× (z -9.6) |
| [[A-427 (line)]] | wt | 9.40 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.156× (z -9.3) |
| [[A549 (line)]] | wt | 6.96 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0880× (z -10.7) |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -10.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 6.20 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -10.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0712× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0916× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 5.18 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0871× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 7.76 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0970× (z -10.8) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL9]] | +0.74 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[ERAL1]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.70 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[RIMOC1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[AUP1]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[SRP68]] | +0.66 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[PARP3]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SNX17]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PRMT5]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SLC25A46]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TRUB1]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RNF6]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A5]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PTMA]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[UBL5]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ATP5F1E]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PTMAP2]] ⚠ | -0.58 | -0.59 / -0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6A1]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[IGFBP2]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[RPLP2]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[COX6C]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[RPL23A]] | -0.55 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[METRN]] | -0.55 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[LRRC75A]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.1, 12.9); signed map (3.8, -30.5). **Vector** length 60.5, 8.23% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.8 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.3 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,867,066-53,882,152 (-) |
| Ensembl biotype | protein_coding |
| Also known as | INO80N, ARP8 |
| Gene groups (HGNC) | INO80 complex subunits; Actin related proteins |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H981](https://www.uniprot.org/uniprotkb/Q9H981) (Actin-related protein 8):

> Plays an important role in the functional organization of mitotic chromosomes. Exhibits low basal ATPase activity, and unable to polymerize.; Proposed core component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair. Required for the recruitment of INO80 (and probably the INO80 complex) to sites of DNA damage. Strongly prefer nucleosomes and H3-H4 tetramers over H2A-H2B dimers, suggesting it may act as a nucleosome …

**Summary**, from NCBI Gene [93973](https://www.ncbi.nlm.nih.gov/gene/93973):

> Predicted to enable mRNA binding activity. Involved in several processes, including positive regulation of DNA-templated transcription; regulation of DNA metabolic process; and regulation of chromosome organization. Located in nucleoplasm. Part of Ino80 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14672) · Entrez [93973](https://www.ncbi.nlm.nih.gov/gene/93973) · UniProt [Q9H981](https://www.uniprot.org/uniprotkb/Q9H981) · Ensembl [ENSG00000113812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113812)

## Data

Gene col 3506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3506); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3506]; `tensor/DDL_lfc|DDL_z.npy` [3506]; `embed/gene_vectors.npy` [3506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3506 or target_col == 3506). Every well: [[ACTR8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
