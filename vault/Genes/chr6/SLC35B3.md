---
symbol: "SLC35B3"
type: "gene"
col: 4571
ensembl_id: "ENSG00000124786"
name: "solute carrier family 35 member B3"
location: "6p24.3"
module: 23
arm: "+"
pooled_cpm: 26.6
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SLC35B3

*solute carrier family 35 member B3* — 6p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.66× (z +7.9, q 2e-12, up in 32 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.27× (z +3.9, q 0.030, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.554× (z -9.6, q 5e-19, down in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.584× (z -8.7, q 4e-16, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSTO1]] (+0.62, fdr 1e-05), [[PRANCR]] (+0.59, fdr 1e-05), [[KLRA1P]] (+0.59, fdr 3e-05); moves opposite to [[PADI2]] (-0.49, fdr 1e-04), [[STOX2]] (-0.49, fdr 7e-05), [[MAPT]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +7.9 | 2e-12 | 32/46 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.030 | 16/48 (J82, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.057 | 18/48 (LS 180, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.26×** | +3.4 | 0.085 | 11/48 (HEC-1-A, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.085 | 11/47 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.48×** | +3.3 | 0.087 | 10/47 (AsPC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.089 | 15/48 (HEC-1-A, HT-29, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.554×** | -9.6 | 5e-19 | 36/48 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.559×** | -9.5 | 8e-19 | 34/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.584×** | -8.7 | 4e-16 | 40/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.591×** | -8.2 | 4e-14 | 32/48 (SW48, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -7.2 | 5e-11 | 37/48 (PANC-1, H4, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.630×** | -7.2 | 6e-11 | 30/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -6.0 | 2e-07 | 29/47 (RPMI-7951, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.699×** | -5.6 | 1e-06 | 26/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.707×** | -5.4 | 4e-06 | 26/48 (HOP62, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.695×** | -5.3 | 7e-06 | 28/48 (Hs 766T, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.818×** | -4.6 | 2e-04 | 21/47 (AsPC-1, hTERT-HPNE, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **0.762×** | -4.3 | 1e-03 | 20/47 (LoVo, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.772×** | -4.2 | 0.001 | 23/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.679×** | -3.3 | 0.041 | 14/41 (HS-578T, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 20.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0721× (z -10.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.356× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.271× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 31.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0392× (z -11.9) |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.204× (z -9.6) |
| [[SW1417 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.60× (z +9.7) ⚠ toxic | — |
| [[SW48 (line)]] | wt | 22.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.111× (z -9.7) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSTO1]] | +0.62 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PRANCR]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[KLRA1P]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[CHD1-DT]] | +0.57 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[HEXIM2-AS1]] | +0.57 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ZNF213-AS1]] | +0.56 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[TAS2R4]] | +0.56 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[ANKRD17-DT]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[FAM149B1]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[UGDH-AS1]] | +0.55 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[ZNF596]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PADI2]] | -0.49 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[STOX2]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[MAPT]] | -0.48 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[RERE]] | -0.48 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[EDA]] | -0.48 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[MAGI1]] | -0.47 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[PTPN3]] | -0.47 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[VEZT]] | -0.47 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[RORA]] | -0.46 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[ARHGAP44]] | -0.46 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[RGS2]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.0, 17.6); signed map (26.4, -7.5). **Vector** length 81.0, 16.5% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.6 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | -0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.4 | -8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -8.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.3 — chr6:8,411,435-8,435,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-19, dJ453H5.1, PAPST2; previously C6orf196 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Reactome | 7 pathways, smallest: Transport and metabolism of PAPS; Transport of nucleotide sugars; Transport of vitamins, nucleosides, and related molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1N7](https://www.uniprot.org/uniprotkb/Q9H1N7) (Adenosine 3'-phospho 5'-phosphosulfate transporter 2):

> Probably functions as a 3'-phosphoadenylyl sulfate:adenosine 3',5'-bisphosphate antiporter at the Golgi membranes. Mediates the transport from the cytosol into the lumen of the Golgi of 3'-phosphoadenylyl sulfate/adenosine 3'-phospho 5'-phosphosulfate (PAPS), a universal sulfuryl donor for sulfation events that take place in that compartment.

**Summary**, from NCBI Gene [51000](https://www.ncbi.nlm.nih.gov/gene/51000):

> This gene is a member of the solute carrier family. The encoded protein is involved in the transport of 3-prime phosphoadenosine 5-prime phosphosulfate (PAPS) from the nucleus or the cytosol to the Golgi lumen. This gene has been reported to be expressed preferentially in the human colon tissues. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:21601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21601) · Entrez [51000](https://www.ncbi.nlm.nih.gov/gene/51000) · UniProt [Q9H1N7](https://www.uniprot.org/uniprotkb/Q9H1N7) · Ensembl [ENSG00000124786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124786)

## Data

Gene col 4571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4571); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4571]; `tensor/DDL_lfc|DDL_z.npy` [4571]; `embed/gene_vectors.npy` [4571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4571 or target_col == 4571). Every well: [[SLC35B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
