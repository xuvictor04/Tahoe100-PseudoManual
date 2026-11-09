---
symbol: "ADAR"
type: "gene"
col: 8371
ensembl_id: "ENSG00000160710"
name: "adenosine deaminase RNA specific"
location: "1q21.3"
module: 32
arm: "+"
pooled_cpm: 264.39
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 59
direction_downstream: 28
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ADAR

*adenosine deaminase RNA specific* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.46× (z +9.1, q 7e-17, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.612× (z -16.4, q 0e+00, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTX3L]] (+0.88, fdr 7e-06), [[PARP9]] (+0.88, fdr 7e-06), [[OAS3]] (+0.87, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 59 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); 28 go from it, the strongest it → [[IRF9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +9.1 | 7e-17 | 37/48 (PANC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +5.1 | 1e-04 | 25/49 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +4.8 | 4e-04 | 16/48 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.7 | 4e-04 | 28/47 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +4.6 | 4e-04 | 27/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 5e-04 | 25/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +4.5 | 7e-04 | 18/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.20× | +4.4 | 8e-04 | 20/47 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | 1.20× | +4.3 | 1e-03 | 22/48 (HOP62, SW480, …) | all doses, flat | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.001 | 27/49 (RPMI-7951, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.18× | +4.0 | 0.003 | 22/48 (PANC-1, NCI-H2347, …) | top dose only | composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.0 | 0.003 | 16/50 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.004 | 16/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.9 | 0.004 | 10/48 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.006 | 24/48 (LS 180, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.012 | 18/48 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.014 | 20/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.016 | 20/49 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.11× | +3.4 | 0.016 | 4/48 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.612×** | -16.4 | 0e+00 | 34/49 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.514×** | -16.0 | 0e+00 | 46/48 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.520×** | -15.7 | 0e+00 | 47/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.540×** | -14.8 | 0e+00 | 44/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.670×** | -13.3 | 3e-38 | 32/49 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.608×** | -12.0 | 5e-31 | 37/48 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.621×** | -11.4 | 2e-28 | 36/49 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -10.0 | 1e-21 | 30/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.691×** | -8.9 | 4e-17 | 35/48 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -8.7 | 2e-16 | 26/49 (CHP-212, BT-474, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.700×** | -8.6 | 6e-16 | 31/49 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.737×** | -7.3 | 1e-11 | 30/48 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.820×** | -6.6 | 1e-09 | 24/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -6.3 | 1e-08 | 25/48 (A549, SW 900, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.613×** | -6.2 | 3e-08 | 30/48 (NCI-H2347, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.850× | -5.4 | 2e-06 | 17/49 (NCI-H1573, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 420 | 5 (4 ⚠) | 14 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.73× (z +16.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.15× (z +13.4) | [[Tofacitinib (drug)]] 5 µM 0.468× (z -18.5) |
| [[A-172 (line)]] | wt | 414 | 2 (1 ⚠) | 10 | [[Homoharringtonine (drug)]] 0.5 µM 1.78× (z +8.9) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.76× (z +8.7) | [[Tofacitinib (drug)]] 5 µM 0.475× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 282 | 1 | 10 | [[TAK-901 (drug)]] 5 µM 3.76× (z +9.4) | [[Tofacitinib (drug)]] 5 µM 0.459× (z -14.7) |
| [[A549 (line)]] | wt | 317 | 0 | 10 | — | [[Tofacitinib (drug)]] 5 µM 0.472× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 332 | 1 (1 ⚠) | 9 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.13× (z +11.3) ⚠ cell-cycle shift, explains ~25% of this change | [[Tofacitinib (drug)]] 5 µM 0.374× (z -21.1) |
| [[NCI-H23 (line)]] | alt | 619 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -17.3) |
| [[RKO (line)]] | wt | 299 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -20.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.389× (z -11.5) |
| [[LoVo (line)]] | wt | 344 | 0 | 9 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -18.2) |
| [[NCI-H1573 (line)]] | alt | 363 | 0 | 9 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.468× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 300 | 2 (2 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Tofacitinib (drug)]] 5 µM 0.548× (z -11.7) |
| [[A498 (line)]] | wt | 404 | 0 | 8 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.555× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 274 | 0 | 8 | — | [[Tofacitinib (drug)]] 5 µM 0.437× (z -15.7) |
| [[C-33 A (line)]] | alt | 413 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.330× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 410 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -12.8) |
| [[COLO 205 (line)]] | alt | 434 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.373× (z -16.2) |
| [[KATO III (line)]] | alt | 220 | 1 | 6 | [[Harringtonine (drug)]] 0.5 µM 2.00× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.390× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 247 | 0 | 7 | — | [[Tofacitinib (drug)]] 5 µM 0.452× (z -15.0) |
| [[SNU-423 (line)]] | alt | 230 | 0 | 7 | — | [[Tofacitinib (drug)]] 5 µM 0.480× (z -13.6) |
| [[HS-578T (line)]] | alt | 188 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.13× (z +15.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.15× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.469× (z -9.9) |
| [[SHP-77 (line)]] | alt | 331 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.560× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 286 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.531× (z -12.0) |
| [[BT-474 (line)]] | alt | 332 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -12.3) |
| [[SW 900 (line)]] | alt | 328 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.530× (z -9.4) |
| [[SW1417 (line)]] | alt | 256 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.404× (z -15.9) |
| [[A-427 (line)]] | wt | 218 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.508× (z -11.3) |
| [[C32 (line)]] | wt | 172 | 1 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.03× (z +9.7) | [[Auranofin (drug)]] 5 µM 0.528× (z -8.7) |
| [[J82 (line)]] | alt | 186 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | — |
| [[SW480 (line)]] | alt | 124 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | [[Homoharringtonine (drug)]] 5 µM 0.665× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 373 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 185 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.79× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 193 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.532× (z -9.9) |
| [[HOP62 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 292 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.501× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 118 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.52× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | — |
| [[PANC-1 (line)]] | alt | 205 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.33× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.472× (z -10.0) |
| [[AN3 CA (line)]] | alt | 237 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 207 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 268 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX3L]] | +0.88 | +0.80 / +0.91 | both halves | 7e-06 | STRING 427 |
| [[PARP9]] | +0.88 | +0.81 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 539 |
| [[OAS3]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 689 |
| [[IFIT1]] | +0.87 | +0.80 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 699 |
| [[OAS2]] | +0.86 | +0.80 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 660 |
| [[IFI35]] | +0.85 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 482 |
| [[PARP14]] | +0.85 | +0.79 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 439 |
| [[IFIT5]] | +0.84 | +0.79 / +0.86 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 505 |
| [[TRANK1]] | +0.84 | +0.79 / +0.83 | both halves | 7e-06 | STRING 465 |
| [[MX1]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 723 |
| [[SLC15A3]] | +0.84 | +0.72 / +0.86 | both halves | 7e-06 |  |
| [[EIF2AK2]] | +0.84 | +0.75 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 873 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 30, C 29. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises ADAR's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without OAS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises ADAR's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.57× lower at baseline in the lines without OAS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS2]] | B | OAS2 activity strengthens ADAR's drug response | lines that do not express OAS2 (14) vs lines expressing it (35) | the lines without OAS2 respond 0.44× as strongly (z diff +2.77); strongest at Auranofin 5 µM: 0.96x vs 0.62x (z diff +6.4) | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[CMPK2]] | B | CMPK2 activity raises ADAR's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without CMPK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[BATF2]] | B | BATF2 activity raises ADAR's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.54× lower at baseline in the lines without BATF2 | 0.007 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity strengthens ADAR's drug response | lines that do not express BATF2 (13) vs lines expressing it (36) | the lines without BATF2 respond 0.54× as strongly (z diff +2.62); strongest at Auranofin 5 µM: 0.92x vs 0.64x (z diff +5.4) | 0.008 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFI6]] | B | IFI6 activity raises ADAR's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without IFI6 | 0.009 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity strengthens ADAR's drug response | lines that do not express PARP9 (7) vs lines expressing it (42) | the lines without PARP9 respond 0.33× as strongly (z diff +3.46); strongest at Auranofin 5 µM: 1.06x vs 0.66x (z diff +6.7) | 0.010 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OAS1]] | B | OAS1 activity strengthens ADAR's drug response | lines that do not express OAS1 (13) vs lines expressing it (36) | the lines without OAS1 respond 0.43× as strongly (z diff +2.87); strongest at Auranofin 5 µM: 0.95x vs 0.63x (z diff +5.9) | 0.012 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFI6]] | B | IFI6 activity strengthens ADAR's drug response | lines that do not express IFI6 (13) vs lines expressing it (36) | the lines without IFI6 respond 0.38× as strongly (z diff +3.27); strongest at Auranofin 5 µM: 1.00x vs 0.62x (z diff +7.1) | 0.013 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[OAS3]] | B | OAS3 activity raises ADAR's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without OAS3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[IFI27]] | B | IFI27 activity raises ADAR's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without IFI27 | 0.017 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 0, C 28. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF9]] | C | ADAR's natural level strengthens IRF9's drug response | ADAR's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.79; direction not clear | 3e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | ADAR's natural level strengthens IFIT5's drug response | ADAR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.77; direction not clear | 1e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | ADAR's natural level strengthens TRIM25's drug response | ADAR's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.71; direction not clear | 8e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | ADAR's natural level strengthens PML's drug response | ADAR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.70; direction not clear | 1e-03 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | ADAR's natural level strengthens PARP12's drug response | ADAR's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.69; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP14]] | C | ADAR's natural level strengthens PARP14's drug response | ADAR's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.67; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | ADAR's natural level strengthens CMTR1's drug response | ADAR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.66; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[REC8]] | C | ADAR's natural level strengthens REC8's drug response | ADAR's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.75; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | ADAR's natural level strengthens HELZ2's drug response | ADAR's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.84; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[STAT1]] | C | ADAR's natural level strengthens STAT1's drug response | ADAR's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.89; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NMI]] | C | ADAR's natural level strengthens NMI's drug response | ADAR's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.52; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | ADAR's natural level strengthens PARP10's drug response | ADAR's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.73; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.874). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 54.3); signed map (64.2, 32.4). **Vector** length 162, 60.8% of its response variance represented; |z| ≥ 3 in 1,611 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.78 to 23); *Interferon gamma signaling* (reactome, mean cos +0.72 to 17); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.73 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.0 | +9.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +8.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +8.0 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +7.3 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.0 | +4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +6.7 | +4.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +6.4 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +6.4 | +3.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -11.3 | -16.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.3 | -13.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -9.9 | -12.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.7 | -11.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.1 | -8.6 |

