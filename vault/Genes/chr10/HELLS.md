---
symbol: "HELLS"
type: "gene"
col: 4145
ensembl_id: "ENSG00000119969"
name: "helicase, lymphoid specific"
location: "10q23.33"
module: 6
arm: "+"
pooled_cpm: 95.25
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 27
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# HELLS

*helicase, lymphoid specific* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (30 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.94× (z +21.5, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +11.7, q 1e-29, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.685× (z -5.6, q 8e-06, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.781× (z -5.5, q 8e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM4]] (+0.91, fdr 7e-06), [[MYBL2]] (+0.88, fdr 7e-06), [[TYMS]] (+0.87, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 32 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 30 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **3.94×** | +21.5 | 0e+00 | 46/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **4.00×** | +20.9 | 0e+00 | 43/44 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **3.35×** | +17.5 | 0e+00 | 43/45 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.55×** | +14.7 | 0e+00 | 45/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.25×** | +12.7 | 6e-35 | 44/48 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **2.22×** | +12.1 | 2e-31 | 41/48 (HOP62, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +11.7 | 1e-29 | 34/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.66×** | +11.2 | 2e-27 | 36/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.04×** | +11.2 | 3e-27 | 41/48 (J82, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **2.05×** | +10.8 | 2e-25 | 41/50 (SW 900, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.90×** | +10.1 | 4e-22 | 43/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.72×** | +8.5 | 7e-16 | 38/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.65×** | +7.8 | 2e-13 | 36/48 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.64×** | +7.8 | 3e-13 | 38/48 (SHP-77, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.63×** | +7.4 | 6e-12 | 34/48 (J82, A498, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.3 | 9e-09 | 26/48 (J82, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +4.5 | 1e-04 | 21/49 (AsPC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.002 | 22/48 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.006 | 20/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.006 | 17/47 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.006 | 15/48 (J82, SW480, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.018 | 14/48 (hTERT-HPNE, SW 1088, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.036 | 18/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.037 | 11/48 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.037 | 18/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.048 | 13/48 (SW480, A-427, …) | top dose only | plate-row cell shift |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.048 | 11/48 (J82, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.20× | +2.8 | 0.065 | 10/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | 1.19× | +2.7 | 0.080 | 8/48 (SW480, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.685×** | -5.6 | 8e-06 | 28/48 (LS 180, A-427, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.781×** | -5.5 | 8e-06 | 27/48 (HCT15, RKO, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.783×** | -5.5 | 8e-06 | 28/48 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.787×** | -5.4 | 1e-05 | 31/48 (RKO, SW480, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.700×** | -5.3 | 1e-05 | 32/48 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.728×** | -5.0 | 5e-05 | 28/48 (Panc 03.27, HepG2/C3A, …) | two highest doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.636×** | -4.9 | 9e-05 | 24/48 (SW480, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.736×** | -4.9 | 9e-05 | 29/48 (RKO, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.761×** | -4.3 | 1e-03 | 24/48 (HCT15, HT-29, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.834× | -4.1 | 0.003 | 21/49 (NCI-H23, HOP62, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.775×** | -4.0 | 0.003 | 21/47 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **0.774×** | -3.9 | 0.004 | 22/47 (AsPC-1, RKO, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.568×** | -3.9 | 0.004 | 19/48 (A-172, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.576×** | -3.8 | 0.005 | 17/48 (SHP-77, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.704×** | -3.8 | 0.006 | 20/48 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.587×** | -3.7 | 0.008 | 21/47 (A-427, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.010 | 22/48 (SK-MEL-2, C-33 A, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.800×** | -3.6 | 0.011 | 18/48 (CHP-212, SW 900, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.719×** | -3.5 | 0.011 | 22/48 (SW480, A498, …) | two highest doses | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.799×** | -3.4 | 0.019 | 17/48 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.45 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 126 | 13 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +20.6) | — |
| [[A-427 (line)]] | wt | 200 | 2 (2 ⚠) | 7 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -19.3) |
| [[A498 (line)]] | wt | 92.4 | 6 (5 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.9) | [[Selinexor (drug)]] 5 µM 0.483× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 67.1 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.26× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.5) | — |
| [[A549 (line)]] | wt | 72.7 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.44× (z +14.0) | — |
| [[C32 (line)]] | wt | 48.2 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +13.2) | — |
| [[CFPAC-1 (line)]] | alt | 54.2 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 29.9 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.8× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.20× (z +11.9) | — |
| [[LoVo (line)]] | wt | 55.3 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.81× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[LS 180 (line)]] | wt | 83.9 | 3 (3 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.251× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.378× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 45.2 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +15.4) | — |
| [[SNU-423 (line)]] | alt | 65.4 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.56× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.93× (z +11.2) | — |
| [[SW480 (line)]] | alt | 141 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[A-172 (line)]] | wt | 89.3 | 4 (4 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.402× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 32.9 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 151 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[HOP62 (line)]] | alt | 73.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[HT-29 (line)]] | alt | 69.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 72.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.49× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 84.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.85× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H2347 (line)]] | alt | 42.6 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 79.5 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[H4 (line)]] | wt | 59.9 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.300× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 73.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 73.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.35× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 83.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H1573 (line)]] | alt | 45.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.76× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H2030 (line)]] | alt | 55.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[RPMI-7951 (line)]] | alt | 45.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.78× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[SW1417 (line)]] | alt | 92.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 240 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[HepG2_C3A (line)]] | wt | 45.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.1) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[KATO III (line)]] | alt | 86.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[SHP-77 (line)]] | alt | 217 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.9) | — |
| [[SW48 (line)]] | wt | 134 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[HCT15 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H23 (line)]] | alt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -9.5) |
| [[RKO (line)]] | wt | 137 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[SNU-1 (line)]] | wt | 85.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[SW 1271 (line)]] | alt | 69.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0763× (z -8.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 213 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 285 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM4]] | +0.91 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 711 |
| [[MYBL2]] | +0.88 | +0.84 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[TYMS]] | +0.87 | +0.85 / +0.83 | both halves | 7e-06 | STRING 552 |
| [[MCM3]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 728 |
| [[WDR76]] | +0.86 | +0.82 / +0.88 | both halves | 7e-06 | STRING 972 |
| [[CLSPN]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | STRING 558 |
| [[TIMELESS]] | +0.85 | +0.77 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 429 |
| [[RAD51AP1]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 555 |
| [[PCLAF]] | +0.84 | +0.80 / +0.86 | both halves | 7e-06 | STRING 572 |
| [[XRCC2]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 |  |
| [[E2F8]] | +0.84 | +0.85 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 536 |
| [[CENPH]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | STRING 415 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises HELLS's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without E2F2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises HELLS's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 5.3% of all compounds | 0.026 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises HELLS's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.04× lower at baseline in the lines without CDC25A | 0.040 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises HELLS's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without E2F8 | 0.047 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HELLS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises HELLS's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.94× lower at baseline in the lines without TCF19 | 0.069 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises HELLS's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without TLCD3B | 0.081 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers HELLS's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MYBL2]] | C | MYBL2 activity raises HELLS's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.14× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[RB1]] | C | RB1 activity strengthens HELLS's drug response | recorded loss-of-function mutation of RB1 in 3 lines vs 46 not recorded | the RB1-altered lines respond 0.48× as strongly (z diff +1.67); strongest at Dinaciclib 0.05 µM: 0.94x vs 3.43x (z diff +9.1) | 0.131 over the table, 0.004 within its group | ⚠ within its group only (a lead); few lines (3 vs 46); tissue-confounded; across organs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.875). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.6, -43.9); signed map (-37.6, -47.0). **Vector** length 150, 62.5% of its response variance represented; |z| ≥ 3 in 1,859 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.70 to 28); *DNA Replication* (reactome, mean cos +0.68 to 40); *E2F G1/S* (control, mean cos +0.70 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +7.1 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +6.4 | +17.5 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | +6.2 | +5.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +5.9 | +21.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +4.4 | +3.0 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +4.0 | +3.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.9 | +2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.9 | +2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.8 | +2.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -9.8 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.6 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.9 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.3 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.0 | -0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.7 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | helicase, lymphoid specific |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:94,545,329-94,613,905 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PASG, SMARCA6, LSH, Nbla10143, SALNR |
| Gene groups (HGNC) | SNF2 related family; DexD/H helicases |
| Hallmark sets | E2F_TARGETS |
| Reactome | 3 pathways, smallest: TGFBR3 expression; Signaling by TGFBR3; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRZ9](https://www.uniprot.org/uniprotkb/Q9NRZ9) (Lymphoid-specific helicase):

> ATP-dependent chromatin remodeler that regulates chromatin accessibility, DNA methylation, and histone modifications. It facilitates de novo DNA methylation at repetitive sequences and promotes transcriptional silencing via recruitment of DNA methyltransferases (DNMTs) and histone deacetylases (HDACs), contributing to heterochromatin formation and repression of transposable elements. Also involved in DNA repair by recruiting DNA damage response mediators to double-strand breaks in …

**Summary**, from NCBI Gene [3070](https://www.ncbi.nlm.nih.gov/gene/3070):

> This gene encodes a lymphoid-specific helicase. Other helicases function in processes involving DNA strand separation, including replication, repair, recombination, and transcription. This protein is thought to be involved with cellular proliferation and may play a role in leukemogenesis. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:4861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4861) · Entrez [3070](https://www.ncbi.nlm.nih.gov/gene/3070) · UniProt [Q9NRZ9](https://www.uniprot.org/uniprotkb/Q9NRZ9) · Ensembl [ENSG00000119969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119969)

## Data

Gene col 4145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4145); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4145]; `tensor/DDL_lfc|DDL_z.npy` [4145]; `embed/gene_vectors.npy` [4145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4145 or target_col == 4145). Every well: [[HELLS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HELLS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
