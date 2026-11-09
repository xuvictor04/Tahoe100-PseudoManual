---
symbol: "XNDC1N"
type: "gene"
col: 14874
ensembl_id: "ENSG00000254469"
name: "XRCC1 N-terminal domain containing 1, N-terminal like"
location: "11q13.4"
module: 71
arm: "+"
pooled_cpm: 26.99
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 27
n_dd_up_clean: 14
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# XNDC1N

*XRCC1 N-terminal domain containing 1, N-terminal like* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.34× (z +12.9, q 1e-35, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.314× (z -17.6, q 0e+00, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.298× (z -13.1, q 2e-36, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XNDC1N-ZNF705EP-ALG1L9P]] (+0.83, fdr 7e-06, ⚠ same locus), [[BRCA1]] (+0.75, fdr 7e-06), [[KNTC1]] (+0.72, fdr 7e-06), [[TYMS]] (+0.69, fdr 7e-06); moves opposite to [[CCDC112]] (-0.65, fdr 1e-05), [[SYP]] (-0.60, fdr 1e-04), [[PIGH]] (-0.58, fdr 3e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[XNDC1N-ZNF705EP-ALG1L9P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +12.9 | 1e-35 | 43/47 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +9.2 | 9e-18 | 42/47 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.6 | 8e-09 | 34/48 (SW1417, Panc 03.27, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.6 | 3e-06 | 33/48 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.4 | 7e-06 | 21/36 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.024 | 19/48 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.024 | 15/47 (A-172, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.037 | 18/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.041 | 14/48 (PANC-1, HOP62, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.044 | 14/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.044 | 13/48 (MIA PaCa-2, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.3 | 0.049 | 19/43 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.050 | 20/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.078 | 14/48 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.079 | 10/48 (SW1417, PANC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.091 | 11/48 (C32, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.314×** | -17.6 | 0e+00 | 42/47 (PANC-1, CFPAC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.298×** | -13.1 | 2e-36 | 46/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.330×** | -11.9 | 1e-30 | 40/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.361×** | -10.5 | 7e-24 | 41/47 (COLO 205, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.392×** | -10.1 | 6e-22 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.399×** | -9.9 | 4e-21 | 37/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.400×** | -9.9 | 4e-21 | 44/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.504×** | -7.4 | 1e-11 | 33/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.504×** | -6.6 | 2e-09 | 34/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.317×** | -6.5 | 5e-09 | 38/48 (KATO III, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.581×** | -5.6 | 9e-07 | 29/45 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.699×** | -5.5 | 2e-06 | 29/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.604×** | -5.4 | 2e-06 | 33/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.412×** | -5.0 | 2e-05 | 27/46 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -4.6 | 2e-04 | 28/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.626×** | -4.5 | 2e-04 | 31/48 (PANC-1, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -4.3 | 7e-04 | 31/48 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.473×** | -4.2 | 7e-04 | 30/48 (CFPAC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.667×** | -4.1 | 0.001 | 26/48 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.775×** | -3.9 | 0.003 | 23/48 (HEC-1-A, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.527×** | -3.6 | 0.008 | 22/46 (HEC-1-A, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.4 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -20.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -13.6) |
| [[SW480 (line)]] | alt | 47.4 | 2 | 6 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +11.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -17.8) |
| [[COLO 205 (line)]] | alt | 53.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -17.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0927× (z -17.0) |
| [[HT-29 (line)]] | alt | 36.4 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -13.5) |
| [[LoVo (line)]] | wt | 26.0 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0966× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 62.5 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.161× (z -14.1) |
| [[A-427 (line)]] | wt | 32.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -14.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.205× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 41.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.257× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 46.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -18.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -11.6) |
| [[KATO III (line)]] | alt | 55.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0306× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -11.8) |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.213× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -13.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.160× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 27.1 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -12.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -9.5) |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.122× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 40.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 73.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -10.1) |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -17.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -12.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -13.4) ⚠ toxic |
| [[C32 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -8.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0564× (z -9.4) |
| [[H4 (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0685× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0850× (z -9.4) |
| [[HS-578T (line)]] | alt | 14.0 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -11.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 16.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0767× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.11× (z +10.6) | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0809× (z -8.8) |
| [[A549 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.83 | +0.79 / +0.75 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[BRCA1]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[TYMS]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.68 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[UBL7-DT]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[C21orf58]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MCM5]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZNF876P]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[RMI2]] | +0.64 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PRIMPOL]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RBBP4]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CENPH]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC112]] | -0.65 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SYP]] | -0.60 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[PIGH]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PGBD1]] | -0.57 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[DOCK6]] | -0.56 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[MAP1S]] | -0.55 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[LRRC8E]] | -0.55 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TUBB2B]] | -0.55 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[ZNF555]] | -0.54 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[GGT7]] | -0.54 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[PCTP]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[POLM]] | -0.53 | -0.36 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers XNDC1N's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XNDC1N-ZNF705EP-ALG1L9P]] | C | XNDC1N's natural level strengthens XNDC1N-ZNF705EP-ALG1L9P's drug response | XNDC1N's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.47; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.2, -46.1); signed map (-40.8, -47.6). **Vector** length 92.6, 27.5% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +12.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.4 | +1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +2.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.3 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.1 | -17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.9 | -9.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.7 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -5.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | XRCC1 N-terminal domain containing 1, N-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:71,865,504-71,928,654 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q6ZNB5](https://www.uniprot.org/uniprotkb/Q6ZNB5) carries no function annotation.

**Summary**, from NCBI Gene [100133315](https://www.ncbi.nlm.nih.gov/gene/100133315):

> Predicted to enable damaged DNA binding activity. Predicted to be involved in single strand break repair. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:54661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54661) · Entrez [100133315](https://www.ncbi.nlm.nih.gov/gene/100133315) · UniProt [Q6ZNB5](https://www.uniprot.org/uniprotkb/Q6ZNB5) · Ensembl [ENSG00000254469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254469)

## Data

Gene col 14874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14874); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14874]; `tensor/DDL_lfc|DDL_z.npy` [14874]; `embed/gene_vectors.npy` [14874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14874 or target_col == 14874). Every well: [[XNDC1N — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XNDC1N.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
