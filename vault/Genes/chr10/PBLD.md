---
symbol: "PBLD"
type: "gene"
col: 2924
ensembl_id: "ENSG00000108187"
name: "phenazine biosynthesis like protein domain containing"
location: "10q21.3"
module: 35
arm: "+"
pooled_cpm: 6.65
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 13
n_dd_up_clean: 18
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 13
direction_downstream: 2
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PBLD

*phenazine biosynthesis like protein domain containing* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.28× (z +35.3, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.312× (z -13.8, q 3e-40, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMADHC-DT]] (+0.84, fdr 3e-05), [[ERCC6L2-AS1]] (+0.84, fdr 3e-04), [[PPP1R12A-AS2]] (+0.83, fdr 5e-04); moves opposite to [[MAST3]] (-0.81, fdr 1e-05), [[YIF1B]] (-0.74, fdr 0.002, ⚠ one half only (not replicated)), [[ANKRD27]] (-0.73, fdr 8e-04, ⚠ one half only (not replicated)), [[FCHO1]] (-0.72, fdr 2e-05), [[PAFAH1B3]] (-0.71, fdr 3e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[PEF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.28×** | +35.3 | 0e+00 | 41/42 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.00×** | +18.3 | 0e+00 | 36/39 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.40×** | +16.9 | 0e+00 | 36/41 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.62×** | +16.1 | 0e+00 | 38/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +13.7 | 7e-41 | 31/40 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +10.7 | 1e-24 | 13/18 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +10.0 | 1e-21 | 24/28 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +8.0 | 1e-13 | 29/46 (PANC-1, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +7.8 | 4e-13 | 24/40 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.5 | 3e-12 | 9/12 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +6.6 | 2e-09 | 19/29 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +5.2 | 1e-05 | 18/44 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.9 | 4e-05 | 16/45 (HT-29, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.7 | 1e-04 | 17/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +4.5 | 3e-04 | 12/44 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.4 | 4e-04 | 9/43 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.008 | 8/44 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.008 | 6/44 (HOP62, A-427, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.027 | 6/45 (A-427, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.312×** | -13.8 | 3e-40 | 40/46 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.367×** | -11.8 | 9e-30 | 39/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.389×** | -11.1 | 2e-26 | 36/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.406×** | -8.7 | 6e-16 | 29/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.691×** | -6.1 | 9e-08 | 23/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.386×** | -5.9 | 4e-07 | 19/42 (SK-MEL-2, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.609×** | -5.8 | 4e-07 | 21/42 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.723×** | -3.8 | 0.010 | 16/40 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.732×** | -3.7 | 0.015 | 11/44 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.724×** | -3.6 | 0.015 | 10/36 (A-427, NCI-H23, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.751×** | -3.2 | 0.062 | 11/43 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.827×** | -3.1 | 0.078 | 9/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.761×** | -3.1 | 0.095 | 8/47 (NCI-H1573, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.37 | 3 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +14.9) | [[Belinostat (drug)]] 5 µM 0.171× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 13.9 | 2 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +14.0) | [[Belinostat (drug)]] 5 µM 0.174× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 7.91 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +17.1) | [[Digitoxin (drug)]] 5 µM 0.0751× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.169× (z -10.4) |
| [[HOP62 (line)]] | alt | 4.80 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 8.39 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.96× (z +18.3) | — |
| [[HT-29 (line)]] | alt | 5.73 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +12.9) | [[Canagliflozin (drug)]] 5 µM 0.0759× (z -9.5) |
| [[SNU-423 (line)]] | alt | 9.19 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +13.9) | — |
| [[A-172 (line)]] | wt | 9.00 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +13.1) | — |
| [[A-427 (line)]] | wt | 15.6 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.136× (z -10.1) |
| [[A498 (line)]] | wt | 7.32 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 8.48 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.78× (z +13.3) | — |
| [[J82 (line)]] | alt | 5.54 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.5) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0764× (z -9.9) |
| [[KATO III (line)]] | alt | 4.15 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +12.7) | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0655× (z -9.2) |
| [[LoVo (line)]] | wt | 5.24 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 4.22 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.6) | [[Belinostat (drug)]] 5 µM 0.0325× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 11.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 2.68 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +11.7) | [[Vortioxetine (drug)]] 5 µM 0.0673× (z -9.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 5.31 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -8.6) |
| [[A549 (line)]] | wt | 5.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.2× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 8.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +10.6) | — |
| [[C32 (line)]] | wt | 4.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 6.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +13.6) | — |
| [[COLO 205 (line)]] | alt | 6.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.70× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 6.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.81× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 6.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 3.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 3.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.53× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 3.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.78× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +12.0) | — |
| [[RKO (line)]] | wt | 6.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.42× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 6.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 5.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +10.6) | — |
| [[SW48 (line)]] | wt | 5.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | +0.84 | +0.81 / +0.43 | both halves | 3e-05 |  |
| [[ERCC6L2-AS1]] | +0.84 | +0.85 / +0.27 | both halves | 3e-04 |  |
| [[PPP1R12A-AS2]] | +0.83 | +0.83 / +0.24 | both halves | 5e-04 |  |
| [[MFF-DT]] | +0.83 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[AP4S1]] | +0.82 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.82 | +0.82 / +0.36 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | +0.81 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.81 | +0.76 / +0.40 | both halves | 5e-05 |  |
| [[PKN2-AS1]] | +0.80 | +0.80 / +0.30 | both halves | 2e-04 |  |
| [[EFCAB2]] | +0.80 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[CCT6B]] | +0.80 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[CIBAR1-DT]] | +0.80 | +0.77 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.81 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[YIF1B]] | -0.74 | -0.63 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[ANKRD27]] | -0.73 | -0.72 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[FCHO1]] | -0.72 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[SLC27A1]] | -0.71 | -0.62 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[PAFAH1B3]] | -0.71 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[RALGAPA2]] | -0.70 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[SMYD3]] | -0.70 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[WRAP73]] | -0.70 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PBLD's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.5% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[WASF3]] | B | WASF3 activity raises PBLD's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.32× lower at baseline in the lines without WASF3 | 0.025 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[IGF2BP1]] | B | IGF2BP1 activity raises PBLD's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 1.24× lower at baseline in the lines without IGF2BP1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[KCNS3]] | B | KCNS3 activity raises PBLD's level | lines that do not express KCNS3 (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without KCNS3 | 0.033 | ⚠ within organs, on part of the lines; also absent: EFCAB13, JHY, SAA1; maybe low, not absent |
| [[ANKRD18B]] | B | ANKRD18B activity raises PBLD's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.19× lower at baseline in the lines without ANKRD18B | 0.038 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[HDGFL3]] | B | HDGFL3 activity raises PBLD's level | lines that do not express HDGFL3 (10) vs lines expressing it (40) | 1.16× lower at baseline in the lines without HDGFL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: HLTF, GAMT, TIGD7 |
| [[EFCAB6]] | B | EFCAB6 activity raises PBLD's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.33× lower at baseline in the lines without EFCAB6 | 0.070 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[TOX2]] | B | TOX2 activity raises PBLD's level | lines that do not express TOX2 (18) vs lines expressing it (32) | 1.24× lower at baseline in the lines without TOX2 | 0.077 | ⚠ within organs, on part of the lines; also absent: TWIST2, OLFM1, PLEKHG4B |
| [[LPAR3]] | B | LPAR3 activity raises PBLD's level | lines that do not express LPAR3 (16) vs lines expressing it (34) | 1.18× lower at baseline in the lines without LPAR3 | 0.082 | ⚠ within organs, on part of the lines; also absent: BEX4, ADAMTS18, GAB3; maybe low, not absent |
| [[PLS3-AS1]] | B | PLS3-AS1 activity raises PBLD's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without PLS3-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises PBLD's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without CYP1B1-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[RASSF8-AS1]] | B | RASSF8-AS1 activity raises PBLD's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without RASSF8-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PEF1]] | C | PBLD's natural level strengthens PEF1's drug response | PBLD's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.21; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | PBLD's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | PBLD's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.417 over the table, 0.042 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.821). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.1, 11.0); signed map (23.7, -8.1). **Vector** length 105, 24.3% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.1 | +35.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +18.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.5 | +16.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +16.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.1 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.8 | -13.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.1 | -11.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.8 | -8.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.6 | -11.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.6 | -5.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.0 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | phenazine biosynthesis like protein domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:68,282,660-68,333,049 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAWBP, MAWDBP, FLJ14767 |
| Matched by | ensembl_id |

