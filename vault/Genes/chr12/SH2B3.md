---
symbol: "SH2B3"
type: "gene"
col: 3209
ensembl_id: "ENSG00000111252"
name: "SH2B adaptor protein 3"
location: "12q24.12"
module: 84
arm: "+"
pooled_cpm: 33.12
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 14
direction_downstream: 1
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# SH2B3

*SH2B adaptor protein 3* — 12q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.98× (z +11.0, q 2e-25, up in 31 of 43 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.44× (z +8.3, q 1e-14, up in 23 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.641× (z -7.2, q 3e-10, down in 22 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.695× (z -6.9, q 1e-09, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX1A]] (+0.67, fdr 7e-06), [[MYO10]] (+0.65, fdr 7e-06), [[SPRY4]] (+0.65, fdr 7e-06); moves opposite to [[LINC02057]] (-0.51, fdr 3e-05), [[TGFB2]] (-0.51, fdr 3e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[SERPINE1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ST3GAL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.98×** | +11.0 | 2e-25 | 31/43 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.90×** | +10.3 | 1e-22 | 27/43 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.79×** | +9.4 | 1e-18 | 26/43 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +8.3 | 1e-14 | 23/42 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +7.6 | 2e-12 | 27/43 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +7.6 | 2e-12 | 25/42 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.6 | 3e-09 | 11/43 (A-172, J82, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.9 | 2e-07 | 22/41 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.41×** | +5.5 | 2e-06 | 18/43 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +5.5 | 3e-06 | 20/43 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 8e-06 | 21/43 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.9 | 5e-05 | 16/43 (SW480, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.29×** | +4.1 | 0.002 | 14/43 (A549, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.20× | +4.1 | 0.002 | 15/41 (A549, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.7 | 0.008 | 11/43 (NCI-H460, A498, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.011 | 9/43 (J82, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.082 | 15/43 (SW480, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.091 | 9/43 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.641×** | -7.2 | 3e-10 | 22/37 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.695×** | -6.9 | 1e-09 | 25/43 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.673×** | -6.7 | 4e-09 | 26/43 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.675×** | -6.5 | 1e-08 | 23/43 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.440×** | -6.3 | 3e-08 | 22/41 (RPMI-7951, J82, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.740×** | -5.7 | 1e-06 | 23/43 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.735×** | -5.0 | 4e-05 | 18/42 (SK-MEL-2, HOP62, …) | two highest doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.722×** | -5.0 | 4e-05 | 19/43 (C32, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.718×** | -5.0 | 4e-05 | 21/34 (HOP62, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.729×** | -4.9 | 5e-05 | 21/43 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.743×** | -4.6 | 2e-04 | 16/29 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.819×** | -4.6 | 2e-04 | 20/43 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.754×** | -4.6 | 2e-04 | 16/43 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.759×** | -4.5 | 3e-04 | 14/43 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.760×** | -4.3 | 7e-04 | 19/42 (HOP62, J82, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.769×** | -4.3 | 8e-04 | 18/43 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.844× | -3.9 | 0.004 | 15/43 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.724×** | -3.7 | 0.006 | 9/40 (HCT15, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 156 | 0 | 14 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.160× (z -12.0) |
| [[C32 (line)]] | wt | 54.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.2) |
| [[PANC-1 (line)]] | alt | 52.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +13.9) | — |
| [[SK-MEL-2 (line)]] | alt | 90.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.357× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 14.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +20.5) | — |
| [[LOX-IMVI (line)]] | wt | 47.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 27.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -9.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 70.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -11.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 94.9 | 0 | 2 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.194× (z -12.8) |
| [[A-172 (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.49 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -8.6) ⚠ toxic |
| [[A549 (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +14.3) | — |
| [[H4 (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +12.4) | — |
| [[J82 (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 1 | — | [[Adagrasib (drug)]] 5 µM 0.210× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX1A]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MYO10]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | same gene group |
| [[SPRY4]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CD82]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RASA3]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 | same gene group |
| [[RAC2]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PHC2]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[KIF21B]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 | pathway: Factors involved in megakaryocyte development and platelet production |
| [[FLT1]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[HIVEP3]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[KCNN4]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[RFX8]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02057]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TGFB2]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE1]] | B | SERPINE1 activity raises SH2B3's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.82× lower at baseline in the lines without SERPINE1 | 0.006 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[VEPH1]] | B | VEPH1 activity raises SH2B3's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without VEPH1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[LINC01812]] | B | LINC01812 activity raises SH2B3's level | lines that do not express LINC01812 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without LINC01812 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235495, ENSG00000224865, ENSG00000287622 |
| [[CDH13]] | B | CDH13 activity raises SH2B3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without CDH13 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[GFPT2]] | B | GFPT2 activity raises SH2B3's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without GFPT2 | 0.028 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[ITGA11]] | B | ITGA11 activity raises SH2B3's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.31× lower at baseline in the lines without ITGA11 | 0.034 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[INSYN2B]] | B | INSYN2B activity raises SH2B3's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 2.54× lower at baseline in the lines without INSYN2B | 0.054 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[NAV1]] | B | NAV1 activity raises SH2B3's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.44× lower at baseline in the lines without NAV1 | 0.062 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises SH2B3's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without HS3ST3A1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[LRFN5]] | B | LRFN5 activity raises SH2B3's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 1.88× lower at baseline in the lines without LRFN5 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1 |
| [[SPOCD1]] | B | SPOCD1 activity raises SH2B3's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 2.30× lower at baseline in the lines without SPOCD1 | 0.089 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[FLT1]] | B | FLT1 activity raises SH2B3's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without FLT1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL2]] | B | SH2B3 activity raises ST3GAL2's level | lines that do not express SH2B3 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without SH2B3 | 0.089 | ⚠ within organs, on part of the lines; also absent: VAT1, CEP112, FCHSD1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.6, 6.4); signed map (6.2, 49.6). **Vector** length 118, 31.2% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.7 | +11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.9 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.4 | -0.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.9 | -6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -6.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.3 | -6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.1 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -4.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.7 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | SH2B adaptor protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.12 — chr12:111,405,923-111,451,623 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LNK, IDDM20 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing; SH2B adaptor protein family |
| Hallmark sets | COMPLEMENT |
| Reactome | 8 pathways, smallest: Negative regulation of FLT3; Regulation of KIT signaling; FLT3 Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQQ2](https://www.uniprot.org/uniprotkb/Q9UQQ2) (SH2B adapter protein 3):

> Links T-cell receptor activation signal to phospholipase C-gamma-1, GRB2 and phosphatidylinositol 3-kinase.

**Summary**, from NCBI Gene [10019](https://www.ncbi.nlm.nih.gov/gene/10019):

> This gene encodes a member of the SH2B adaptor family of proteins, which are involved in a range of signaling activities by growth factor and cytokine receptors. The encoded protein is a key negative regulator of cytokine signaling and plays a critical role in hematopoiesis. Mutations in this gene have been associated with susceptibility to celiac disease type 13 and susceptibility to insulin-dependent diabetes mellitus. Alternatively spliced transcript variants encoding different isoforms have …

**Accessions** — [HGNC:29605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29605) · Entrez [10019](https://www.ncbi.nlm.nih.gov/gene/10019) · UniProt [Q9UQQ2](https://www.uniprot.org/uniprotkb/Q9UQQ2) · Ensembl [ENSG00000111252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111252)

## Data

Gene col 3209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3209); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3209]; `tensor/DDL_lfc|DDL_z.npy` [3209]; `embed/gene_vectors.npy` [3209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3209 or target_col == 3209). Every well: [[SH2B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH2B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
