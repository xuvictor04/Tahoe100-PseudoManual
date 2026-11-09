---
symbol: "DLEU2"
type: "gene"
col: 13803
ensembl_id: "ENSG00000231607"
name: "deleted in lymphocytic leukemia 2"
location: "13q14.2"
module: 91
arm: "+"
pooled_cpm: 197.79
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 25
n_dd_up_clean: 15
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# DLEU2

*deleted in lymphocytic leukemia 2* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.36× (z +34.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.672× (z -15.8, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUCKS1]] (+0.68, fdr 7e-06), [[CDK19]] (+0.68, fdr 7e-06), [[SNHG31]] (+0.63, fdr 1e-05); moves opposite to [[RABGGTB]] (-0.65, fdr 8e-06), [[CHCHD6]] (-0.60, fdr 1e-05), [[NLE1]] (-0.60, fdr 1e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +34.1 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +29.0 | 0e+00 | 46/49 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +20.2 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +20.0 | 0e+00 | 42/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +16.1 | 0e+00 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +15.2 | 0e+00 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +15.2 | 0e+00 | 40/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +14.1 | 4e-43 | 38/50 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +14.0 | 1e-42 | 41/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +11.0 | 4e-26 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +9.3 | 6e-19 | 30/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.24×** | +5.9 | 1e-07 | 30/49 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.23×** | +5.1 | 2e-05 | 24/50 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.44×** | +5.0 | 2e-05 | 22/50 (C32, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +4.6 | 2e-04 | 18/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +4.5 | 2e-04 | 17/48 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.9 | 0.003 | 12/48 (SW480, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.672×** | -15.8 | 0e+00 | 38/48 (A-172, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.632×** | -12.9 | 2e-35 | 38/49 (HCT15, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.702×** | -9.9 | 6e-21 | 39/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.694×** | -9.9 | 9e-21 | 30/44 (HCT15, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.721×** | -9.1 | 7e-18 | 37/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.734×** | -8.6 | 5e-16 | 33/48 (NCI-H1792, RPMI-7951, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.688×** | -8.6 | 5e-16 | 38/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.545×** | -8.3 | 7e-15 | 41/48 (KATO III, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.726×** | -8.0 | 1e-13 | 33/45 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.624×** | -6.4 | 7e-09 | 24/38 (HEC-1-A, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.803×** | -6.1 | 4e-08 | 27/48 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.650×** | -5.9 | 2e-07 | 31/47 (SW480, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.817×** | -5.7 | 7e-07 | 24/48 (HOP62, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.669×** | -5.5 | 2e-06 | 26/45 (SW48, HT-29, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.819×** | -5.4 | 3e-06 | 25/47 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.824×** | -5.2 | 6e-06 | 24/48 (SNU-423, NCI-H661, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.684×** | -5.2 | 7e-06 | 27/48 (KATO III, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.689×** | -5.1 | 1e-05 | 28/48 (KATO III, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.710×** | -4.7 | 9e-05 | 23/49 (RPMI-7951, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.712×** | -4.6 | 1e-04 | 24/48 (Hs 766T, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.856× | -4.3 | 4e-04 | 17/48 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -4.2 | 6e-04 | 24/48 (RPMI-7951, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.818×** | -4.0 | 0.002 | 17/48 (HT-29, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 214 | 13 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +13.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.380× (z -12.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.542× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 151 | 14 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +30.9) | [[Selinexor (drug)]] 5 µM 0.555× (z -12.4) |
| [[SW480 (line)]] | alt | 294 | 9 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -13.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 279 | 9 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +27.4) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -14.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 267 | 5 (1 ⚠) | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.580× (z -10.6) |
| [[PANC-1 (line)]] | alt | 122 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +32.3) | — |
| [[HOP62 (line)]] | alt | 211 | 8 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +19.7) | [[Selinexor (drug)]] 5 µM 0.526× (z -14.0) |
| [[A-172 (line)]] | wt | 159 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.4) | [[Selinexor (drug)]] 5 µM 0.371× (z -16.8) |
| [[BT-474 (line)]] | alt | 198 | 8 (1 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.14× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 545 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -19.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 369 | 2 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.382× (z -10.3) |
| [[LoVo (line)]] | wt | 189 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +26.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 123 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +27.0) | — |
| [[Panc 03.27 (line)]] | alt | 244 | 5 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +22.4) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.583× (z -10.0) |
| [[RKO (line)]] | wt | 191 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +20.6) | [[Selinexor (drug)]] 5 µM 0.540× (z -9.1) |
| [[SW1417 (line)]] | alt | 154 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +23.6) | — |
| [[COLO 205 (line)]] | alt | 575 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +22.5) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -14.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 175 | 6 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +18.1) | [[Selinexor (drug)]] 5 µM 0.588× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 179 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -18.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 230 | 5 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.559× (z -9.1) |
| [[A-427 (line)]] | wt | 166 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.7) | [[Selinexor (drug)]] 5 µM 0.441× (z -16.6) |
| [[Hs 766T (line)]] | wt | 208 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +16.9) | [[Selinexor (drug)]] 5 µM 0.579× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 139 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +15.9) | [[Selinexor (drug)]] 5 µM 0.438× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 95.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +26.4) | — |
| [[HCT15 (line)]] | alt | 330 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -23.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 114 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +18.6) | — |
| [[LS 180 (line)]] | wt | 181 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +17.9) | — |
| [[NCI-H1573 (line)]] | alt | 87.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +26.5) | — |
| [[RPMI-7951 (line)]] | alt | 287 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 172 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +18.5) | [[Selinexor (drug)]] 5 µM 0.578× (z -9.9) |
| [[SW 900 (line)]] | alt | 227 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.0) | — |
| [[A549 (line)]] | wt | 105 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.6) | [[Selinexor (drug)]] 5 µM 0.578× (z -9.3) |
| [[C-33 A (line)]] | alt | 145 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -13.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 126 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +17.1) | [[Selinexor (drug)]] 5 µM 0.439× (z -14.6) |
| [[H4 (line)]] | wt | 130 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 129 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +18.8) | — |
| [[NCI-H1792 (line)]] | alt | 86.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.450× (z -8.5) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 138 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.453× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 110 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.5) | [[Lonafarnib (drug)]] 5 µM 0.225× (z -8.8) ⚠ toxic |
| [[A498 (line)]] | wt | 207 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.1) | [[Selinexor (drug)]] 5 µM 0.507× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 192 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.1) | [[Selinexor (drug)]] 5 µM 0.506× (z -10.5) |
| [[SNU-1 (line)]] | wt | 256 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 261 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +24.1) | — |
| [[SW 1271 (line)]] | alt | 339 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +13.4) | — |
| [[CHP-212 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 196 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCKS1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CDK19]] | +0.68 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SNHG31]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[NUSAP1]] | +0.63 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.61 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[KIF24]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[RMI2]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ASH1L]] | +0.61 | +0.60 / +0.49 | both halves | 2e-05 |  |
| [[RMI1]] | +0.60 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ASF1B]] | +0.60 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SKA2]] | +0.60 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[UNK]] | +0.58 | +0.63 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGGTB]] | -0.65 | -0.58 / -0.60 | both halves | 8e-06 |  |
| [[CHCHD6]] | -0.60 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[NLE1]] | -0.60 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CCT2]] | -0.59 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[PEX5]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[PHB1]] | -0.58 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MLX]] | -0.57 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[DLAT]] | -0.57 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[MAPKAPK3]] | -0.57 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[WDR36]] | -0.57 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.56 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[EIF3M]] | -0.56 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DLEU2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.4, -52.7); signed map (-49.4, -48.3). **Vector** length 152, 54.5% of its response variance represented; |z| ≥ 3 in 1,706 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.51 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +11.3 | +20.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +11.2 | +20.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.1 | +15.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +9.7 | +16.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +14.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +15.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +3.6 |
|  | [[Binimetinib (drug)]] 0.05 µM | ⚠ position correction uncertain | +3.7 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Binimetinib (drug)]] 5 µM | ⚠ position correction uncertain | +3.3 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -15.1 | -15.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -9.8 | -9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -9.4 | -8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.4 | -9.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.2 | -8.6 |
|  | [[EX229 (drug)]] 5 µM |  | -6.8 | -8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.9 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.0 | -5.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.9 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | deleted in lymphocytic leukemia 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q14.2 — chr13:49,956,670-50,125,720 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LEU2, TRIM13OS, NCRNA00022, LINC00022, MIR15AHG; previously DLB2, BCMSUN, RFP2OS |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [8847](https://www.ncbi.nlm.nih.gov/gene/8847):

> This locus represents a microRNA host gene and also produces long alternatively spliced non-coding RNAs. This genome region was observed to be deleted or epigenetically suppressed in leukemia, and was implicated as a negative regulator of cell proliferation. However, an alternative transcript produced at this locus was also found to promote progression through the cell cycle via angiotensin I converting enzyme 2 and cyclin D1. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:13748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13748) · Entrez [8847](https://www.ncbi.nlm.nih.gov/gene/8847) · Ensembl [ENSG00000231607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231607)

## Data

Gene col 13803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13803); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13803]; `tensor/DDL_lfc|DDL_z.npy` [13803]; `embed/gene_vectors.npy` [13803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13803 or target_col == 13803). Every well: [[DLEU2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLEU2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
