---
symbol: "TRAF7"
type: "gene"
col: 5230
ensembl_id: "ENSG00000131653"
name: "TNF receptor associated factor 7"
location: "16p13.3"
module: 2
arm: "+"
pooled_cpm: 20.71
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TRAF7

*TNF receptor associated factor 7* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +19.1, q 0e+00, up in 42 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.41× (z +5.7, q 8e-07, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.893× (z -6.7, q 1e-08, down in 8 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Hydroxyurea (drug)]] 0.5 µM: 0.817× (z -3.4, q 0.083, down in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.259×, RKO 0.292×, HT-29 0.437×, LoVo 0.412×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1573 0.443×, C-33 A 0.359×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.196×; ⚠ cell-cycle shift, explains ~0% of this change); [[MK-3903 (drug)]] 0.05 µM in 1 line (AN3 CA 0.0818×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX3]] (+0.69, fdr 7e-06), [[TBCD]] (+0.68, fdr 1e-05), [[ABCA2]] (+0.66, fdr 1e-05); moves opposite to [[EIF3J-DT]] (-0.61, fdr 2e-05), [[ZSWIM3]] (-0.59, fdr 1e-05), [[PCF11-AS1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[DGKZ]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +19.1 | 0e+00 | 42/42 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +16.7 | 0e+00 | 33/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +12.6 | 6e-34 | 36/39 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +8.9 | 1e-16 | 33/42 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.65×** | +8.2 | 2e-14 | 32/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.61×** | +7.9 | 4e-13 | 29/47 (KATO III, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.57×** | +7.5 | 6e-12 | 34/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.7 | 8e-07 | 24/46 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +4.6 | 2e-04 | 21/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.27×** | +3.8 | 0.007 | 16/45 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.015 | 18/46 (SW 900, SW1417, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.017 | 15/47 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.024 | 13/47 (SW1417, SW48, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +3.2 | 0.047 | 12/47 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.072 | 9/44 (SW480, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.073 | 9/47 (C32, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5230.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-427 0.259×, RKO 0.292×, HT-29 0.437×, LoVo 0.412×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H1573 0.443×, C-33 A 0.359×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.196×; ⚠ cell-cycle shift, explains ~0% of this change); [[MK-3903 (drug)]] 0.05 µM in 1 line (AN3 CA 0.0818×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -6.7 | 1e-08 | 8/48 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.774×** | -5.8 | 2e-06 | 23/48 (A498, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.756×** | -4.7 | 6e-04 | 19/48 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -4.0 | 0.008 | 19/47 (A-427, RKO, …) | rises with dose | composition shift |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.083 | 10/47 (SNU-423, SW480, …) | inconsistent across doses | position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.823× | -3.3 | 0.11 | 6/47 (RKO, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Triclosan (drug)]] 5 µM |  | 0.873× | -3.1 | 0.17 | 14/48 (CHP-212, COLO 205, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.825× | -3.0 | 0.17 | 7/48 (SW 1088, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 29.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.1) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.522× (z -8.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 18.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.06× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 35.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +12.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 28.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 40.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +13.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 26.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 1 | — | [[MK-3903 (drug)]] 0.05 µM 0.0818× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 7.89 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.49× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.25× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX3]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TBCD]] | +0.68 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.66 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PTGES2]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CS]] | +0.65 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[BLTP2]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CDK16]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[LHPP]] | +0.64 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[AKT1]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 | STRING 542 |
| [[SBF1]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ADAM15]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.63 | +0.56 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3J-DT]] | -0.61 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ZSWIM3]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PCF11-AS1]] | -0.58 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[KDM4D]] | -0.57 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[PBDC1]] | -0.57 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ZNF341-AS1]] | -0.57 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[PPP2R3C]] | -0.56 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[ZNF75A]] | -0.56 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[ZNF407-AS1]] | -0.55 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[SNRPB2]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ZNF585A]] | -0.55 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZNF791]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKZ]] | C | TRAF7's natural level weakens DGKZ's drug response | TRAF7's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69, reverse +0.09; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.7, -22.2); signed map (-44.6, -12.2). **Vector** length 74.6, 14.3% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +12.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.0 | +7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.5 | +0.9 |
|  | [[Pentoxifylline (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.3 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.6 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor associated factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,155,698-2,178,129 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF119, DKFZp586I021, MGC7807; previously RFWD1 |
| Gene groups (HGNC) | Ring finger proteins; WD repeat domain containing; TNF receptor associated factors; Zinc fingers TRAF-type; RING finger E3 ubiquitin protein ligases |
| Reactome | 8 pathways, smallest: Activation of STAT3 by cadherin engagement; Adherens junctions interactions; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6Q0C0](https://www.uniprot.org/uniprotkb/Q6Q0C0) (E3 ubiquitin-protein ligase TRAF7):

> E3 ubiquitin and SUMO-protein ligase that plays a role in different biological processes such as innate immunity, inflammation or apoptosis. Potentiates MAP3K3-mediated activation of JUN/AP1 and DDIT3 transcriptional regulators. Negatively regulates MYB transcriptional activity by sequestering it to the cytosol via SUMOylation (By similarity). Plays a role in the phosphorylation of MAPK1 and/or MAPK3, probably via its interaction with MAP3K3. Negatively regulates RLR-mediated innate immunity by …

**Summary**, from NCBI Gene [84231](https://www.ncbi.nlm.nih.gov/gene/84231):

> Tumor necrosis factor (TNF; see MIM 191160) receptor-associated factors, such as TRAF7, are signal transducers for members of the TNF receptor superfamily (see MIM 191190). TRAFs are composed of an N-terminal cysteine/histidine-rich region containing zinc RING and/or zinc finger motifs; a coiled-coil (leucine zipper) motif; and a homologous region that defines the TRAF family, the TRAF domain, which is involved in self-association and receptor binding.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:20456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20456) · Entrez [84231](https://www.ncbi.nlm.nih.gov/gene/84231) · UniProt [Q6Q0C0](https://www.uniprot.org/uniprotkb/Q6Q0C0) · Ensembl [ENSG00000131653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131653)

## Data

Gene col 5230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5230); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5230]; `tensor/DDL_lfc|DDL_z.npy` [5230]; `embed/gene_vectors.npy` [5230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5230 or target_col == 5230). Every well: [[TRAF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
