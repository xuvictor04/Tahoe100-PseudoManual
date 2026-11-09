---
symbol: "EIF5"
type: "gene"
col: 2010
ensembl_id: "ENSG00000100664"
name: "eukaryotic translation initiation factor 5"
location: "14q32.32"
module: 135
arm: "+"
pooled_cpm: 121.69
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 8
n_dd_up_clean: 32
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# EIF5

*eukaryotic translation initiation factor 5* — 14q32.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.68× (z +42.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.862× (z -9.6, q 3e-19, down in 8 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.609× (z -9.6, q 3e-19, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF6]] (+0.73, fdr 1e-05), [[LINC00571]] (+0.72, fdr 1e-05), [[ZSCAN29]] (+0.72, fdr 7e-06); moves opposite to [[ANAPC11]] (-0.69, fdr 1e-04), [[HMGN3]] (-0.68, fdr 1e-05), [[GUSBP18]] (-0.67, fdr 1e-04).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RNF103-CHMP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.68×** | +42.0 | 0e+00 | 48/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.44×** | +28.7 | 0e+00 | 48/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.59×** | +24.6 | 0e+00 | 47/48 (LoVo, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.19×** | +21.4 | 0e+00 | 47/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.16×** | +14.8 | 0e+00 | 45/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +12.0 | 2e-31 | 47/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +11.8 | 2e-30 | 44/49 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +10.2 | 2e-22 | 35/48 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.71×** | +9.8 | 1e-20 | 46/48 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +9.5 | 8e-20 | 43/47 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +9.5 | 1e-19 | 45/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +8.3 | 4e-15 | 39/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.51×** | +7.9 | 2e-13 | 44/48 (SW480, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +7.7 | 4e-13 | 34/48 (J82, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.7 | 6e-10 | 35/50 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +6.2 | 2e-08 | 34/49 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.862× | -9.6 | 3e-19 | 8/50 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -9.6 | 3e-19 | 42/48 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.666×** | -7.9 | 8e-13 | 43/48 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.673×** | -6.9 | 8e-10 | 41/48 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.711×** | -5.9 | 3e-07 | 33/48 (NCI-H2347, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.750×** | -5.6 | 2e-06 | 31/48 (BT-474, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.578×** | -5.5 | 3e-06 | 42/49 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.778×** | -4.9 | 8e-05 | 38/49 (SW 1088, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.810×** | -4.1 | 0.003 | 26/49 (LOX-IMVI, CHP-212, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.869× | -3.8 | 0.009 | 13/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -3.2 | 0.079 | 11/48 (BT-474, LOX-IMVI, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.848× | -3.1 | 0.095 | 17/47 (HT-29, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 106 | 14 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +28.6) | — |
| [[NCI-H1573 (line)]] | alt | 134 | 12 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.34× (z +36.9) | [[Belinostat (drug)]] 5 µM 0.485× (z -8.5) |
| [[J82 (line)]] | alt | 115 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +25.0) | — |
| [[HT-29 (line)]] | alt | 89.2 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +26.7) | — |
| [[LoVo (line)]] | wt | 119 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +37.3) | — |
| [[NCI-H2347 (line)]] | alt | 177 | 7 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.4) | [[Belinostat (drug)]] 5 µM 0.420× (z -10.4) |
| [[PANC-1 (line)]] | alt | 86.4 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +23.2) | — |
| [[SW480 (line)]] | alt | 147 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +23.6) | — |
| [[BT-474 (line)]] | alt | 143 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +19.0) | — |
| [[SW 900 (line)]] | alt | 128 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +25.4) | [[Belinostat (drug)]] 5 µM 0.444× (z -8.5) |
| [[KATO III (line)]] | alt | 111 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +21.9) | — |
| [[LS 180 (line)]] | wt | 124 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +19.4) | — |
| [[Panc 03.27 (line)]] | alt | 147 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +27.5) | — |
| [[SNU-1 (line)]] | wt | 127 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.0) | — |
| [[A498 (line)]] | wt | 81.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +27.2) | — |
| [[AsPC-1 (line)]] | alt | 126 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +31.3) | — |
| [[HEC-1-A (line)]] | alt | 131 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +24.9) | — |
| [[LOX-IMVI (line)]] | wt | 129 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +26.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 164 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +20.0) | — |
| [[NCI-H2030 (line)]] | alt | 179 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +20.6) | — |
| [[RKO (line)]] | wt | 148 | 6 | 0 | [[Auranofin (drug)]] 5 µM 5.48× (z +20.0) | — |
| [[RPMI-7951 (line)]] | alt | 104 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +22.8) | — |
| [[A-172 (line)]] | wt | 60.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +26.5) | — |
| [[A549 (line)]] | wt | 108 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +29.0) | — |
| [[C32 (line)]] | wt | 99.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +22.0) | — |
| [[COLO 205 (line)]] | alt | 81.7 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +29.3) | [[Belinostat (drug)]] 5 µM 0.398× (z -8.5) |
| [[HOP62 (line)]] | alt | 148 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +29.8) | — |
| [[Hs 766T (line)]] | wt | 68.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +23.9) | — |
| [[HS-578T (line)]] | alt | 77.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +24.1) | — |
| [[hTERT-HPNE (line)]] | wt | 96.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +26.9) | — |
| [[NCI-H1792 (line)]] | alt | 96.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +31.3) | — |
| [[SK-MEL-2 (line)]] | alt | 139 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +20.5) | — |
| [[SNU-423 (line)]] | alt | 130 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +30.3) | — |
| [[SW1417 (line)]] | alt | 140 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +20.9) | — |
| [[A-427 (line)]] | wt | 136 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 204 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +26.7) | — |
| [[H4 (line)]] | wt | 76.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +17.6) | — |
| [[NCI-H23 (line)]] | alt | 115 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +20.3) | [[Belinostat (drug)]] 5 µM 0.457× (z -9.0) |
| [[SHP-77 (line)]] | alt | 90.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +13.0) | — |
| [[AN3 CA (line)]] | alt | 99.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 90.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.82× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 163 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +17.5) | — |
| [[HepG2_C3A (line)]] | wt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.3) | — |
| [[SW48 (line)]] | wt | 161 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.8) | — |
| [[SW 1271 (line)]] | alt | 155 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +11.2) | — |
| [[SW 1088 (line)]] | alt | 99.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +11.0) | — |
| [[CHP-212 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF6]] | +0.73 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[LINC00571]] | +0.72 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ZSCAN29]] | +0.72 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.70 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[MMADHC-DT]] | +0.69 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[PPP1R12A-AS2]] | +0.69 | +0.58 / +0.37 | both halves | 9e-05 |  |
| [[ATXN1L]] | +0.69 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | +0.69 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[NEK11]] | +0.68 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.68 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[ZNF189]] | +0.68 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[ATF5]] | +0.68 | +0.62 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC11]] | -0.69 | -0.69 / -0.34 | both halves | 1e-04 |  |
| [[HMGN3]] | -0.68 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[GUSBP18]] | -0.67 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[L2HGDH]] | -0.66 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[NHP2]] | -0.66 | -0.47 / -0.37 | both halves | 8e-05 | STRING 628 |
| [[NDUFB6]] | -0.63 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[KIAA1328]] | -0.63 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[TMEM160]] | -0.63 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[METRN]] | -0.63 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[YIF1B]] | -0.62 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[EFHC1]] | -0.62 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[SLC9A6]] | -0.62 | -0.57 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF103-CHMP3]] | B | RNF103-CHMP3 activity raises EIF5's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without RNF103-CHMP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises EIF5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises EIF5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers EIF5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HMGA1P4]] | C | HMGA1P4 activity raises EIF5's level | lines that do not express HMGA1P4 (3) vs lines expressing it (47) | 1.50× lower at baseline in the lines without HMGA1P4 | 0.088 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, CASP8, SP100 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (8.2, 10.9); signed map (21.9, -7.4). **Vector** length 125, 45.5% of its response variance represented; |z| ≥ 3 in 1,620 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.9 | +24.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.4 | +28.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.5 | +7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +14.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.3 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +9.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -9.6 | -9.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.8 | -6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.5 | -7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.9 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.1 | -5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.8 | -5.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -2.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.32 — chr14:103,333,544-103,345,025 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 5 pathways, smallest: Ribosomal scanning and start codon recognition; GTP hydrolysis and joining of the 60S ribosomal subunit; Cap-dependent Translation Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P55010](https://www.uniprot.org/uniprotkb/P55010) (Eukaryotic translation initiation factor 5):

> Component of the 43S pre-initiation complex (43S PIC), which binds to the mRNA cap-proximal region, scans mRNA 5'-untranslated region, and locates the initiation codon. In this complex, acts as a GTPase-activating protein, by promoting GTP hydrolysis by eIF2G (EIF2S3). During scanning, interacts with both EIF1 (via its C-terminal domain (CTD)) and EIF1A (via its NTD). This interaction with EIF1A contributes to the maintenance of EIF1 within the open 43S PIC. When start codon is recognized, …

**Summary**, from NCBI Gene [1983](https://www.ncbi.nlm.nih.gov/gene/1983):

> Eukaryotic translation initiation factor-5 (EIF5) interacts with the 40S initiation complex to promote hydrolysis of bound GTP with concomitant joining of the 60S ribosomal subunit to the 40S initiation complex. The resulting functional 80S ribosomal initiation complex is then active in peptidyl transfer and chain elongations (summary by Si et al., 1996 [PubMed 8663286]).[supplied by OMIM, May 2010]

**Accessions** — [HGNC:3299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3299) · Entrez [1983](https://www.ncbi.nlm.nih.gov/gene/1983) · UniProt [P55010](https://www.uniprot.org/uniprotkb/P55010) · Ensembl [ENSG00000100664](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100664)

## Data

Gene col 2010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2010); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2010]; `tensor/DDL_lfc|DDL_z.npy` [2010]; `embed/gene_vectors.npy` [2010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2010 or target_col == 2010). Every well: [[EIF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
