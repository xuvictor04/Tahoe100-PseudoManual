---
symbol: "HUWE1"
type: "gene"
col: 1472
ensembl_id: "ENSG00000086758"
name: "HECT, UBA and WWE domain containing E3 ubiquitin protein ligase 1"
location: "Xp11.22"
module: 25
arm: "+"
pooled_cpm: 394.25
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# HUWE1

*HECT, UBA and WWE domain containing E3 ubiquitin protein ligase 1* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +10.8, q 3e-24, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.649× (z -11.1, q 5e-26, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NONO]] (+0.73, fdr 7e-06), [[PDAP1]] (+0.71, fdr 7e-06), [[DYNC1H1]] (+0.70, fdr 7e-06); moves opposite to [[SNHG9]] (-0.63, fdr 2e-05), [[SNHG19]] (-0.62, fdr 3e-05), [[COMMD6]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +10.8 | 3e-24 | 42/48 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 2e-06 | 42/48 (HT-29, COLO 205, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.5 | 7e-06 | 35/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.5 | 7e-06 | 37/48 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +5.3 | 2e-05 | 38/48 (HT-29, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 3e-05 | 37/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +5.0 | 5e-05 | 30/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.0 | 0.004 | 30/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.014 | 27/49 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +3.7 | 0.014 | 25/48 (A498, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.37× | +3.0 | 0.13 | 26/48 (RKO, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1472.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -11.1 | 5e-26 | 44/49 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.545×** | -10.6 | 5e-24 | 46/47 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.709×** | -6.3 | 7e-08 | 43/48 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.685×** | -4.9 | 1e-04 | 45/48 (SHP-77, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.768×** | -4.8 | 2e-04 | 32/48 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.772×** | -4.7 | 2e-04 | 35/48 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.778×** | -4.6 | 4e-04 | 31/48 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.828×** | -3.4 | 0.042 | 25/48 (SW48, PANC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.785× | -3.1 | 0.11 | 32/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 339 | 5 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -12.8) |
| [[A498 (line)]] | wt | 271 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 302 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -10.4) |
| [[PANC-1 (line)]] | alt | 506 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -12.1) |
| [[C32 (line)]] | wt | 229 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 493 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -9.8) |
| [[HT-29 (line)]] | alt | 410 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.452× (z -10.5) ⚠ toxic |
| [[J82 (line)]] | alt | 458 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -11.9) |
| [[LoVo (line)]] | wt | 312 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 316 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 506 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -11.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 546 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 1.95× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -10.1) |
| [[SNU-1 (line)]] | wt | 331 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -13.8) |
| [[A549 (line)]] | wt | 432 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -19.4) |
| [[AsPC-1 (line)]] | alt | 216 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +17.1) | — |
| [[CHP-212 (line)]] | wt | 369 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.6) |
| [[COLO 205 (line)]] | alt | 384 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.484× (z -9.2) ⚠ toxic |
| [[HOP62 (line)]] | alt | 561 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.464× (z -10.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -10.3) |
| [[HS-578T (line)]] | alt | 233 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 342 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.368× (z -12.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.2) |
| [[KATO III (line)]] | alt | 464 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.458× (z -10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 222 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +15.7) | [[Panobinostat (drug)]] 5 µM 0.575× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 441 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.462× (z -10.3) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 209 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 370 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.519× (z -9.6) |
| [[RKO (line)]] | wt | 341 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.558× (z -8.5) ⚠ toxic |
| [[SW 900 (line)]] | alt | 377 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.293× (z -14.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.484× (z -8.8) |
| [[SW480 (line)]] | alt | 616 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.444× (z -12.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -11.6) |
| [[A-172 (line)]] | wt | 336 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.3) | — |
| [[A-427 (line)]] | wt | 463 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.472× (z -10.1) ⚠ toxic |
| [[BT-474 (line)]] | alt | 449 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.533× (z -9.0) ⚠ cell-cycle shift, explains ~15% of this change |
| [[C-33 A (line)]] | alt | 356 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -10.9) |
| [[H4 (line)]] | wt | 477 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.10× (z +9.0) ⚠ unreliable plate only | — |
| [[Hs 766T (line)]] | wt | 330 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 331 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -10.5) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 280 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.539× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 318 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.530× (z -8.5) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SHP-77 (line)]] | alt | 733 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.474× (z -11.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 603 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -9.9) |
| [[SW1417 (line)]] | alt | 453 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.469× (z -10.4) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 357 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 417 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 232 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 371 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NONO]] | +0.73 | +0.67 / +0.78 | both halves | 7e-06 | STRING 424 |
| [[PDAP1]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[DYNC1H1]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 | STRING 602 |
| [[LIN7C]] | +0.70 | +0.58 / +0.78 | both halves | 8e-06 |  |
| [[PTPN11]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[YWHAE]] | +0.69 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[CCT7]] | +0.66 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PSMC3]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 437 |
| [[SPTBN1]] | +0.65 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[DBN1]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.63 | +0.56 / +0.70 | both halves | 1e-05 | same gene group |
| [[CLTC]] | +0.63 | +0.51 / +0.71 | both halves | 1e-05 | STRING 622 |

