---
symbol: "ACTR1B"
type: "gene"
col: 3618
ensembl_id: "ENSG00000115073"
name: "actin related protein 1B"
location: "2q11.2"
module: 189
arm: "+"
pooled_cpm: 15.17
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# ACTR1B

*actin related protein 1B* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +10.9, q 5e-25, up in 30 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 3.37×, LoVo 5.59×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.491× (z -10.4, q 1e-22, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRNIP]] (+0.59, fdr 1e-05), [[ILK]] (+0.59, fdr 1e-05), [[FAM161B]] (+0.58, fdr 1e-05); moves opposite to [[TXN]] (-0.59, fdr 2e-05), [[MKRN5P]] (-0.56, fdr 3e-05), [[C1orf216]] (-0.55, fdr 1e-05).
> It is in [[Module 189]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3618.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 3.37×, LoVo 5.59×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +10.9 | 5e-25 | 30/37 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.3 | 6e-11 | 16/27 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.37×** | +4.6 | 8e-04 | 18/44 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +4.4 | 0.002 | 13/31 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | 1.50× | +3.1 | 0.22 | 5/43 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.491×** | -10.4 | 1e-22 | 38/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -10.3 | 2e-22 | 38/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.528×** | -9.3 | 2e-18 | 34/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.534×** | -9.2 | 8e-18 | 34/47 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -7.5 | 8e-12 | 27/46 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.600×** | -7.0 | 2e-10 | 27/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -6.7 | 1e-09 | 30/47 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.615×** | -6.7 | 1e-09 | 30/46 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.642×** | -6.5 | 6e-09 | 25/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -6.0 | 1e-07 | 34/48 (H4, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -5.7 | 5e-07 | 25/44 (A-427, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.721×** | -4.8 | 8e-05 | 16/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.536×** | -4.8 | 8e-05 | 17/37 (A498, J82, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.743×** | -4.3 | 6e-04 | 15/48 (SW 900, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.828×** | -3.9 | 0.003 | 18/48 (SNU-423, J82, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.766×** | -3.9 | 0.003 | 16/47 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.860× | -3.1 | 0.060 | 12/48 (HOP62, NCI-H460, …) | top dose only | position effect removed |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.799×** | -3.0 | 0.070 | 6/48 (SW48, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.807×** | -2.9 | 0.095 | 6/47 (HS-578T, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 34.8 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.256× (z -11.9) |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.208× (z -9.6) |
| [[A-427 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0860× (z -8.7) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.105× (z -9.3) ⚠ toxic; unreliable plate only |
| [[LoVo (line)]] | wt | 8.25 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.217× (z -8.9) |
| [[LS 180 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -10.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.182× (z -14.1) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.220× (z -8.7) |
| [[A-172 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRNIP]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ILK]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[FAM161B]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CEP63]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ACAP3]] | +0.57 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[HADHB]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[RING1]] | +0.56 | +0.57 / +0.37 | both halves | 8e-05 |  |
| [[UACA]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DNAL4]] | +0.55 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[PDLIM2]] | +0.55 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[EMC9]] | +0.54 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[FIBP]] | +0.53 | +0.46 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[MKRN5P]] | -0.56 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[C1orf216]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TRRAP]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[MGST1]] | -0.53 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TRMT11]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[COX10]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NAA50]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[EPM2A]] | -0.52 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[MCM9]] | -0.51 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[HSPE1]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LARP4]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.7, -33.6); signed map (-11.2, 17.0). **Vector** length 79.4, 16.1% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +10.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.1 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.3 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -4.4 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -9.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:97,655,939-97,664,044 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Arp1B; previously CTRN2 |
| Gene groups (HGNC) | Actin related proteins |
| Reactome | 7 pathways, smallest: Processing of antigen in germinal center B cells; MHC class II antigen presentation; Affinity selection of immunoglobulins |
| Matched by | ensembl_id |

**Function**, from UniProt [P42025](https://www.uniprot.org/uniprotkb/P42025) (Beta-centractin):

> Component of a multi-subunit complex involved in microtubule based vesicle motility. It is associated with the centrosome.

**Summary**, from NCBI Gene [10120](https://www.ncbi.nlm.nih.gov/gene/10120):

> This gene encodes a 42.3 kD subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein and is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positioning, and axonogenesis. This subunit, like ACTR1A, is an actin-related protein. These two proteins, which …

**Accessions** — [HGNC:168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:168) · Entrez [10120](https://www.ncbi.nlm.nih.gov/gene/10120) · UniProt [P42025](https://www.uniprot.org/uniprotkb/P42025) · Ensembl [ENSG00000115073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115073)

## Data

Gene col 3618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3618); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3618]; `tensor/DDL_lfc|DDL_z.npy` [3618]; `embed/gene_vectors.npy` [3618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3618 or target_col == 3618). Every well: [[ACTR1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
