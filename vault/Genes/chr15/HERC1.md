---
symbol: "HERC1"
type: "gene"
col: 2390
ensembl_id: "ENSG00000103657"
name: "HECT and RLD domain containing E3 ubiquitin protein ligase family member 1"
location: "15q22.31"
module: 83
arm: "-"
pooled_cpm: 160.06
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# HERC1

*HECT and RLD domain containing E3 ubiquitin protein ligase family member 1* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.41× (z +16.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.502× (z -13.2, q 5e-37, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF3A]] (+0.68, fdr 7e-06), [[ARL3]] (+0.60, fdr 3e-05), [[DHTKD1]] (+0.58, fdr 2e-04); moves opposite to [[GLIPR1-AS1]] (-0.59, fdr 5e-05), [[MIRLET7A1HG]] (-0.59, fdr 2e-05), [[FBXL19-AS1]] (-0.57, fdr 4e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2390.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.41×** | +16.9 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +15.8 | 0e+00 | 48/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +15.3 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +8.4 | 6e-15 | 45/48 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.25×** | +8.1 | 5e-14 | 47/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +5.5 | 3e-06 | 24/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 3e-05 | 35/48 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +4.8 | 1e-04 | 36/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 23/48 (CFPAC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.7 | 0.012 | 15/48 (NCI-H2347, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.026 | 27/48 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +3.0 | 0.11 | 20/50 (C32, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2390.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.502×** | -13.2 | 5e-37 | 47/48 (HT-29, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -12.5 | 2e-33 | 39/44 (NCI-H1573, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.545×** | -11.6 | 6e-29 | 44/49 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -9.2 | 8e-18 | 39/45 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -6.7 | 2e-09 | 37/47 (SW1417, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.705×** | -6.7 | 2e-09 | 37/48 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.741×** | -5.7 | 7e-07 | 33/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.609×** | -5.0 | 5e-05 | 34/48 (A549, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.617×** | -4.8 | 9e-05 | 33/48 (HOP62, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -4.4 | 7e-04 | 0/50 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.876× | -3.6 | 0.017 | 6/48 (A-172, J82, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.718×** | -3.3 | 0.043 | 29/48 (Panc 03.27, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.888× | -3.2 | 0.054 | 17/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.846× | -3.2 | 0.054 | 21/48 (HS-578T, A-172, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.893× | -3.0 | 0.087 | 6/48 (NCI-H2347, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2390. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 120 | 6 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.64× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 137 | 3 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.510× (z -10.7) |
| [[HT-29 (line)]] | alt | 203 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +13.5) | [[Auranofin (drug)]] 5 µM 0.309× (z -14.9) |
| [[PANC-1 (line)]] | alt | 129 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.531× (z -9.9) |
| [[LoVo (line)]] | wt | 293 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.379× (z -13.8) |
| [[SW480 (line)]] | alt | 151 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +15.0) | [[Auranofin (drug)]] 5 µM 0.381× (z -14.3) |
| [[A549 (line)]] | wt | 227 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 90.5 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +14.5) | [[Auranofin (drug)]] 5 µM 0.339× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 94.1 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.57× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.503× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 225 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.13× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 118 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.302× (z -13.9) |
| [[SW1417 (line)]] | alt | 225 | 1 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -10.4) |
| [[SW48 (line)]] | wt | 161 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -10.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 95.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -13.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 139 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +10.2) | [[Auranofin (drug)]] 5 µM 0.349× (z -13.8) |
| [[J82 (line)]] | alt | 160 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -14.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 154 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -8.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 97.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.11× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.442× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 113 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +14.1) | — |
| [[H4 (line)]] | wt | 128 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -9.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 136 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.78× (z +11.3) | [[Auranofin (drug)]] 5 µM 0.443× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 151 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.35× (z +11.4) | [[Auranofin (drug)]] 5 µM 0.500× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 116 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.99× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -18.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 237 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -12.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 169 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 103 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.71× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.440× (z -10.1) |
| [[A498 (line)]] | wt | 227 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -14.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 168 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 131 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 127 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 211 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.467× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 189 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 214 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +9.2) | [[Auranofin (drug)]] 5 µM 0.421× (z -12.2) |
| [[SW 900 (line)]] | alt | 181 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.00× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.480× (z -9.1) |
| [[A-172 (line)]] | wt | 167 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 1.97× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.450× (z -10.6) |
| [[AN3 CA (line)]] | alt | 200 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -16.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 187 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 164 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 130 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 141 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.01× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.488× (z -9.6) |
| [[C-33 A (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 158 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.340× (z -13.0) |
| [[CHP-212 (line)]] | wt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -10.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 255 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2390), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF3A]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ARL3]] | +0.60 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[DHTKD1]] | +0.58 | +0.31 / +0.43 | both halves | 2e-04 |  |
| [[SUCLG1]] | +0.56 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[SPAST]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PIN1]] | +0.56 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[RWDD1]] | +0.55 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[ZYG11B]] | +0.55 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[GBF1]] | +0.54 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[RTRAF]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[MBTPS1]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[STX18]] | +0.54 | +0.50 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIPR1-AS1]] | -0.59 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[MIRLET7A1HG]] | -0.59 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[FBXL19-AS1]] | -0.57 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[UBE2D3-AS1]] | -0.57 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[SPTY2D1OS]] | -0.56 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[MPDU1]] | -0.56 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[DUS3L]] | -0.55 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[PARD6G-AS1]] | -0.55 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[ZNF789]] | -0.54 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[TIRAP-AS1]] | -0.53 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[LINC01618]] | -0.53 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[MIR30DHG]] | -0.53 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HERC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.7, 8.7); signed map (-33.6, 15.8). **Vector** length 101, 35.2% of its response variance represented; |z| ≥ 3 in 1,238 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.7 | +15.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +8.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +15.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +16.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -13.6 | -13.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | HECT and RLD domain containing E3 ubiquitin protein ligase family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:63,608,618-63,833,948 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p532, p619 |
| Gene groups (HGNC) | WD repeat domain containing; HECT and RLD domain containing E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15751](https://www.uniprot.org/uniprotkb/Q15751) (Probable E3 ubiquitin-protein ligase HERC1):

> Involved in membrane trafficking via some guanine nucleotide exchange factor (GEF) activity and its ability to bind clathrin. Acts as a GEF for Arf and Rab, by exchanging bound GDP for free GTP. Binds phosphatidylinositol 4,5-bisphosphate, which is required for GEF activity. May also act as a E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates.

**Summary**, from NCBI Gene [8925](https://www.ncbi.nlm.nih.gov/gene/8925):

> This gen encodes a member of the HERC protein family. This protein stimulates guanine nucleotide exchange on ARF1 and Rab proteins. This protein may be involved in membrane transport processes. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:4867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4867) · Entrez [8925](https://www.ncbi.nlm.nih.gov/gene/8925) · UniProt [Q15751](https://www.uniprot.org/uniprotkb/Q15751) · Ensembl [ENSG00000103657](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103657)

## Data

Gene col 2390: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2390); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2390, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2390]; `tensor/DDL_lfc|DDL_z.npy` [2390]; `embed/gene_vectors.npy` [2390]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2390 or target_col == 2390). Every well: [[HERC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
