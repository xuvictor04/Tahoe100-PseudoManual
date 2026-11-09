---
symbol: "TNPO1"
type: "gene"
col: 1368
ensembl_id: "ENSG00000083312"
name: "transportin 1"
location: "5q13.2"
module: 25
arm: "+"
pooled_cpm: 253.71
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# TNPO1

*transportin 1* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +19.7, q 0e+00, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.569×, SK-MEL-2 0.663×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.392×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.418×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.426×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCKAP1]] (+0.68, fdr 7e-06), [[VPS36]] (+0.64, fdr 1e-05), [[GSR]] (+0.62, fdr 1e-05); moves opposite to [[ZKSCAN5]] (-0.62, fdr 3e-05), [[ISG20L2]] (-0.61, fdr 2e-05), [[BLZF1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ENAH]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +19.7 | 0e+00 | 40/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.82×** | +15.7 | 0e+00 | 47/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +15.2 | 0e+00 | 38/49 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +14.0 | 4e-42 | 43/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +13.5 | 3e-39 | 37/44 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +13.3 | 3e-38 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +13.2 | 1e-37 | 42/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +12.6 | 8e-35 | 39/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +12.6 | 8e-35 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +12.4 | 1e-33 | 44/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +11.1 | 9e-27 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +10.7 | 8e-25 | 41/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +10.2 | 1e-22 | 39/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +9.3 | 5e-19 | 33/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.40×** | +9.0 | 1e-17 | 31/45 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +5.7 | 3e-07 | 18/48 (J82, A549, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +5.3 | 3e-06 | 14/49 (HT-29, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 1e-05 | 29/49 (LS 180, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +4.7 | 4e-05 | 21/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.7 | 0.004 | 14/48 (HepG2/C3A, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1368.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.569×, SK-MEL-2 0.663×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.392×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.418×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.426×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.858× | -4.4 | 0.006 | 14/48 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.873× | -3.9 | 0.018 | 14/48 (AsPC-1, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.874× | -3.9 | 0.018 | 13/49 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.876× | -3.8 | 0.018 | 13/48 (AN3 CA, RKO, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.873× | -3.8 | 0.018 | 12/49 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.885× | -3.5 | 0.039 | 7/48 (RPMI-7951, SNU-423, …) | two highest doses |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.921× | -3.4 | 0.062 | 0/49 | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.892× | -3.3 | 0.069 | 16/48 (A-427, SK-MEL-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.893× | -3.3 | 0.072 | 9/48 (SW 1088, HOP62, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.897× | -3.1 | 0.097 | 9/48 (Hs 766T, C-33 A, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 0.927× | -3.1 | 0.097 | 0/48 | top dose only |  |
| [[Ranolazine (drug)]] 0.05 µM |  | 0.899× | -3.1 | 0.10 | 9/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 223 | 15 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.58× (z +15.1) | — |
| [[NCI-H1792 (line)]] | alt | 191 | 14 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 292 | 14 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +14.5) | — |
| [[SW480 (line)]] | alt | 236 | 14 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +16.7) | — |
| [[A-172 (line)]] | wt | 225 | 9 (6 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.91× (z +10.5) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.91× (z +10.3) | — |
| [[A549 (line)]] | wt | 241 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +18.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 216 | 9 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.39× (z +11.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.2) | — |
| [[KATO III (line)]] | alt | 142 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 255 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +16.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 285 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 213 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +17.1) | — |
| [[LOX-IMVI (line)]] | wt | 303 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +15.0) | — |
| [[NCI-H460 (line)]] | wt | 428 | 6 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.96× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 180 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 160 | 6 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.17× (z +14.3) | — |
| [[NCI-H23 (line)]] | alt | 224 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.86× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 239 | 5 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.84× (z +14.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 3.12× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 137 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.3) | — |
| [[C32 (line)]] | wt | 193 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.8) | — |
| [[J82 (line)]] | alt | 237 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.68× (z +13.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.4) | — |
| [[A498 (line)]] | wt | 256 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +16.1) | — |
| [[COLO 205 (line)]] | alt | 99.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +13.4) | — |
| [[H4 (line)]] | wt | 223 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.05 µM 2.85× (z +9.9) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[HCT15 (line)]] | alt | 239 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.38× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 262 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 379 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.418× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 200 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 241 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 189 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.6) | — |
| [[C-33 A (line)]] | alt | 303 | 1 | 1 (1 ⚠) | [[5-Azacytidine (drug)]] 5 µM 1.95× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -13.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 266 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 161 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.04× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 379 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 420 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.426× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 193 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 389 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.81× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 237 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 253 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 359 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 397 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 320 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 355 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP1]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[VPS36]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[GSR]] | +0.62 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[TSEN15]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ENAH]] | +0.59 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[IDE]] | +0.59 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[FECH]] | +0.58 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[UBQLN1]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[RAD23B]] | +0.57 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[ME2]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NAE1]] | +0.57 | +0.57 / +0.49 | both halves | 2e-05 |  |
| [[MAPK9]] | +0.57 | +0.43 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN5]] | -0.62 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[ISG20L2]] | -0.61 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[BLZF1]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ZNF324]] | -0.56 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[TPRN]] | -0.56 | -0.28 / -0.56 | both halves | 3e-04 |  |
| [[DIABLO]] | -0.56 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[ZNF200]] | -0.56 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SUPT4H1]] | -0.56 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[LINS1]] | -0.54 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[SAP30BP]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[WBP1L]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CCNT1]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENAH]] | C | ENAH activity raises TNPO1's level | lines that do not express ENAH (3) vs lines expressing it (47) | 1.78× lower at baseline in the lines without ENAH | 0.011 | ⚠ few lines (3 vs 47); across organs; also absent: SSBP2, DIP2C, SOX12; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.9, -14.9); signed map (-11.6, -41.0). **Vector** length 101, 33.6% of its response variance represented; |z| ≥ 3 in 1,503 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +13.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.8 | +14.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +10.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.3 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.4 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.4 | -1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.4 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -0.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | transportin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:72,816,312-72,916,733 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIP, TRN, IPO2, MIP1; previously KPNB2 |
| Gene groups (HGNC) | Importins; Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Reactome | 14 pathways, smallest: Tristetraprolin (TTP, ZFP36) binds and destabilizes mRNA; Postmitotic nuclear pore complex (NPC) reformation; Intraflagellar transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92973](https://www.uniprot.org/uniprotkb/Q92973) (Transportin-1):

> Functions in nuclear protein import as nuclear transport receptor. Serves as receptor for nuclear localization signals (NLS) in cargo substrates. May mediate docking of the importin/substrate complex to the nuclear pore complex (NPC) through binding to nucleoporin and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to the importin, the importin/substrate complex dissociates and importin is …

**Summary**, from NCBI Gene [3842](https://www.ncbi.nlm.nih.gov/gene/3842):

> This gene encodes the beta subunit of the karyopherin receptor complex which interacts with nuclear localization signals to target nuclear proteins to the nucleus. The karyopherin receptor complex is a heterodimer of an alpha subunit which recognizes the nuclear localization signal and a beta subunit which docks the complex at nucleoporins. Alternate splicing of this gene results in several transcript variants encoding different proteins. [provided by RefSeq, Jun 2018]

**Accessions** — [HGNC:6401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6401) · Entrez [3842](https://www.ncbi.nlm.nih.gov/gene/3842) · UniProt [Q92973](https://www.uniprot.org/uniprotkb/Q92973) · Ensembl [ENSG00000083312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083312)

## Data

Gene col 1368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1368); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1368]; `tensor/DDL_lfc|DDL_z.npy` [1368]; `embed/gene_vectors.npy` [1368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1368 or target_col == 1368). Every well: [[TNPO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNPO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
