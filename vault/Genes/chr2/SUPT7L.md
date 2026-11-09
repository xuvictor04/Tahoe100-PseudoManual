---
symbol: "SUPT7L"
type: "gene"
col: 4115
ensembl_id: "ENSG00000119760"
name: "SPT7 like, STAGA complex subunit gamma"
location: "2p23.3"
module: 23
arm: "+"
pooled_cpm: 29.88
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SUPT7L

*SPT7 like, STAGA complex subunit gamma* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +13.2, q 3e-37, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.813× (z -5.9, q 2e-06, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.0817×, A-172 0.144×, AsPC-1 0.137×, NCI-H1573 0.288×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Mifepristone (drug)]] 0.05 µM in 1 line (SW48 0.0401×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (HCT15 0.0844×); [[Saquinavir (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.177×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM48]] (+0.75, fdr 7e-06), [[ZNF189]] (+0.70, fdr 1e-05), [[PSMC2]] (+0.66, fdr 1e-05); moves opposite to [[GNB1L]] (-0.63, fdr 1e-05), [[PPAT]] (-0.60, fdr 2e-05), [[PPM1G]] (-0.60, fdr 6e-05).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +13.2 | 3e-37 | 41/48 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +12.3 | 3e-32 | 37/47 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.76×** | +11.5 | 3e-28 | 40/48 (PANC-1, LS 180, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +10.5 | 9e-24 | 40/47 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +10.0 | 1e-21 | 38/48 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +9.8 | 7e-21 | 32/47 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +9.3 | 1e-18 | 35/48 (PANC-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +8.6 | 7e-16 | 34/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +8.5 | 1e-15 | 31/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +8.1 | 2e-14 | 33/48 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +7.3 | 1e-11 | 29/42 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.9 | 2e-10 | 28/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +6.5 | 3e-09 | 26/47 (Panc 03.27, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +6.5 | 3e-09 | 29/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.3 | 1e-08 | 33/48 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +5.8 | 2e-07 | 27/48 (NCI-H1573, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.7 | 4e-07 | 18/48 (SW1417, HS-578T, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +4.8 | 4e-05 | 23/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4115.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.0817×, A-172 0.144×, AsPC-1 0.137×, NCI-H1573 0.288×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Mifepristone (drug)]] 0.05 µM in 1 line (SW48 0.0401×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (HCT15 0.0844×); [[Saquinavir (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -5.9 | 2e-06 | 24/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -4.1 | 0.011 | 0/48 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.836× | -3.6 | 0.055 | 15/48 (NCI-H460, HCT15, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.855× | -3.2 | 0.21 | 16/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.6) | — |
| [[A-172 (line)]] | wt | 24.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[A549 (line)]] | wt | 31.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 29.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H23 (line)]] | alt | 41.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H460 (line)]] | wt | 32.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0817× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[A-427 (line)]] | wt | 41.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.3) | — |
| [[A498 (line)]] | wt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0947× (z -9.4) |
| [[HCT15 (line)]] | alt | 35.7 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0844× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.177× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 44.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.1) | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0779× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.186× (z -9.3) |
| [[SNU-1 (line)]] | wt | 37.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.364× (z -9.3) |
| [[SW48 (line)]] | wt | 26.4 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0401× (z -14.8) |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM48]] | +0.75 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[ZNF189]] | +0.70 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[PSMC2]] | +0.66 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[EAF1]] | +0.65 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[DNAJC30]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TMEM199]] | +0.63 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[POLL]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[C3orf38]] | +0.62 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[SLC4A1AP]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 | STRING 567; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ARFGAP2]] | +0.61 | +0.66 / +0.39 | both halves | 6e-05 |  |
| [[PEF1]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[BTN2A1]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[ATXN1L]] | +0.60 | +0.50 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB1L]] | -0.63 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PPAT]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PPM1G]] | -0.60 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[EML4]] | -0.60 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TRAP1]] | -0.60 | -0.49 / -0.55 | both halves | 2e-05 |  |
| [[GMDS]] | -0.59 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[TBCD]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[C20orf27]] | -0.58 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[GPSM2]] | -0.57 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[ARHGAP8]] | -0.57 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[NHP2]] | -0.56 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[SERBP1]] | -0.55 | -0.30 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-38.5, 13.0); signed map (13.4, -24.6). **Vector** length 82.2, 16.3% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.8 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +13.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SPT7 like, STAGA complex subunit gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,650,809-27,663,840 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STAF65gamma, KIAA0764, SPT7L, STAF65 |
| Gene groups (HGNC) | SAGA complex |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O94864](https://www.uniprot.org/uniprotkb/O94864) (STAGA complex 65 subunit gamma):

> As a component of the STAGA transcription coactivator-HAT complex, is involved in transcriptional regulation.

**Summary**, from NCBI Gene [9913](https://www.ncbi.nlm.nih.gov/gene/9913):

> SUPT7L is a protein subunit of the human STAGA complex (SPT3; (MIM 602947)/TAF9 (MIM 600822)/GCN5 (MIM 602301) acetyltransferase complex), which is a chromatin-modifying multiprotein complex (Martinez et al., 2001 [PubMed 11564863]).[supplied by OMIM, Apr 2009]

**Accessions** — [HGNC:30632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30632) · Entrez [9913](https://www.ncbi.nlm.nih.gov/gene/9913) · UniProt [O94864](https://www.uniprot.org/uniprotkb/O94864) · Ensembl [ENSG00000119760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119760)

## Data

Gene col 4115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4115); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4115]; `tensor/DDL_lfc|DDL_z.npy` [4115]; `embed/gene_vectors.npy` [4115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4115 or target_col == 4115). Every well: [[SUPT7L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUPT7L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
