---
symbol: "FBXL8"
type: "gene"
col: 5746
ensembl_id: "ENSG00000135722"
name: "F-box and leucine rich repeat protein 8"
location: "16q22.1"
module: 11
arm: "-"
pooled_cpm: 10.4
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# FBXL8

*F-box and leucine rich repeat protein 8* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.94× (z +15.8, q 0e+00, up in 13 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +6.8, q 2e-09, up in 24 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H2030 5.37×, A498 6.14×, SW480 4.11×, NCI-H2347 7.17×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 11.6×, KATO III 8.28×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.437× (z -14.0, q 2e-41, down in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.332× (z -13.1, q 6e-37, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSF4]] (+0.72, fdr 7e-06, ⚠ same locus), [[NUCB1]] (+0.56, fdr 2e-05), [[NRSN2]] (+0.55, fdr 2e-05), [[VSIG10L]] (+0.53, fdr 8e-05); moves opposite to [[PET117]] (-0.55, fdr 3e-04), [[MRPL15]] (-0.53, fdr 3e-05), [[ZNF22]] (-0.51, fdr 4e-04).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5746.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H2030 5.37×, A498 6.14×, SW480 4.11×, NCI-H2347 7.17×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 11.6×, KATO III 8.28×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +15.8 | 0e+00 | 13/19 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +9.2 | 1e-17 | 22/34 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +8.8 | 3e-16 | 11/23 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.8 | 2e-09 | 24/44 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.057 | 16/47 (A-172, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.437×** | -14.0 | 2e-41 | 35/46 (A549, SHP-77, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.332×** | -13.1 | 6e-37 | 38/44 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.341×** | -12.8 | 2e-35 | 37/43 (J82, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.412×** | -10.6 | 7e-24 | 36/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.404×** | -10.4 | 3e-23 | 38/46 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.458×** | -9.3 | 1e-18 | 35/46 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.458×** | -9.3 | 1e-18 | 33/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.471×** | -9.0 | 2e-17 | 35/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.509×** | -8.0 | 5e-14 | 35/47 (HS-578T, RKO, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.522×** | -7.7 | 5e-13 | 28/47 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.583×** | -6.4 | 7e-09 | 27/47 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.586×** | -6.4 | 1e-08 | 26/47 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.614×** | -5.8 | 3e-07 | 21/45 (NCI-H1573, NCI-H1792, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.419×** | -5.4 | 2e-06 | 26/47 (A549, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.601×** | -5.4 | 3e-06 | 25/46 (H4, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.641×** | -5.1 | 1e-05 | 19/47 (A549, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.744×** | -5.0 | 2e-05 | 23/47 (NCI-H460, A549, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -4.1 | 1e-03 | 16/44 (C32, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.737×** | -3.5 | 0.012 | 18/46 (CFPAC-1, H4, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.743×** | -3.4 | 0.017 | 12/45 (A498, J82, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.598×** | -3.2 | 0.031 | 10/45 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -2.8 | 0.095 | 14/45 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 15.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -17.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.105× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -8.7) |
| [[SW480 (line)]] | alt | 11.8 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.11× (z +8.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -11.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -10.4) |
| [[A-172 (line)]] | wt | 20.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0883× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~58% of this change |
| [[H4 (line)]] | wt | 18.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0706× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.118× (z -8.7) |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0664× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 7.06 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.28× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.175× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 20.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.37× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -10.3) |
| [[C32 (line)]] | wt | 9.29 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0704× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.106× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0837× (z -11.4) |
| [[PANC-1 (line)]] | alt | 9.16 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 8.42 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0547× (z -11.0) |
| [[A-427 (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -9.0) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A498 (line)]] | wt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 3.86 | 0 | 1 (1 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM 0.0644× (z -8.9) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -9.1) |
| [[HS-578T (line)]] | alt | 6.82 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.120× (z -8.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HT-29 (line)]] | alt | 6.49 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0726× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 6.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.6× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 7.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0685× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 4.87 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.17× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 8.06 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0581× (z -11.4) |
| [[RKO (line)]] | wt | 5.30 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.05 µM 0.0654× (z -8.7) |
| [[SHP-77 (line)]] | alt | 8.21 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0823× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 18 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSF4]] | +0.72 | +0.76 / +0.69 | both halves | 7e-06 | ⚠ same locus (0.1 kb, same strand: neighbours can correlate without regulation) |
| [[NUCB1]] | +0.56 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[NRSN2]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[VSIG10L]] | +0.53 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[CYP27C1]] | +0.53 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[NLGN2]] | +0.52 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[CACNG6]] | +0.52 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[ATN1]] | +0.50 | +0.24 / +0.62 | both halves | 5e-04 |  |
| [[VAMP1]] | +0.50 | +0.33 / +0.37 | both halves | 1e-04 |  |
| [[SDF4]] | +0.50 | +0.26 / +0.58 | both halves | 4e-04 |  |
| [[GNAS]] | +0.49 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[THBS3]] | +0.49 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[BHLHE40-AS1]] | +0.49 | +0.21 / +0.50 | both halves | 6e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PET117]] | -0.55 | -0.27 / -0.60 | both halves | 3e-04 |  |
| [[MRPL15]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ZNF22]] | -0.51 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[MRPS18B]] | -0.51 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[NUDT11]] | -0.51 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[VPS8]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[KRI1]] | -0.47 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[VPS25]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[KBTBD6]] | -0.46 | -0.20 / -0.59 | ⚠ one half (not replicated) | 8e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[KAT14]] | -0.45 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[PIGBOS1]] | -0.45 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[DMAC1]] | -0.45 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[MRPL36]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.345). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (23.5, -33.4); signed map (52.2, -17.8). **Vector** length 63.8, 10.4% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -13.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -5.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,159,932-67,164,570 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Fbl8 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CD0](https://www.uniprot.org/uniprotkb/Q96CD0) (F-box/LRR-repeat protein 8):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex.

**Summary**, from NCBI Gene [55336](https://www.ncbi.nlm.nih.gov/gene/55336):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:17875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17875) · Entrez [55336](https://www.ncbi.nlm.nih.gov/gene/55336) · UniProt [Q96CD0](https://www.uniprot.org/uniprotkb/Q96CD0) · Ensembl [ENSG00000135722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135722)

## Data

Gene col 5746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5746); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5746]; `tensor/DDL_lfc|DDL_z.npy` [5746]; `embed/gene_vectors.npy` [5746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5746 or target_col == 5746). Every well: [[FBXL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
