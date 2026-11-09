---
symbol: "FLOT2"
type: "gene"
col: 5342
ensembl_id: "ENSG00000132589"
name: "flotillin 2"
location: "17q11.2"
module: 3
arm: "-"
pooled_cpm: 30.03
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 29
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# FLOT2

*flotillin 2* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.60× (z +14.3, q 1e-43, up in 30 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.35× (z +4.7, q 3e-04, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.472× (z -16.5, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX11]] (+0.54, fdr 4e-05), [[ARPIN]] (+0.54, fdr 3e-05), [[STOM]] (+0.52, fdr 3e-05); moves opposite to [[SEC61G]] (-0.52, fdr 7e-05), [[POLR2J3-1]] (-0.52, fdr 4e-05), [[UBA52]] (-0.50, fdr 6e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STOM]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SEPTIN11]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +14.3 | 1e-43 | 30/35 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +13.3 | 6e-38 | 41/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +7.8 | 1e-12 | 30/40 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.2 | 9e-11 | 6/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 3e-04 | 24/47 (NCI-H1792, KATO III, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.003 | 22/45 (MIA PaCa-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.003 | 20/48 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.012 | 19/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.054 | 8/44 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +3.3 | 0.054 | 13/45 (HS-578T, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.057 | 8/48 (A498, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.078 | 15/45 (SHP-77, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.089 | 11/48 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.11 | 11/47 (A549, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.472×** | -16.5 | 0e+00 | 39/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.458×** | -12.1 | 2e-31 | 42/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.511×** | -10.4 | 3e-23 | 38/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.527×** | -10.0 | 3e-21 | 36/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -8.8 | 1e-16 | 33/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.552×** | -8.7 | 3e-16 | 42/48 (HT-29, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.574×** | -8.6 | 6e-16 | 32/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.578×** | -8.5 | 1e-15 | 35/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -8.4 | 3e-15 | 34/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -8.4 | 3e-15 | 35/46 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -8.3 | 5e-15 | 30/48 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -7.5 | 4e-12 | 35/47 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.441×** | -6.5 | 4e-09 | 30/42 (SHP-77, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.700×** | -5.4 | 2e-06 | 24/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.796×** | -5.0 | 2e-05 | 26/47 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.735×** | -4.7 | 1e-04 | 26/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.769×** | -4.0 | 0.002 | 21/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.786×** | -3.7 | 0.006 | 22/47 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.2 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.9) |
| [[HT-29 (line)]] | alt | 36.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 94.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +13.4) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.475× (z -9.3) |
| [[LoVo (line)]] | wt | 33.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.3) |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -11.4) |
| [[HOP62 (line)]] | alt | 36.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 39.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.2) ⚠ cell-cycle shift, explains ~14% of this change |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.273× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 31.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 24.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.5) |
| [[RKO (line)]] | wt | 30.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.4) |
| [[SHP-77 (line)]] | alt | 49.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.315× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.3) |
| [[SNU-423 (line)]] | alt | 29.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -12.4) |
| [[SW1417 (line)]] | alt | 22.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -8.5) |
| [[SW480 (line)]] | alt | 31.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.7) |
| [[A-172 (line)]] | wt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.4) |
| [[C32 (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.2) |
| [[Hs 766T (line)]] | wt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.9) |
| [[KATO III (line)]] | alt | 26.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.261× (z -9.7) |
| [[LS 180 (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.60× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.0) |
| [[A-427 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX11]] | +0.54 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[ARPIN]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[STOM]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 | pathway: RHOA GTPase cycle; STRING 868 |
| [[HNRNPK]] | +0.52 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[USP39]] | +0.52 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[UHMK1]] | +0.52 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ZNF33B]] | +0.51 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[PTPA]] | +0.51 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[CPNE1]] | +0.51 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[MTA2]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[YWHAE]] | +0.51 | +0.40 / +0.47 | both halves | 5e-05 | pathway: Programmed Cell Death |
| [[SSU72]] | +0.50 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61G]] | -0.52 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[POLR2J3-1]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[UBA52]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 | pathway: Programmed Cell Death |
| [[CAMLG]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RPL36AL]] ⚠ | -0.49 | -0.40 / -0.42 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SELENOK]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[RPL18]] ⚠ | -0.49 | -0.40 / -0.44 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | -0.48 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[SPCS1]] | -0.48 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[KATNBL1]] | -0.47 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[FTL]] | -0.47 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[CCDC82]] | -0.46 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[EMC6]] | -0.46 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[TMEM258]] | -0.46 | -0.36 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STOM]] | B | STOM activity lowers FLOT2's level | lines that do not express STOM (16) vs lines expressing it (34) | 1.35× higher at baseline in the lines without STOM | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000227355, TRIM6, AOX1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN11]] | C | FLOT2's natural level strengthens SEPTIN11's drug response | FLOT2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.04; direction clear | 0.007 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.396). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.5, -27.2); signed map (15.2, -42.3). **Vector** length 80.8, 19.2% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.4 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | +4.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.1 | +0.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.6 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -12.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.1 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.6 | -5.0 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | flotillin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,879,335-28,897,733 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ESA, ESA1, ECS-1, ECS1; previously M17S1 |
| Gene groups (HGNC) | Flotillins |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 15 pathways, smallest: Synaptic adhesion-like molecules; RIPK1-mediated regulated necrosis; Regulation of necroptotic cell death |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14254](https://www.uniprot.org/uniprotkb/Q14254) (Flotillin-2):

> May act as a scaffolding protein within caveolar membranes, functionally participating in formation of caveolae or caveolae-like vesicles. May be involved in epidermal cell adhesion and epidermal structure and function.

**Summary**, from NCBI Gene [2319](https://www.ncbi.nlm.nih.gov/gene/2319):

> Caveolae are small domains on the inner cell membrane involved in vesicular trafficking and signal transduction. This gene encodes a caveolae-associated, integral membrane protein, which is thought to function in neuronal signaling. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3758) · Entrez [2319](https://www.ncbi.nlm.nih.gov/gene/2319) · UniProt [Q14254](https://www.uniprot.org/uniprotkb/Q14254) · Ensembl [ENSG00000132589](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132589)

## Data

Gene col 5342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5342); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5342]; `tensor/DDL_lfc|DDL_z.npy` [5342]; `embed/gene_vectors.npy` [5342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5342 or target_col == 5342). Every well: [[FLOT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLOT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
