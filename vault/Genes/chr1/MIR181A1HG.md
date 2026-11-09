---
symbol: "MIR181A1HG"
type: "gene"
col: 13728
ensembl_id: "ENSG00000229989"
name: "MIR181A1 host gene"
location: "1q32.1"
module: 24
arm: "+"
pooled_cpm: 118.61
n_lines_expressing: 43
n_dd_up: 38
n_dd_down: 16
n_dd_up_clean: 35
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MIR181A1HG

*MIR181A1 host gene* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.62× (z +10.2, q 8e-22, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.400× (z -19.3, q 0e+00, down in 41 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM30]] (+0.61, fdr 3e-05), [[MMP16]] (+0.56, fdr 1e-05), [[MNAT1]] (+0.56, fdr 6e-05); moves opposite to [[TRPV1]] (-0.49, fdr 2e-04), [[MLYCD]] (-0.48, fdr 4e-04), [[STRADA]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MEF2C]] → it (grade B ⚠); 2 go from it, the strongest it → [[TRPS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 3 with an alert ⚠; shown: the 15 strongest. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +10.2 | 8e-22 | 35/41 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +9.2 | 1e-17 | 35/42 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +8.5 | 3e-15 | 30/41 (NCI-H2347, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +8.2 | 3e-14 | 34/41 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +8.0 | 1e-13 | 22/41 (Hs 766T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +7.8 | 9e-13 | 28/41 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +7.2 | 5e-11 | 23/41 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +6.5 | 4e-09 | 24/41 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.51×** | +6.2 | 4e-08 | 24/41 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Menadione (drug)]] 5 µM |  | **1.52×** | +6.1 | 7e-08 | 32/40 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.32×** | +5.6 | 1e-06 | 30/41 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM |  | **1.28×** | +5.2 | 1e-05 | 24/41 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.0 | 2e-05 | 23/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +4.6 | 2e-04 | 19/41 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.4 | 3e-04 | 23/41 (NCI-H23, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.400×** | -19.3 | 0e+00 | 41/42 (CHP-212, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.309×** | -16.9 | 0e+00 | 31/35 (SK-MEL-2, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.379×** | -14.5 | 3e-45 | 37/42 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -9.0 | 3e-17 | 31/41 (C32, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -8.2 | 3e-14 | 32/43 (A-427, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.593×** | -7.8 | 6e-13 | 32/41 (SW 1271, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.579×** | -7.5 | 4e-12 | 28/38 (CHP-212, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.603×** | -7.2 | 3e-11 | 24/40 (CHP-212, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.741×** | -4.5 | 5e-04 | 22/41 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.739×** | -4.3 | 8e-04 | 22/40 (C32, CHP-212, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.677×** | -4.1 | 0.002 | 22/41 (SK-MEL-2, NCI-H1792, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -4.1 | 0.002 | 22/41 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.623×** | -3.7 | 0.010 | 18/32 (HEC-1-A, C32, …) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -3.4 | 0.027 | 22/38 (RPMI-7951, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.651×** | -3.3 | 0.032 | 16/41 (RPMI-7951, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Uridine (drug)]] 5 µM |  | **0.816×** | -3.0 | 0.088 | 7/42 (CFPAC-1, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 544 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0996× (z -30.9) |
| [[NCI-H460 (line)]] | wt | 159 | 6 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.95× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -22.1) |
| [[NCI-H2347 (line)]] | alt | 60.7 | 5 | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.37× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -14.6) |
| [[A-427 (line)]] | wt | 783 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0859× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0836× (z -24.1) |
| [[SK-MEL-2 (line)]] | alt | 217 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0589× (z -25.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -21.8) |
| [[A498 (line)]] | wt | 35.0 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.11× (z +15.8) | — |
| [[CFPAC-1 (line)]] | alt | 142 | 1 | 5 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.82× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -14.3) |
| [[CHP-212 (line)]] | wt | 859 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0474× (z -35.6) |
| [[HEC-1-A (line)]] | alt | 124 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.9) |
| [[HT-29 (line)]] | alt | 150 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 232 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -25.3) |
| [[SNU-423 (line)]] | alt | 224 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -17.0) |
| [[SW 900 (line)]] | alt | 301 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0895× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -15.3) |
| [[H4 (line)]] | wt | 143 | 1 | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.20× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -15.5) |
| [[KATO III (line)]] | alt | 127 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.6) |
| [[LoVo (line)]] | wt | 61.2 | 5 | 0 | [[Belinostat (drug)]] 5 µM 3.54× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 157 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -17.8) |
| [[LS 180 (line)]] | wt | 127 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 30.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.59× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 69.5 | 4 (4 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 3.57× (z +8.8) ⚠ unreliable plate only | — |
| [[Hs 766T (line)]] | wt | 70.7 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +23.3) | [[Dinaciclib (drug)]] 5 µM 0.0391× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 94.9 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.35× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 92.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 35.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +19.7) | — |
| [[Panc 03.27 (line)]] | alt | 71.9 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 132 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.5) |
| [[SW 1271 (line)]] | alt | 238 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0414× (z -15.8) ⚠ transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -13.6) |
| [[A-172 (line)]] | wt | 90.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 73.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0458× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -10.2) |
| [[HOP62 (line)]] | alt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +9.9) | — |
| [[NCI-H661 (line)]] | alt | 236 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0295× (z -16.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 75.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -12.8) |
| [[SW1417 (line)]] | alt | 72.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 77.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -11.8) |
| [[RKO (line)]] | wt | 50.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -11.2) |
| [[SW 1088 (line)]] | alt | 204 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0808× (z -8.7) |
| [[SW480 (line)]] | alt | 65.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.6) |
| [[A549 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 65.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM30]] | +0.61 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MMP16]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[MNAT1]] | +0.56 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[GGT7]] | +0.56 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[HDAC8]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[HEY1]] | +0.52 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[NBEA]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[ATP5PO]] ⚠ | +0.52 | +0.37 / +0.48 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZC4H2]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ZC3H12B]] | +0.51 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[PSMB1]] | +0.50 | +0.29 / +0.45 | both halves | 3e-04 |  |
| [[TTC3P1]] | +0.50 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[NDUFC2]] | +0.50 | +0.35 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPV1]] | -0.49 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[MLYCD]] | -0.48 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[STRADA]] | -0.47 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[SHPK]] | -0.45 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DUSP22]] | -0.45 | -0.21 / -0.54 | both halves | 6e-04 |  |
| [[MAEA]] | -0.45 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[SIAH2-AS1]] | -0.44 | -0.34 / -0.23 | both halves | 5e-04 |  |
| [[PIGG]] | -0.43 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[SMG1P6]] | -0.43 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[KLF3-AS1]] | -0.42 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[MAF1]] | -0.42 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[ATXN7L3-AS1]] | -0.42 | -0.29 / -0.30 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C]] | B | MEF2C activity raises MIR181A1HG's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 2.60× lower at baseline in the lines without MEF2C | 0.013 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[SMIM10]] | B | SMIM10 activity raises MIR181A1HG's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without SMIM10 | 0.056 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[KC6]] | B | KC6 activity raises MIR181A1HG's level | lines that do not express KC6 (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without KC6 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[XKR6]] | B | XKR6 activity raises MIR181A1HG's level | lines that do not express XKR6 (18) vs lines expressing it (32) | 1.81× lower at baseline in the lines without XKR6 | 0.085 | ⚠ within organs, on part of the lines; also absent: CIART, RNF182, LINC00702 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPS1]] | B | MIR181A1HG activity raises TRPS1's level | lines that do not express MIR181A1HG (7) vs lines expressing it (43) | 4.41× lower at baseline in the lines without MIR181A1HG | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NDUFC2]] | B | MIR181A1HG activity raises NDUFC2's level | lines that do not express MIR181A1HG (7) vs lines expressing it (43) | 1.39× lower at baseline in the lines without MIR181A1HG | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.282). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-22.0, 29.1); signed map (-6.8, 12.8). **Vector** length 117, 32.3% of its response variance represented; |z| ≥ 3 in 1,465 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.1 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.2 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.0 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.0 | +8.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.9 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +2.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.3 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -19.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -9.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.2 | -4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.7 | -16.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | MIR181A1 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.1 — chr1:198,777,861-198,937,471 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100131234](https://www.ncbi.nlm.nih.gov/gene/100131234):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:48659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48659) · Entrez [100131234](https://www.ncbi.nlm.nih.gov/gene/100131234) · Ensembl [ENSG00000229989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229989)

## Data

Gene col 13728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13728); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13728]; `tensor/DDL_lfc|DDL_z.npy` [13728]; `embed/gene_vectors.npy` [13728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13728 or target_col == 13728). Every well: [[MIR181A1HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR181A1HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
