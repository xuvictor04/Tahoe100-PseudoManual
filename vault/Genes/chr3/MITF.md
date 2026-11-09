---
symbol: "MITF"
type: "gene"
col: 11886
ensembl_id: "ENSG00000187098"
name: "melanocyte inducing transcription factor"
location: "3p13"
module: 17
arm: "+"
pooled_cpm: 36.54
n_lines_expressing: 41
n_dd_up: 29
n_dd_down: 19
n_dd_up_clean: 26
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MITF

*melanocyte inducing transcription factor* — 3p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 4.10× (z +25.3, q 0e+00, up in 35 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.488× (z -12.9, q 4e-35, down in 29 of 39 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.615× (z -8.7, q 9e-16, down in 27 of 39 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SASH1]] (+0.54, fdr 5e-05), [[HERC1]] (+0.52, fdr 1e-04), [[NEK7]] (+0.49, fdr 4e-04); moves opposite to [[APTX]] (-0.45, fdr 2e-04), [[SLC30A6]] (-0.44, fdr 3e-05), [[MRPS25]] (-0.44, fdr 3e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMCC2]] → it (grade B ⚠); 3 go from it, the strongest it → [[TMCC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **4.10×** | +25.3 | 0e+00 | 35/39 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.64×** | +23.2 | 0e+00 | 34/39 (NCI-H2347, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.56×** | +22.8 | 0e+00 | 34/39 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.19×** | +20.8 | 0e+00 | 31/39 (NCI-H2347, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.74×** | +18.1 | 0e+00 | 34/39 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +14.8 | 0e+00 | 23/39 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +14.6 | 0e+00 | 28/39 (SW480, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **4.14×** | +13.3 | 9e-39 | 32/39 (NCI-H2347, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +12.9 | 4e-36 | 25/38 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +9.5 | 2e-19 | 22/39 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +8.5 | 1e-15 | 24/39 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +8.2 | 2e-14 | 21/39 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +6.7 | 8e-10 | 21/38 (A-172, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.47×** | +6.6 | 1e-09 | 20/38 (CFPAC-1, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.43×** | +6.2 | 3e-08 | 18/39 (SW480, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +6.2 | 3e-08 | 21/40 (PANC-1, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +5.9 | 9e-08 | 17/38 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11886.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.488×** | -12.9 | 4e-35 | 29/39 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.615×** | -8.7 | 9e-16 | 27/39 (C32, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.444×** | -7.6 | 5e-12 | 26/39 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -6.1 | 1e-07 | 15/26 (NCI-H2030, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.524×** | -6.1 | 1e-07 | 23/39 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.644×** | -5.6 | 2e-06 | 19/39 (A498, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.567×** | -5.3 | 8e-06 | 22/39 (LOX-IMVI, A498, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.577×** | -5.2 | 2e-05 | 21/39 (NCI-H2030, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.756×** | -5.0 | 3e-05 | 20/36 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.766×** | -4.8 | 9e-05 | 16/38 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 0.05 µM |  | **0.758×** | -4.7 | 1e-04 | 16/39 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.697×** | -4.6 | 2e-04 | 14/39 (HEC-1-A, NCI-H2030, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.842× | -4.4 | 6e-04 | 13/39 (A-172, SW 900, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.652×** | -4.0 | 0.002 | 12/35 (SHP-77, C32, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.823×** | -3.5 | 0.018 | 11/39 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.766×** | -3.4 | 0.023 | 13/39 (HEC-1-A, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.831×** | -3.3 | 0.028 | 11/38 (A-427, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.705×** | -3.3 | 0.032 | 14/37 (NCI-H2030, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.034 | 11/39 (A-427, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 90.2 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +14.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -9.9) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 294 | 0 | 8 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.176× (z -13.5) |
| [[SW1417 (line)]] | alt | 29.0 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.199× (z -11.4) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 48.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.2) | — |
| [[NCI-H460 (line)]] | wt | 17.7 | 7 | 0 | [[Belinostat (drug)]] 5 µM 4.51× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +12.2) | — |
| [[SW480 (line)]] | alt | 9.46 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 33.8 | 6 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 5.84× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.35× (z +9.7) | — |
| [[J82 (line)]] | alt | 27.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.77× (z +11.5) | — |
| [[LoVo (line)]] | wt | 12.6 | 6 | 0 | [[Belinostat (drug)]] 5 µM 8.05× (z +13.6) | — |
| [[A498 (line)]] | wt | 28.8 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +17.6) | [[Auranofin (drug)]] 5 µM 0.411× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 187 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -11.5) |
| [[A549 (line)]] | wt | 52.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.62× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 21.4 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 5.03× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -9.0) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 14.0 | 4 | 0 | [[Belinostat (drug)]] 5 µM 5.97× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 23.8 | 4 | 0 | [[Belinostat (drug)]] 5 µM 3.31× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 30.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.39× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 27.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 25.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.79× (z +10.4) | — |
| [[RKO (line)]] | wt | 26.6 | 3 | 0 | [[Panobinostat (drug)]] 0.05 µM 4.80× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.79× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 77.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0716× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 55.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 15.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 7.39× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 1 | 0 | [[Belinostat (drug)]] 5 µM 6.96× (z +8.5) | — |
| [[A-172 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SASH1]] | +0.54 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[HERC1]] | +0.52 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[NEK7]] | +0.49 | +0.26 / +0.55 | both halves | 4e-04 |  |
| [[PLCB4]] | +0.49 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[MAGI1]] | +0.49 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[ARHGAP17]] | +0.48 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[ELAPOR2]] | +0.47 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[MOXD1]] | +0.47 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[NEGR1]] | +0.46 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[TAB2]] | +0.46 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[ANKRD13A]] | +0.45 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[RAB30]] | +0.45 | +0.38 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTX]] | -0.45 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[SLC30A6]] | -0.44 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[MRPS25]] | -0.44 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[ACAD9]] | -0.43 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[XPNPEP3]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[LINC02935]] | -0.43 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SMG1P6]] | -0.42 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[TM4SF19]] | -0.42 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[EXOSC3]] | -0.41 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[AIFM2]] | -0.41 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[GLIPR1-AS1]] | -0.41 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[PPP4R3B]] | -0.41 | -0.20 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[ZCCHC4]] | -0.41 | -0.34 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCC2]] | B | TMCC2 activity raises MITF's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 4.38× lower at baseline in the lines without TMCC2 | 0.064 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MITF's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[TMOD2]] | C | TMOD2 activity raises MITF's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 5.57× lower at baseline in the lines without TMOD2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCC2]] | B | MITF activity raises TMCC2's level | lines that do not express MITF (9) vs lines expressing it (41) | 2.25× lower at baseline in the lines without MITF | 0.008 | ⚠ within organs, on part of the lines; also absent: LRP12, DUBR, CYP46A1 |
| [[ZNF621]] | B | MITF activity raises ZNF621's level | lines that do not express MITF (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without MITF | 0.083 | ⚠ within organs, on part of the lines; also absent: LRP12, DUBR, CYP46A1 |
| [[TSPAN2]] | B | MITF activity raises TSPAN2's level | lines that do not express MITF (9) vs lines expressing it (41) | 1.80× lower at baseline in the lines without MITF | 0.093 | ⚠ within organs, on part of the lines; also absent: LRP12, DUBR, CYP46A1 |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.218). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (20.1, 11.8); signed map (24.3, 32.7). **Vector** length 92.2, 21.3% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +14.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +23.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +13.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -8.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -6.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | melanocyte inducing transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p13 — chr3:69,739,456-69,968,336 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MI, bHLHe32; previously WS2A, WS2 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 14 pathways, smallest: Regulation of MITF-M dependent genes involved in metabolism; Regulation of MITF-M dependent genes involved in invasion; Regulation of MITF-M-dependent genes involved in DNA replication, damage repair and senescence |
| Matched by | ensembl_id |

