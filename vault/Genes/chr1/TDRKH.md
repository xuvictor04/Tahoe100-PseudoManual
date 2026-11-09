---
symbol: "TDRKH"
type: "gene"
col: 11244
ensembl_id: "ENSG00000182134"
name: "tudor and KH domain containing"
location: "1q21.3"
module: 208
arm: "+"
pooled_cpm: 11.35
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 14
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# TDRKH

*tudor and KH domain containing* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.23× (z +25.8, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.518× (z -9.3, q 6e-18, down in 27 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.393× (z -6.9, q 1e-09, down in 20 of 39 measured lines).
> Its strongest partners by |cos| (50 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 50 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABTB1]] (+0.54, fdr 0.002, ⚠ one half only (not replicated)), [[LPIN1]] (+0.54, fdr 3e-05), [[NPC1]] (+0.51, fdr 1e-04), [[RHOC]] (+0.51, fdr 3e-04); moves opposite to [[RAF1]] (-0.50, fdr 1e-04), [[NDUFS3]] (-0.49, fdr 0.002, ⚠ not reproduced), [[MAIP1]] (-0.48, fdr 0.002, ⚠ not reproduced), [[TDRD3]] (-0.47, fdr 6e-04), [[RBM26]] (-0.44, fdr 2e-04).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MMP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.23×** | +25.8 | 0e+00 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.10×** | +25.6 | 0e+00 | 46/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.57×** | +21.5 | 0e+00 | 45/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.03×** | +10.0 | 3e-21 | 37/46 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +9.7 | 3e-20 | 25/43 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +9.0 | 2e-17 | 33/40 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +8.7 | 3e-16 | 28/46 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +8.4 | 3e-15 | 12/18 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.74×** | +7.5 | 6e-12 | 30/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.3 | 2e-11 | 19/31 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.2 | 2e-11 | 24/47 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.2 | 3e-11 | 23/41 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.6 | 1e-09 | 21/43 (Hs 766T, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.9 | 2e-07 | 17/44 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +5.7 | 6e-07 | 12/24 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.5 | 2e-06 | 16/42 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +5.0 | 2e-05 | 19/44 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 2e-05 | 19/44 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.518×** | -9.3 | 6e-18 | 27/46 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.393×** | -6.9 | 1e-09 | 20/39 (C-33 A, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.600×** | -5.2 | 4e-05 | 19/43 (SNU-1, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.499×** | -5.2 | 4e-05 | 17/41 (SW1417, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.582×** | -4.0 | 0.007 | 15/42 (Hs 766T, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.588×** | -3.9 | 0.007 | 11/42 (Hs 766T, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.608×** | -3.7 | 0.018 | 14/35 (SHP-77, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.702×** | -3.6 | 0.024 | 11/47 (NCI-H661, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.781×** | -3.5 | 0.027 | 15/42 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.715×** | -3.4 | 0.038 | 9/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.790×** | -3.4 | 0.039 | 13/46 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.781×** | -3.3 | 0.040 | 10/44 (AN3 CA, C32, …) | all doses, flat |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.797×** | -3.2 | 0.053 | 8/46 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.650×** | -3.2 | 0.055 | 12/44 (MIA PaCa-2, A498, …) | all doses, flat | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.78× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 5.47 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 17.0× (z +14.5) | — |
| [[A-172 (line)]] | wt | 13.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.41× (z +12.7) | — |
| [[A498 (line)]] | wt | 8.00 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.63× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.08× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 7.59 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 13.5× (z +10.7) | [[EX229 (drug)]] 0.05 µM 0.0564× (z -11.1) |
| [[J82 (line)]] | alt | 14.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.06× (z +11.4) | — |
| [[LoVo (line)]] | wt | 5.55 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.99× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.00 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 15.5× (z +9.5) | [[MK-8353 (drug)]] 0.05 µM 0.0499× (z -9.8) |
| [[LS 180 (line)]] | wt | 6.21 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.80× (z +10.7) | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.32× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 12.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.61× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -11.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 9.30 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.93× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 18.9× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 14.1 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 5.70× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 11.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +11.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0815× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~6% of this change |
| [[HOP62 (line)]] | alt | 4.17 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 13.4× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 11.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.57× (z +9.8) | — |
| [[KATO III (line)]] | alt | 13.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.19× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.22× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.23× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 7.99 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.22× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 19.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 27.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -12.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 18.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.99× (z +8.6) | — |
| [[A-427 (line)]] | wt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -12.4) |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0878× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 39 of them with an alert (⚠; 39 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABTB1]] | +0.54 | +0.12 / +0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[LPIN1]] | +0.54 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[NPC1]] | +0.51 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[RHOC]] | +0.51 | +0.28 / +0.39 | both halves | 3e-04 |  |
| [[DYNLT3]] | +0.50 | +0.29 / +0.42 | both halves | 3e-04 |  |
| [[EHBP1L1]] | +0.50 | +0.15 / +0.35 | ⚠ not reproduced | 0.001 |  |
| [[RNF123]] | +0.50 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[CRIPT]] | +0.48 | +0.06 / +0.53 | ⚠ one half (not replicated) | 0.004 |  |
| [[CSGALNACT2]] | +0.48 | +0.21 / +0.48 | both halves | 7e-04 |  |
| [[ENTPD4]] | +0.48 | +0.10 / +0.48 | ⚠ not reproduced | 0.002 |  |
| [[JOSD1]] | +0.48 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[EFL1]] | +0.47 | +0.35 / +0.35 | both halves | 1e-04 |  |
| [[HIF1AN]] | +0.47 | +0.25 / +0.41 | both halves | 4e-04 |  |
| [[PI4K2A]] | +0.46 | +0.33 / +0.37 | both halves | 1e-04 |  |
| [[RANGAP1]] | +0.46 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[SEPTIN10]] | +0.46 | +0.28 / +0.31 | both halves | 3e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 7 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAF1]] | -0.50 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[NDUFS3]] | -0.49 | -0.14 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[MAIP1]] | -0.48 | -0.12 / -0.46 | ⚠ not reproduced | 0.002 |  |
| [[TDRD3]] | -0.47 | -0.22 / -0.46 | both halves | 6e-04 | same gene group; STRING 518 |
| [[CNPY2]] | -0.45 | -0.07 / -0.45 | ⚠ not reproduced | 0.004 |  |
| [[TNPO2]] | -0.44 | -0.15 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[NGDN]] | -0.44 | -0.16 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[RBM26]] | -0.44 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[CCNT2]] | -0.44 | -0.23 / -0.32 | both halves | 5e-04 |  |
| [[FAM120C]] | -0.43 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[ZCCHC8]] | -0.43 | -0.14 / -0.38 | ⚠ not reproduced | 0.002 |  |
| [[RBM5]] | -0.43 | -0.16 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[RPRD1B]] | -0.42 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[PPP4R3A]] | -0.42 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[ADNP]] | -0.41 | -0.21 / -0.47 | both halves | 7e-04 |  |
| [[SUPV3L1]] | -0.41 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ZNF148]] | -0.40 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[MED4]] | -0.40 | -0.21 / -0.34 | both halves | 6e-04 |  |
| [[GAS2]] | -0.40 | -0.20 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP1]] | B | MMP1 activity lowers TDRKH's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.43× higher at baseline in the lines without MMP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[TOP2A]] | B | TOP2A activity lowers TDRKH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.7, -48.0); signed map (-8.7, 44.3). **Vector** length 68.6, 12.0% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +7.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +3.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +8.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +4.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -9.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -5.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | tudor and KH domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,770,107-151,791,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TDRD2 |
| Gene groups (HGNC) | Tudor domain containing |
| Reactome | 2 pathways, smallest: PIWI-interacting RNA (piRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2W6](https://www.uniprot.org/uniprotkb/Q9Y2W6) (Tudor and KH domain-containing protein):

> Participates in the primary piRNA biogenesis pathway and is required during spermatogenesis to repress transposable elements and prevent their mobilization, which is essential for the germline integrity. The piRNA metabolic process mediates the repression of transposable elements during meiosis by forming complexes composed of piRNAs and Piwi proteins and govern the methylation and subsequent repression of transposons. Required for the final steps of primary piRNA biogenesis by participating in …

**Summary**, from NCBI Gene [11022](https://www.ncbi.nlm.nih.gov/gene/11022):

> Predicted to enable RNA binding activity. Predicted to be involved in several processes, including P granule organization; male meiotic nuclear division; and piRNA processing. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11713) · Entrez [11022](https://www.ncbi.nlm.nih.gov/gene/11022) · UniProt [Q9Y2W6](https://www.uniprot.org/uniprotkb/Q9Y2W6) · Ensembl [ENSG00000182134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182134)

## Data

Gene col 11244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11244); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11244]; `tensor/DDL_lfc|DDL_z.npy` [11244]; `embed/gene_vectors.npy` [11244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11244 or target_col == 11244). Every well: [[TDRKH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDRKH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
