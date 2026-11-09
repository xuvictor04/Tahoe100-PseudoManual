---
symbol: "DNAAF5"
type: "gene"
col: 9010
ensembl_id: "ENSG00000164818"
name: "dynein axonemal assembly factor 5"
location: "7p22.3"
module: 4
arm: "+"
pooled_cpm: 32.84
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DNAAF5

*dynein axonemal assembly factor 5* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.96× (z +16.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.679× (z -10.8, q 1e-24, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1A]] (+0.71, fdr 7e-06), [[TOMM40]] (+0.69, fdr 7e-06), [[EFTUD2]] (+0.66, fdr 7e-06); moves opposite to [[ABI1]] (-0.61, fdr 2e-05), [[CHMP2B]] (-0.58, fdr 1e-05), [[OAZ1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.96×** | +16.4 | 0e+00 | 46/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.20×** | +11.9 | 2e-30 | 40/48 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +8.6 | 2e-15 | 37/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +5.5 | 4e-06 | 20/48 (AsPC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.33×** | +5.2 | 2e-05 | 19/47 (SW48, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 1e-04 | 21/48 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +4.8 | 1e-04 | 17/40 (SNU-423, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.7 | 2e-04 | 20/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 0.001 | 17/48 (H4, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.2 | 0.001 | 20/43 (AsPC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.005 | 18/48 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | **1.22×** | +3.7 | 0.012 | 16/39 (LS 180, LOX-IMVI, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.019 | 13/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.4 | 0.031 | 11/30 (NCI-H1792, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.075 | 12/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.075 | 15/48 (LOX-IMVI, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.679×** | -10.8 | 1e-24 | 42/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.736×** | -6.1 | 3e-07 | 26/48 (C-33 A, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.793×** | -4.6 | 7e-04 | 23/48 (SW48, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.796×** | -4.5 | 8e-04 | 21/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.803×** | -4.2 | 0.003 | 18/47 (RPMI-7951, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.811×** | -4.0 | 0.005 | 18/47 (SW480, SNU-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.6 | 0.024 | 18/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.848× | -3.3 | 0.071 | 10/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.858× | -3.1 | 0.11 | 8/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.852× | -3.1 | 0.11 | 18/48 (A-172, NCI-H23, …) | two highest doses | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.858× | -3.1 | 0.11 | 10/48 (KATO III, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 32.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +20.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.360× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 41.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 57.4 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.76× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 74.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.46× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 39.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.02× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.275× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[A-427 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -11.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 27.8 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0978× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0871× (z -9.6) |
| [[LoVo (line)]] | wt | 32.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.32× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 33.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.36× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 32.8 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.220× (z -10.1) |
| [[SHP-77 (line)]] | alt | 63.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.82× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 48.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.265× (z -8.6) |
| [[SW480 (line)]] | alt | 46.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.87× (z +9.5) | — |
| [[A-172 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1A]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PPAN]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[LSG1]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[NUP155]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[PFAS]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[CHID1]] | +0.64 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[ZNF202]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[TSR1]] | +0.63 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[GCN1]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABI1]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CHMP2B]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[OAZ1]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PEAK1]] | -0.57 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PNRC1]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[CDKN1C]] | -0.56 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[UBE2B]] | -0.56 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[DAAM1]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-14.0, -34.8); signed map (-4.4, -47.0). **Vector** length 95.3, 20.2% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +16.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +11.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | +3.1 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +4.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +5.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.1 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.1 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal assembly factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:726,699-786,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20397, FLJ31671, FLJ39381, FLJ25564, CILD18; previously HEATR2 |
| Gene groups (HGNC) | TOG domain containing; Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y56](https://www.uniprot.org/uniprotkb/Q86Y56) (Dynein axonemal assembly factor 5):

> Cytoplasmic protein involved in the delivery of the dynein machinery to the motile cilium. It is required for the assembly of the axonemal dynein inner and outer arms, two structures attached to the peripheral outer doublet A microtubule of the axoneme, that play a crucial role in cilium motility.

**Summary**, from NCBI Gene [54919](https://www.ncbi.nlm.nih.gov/gene/54919):

> The protein encoded by this gene is essential for the preassembly or stability of axonemal dynein arms, and is found only in organisms with motile cilia and flagella. Mutations in this gene are associated with primary ciliary dyskinesia-18, a disorder characterized by abnormalities of motile cilia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:26013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26013) · Entrez [54919](https://www.ncbi.nlm.nih.gov/gene/54919) · UniProt [Q86Y56](https://www.uniprot.org/uniprotkb/Q86Y56) · Ensembl [ENSG00000164818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164818)

## Data

Gene col 9010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9010); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9010]; `tensor/DDL_lfc|DDL_z.npy` [9010]; `embed/gene_vectors.npy` [9010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9010 or target_col == 9010). Every well: [[DNAAF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAAF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
