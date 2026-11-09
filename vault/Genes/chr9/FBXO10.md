---
symbol: "FBXO10"
type: "gene"
col: 7234
ensembl_id: "ENSG00000147912"
name: "F-box protein 10"
location: "9p13.2"
module: 38
arm: "+"
pooled_cpm: 22.28
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# FBXO10

*F-box protein 10* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.69× (z +13.2, q 6e-37, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.594× (z -7.0, q 2e-09, down in 28 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.535× (z -4.4, q 0.002, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.110×, KATO III 0.109×, PANC-1 0.243×, SW480 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 0.288×, SW480 0.318×, LoVo 0.334×, NCI-H23 0.259×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.0492×, SHP-77 0.175×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW48 0.0933×); [[Silodosin (drug)]] 0.05 µM in 1 line (C32 0.0696×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.287×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKL1]] (+0.76, fdr 7e-06), [[UBE2CP5]] (+0.72, fdr 7e-06), [[DPH5-DT]] (+0.70, fdr 7e-06); moves opposite to [[ALAD]] (-0.61, fdr 2e-04), [[MDH1]] (-0.61, fdr 4e-05), [[TMEM106C]] (-0.60, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SNHG26]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.69×** | +13.2 | 6e-37 | 39/47 (SW480, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +11.4 | 7e-28 | 34/46 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.5 | 1e-11 | 29/45 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.40×** | +6.3 | 3e-08 | 23/47 (SK-MEL-2, SW1417, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +6.2 | 6e-08 | 26/43 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +5.0 | 4e-05 | 22/47 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 9e-04 | 19/46 (SK-MEL-2, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.43×** | +4.2 | 0.002 | 19/47 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +4.0 | 0.003 | 18/45 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.004 | 21/45 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.013 | 16/46 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.015 | 8/46 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.022 | 19/47 (SK-MEL-2, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.3 | 0.038 | 9/26 (SW480, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +3.1 | 0.071 | 15/46 (NCI-H2347, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7234.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.110×, KATO III 0.109×, PANC-1 0.243×, SW480 0.337×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 0.288×, SW480 0.318×, LoVo 0.334×, NCI-H23 0.259×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (LoVo 0.0492×, SHP-77 0.175×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW48 0.0933×); [[Silodosin (drug)]] 0.05 µM in 1 line (C32 0.0696×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.287×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.594×** | -7.0 | 2e-09 | 28/41 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.638×** | -5.8 | 2e-06 | 18/30 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.670×** | -4.9 | 1e-04 | 22/37 (LoVo, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.535×** | -4.4 | 0.002 | 19/47 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.647× | -3.0 | 0.25 | 11/44 (RKO, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.799× | -3.0 | 0.25 | 5/47 (LoVo, H4, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 51.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0492× (z -27.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 52.3 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.57× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -15.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.8 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.73× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -11.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 48.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.287× (z -9.0) |
| [[SW48 (line)]] | wt | 26.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0933× (z -10.2) |
| [[HOP62 (line)]] | alt | 16.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +10.9) | — |
| [[J82 (line)]] | alt | 21.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 43.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.22× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 14.2 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.07× (z +8.9) | — |
| [[A-172 (line)]] | wt | 14.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.70× (z +9.4) | — |
| [[A-427 (line)]] | wt | 9.01 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.150× (z -8.5) ⚠ toxic |
| [[C-33 A (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 7.83 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0696× (z -9.9) |
| [[H4 (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -8.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.00× (z +9.0) | — |
| [[RKO (line)]] | wt | 30.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -9.0) ⚠ cell-cycle shift, explains ~9% of this change |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -9.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -10.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0817× (z -14.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 15.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.39× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL1]] | +0.76 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[UBE2CP5]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[DPH5-DT]] | +0.70 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[TAS2R4]] | +0.70 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[APRG1]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MSH4]] | +0.66 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MIRLET7IHG]] | +0.65 | +0.76 / +0.42 | both halves | 4e-05 |  |
| [[PLAC8L1]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[KCNJ14]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[IDI2-AS1]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[C1S]] | +0.64 | +0.67 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.61 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[MDH1]] | -0.61 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[TMEM106C]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[AKTIP]] | -0.60 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[CLSTN1]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[HLTF]] | -0.58 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[MPP1]] | -0.58 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ADD3]] | -0.57 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[CAT]] | -0.57 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[MYH10]] | -0.55 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[LANCL1]] | -0.55 | -0.50 / -0.49 | both halves | 2e-05 |  |
| [[FAM234A]] | -0.55 | -0.33 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG26]] | B | SNHG26 activity raises FBXO10's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without SNHG26 | 0.041 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |
| [[SLC16A1-AS1]] | B | SLC16A1-AS1 activity raises FBXO10's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without SLC16A1-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.9, -20.1); signed map (10.6, 8.2). **Vector** length 97.4, 21.3% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.5 | +13.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +11.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +0.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,510,892-37,576,380 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX10 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK96](https://www.uniprot.org/uniprotkb/Q9UK96) (F-box only protein 10):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Mediates the ubiquitination and degradation of BCL2, an antiapoptotic protein, thereby playing a role in apoptosis by controlling the stability of BCL2. Targets also the receptor for advanced glycation end products RAGE for ubiquitination and subsequent lysosomal degradation. Directly controls HGAL/GCSAM ubiquitination and degradation and thereby decreases BCR signaling.

**Summary**, from NCBI Gene [26267](https://www.ncbi.nlm.nih.gov/gene/26267):

> Members of the F-box protein family, such as FBXO10, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:13589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13589) · Entrez [26267](https://www.ncbi.nlm.nih.gov/gene/26267) · UniProt [Q9UK96](https://www.uniprot.org/uniprotkb/Q9UK96) · Ensembl [ENSG00000147912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147912)

## Data

Gene col 7234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7234); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7234]; `tensor/DDL_lfc|DDL_z.npy` [7234]; `embed/gene_vectors.npy` [7234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7234 or target_col == 7234). Every well: [[FBXO10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
