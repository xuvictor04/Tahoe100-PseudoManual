---
symbol: "MCM4"
type: "gene"
col: 2491
ensembl_id: "ENSG00000104738"
name: "minichromosome maintenance complex component 4"
location: "8q11.21"
module: 6
arm: "+"
pooled_cpm: 47.23
n_lines_expressing: 48
n_dd_up: 30
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCM4

*minichromosome maintenance complex component 4* — 8q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.37× (z +18.1, q 0e+00, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.43× (z +6.2, q 3e-08, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.696× (z -6.3, q 1e-07, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~65% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.763× (z -4.7, q 3e-04, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM3]] (+0.93, fdr 7e-06), [[HELLS]] (+0.91, fdr 7e-06), [[MYBL2]] (+0.90, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 23 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **4.37×** | +18.1 | 0e+00 | 43/44 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **3.97×** | +16.2 | 0e+00 | 39/39 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **3.15×** | +13.0 | 3e-36 | 38/41 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.75×** | +9.7 | 5e-20 | 30/45 (A549, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.03×** | +8.6 | 7e-16 | 36/46 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.82×** | +7.3 | 2e-11 | 35/46 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~69% of this change | **1.83×** | +7.1 | 8e-11 | 35/45 (C32, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.75×** | +6.8 | 7e-10 | 34/46 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.75×** | +6.6 | 3e-09 | 35/46 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.73×** | +6.4 | 8e-09 | 31/45 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.2 | 3e-08 | 30/46 (HS-578T, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.66×** | +5.9 | 1e-07 | 30/46 (C32, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.61×** | +5.8 | 3e-07 | 30/44 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.57×** | +5.5 | 1e-06 | 30/46 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.51×** | +5.0 | 2e-05 | 27/45 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +4.5 | 2e-04 | 21/46 (C32, PANC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.004 | 19/46 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.028 | 20/45 (H4, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.029 | 16/46 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.066 | 17/46 (C32, A549, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.069 | 12/46 (A498, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2491.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.696×** | -6.3 | 1e-07 | 36/46 (RKO, KATO III, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.644×** | -5.4 | 2e-05 | 29/46 (A498, H4, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.558×** | -5.1 | 6e-05 | 28/46 (PANC-1, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.763×** | -4.7 | 3e-04 | 26/46 (HCT15, RKO, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.694×** | -4.3 | 0.002 | 23/46 (RKO, SHP-77, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.734×** | -3.8 | 0.013 | 22/45 (NCI-H2030, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.561×** | -3.7 | 0.016 | 18/45 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.745×** | -3.6 | 0.016 | 22/46 (COLO 205, CHP-212, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.813×** | -3.6 | 0.016 | 18/46 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.745×** | -3.6 | 0.016 | 20/45 (KATO III, HCT15, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.739×** | -3.6 | 0.017 | 22/45 (HOP62, A-427, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.755×** | -3.5 | 0.024 | 18/46 (RKO, PANC-1, …) | rises with dose | position effect removed |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **0.761×** | -3.2 | 0.051 | 12/45 (hTERT-HPNE, HOP62, …) | top dose only | plate-row cell shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.608×** | -3.2 | 0.053 | 16/45 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.774×** | -3.2 | 0.053 | 19/46 (HOP62, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -3.2 | 0.053 | 17/46 (HOP62, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.767×** | -3.1 | 0.053 | 17/45 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.838× | -3.1 | 0.053 | 17/46 (NCI-H2030, MIA PaCa-2, …) | all doses, flat |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.619×** | -3.1 | 0.054 | 16/46 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.707×** | -3.1 | 0.058 | 16/46 (MIA PaCa-2, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.628×** | -3.0 | 0.064 | 16/46 (LS 180, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.34 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 45.4 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[A498 (line)]] | wt | 81.9 | 2 (2 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Selinexor (drug)]] 5 µM 0.381× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 31.3 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.52× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[A549 (line)]] | wt | 21.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 51.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.78× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[SNU-423 (line)]] | alt | 26.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.25× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[SW480 (line)]] | alt | 88.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 37.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[HT-29 (line)]] | alt | 31.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.64× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[J82 (line)]] | alt | 107 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.24× (z +9.4) ⚠ cell-cycle shift, explains ~94% of this change | — |
| [[NCI-H460 (line)]] | wt | 24.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Selinexor (drug)]] 0.5 µM 0.234× (z -9.4) ⚠ cell-cycle shift, explains ~95% of this change |
| [[PANC-1 (line)]] | alt | 33.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[A-427 (line)]] | wt | 72.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -26.5) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 23.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.157× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 97.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.12× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[LoVo (line)]] | wt | 27.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.96× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[LS 180 (line)]] | wt | 46.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Selinexor (drug)]] 5 µM 0.233× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 80.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 33.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 25.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.00× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[SW1417 (line)]] | alt | 37.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.5) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[CFPAC-1 (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[Hs 766T (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[KATO III (line)]] | alt | 61.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[NCI-H2347 (line)]] | alt | 40.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.2) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.134× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[SHP-77 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[A-172 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.89 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 87.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[HELLS]] | +0.91 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 711 |
| [[MYBL2]] | +0.90 | +0.88 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 533 |
| [[MCM2]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[E2F1]] | +0.89 | +0.89 / +0.85 | both halves | 7e-06 | pathway: G1/S Transition; STRING 627 |
| [[CLSPN]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 971 |
| [[WDR76]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | STRING 611 |
| [[CDC45]] | +0.88 | +0.85 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[MCM10]] | +0.87 | +0.86 / +0.88 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 999 |
| [[FAM111B]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 896 |
| [[E2F2]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | pathway: Mitotic G1 phase and G1/S transition; STRING 508 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 8, C 7. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises MCM4's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.90× lower at baseline in the lines without TCF19 | 0.008 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises MCM4's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 3.07× lower at baseline in the lines without CDC25A | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises MCM4's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without MYBL1 | 0.019 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises MCM4's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without E2F2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MCM4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDCA7]] | B | CDCA7 activity raises MCM4's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without CDCA7 | 0.058 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[ZNF724]] | B | ZNF724 activity weakens MCM4's drug response | lines that do not express ZNF724 (8) vs lines expressing it (38) | the lines without ZNF724 respond 1.42× as strongly (z diff -1.41); strongest at Panobinostat 0.5 µM: 2.36x vs 1.71x (z diff -1.9) | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577; target measured in part of the lines; artifact flags |
| [[POGLUT3]] | B | POGLUT3 activity raises MCM4's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without POGLUT3 | 0.099 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[MCM10]] | C | MCM10 activity raises MCM4's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 3.01× lower at baseline in the lines without MCM10 | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[ZNF367]] | C | ZNF367 activity raises MCM4's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 3.06× lower at baseline in the lines without ZNF367 | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent; co-absent with the target |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises MCM4's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.73× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[PKMYT1]] | C | PKMYT1 activity raises MCM4's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.22× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.918). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.0, -44.3); signed map (-37.7, -46.3). **Vector** length 131, 49.0% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Homology Directed Repair* (reactome, mean cos +0.71 to 32); *Chromosome Maintenance* (reactome, mean cos +0.70 to 29); *HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA)* (reactome, mean cos +0.72 to 29).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +5.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +4.7 | +13.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.2 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | +3.2 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.3 | +2.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.2 | +2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +3.8 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.7 | +0.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -5.4 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -5.2 | -5.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -5.0 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.9 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.1 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance complex component 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.21 — chr8:47,960,185-47,978,160 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDC54, hCdc21, P1-Cdc21, MGC33310; previously CDC21 |
| Gene groups (HGNC) | MCM family; minichromosome maintenance 2-7 complex |
| Hallmark sets | MYC_TARGETS_V2, MTORC1_SIGNALING, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 17 pathways, smallest: Unwinding of DNA; Activation of the pre-replicative complex; DNA strand elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P33991](https://www.uniprot.org/uniprotkb/P33991) (DNA replication licensing factor MCM4):

> Acts as a component of the MCM2-7 complex (MCM complex) which is the replicative helicase essential for 'once per cell cycle' DNA replication initiation and elongation in eukaryotic cells. Core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built. The active ATPase sites in the MCM2-7 ring are formed through the interaction surfaces of two neighboring subunits such that a critical structure of a …

**Summary**, from NCBI Gene [4173](https://www.ncbi.nlm.nih.gov/gene/4173):

> The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication related proteins. The MCM complex consisting of this protein and MCM2, 6 and 7 proteins possesses DNA …

**Accessions** — [HGNC:6947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6947) · Entrez [4173](https://www.ncbi.nlm.nih.gov/gene/4173) · UniProt [P33991](https://www.uniprot.org/uniprotkb/P33991) · Ensembl [ENSG00000104738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104738)

## Data

Gene col 2491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2491); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2491]; `tensor/DDL_lfc|DDL_z.npy` [2491]; `embed/gene_vectors.npy` [2491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2491 or target_col == 2491). Every well: [[MCM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
