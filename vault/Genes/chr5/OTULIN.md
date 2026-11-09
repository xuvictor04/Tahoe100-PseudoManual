---
symbol: "OTULIN"
type: "gene"
col: 7773
ensembl_id: "ENSG00000154124"
name: "OTU deubiquitinase with linear linkage specificity"
location: "5p15.2"
module: 30
arm: "+"
pooled_cpm: 54.04
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# OTULIN

*OTU deubiquitinase with linear linkage specificity* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.78× (z +8.8, q 6e-16, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.569× (z -9.1, q 5e-17, down in 35 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.179×, A549 0.275×, NCI-H2347 0.312×, SK-MEL-2 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.156×, A498 0.311×, NCI-H2347 0.329×, Panc 03.27 0.270×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.156×, NCI-H2030 0.422×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTCA]] (+0.73, fdr 7e-06), [[ZW10]] (+0.69, fdr 2e-05), [[RAB18]] (+0.68, fdr 9e-06); moves opposite to [[ERCC6L2]] (-0.63, fdr 1e-05), [[ZNF335]] (-0.63, fdr 7e-06), [[PER2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +8.8 | 6e-16 | 45/48 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +8.7 | 7e-16 | 45/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +7.2 | 9e-11 | 40/48 (HOP62, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +6.0 | 3e-07 | 34/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.6 | 2e-06 | 29/48 (RKO, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +5.2 | 2e-05 | 32/48 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.9 | 9e-05 | 31/45 (SNU-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.5 | 4e-04 | 28/47 (COLO 205, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.4 | 8e-04 | 22/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.003 | 22/48 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.018 | 21/49 (CFPAC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.047 | 14/48 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.092 | 6/48 (A498, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7773.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.179×, A549 0.275×, NCI-H2347 0.312×, SK-MEL-2 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.156×, A498 0.311×, NCI-H2347 0.329×, Panc 03.27 0.270×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.156×, NCI-H2030 0.422×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.569×** | -9.1 | 5e-17 | 35/49 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -7.3 | 6e-11 | 28/39 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -4.9 | 2e-04 | 3/49 (SW48, NCI-H661, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.801×** | -3.6 | 0.036 | 24/48 (RPMI-7951, BT-474, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.801×** | -3.6 | 0.036 | 24/48 (NCI-H23, NCI-H1573, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.802×** | -3.6 | 0.036 | 19/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.859× | -3.5 | 0.043 | 14/48 (A498, AN3 CA, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **0.794×** | -3.4 | 0.043 | 21/44 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 95.2 | 1 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.38× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 79.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -10.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -16.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -11.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[C32 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -8.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 37.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.33× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[HS-578T (line)]] | alt | 78.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -9.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[NCI-H1792 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -22.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -16.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 44.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.73× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 68.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTCA]] | +0.73 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[ZW10]] | +0.69 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[RAB18]] | +0.68 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[CACYBP]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ATP2C1]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.65 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[NAPB]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[MBD2]] | +0.65 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[STAM]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[GDAP2]] | +0.64 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[USP35]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[RNF216P1]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.63 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[ZNF335]] | -0.63 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[PER2]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[HELQ]] | -0.59 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[BPTF]] | -0.59 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[LRCH3]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[EP300]] | -0.57 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[PFN1]] | -0.57 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[ARMH4]] | -0.57 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[KDSR]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[POLR2L]] | -0.56 | -0.68 / -0.46 | both halves | 2e-05 |  |
| [[IBA57]] | -0.56 | -0.56 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-9.5, -11.0); signed map (-34.2, -16.6). **Vector** length 104, 26.3% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.5 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.8 | +7.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.8 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -7.2 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.7 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -6.6 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase with linear linkage specificity |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:14,664,664-14,699,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34884; previously FAM105B |
| Gene groups (HGNC) | OTU domain containing |
| Reactome | 5 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Regulation of TNFR1 signaling; TNF signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BN8](https://www.uniprot.org/uniprotkb/Q96BN8) (Ubiquitin thioesterase otulin):

> Deubiquitinase that specifically removes linear ('Met-1'-linked) polyubiquitin chains to substrates and acts as a regulator of angiogenesis and innate immune response. Required during angiogenesis, craniofacial and neuronal development by regulating the canonical Wnt signaling together with the LUBAC complex. Acts as a negative regulator of NF-kappa-B by regulating the activity of the LUBAC complex. OTULIN function is mainly restricted to homeostasis of the LUBAC complex: acts by removing …

**Summary**, from NCBI Gene [90268](https://www.ncbi.nlm.nih.gov/gene/90268):

> This gene encodes a member of the peptidase C65 family of ubiquitin isopeptidases. Members of this family remove ubiquitin from proteins. The encoded enzyme specifically recognizes and removes M1(Met1)-linked, or linear, ubiquitin chains from protein substrates. Linear ubiquitin chains are known to regulate the NF-kappa B signaling pathway in the context of immunity and inflammation. Mutations in this gene cause a potentially fatal autoinflammatory syndrome in human patients. [provided by …

**Accessions** — [HGNC:25118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25118) · Entrez [90268](https://www.ncbi.nlm.nih.gov/gene/90268) · UniProt [Q96BN8](https://www.uniprot.org/uniprotkb/Q96BN8) · Ensembl [ENSG00000154124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154124)

## Data

Gene col 7773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7773); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7773]; `tensor/DDL_lfc|DDL_z.npy` [7773]; `embed/gene_vectors.npy` [7773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7773 or target_col == 7773). Every well: [[OTULIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTULIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
