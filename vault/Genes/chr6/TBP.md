---
symbol: "TBP"
type: "gene"
col: 3384
ensembl_id: "ENSG00000112592"
name: "TATA-box binding protein"
location: "6q27"
module: 89
arm: "+"
pooled_cpm: 24.81
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# TBP

*TATA-box binding protein* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.89× (z +14.4, q 2e-44, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.721× (z -7.5, q 5e-11, down in 26 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.866× (z -4.6, q 5e-04, down in 13 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (hTERT-HPNE 0.122×, HT-29 0.247×, SHP-77 0.259×, A549 0.226×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.0628×, A-427 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HepG2/C3A 0.140×, NCI-H2030 0.248×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.183×); [[Mifepristone (drug)]] 0.05 µM in 1 line (BT-474 0.162×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF5A]] (+0.68, fdr 7e-06), [[WDR53]] (+0.64, fdr 1e-05), [[POLR3F]] (+0.63, fdr 1e-05); moves opposite to [[TRAK1]] (-0.58, fdr 2e-05), [[HYCC1]] (-0.49, fdr 3e-04), [[CD83]] (-0.49, fdr 5e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +14.4 | 2e-44 | 42/47 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +12.8 | 3e-35 | 36/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +11.4 | 6e-28 | 32/48 (SW1417, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +9.8 | 1e-20 | 33/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +8.3 | 1e-14 | 25/47 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.44×** | +8.3 | 1e-14 | 34/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +8.3 | 1e-14 | 29/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +7.8 | 4e-13 | 31/47 (MIA PaCa-2, LoVo, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +7.4 | 7e-12 | 27/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +7.2 | 3e-11 | 26/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +6.9 | 2e-10 | 28/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +6.3 | 1e-08 | 21/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +5.6 | 1e-06 | 20/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +5.5 | 1e-06 | 23/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.29×** | +5.5 | 1e-06 | 20/48 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +4.5 | 2e-04 | 17/46 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.0 | 0.002 | 9/48 (SW1417, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.069 | 7/48 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3384.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (hTERT-HPNE 0.122×, HT-29 0.247×, SHP-77 0.259×, A549 0.226×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (KATO III 0.0628×, A-427 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HepG2/C3A 0.140×, NCI-H2030 0.248×; ⚠ toxic; transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.183×); [[Mifepristone (drug)]] 0.05 µM in 1 line (BT-474 0.162×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.721×** | -7.5 | 5e-11 | 26/42 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -6.2 | 2e-07 | 17/34 (hTERT-HPNE, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.800×** | -4.7 | 5e-04 | 16/38 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -4.6 | 5e-04 | 13/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -4.4 | 0.001 | 11/47 (HT-29, NCI-H23, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.864× | -3.3 | 0.087 | 3/48 (CHP-212, A-427, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 29.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.183× (z -8.9) |
| [[KATO III (line)]] | alt | 28.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.27× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0628× (z -22.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.4) | — |
| [[A-427 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -10.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.162× (z -8.9) |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0716× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -11.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.79× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 42.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.3) | — |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF5A]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[WDR53]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[POLR3F]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 | pathway: RNA Polymerase III Abortive And Retractive Initiation; STRING 902 |
| [[TMEM79]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[TMEM199]] | +0.62 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[TEFM]] | +0.61 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[BRAP]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[KRBOX4]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZSCAN25]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZNF791]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SLC25A17]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HYCC1]] | -0.49 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[CD83]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.1, 6.4); signed map (-9.6, -15.5). **Vector** length 60.6, 8.91% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +14.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +11.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.5 | +9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.5 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.7 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.4 | -7.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:170,554,302-170,572,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFIID, TBP1; previously GTF2D1, SCA17 |
| Gene groups (HGNC) | General transcription factors; General transcription factor IID complex subunits; General transcription factor IIIB complex subunits; TATA-box binding protein family |
| Reactome | 39 pathways, smallest: SIRT1 negatively regulates rRNA expression; RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [P20226](https://www.uniprot.org/uniprotkb/P20226) (TATA-box-binding protein):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. The TFIID complex …

**Summary**, from NCBI Gene [6908](https://www.ncbi.nlm.nih.gov/gene/6908):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11588) · Entrez [6908](https://www.ncbi.nlm.nih.gov/gene/6908) · UniProt [P20226](https://www.uniprot.org/uniprotkb/P20226) · Ensembl [ENSG00000112592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112592)

## Data

Gene col 3384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3384); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3384]; `tensor/DDL_lfc|DDL_z.npy` [3384]; `embed/gene_vectors.npy` [3384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3384 or target_col == 3384). Every well: [[TBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
