---
symbol: "ZRANB2"
type: "gene"
col: 5330
ensembl_id: "ENSG00000132485"
name: "zinc finger RANBP2-type containing 2"
location: "1p31.1"
module: 64
arm: "+"
pooled_cpm: 155.76
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# ZRANB2

*zinc finger RANBP2-type containing 2* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.10× (z +17.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.723× (z -7.6, q 2e-11, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC2]] (+0.65, fdr 1e-05), [[AIMP1]] (+0.61, fdr 1e-05), [[SMC5-DT]] (+0.61, fdr 2e-05); moves opposite to [[LSM4]] (-0.61, fdr 1e-05), [[POC1A]] (-0.55, fdr 1e-05), [[TICRR]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5330.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +17.3 | 0e+00 | 48/48 (SW480, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +12.7 | 2e-34 | 42/49 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +11.7 | 1e-29 | 41/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +10.7 | 1e-24 | 29/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +10.3 | 7e-23 | 38/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.7 | 4e-16 | 31/44 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +7.6 | 3e-12 | 41/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +7.3 | 2e-11 | 40/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +6.5 | 4e-09 | 29/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.8 | 4e-07 | 32/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.4 | 3e-06 | 29/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +5.4 | 4e-06 | 29/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 2e-04 | 28/47 (NCI-H460, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 18/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.009 | 27/49 (PANC-1, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.011 | 25/48 (SW1417, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.047 | 19/48 (HS-578T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.059 | 17/48 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.059 | 16/48 (SHP-77, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | 1.14× | +3.0 | 0.067 | 11/48 (COLO 205, NCI-H460, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.09× | +2.9 | 0.083 | 0/49 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5330.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.723×** | -7.6 | 2e-11 | 40/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.767×** | -6.2 | 2e-07 | 31/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.821×** | -4.6 | 8e-04 | 24/48 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.872× | -4.5 | 9e-04 | 19/49 (A498, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.7 | 0.026 | 18/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.756×** | -3.4 | 0.061 | 18/49 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.872× | -3.2 | 0.11 | 13/48 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.878× | -3.0 | 0.17 | 13/47 (H4, SW 900, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5330. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 129 | 12 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +15.6) | — |
| [[NCI-H1573 (line)]] | alt | 176 | 5 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.516× (z -10.2) |
| [[A498 (line)]] | wt | 197 | 3 (1 ⚠) | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.84× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -10.3) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.576× (z -9.6) |
| [[HT-29 (line)]] | alt | 151 | 5 (3 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.01× (z +15.8) | [[Lonafarnib (drug)]] 5 µM 0.275× (z -9.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 150 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.14× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 134 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.35× (z +12.1) | — |
| [[SW480 (line)]] | alt | 176 | 4 (3 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.40× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.631× (z -8.5) |
| [[A-172 (line)]] | wt | 111 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.8) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +14.5) | — |
| [[HOP62 (line)]] | alt | 91.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.9) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 365 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 150 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.13× (z +10.0) | — |
| [[C32 (line)]] | wt | 94.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 185 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.61× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 152 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.24× (z +9.9) | — |
| [[LoVo (line)]] | wt | 171 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.39× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 154 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.26× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.87× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 175 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.8) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 169 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.05× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.520× (z -9.5) |
| [[SHP-77 (line)]] | alt | 120 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 161 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.58× (z +11.1) | — |
| [[A-427 (line)]] | wt | 122 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.08× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 150 | 1 | 1 | [[Auranofin (drug)]] 5 µM 1.88× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.550× (z -8.5) |
| [[HCT15 (line)]] | alt | 182 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.8) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +9.3) | — |
| [[J82 (line)]] | alt | 194 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.9) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.08× (z +10.6) | — |
| [[KATO III (line)]] | alt | 155 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.30× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 99.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.8) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[RKO (line)]] | wt | 161 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.36× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 176 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 131 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.43× (z +10.8) | — |
| [[A549 (line)]] | wt | 83.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +10.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 142 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.42× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 120 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.15× (z +14.1) | — |
| [[C-33 A (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.60× (z +9.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 89.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.00× (z +9.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 232 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.07× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 143 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.00× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 127 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.59× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 178 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +9.9) | — |
| [[SW48 (line)]] | wt | 147 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.97× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 227 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5330), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | +0.65 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[AIMP1]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SMC5-DT]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SSBP1]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ARMCX3]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[USP16]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.57 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[NSRP1]] | +0.57 | +0.66 / +0.44 | both halves | 3e-05 | same gene group |
| [[OCIAD1]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[PPID]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[KCNMB3]] | +0.56 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[DNAJC7]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM4]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[POC1A]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TICRR]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[BARD1]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[NCAPD3]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[CBX2]] | -0.52 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[PDE7A]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SIN3A]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[BSG]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[LIX1L]] | -0.51 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[SLC25A39]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[KIF22]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ZRANB2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-35.3, -37.0); signed map (9.2, -23.7). **Vector** length 116, 35.8% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.3 | +17.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +7.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.7 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +4.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.8 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger RANBP2-type containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:71,063,291-71,081,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZIS, ZIS1, ZIS2; previously ZNF265 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O95218](https://www.uniprot.org/uniprotkb/O95218) (Zinc finger Ran-binding domain-containing protein 2):

> Splice factor required for alternative splicing of TRA2B/SFRS10 transcripts. Binds to ssRNA containing the consensus sequence 5'-AGGUAA-3'. May interfere with constitutive 5'-splice site selection.

**Summary**, from NCBI Gene [9406](https://www.ncbi.nlm.nih.gov/gene/9406):

> Enables RNA binding activity. Predicted to be involved in RNA splicing and mRNA processing. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13058) · Entrez [9406](https://www.ncbi.nlm.nih.gov/gene/9406) · UniProt [O95218](https://www.uniprot.org/uniprotkb/O95218) · Ensembl [ENSG00000132485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132485)

## Data

Gene col 5330: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5330); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5330, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5330]; `tensor/DDL_lfc|DDL_z.npy` [5330]; `embed/gene_vectors.npy` [5330]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5330 or target_col == 5330). Every well: [[ZRANB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZRANB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
