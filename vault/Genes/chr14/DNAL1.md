---
symbol: "DNAL1"
type: "gene"
col: 4092
ensembl_id: "ENSG00000119661"
name: "dynein axonemal light chain 1"
location: "14q24.3"
module: 17
arm: "+"
pooled_cpm: 21.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DNAL1

*dynein axonemal light chain 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.98× (z +25.4, q 0e+00, up in 29 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.32× (z +20.3, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.796× (z -7.8, q 3e-12, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFT52]] (+0.70, fdr 7e-06), [[NPHP1]] (+0.65, fdr 2e-05), [[TMEM67]] (+0.63, fdr 1e-05); moves opposite to [[KLHL29]] (-0.55, fdr 1e-05), [[RPP25]] (-0.52, fdr 2e-04), [[PRKCE]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.98×** | +25.4 | 0e+00 | 29/33 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +20.3 | 0e+00 | 39/43 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +20.3 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +19.4 | 0e+00 | 44/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.34×** | +19.0 | 0e+00 | 30/37 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +17.7 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.53×** | +11.7 | 8e-30 | 32/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +10.5 | 6e-24 | 25/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +6.9 | 3e-10 | 23/48 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +6.4 | 6e-09 | 19/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +6.4 | 9e-09 | 20/47 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.30×** | +6.1 | 5e-08 | 16/43 (CFPAC-1, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.7 | 4e-07 | 16/48 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.18× | +5.7 | 5e-07 | 17/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +5.6 | 8e-07 | 18/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +4.9 | 3e-05 | 14/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +4.6 | 1e-04 | 14/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.001 | 14/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.3 | 0.026 | 9/47 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.046 | 2/48 (HEC-1-A, SK-MEL-2) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -7.8 | 3e-12 | 23/48 (NCI-H1792, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -6.7 | 4e-09 | 23/47 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.821×** | -4.8 | 4e-04 | 19/46 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.693×** | -4.6 | 5e-04 | 16/46 (SNU-423, SW48, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.1 | 0.004 | 19/47 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.790×** | -4.1 | 0.004 | 12/48 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.848× | -4.0 | 0.005 | 16/48 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.854× | -3.8 | 0.010 | 7/47 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.878× | -3.1 | 0.099 | 13/48 (J82, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.879× | -3.1 | 0.099 | 11/48 (H4, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.882× | -3.0 | 0.12 | 9/48 (LS 180, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.6) | — |
| [[PANC-1 (line)]] | alt | 15.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 39.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.17× (z +14.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.284× (z -13.0) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 22.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.46× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.11× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.99× (z +9.8) | — |
| [[LoVo (line)]] | wt | 17.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 22.6× (z +22.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 14.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.98× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 24.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 35.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.5× (z +19.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 35.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.29× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.8× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 2 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0825× (z -9.3) |
| [[HOP62 (line)]] | alt | 25.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +10.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +9.0) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -12.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.128× (z -10.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT52]] | +0.70 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[NPHP1]] | +0.65 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[TMEM67]] | +0.63 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[RTF2]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[NEK4]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[LMAN2L]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SUDS3]] | +0.59 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[IFT81]] | +0.58 | +0.39 / +0.65 | both halves | 6e-05 |  |
| [[TCTN2]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[IFT22]] | +0.56 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[VTI1B]] | +0.56 | +0.27 / +0.59 | both halves | 3e-04 |  |
| [[ASCC2]] | +0.56 | +0.46 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL29]] | -0.55 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[RPP25]] | -0.52 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[PRKCE]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[GATA2]] | -0.51 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[FZD7]] | -0.49 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[MSX1]] | -0.46 | -0.12 / -0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[PTGR3]] | -0.46 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[ZNF330]] | -0.45 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[TLNRD1]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[F12]] | -0.45 | -0.21 / -0.52 | both halves | 7e-04 |  |
| [[ORAI1]] | -0.45 | -0.26 / -0.60 | both halves | 4e-04 |  |
| [[FAM89A]] | -0.45 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[CDK5R1]] | -0.45 | -0.27 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.6, 0.5); signed map (-20.5, -18.5). **Vector** length 94.8, 20.5% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +20.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +19.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +25.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.7 | +1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.5 | -7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -5.8 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal light chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,644,875-73,703,732 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC12435, 1700010H15RiK, CILD16; previously C14orf168 |
| Gene groups (HGNC) | Dyneins, axonemal outer arm complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4LDG9](https://www.uniprot.org/uniprotkb/Q4LDG9) (Dynein axonemal light chain 1):

> Part of the multisubunit axonemal ATPase complexes that generate the force for cilia motility and govern beat frequency (By similarity). Component of the outer arm dynein (ODA). May be involved in a mechanosensory feedback mechanism controlling ODA activity based on external conformational cues by tethering the outer arm dynein heavy chain (DNAH5) to the microtubule within the axoneme (By similarity). Important for ciliary function in the airways and for the function of the cilia that produce …

**Summary**, from NCBI Gene [83544](https://www.ncbi.nlm.nih.gov/gene/83544):

> This gene encodes an axonemal dynein light chain which functions as a component of the outer dynein arms complex. This complex acts as the molecular motor that provides the force to move cilia in an ATP-dependent manner. The encoded protein is expressed in tissues with motile cilia or flagella and may be involved in the movement of sperm flagella. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:23247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23247) · Entrez [83544](https://www.ncbi.nlm.nih.gov/gene/83544) · UniProt [Q4LDG9](https://www.uniprot.org/uniprotkb/Q4LDG9) · Ensembl [ENSG00000119661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119661)

## Data

Gene col 4092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4092); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4092]; `tensor/DDL_lfc|DDL_z.npy` [4092]; `embed/gene_vectors.npy` [4092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4092 or target_col == 4092). Every well: [[DNAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
