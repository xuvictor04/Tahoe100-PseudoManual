---
symbol: "COPB2-DT"
type: "gene"
col: 14580
ensembl_id: "ENSG00000248932"
name: "COPB2 divergent transcript"
location: "3q23"
module: 23
arm: "+"
pooled_cpm: 55.36
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 22
n_dd_up_clean: 17
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# COPB2-DT

*COPB2 divergent transcript* — 3q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.10× (z +14.3, q 7e-44, up in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +5.6, q 3e-06, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.342× (z -11.5, q 7e-28, down in 43 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.374× (z -10.5, q 2e-23, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGDH-AS1]] (+0.74, fdr 7e-06), [[DNAJC27-AS1]] (+0.71, fdr 7e-06), [[CYB5D2]] (+0.70, fdr 7e-06); moves opposite to [[PET117]] (-0.57, fdr 4e-04), [[LHX2]] (-0.55, fdr 3e-05), [[TFB1M]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.10×** | +14.3 | 7e-44 | 37/42 (RPMI-7951, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.6 | 3e-15 | 34/46 (RPMI-7951, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +5.7 | 2e-06 | 29/43 (RPMI-7951, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.6 | 3e-06 | 31/47 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.004 | 30/46 (C32, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.008 | 28/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.011 | 30/47 (A-172, HepG2/C3A, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.011 | 26/47 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.013 | 26/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.43×** | +3.6 | 0.016 | 24/49 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.034 | 24/47 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.042 | 16/47 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.042 | 19/47 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.78×** | +3.3 | 0.042 | 17/49 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.042 | 19/47 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.049 | 24/47 (SW48, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.069 | 17/47 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.069 | 20/47 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.069 | 22/47 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.342×** | -11.5 | 7e-28 | 43/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.374×** | -10.5 | 2e-23 | 42/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.380×** | -10.4 | 6e-23 | 43/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.414×** | -9.4 | 5e-19 | 42/47 (PANC-1, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.469×** | -8.1 | 6e-14 | 39/47 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.494×** | -7.1 | 9e-11 | 34/46 (LoVo, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.522×** | -7.0 | 3e-10 | 38/47 (KATO III, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.537×** | -6.7 | 2e-09 | 39/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.534×** | -6.3 | 1e-08 | 31/47 (hTERT-HPNE, A-427, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.569×** | -5.7 | 7e-07 | 31/47 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.616×** | -4.9 | 5e-05 | 27/45 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.448×** | -4.5 | 3e-04 | 30/44 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.681×** | -4.1 | 0.002 | 27/47 (A-427, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.484×** | -4.1 | 0.002 | 30/47 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.488×** | -4.0 | 0.002 | 27/47 (NCI-H1573, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.768×** | -4.0 | 0.003 | 25/48 (SW 1088, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.597×** | -3.9 | 0.003 | 32/47 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.697×** | -3.8 | 0.004 | 29/47 (BT-474, A-427, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.560×** | -3.2 | 0.032 | 21/47 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.817×** | -3.0 | 0.064 | 13/48 (PANC-1, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 52.1 | 2 (2 ⚠) | 9 (7 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.01× (z +13.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.168× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -14.4) |
| [[SW480 (line)]] | alt | 102 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -14.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -12.2) |
| [[A-427 (line)]] | wt | 94.2 | 0 | 7 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.343× (z -10.0) |
| [[COLO 205 (line)]] | alt | 145 | 0 | 7 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -13.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 72.8 | 1 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -16.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 51.0 | 0 | 6 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.241× (z -10.2) |
| [[KATO III (line)]] | alt | 119 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0678× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.214× (z -10.8) |
| [[LoVo (line)]] | wt | 64.2 | 2 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 80.4 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0620× (z -14.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.104× (z -11.7) |
| [[HOP62 (line)]] | alt | 62.3 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.29× (z +11.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.177× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 111 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.171× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 39.4 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.71× (z +13.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.197× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 15.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.38× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 45.0 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.33× (z +13.7) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -11.0) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -9.9) |
| [[A549 (line)]] | wt | 46.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.87× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 45.9 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.224× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 33.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.7× (z +14.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.7× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.158× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.60× (z +8.5) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.129× (z -10.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[J82 (line)]] | alt | 36.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.24× (z +12.4) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.246× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 28.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.87× (z +9.0) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.185× (z -10.1) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 46.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.51× (z +9.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.265× (z -8.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.16× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.8× (z +13.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -8.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[C-33 A (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.89× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 81.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.73× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.03× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0502× (z -8.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW1417 (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 41.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0874× (z -10.6) |
| [[A-172 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGDH-AS1]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[DNAJC27-AS1]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[CYB5D2]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[UFL1-AS1]] | +0.66 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[SDCBP2-AS1]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ENTPD3-AS1]] | +0.64 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[MSTO1]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ACYP2]] | +0.63 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SOX2-OT]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[EFCAB6]] | +0.63 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[CHD1-DT]] | +0.63 | +0.71 / +0.54 | both halves | 1e-05 | same gene group |
| [[HEXIM2-AS1]] | +0.63 | +0.69 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PET117]] | -0.57 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[LHX2]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TFB1M]] | -0.54 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[SLC25A4]] | -0.54 | -0.06 / -0.56 | ⚠ one half (not replicated) | 0.004 |  |
| [[MRPL17]] | -0.53 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[DCTPP1]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[GALNT12]] | -0.51 | -0.51 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers COPB2-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.6, 19.0); signed map (30.1, -7.8). **Vector** length 105, 36.8% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +14.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.6 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.6 | +3.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.9 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | +0.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.8 | -1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -7.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | COPB2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q23 — chr3:139,389,761-139,782,699 (+) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-319G6.1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100507291](https://www.ncbi.nlm.nih.gov/gene/100507291):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:55579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55579) · Entrez [100507291](https://www.ncbi.nlm.nih.gov/gene/100507291) · Ensembl [ENSG00000248932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248932)

## Data

Gene col 14580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14580); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14580]; `tensor/DDL_lfc|DDL_z.npy` [14580]; `embed/gene_vectors.npy` [14580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14580 or target_col == 14580). Every well: [[COPB2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPB2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
