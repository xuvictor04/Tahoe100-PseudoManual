---
symbol: "NME1"
type: "gene"
col: 14205
ensembl_id: "ENSG00000239672"
name: "NME/NM23 nucleoside diphosphate kinase 1"
location: "17q21.33"
module: 4
arm: "+"
pooled_cpm: 28.36
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NME1

*NME/NM23 nucleoside diphosphate kinase 1* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.28× (z +13.8, q 3e-40, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 2.85× (z +4.2, q 0.002, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.520× (z -4.4, q 0.005, down in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 0.345× (z -4.3, q 0.005, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR77]] (+0.71, fdr 7e-06), [[PA2G4]] (+0.70, fdr 7e-06), [[ALDH1B1]] (+0.70, fdr 7e-06); moves opposite to [[KLHL24]] (-0.64, fdr 7e-06), [[UBXN1]] (-0.63, fdr 1e-05), [[UBE2B]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIK3CB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **5.28×** | +13.8 | 3e-40 | 44/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **4.67×** | +12.3 | 5e-32 | 37/38 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.46×** | +9.5 | 5e-19 | 40/44 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +5.6 | 3e-06 | 37/45 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **2.01×** | +5.5 | 4e-06 | 37/46 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.94×** | +5.5 | 4e-06 | 32/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.92×** | +5.4 | 6e-06 | 34/47 (NCI-H1792, SW480, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.94×** | +4.6 | 3e-04 | 31/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.73×** | +4.4 | 8e-04 | 29/48 (NCI-H1792, NCI-H460, …) | two highest doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **2.85×** | +4.2 | 0.002 | 35/47 (NCI-H2347, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **1.66×** | +4.2 | 0.002 | 28/46 (CFPAC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.96×** | +3.9 | 0.005 | 32/46 (SK-MEL-2, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.60×** | +3.8 | 0.006 | 32/46 (CFPAC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.57×** | +3.8 | 0.006 | 27/46 (SW1417, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.37×** | +3.7 | 0.009 | 26/48 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.50×** | +3.7 | 0.009 | 26/46 (AsPC-1, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.011 | 25/48 (A-172, HS-578T, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.019 | 25/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.27×** | +3.3 | 0.032 | 23/46 (A-172, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.038 | 22/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **2.19×** | +3.1 | 0.045 | 24/45 (PANC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.69×** | +3.0 | 0.056 | 15/48 (A498, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **2.13×** | +3.0 | 0.056 | 18/46 (NCI-H1792, C32, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.68×** | +3.0 | 0.057 | 14/47 (SW1417, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +2.8 | 0.084 | 19/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.42×** | +2.8 | 0.096 | 18/46 (SW1417, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.520×** | -4.4 | 0.005 | 34/48 (LoVo, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.345×** | -4.3 | 0.005 | 35/48 (BT-474, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.368×** | -4.0 | 0.011 | 31/48 (H4, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.420×** | -3.5 | 0.070 | 25/48 (SK-MEL-2, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.439× | -3.3 | 0.11 | 25/48 (HEC-1-A, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.762× | -3.2 | 0.11 | 21/48 (LS 180, KATO III, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 5 µM |  | 0.450× | -3.2 | 0.11 | 23/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.677× | -3.1 | 0.13 | 22/46 (C-33 A, LoVo, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.590× | -3.1 | 0.14 | 24/48 (KATO III, A498, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.73 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 35.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.6× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 31.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.53× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-172 (line)]] | wt | 24.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HOP62 (line)]] | alt | 15.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 43.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RKO (line)]] | wt | 47.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 43.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -10.8) |
| [[SW 900 (line)]] | alt | 15.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.01× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[SW480 (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.39× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-427 (line)]] | wt | 66.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A549 (line)]] | wt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HT-29 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[J82 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[KATO III (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.42× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LoVo (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[LS 180 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.2× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H23 (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.31× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SNU-423 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AN3 CA (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR77]] | +0.71 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[PA2G4]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ALDH1B1]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[C1QBP]] | +0.70 | +0.79 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[POLR1A]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[WDR43]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PHB1]] | +0.69 | +0.75 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 604 |
| [[ADAT2]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[WDR4]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[USP10]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ATIC]] | +0.67 | +0.74 / +0.62 | both halves | 7e-06 | pathway: Metabolism of nucleotides |
| [[POLR1B]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | -0.64 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[UBXN1]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.61 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.61 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[HDAC5]] | -0.61 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[EIF1]] | -0.61 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[GABARAP]] ⚠ | -0.60 | -0.60 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GGNBP2]] | -0.60 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[PHF1]] | -0.60 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[OSER1-DT]] | -0.60 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[KLC4]] | -0.59 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[SYF2]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[TOM1]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CB]] | B | PIK3CB activity raises NME1's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.5, -38.9); signed map (-5.0, -49.0). **Vector** length 79.4, 25.8% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -2.8 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.5 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | NME/NM23 nucleoside diphosphate kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:51,153,559-51,162,428 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NM23, NM23-H1, NDPKA |
| Gene groups (HGNC) | NME/NM23 family; SET complex |
| Hallmark sets | ALLOGRAFT_REJECTION, DNA_REPAIR, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 5 pathways, smallest: Ribavirin ADME; Azathioprine ADME; Interconversion of nucleotide di- and triphosphates |
| Matched by | ensembl_id |

**Function**, from UniProt [P15531](https://www.uniprot.org/uniprotkb/P15531) (Nucleoside diphosphate kinase A):

> Catalyzes the transfer of a gamma-phosphoryl group from a nucleoside triphosphate, mainly ATP, to a nucleoside diphosphate via a ping-pong mechanism involving a phosphohistidine intermediate, therefore contributing to the nucleoside triphosphate homeostasis. Also phosphorylates geranyl pyrophosphate (GPP) and farnesyl pyrophosphate (FPP), linking it to isoprenoid metabolism. Additionally, functions as a non-specific serine/threonine kinase and histidine protein kinase, transferring phosphoryl …

**Summary**, from NCBI Gene [4830](https://www.ncbi.nlm.nih.gov/gene/4830):

> This gene (NME1) was identified because of its reduced mRNA transcript levels in highly metastatic cells. Nucleoside diphosphate kinase (NDK) exists as a hexamer composed of 'A' (encoded by this gene) and 'B' (encoded by NME2) isoforms. Mutations in this gene have been identified in aggressive neuroblastomas. Two transcript variants encoding different isoforms have been found for this gene. Co-transcription of this gene and the neighboring downstream gene (NME2) generates naturally-occurring …

**Accessions** — [HGNC:7849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7849) · Entrez [4830](https://www.ncbi.nlm.nih.gov/gene/4830) · UniProt [P15531](https://www.uniprot.org/uniprotkb/P15531) · Ensembl [ENSG00000239672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239672)

## Data

Gene col 14205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14205); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14205]; `tensor/DDL_lfc|DDL_z.npy` [14205]; `embed/gene_vectors.npy` [14205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14205 or target_col == 14205). Every well: [[NME1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NME1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
