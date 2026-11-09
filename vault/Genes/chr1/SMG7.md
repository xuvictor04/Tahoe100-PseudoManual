---
symbol: "SMG7"
type: "gene"
col: 3824
ensembl_id: "ENSG00000116698"
name: "SMG7 nonsense mediated mRNA decay factor"
location: "1q25.3"
module: 25
arm: "+"
pooled_cpm: 174.14
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SMG7

*SMG7 nonsense mediated mRNA decay factor* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +16.7, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.775× (z -4.9, q 6e-04, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX9]] (+0.70, fdr 7e-06), [[RBBP9]] (+0.69, fdr 7e-06), [[RAD23B]] (+0.68, fdr 7e-06); moves opposite to [[NOSIP]] (-0.66, fdr 1e-05), [[RABGEF1]] (-0.64, fdr 1e-05), [[GAN]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLHL29]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +16.7 | 0e+00 | 42/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.91×** | +13.7 | 4e-40 | 48/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +12.4 | 4e-33 | 45/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.02×** | +11.1 | 2e-26 | 46/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +10.4 | 2e-23 | 41/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.7 | 4e-20 | 40/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +9.4 | 3e-19 | 43/47 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +6.8 | 1e-09 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.2 | 4e-08 | 37/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 1e-07 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +5.6 | 1e-06 | 35/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +5.4 | 3e-06 | 28/45 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 2e-05 | 34/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +5.0 | 3e-05 | 30/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 4e-05 | 26/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +4.4 | 4e-04 | 24/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.040 | 19/49 (HS-578T, J82, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.047 | 20/49 (HT-29, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.075 | 21/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.775×** | -4.9 | 6e-04 | 28/48 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.792×** | -4.5 | 0.002 | 26/48 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.798×** | -4.2 | 0.006 | 24/50 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.868× | -3.9 | 0.016 | 22/49 (A549, SW1417, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.024 | 23/48 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | **0.830×** | -3.5 | 0.052 | 21/44 (SK-MEL-2, C-33 A, …) | top dose only | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.781×** | -3.4 | 0.056 | 25/48 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 206 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +21.2) | — |
| [[PANC-1 (line)]] | alt | 150 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +36.7) | — |
| [[SW 900 (line)]] | alt | 218 | 8 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.06× (z +12.0) | — |
| [[SW480 (line)]] | alt | 164 | 6 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 5.41× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.581× (z -9.3) |
| [[A549 (line)]] | wt | 151 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +26.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -11.2) ⚠ cell-cycle shift, explains ~1% of this change |
| [[LS 180 (line)]] | wt | 199 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +16.7) | — |
| [[NCI-H1792 (line)]] | alt | 150 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.45× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.21× (z +12.3) | — |
| [[A-427 (line)]] | wt | 179 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.84× (z +13.7) | — |
| [[SW48 (line)]] | wt | 157 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 111 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 187 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +18.3) | — |
| [[HOP62 (line)]] | alt | 145 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.17× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 132 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.64× (z +13.6) | — |
| [[LoVo (line)]] | wt | 165 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.64× (z +13.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 4.93× (z +12.2) | — |
| [[A-172 (line)]] | wt | 177 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 208 | 3 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.35× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -8.8) |
| [[H4 (line)]] | wt | 146 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.60× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.52× (z +9.7) | — |
| [[J82 (line)]] | alt | 166 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.98× (z +13.4) | — |
| [[NCI-H1573 (line)]] | alt | 205 | 4 (2 ⚠) | 0 | [[Lonafarnib (drug)]] 5 µM 6.64× (z +12.8) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 5.25× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 165 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 161 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[C32 (line)]] | wt | 144 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 9.57× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 238 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.66× (z +9.9) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.451× (z -8.5) |
| [[HT-29 (line)]] | alt | 143 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.24× (z +13.0) | — |
| [[KATO III (line)]] | alt | 128 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.34× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 157 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.41× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 129 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.58× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.6) | — |
| [[RKO (line)]] | wt | 136 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.0) | — |
| [[A498 (line)]] | wt | 243 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +16.8) | — |
| [[COLO 205 (line)]] | alt | 163 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.00× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 142 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.53× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 275 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SHP-77 (line)]] | alt | 190 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 170 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.60× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.5) | — |
| [[SW1417 (line)]] | alt | 232 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.488× (z -9.4) |
| [[C-33 A (line)]] | alt | 173 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change |
| [[CFPAC-1 (line)]] | alt | 203 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 262 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 135 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.13× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 149 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.48× (z +13.0) | — |
| [[AN3 CA (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX9]] | +0.70 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[RBBP9]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[RAD23B]] | +0.68 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[FECH]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[FAM98B]] | +0.63 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.62 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[DLD]] | +0.62 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[FUBP1]] | +0.61 | +0.39 / +0.72 | both halves | 5e-05 |  |
| [[MTMR2]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[RAVER2]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[FBXO7]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOSIP]] | -0.66 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[RABGEF1]] | -0.64 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[GAN]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | -0.61 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[PPFIA1]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[VRK3]] | -0.59 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[PPP1R13L]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[HIC2]] | -0.59 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[SLC35E1]] | -0.59 | -0.38 / -0.65 | both halves | 6e-05 |  |
| [[MYO9B]] | -0.58 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[POLR2J4]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[HM13]] | -0.57 | -0.38 / -0.68 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL29]] | B | KLHL29 activity lowers SMG7's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.17× higher at baseline in the lines without KLHL29 | 0.067 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.8, -16.3); signed map (-16.5, -41.8). **Vector** length 101, 35.3% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | +6.5 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | +6.3 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +0.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.3 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -2.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | +6.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | SMG7 nonsense mediated mRNA decay factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:183,472,216-183,598,246 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0250, EST1C, SGA56M, SMG-7; previously C1orf16 |
| Reactome | 3 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92540](https://www.uniprot.org/uniprotkb/Q92540) (Nonsense-mediated mRNA decay factor SMG7):

> Plays a role in nonsense-mediated mRNA decay. Recruits UPF1 to cytoplasmic mRNA decay bodies. Together with SMG5 is thought to provide a link to the mRNA degradation machinery involving exonucleolytic pathways, and to serve as an adapter for UPF1 to protein phosphatase 2A (PP2A), thereby triggering UPF1 dephosphorylation.

**Summary**, from NCBI Gene [9887](https://www.ncbi.nlm.nih.gov/gene/9887):

> This gene encodes a protein that is essential for nonsense-mediated mRNA decay (NMD); a process whereby transcripts with premature termination codons are targeted for rapid degradation by a mRNA decay complex. The mRNA decay complex consists, in part, of this protein along with proteins SMG5 and UPF1. The N-terminal domain of this protein is thought to mediate its association with SMG5 or UPF1 while the C-terminal domain interacts with the mRNA decay complex. This protein may therefore couple …

**Accessions** — [HGNC:16792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16792) · Entrez [9887](https://www.ncbi.nlm.nih.gov/gene/9887) · UniProt [Q92540](https://www.uniprot.org/uniprotkb/Q92540) · Ensembl [ENSG00000116698](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116698)

## Data

Gene col 3824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3824); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3824]; `tensor/DDL_lfc|DDL_z.npy` [3824]; `embed/gene_vectors.npy` [3824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3824 or target_col == 3824). Every well: [[SMG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
