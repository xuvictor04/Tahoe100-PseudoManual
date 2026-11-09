---
symbol: "KHDRBS1"
type: "gene"
col: 4295
ensembl_id: "ENSG00000121774"
name: "KH RNA binding domain containing, signal transduction associated 1"
location: "1p35.2"
module: 85
arm: "+"
pooled_cpm: 268.05
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# KHDRBS1

*KH RNA binding domain containing, signal transduction associated 1* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.96× (z +10.6, q 2e-23, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.53× (z +4.6, q 7e-04, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HOP62 4.51×, RPMI-7951 4.32×, Hs 766T 3.82×, PANC-1 2.44×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HOP62 3.83×, RPMI-7951 3.73×, Hs 766T 3.35×, COLO 205 3.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 2.48×, Hs 766T 2.60×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.772× (z -7.5, q 3e-11, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.63, fdr 2e-04), [[FAM13B]] (+0.62, fdr 1e-04), [[PTP4A2]] (+0.60, fdr 4e-05); moves opposite to [[PBDC1]] (-0.65, fdr 1e-05), [[ZNF564]] (-0.64, fdr 2e-04), [[RNF146]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[VIM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4295.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HOP62 4.51×, RPMI-7951 4.32×, Hs 766T 3.82×, PANC-1 2.44×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HOP62 3.83×, RPMI-7951 3.73×, Hs 766T 3.35×, COLO 205 3.78×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HOP62 2.48×, Hs 766T 2.60×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +10.6 | 2e-23 | 42/49 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +10.3 | 2e-22 | 39/44 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +7.8 | 1e-12 | 38/45 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.6 | 7e-04 | 34/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.26×** | +4.5 | 8e-04 | 25/47 (COLO 205, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.6 | 0.030 | 22/48 (AN3 CA, RKO, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.040 | 27/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.088 | 16/48 (SW48, LOX-IMVI, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.33× | +3.1 | 0.14 | 21/38 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.772×** | -7.5 | 3e-11 | 33/48 (HOP62, AN3 CA, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -6.7 | 7e-09 | 30/49 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.804×** | -6.3 | 5e-08 | 28/48 (AN3 CA, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.811×** | -6.1 | 2e-07 | 32/48 (NCI-H2347, C32, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.802×** | -4.5 | 6e-04 | 30/48 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -4.4 | 9e-04 | 32/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.811×** | -4.3 | 0.001 | 28/48 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.837× | -3.6 | 0.018 | 21/49 (A-172, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.795×** | -3.6 | 0.018 | 27/48 (CFPAC-1, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.840× | -3.6 | 0.018 | 23/48 (C-33 A, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 0.837× | -3.5 | 0.022 | 21/47 (PANC-1, C32, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.844× | -3.5 | 0.022 | 14/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.845× | -3.5 | 0.022 | 20/48 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 0.845× | -3.5 | 0.022 | 22/48 (hTERT-HPNE, SK-MEL-2, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 0.858× | -3.2 | 0.060 | 15/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.750×** | -3.1 | 0.071 | 21/49 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 316 | 5 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.44× (z +16.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.604× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 217 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.31× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | — |
| [[C-33 A (line)]] | alt | 372 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -16.9) |
| [[HOP62 (line)]] | alt | 304 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +24.7) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.605× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 252 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +15.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 281 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +17.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 456 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 205 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.602× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 254 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +19.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 317 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -14.5) |
| [[A498 (line)]] | wt | 204 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +14.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 403 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -20.3) |
| [[BT-474 (line)]] | alt | 219 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +11.7) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 292 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.26× (z +9.0) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.579× (z -8.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[CFPAC-1 (line)]] | alt | 301 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.98× (z +10.2) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.635× (z -9.7) |
| [[COLO 205 (line)]] | alt | 183 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.00× (z +12.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 227 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +9.2) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.599× (z -9.7) |
| [[LoVo (line)]] | wt | 219 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.98× (z +10.0) ⚠ toxic; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 294 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.640× (z -9.1) |
| [[SNU-1 (line)]] | wt | 350 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.1) |
| [[SW1417 (line)]] | alt | 209 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 305 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.614× (z -10.5) |
| [[A-172 (line)]] | wt | 188 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.90× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 239 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.95× (z +9.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 290 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.593× (z -8.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 220 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.93× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 219 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 166 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.10× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | — |
| [[NCI-H1792 (line)]] | alt | 253 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 269 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 312 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.595× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.646× (z -8.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[SW48 (line)]] | wt | 280 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 276 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 281 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 266 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 196 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 334 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 274 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 407 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 245 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.63 | +0.65 / +0.31 | both halves | 2e-04 |  |
| [[FAM13B]] | +0.62 | +0.69 / +0.33 | both halves | 1e-04 |  |
| [[PTP4A2]] | +0.60 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[GNAI2]] | +0.58 | +0.54 / +0.30 | both halves | 2e-04 |  |
| [[RALY]] | +0.57 | +0.48 / +0.49 | both halves | 2e-05 | STRING 754 |
| [[CNN2]] | +0.55 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[SEPTIN6]] | +0.52 | +0.46 / +0.24 | both halves | 4e-04 |  |
| [[PDZD7]] | +0.52 | +0.47 / +0.25 | both halves | 4e-04 |  |
| [[SBF2]] | +0.52 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[RSU1]] | +0.52 | +0.42 / +0.32 | both halves | 1e-04 |  |
| [[SNX1]] | +0.51 | +0.60 / +0.25 | both halves | 4e-04 |  |
| [[STAU1]] | +0.51 | +0.50 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBDC1]] | -0.65 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ZNF564]] | -0.64 | -0.68 / -0.29 | both halves | 2e-04 |  |
| [[RNF146]] | -0.61 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[FBXW4]] | -0.60 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[KCNRG]] | -0.58 | -0.62 / -0.29 | both halves | 3e-04 |  |
| [[MARVELD2]] | -0.58 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ZSCAN29]] | -0.56 | -0.60 / -0.37 | both halves | 7e-05 |  |
| [[FAIM]] | -0.56 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[RPP38]] | -0.56 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ARL14EP]] | -0.55 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[KICS2]] | -0.55 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[MIER3]] | -0.54 | -0.38 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VIM]] | B | VIM activity raises KHDRBS1's level | lines that do not express VIM (18) vs lines expressing it (32) | 1.12× lower at baseline in the lines without VIM | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LOXL2, ADAMTS18, MAP1B |
| [[CARD6]] | B | CARD6 activity lowers KHDRBS1's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.19× higher at baseline in the lines without CARD6 | 0.082 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-0.8, 6.1); signed map (-32.6, -0.7). **Vector** length 106, 35.8% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.8 | +0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | -0.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.0 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -7.9 | -6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | -7.7 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -7.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.7 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | KH RNA binding domain containing, signal transduction associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:32,013,868-32,060,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sam68, p62, FLJ34027 |
| Gene groups (HGNC) | Signal transduction and activation of RNA metabolism family |
| Reactome | 3 pathways, smallest: PTK6 Regulates Proteins Involved in RNA Processing; Signaling by Non-Receptor Tyrosine Kinases; Signaling by PTK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07666](https://www.uniprot.org/uniprotkb/Q07666) (KH domain-containing, RNA-binding, signal transduction-associated protein 1):

> Recruited and tyrosine phosphorylated by several receptor systems, for example the T-cell, leptin and insulin receptors. Once phosphorylated, functions as an adapter protein in signal transduction cascades by binding to SH2 and SH3 domain-containing proteins. Role in G2-M progression in the cell cycle. Represses CBP-dependent transcriptional activation apparently by competing with other nuclear factors for binding to CBP. Also acts as a putative regulator of mRNA stability and/or translation …

**Summary**, from NCBI Gene [10657](https://www.ncbi.nlm.nih.gov/gene/10657):

> This gene encodes a member of the K homology domain-containing, RNA-binding, signal transduction-associated protein family. The encoded protein appears to have many functions and may be involved in a variety of cellular processes, including alternative splicing, cell cycle regulation, RNA 3'-end formation, tumorigenesis, and regulation of human immunodeficiency virus gene expression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:18116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18116) · Entrez [10657](https://www.ncbi.nlm.nih.gov/gene/10657) · UniProt [Q07666](https://www.uniprot.org/uniprotkb/Q07666) · Ensembl [ENSG00000121774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121774)

## Data

Gene col 4295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4295); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4295]; `tensor/DDL_lfc|DDL_z.npy` [4295]; `embed/gene_vectors.npy` [4295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4295 or target_col == 4295). Every well: [[KHDRBS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KHDRBS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
