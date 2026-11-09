---
symbol: "NDUFAF6"
type: "gene"
col: 7954
ensembl_id: "ENSG00000156170"
name: "NADH:ubiquinone oxidoreductase complex assembly factor 6"
location: "8q22.1"
module: 15
arm: "+"
pooled_cpm: 73.08
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# NDUFAF6

*NADH:ubiquinone oxidoreductase complex assembly factor 6* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.72× (z +29.8, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.718× (z -7.1, q 5e-10, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB44]] (+0.62, fdr 2e-05), [[NAF1]] (+0.61, fdr 3e-05), [[PCMTD1]] (+0.61, fdr 6e-05); moves opposite to [[ALAS1]] (-0.64, fdr 3e-05), [[AFF4]] (-0.56, fdr 3e-05), [[FLNC]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +29.8 | 0e+00 | 48/49 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +15.8 | 0e+00 | 44/47 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +11.3 | 3e-27 | 37/50 (RKO, H4, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +10.5 | 1e-23 | 38/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.57×** | +9.8 | 1e-20 | 39/48 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.57×** | +9.7 | 2e-20 | 40/48 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +9.4 | 6e-19 | 38/48 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.41×** | +7.4 | 8e-12 | 30/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.41×** | +7.2 | 4e-11 | 34/47 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +7.1 | 6e-11 | 27/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.33×** | +6.2 | 2e-08 | 27/48 (A498, C32, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.75×** | +5.8 | 3e-07 | 31/49 (J82, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 7e-07 | 23/48 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.20× | +5.5 | 2e-06 | 23/48 (A498, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +5.3 | 3e-06 | 23/48 (HS-578T, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +5.1 | 1e-05 | 22/48 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.5 | 2e-04 | 21/48 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.20×** | +4.0 | 0.002 | 16/48 (SHP-77, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.002 | 17/50 (SHP-77, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.13× | +3.7 | 0.005 | 12/49 (RPMI-7951, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7954.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -7.1 | 5e-10 | 28/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.677×** | -7.0 | 5e-10 | 37/48 (HT-29, KATO III, …) | all doses, flat |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.577×** | -5.7 | 2e-06 | 29/46 (NCI-H1792, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.781×** | -5.3 | 2e-05 | 25/48 (SW1417, HT-29, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.791×** | -5.1 | 5e-05 | 23/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.619×** | -5.0 | 6e-05 | 21/47 (J82, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.759×** | -5.0 | 6e-05 | 25/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.625×** | -4.9 | 8e-05 | 22/48 (KATO III, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **0.802×** | -4.7 | 1e-04 | 23/47 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.804×** | -4.7 | 2e-04 | 24/49 (J82, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.743×** | -4.6 | 3e-04 | 20/48 (SW480, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.664×** | -4.2 | 0.001 | 21/48 (KATO III, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.666×** | -4.2 | 0.001 | 20/48 (HT-29, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.817×** | -4.2 | 0.001 | 20/44 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.678×** | -4.0 | 0.002 | 17/48 (KATO III, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.844× | -3.6 | 0.010 | 12/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.807×** | -3.3 | 0.032 | 17/49 (HT-29, A498, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.865× | -3.1 | 0.055 | 15/47 (SK-MEL-2, RKO, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 77.0 | 5 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +17.9) | [[Harringtonine (drug)]] 5 µM 0.281× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 61.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 48.4 | 4 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +13.5) | [[Harringtonine (drug)]] 0.5 µM 0.472× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 41.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +19.7) | — |
| [[PANC-1 (line)]] | alt | 66.7 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.1) | [[Harringtonine (drug)]] 5 µM 0.315× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.8) |
| [[RKO (line)]] | wt | 132 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +16.5) | — |
| [[SHP-77 (line)]] | alt | 218 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -19.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -10.4) |
| [[C32 (line)]] | wt | 68.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +17.7) | — |
| [[H4 (line)]] | wt | 57.5 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 81.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +13.8) | [[Harringtonine (drug)]] 5 µM 0.406× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 70.8 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +13.4) | [[Tucidinostat (drug)]] 5 µM 0.535× (z -8.5) |
| [[LoVo (line)]] | wt | 74.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +20.2) | — |
| [[AN3 CA (line)]] | alt | 60.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 72.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 76.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.402× (z -12.0) |
| [[HT-29 (line)]] | alt | 52.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +16.2) | — |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +12.5) | — |
| [[J82 (line)]] | alt | 205 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -15.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 61.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 52.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +21.3) | — |
| [[NCI-H2030 (line)]] | alt | 69.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 59.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -14.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 52.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 55.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 38.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +15.2) | — |
| [[SW1417 (line)]] | alt | 88.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +13.5) | — |
| [[SW480 (line)]] | alt | 90.8 | 1 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.405× (z -12.5) |
| [[A-427 (line)]] | wt | 59.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 35.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 77.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +14.1) | — |
| [[HCT15 (line)]] | alt | 90.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 58.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +17.1) | — |
| [[Hs 766T (line)]] | wt | 47.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 96.5 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 55.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 64.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +16.7) | — |
| [[SK-MEL-2 (line)]] | alt | 55.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +11.4) | — |
| [[SW48 (line)]] | wt | 73.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB44]] | +0.62 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[NAF1]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[PCMTD1]] | +0.61 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[LEMD3]] | +0.57 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[PAXBP1]] | +0.55 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[FAM185A]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[STARD7-AS1]] | +0.55 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[DPY19L2P3]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[H3-3A-DT]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[RBBP4]] | +0.53 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[SMPD4BP]] | +0.52 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[TAF5]] | +0.52 | +0.30 / +0.60 | both halves | 2e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAS1]] | -0.64 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[AFF4]] | -0.56 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[FLNC]] | -0.54 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CLTC]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ZKSCAN2]] | -0.51 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.51 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[OSGIN1]] | -0.51 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ULBP3]] | -0.50 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[RANBP6]] | -0.50 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[GDF11]] | -0.49 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[RPLP0P2]] | -0.49 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[CLCN3]] | -0.49 | -0.30 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NDUFAF6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-0.2, -42.3); signed map (5.8, -4.7). **Vector** length 112, 32.1% of its response variance represented; |z| ≥ 3 in 1,378 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +15.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +29.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | +6.4 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.8 | +6.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.3 | +5.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.4 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.9 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.3 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase complex assembly factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,895,533-95,116,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | lncREST, MGC40214; previously C8orf38 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q330K2](https://www.uniprot.org/uniprotkb/Q330K2) (NADH dehydrogenase):

> Involved in the assembly of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I) at early stages. May play a role in the biogenesis of complex I subunit MT-ND1.

**Summary**, from NCBI Gene [137682](https://www.ncbi.nlm.nih.gov/gene/137682):

> This gene encodes a protein that localizes to mitochondria and contains a predicted phytoene synthase domain. The encoded protein plays an important role in the assembly of complex I (NADH-ubiquinone oxidoreductase) of the mitochondrial respiratory chain through regulation of subunit ND1 biogenesis. Mutations in this gene are associated with complex I enzymatic deficiency. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:28625](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28625) · Entrez [137682](https://www.ncbi.nlm.nih.gov/gene/137682) · UniProt [Q330K2](https://www.uniprot.org/uniprotkb/Q330K2) · Ensembl [ENSG00000156170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156170)

## Data

Gene col 7954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7954); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7954]; `tensor/DDL_lfc|DDL_z.npy` [7954]; `embed/gene_vectors.npy` [7954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7954 or target_col == 7954). Every well: [[NDUFAF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
