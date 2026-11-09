---
symbol: "APMAP"
type: "gene"
col: 2147
ensembl_id: "ENSG00000101474"
name: "adipocyte plasma membrane associated protein"
location: "20p11.21"
module: 23
arm: "-"
pooled_cpm: 37.45
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# APMAP

*adipocyte plasma membrane associated protein* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.94× (z +23.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.664× (z -8.7, q 1e-15, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO1]] (+0.70, fdr 1e-05), [[COLGALT1]] (+0.69, fdr 1e-05), [[BLTP2]] (+0.68, fdr 7e-06); moves opposite to [[ATE1OSP]] (-0.70, fdr 1e-05), [[OXA1L-DT]] (-0.68, fdr 1e-05), [[AK9]] (-0.67, fdr 4e-05).
> It sits in the **-** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.94×** | +23.0 | 0e+00 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.77×** | +21.7 | 0e+00 | 45/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.61×** | +20.5 | 0e+00 | 46/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +12.2 | 4e-32 | 42/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.62×** | +9.8 | 9e-21 | 27/38 (A-172, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.54×** | +9.3 | 2e-18 | 31/45 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +8.4 | 5e-15 | 34/48 (HCT15, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.42×** | +7.5 | 4e-12 | 30/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.46×** | +7.5 | 5e-12 | 28/42 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.43×** | +7.3 | 1e-11 | 26/47 (SW480, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +5.9 | 2e-07 | 23/48 (SNU-423, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +5.4 | 4e-06 | 22/48 (BT-474, PANC-1, …) | two highest doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.3 | 5e-06 | 26/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.6 | 2e-04 | 18/48 (SW1417, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.23×** | +4.3 | 5e-04 | 18/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +4.3 | 6e-04 | 20/48 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.021 | 16/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.053 | 4/48 (CFPAC-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.087 | 5/48 (SW480, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.664×** | -8.7 | 1e-15 | 35/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.764×** | -5.8 | 2e-06 | 24/48 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **0.786×** | -5.1 | 5e-05 | 23/48 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.803×** | -4.3 | 0.002 | 23/47 (HS-578T, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.812×** | -4.3 | 0.002 | 22/48 (AN3 CA, SW 1088, …) | top dose only | position effect removed |
| [[Alpelisib (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.089 | 17/47 (NCI-H1792, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.862× | -3.2 | 0.11 | 20/47 (SNU-1, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 49.7 | 7 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 79.1 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.08× (z +13.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.455× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 36.0 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +10.7) | — |
| [[A-172 (line)]] | wt | 37.9 | 2 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.01× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.50× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.378× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 21.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.4) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.97× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 29.2 | 4 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.03× (z +11.7) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.91× (z +9.3) | — |
| [[SW480 (line)]] | alt | 45.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +18.1) | — |
| [[A549 (line)]] | wt | 35.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 34.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +12.5) | — |
| [[COLO 205 (line)]] | alt | 27.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.88× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 52.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.38× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.8) ⚠ cell-cycle shift, explains ~15% of this change |
| [[HT-29 (line)]] | alt | 30.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.7) | — |
| [[KATO III (line)]] | alt | 48.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +13.0) | — |
| [[LoVo (line)]] | wt | 27.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 25.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 29.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.31× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.47× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.31× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 30.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +12.3) | — |
| [[RKO (line)]] | wt | 60.8 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.43× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -21.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 24.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 29.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 34.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 53.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +10.6) | — |
| [[J82 (line)]] | alt | 33.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[AN3 CA (line)]] | alt | 41.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.120× (z -8.9) |
| [[BT-474 (line)]] | alt | 35.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.34× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 28.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 90.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO1]] | +0.70 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.69 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CS]] | +0.66 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[GUSB]] | +0.66 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[GGCX]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.64 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ADAM15]] | +0.64 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[PLBD2]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ANXA6]] | +0.62 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PARP1]] | +0.62 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ABCA2]] | +0.61 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1OSP]] | -0.70 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | -0.68 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[AK9]] | -0.67 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[THAP2]] | -0.65 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[KRCC1]] | -0.65 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[N4BP2L1]] | -0.65 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[NSMCE1-DT]] | -0.65 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[ASH1L]] | -0.64 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[C3orf38]] | -0.64 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CCDC122]] | -0.64 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | -0.63 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[GUCY2C-AS1]] | -0.63 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-9.5, -21.2); signed map (-27.2, -42.0). **Vector** length 93.4, 21.5% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.1 | +20.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +21.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +23.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +8.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.1 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.4 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -6.2 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +2.7 |

## What is on record

|  |  |
|---|---|
| Name | adipocyte plasma membrane associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:24,962,925-24,992,751 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BSCv; previously C20orf3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HDC9](https://www.uniprot.org/uniprotkb/Q9HDC9) (Adipocyte plasma membrane-associated protein):

> Exhibits strong arylesterase activity with beta-naphthyl acetate and phenyl acetate. May play a role in adipocyte differentiation.

**Summary**, from NCBI Gene [57136](https://www.ncbi.nlm.nih.gov/gene/57136):

> Enables arylesterase activity. Located in cell surface and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13238) · Entrez [57136](https://www.ncbi.nlm.nih.gov/gene/57136) · UniProt [Q9HDC9](https://www.uniprot.org/uniprotkb/Q9HDC9) · Ensembl [ENSG00000101474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101474)

## Data

Gene col 2147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2147); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2147]; `tensor/DDL_lfc|DDL_z.npy` [2147]; `embed/gene_vectors.npy` [2147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2147 or target_col == 2147). Every well: [[APMAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APMAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
