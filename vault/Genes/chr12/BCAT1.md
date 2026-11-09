---
symbol: "BCAT1"
type: "gene"
col: 697
ensembl_id: "ENSG00000060982"
name: "branched chain amino acid transaminase 1"
location: "12p12.1"
module: 63
arm: "+"
pooled_cpm: 88.61
n_lines_expressing: 25
n_dd_up: 27
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# BCAT1

*branched chain amino acid transaminase 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.13× (z +27.8, q 0e+00, up in 15 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.65× (z +9.8, q 1e-20, up in 17 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.502× (z -13.5, q 5e-39, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH1L2]] (+0.58, fdr 1e-05), [[PHGDH]] (+0.52, fdr 2e-05), [[TARS1]] (+0.51, fdr 8e-05); moves opposite to [[ZBTB48]] (-0.47, fdr 1e-04), [[TUBD1]] (-0.46, fdr 2e-04), [[RABIF]] (-0.43, fdr 2e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[POSTN]] → it (grade C ⚠); 7 go from it, the strongest it → [[CLIC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.13×** | +27.8 | 0e+00 | 15/23 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +20.6 | 0e+00 | 16/21 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +14.2 | 2e-43 | 14/21 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +9.8 | 1e-20 | 17/23 (A498, NCI-H23, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.48×** | +7.7 | 2e-12 | 19/23 (NCI-H460, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.4 | 2e-11 | 5/23 (NCI-H23, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +6.4 | 2e-08 | 11/24 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +6.0 | 2e-07 | 4/17 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.9 | 2e-07 | 6/23 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.3 | 6e-06 | 12/22 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.28×** | +4.9 | 6e-05 | 2/23 (NCI-H1792, HS-578T) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.7 | 1e-04 | 16/23 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +4.3 | 7e-04 | 15/23 (J82, NCI-H23, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +4.3 | 8e-04 | 13/23 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.002 | 1/23 (NCI-H23) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.005 | 1/25 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.005 | 2/23 (NCI-H460, NCI-H23) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.009 | 8/23 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.010 | 7/23 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.016 | 7/23 (A-172, Hs 766T, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.016 | 1/23 (A-172) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.019 | 2/23 (C-33 A, A-172) | top dose only |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.027 | 5/23 (NCI-H23, C-33 A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.502×** | -13.5 | 5e-39 | 21/23 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.519×** | -12.9 | 2e-35 | 21/23 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.526×** | -12.6 | 3e-34 | 22/23 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.658×** | -8.2 | 3e-14 | 19/23 (LS 180, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.688×** | -7.3 | 3e-11 | 19/23 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.716×** | -6.6 | 5e-09 | 15/23 (CFPAC-1, J82, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.820×** | -5.5 | 3e-06 | 9/23 (LS 180, J82, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.767×** | -4.8 | 1e-04 | 12/23 (Hs 766T, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.672×** | -4.1 | 0.003 | 11/24 (CHP-212, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.864× | -4.0 | 0.003 | 0/23 | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.687×** | -3.9 | 0.006 | 19/23 (J82, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.829×** | -3.7 | 0.011 | 5/22 (A-172, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.881× | -3.4 | 0.028 | 2/23 (NCI-H23, SW 1088) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.831×** | -3.4 | 0.032 | 0/23 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.078 | 0/23 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 357 | 0 | 11 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.289× (z -19.4) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.222× (z -16.6) |
| [[NCI-H460 (line)]] | wt | 57.0 | 4 (4 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.13× (z +14.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.423× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 473 | 1 (1 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -22.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -18.4) |
| [[J82 (line)]] | alt | 374 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -22.7) |
| [[LoVo (line)]] | wt | 94.0 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.8) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.311× (z -11.0) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.328× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 266 | 1 (1 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -12.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.414× (z -10.3) |
| [[CHP-212 (line)]] | wt | 394 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.233× (z -13.2) |
| [[HOP62 (line)]] | alt | 553 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -18.1) |
| [[Hs 766T (line)]] | wt | 90.5 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 269 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -22.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.201× (z -20.1) |
| [[HS-578T (line)]] | alt | 160 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -15.5) |
| [[C-33 A (line)]] | alt | 145 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -19.8) |
| [[A498 (line)]] | wt | 87.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -10.2) |
| [[H4 (line)]] | wt | 154 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0432× (z -13.0) |
| [[A-172 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.58 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.57 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.10 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH1L2]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 | STRING 414 |
| [[PHGDH]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 520 |
| [[TARS1]] | +0.51 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[PSAT1]] | +0.50 | +0.38 / +0.55 | both halves | 6e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 653 |
| [[PYCR1]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[YARS1]] | +0.50 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[OGT]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[IARS1]] | +0.49 | +0.41 / +0.54 | both halves | 4e-05 | pathway: Metabolism of amino acids and derivatives |
| [[SLC39A14]] | +0.48 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[XPOT]] | +0.47 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[TCEA1]] | +0.47 | +0.33 / +0.56 | both halves | 1e-04 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PRUNE2]] | +0.47 | +0.30 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 4 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB48]] | -0.47 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[TUBD1]] | -0.46 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[RABIF]] | -0.43 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[CDC37L1]] | -0.42 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[TOPORS]] | -0.41 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[CIB1]] | -0.41 | -0.16 / -0.50 | ⚠ not reproduced | 0.001 |  |
| [[MRPL51]] ⚠ | -0.41 | -0.26 / -0.46 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TBCC]] | -0.39 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[SOX4]] | -0.39 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[ZNF503]] | -0.38 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[FBXO46]] | -0.38 | -0.20 / -0.38 | ⚠ not reproduced | 8e-04 |  |
| [[RETREG3]] | -0.38 | -0.19 / -0.40 | ⚠ not reproduced | 8e-04 |  |
| [[BMS1P1]] | -0.38 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[POLD4]] | -0.38 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[GCC2]] | -0.37 | -0.28 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POSTN]] | C | POSTN activity raises BCAT1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 6.51× lower at baseline in the lines without POSTN | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[CHRDL1]] | C | CHRDL1 activity raises BCAT1's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 4.17× lower at baseline in the lines without CHRDL1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[ITGBL1]] | C | ITGBL1 activity raises BCAT1's level | lines that do not express ITGBL1 (30) vs lines expressing it (20) | 3.71× lower at baseline in the lines without ITGBL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: STEAP1B-AS1, FLI1, ENSG00000255983; co-absent with the target |
| [[ALDH1L2]] | C | ALDH1L2 activity raises BCAT1's level | lines that do not express ALDH1L2 (23) vs lines expressing it (27) | 3.00× lower at baseline in the lines without ALDH1L2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ENSG00000230490, GPR173; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLIC4]] | B | BCAT1 activity raises CLIC4's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 1.63× lower at baseline in the lines without BCAT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX |
| [[LTBP1]] | B | BCAT1 activity raises LTBP1's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 2.26× lower at baseline in the lines without BCAT1 | 0.085 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX |
| [[PHGDH]] | B | BCAT1 activity raises PHGDH's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without BCAT1 | 0.088 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX |
| [[ALDH1L2]] | C | BCAT1 activity raises ALDH1L2's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 2.82× lower at baseline in the lines without BCAT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX; co-absent with the target |
| [[CHRDL1]] | C | BCAT1 activity raises CHRDL1's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 1.94× lower at baseline in the lines without BCAT1 | 0.029 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX; co-absent with the target |
| [[COL12A1]] | C | BCAT1 activity raises COL12A1's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 3.74× lower at baseline in the lines without BCAT1 | 0.073 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX; co-absent with the target |
| [[POSTN]] | C | BCAT1 activity raises POSTN's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 3.13× lower at baseline in the lines without BCAT1 | 0.085 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX; co-absent with the target |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.2, 46.5); signed map (-14.8, 25.1). **Vector** length 77.1, 19.5% of its response variance represented; |z| ≥ 3 in 774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.5 | +20.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.4 | +27.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.3 | +14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.4 | -6.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -3.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | branched chain amino acid transaminase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:24,810,024-24,949,101 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCATc; previously BCT1 |
| Gene groups (HGNC) | Branched chain amino acid transaminase family |
| Hallmark sets | ALLOGRAFT_REJECTION, XENOBIOTIC_METABOLISM, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Branched-chain amino acid catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P54687](https://www.uniprot.org/uniprotkb/P54687) (Branched-chain-amino-acid aminotransferase, cytosolic):

> Catalyzes the first reaction in the catabolism of the essential branched chain amino acids leucine, isoleucine, and valine.

**Summary**, from NCBI Gene [586](https://www.ncbi.nlm.nih.gov/gene/586):

> This gene encodes the cytosolic form of the enzyme branched-chain amino acid transaminase. This enzyme catalyzes the reversible transamination of branched-chain alpha-keto acids to branched-chain L-amino acids essential for cell growth. Two different clinical disorders have been attributed to a defect of branched-chain amino acid transamination: hypervalinemia and hyperleucine-isoleucinemia. As there is also a gene encoding a mitochondrial form of this enzyme, mutations in either gene may …

**Accessions** — [HGNC:976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:976) · Entrez [586](https://www.ncbi.nlm.nih.gov/gene/586) · UniProt [P54687](https://www.uniprot.org/uniprotkb/P54687) · Ensembl [ENSG00000060982](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060982)

## Data

Gene col 697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 697); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 697]; `tensor/DDL_lfc|DDL_z.npy` [697]; `embed/gene_vectors.npy` [697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 697 or target_col == 697). Every well: [[BCAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
