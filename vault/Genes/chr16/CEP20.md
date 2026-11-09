---
symbol: "CEP20"
type: "gene"
col: 5444
ensembl_id: "ENSG00000133393"
name: "centrosomal protein 20"
location: "16p13.11"
module: 25
arm: "+"
pooled_cpm: 31.86
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# CEP20

*centrosomal protein 20* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.12× (z +18.6, q 0e+00, up in 32 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.56× (z +11.5, q 2e-28, up in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A498 3.03×, NCI-H460 3.17×, A549 3.44×, NCI-H1792 4.14×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 4.69×, KATO III 3.77×, A498 2.88×, NCI-H460 2.97×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (HEC-1-A 2.52×, HT-29 2.73×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.768× (z -9.7, q 2e-19, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRRAP]] (+0.58, fdr 1e-04), [[SRP9]] (+0.57, fdr 2e-05), [[ZCCHC4]] (+0.56, fdr 1e-05); moves opposite to [[POLD4]] (-0.57, fdr 4e-05), [[USP43]] (-0.55, fdr 4e-05), [[IRF7]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5444.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (A498 3.03×, NCI-H460 3.17×, A549 3.44×, NCI-H1792 4.14×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 4.69×, KATO III 3.77×, A498 2.88×, NCI-H460 2.97×, …; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (HEC-1-A 2.52×, HT-29 2.73×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +18.6 | 0e+00 | 32/37 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +15.2 | 0e+00 | 33/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +11.5 | 2e-28 | 36/48 (HEC-1-A, HT-29, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +6.9 | 7e-10 | 24/41 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.30×** | +6.8 | 1e-09 | 22/46 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **1.28×** | +6.3 | 3e-08 | 19/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +5.7 | 8e-07 | 19/48 (HEC-1-A, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.9 | 9e-05 | 16/48 (A549, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.14× | +4.8 | 1e-04 | 6/48 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +4.1 | 0.002 | 8/46 (A498, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +3.9 | 0.005 | 16/48 (NCI-H23, A549, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.006 | 18/45 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.8 | 0.006 | 9/48 (HS-578T, J82, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.15× | +3.7 | 0.009 | 4/48 (RKO, NCI-H23, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.3 | 0.041 | 9/33 (HOP62, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.09× | +3.2 | 0.048 | 8/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.2 | 0.049 | 11/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.12× | +2.9 | 0.098 | 5/48 (A498, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.768×** | -9.7 | 2e-19 | 32/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.798×** | -8.3 | 4e-14 | 23/47 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.719×** | -8.2 | 5e-14 | 27/48 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.774×** | -6.6 | 5e-09 | 24/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.781×** | -6.4 | 2e-08 | 26/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.825×** | -5.0 | 6e-05 | 14/48 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.824×** | -4.8 | 1e-04 | 11/48 (hTERT-HPNE, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.836× | -4.6 | 3e-04 | 16/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.843× | -4.4 | 6e-04 | 11/48 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.722×** | -4.4 | 6e-04 | 15/47 (KATO III, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.4 | 6e-04 | 16/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.845× | -4.3 | 7e-04 | 12/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.891× | -4.2 | 1e-03 | 16/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -4.0 | 0.003 | 17/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.850× | -3.9 | 0.004 | 17/47 (NCI-H661, LOX-IMVI, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | 0.869× | -3.7 | 0.009 | 6/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.824×** | -3.6 | 0.012 | 9/48 (LS 180, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.875× | -3.5 | 0.017 | 9/48 (SW 1271, CFPAC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.792×** | -3.2 | 0.045 | 7/48 (NCI-H2030, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.919× | -3.1 | 0.053 | 11/48 (PANC-1, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.4 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.3) |
| [[PANC-1 (line)]] | alt | 73.9 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.19× (z +10.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.478× (z -10.8) |
| [[A498 (line)]] | wt | 39.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 24.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 33.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -16.0) ⚠ cell-cycle shift, explains ~96% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.446× (z -9.0) |
| [[SW480 (line)]] | alt | 40.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -8.7) |
| [[A-172 (line)]] | wt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 41.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.9) |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0894× (z -9.5) |
| [[HS-578T (line)]] | alt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 30.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.73× (z +8.7) | — |
| [[J82 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.9) |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.1) |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRRAP]] | +0.58 | +0.33 / +0.70 | both halves | 1e-04 |  |
| [[SRP9]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ZCCHC4]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PPWD1]] | +0.55 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[MBTPS2]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[KAT7]] | +0.54 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[UBE2V1]] | +0.53 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[CAPRIN1]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[DPY19L4]] | +0.53 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[MANEA]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ARL5A]] | +0.52 | +0.27 / +0.58 | both halves | 3e-04 |  |
| [[NUP155]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD4]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[USP43]] | -0.55 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[IRF7]] | -0.53 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[ABTB2]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[MARCHF9]] | -0.50 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[RNF19B]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ACHE]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[BIK]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NBPF14]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[ACAP1]] | -0.48 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[CDKL5]] | -0.48 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[TSC22D2]] | -0.47 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.9, 18.0); signed map (-16.1, -39.0). **Vector** length 93.0, 19.3% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +11.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.9 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.9 | +5.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -8.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.0 | -4.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,865,719-15,888,625 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686N1651, FLJ31153, PHSECRG2, FOR20; previously C16orf63, FOPNL |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NB1](https://www.uniprot.org/uniprotkb/Q96NB1) (Centrosomal protein 20):

> Involved in the biogenesis of cilia. Required for the recruitment of PLK1 to centrosomes and S phase progression.

**Summary**, from NCBI Gene [123811](https://www.ncbi.nlm.nih.gov/gene/123811):

> Enables identical protein binding activity. Involved in cilium assembly. Located in centriolar satellite. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26435) · Entrez [123811](https://www.ncbi.nlm.nih.gov/gene/123811) · UniProt [Q96NB1](https://www.uniprot.org/uniprotkb/Q96NB1) · Ensembl [ENSG00000133393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133393)

## Data

Gene col 5444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5444); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5444]; `tensor/DDL_lfc|DDL_z.npy` [5444]; `embed/gene_vectors.npy` [5444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5444 or target_col == 5444). Every well: [[CEP20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