**Function**, from UniProt [P30039](https://www.uniprot.org/uniprotkb/P30039) (Phenazine biosynthesis-like domain-containing protein):

> Functions as a positive regulator of the antiviral immune response by modulating innate immunity and viral replication by enhancing type I interferon (IFN-I) response. PBLD enhances IFN-I signaling via multiple pathways. Promotes IRF3-mediated IFN-I production and apoptosis, thereby inhibiting viral replication. Up-regulates IFN-I response by activating the NF-kappaB signaling pathway, potentially through inhibition of TRIM21-mediated degradation of phosphorylated IKKbeta, thereby sustaining …

**Summary**, from NCBI Gene [64081](https://www.ncbi.nlm.nih.gov/gene/64081):

> Enables identical protein binding activity. Involved in several processes, including antiviral innate immune response; maintenance of gastrointestinal epithelium; and positive regulation of canonical NF-kappaB signal transduction. Acts upstream of or within with a positive effect on negative regulation of transforming growth factor beta receptor signaling pathway. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23301) · Entrez [64081](https://www.ncbi.nlm.nih.gov/gene/64081) · UniProt [P30039](https://www.uniprot.org/uniprotkb/P30039) · Ensembl [ENSG00000108187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108187)

## Data

Gene col 2924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2924); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2924]; `tensor/DDL_lfc|DDL_z.npy` [2924]; `embed/gene_vectors.npy` [2924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2924 or target_col == 2924). Every well: [[PBLD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PBLD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
