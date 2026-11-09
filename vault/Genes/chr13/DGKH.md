---
symbol: "DGKH"
type: "gene"
col: 2270
ensembl_id: "ENSG00000102780"
name: "diacylglycerol kinase eta"
location: "13q14.11"
module: 65
arm: "-"
pooled_cpm: 156.51
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# DGKH

*diacylglycerol kinase eta* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +13.8, q 1e-40, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.504× (z -11.4, q 2e-27, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRG]] (+0.66, fdr 1e-05), [[BAZ1A]] (+0.64, fdr 1e-05), [[GNG12-AS1]] (+0.63, fdr 2e-05); moves opposite to [[RAB3A]] (-0.68, fdr 2e-05), [[OSBPL7]] (-0.67, fdr 1e-05), [[ARL6]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +13.8 | 1e-40 | 43/49 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +8.9 | 2e-16 | 29/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.4 | 6e-15 | 40/48 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.3 | 5e-08 | 37/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.2 | 5e-08 | 36/50 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.2 | 2e-05 | 28/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.016 | 24/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.017 | 22/48 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.21× | +3.1 | 0.10 | 21/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.11 | 22/47 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.504×** | -11.4 | 2e-27 | 41/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.544×** | -10.1 | 1e-21 | 39/48 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -9.9 | 1e-20 | 40/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -6.4 | 2e-08 | 32/49 (RKO, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.710×** | -5.7 | 1e-06 | 35/48 (Panc 03.27, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -5.2 | 2e-05 | 33/47 (LOX-IMVI, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -4.5 | 5e-04 | 27/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.765×** | -4.5 | 6e-04 | 27/48 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.803×** | -3.7 | 0.015 | 28/49 (BT-474, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.805×** | -3.6 | 0.016 | 25/48 (BT-474, COLO 205, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.802×** | -3.4 | 0.033 | 25/45 (NCI-H23, J82, …) | inconsistent across doses | composition shift |
| [[Vilanterol (drug)]] 5 µM |  | 0.869× | -3.3 | 0.040 | 7/49 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.817×** | -3.2 | 0.062 | 22/48 (COLO 205, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.878× | -3.1 | 0.078 | 10/48 (RKO, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 55.3 | 18 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.15× (z +16.4) | — |
| [[LS 180 (line)]] | wt | 159 | 1 | 10 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -21.2) |
| [[SNU-1 (line)]] | wt | 292 | 6 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 72.2 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 246 | 1 | 8 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 67.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +30.5) | — |
| [[COLO 205 (line)]] | alt | 362 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -14.0) |
| [[RKO (line)]] | wt | 278 | 2 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -13.4) |
| [[SW480 (line)]] | alt | 205 | 3 | 4 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.395× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 111 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +17.1) | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 125 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.393× (z -10.7) |
| [[PANC-1 (line)]] | alt | 216 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +32.6) | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -12.6) |
| [[A-172 (line)]] | wt | 101 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 161 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 189 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -13.3) |
| [[Hs 766T (line)]] | wt | 321 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -11.2) |
| [[J82 (line)]] | alt | 216 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.435× (z -10.4) |
| [[SW1417 (line)]] | alt | 142 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -13.4) |
| [[A549 (line)]] | wt | 118 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.7) | [[Belinostat (drug)]] 5 µM 0.401× (z -8.6) |
| [[C32 (line)]] | wt | 102 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +17.0) | — |
| [[H4 (line)]] | wt | 74.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 500 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 172 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.2) | [[Docetaxel (drug)]] 0.05 µM 0.382× (z -10.5) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.388× (z -10.3) |
| [[SW48 (line)]] | wt | 125 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.4) | [[Ixazomib citrate (drug)]] 0.5 µM 0.377× (z -8.6) |
| [[A-427 (line)]] | wt | 108 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.454× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 62.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +15.7) | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HOP62 (line)]] | alt | 64.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +14.7) | — |
| [[LoVo (line)]] | wt | 169 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +13.2) | [[TAK-901 (drug)]] 5 µM 0.203× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 121 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 2.57× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.414× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 109 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 155 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 114 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 50.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 183 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.3) |
| [[C-33 A (line)]] | alt | 238 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 354 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.217× (z -10.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 85.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 210 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[KATO III (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.432× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 83.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -10.8) |
| [[SW 900 (line)]] | alt | 146 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*29 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRG]] | +0.66 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[BAZ1A]] | +0.64 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[GNG12-AS1]] | +0.63 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[ZNF800]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CFLAR]] | +0.62 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[ATP11C]] | +0.61 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[MSRA]] | +0.60 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[KDSR]] | +0.59 | +0.56 / +0.39 | both halves | 6e-05 |  |
| [[E2F3]] | +0.59 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[GCNT4]] | +0.58 | +0.46 / +0.33 | both halves | 1e-04 |  |
| [[CLOCK]] | +0.57 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ITPA]] | +0.57 | +0.51 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*71 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.68 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[OSBPL7]] | -0.67 | -0.58 / -0.51 | both halves | 1e-05 | same gene group |
| [[ARL6]] | -0.67 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TMEM9]] | -0.67 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[USP30]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[KCTD6]] | -0.65 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[PRMT9]] | -0.64 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[PAK4]] | -0.63 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[PRUNE1]] | -0.63 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[RGS14]] | -0.62 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[IFT172]] | -0.61 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ZFP14]] | -0.60 | -0.50 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DGKH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers DGKH's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (0.1, -8.3); signed map (16.1, -7.1). **Vector** length 148, 49.6% of its response variance represented; |z| ≥ 3 in 1,398 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.4 | +13.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.2 | +8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.8 | +6.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.8 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.5 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.0 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.8 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.3 | -11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -9.1 | -9.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.8 | -10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.4 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase eta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:42,040,036-42,256,578 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DGKeta |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Sterile alpha motif domain containing; Diacylglycerol kinase family |
| Hallmark sets | COMPLEMENT |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XP1](https://www.uniprot.org/uniprotkb/Q86XP1) (Diacylglycerol kinase eta):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes (Probable). Plays a key role in promoting cell growth. Activates the Ras/B-Raf/C-Raf/MEK/ERK signaling pathway induced by EGF. Regulates the …

**Summary**, from NCBI Gene [160851](https://www.ncbi.nlm.nih.gov/gene/160851):

> This gene encodes a member of the diacylglycerol kinase (DGK) enzyme family. Members of this family are involved in regulating intracellular concentrations of diacylglycerol and phosphatidic acid. Variation in this gene has been associated with bipolar disorder. Alternatively spliced transcript variants have been identified. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:2854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2854) · Entrez [160851](https://www.ncbi.nlm.nih.gov/gene/160851) · UniProt [Q86XP1](https://www.uniprot.org/uniprotkb/Q86XP1) · Ensembl [ENSG00000102780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102780)

## Data

Gene col 2270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2270); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2270]; `tensor/DDL_lfc|DDL_z.npy` [2270]; `embed/gene_vectors.npy` [2270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2270 or target_col == 2270). Every well: [[DGKH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
