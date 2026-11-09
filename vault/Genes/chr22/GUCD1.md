---
symbol: "GUCD1"
type: "gene"
col: 6252
ensembl_id: "ENSG00000138867"
name: "guanylyl cyclase domain containing 1"
location: "22q11.23"
module: 2
arm: "+"
pooled_cpm: 21.2
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# GUCD1

*guanylyl cyclase domain containing 1* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +19.3, q 0e+00, up in 42 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (SW480 2.29×, PANC-1 2.32×, NCI-H460 2.69×, Panc 03.27 2.58×, …).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.510× (z -17.4, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE27]] (+0.65, fdr 1e-05), [[XAB2]] (+0.65, fdr 1e-05), [[TP53I13]] (+0.63, fdr 8e-06); moves opposite to [[PCNX2]] (-0.60, fdr 1e-05), [[RPAP3]] (-0.58, fdr 1e-05), [[MRPS33]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6252.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (SW480 2.29×, PANC-1 2.32×, NCI-H460 2.69×, Panc 03.27 2.58×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +19.3 | 0e+00 | 42/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.4 | 2e-05 | 22/46 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +4.5 | 0.002 | 17/43 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +4.4 | 0.002 | 20/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.035 | 12/48 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.3 | 0.071 | 1/48 (NCI-H1792) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.14× | +3.3 | 0.071 | 13/48 (AsPC-1, C32, …) | top dose only | low cells (technical?) |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.13 | 1/48 (A-172) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.16 | 14/47 (COLO 205, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.510×** | -17.4 | 0e+00 | 39/47 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.442×** | -14.3 | 7e-44 | 40/47 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -10.3 | 1e-22 | 30/47 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.606×** | -9.1 | 1e-17 | 38/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.715×** | -8.6 | 6e-16 | 36/48 (NCI-H1573, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.658×** | -7.6 | 2e-12 | 30/48 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.768×** | -4.8 | 1e-04 | 20/46 (HCT15, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.773×** | -4.7 | 2e-04 | 18/48 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.815×** | -3.7 | 0.012 | 17/48 (NCI-H661, SNU-1, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.810×** | -3.7 | 0.012 | 10/47 (NCI-H2030, AN3 CA, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.831×** | -3.4 | 0.038 | 4/48 (SW48, RKO, …) | inconsistent across doses | position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.882× | -3.2 | 0.055 | 9/48 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.716×** | -3.2 | 0.062 | 15/48 (Hs 766T, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.845× | -3.1 | 0.082 | 16/48 (C-33 A, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 23.8 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 33.8 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.5) |
| [[RKO (line)]] | wt | 21.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.119× (z -12.9) |
| [[KATO III (line)]] | alt | 27.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -13.2) |
| [[SW1417 (line)]] | alt | 39.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.4) |
| [[SW480 (line)]] | alt | 21.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.0) |
| [[COLO 205 (line)]] | alt | 51.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.4) |
| [[Hs 766T (line)]] | wt | 28.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 21.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 16.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -8.9) |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.423× (z -8.9) |
| [[A-172 (line)]] | wt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.9) |
| [[A-427 (line)]] | wt | 16.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.235× (z -8.5) |
| [[A498 (line)]] | wt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.4) |
| [[A549 (line)]] | wt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +8.5) | — |
| [[C32 (line)]] | wt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -10.4) |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.242× (z -8.5) |
| [[LoVo (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.5) |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0936× (z -10.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -9.8) |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE27]] | +0.65 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[XAB2]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[TP53I13]] | +0.63 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[RAB5B]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TIMM10B]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[NDOR1]] | +0.60 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[PRDM10]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[WDR20]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SNHG30]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LMF2]] | +0.59 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[USF1]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ATG9A]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX2]] | -0.60 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[RPAP3]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[MRPS33]] | -0.58 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[METTL5]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ZMYM4]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TRMT10B]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RAD50]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[MAP9]] | -0.53 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SMIM30]] | -0.53 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[NEDD4]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 | STRING 458 |
| [[GORAB]] | -0.53 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[EXOC6]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GUCD1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SPAG4]] | B | SPAG4 activity raises GUCD1's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without SPAG4 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |
| [[NLGN2]] | C | NLGN2 activity lowers GUCD1's level | lines that do not express NLGN2 (4) vs lines expressing it (46) | 1.57× higher at baseline in the lines without NLGN2 | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: FSD1L, SLC29A4, DPF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.369). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-14.5, -15.7); signed map (-23.3, 1.5). **Vector** length 96.1, 20.1% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +19.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.0 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.5 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.7 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -14.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -17.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -9.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | guanylyl cyclase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:24,540,423-24,555,935 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC1842, LLN4; previously C22orf13 |
| Matched by | ensembl_id |

UniProt [Q96NT3](https://www.uniprot.org/uniprotkb/Q96NT3) carries no function annotation.

**Summary**, from NCBI Gene [83606](https://www.ncbi.nlm.nih.gov/gene/83606):

> Predicted to be involved in liver regeneration and response to cAMP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14237) · Entrez [83606](https://www.ncbi.nlm.nih.gov/gene/83606) · UniProt [Q96NT3](https://www.uniprot.org/uniprotkb/Q96NT3) · Ensembl [ENSG00000138867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138867)

## Data

Gene col 6252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6252); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6252]; `tensor/DDL_lfc|DDL_z.npy` [6252]; `embed/gene_vectors.npy` [6252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6252 or target_col == 6252). Every well: [[GUCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