## What is on record

|  |  |
|---|---|
| Name | adenosine deaminase RNA specific |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,581,695-154,628,013 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADAR1, DRADA; previously IFI4, G1P1 |
| Gene groups (HGNC) | Adenosine deaminases acting on RNA |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 7 pathways, smallest: mRNA Editing; Interferon alpha/beta signaling; PKR-mediated signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P55265](https://www.uniprot.org/uniprotkb/P55265) (Double-stranded RNA-specific adenosine deaminase):

> Catalyzes the hydrolytic deamination of adenosine to inosine in double-stranded RNA (dsRNA) referred to as A-to-I RNA editing. Edits both cellular (self) and viral (non-self) dsRNAs: can edit RNAs at multiple sites (hyper-editing) or at specific sites (site-specific editing). The primary role of ADAR is to edit and 'mask' cellular dsRNAs, which are frequently produced, and prevent recognition by innate immune receptors, such as IFIH1/MDA5, EIF2AK2/PKR and ZBP1, and autoimmunity. Edits …

**Summary**, from NCBI Gene [103](https://www.ncbi.nlm.nih.gov/gene/103):

> This gene encodes the enzyme responsible for RNA editing by site-specific deamination of adenosines. This enzyme destabilizes double-stranded RNA through conversion of adenosine to inosine. Mutations in this gene have been associated with dyschromatosis symmetrica hereditaria. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:225) · Entrez [103](https://www.ncbi.nlm.nih.gov/gene/103) · UniProt [P55265](https://www.uniprot.org/uniprotkb/P55265) · Ensembl [ENSG00000160710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160710)

## Data

Gene col 8371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8371); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8371]; `tensor/DDL_lfc|DDL_z.npy` [8371]; `embed/gene_vectors.npy` [8371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8371 or target_col == 8371). Every well: [[ADAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
