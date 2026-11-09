---
symbol: "RIPOR1"
type: "gene"
col: 462
ensembl_id: "ENSG00000039523"
name: "RHO family interacting cell polarization regulator 1"
location: "16q22.1"
module: 138
arm: "+"
pooled_cpm: 23.81
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# RIPOR1

*RHO family interacting cell polarization regulator 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +7.8, q 2e-12, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.531× (z -9.4, q 3e-18, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.667× (z -8.5, q 5e-15, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LZTR1]] (+0.68, fdr 1e-05), [[CRTC2]] (+0.65, fdr 7e-06), [[INF2]] (+0.65, fdr 7e-06); moves opposite to [[COX8A]] (-0.56, fdr 5e-05), [[COX7A2]] (-0.56, fdr 3e-05, ⚠ COX7A2 in the vector space only through flagged drug-doses), [[NDUFA4]] (-0.55, fdr 1e-05), [[MIF]] (-0.53, fdr 5e-05).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +7.8 | 2e-12 | 25/46 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.1 | 4e-07 | 18/30 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.0 | 1e-04 | 24/45 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.7 | 4e-04 | 22/40 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.5 | 7e-04 | 21/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 0.001 | 20/47 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.003 | 17/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.023 | 12/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.023 | 15/47 (J82, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.25×** | +3.3 | 0.060 | 9/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.066 | 15/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.0 | 0.11 | 2/47 (NCI-H1573, HCT15) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.531×** | -9.4 | 3e-18 | 35/47 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -8.5 | 5e-15 | 31/47 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.623×** | -7.0 | 4e-10 | 27/47 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -5.5 | 6e-06 | 26/47 (J82, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.738×** | -4.3 | 0.002 | 17/47 (AsPC-1, Hs 766T, …) | rises with dose | position effect removed |
| [[Sulfisoxazole (drug)]] 5 µM |  | **0.819×** | -4.2 | 0.002 | 17/47 (LoVo, A549, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.758×** | -4.1 | 0.003 | 16/47 (SW 1088, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -4.0 | 0.005 | 12/47 (MIA PaCa-2, HOP62, …) | rises with dose | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.761×** | -3.9 | 0.006 | 17/46 (BT-474, C32, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.770×** | -3.9 | 0.006 | 19/47 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.767×** | -3.8 | 0.007 | 17/44 (A-172, HT-29, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.033 | 16/46 (SW 900, SNU-423, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.035 | 10/46 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.803×** | -3.3 | 0.043 | 20/47 (HOP62, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Allantoin (drug)]] 5 µM |  | 0.857× | -3.3 | 0.043 | 9/47 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.817×** | -3.0 | 0.090 | 18/47 (hTERT-HPNE, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 58.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +17.0) | — |
| [[Hs 766T (line)]] | wt | 51.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -13.6) |
| [[A-172 (line)]] | wt | 32.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.303× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HOP62 (line)]] | alt | 37.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -16.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -11.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 17.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.9) | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -9.5) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.9) |
| [[SNU-423 (line)]] | alt | 22.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.231× (z -10.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[AsPC-1 (line)]] | alt | 30.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -13.1) |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -8.6) |
| [[J82 (line)]] | alt | 45.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.8) | — |
| [[KATO III (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -8.6) |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.154× (z -9.4) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 1 | — | [[Megestrol (drug)]] 0.5 µM 0.220× (z -8.6) |
| [[SW 900 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.1) | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZTR1]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CRTC2]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[INF2]] | +0.65 | +0.63 / +0.70 | both halves | 7e-06 | same gene group |
| [[SLC4A2]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RPS6KA4]] | +0.63 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[HOMER3]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MED22]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[ARFRP1]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[RHBDF1]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[FLII]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[DBN1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX8A]] | -0.56 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[COX7A2]] ⚠ | -0.56 | -0.44 / -0.56 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA4]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[UQCRQ]] ⚠ | -0.54 | -0.43 / -0.56 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIF]] | -0.53 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[CA5BP1]] | -0.52 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[ATP5PD]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ODR4]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.51 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[NDUFA1]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[NDUFB11]] ⚠ | -0.50 | -0.48 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RAB33B-AS1]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NDUFA2]] | -0.50 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[COX7C]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[SSR4]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.8, -26.7); signed map (5.1, -8.1). **Vector** length 94.7, 20.6% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.7 | +2.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | RHO family interacting cell polarization regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,518,418-67,546,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13725; previously FAM65A |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZS17](https://www.uniprot.org/uniprotkb/Q6ZS17) (Rho family-interacting cell polarization regulator 1):

> Downstream effector protein for Rho-type small GTPases that plays a role in cell polarity and directional migration. Acts as an adapter protein, linking active Rho proteins to STK24 and STK26 kinases, and hence positively regulates Golgi reorientation in polarized cell migration upon Rho activation. Involved in the subcellular relocation of STK26 from the Golgi to cytoplasm punctae in a Rho- and PDCD10-dependent manner upon serum stimulation.

**Summary**, from NCBI Gene [79567](https://www.ncbi.nlm.nih.gov/gene/79567):

> Enables 14-3-3 protein binding activity. Involved in several processes, including establishment of Golgi localization; negative regulation of Rho guanyl-nucleotide exchange factor activity; and negative regulation of Rho protein signal transduction. Located in several cellular components, including Golgi apparatus; cell leading edge; and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25836) · Entrez [79567](https://www.ncbi.nlm.nih.gov/gene/79567) · UniProt [Q6ZS17](https://www.uniprot.org/uniprotkb/Q6ZS17) · Ensembl [ENSG00000039523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000039523)

## Data

Gene col 462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 462); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 462]; `tensor/DDL_lfc|DDL_z.npy` [462]; `embed/gene_vectors.npy` [462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 462 or target_col == 462). Every well: [[RIPOR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIPOR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
