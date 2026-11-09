---
symbol: "THAP1"
type: "gene"
col: 5257
ensembl_id: "ENSG00000131931"
name: "THAP domain containing 1"
location: "8p11.21"
module: 11
arm: "+"
pooled_cpm: 14.77
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# THAP1

*THAP domain containing 1* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.11× (z +20.8, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.34× (z +15.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.689× (z -4.8, q 5e-04, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REST]] (+0.79, fdr 7e-06), [[TOPORS]] (+0.73, fdr 7e-06), [[FAM200A]] (+0.73, fdr 7e-06); moves opposite to [[MFSD14B]] (-0.69, fdr 7e-06), [[TCF3]] (-0.63, fdr 1e-05), [[PARP1]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.11×** | +20.8 | 0e+00 | 46/47 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.34×** | +15.7 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.32×** | +15.6 | 0e+00 | 43/46 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +13.5 | 4e-39 | 45/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.49×** | +11.8 | 3e-30 | 44/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.20×** | +10.2 | 2e-22 | 42/46 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.08×** | +9.5 | 1e-19 | 38/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.13×** | +9.4 | 3e-19 | 40/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.02×** | +9.1 | 4e-18 | 41/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.58×** | +8.7 | 3e-16 | 36/48 (SW480, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +7.6 | 2e-12 | 33/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.43×** | +4.6 | 2e-04 | 21/43 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 23/47 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.7 | 0.007 | 20/43 (C-33 A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.34×** | +3.6 | 0.010 | 19/43 (LoVo, NCI-H460, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.087 | 16/47 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.689×** | -4.8 | 5e-04 | 23/48 (HOP62, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Folic acid (drug)]] 5 µM |  | **0.770×** | -4.8 | 5e-04 | 23/48 (LOX-IMVI, NCI-H460, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.697×** | -4.7 | 6e-04 | 22/47 (SNU-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.767×** | -3.4 | 0.081 | 15/46 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.4 | 0.081 | 2/48 (NCI-H661, SW 1271) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.841× | -3.2 | 0.13 | 8/48 (SW 900, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | 0.628× | -3.1 | 0.13 | 9/48 (HCT15, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.1 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.27× (z +14.6) | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +16.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.87× (z +12.0) | — |
| [[A549 (line)]] | wt | 17.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +17.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.82× (z +13.4) | — |
| [[PANC-1 (line)]] | alt | 10.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +15.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.53× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 16.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.52× (z +10.2) | — |
| [[LoVo (line)]] | wt | 9.71 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +11.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.75× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 13.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.80× (z +9.8) | — |
| [[A498 (line)]] | wt | 14.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 14.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 22.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.63× (z +9.3) | — |
| [[KATO III (line)]] | alt | 15.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.75× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 16.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 9.49 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.95× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.74× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +16.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.70× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +11.1) | — |
| [[RKO (line)]] | wt | 21.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.80× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 19.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 11.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +9.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0693× (z -8.7) |
| [[Hs 766T (line)]] | wt | 16.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +11.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.156× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +9.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REST]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[TOPORS]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.73 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[ZNF24]] | +0.73 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.72 | +0.73 / +0.46 | both halves | 2e-05 |  |
| [[THAP6]] | +0.72 | +0.73 / +0.57 | both halves | 1e-05 | same gene group |
| [[TRIP11]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[RSF1]] | +0.72 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[CLK4]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.71 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[EPC1]] | +0.70 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[MFAP1]] | +0.69 | +0.73 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14B]] | -0.69 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[TCF3]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[PARP1]] | -0.62 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[HERC2]] | -0.62 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[FAR1]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[NUP93]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[LRP8]] | -0.61 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[FAM20B]] | -0.60 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[OLA1]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.60 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[CHID1]] | -0.60 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[MACROH2A1]] | -0.60 | -0.50 / -0.70 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises THAP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.5, 6.1); signed map (5.0, -18.5). **Vector** length 83.5, 18.8% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +15.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +6.6 | +20.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +9.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.3 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | +1.9 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,836,674-42,843,325 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10477, 4833431A01Rik; previously DYT6 |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVV9](https://www.uniprot.org/uniprotkb/Q9NVV9) (THAP domain-containing protein 1):

> DNA-binding transcription regulator that regulates endothelial cell proliferation and G1/S cell-cycle progression. Specifically binds the 5'-[AT]NTNN[GT]GGCA[AGT]-3' core DNA sequence and acts by modulating expression of pRB-E2F cell-cycle target genes, including RRM1. Component of a THAP1/THAP3-HCFC1-OGT complex that is required for the regulation of the transcriptional activity of RRM1. May also have pro-apoptotic activity by potentiating both serum-withdrawal and TNF-induced apoptosis.

**Summary**, from NCBI Gene [55145](https://www.ncbi.nlm.nih.gov/gene/55145):

> The protein encoded by this gene contains a THAP domain, a conserved DNA-binding domain. This protein colocalizes with the apoptosis response protein PAWR/PAR-4 in promyelocytic leukemia (PML) nuclear bodies, and functions as a proapoptotic factor that links PAWR to PML nuclear bodies. Alternatively spliced transcript variants encoding distinct isoforms have been observed. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20856) · Entrez [55145](https://www.ncbi.nlm.nih.gov/gene/55145) · UniProt [Q9NVV9](https://www.uniprot.org/uniprotkb/Q9NVV9) · Ensembl [ENSG00000131931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131931)

## Data

Gene col 5257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5257); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5257]; `tensor/DDL_lfc|DDL_z.npy` [5257]; `embed/gene_vectors.npy` [5257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5257 or target_col == 5257). Every well: [[THAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
