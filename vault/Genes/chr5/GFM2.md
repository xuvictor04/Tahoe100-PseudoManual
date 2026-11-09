---
symbol: "GFM2"
type: "gene"
col: 8937
ensembl_id: "ENSG00000164347"
name: "GTP dependent ribosome recycling factor mitochondrial GFM2"
location: "5q13.3"
module: 25
arm: "+"
pooled_cpm: 36.04
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GFM2

*GTP dependent ribosome recycling factor mitochondrial GFM2* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.89× (z +14.2, q 5e-43, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.712× (z -7.6, q 2e-11, down in 28 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.757× (z -6.2, q 1e-07, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.394×, SK-MEL-2 0.323×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.151×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.392×); [[OTS514 (drug)]] 5 µM in 1 line (COLO 205 0.0871×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYZ]] (+0.72, fdr 7e-06), [[GPN1]] (+0.71, fdr 7e-06), [[AP3M1]] (+0.70, fdr 7e-06); moves opposite to [[PKNOX1]] (-0.62, fdr 1e-05), [[TNRC6C]] (-0.58, fdr 1e-05), [[RELB]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +14.2 | 5e-43 | 44/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +13.5 | 5e-39 | 39/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +13.4 | 8e-39 | 44/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +12.5 | 6e-34 | 43/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +10.8 | 4e-25 | 38/48 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +9.6 | 1e-19 | 36/48 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +9.0 | 2e-17 | 35/48 (PANC-1, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +8.3 | 7e-15 | 33/48 (NCI-H1573, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +8.2 | 1e-14 | 32/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +8.2 | 1e-14 | 35/48 (A-427, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.8 | 7e-10 | 17/38 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +6.2 | 2e-08 | 30/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **1.65×** | +5.8 | 2e-07 | 23/47 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +5.6 | 8e-07 | 20/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +5.5 | 1e-06 | 27/48 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.3 | 7e-04 | 13/48 (HEC-1-A, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.001 | 19/48 (HOP62, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8937.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.394×, SK-MEL-2 0.323×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.151×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.392×); [[OTS514 (drug)]] 5 µM in 1 line (COLO 205 0.0871×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.712×** | -7.6 | 2e-11 | 28/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.757×** | -6.2 | 1e-07 | 21/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.801×** | -4.9 | 1e-04 | 20/48 (NCI-H460, AN3 CA, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -3.7 | 0.027 | 17/48 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.849× | -3.7 | 0.028 | 13/48 (NCI-H1792, SNU-423, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | 0.856× | -3.5 | 0.050 | 16/47 (HS-578T, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.081 | 9/48 (HCT15, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.866× | -3.2 | 0.088 | 17/48 (A498, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.863× | -3.2 | 0.094 | 19/48 (NCI-H460, PANC-1, …) | two highest doses | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.906× | -3.1 | 0.097 | 11/48 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.825× | -3.1 | 0.11 | 10/47 (C32, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.909× | -3.0 | 0.12 | 8/48 (HS-578T, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -16.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.392× (z -11.6) |
| [[LoVo (line)]] | wt | 43.4 | 5 | 0 | [[Auranofin (drug)]] 5 µM 2.76× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 24.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 16.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +8.8) | — |
| [[A498 (line)]] | wt | 40.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.20× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 18.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.55× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 38.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.112× (z -9.5) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 40.7 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0871× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 31.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.30× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 35.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.34× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[PANC-1 (line)]] | alt | 33.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.06× (z +8.6) | — |
| [[RKO (line)]] | wt | 48.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.71× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -17.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 60.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.27× (z +9.9) | — |
| [[A-172 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZ]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[GPN1]] | +0.71 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[AP3M1]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[RTF2]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[SUDS3]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SAMM50]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[OPA1]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[GTF3C3]] | +0.66 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GDAP2]] | +0.65 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.64 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[VTI1B]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKNOX1]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RELB]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ERF]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SERTAD1]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[PIM3]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[APLF]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[HES4]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[LRCH3]] | -0.53 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[FAM193A]] | -0.53 | -0.43 / -0.44 | both halves | 4e-05 |  |
| [[HLA-B]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[EPOP]] | -0.53 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.1, -13.3); signed map (-29.9, -28.6). **Vector** length 95.8, 21.7% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.2 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +13.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +8.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +9.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | GTP dependent ribosome recycling factor mitochondrial GFM2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:74,721,206-74,767,147 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mtEFG2, EFG2, FLJ21661, EF-G2mt |
| Gene groups (HGNC) | Translational GTPases |
| Reactome | 3 pathways, smallest: Mitochondrial translation termination; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969S9](https://www.uniprot.org/uniprotkb/Q969S9) (Ribosome-releasing factor 2, mitochondrial):

> Mitochondrial GTPase that mediates the disassembly of ribosomes from messenger RNA at the termination of mitochondrial protein biosynthesis. Acts in collaboration with MRRF. Promotes mitochondrial ribosome recycling by dissolution of intersubunit contacts. GTP hydrolysis follows the ribosome disassembly and probably occurs on the ribosome large subunit. Not involved in the GTP-dependent ribosomal translocation step during translation elongation.

**Summary**, from NCBI Gene [84340](https://www.ncbi.nlm.nih.gov/gene/84340):

> Eukaryotes contain two protein translational systems, one in the cytoplasm and one in the mitochondria. Mitochondrial translation is crucial for maintaining mitochondrial function and mutations in this system lead to a breakdown in the respiratory chain-oxidative phosphorylation system and to impaired maintenance of mitochondrial DNA. This gene encodes one of the mitochondrial translation elongation factors, which is a GTPase that plays a role at the termination of mitochondrial translation by …

**Accessions** — [HGNC:29682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29682) · Entrez [84340](https://www.ncbi.nlm.nih.gov/gene/84340) · UniProt [Q969S9](https://www.uniprot.org/uniprotkb/Q969S9) · Ensembl [ENSG00000164347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164347)

## Data

Gene col 8937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8937); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8937]; `tensor/DDL_lfc|DDL_z.npy` [8937]; `embed/gene_vectors.npy` [8937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8937 or target_col == 8937). Every well: [[GFM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