**Function**, from UniProt [O75030](https://www.uniprot.org/uniprotkb/O75030) (Microphthalmia-associated transcription factor):

> Transcription factor that acts as a master regulator of melanocyte survival and differentiation as well as melanosome biogenesis. Binds to M-boxes (5'-TCATGTG-3') and symmetrical DNA sequences (E-boxes) (5'-CACGTG-3') found in the promoter of pigmentation genes, such as tyrosinase (TYR). Involved in the cellular response to amino acid availability by acting downstream of MTOR: in the presence of nutrients, MITF phosphorylation by MTOR promotes its inactivation. Upon starvation or lysosomal …

**Summary**, from NCBI Gene [4286](https://www.ncbi.nlm.nih.gov/gene/4286):

> The protein encoded by this gene is a transcription factor that contains both basic helix-loop-helix and leucine zipper structural features. The encoded protein regulates melanocyte development and is responsible for pigment cell-specific transcription of the melanogenesis enzyme genes. Heterozygous mutations in the this gene cause auditory-pigmentary syndromes, such as Waardenburg syndrome type 2 and Tietz syndrome. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:7105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7105) · Entrez [4286](https://www.ncbi.nlm.nih.gov/gene/4286) · UniProt [O75030](https://www.uniprot.org/uniprotkb/O75030) · Ensembl [ENSG00000187098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187098)

## Data

Gene col 11886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11886); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11886]; `tensor/DDL_lfc|DDL_z.npy` [11886]; `embed/gene_vectors.npy` [11886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11886 or target_col == 11886). Every well: [[MITF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MITF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
