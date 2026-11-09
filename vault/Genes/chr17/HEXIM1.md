---
symbol: "HEXIM1"
type: "gene"
col: 11860
ensembl_id: "ENSG00000186834"
name: "HEXIM P-TEFb complex subunit 1"
location: "17q21.31"
module: 93
arm: "+"
pooled_cpm: 46.9
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 3
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# HEXIM1

*HEXIM P-TEFb complex subunit 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.00× (z +26.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.731× (z -4.4, q 0.007, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00910]] (+0.71, fdr 7e-06), [[TEX14]] (+0.70, fdr 1e-05), [[POLR2A]] (+0.69, fdr 1e-05); moves opposite to [[NUP93]] (-0.61, fdr 3e-05), [[WDR5]] (-0.57, fdr 3e-05), [[FAR1]] (-0.56, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.00×** | +26.4 | 0e+00 | 47/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +18.0 | 0e+00 | 40/47 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.84×** | +11.7 | 3e-29 | 45/48 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.84×** | +11.4 | 4e-28 | 46/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +11.2 | 5e-27 | 46/47 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.92×** | +8.7 | 5e-16 | 32/38 (LoVo, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.81×** | +8.2 | 2e-14 | 36/48 (LoVo, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +7.7 | 7e-13 | 33/47 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +7.6 | 2e-12 | 30/48 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.8 | 6e-10 | 36/48 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.6 | 2e-09 | 33/49 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +6.0 | 1e-07 | 37/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.53×** | +5.9 | 2e-07 | 30/48 (A549, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.3 | 6e-06 | 29/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.85×** | +4.4 | 3e-04 | 28/48 (LOX-IMVI, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 20/48 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.005 | 26/48 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.015 | 18/48 (CFPAC-1, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.016 | 18/47 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -4.4 | 0.007 | 23/47 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.746×** | -4.1 | 0.012 | 21/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.593×** | -3.8 | 0.028 | 27/49 (CHP-212, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.841× | -3.3 | 0.12 | 16/49 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.7 | 11 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +21.8) | — |
| [[HEC-1-A (line)]] | alt | 29.8 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.24× (z +21.4) | — |
| [[A498 (line)]] | wt | 43.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +31.3) | — |
| [[CFPAC-1 (line)]] | alt | 69.0 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +18.6) | — |
| [[HS-578T (line)]] | alt | 18.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.49× (z +16.0) | — |
| [[J82 (line)]] | alt | 30.9 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +16.4) | — |
| [[KATO III (line)]] | alt | 38.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +18.1) | — |
| [[C32 (line)]] | wt | 52.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +20.1) | — |
| [[LoVo (line)]] | wt | 52.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +17.4) | — |
| [[LOX-IMVI (line)]] | wt | 55.2 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +16.5) | — |
| [[NCI-H1573 (line)]] | alt | 41.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +17.8) | — |
| [[PANC-1 (line)]] | alt | 39.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +16.4) | — |
| [[SW480 (line)]] | alt | 62.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +20.4) | — |
| [[A-172 (line)]] | wt | 26.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +16.9) | — |
| [[COLO 205 (line)]] | alt | 37.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +19.1) | — |
| [[HOP62 (line)]] | alt | 45.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +18.8) | — |
| [[Hs 766T (line)]] | wt | 25.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 35.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +14.3) | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 30.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +17.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +18.4) | — |
| [[NCI-H2347 (line)]] | alt | 44.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +12.8) | — |
| [[RKO (line)]] | wt | 29.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 41.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 36.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +15.9) | — |
| [[SW1417 (line)]] | alt | 78.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.5) | — |
| [[A549 (line)]] | wt | 45.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.84× (z +17.3) | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +14.1) | — |
| [[H4 (line)]] | wt | 50.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -8.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 40.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +19.3) | — |
| [[NCI-H23 (line)]] | alt | 63.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 82.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +15.1) | — |
| [[SNU-1 (line)]] | wt | 65.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.275× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 29.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +9.6) | — |
| [[A-427 (line)]] | wt | 137 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.3) |
| [[BT-474 (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 39.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +11.5) | — |
| [[CHP-212 (line)]] | wt | 65.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 69.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 67.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +11.0) | — |
| [[NCI-H661 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0794× (z -9.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 26.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +12.7) | — |
| [[SW 1271 (line)]] | alt | 63.5 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0658× (z -8.9) |
| [[SW 900 (line)]] | alt | 35.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00910]] | +0.71 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[TEX14]] | +0.70 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[POLR2A]] | +0.69 | +0.54 / +0.66 | both halves | 1e-05 | STRING 705 |
| [[MEPCE]] | +0.67 | +0.77 / +0.42 | both halves | 4e-05 | STRING 999 |
| [[MED29]] | +0.67 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[BRD2]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 | STRING 560 |
| [[C21orf91]] | +0.65 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CHCHD7]] | +0.64 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[BOLA1]] | +0.64 | +0.73 / +0.39 | both halves | 6e-05 |  |
| [[UBE2D3-AS1]] | +0.63 | +0.71 / +0.36 | both halves | 9e-05 |  |
| [[KMT2E-AS1]] | +0.63 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[KLHL15]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP93]] | -0.61 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[WDR5]] | -0.57 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[FAR1]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[GCSH]] | -0.55 | -0.68 / -0.33 | both halves | 1e-04 |  |
| [[PCGF6]] | -0.55 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[TREX2]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[TALDO1]] | -0.54 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[WRN]] | -0.54 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[XPO5]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[APIP]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ORC5]] | -0.53 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[EDEM2]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HEXIM1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.3, -27.0); signed map (4.3, 15.9). **Vector** length 117, 35.3% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.0 | +11.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.1 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +11.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.5 | +0.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.3 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +1.9 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | +2.4 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.8 | +2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -6.1 | +8.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -5.9 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -5.6 | +8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.1 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | HEXIM P-TEFb complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,148,475-45,152,099 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLP-1, HIS1, MAQ1, EDG1 |
| Gene groups (HGNC) | P-TEFb complex subunits |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [O94992](https://www.uniprot.org/uniprotkb/O94992) (Protein HEXIM1):

> Transcriptional regulator which functions as a general RNA polymerase II transcription inhibitor. Core component of the 7SK RNP complex: in cooperation with 7SK snRNA sequesters P-TEFb in a large inactive 7SK snRNP complex preventing RNA polymerase II phosphorylation and subsequent transcriptional elongation. May also regulate NF-kappa-B, ESR1, NR3C1 and CIITA-dependent transcriptional activity. Plays a role in the regulation of DNA virus-mediated innate immune response by assembling into the …

**Summary**, from NCBI Gene [10614](https://www.ncbi.nlm.nih.gov/gene/10614):

> Expression of this gene is induced by hexamethylene-bis-acetamide in vascular smooth muscle cells. This gene has no introns. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24953) · Entrez [10614](https://www.ncbi.nlm.nih.gov/gene/10614) · UniProt [O94992](https://www.uniprot.org/uniprotkb/O94992) · Ensembl [ENSG00000186834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186834)

## Data

Gene col 11860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11860); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11860]; `tensor/DDL_lfc|DDL_z.npy` [11860]; `embed/gene_vectors.npy` [11860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11860 or target_col == 11860). Every well: [[HEXIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEXIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
