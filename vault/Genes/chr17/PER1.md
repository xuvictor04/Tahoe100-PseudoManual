---
symbol: "PER1"
type: "gene"
col: 10997
ensembl_id: "ENSG00000179094"
name: "period circadian regulator 1"
location: "17p13.1"
module: 106
arm: "+"
pooled_cpm: 67.91
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 15
n_dd_up_clean: 26
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# PER1

*period circadian regulator 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.1× (z +27.0, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.476× (z -5.7, q 7e-06, down in 29 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.515× (z -5.3, q 3e-05, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YY1AP1]] (+0.70, fdr 7e-06), [[NFKBIA]] (+0.65, fdr 7e-06), [[FLVCR2]] (+0.64, fdr 7e-06); moves opposite to [[ARPC5]] (-0.60, fdr 1e-05), [[CCT6A]] (-0.59, fdr 4e-05), [[VCP]] (-0.57, fdr 2e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.1×** | +27.0 | 0e+00 | 47/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.98×** | +13.6 | 7e-40 | 46/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **5.27×** | +13.2 | 2e-37 | 47/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.40×** | +11.7 | 1e-29 | 45/47 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.08×** | +11.2 | 8e-27 | 46/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **9.81×** | +9.5 | 3e-19 | 47/48 (NCI-H2347, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **7.36×** | +8.3 | 1e-14 | 43/47 (SW48, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.79×** | +8.1 | 3e-14 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.67×** | +7.8 | 5e-13 | 41/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +5.2 | 1e-05 | 35/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.01×** | +5.0 | 3e-05 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.88×** | +5.0 | 3e-05 | 32/47 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.52×** | +4.7 | 1e-04 | 30/47 (LoVo, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.1 | 0.001 | 30/46 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.76×** | +4.1 | 0.002 | 28/49 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.008 | 27/47 (KATO III, SW48, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.009 | 31/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10997.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.476×** | -5.7 | 7e-06 | 29/42 (Hs 766T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.515×** | -5.3 | 3e-05 | 37/47 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.586×** | -4.3 | 0.004 | 30/46 (SNU-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.599×** | -4.1 | 0.006 | 33/48 (HCT15, PANC-1, …) | top dose only | position effect removed |
| [[Megestrol (drug)]] 5 µM |  | **0.700×** | -4.0 | 0.006 | 29/48 (SW1417, SW48, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.646×** | -3.5 | 0.044 | 30/47 (MIA PaCa-2, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **0.619×** | -3.4 | 0.047 | 28/48 (KATO III, HOP62, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.062 | 24/47 (HCT15, SW480, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.635×** | -3.3 | 0.070 | 28/47 (NCI-H661, SHP-77, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.642×** | -3.2 | 0.076 | 31/48 (SW48, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.672×** | -3.2 | 0.076 | 26/47 (SW48, A-427, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.649×** | -3.1 | 0.090 | 25/47 (KATO III, A549, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.479×** | -3.1 | 0.093 | 26/47 (NCI-H661, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.686×** | -3.0 | 0.100 | 22/47 (SW1417, J82, …) | inconsistent across doses | position effect removed |
| [[Brimonidine (drug)]] 5 µM |  | **0.687×** | -3.0 | 0.100 | 27/47 (HEC-1-A, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.7 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.6× (z +26.2) | — |
| [[SW480 (line)]] | alt | 56.0 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +22.0) | — |
| [[PANC-1 (line)]] | alt | 42.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +27.3) | — |
| [[SW48 (line)]] | wt | 65.6 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.3× (z +21.6) | — |
| [[A-427 (line)]] | wt | 78.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +24.5) | — |
| [[COLO 205 (line)]] | alt | 28.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 71.7× (z +25.7) | — |
| [[HOP62 (line)]] | alt | 79.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +17.5) | — |
| [[LoVo (line)]] | wt | 35.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +22.2) | — |
| [[LOX-IMVI (line)]] | wt | 64.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.11× (z +20.0) | — |
| [[NCI-H1792 (line)]] | alt | 34.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +17.0) | — |
| [[SW 900 (line)]] | alt | 124 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +20.7) | — |
| [[A549 (line)]] | wt | 77.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +24.2) | — |
| [[Hs 766T (line)]] | wt | 66.4 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 55.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +20.6) | — |
| [[LS 180 (line)]] | wt | 30.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +18.3) | — |
| [[NCI-H1573 (line)]] | alt | 91.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +21.9) | — |
| [[NCI-H2347 (line)]] | alt | 58.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +22.3) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 69.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +23.3) | — |
| [[A-172 (line)]] | wt | 75.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +21.7) | — |
| [[AsPC-1 (line)]] | alt | 67.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.8× (z +25.6) | — |
| [[BT-474 (line)]] | alt | 63.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 52.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.7× (z +23.1) | — |
| [[HT-29 (line)]] | alt | 47.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +20.2) | — |
| [[J82 (line)]] | alt | 48.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +17.8) | — |
| [[NCI-H23 (line)]] | alt | 146 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +18.2) | — |
| [[A498 (line)]] | wt | 80.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +18.9) | — |
| [[H4 (line)]] | wt | 71.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +20.0) | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -11.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 105 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +17.7) | — |
| [[RPMI-7951 (line)]] | alt | 106 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +20.7) | — |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 102 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0746× (z -11.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 132 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 50.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +19.3) | — |
| [[HS-578T (line)]] | alt | 85.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +17.3) | — |
| [[Panc 03.27 (line)]] | alt | 42.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +21.6) | — |
| [[RKO (line)]] | wt | 23.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 99.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +15.9) | — |
| [[SNU-423 (line)]] | alt | 77.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +16.4) | — |
| [[AN3 CA (line)]] | alt | 115 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 68.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 75.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +18.4) | — |
| [[CHP-212 (line)]] | wt | 81.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 76.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.53× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 63.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +10.7) | — |
| [[SW 1271 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[NFKBIA]] | +0.65 | +0.58 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[FLVCR2]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | same gene group |
| [[KLF9]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TSC22D3]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 | STRING 488 |
| [[BCL6]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GADD45B]] | +0.60 | +0.62 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EDN2]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[TNFAIP3]] | +0.60 | +0.57 / +0.60 | both halves | 9e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IRS2]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PHF21A]] | +0.59 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[ESYT2]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC5]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.59 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[VCP]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[ZNF731P]] | -0.56 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[PSMD1]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 | pathway: Circadian clock |
| [[PSMD2]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 | pathway: Circadian clock |
| [[TTL]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[HSP90AA1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CCT3]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[GATAD2A]] | -0.54 | -0.46 / -0.55 | both halves | 2e-05 | same gene group |
| [[NUDC]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[NIPAL1]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises PER1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.1, 14.3); signed map (15.0, 28.6). **Vector** length 117, 44.4% of its response variance represented; |z| ≥ 3 in 1,367 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Triamcinolone (drug)]] 5 µM |  | +5.5 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +4.9 | +3.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.9 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.5 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.1 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | period circadian regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,140,472-8,156,506 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIGUI; previously PER |
| Gene groups (HGNC) | MicroRNA protein coding host genes; PAS domain containing; Period circadian regulator family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 6 pathways, smallest: Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; Phosphorylation and nuclear translocation of the CRY:PER:kinase complex; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O15534](https://www.uniprot.org/uniprotkb/O15534) (Period circadian protein homolog 1):

> Transcriptional repressor which forms a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, …

**Summary**, from NCBI Gene [5187](https://www.ncbi.nlm.nih.gov/gene/5187):

> This gene is a member of the Period family of genes and is expressed in a circadian pattern in the suprachiasmatic nucleus, the primary circadian pacemaker in the mammalian brain. Genes in this family encode components of the circadian rhythms of locomotor activity, metabolism, and behavior. This gene is upregulated by CLOCK/ARNTL heterodimers but then represses this upregulation in a feedback loop using PER/CRY heterodimers to interact with CLOCK/ARNTL. Polymorphisms in this gene may increase …

**Accessions** — [HGNC:8845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8845) · Entrez [5187](https://www.ncbi.nlm.nih.gov/gene/5187) · UniProt [O15534](https://www.uniprot.org/uniprotkb/O15534) · Ensembl [ENSG00000179094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179094)

## Data

Gene col 10997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10997); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10997]; `tensor/DDL_lfc|DDL_z.npy` [10997]; `embed/gene_vectors.npy` [10997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10997 or target_col == 10997). Every well: [[PER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
