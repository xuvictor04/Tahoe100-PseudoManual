---
symbol: "CDK5RAP1"
type: "gene"
col: 2129
ensembl_id: "ENSG00000101391"
name: "CDK5RAP1 mitochondrial tRNA methylthiotransferase"
location: "20q11.21"
module: 30
arm: "+"
pooled_cpm: 35.27
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CDK5RAP1

*CDK5RAP1 mitochondrial tRNA methylthiotransferase* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.73× (z +10.1, q 2e-21, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.590× (z -9.8, q 6e-20, down in 34 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.227×, HOP62 0.259×, A498 0.262×, SNU-423 0.206×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.217×, RPMI-7951 0.177×, SNU-423 0.240×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.243×, J82 0.359×, SW1417 0.328×; ⚠ toxic; transcription drop); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0625×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (CHP-212 0.0814×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMF1]] (+0.75, fdr 7e-06), [[DHX57]] (+0.74, fdr 7e-06), [[GTF3C2]] (+0.74, fdr 7e-06); moves opposite to [[HIVEP2-DT]] (-0.67, fdr 7e-06), [[SKIL]] (-0.67, fdr 1e-05), [[SGO1-AS1]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +10.1 | 2e-21 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +9.5 | 9e-19 | 41/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +9.1 | 2e-17 | 40/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +8.9 | 1e-16 | 40/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +7.9 | 3e-13 | 40/48 (KATO III, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.8 | 9e-10 | 32/47 (NCI-H2030, COLO 205, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +6.8 | 9e-10 | 34/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +6.3 | 3e-08 | 29/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +5.4 | 5e-06 | 28/48 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +5.3 | 7e-06 | 24/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 15/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.7 | 0.011 | 19/48 (SW480, NCI-H23, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.21×** | +3.6 | 0.016 | 17/48 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.20×** | +3.4 | 0.024 | 17/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.4 | 0.028 | 10/48 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.088 | 11/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.094 | 14/47 (SW480, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2129.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 0.227×, HOP62 0.259×, A498 0.262×, SNU-423 0.206×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.217×, RPMI-7951 0.177×, SNU-423 0.240×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.243×, J82 0.359×, SW1417 0.328×; ⚠ toxic; transcription drop); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0625×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (CHP-212 0.0814×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.590×** | -9.8 | 6e-20 | 34/47 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -9.7 | 1e-19 | 27/37 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.634×** | -7.8 | 9e-13 | 24/42 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -3.7 | 0.028 | 0/48 | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.886× | -3.2 | 0.16 | 7/48 (A498, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 39.3 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 39.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 62.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -11.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 34.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 2 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0625× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 38.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -9.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -12.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 77.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 47.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMF1]] | +0.75 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[DHX57]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[GTF3C2]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[AP3S2]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[E4F1]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[SNRNP40]] | +0.72 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[PARGP1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[NDUFB7]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[MMS19]] | +0.69 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[NSFP1]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TAB1]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CCZ1B]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2-DT]] | -0.67 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[SKIL]] | -0.67 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.63 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[TUG1]] | -0.63 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[ABCA10]] | -0.63 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[HIVEP2]] | -0.61 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.61 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[LEKR1]] | -0.61 | -0.58 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-5.9, -16.3); signed map (-17.6, -18.7). **Vector** length 98.2, 23.1% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.8 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.4 | -9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.2 | -9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | CDK5RAP1 mitochondrial tRNA methylthiotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:33,358,839-33,401,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-05, HSPC167, C42; previously C20orf34 |
| Gene groups (HGNC) | Radical S-adenosylmethionine domain containing; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SZ6](https://www.uniprot.org/uniprotkb/Q96SZ6) (Mitochondrial tRNA methylthiotransferase CDK5RAP1):

> Methylthiotransferase that catalyzes the conversion of N6-(dimethylallyl)adenosine (i(6)A) to 2-methylthio-N6-(dimethylallyl)adenosine (ms(2)i(6)A) at position 37 (adjacent to the 3'-end of the anticodon) of four mitochondrial DNA-encoded tRNAs (Ser(UCN), Phe, Tyr and Trp). Essential for efficient and highly accurate protein translation by the ribosome. Specifically inhibits CDK5 activation by CDK5R1. Essential for efficient mitochondrial protein synthesis and respiratory chain; shows …

**Summary**, from NCBI Gene [51654](https://www.ncbi.nlm.nih.gov/gene/51654):

> This gene encodes a regulator of cyclin-dependent kinase 5 activity. This protein has also been reported to modify RNA by adding a methylthio-group and may thus have a dual function as an RNA methylthiotransferase and as an inhibitor of cyclin-dependent kinase 5 activity. Alternative splicing results in multiple transcript variants that encode different isoforms. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:15880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15880) · Entrez [51654](https://www.ncbi.nlm.nih.gov/gene/51654) · UniProt [Q96SZ6](https://www.uniprot.org/uniprotkb/Q96SZ6) · Ensembl [ENSG00000101391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101391)

## Data

Gene col 2129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2129); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2129]; `tensor/DDL_lfc|DDL_z.npy` [2129]; `embed/gene_vectors.npy` [2129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2129 or target_col == 2129). Every well: [[CDK5RAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK5RAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
