---
symbol: "MFSD1"
type: "gene"
col: 4022
ensembl_id: "ENSG00000118855"
name: "major facilitator superfamily domain containing 1"
location: "3q25.32"
module: 26
arm: "+"
pooled_cpm: 38.21
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MFSD1

*major facilitator superfamily domain containing 1* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +22.0, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.745× (z -5.4, q 4e-05, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.136×); [[Pemetrexed (drug)]] 5 µM in 1 line (hTERT-HPNE 0.192×); [[Dexamethasone (drug)]] 0.5 µM in 1 line (H4 0.308×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACYP2]] (+0.62, fdr 1e-05), [[SDCBP2-AS1]] (+0.58, fdr 3e-05), [[ATXN10]] (+0.57, fdr 3e-05); moves opposite to [[SLC35A1]] (-0.60, fdr 2e-05), [[NBPF3]] (-0.53, fdr 3e-04), [[CHEK2]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CACNA2D1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +22.0 | 0e+00 | 45/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +19.8 | 0e+00 | 37/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +18.9 | 0e+00 | 41/45 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +14.6 | 0e+00 | 29/36 (SNU-423, C32, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +14.3 | 4e-44 | 35/40 (SNU-423, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +13.8 | 2e-41 | 41/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +13.7 | 1e-40 | 42/47 (PANC-1, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +11.8 | 2e-30 | 39/47 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +11.3 | 5e-28 | 36/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +11.3 | 6e-28 | 37/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +10.4 | 1e-23 | 36/46 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +10.0 | 1e-21 | 40/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +8.2 | 1e-14 | 34/47 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +7.3 | 1e-11 | 28/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +6.8 | 5e-10 | 26/47 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +6.5 | 3e-09 | 25/47 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +6.2 | 2e-08 | 25/47 (SW480, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.7 | 4e-07 | 25/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4022.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.136×); [[Pemetrexed (drug)]] 5 µM in 1 line (hTERT-HPNE 0.192×); [[Dexamethasone (drug)]] 0.5 µM in 1 line (H4 0.308×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -5.4 | 4e-05 | 27/47 (A-427, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -4.0 | 0.020 | 0/47 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -3.7 | 0.041 | 15/47 (HEC-1-A, A-427, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.873× | -3.5 | 0.064 | 14/47 (BT-474, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 44.5 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 32.6 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +13.5) | — |
| [[SW480 (line)]] | alt | 26.5 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +16.2) | — |
| [[A-172 (line)]] | wt | 36.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 20.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +14.5) | — |
| [[HOP62 (line)]] | alt | 35.4 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +12.4) | — |
| [[J82 (line)]] | alt | 85.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +21.9) | — |
| [[KATO III (line)]] | alt | 44.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 28.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +24.8) | — |
| [[COLO 205 (line)]] | alt | 36.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +18.5) | — |
| [[NCI-H2347 (line)]] | alt | 24.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +15.9) | — |
| [[RPMI-7951 (line)]] | alt | 72.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 36.6 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.6) | — |
| [[A498 (line)]] | wt | 54.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 31.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +19.4) | — |
| [[Panc 03.27 (line)]] | alt | 44.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.3) | — |
| [[A-427 (line)]] | wt | 54.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.9) | — |
| [[A549 (line)]] | wt | 21.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 34.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 20.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +14.6) | — |
| [[HT-29 (line)]] | alt | 22.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 25.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 69.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +8.8) ⚠ toxic; transcription drop | [[Triamcinolone (drug)]] 5 µM 0.480× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 47.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.4) | — |
| [[RKO (line)]] | wt | 35.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 48.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.3) | [[AZD2858 (drug)]] 0.5 µM 0.216× (z -8.5) ⚠ toxic |
| [[C32 (line)]] | wt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +10.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 20.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +15.0) | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0912× (z -8.7) |
| [[H4 (line)]] | wt | 100.0 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.308× (z -9.2) |
| [[HCT15 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.136× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.192× (z -9.3) |
| [[SHP-77 (line)]] | alt | 43.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACYP2]] | +0.62 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[SDCBP2-AS1]] | +0.58 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[ATXN10]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[BBOX1-AS1]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NEK11]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | +0.55 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[CATSPERE]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ALOX12-AS1]] | +0.54 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[CRPPA]] | +0.54 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[IQCG]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[LINC00907]] | +0.53 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ZNF407]] | +0.53 | +0.29 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A1]] | -0.60 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[NBPF3]] | -0.53 | -0.64 / -0.28 | both halves | 3e-04 |  |
| [[CHEK2]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[AFMID]] | -0.51 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ATG4C]] | -0.51 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[MT1X]] | -0.50 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[PET117]] | -0.50 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[C17orf58]] | -0.50 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[PCTP]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[KLHL8]] | -0.49 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[DPY30]] | -0.49 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[KLHL26]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D1]] | B | CACNA2D1 activity raises MFSD1's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without CACNA2D1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[TOP2A]] | B | TOP2A activity lowers MFSD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC2-AS2]] | B | HDAC2-AS2 activity raises MFSD1's level | lines that do not express HDAC2-AS2 (5) vs lines expressing it (45) | 1.76× lower at baseline in the lines without HDAC2-AS2 | 0.067 | ⚠ within organs, on part of the lines; also absent: OPN3, ACVR1C, METTL21EP-1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.4, 8.1); signed map (19.8, -25.2). **Vector** length 96.3, 24.4% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.1 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +18.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +14.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +4.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | +11.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | major facilitator superfamily domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:158,732,198-158,829,719 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Minerva, SLC72A1, FLJ14153, UG0581B09 |
| Gene groups (HGNC) | Solute carrier family 72 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3U5](https://www.uniprot.org/uniprotkb/Q9H3U5) (Lysosomal dipeptide transporter MFSD1):

> Lysosomal dipeptide uniporter that selectively exports lysine, arginine or histidine-containing dipeptides with a net positive charge from the lysosome lumen into the cytosol. Could play a role in a specific type of protein O-glycosylation indirectly regulating macrophages migration and tissue invasion. Also essential for liver homeostasis (By similarity).

**Summary**, from NCBI Gene [64747](https://www.ncbi.nlm.nih.gov/gene/64747):

> Enables dipeptide uniporter activity. Involved in dipeptide transmembrane transport from lysosomal lumen to cytosol. Is active in lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25874) · Entrez [64747](https://www.ncbi.nlm.nih.gov/gene/64747) · UniProt [Q9H3U5](https://www.uniprot.org/uniprotkb/Q9H3U5) · Ensembl [ENSG00000118855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118855)

## Data

Gene col 4022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4022); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4022]; `tensor/DDL_lfc|DDL_z.npy` [4022]; `embed/gene_vectors.npy` [4022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4022 or target_col == 4022). Every well: [[MFSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
