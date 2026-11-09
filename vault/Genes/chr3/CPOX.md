---
symbol: "CPOX"
type: "gene"
col: 1291
ensembl_id: "ENSG00000080819"
name: "coproporphyrinogen oxidase"
location: "3q11.2"
module: 88
arm: "-"
pooled_cpm: 38.38
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# CPOX

*coproporphyrinogen oxidase* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.20× (z +4.9, q 6e-04, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.412× (z -23.3, q 0e+00, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF511]] (+0.65, fdr 1e-05), [[NFRKB]] (+0.60, fdr 3e-05), [[VDAC3]] (+0.59, fdr 1e-05); moves opposite to [[SDCBP2-AS1]] (-0.62, fdr 1e-05), [[RAB30-DT]] (-0.60, fdr 4e-05), [[LINC00174]] (-0.58, fdr 2e-05).
> It sits in the **-** arm of [[Module 088]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.9 | 6e-04 | 21/47 (SW480, SNU-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.59×** | +4.5 | 0.002 | 21/45 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.010 | 17/47 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.022 | 15/44 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | 1.19× | +3.3 | 0.098 | 18/43 (SW480, RPMI-7951, …) | two highest doses | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.098 | 14/47 (SW480, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.412×** | -23.3 | 0e+00 | 38/46 (Hs 766T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.443×** | -14.5 | 1e-45 | 34/47 (Hs 766T, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -13.2 | 2e-37 | 34/46 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.671×** | -7.4 | 2e-11 | 26/47 (SW 900, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -6.8 | 1e-09 | 23/46 (SW48, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -6.8 | 1e-09 | 32/47 (Hs 766T, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.747×** | -5.4 | 5e-06 | 22/45 (SW 900, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.757×** | -5.2 | 2e-05 | 22/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.595×** | -5.0 | 3e-05 | 23/45 (NCI-H2347, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -4.3 | 9e-04 | 1/47 (SW 1271) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.796×** | -4.1 | 0.003 | 16/46 (RKO, H4, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.807×** | -4.0 | 0.004 | 17/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.029 | 7/46 (SNU-1, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.2 | 0.048 | 18/47 (SW48, Hs 766T, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.834× | -3.2 | 0.049 | 19/45 (H4, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 102 | 0 | 28 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -26.3) |
| [[SW48 (line)]] | wt | 448 | 0 | 13 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0756× (z -22.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -21.0) |
| [[SW 900 (line)]] | alt | 44.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -20.8) |
| [[LoVo (line)]] | wt | 41.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.0) |
| [[A-172 (line)]] | wt | 34.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -16.6) |
| [[A-427 (line)]] | wt | 296 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 68.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -15.1) |
| [[PANC-1 (line)]] | alt | 13.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.0) |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0454× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0981× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 46.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -22.5) |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 27.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.7) |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -8.6) |
| [[HCT15 (line)]] | alt | 41.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -16.8) |
| [[HS-578T (line)]] | alt | 49.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.5) |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.9) |
| [[KATO III (line)]] | alt | 26.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -10.4) |
| [[A498 (line)]] | wt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.1) |
| [[A549 (line)]] | wt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.9) |
| [[C32 (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -15.7) |
| [[LOX-IMVI (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.5) |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.0) |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF511]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NFRKB]] | +0.60 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[VDAC3]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[MFSD9]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[FAM102B]] | +0.58 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[ATP8A1]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[STN1]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.58 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ATG4C]] | +0.58 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[ARHGEF26]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[LPCAT4]] | +0.57 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[NIPA1]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP2-AS1]] | -0.62 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.60 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[LINC00174]] | -0.58 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[PPP3CB-AS1]] | -0.58 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.57 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[R3HDM2]] | -0.56 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[CHMP4A]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[ST7L]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[CHMP3]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[GABPB2]] | -0.55 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[PDCL3P4]] | -0.55 | -0.57 / -0.37 | both halves | 9e-05 |  |
| [[ACYP2]] | -0.55 | -0.57 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (5.8, 7.2); signed map (-35.3, -5.6). **Vector** length 87.1, 17.7% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.8 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -23.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -13.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -6.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | coproporphyrinogen oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:98,579,446-98,593,648 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPX, HCP; previously CPO |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM, HEME_METABOLISM |
| Reactome | 2 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [P36551](https://www.uniprot.org/uniprotkb/P36551) (Oxygen-dependent coproporphyrinogen-III oxidase, mitochondrial):

> Catalyzes the aerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen-III to yield the vinyl groups in protoporphyrinogen-IX and participates to the sixth step in the heme biosynthetic pathway.

**Summary**, from NCBI Gene [1371](https://www.ncbi.nlm.nih.gov/gene/1371):

> The protein encoded by this gene is the sixth enzyme of the heme biosynthetic pathway. The encoded enzyme is soluble and found in the intermembrane space of mitochondria. This enzyme catalyzes the stepwise oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX, a precursor of heme. Defects in this gene are a cause of hereditary coproporphyria (HCP).[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:2321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2321) · Entrez [1371](https://www.ncbi.nlm.nih.gov/gene/1371) · UniProt [P36551](https://www.uniprot.org/uniprotkb/P36551) · Ensembl [ENSG00000080819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080819)

## Data

Gene col 1291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1291); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1291]; `tensor/DDL_lfc|DDL_z.npy` [1291]; `embed/gene_vectors.npy` [1291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1291 or target_col == 1291). Every well: [[CPOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
