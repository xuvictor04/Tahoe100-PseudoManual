---
symbol: "SACM1L"
type: "gene"
col: 13063
ensembl_id: "ENSG00000211456"
name: "SAC1 like phosphatidylinositide phosphatase"
location: "3p21.31"
module: 171
arm: "+"
pooled_cpm: 53.96
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# SACM1L

*SAC1 like phosphatidylinositide phosphatase* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 1.55× (z +3.7, q 0.077, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 2.99×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.787× (z -5.6, q 2e-05, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (HepG2/C3A 0.103×, C-33 A 0.160×, hTERT-HPNE 0.154×, NCI-H1573 0.223×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 0.414×, A498 0.490×, NCI-H2347 0.568×, A549 0.500×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.173×, SW1417 0.309×, NCI-H460 0.392×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AN3 CA 0.0725×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRS2]] (+0.68, fdr 7e-06), [[SEPTIN7P2]] (+0.64, fdr 1e-05), [[SPAST]] (+0.64, fdr 7e-06); moves opposite to [[KCTD11]] (-0.61, fdr 7e-06), [[DPH1-AS1]] (-0.58, fdr 1e-05), [[KDM6B]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13063.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 2.99×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.077 | 22/48 (KATO III, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +3.6 | 0.077 | 23/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.22× | +3.3 | 0.18 | 19/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.21× | +3.2 | 0.20 | 16/48 (HEC-1-A, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13063.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (HepG2/C3A 0.103×, C-33 A 0.160×, hTERT-HPNE 0.154×, NCI-H1573 0.223×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 0.414×, A498 0.490×, NCI-H2347 0.568×, A549 0.500×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.173×, SW1417 0.309×, NCI-H460 0.392×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Monocrotaline (drug)]] 0.05 µM in 1 line (AN3 CA 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -5.6 | 2e-05 | 26/48 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.749×** | -4.4 | 0.003 | 26/45 (HepG2/C3A, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.767×** | -4.2 | 0.005 | 24/43 (C-33 A, SNU-1, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.769×** | -4.1 | 0.005 | 21/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.779×** | -4.1 | 0.005 | 25/49 (RKO, SW1417, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.806×** | -3.5 | 0.038 | 19/48 (HS-578T, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.812×** | -3.4 | 0.050 | 19/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.813×** | -3.4 | 0.050 | 19/47 (Panc 03.27, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.870× | -3.2 | 0.078 | 10/48 (SHP-77, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.876× | -3.1 | 0.12 | 14/48 (HOP62, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 64.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[AsPC-1 (line)]] | alt | 43.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -9.9) |
| [[SW48 (line)]] | wt | 77.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[A498 (line)]] | wt | 59.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.7) |
| [[A549 (line)]] | wt | 40.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -8.7) |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0725× (z -13.0) |
| [[C32 (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.117× (z -9.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[hTERT-HPNE (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[LoVo (line)]] | wt | 58.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H23 (line)]] | alt | 45.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 78.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0558× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 59.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.120× (z -9.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0936× (z -10.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 94.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRS2]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[SEPTIN7P2]] | +0.64 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[SPAST]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TMEM183A]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TM9SF2]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ANAPC5]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[VTI1B]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PIKFYVE]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 | pathway: PI Metabolism |
| [[ZW10]] | +0.59 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[SAMM50]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.58 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[PRRC1]] | +0.57 | +0.59 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD11]] | -0.61 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[DPH1-AS1]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[KDM6B]] | -0.57 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[ADNP2]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ABL2]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ZNF335]] | -0.53 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[HDAC9]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PLA2G4C]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 | pathway: Phospholipid metabolism |
| [[PKNOX1]] | -0.51 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[ZNF341-AS1]] | -0.51 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[SYS1]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[IBA57]] | -0.51 | -0.54 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.686). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-8.6, -14.0); signed map (-36.8, -14.6). **Vector** length 99.9, 25.0% of its response variance represented; |z| ≥ 3 in 745 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +2.6 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.8 | +0.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -1.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -5.0 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.2 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -2.0 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | SAC1 like phosphatidylinositide phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:45,689,056-45,745,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAC1, KIAA0851 |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 5 pathways, smallest: Synthesis of PIPs at the ER membrane; Synthesis of PIPs at the Golgi membrane; PI Metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTJ5](https://www.uniprot.org/uniprotkb/Q9NTJ5) (Phosphatidylinositol-3-phosphatase SAC1):

> Phosphoinositide phosphatase which catalyzes the hydrolysis of phosphatidylinositol 4-phosphate (PtdIns(4)P). Can also catalyze the hydrolysis of phosphatidylinositol 3-phosphate (PtdIns(3)P) and has low activity towards phosphatidylinositol-3,5-bisphosphate (PtdIns(3,5)P2) (By similarity). Shows a very robust PtdIns(4)P phosphatase activity when it binds PtdIns(4)P in a 'cis' configuration in the cellular environment, with much less activity seen when it binds PtdIns(4)P in 'trans' …

**Summary**, from NCBI Gene [22908](https://www.ncbi.nlm.nih.gov/gene/22908):

> This gene encodes an integral membrane protein, which is localized to the endoplasmic reticulum, and functions as a phosphoinositide phosphatase that hydrolyzes phosphatidylinositol 3-phosphate, phosphatidylinositol 4-phosphate, and phosphatidylinositol 3,5-bisphosphate. Deletion of this gene in mouse results in preimplantation lethality. Other studies suggest that this gene is also involved in the organization of golgi membranes and mitotic spindles. Alternatively spliced transcript variants …

**Accessions** — [HGNC:17059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17059) · Entrez [22908](https://www.ncbi.nlm.nih.gov/gene/22908) · UniProt [Q9NTJ5](https://www.uniprot.org/uniprotkb/Q9NTJ5) · Ensembl [ENSG00000211456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211456)

## Data

Gene col 13063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13063); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13063]; `tensor/DDL_lfc|DDL_z.npy` [13063]; `embed/gene_vectors.npy` [13063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13063 or target_col == 13063). Every well: [[SACM1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SACM1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
