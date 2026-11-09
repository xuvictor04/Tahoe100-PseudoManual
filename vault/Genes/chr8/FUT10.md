---
symbol: "FUT10"
type: "gene"
col: 10285
ensembl_id: "ENSG00000172728"
name: "protein O-fucosyltransferase 3"
location: "8p12"
module: 25
arm: "+"
pooled_cpm: 22.76
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# FUT10

*protein O-fucosyltransferase 3* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.76× (z +24.6, q 0e+00, up in 30 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.49× (z +7.6, q 3e-12, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.915× (z -6.0, q 1e-06, down in 1 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Simotinib (drug)]] 0.05 µM: 0.801× (z -3.9, q 0.009, down in 14 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.206×, NCI-H1573 0.158×; ⚠ cell-cycle shift, explains ~48% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0618×; ⚠ toxic; cell-cycle shift, explains ~66% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.333×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (AN3 CA 0.126×).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCP2]] (+0.61, fdr 2e-05), [[RAVER2]] (+0.61, fdr 1e-05), [[RAD23B]] (+0.60, fdr 6e-05); moves opposite to [[H3-3B]] (-0.58, fdr 3e-05), [[TRAPPC4]] (-0.57, fdr 2e-04), [[ZNF324]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRTAP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10285.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +24.6 | 0e+00 | 30/33 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +20.0 | 0e+00 | 36/42 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +19.4 | 0e+00 | 31/36 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +7.6 | 3e-12 | 26/48 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.32×** | +7.6 | 3e-12 | 29/48 (A-172, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.2 | 5e-08 | 23/48 (A-172, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +5.7 | 1e-06 | 21/47 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +5.6 | 1e-06 | 17/46 (A-172, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +5.3 | 7e-06 | 20/47 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.1 | 2e-05 | 13/27 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +5.0 | 3e-05 | 16/48 (A-172, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.28×** | +4.8 | 8e-05 | 15/46 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.29×** | +4.7 | 1e-04 | 18/45 (A-172, J82, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +4.5 | 2e-04 | 12/46 (A549, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 8e-04 | 17/46 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.004 | 14/47 (NCI-H1573, A549, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.017 | 11/48 (AsPC-1, H4, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.023 | 13/47 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.052 | 13/47 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.066 | 4/46 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.068 | 7/47 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.070 | 3/47 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.085 | 1/48 (KATO III) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10285.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.206×, NCI-H1573 0.158×; ⚠ cell-cycle shift, explains ~48% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0618×; ⚠ toxic; cell-cycle shift, explains ~66% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.333×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (AN3 CA 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -6.0 | 1e-06 | 1/48 (hTERT-HPNE) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **0.796×** | -4.4 | 0.003 | 17/44 (NCI-H661, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.808×** | -4.1 | 0.008 | 14/47 (SW480, NCI-H2030, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.814×** | -4.0 | 0.009 | 20/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.05 µM |  | **0.801×** | -3.9 | 0.009 | 14/46 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.697×** | -3.8 | 0.016 | 12/44 (Panc 03.27, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.876× | -3.6 | 0.026 | 14/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.845× | -3.2 | 0.089 | 8/47 (SNU-423, RKO, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.748× | -3.0 | 0.16 | 9/46 (SNU-423, CHP-212, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10285. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 37.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +14.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 22.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 23.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 9.95 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 21.4× (z +16.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 26.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.99× (z +17.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 26.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.7× (z +23.0) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 23.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.49× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 13.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 10.6× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 10.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.60× (z +14.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 8.96 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.79× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 17.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.28× (z +10.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -13.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.333× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 20.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.91× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 38.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.126× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0618× (z -16.1) ⚠ toxic; cell-cycle shift, explains ~66% of this change |
| [[Hs 766T (line)]] | wt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 9.41 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.64× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -12.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[RPMI-7951 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.87× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10285), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCP2]] | +0.61 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[RAVER2]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.60 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[DPY19L4]] | +0.58 | +0.14 / +0.64 | ⚠ one half (not replicated) | 0.002 |  |
| [[FECH]] | +0.58 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[DHFR]] | +0.57 | +0.17 / +0.62 | ⚠ one half (not replicated) | 0.001 |  |
| [[TMEM64]] | +0.57 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[LARP1]] | +0.56 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[GSR]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[UBQLN1]] | +0.55 | +0.37 / +0.58 | both halves | 9e-05 |  |
| [[BTBD1]] | +0.55 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[SMG7]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.55 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[PFKM]] | +0.55 | +0.38 / +0.58 | both halves | 7e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.58 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TRAPPC4]] | -0.57 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[ZNF324]] | -0.57 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[CDKL5]] | -0.57 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PMM1]] | -0.57 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[YIF1A]] | -0.55 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[SLC10A3]] | -0.55 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[C6orf47]] | -0.55 | -0.14 / -0.64 | ⚠ one half (not replicated) | 0.002 |  |
| [[ZKSCAN1]] | -0.55 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[ING2]] | -0.55 | -0.26 / -0.63 | both halves | 4e-04 |  |
| [[MED19]] | -0.54 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[NAGK]] | -0.53 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ALG2]] | -0.52 | -0.28 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRTAP]] | C | CRTAP activity raises FUT10's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without CRTAP | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.9, -15.4); signed map (-15.3, -41.7). **Vector** length 97.7, 21.1% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +24.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +20.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.4 | +19.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.9 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +0.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +3.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.9 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | protein O-fucosyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:33,370,824-33,473,146 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously FUT10 |
| Gene groups (HGNC) | Fucosyltransferases |
| Reactome | 1 pathways, smallest: O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4F1](https://www.uniprot.org/uniprotkb/Q6P4F1) (GDP-fucose protein O-fucosyltransferase 3):

> Protein O-fucosyltransferase that specifically catalyzes O-fucosylation of serine or threonine residues in EMI domains of target proteins, such as MMRN1, MMRN2 and EMID1. Attaches fucose through an O-glycosidic linkage. O-fucosylation of EMI domain-containing proteins may be required for facilitating protein folding and secretion. May also show alpha-(1,3)-fucosyltransferase activity toward the innermost N-acetyl glucosamine (GlcNAc) residue in biantennary N-glycan acceptors. However, this was …

**Summary**, from NCBI Gene [84750](https://www.ncbi.nlm.nih.gov/gene/84750):

> Enables peptide-O-fucosyltransferase activity. Involved in N-glycan processing and positive regulation of protein secretion. Is active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19234) · Entrez [84750](https://www.ncbi.nlm.nih.gov/gene/84750) · UniProt [Q6P4F1](https://www.uniprot.org/uniprotkb/Q6P4F1) · Ensembl [ENSG00000172728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172728)

## Data

Gene col 10285: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10285); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10285, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10285]; `tensor/DDL_lfc|DDL_z.npy` [10285]; `embed/gene_vectors.npy` [10285]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10285 or target_col == 10285). Every well: [[FUT10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUT10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
