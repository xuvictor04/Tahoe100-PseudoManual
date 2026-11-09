---
symbol: "BRPF3"
type: "gene"
col: 1761
ensembl_id: "ENSG00000096070"
name: "bromodomain and PHD finger containing 3"
location: "6p21.31"
module: 173
arm: "+"
pooled_cpm: 27.04
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# BRPF3

*bromodomain and PHD finger containing 3* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +14.9, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.361× (z -15.7, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEPCE]] (+0.77, fdr 1e-05), [[ARFGAP2]] (+0.75, fdr 7e-06), [[AKT1S1]] (+0.73, fdr 1e-05); moves opposite to [[SBF2]] (-0.69, fdr 5e-05), [[PDCD10]] (-0.66, fdr 8e-05), [[HDAC3]] (-0.65, fdr 1e-05).
> It is in [[Module 173]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +14.9 | 0e+00 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +5.8 | 2e-06 | 27/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.6 | 3e-06 | 30/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.17× | +3.5 | 0.071 | 16/48 (J82, A-427, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.081 | 17/48 (HepG2/C3A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | 1.49× | +3.2 | 0.13 | 6/47 (NCI-H23, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1761.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.361×** | -15.7 | 0e+00 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.371×** | -15.2 | 0e+00 | 45/47 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.385×** | -14.7 | 0e+00 | 47/48 (A-172, HT-29, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -14.6 | 0e+00 | 47/48 (NCI-H1792, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.394×** | -14.3 | 2e-44 | 43/48 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.697×** | -7.9 | 4e-13 | 37/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.423×** | -6.9 | 4e-10 | 40/48 (NCI-H460, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.681×** | -5.9 | 3e-07 | 31/48 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -5.6 | 1e-06 | 30/48 (A498, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.590×** | -4.2 | 0.001 | 14/31 (HS-578T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.783×** | -3.8 | 0.009 | 24/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.785×** | -3.7 | 0.010 | 23/47 (J82, SHP-77, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.635×** | -3.6 | 0.012 | 15/48 (LS 180, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.802×** | -3.4 | 0.029 | 16/48 (SW 900, HT-29, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.858× | -3.3 | 0.034 | 20/47 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **0.755×** | -3.1 | 0.070 | 9/48 (BT-474, A498, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.682×** | -3.1 | 0.070 | 14/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.816×** | -3.0 | 0.081 | 12/48 (NCI-H1792, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.8 | 4 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +17.2) | [[Belinostat (drug)]] 5 µM 0.201× (z -12.7) |
| [[A498 (line)]] | wt | 28.5 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +15.7) | [[Belinostat (drug)]] 5 µM 0.278× (z -12.0) |
| [[HOP62 (line)]] | alt | 34.8 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.1) | [[Belinostat (drug)]] 5 µM 0.246× (z -12.4) |
| [[HT-29 (line)]] | alt | 37.6 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -11.8) |
| [[SW480 (line)]] | alt | 22.8 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.326× (z -10.8) |
| [[A-172 (line)]] | wt | 19.9 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.196× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 57.7 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.231× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.276× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 30.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 30.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 17.1 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.7) | [[Belinostat (drug)]] 0.5 µM 0.196× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 46.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -14.7) |
| [[SNU-1 (line)]] | wt | 38.9 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0579× (z -16.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.184× (z -10.1) |
| [[J82 (line)]] | alt | 25.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.351× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.352× (z -8.6) |
| [[PANC-1 (line)]] | alt | 22.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +18.4) | — |
| [[SNU-423 (line)]] | alt | 39.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +13.3) | [[Belinostat (drug)]] 0.5 µM 0.288× (z -10.2) |
| [[H4 (line)]] | wt | 24.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -9.0) |
| [[KATO III (line)]] | alt | 35.6 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.291× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.05 µM 0.272× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 25.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -13.0) |
| [[NCI-H2030 (line)]] | alt | 29.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 26.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 36.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -12.6) |
| [[A-427 (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 44.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0973× (z -11.0) |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.153× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.198× (z -10.3) |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.198× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.174× (z -9.6) |
| [[LoVo (line)]] | wt | 25.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.187× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 47.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.248× (z -12.0) |
| [[RKO (line)]] | wt | 32.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.277× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +12.0) | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.121× (z -9.3) |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEPCE]] | +0.77 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[ARFGAP2]] | +0.75 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.73 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.73 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MED12]] | +0.73 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[FKRP]] | +0.72 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[C19orf54]] | +0.71 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[CNOT3]] | +0.71 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[PMF1]] | +0.71 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[ATF5]] | +0.70 | +0.70 / +0.37 | both halves | 7e-05 |  |
| [[EIF2B5]] | +0.69 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[FIZ1]] | +0.68 | +0.59 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBF2]] | -0.69 | -0.69 / -0.39 | both halves | 5e-05 |  |
| [[PDCD10]] | -0.66 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[HDAC3]] | -0.65 | -0.60 / -0.55 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[SNRPD2]] | -0.65 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TSEN54]] | -0.64 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[FOXJ3]] | -0.64 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.64 | -0.65 / -0.46 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.63 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[LPCAT4]] | -0.63 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[NME2]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[PDZD7]] | -0.62 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[ARL6]] | -0.62 | -0.55 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.8, 4.9); signed map (16.1, -22.6). **Vector** length 110, 27.9% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +13.1 | +14.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.0 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.1 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -8.0 | -14.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.2 | -15.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -15.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.6 | -6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -1.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain and PHD finger containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:36,196,744-36,232,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1286 |
| Gene groups (HGNC) | PHD finger proteins; PWWP domain containing; Bromodomain containing |
| Hallmark sets | COMPLEMENT |
| Reactome | 10 pathways, smallest: Regulation of TP53 Activity through Acetylation; HATs acetylate histones; Platelet degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULD4](https://www.uniprot.org/uniprotkb/Q9ULD4) (Bromodomain and PHD finger-containing protein 3):

> Scaffold subunit of various histone acetyltransferase (HAT) complexes, such as the MOZ/MORF and HBO1 complexes, which have a histone H3 acetyltransferase activity. Plays a role in DNA replication initiation by directing KAT7/HBO1 specificity towards histone H3 'Lys-14' acetylation (H3K14ac), thereby facilitating the activation of replication origins. Component of the MOZ/MORF complex which has a histone H3 acetyltransferase activity.

**Summary**, from NCBI Gene [27154](https://www.ncbi.nlm.nih.gov/gene/27154):

> Contributes to histone acetyltransferase activity. Involved in positive regulation of DNA replication. Located in nucleus. Part of MOZ/MORF histone acetyltransferase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14256](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14256) · Entrez [27154](https://www.ncbi.nlm.nih.gov/gene/27154) · UniProt [Q9ULD4](https://www.uniprot.org/uniprotkb/Q9ULD4) · Ensembl [ENSG00000096070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096070)

## Data

Gene col 1761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1761); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1761]; `tensor/DDL_lfc|DDL_z.npy` [1761]; `embed/gene_vectors.npy` [1761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1761 or target_col == 1761). Every well: [[BRPF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRPF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
