---
symbol: "ASH2L"
type: "gene"
col: 4999
ensembl_id: "ENSG00000129691"
name: "ASH2 like, histone lysine methyltransferase complex subunit"
location: "8p11.23"
module: 71
arm: "+"
pooled_cpm: 36.49
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# ASH2L

*ASH2 like, histone lysine methyltransferase complex subunit* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +7.3, q 2e-10, up in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~14% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.17× (z +5.0, q 8e-05, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.512× (z -14.4, q 3e-44, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN9]] (+0.67, fdr 7e-06), [[DDX59]] (+0.62, fdr 1e-05), [[PPP1R8]] (+0.61, fdr 1e-05); moves opposite to [[SYT5]] (-0.54, fdr 3e-05), [[LHX4]] (-0.52, fdr 5e-05), [[SHC2]] (-0.52, fdr 3e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +7.3 | 2e-10 | 27/48 (SW480, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +5.1 | 8e-05 | 23/46 (A498, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +5.0 | 8e-05 | 18/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.004 | 18/48 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.18× | +3.7 | 0.021 | 11/48 (LoVo, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.15× | +3.1 | 0.19 | 10/48 (PANC-1, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.512×** | -14.4 | 3e-44 | 40/48 (A-427, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.619×** | -10.2 | 5e-22 | 35/46 (LoVo, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -9.4 | 1e-18 | 27/42 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.768×** | -8.3 | 2e-14 | 28/48 (NCI-H23, LoVo, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.524×** | -7.5 | 6e-12 | 31/49 (SNU-1, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -7.5 | 6e-12 | 29/47 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.774×** | -5.5 | 3e-06 | 22/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.808×** | -4.7 | 2e-04 | 21/48 (SW480, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.827×** | -4.1 | 0.003 | 20/46 (SW480, SW48, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.839× | -3.9 | 0.006 | 20/48 (LS 180, NCI-H661, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.791×** | -3.7 | 0.011 | 19/46 (C-33 A, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.5 | 0.020 | 17/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.745×** | -3.4 | 0.029 | 5/47 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.898× | -3.3 | 0.034 | 13/48 (NCI-H1792, HS-578T, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.861× | -3.3 | 0.035 | 11/48 (CHP-212, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.752×** | -3.3 | 0.035 | 19/47 (SW48, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.858× | -3.2 | 0.040 | 15/46 (A498, A-427, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.872× | -3.0 | 0.073 | 9/48 (SHP-77, LoVo, …) | two highest doses |  |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | 0.864× | -3.0 | 0.078 | 10/46 (A-427, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.2 | 0 | 7 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -14.3) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SW480 (line)]] | alt | 49.2 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.328× (z -14.6) |
| [[H4 (line)]] | wt | 39.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -11.5) |
| [[SW48 (line)]] | wt | 43.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0665× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 42.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.242× (z -12.3) |
| [[A-427 (line)]] | wt | 48.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.193× (z -15.8) |
| [[HOP62 (line)]] | alt | 36.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.360× (z -9.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 48.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.312× (z -11.5) |
| [[J82 (line)]] | alt | 55.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -9.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 30.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.282× (z -12.2) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 53.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -13.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -12.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 53.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.258× (z -10.9) |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[HEC-1-A (line)]] | alt | 35.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.396× (z -9.0) |
| [[Hs 766T (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.244× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[KATO III (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.384× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0852× (z -19.2) |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.418× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.499× (z -8.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[A-172 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN9]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[DDX59]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PPP1R8]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[INTS8]] | +0.61 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[QRSL1]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CTCF]] | +0.59 | +0.46 / +0.61 | both halves | 3e-05 | pathway: Activation of HOX genes during differentiation; STRING 625 |
| [[LRR1]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FANCM]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[DHX35]] | +0.58 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[RMI1]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CASD1]] | +0.57 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[RCC1L]] | +0.57 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYT5]] | -0.54 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[LHX4]] | -0.52 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[SHC2]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TMPRSS9]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PTP4A2]] | -0.51 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[MAFK]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |
| [[GNG7]] | -0.51 | -0.39 / -0.44 | both halves | 5e-05 | pathway: Signaling by WNT |
| [[FADS3]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ANKDD1A]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[CELF5]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[SPAG9]] | -0.50 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[NEAT1]] | -0.49 | -0.23 / -0.55 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-50.7, -0.0); signed map (-6.2, -17.7). **Vector** length 83.2, 16.3% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.4 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.4 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +4.4 | +7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.8 | -14.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -4.4 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.8 | -0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ASH2 like, histone lysine methyltransferase complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,105,493-38,144,076 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASH2L2, ASH2, Bre2; previously ASH2L1 |
| Gene groups (HGNC) | PHD finger proteins; WRAD complex |
| Reactome | 30 pathways, smallest: Loss of Function of KMT2D in Kabuki Syndrome; Loss of Function of KMT2D in MLL4 Complex Formation in Kabuki Syndrome; Disorders of Developmental Biology |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBL3](https://www.uniprot.org/uniprotkb/Q9UBL3) (Set1/Ash2 histone methyltransferase complex subunit ASH2):

> Transcriptional regulator. Component or associated component of some histone methyltransferase complexes which regulates transcription through recruitment of those complexes to gene promoters. Component of the Set1/Ash2 histone methyltransferase (HMT) complex, a complex that specifically methylates 'Lys-4' of histone H3, but not if the neighboring 'Lys-9' residue is already methylated. As part of the MLL1/MLL complex it is involved in methylation and dimethylation at 'Lys-4' of histone H3. May …

**Summary**, from NCBI Gene [9070](https://www.ncbi.nlm.nih.gov/gene/9070):

> Enables beta-catenin binding activity and transcription cis-regulatory region binding activity. Involved in positive regulation of cell population proliferation; response to estrogen; and transcription initiation-coupled chromatin remodeling. Acts upstream of or within DNA damage response. Located in nucleoplasm and plasma membrane. Part of MLL3/4 complex and Set1C/COMPASS complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:744) · Entrez [9070](https://www.ncbi.nlm.nih.gov/gene/9070) · UniProt [Q9UBL3](https://www.uniprot.org/uniprotkb/Q9UBL3) · Ensembl [ENSG00000129691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129691)

## Data

Gene col 4999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4999); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4999]; `tensor/DDL_lfc|DDL_z.npy` [4999]; `embed/gene_vectors.npy` [4999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4999 or target_col == 4999). Every well: [[ASH2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASH2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
