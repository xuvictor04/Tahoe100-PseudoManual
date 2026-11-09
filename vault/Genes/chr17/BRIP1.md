---
symbol: "BRIP1"
type: "gene"
col: 5871
ensembl_id: "ENSG00000136492"
name: "BRCA1 interacting DNA helicase 1"
location: "17q23.2"
module: 6
arm: "+"
pooled_cpm: 108.13
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 40
n_dd_up_clean: 12
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# BRIP1

*BRCA1 interacting DNA helicase 1* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.68× (z +7.0, q 1e-09, up in 38 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +6.0, q 3e-07, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (16 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.616× (z -6.5, q 4e-08, down in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.615× (z -6.1, q 4e-07, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLQ]] (+0.91, fdr 7e-06), [[WDHD1]] (+0.89, fdr 7e-06), [[ATAD5]] (+0.89, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.68×** | +7.0 | 1e-09 | 38/47 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.59×** | +6.3 | 1e-07 | 35/47 (A549, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.0 | 3e-07 | 26/47 (NCI-H1792, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.56×** | +5.8 | 1e-06 | 30/47 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.52×** | +5.7 | 1e-06 | 33/47 (RKO, SNU-423, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.46×** | +5.2 | 2e-05 | 30/47 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.44×** | +5.0 | 5e-05 | 32/47 (RKO, HT-29, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +4.7 | 2e-04 | 26/47 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.42×** | +4.6 | 3e-04 | 27/47 (SW480, HT-29, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.26×** | +4.5 | 4e-04 | 25/47 (A549, HT-29, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +4.4 | 6e-04 | 26/47 (LS 180, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +4.2 | 0.001 | 24/47 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.35×** | +4.1 | 0.002 | 22/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.007 | 23/47 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.011 | 21/47 (A-427, SW480, …) | two highest doses |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.011 | 19/47 (SW480, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.011 | 20/47 (LS 180, LoVo, …) | top dose only | plate-row cell shift |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.014 | 26/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.4 | 0.016 | 15/47 (SW480, HS-578T, …) | top dose only |  |
| [[Methotrexate (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.019 | 20/47 (LS 180, SW480, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.019 | 22/47 (SW480, A-427, …) | top dose only | plate-row cell shift |
| [[Busulfan (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.021 | 18/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.028 | 13/48 (BT-474, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.038 | 14/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.075 | 16/47 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.616×** | -6.5 | 4e-08 | 32/47 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.615×** | -6.1 | 4e-07 | 33/47 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -6.0 | 4e-07 | 31/47 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.653×** | -5.8 | 1e-06 | 30/47 (C-33 A, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.676×** | -5.3 | 1e-05 | 30/47 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.666×** | -5.3 | 1e-05 | 23/42 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.683×** | -5.2 | 2e-05 | 29/47 (CFPAC-1, LoVo, …) | two highest doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.594×** | -5.0 | 4e-05 | 33/47 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.775×** | -4.9 | 7e-05 | 33/47 (COLO 205, AN3 CA, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.776×** | -4.8 | 7e-05 | 26/47 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.779×** | -4.8 | 1e-04 | 26/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.705×** | -4.7 | 1e-04 | 24/46 (RKO, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.686×** | -4.7 | 1e-04 | 27/44 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -4.6 | 1e-04 | 28/47 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.717×** | -4.3 | 6e-04 | 26/46 (RKO, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -4.3 | 6e-04 | 25/47 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 5 µM |  | **0.548×** | -4.2 | 7e-04 | 25/47 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.819×** | -3.8 | 0.004 | 24/47 (HCT15, LoVo, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.749×** | -3.7 | 0.005 | 24/47 (HEC-1-A, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **0.825×** | -3.7 | 0.006 | 16/47 (HT-29, Hs 766T, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.600×** | -3.6 | 0.008 | 22/46 (A-172, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.767×** | -3.6 | 0.008 | 23/47 (AN3 CA, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.013 | 24/48 (A-172, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.09 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 151 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0725× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.231× (z -20.1) |
| [[HEC-1-A (line)]] | alt | 435 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.340× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 75.4 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.330× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 74.5 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.231× (z -14.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.368× (z -9.9) |
| [[PANC-1 (line)]] | alt | 73.4 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.5) | [[Harringtonine (drug)]] 0.5 µM 0.415× (z -8.8) |
| [[SW480 (line)]] | alt | 220 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.430× (z -9.4) |
| [[A549 (line)]] | wt | 71.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 35.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +20.0) | — |
| [[LoVo (line)]] | wt | 78.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +12.1) | [[Selinexor (drug)]] 5 µM 0.397× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 160 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.255× (z -11.6) |
| [[A-172 (line)]] | wt | 117 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.323× (z -10.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.192× (z -14.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 88.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -12.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[hTERT-HPNE (line)]] | wt | 47.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +20.6) | — |
| [[KATO III (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.473× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 89.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0555× (z -20.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 238 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.275× (z -12.5) |
| [[C32 (line)]] | wt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.0) | — |
| [[H4 (line)]] | wt | 121 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.229× (z -8.7) |
| [[HCT15 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 52.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.254× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 46.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +24.6) | — |
| [[NCI-H2030 (line)]] | alt | 55.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 94.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +15.5) | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.314× (z -9.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 83.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +16.2) | — |
| [[SW 1271 (line)]] | alt | 86.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.1000× (z -9.3) |
| [[SW1417 (line)]] | alt | 84.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.375× (z -8.5) |
| [[AN3 CA (line)]] | alt | 141 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 94.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 100 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLQ]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 655 |
| [[WDHD1]] | +0.89 | +0.86 / +0.91 | both halves | 7e-06 | STRING 717 |
| [[ATAD5]] | +0.89 | +0.86 / +0.92 | both halves | 7e-06 | STRING 554 |
| [[ZGRF1]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[DTL]] | +0.88 | +0.78 / +0.94 | both halves | 7e-06 | STRING 418 |
| [[ATAD2]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[MIR924HG]] | +0.87 | +0.82 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.87 | +0.80 / +0.91 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 897 |
| [[E2F8]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[DNA2]] | +0.87 | +0.83 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 882 |
| [[CHAF1A]] | +0.86 | +0.82 / +0.89 | both halves | 7e-06 |  |
| [[FANCD2]] | +0.86 | +0.91 / +0.84 | both halves | 7e-06 | same gene group; STRING 997 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises BRIP1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without TCF19 | 0.003 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises BRIP1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.22× lower at baseline in the lines without CDC25A | 0.023 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises BRIP1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without E2F2 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises BRIP1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.74× lower at baseline in the lines without MYBL1 | 0.055 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises BRIP1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without FAM111B | 0.056 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers BRIP1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity strengthens BRIP1's drug response | lines that do not express FAM111B (10) vs lines expressing it (37) | the lines without FAM111B respond 0.85× as strongly (z diff +0.24); rises at some drug-doses, falls at others (65% from rises): Bortezomib 0.05 µM: 0.82x vs 0.55x (z diff +2.5); Cytarabine 5 µM: 1.13x vs 1.58x (z diff +2.3); Cytarabine (hydrochloride) 0.5 µM: 1.34x vs 1.54x (z diff +1.3) | 0.079 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[MCM10]] | C | MCM10 activity raises BRIP1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.72× lower at baseline in the lines without MCM10 | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises BRIP1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without PBK | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises BRIP1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.71× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises BRIP1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.61× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises BRIP1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.46× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.876). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.1, -46.6); signed map (-40.1, -45.1). **Vector** length 166, 62.6% of its response variance represented; |z| ≥ 3 in 1,692 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.66 to 65); *DNA strand elongation* (reactome, mean cos +0.70 to 28); *DNA Replication* (reactome, mean cos +0.69 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +6.0 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +5.7 | +5.2 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +5.3 | +3.5 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.2 | +5.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +5.2 | +5.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +4.2 | +4.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.1 | +2.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +4.0 | +3.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +3.7 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -8.4 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -7.0 | -6.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -6.9 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.6 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -5.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.3 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.1 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | BRCA1 interacting DNA helicase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:61,679,139-61,863,559 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OF, BACH1, FANCJ |
| Gene groups (HGNC) | DEAH-box helicases; FA complementation groups; BRCA1 B complex |
| Reactome | 29 pathways, smallest: Cytosolic iron-sulfur cluster assembly; Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX63](https://www.uniprot.org/uniprotkb/Q9BX63) (Fanconi anemia group J protein):

> DNA-dependent ATPase and 5'-3' DNA helicase required for the maintenance of chromosomal stability. Acts late in the Fanconi anemia pathway, after FANCD2 ubiquitination. Involved in the repair of DNA double-strand breaks by homologous recombination in a manner that depends on its association with BRCA1. Involved in the repair of abasic sites at replication forks by promoting the degradation of DNA-protein cross-links: acts by catalyzing unfolding of HMCES DNA-protein cross-link via its helicase …

**Summary**, from NCBI Gene [83990](https://www.ncbi.nlm.nih.gov/gene/83990):

> The protein encoded by this gene is a member of the RecQ DEAH helicase family and interacts with the BRCT repeats of breast cancer, type 1 (BRCA1). The bound complex is important in the normal double-strand break repair function of breast cancer, type 1 (BRCA1). This gene may be a target of germline cancer-inducing mutations. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20473) · Entrez [83990](https://www.ncbi.nlm.nih.gov/gene/83990) · UniProt [Q9BX63](https://www.uniprot.org/uniprotkb/Q9BX63) · Ensembl [ENSG00000136492](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136492)

## Data

Gene col 5871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5871); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5871]; `tensor/DDL_lfc|DDL_z.npy` [5871]; `embed/gene_vectors.npy` [5871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5871 or target_col == 5871). Every well: [[BRIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
