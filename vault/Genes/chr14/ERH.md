---
symbol: "ERH"
type: "gene"
col: 2006
ensembl_id: "ENSG00000100632"
name: "ERH mRNA splicing and mitosis factor"
location: "14q24.1"
module: 4
arm: "+"
pooled_cpm: 48.78
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ERH

*ERH mRNA splicing and mitosis factor* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.22× (z +16.8, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Rapamycin (drug)]] 5 µM: 0.841× (z -4.8, q 8e-04, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (HCT15 0.262×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP155]] (+0.69, fdr 7e-06), [[DARS2]] (+0.68, fdr 1e-05), [[COPS3]] (+0.68, fdr 7e-06); moves opposite to [[SIRT2]] (-0.66, fdr 7e-06), [[CAMLG]] (-0.65, fdr 1e-05), [[GABARAPL2]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.22×** | +16.8 | 0e+00 | 48/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.32×** | +16.4 | 0e+00 | 43/47 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.22×** | +14.9 | 0e+00 | 38/43 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.90×** | +11.6 | 1e-28 | 35/45 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +8.8 | 1e-16 | 37/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.34×** | +8.1 | 5e-14 | 29/48 (A549, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.6 | 2e-12 | 34/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.46×** | +7.3 | 2e-11 | 31/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.42×** | +6.8 | 7e-10 | 29/46 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +6.6 | 2e-09 | 34/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.37×** | +6.1 | 4e-08 | 29/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +6.0 | 1e-07 | 26/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +5.9 | 2e-07 | 25/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.8 | 2e-07 | 26/48 (SW480, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.37×** | +5.8 | 2e-07 | 28/47 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +5.6 | 6e-07 | 28/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 8e-04 | 20/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.008 | 15/48 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.011 | 9/48 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.042 | 16/48 (A549, NCI-H661, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +2.9 | 0.058 | 13/48 (J82, CFPAC-1, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +2.9 | 0.065 | 12/48 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.32×** | +2.8 | 0.076 | 15/48 (C32, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.23×** | +2.8 | 0.081 | 10/48 (HOP62, A498, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2006.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (HCT15 0.262×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 5 µM |  | 0.841× | -4.8 | 8e-04 | 22/48 (NCI-H661, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.873× | -3.7 | 0.048 | 11/48 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.826×** | -3.6 | 0.048 | 13/47 (LoVo, CHP-212, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.824×** | -3.6 | 0.048 | 13/48 (SW 1271, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.842× | -3.4 | 0.074 | 15/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.720×** | -3.4 | 0.074 | 12/48 (CHP-212, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.828× | -3.0 | 0.15 | 11/48 (A-427, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.857× | -3.0 | 0.15 | 9/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.746× | -3.0 | 0.15 | 12/48 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 42.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.46× (z +18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.65× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 44.4 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.34× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 36.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.90× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 54.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 35.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A498 (line)]] | wt | 54.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[C32 (line)]] | wt | 35.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.3) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 46.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[KATO III (line)]] | alt | 48.8 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.81× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 32.3 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.7× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 29.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 59.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.42× (z +10.6) | — |
| [[A-172 (line)]] | wt | 26.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.89× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 56.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.89× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 44.4 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.35× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 56.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H460 (line)]] | wt | 39.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HCT15 (line)]] | alt | 62.1 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.262× (z -9.9) |
| [[HS-578T (line)]] | alt | 29.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.92× (z +9.0) | — |
| [[J82 (line)]] | alt | 54.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LOX-IMVI (line)]] | wt | 30.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H23 (line)]] | alt | 105 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.93× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 54.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.91× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW1417 (line)]] | alt | 47.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.62× (z +9.4) | — |
| [[A-427 (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 74.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP155]] | +0.69 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[DARS2]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[COPS3]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[ADAT1]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[XRCC6]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[EIF2S1]] | +0.65 | +0.68 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[SSU72]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[XRCC5]] | +0.64 | +0.54 / +0.67 | both halves | 1e-05 | STRING 436 |
| [[TMX2]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[NCBP1]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 434 |
| [[GCN1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[MFN2]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[CAMLG]] | -0.65 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[GABARAPL2]] | -0.65 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.63 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.63 | -0.44 / -0.70 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V1; ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | -0.63 | -0.52 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG7]] | -0.63 | -0.46 / -0.69 | both halves | 3e-05 |  |
| [[RPL36]] | -0.62 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[RPS12]] | -0.61 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[TMEM191A-1]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[RPS27]] | -0.60 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[RPS27A]] ⚠ | -0.60 | -0.46 / -0.66 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | -0.60 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[RPL35A]] | -0.59 | -0.45 / -0.66 | both halves | 3e-05 | STRING 424 |
| [[DUSP18]] | -0.59 | -0.51 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises ERH's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without HES6 | 0.007 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LLGL2]] | B | LLGL2 activity raises ERH's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 1.44× lower at baseline in the lines without LLGL2 | 0.014 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-33.6, -32.3); signed map (-13.9, -43.5). **Vector** length 78.6, 18.7% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.4 | +16.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.3 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.9 | +16.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.6 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.9 | +0.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.7 | +0.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | -2.8 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | -2.0 | -1.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[4EGI-1 (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ERH mRNA splicing and mitosis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:69,380,128-69,398,299 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DROER |
| Hallmark sets | MYC_TARGETS_V1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P84090](https://www.uniprot.org/uniprotkb/P84090) (Enhancer of rudimentary homolog):

> May have a role in the cell cycle.

**Summary**, from NCBI Gene [2079](https://www.ncbi.nlm.nih.gov/gene/2079):

> Enables methyl-CpG binding activity. Predicted to be involved in mRNA export from nucleus and pyrimidine nucleoside metabolic process. Located in midbody and nucleus. Part of methylosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3447) · Entrez [2079](https://www.ncbi.nlm.nih.gov/gene/2079) · UniProt [P84090](https://www.uniprot.org/uniprotkb/P84090) · Ensembl [ENSG00000100632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100632)

## Data

Gene col 2006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2006); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2006]; `tensor/DDL_lfc|DDL_z.npy` [2006]; `embed/gene_vectors.npy` [2006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2006 or target_col == 2006). Every well: [[ERH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
