---
symbol: "CEP78"
type: "gene"
col: 7237
ensembl_id: "ENSG00000148019"
name: "centrosomal protein 78"
location: "9q21.2"
module: 6
arm: "+"
pooled_cpm: 32.17
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CEP78

*centrosomal protein 78* — 9q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.83× (z +19.9, q 0e+00, up in 39 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.98× (z +6.8, q 5e-10, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 0.748× (z -5.6, q 2e-05, down in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.802× (z -4.2, q 0.003, down in 11 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.394×, NCI-H460 0.476×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (H4 0.148×; ⚠ cell-cycle shift, would explain all of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H661 0.0689×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (RKO 0.253×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMS22L]] (+0.82, fdr 7e-06), [[DSCC1]] (+0.81, fdr 7e-06), [[MELK]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 25 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.83×** | +19.9 | 0e+00 | 39/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.92×** | +16.7 | 0e+00 | 40/46 (HT-29, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.35×** | +16.3 | 0e+00 | 40/46 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **2.11×** | +14.2 | 8e-44 | 40/47 (HT-29, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **2.07×** | +13.9 | 8e-42 | 40/47 (A498, HT-29, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **2.10×** | +13.6 | 4e-40 | 32/38 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.81×** | +10.9 | 9e-26 | 39/46 (HT-29, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.72×** | +10.3 | 4e-23 | 35/47 (HT-29, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.61×** | +8.4 | 2e-15 | 29/42 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.46×** | +7.2 | 4e-11 | 27/46 (SW1417, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.45×** | +7.1 | 8e-11 | 30/46 (J82, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +6.8 | 5e-10 | 31/47 (A498, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.43×** | +6.6 | 2e-09 | 29/47 (SNU-423, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | **1.42×** | +6.4 | 7e-09 | 24/46 (C32, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~81% of this change | **1.38×** | +5.8 | 2e-07 | 25/44 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +4.8 | 4e-05 | 20/46 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 2e-04 | 17/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.003 | 15/47 (J82, LOX-IMVI, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.007 | 13/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.023 | 7/44 (RKO, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.027 | 9/46 (HS-578T, RKO, …) | all doses, stronger at high dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.036 | 9/47 (SW48, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.036 | 9/47 (NCI-H1792, RKO, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.1 | 0.036 | 7/47 (A549, LOX-IMVI, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.039 | 11/47 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.12× | +3.0 | 0.042 | 8/47 (NCI-H23, J82, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.045 | 11/47 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.33×** | +2.9 | 0.060 | 0/47 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 1.16× | +2.8 | 0.071 | 10/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7237.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.394×, NCI-H460 0.476×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (H4 0.148×; ⚠ cell-cycle shift, would explain all of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H661 0.0689×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (RKO 0.253×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.748×** | -5.6 | 2e-05 | 22/47 (SNU-1, A-172, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.691×** | -5.0 | 1e-04 | 17/47 (A-427, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.774×** | -4.9 | 2e-04 | 19/47 (LS 180, A-172, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.802×** | -4.2 | 0.003 | 11/46 (RKO, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.852× | -4.1 | 0.004 | 14/47 (SW480, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.801×** | -4.1 | 0.004 | 17/46 (HEC-1-A, COLO 205, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.887× | -3.1 | 0.15 | 8/47 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.847× | -3.1 | 0.15 | 6/47 (RKO, SW1417, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.84 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 26.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[A498 (line)]] | wt | 22.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[HT-29 (line)]] | alt | 19.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +13.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.23× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[PANC-1 (line)]] | alt | 25.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[A549 (line)]] | wt | 30.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 40.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.47× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H460 (line)]] | wt | 30.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 58.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[C32 (line)]] | wt | 24.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.148× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 86.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[KATO III (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[LOX-IMVI (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 28.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H23 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.82× (z +8.5) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0689× (z -9.9) |
| [[RKO (line)]] | wt | 39.6 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.253× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[SW1417 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMS22L]] | +0.82 | +0.80 / +0.79 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.81 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[MELK]] | +0.79 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[WDR76]] | +0.79 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.79 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[CLSPN]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[GINS1]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[CSE1L]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[CENPU]] | +0.77 | +0.75 / +0.75 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[RRM1]] | +0.77 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[EXO1]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[HAUS1]] | +0.77 | +0.76 / +0.68 | both halves | 7e-06 | pathway: AURKA Activation by TPX2; STRING 535 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises CEP78's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without E2F2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises CEP78's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without TCF19 | 0.016 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CEP78's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.70× lower at baseline in the lines without CDC25A | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[ANKRD44]] | B | ANKRD44 activity raises CEP78's level | lines that do not express ANKRD44 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without ANKRD44 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, TBC1D19, SSBP2; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CEP78's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without PBK | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises CEP78's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.67× lower at baseline in the lines without DSCC1 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises CEP78's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.41× lower at baseline in the lines without MCM10 | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises CEP78's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.86× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[MELK]] | C | MELK activity raises CEP78's level | lines that do not express MELK (3) vs lines expressing it (47) | 2.74× lower at baseline in the lines without MELK | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent |
| [[CDC45]], [[CENPM]], [[SKA3]] | C | CDC45, CENPM, SKA3 activity raises CEP78's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.67× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises CEP78's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.23× lower at baseline in the lines without CLSPN | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.827). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.3, -43.0); signed map (-34.8, -43.3). **Vector** length 99.0, 26.3% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.61 to 65); *DNA strand elongation* (reactome, mean cos +0.63 to 28); *DNA Replication* (reactome, mean cos +0.62 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +4.5 | +19.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +4.4 | +13.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +4.1 | +7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | +3.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +2.9 | +8.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +6.8 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.0 | +3.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.2 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +1.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -4.6 | -4.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 78 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.2 — chr9:78,236,062-78,279,690 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12643; previously C9orf81 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JTW2](https://www.uniprot.org/uniprotkb/Q5JTW2) (Centrosomal protein of 78 kDa):

> Centriole wall protein that localizes to mature centrioles and regulates centriole and cilia biogenesis. Involved in centrosome duplication: required for efficient PLK4 centrosomal localization and PLK4-induced overduplication of centrioles. Involved in cilium biogenesis and controls cilium length. Acts as a regulator of protein stability by preventing ubiquitination of centrosomal proteins, such as CCP110 and tektins. Associates with the EDVP complex, preventing ubiquitination and degradation …

**Summary**, from NCBI Gene [84131](https://www.ncbi.nlm.nih.gov/gene/84131):

> This gene encodes a centrosomal protein that is both required for the regulation of centrosome-related events during the cell cycle, and required for ciliogenesis. The encoded protein has an N-terminal leucine-rich repeat (LRR) domain with six consecutive LRR repeats, and a C-terminal coiled-coil domain. It interacts with the N-terminal catalytic domain of polo-like kinase 4 (PLK4) and colocalizes with PLK4 to the distal end of the centriole. Naturally occurring mutations in this gene cause …

**Accessions** — [HGNC:25740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25740) · Entrez [84131](https://www.ncbi.nlm.nih.gov/gene/84131) · UniProt [Q5JTW2](https://www.uniprot.org/uniprotkb/Q5JTW2) · Ensembl [ENSG00000148019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148019)

## Data

Gene col 7237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7237); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7237]; `tensor/DDL_lfc|DDL_z.npy` [7237]; `embed/gene_vectors.npy` [7237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7237 or target_col == 7237). Every well: [[CEP78 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP78.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