## Genes that move opposite

*44 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG9]] | -0.63 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[SNHG19]] | -0.62 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[COMMD6]] | -0.62 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[SNHG25]] | -0.62 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[MIR4458HG]] | -0.62 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.61 | -0.51 / -0.65 | both halves | 1e-05 | same gene group |
| [[NCBP2AS2]] | -0.61 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[ZNF500]] | -0.61 | -0.41 / -0.69 | both halves | 4e-05 |  |
| [[MALSU1]] | -0.60 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[MINCR]] | -0.60 | -0.45 / -0.67 | both halves | 3e-05 |  |
| [[MIR762HG]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[MZT2A]] | -0.59 | -0.43 / -0.65 | both halves | 3e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises HUWE1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-33.9, -20.6); signed map (-16.2, -35.9). **Vector** length 129, 46.9% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.5 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.4 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +0.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +2.9 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.1 | -10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.9 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.7 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | HECT, UBA and WWE domain containing E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:53,532,096-53,686,752 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ib772, KIAA0312, UREB1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; MicroRNA protein coding host genes; HECT domain E3 ubiquitin protein ligases |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 5 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6Z7](https://www.uniprot.org/uniprotkb/Q7Z6Z7) (E3 ubiquitin-protein ligase HUWE1):

> E3 ubiquitin-protein ligase which mediates ubiquitination and subsequent proteasomal degradation of target proteins. Regulates apoptosis by catalyzing the polyubiquitination and degradation of MCL1. Mediates monoubiquitination of DNA polymerase beta (POLB) at 'Lys-41', 'Lys-61' and 'Lys-81', thereby playing a role in base-excision repair. Also ubiquitinates the p53/TP53 tumor suppressor and core histones including H1, H2A, H2B, H3 and H4. Ubiquitinates MFN2 to negatively regulate mitochondrial …

**Summary**, from NCBI Gene [10075](https://www.ncbi.nlm.nih.gov/gene/10075):

> This gene encodes a protein containing a C-terminal HECT (E6AP type E3 ubiquitin protein ligase) domain that functions as an E3 ubiquitin ligase. The encoded protein is required for the ubiquitination and subsequent degradation of the anti-apoptotic protein Mcl1 (myeloid cell leukemia sequence 1 (BCL2-related)). This protein also ubiquitinates the p53 tumor suppressor, core histones, and DNA polymerase beta. Mutations in this gene are associated with Turner type X-linked syndromic cognitive …

**Accessions** — [HGNC:30892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30892) · Entrez [10075](https://www.ncbi.nlm.nih.gov/gene/10075) · UniProt [Q7Z6Z7](https://www.uniprot.org/uniprotkb/Q7Z6Z7) · Ensembl [ENSG00000086758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086758)

## Data

Gene col 1472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1472); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1472]; `tensor/DDL_lfc|DDL_z.npy` [1472]; `embed/gene_vectors.npy` [1472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1472 or target_col == 1472). Every well: [[HUWE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HUWE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
