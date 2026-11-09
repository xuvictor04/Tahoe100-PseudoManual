---
symbol: "MT-CO2"
type: "gene"
col: 12648
ensembl_id: "ENSG00000198712"
name: "mitochondrially encoded cytochrome c oxidase II"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 85.33
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-CO2

*mitochondrially encoded cytochrome c oxidase II* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.08× (z +15.1, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Berberine (chloride hydrate) (drug)]] 5 µM: 1.57× (z +7.1, q 2e-10, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.230× (z -16.7, q 0e+00, down in 47 of 47 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.368× (z -15.6, q 0e+00, down in 46 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12648.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +15.1 | 0e+00 | 47/48 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.40×** | +12.8 | 3e-35 | 45/45 (LOX-IMVI, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +11.6 | 8e-29 | 41/43 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **1.57×** | +7.1 | 2e-10 | 43/48 (SW48, CFPAC-1, …) | top dose only | position effect removed |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.47×** | +5.9 | 4e-07 | 31/48 (SW1417, SNU-423, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.58×** | +5.0 | 7e-05 | 34/49 (SK-MEL-2, LoVo, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.004 | 32/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.013 | 33/47 (A-427, AsPC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +3.7 | 0.015 | 30/49 (MIA PaCa-2, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.063 | 24/48 (KATO III, H4, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.068 | 25/48 (HCT15, KATO III, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.32× | +3.0 | 0.12 | 19/48 (NCI-H1792, C32, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12648.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.230×** | -16.7 | 0e+00 | 47/47 (SK-MEL-2, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.368×** | -15.6 | 0e+00 | 46/48 (A549, PANC-1, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.800×** | -8.8 | 3e-16 | 43/50 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.591×** | -8.1 | 5e-14 | 42/49 (NCI-H460, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -6.0 | 2e-07 | 34/48 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -5.0 | 4e-05 | 30/48 (AN3 CA, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.635×** | -4.9 | 7e-05 | 45/47 (PANC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -4.5 | 6e-04 | 30/48 (RKO, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.685×** | -4.3 | 1e-03 | 28/48 (Hs 766T, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.729×** | -3.4 | 0.037 | 21/48 (SW 1271, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.737×** | -3.4 | 0.039 | 21/48 (LS 180, SW480, …) | rises with dose | composition shift |
| [[Pentamidine (isethionate) (drug)]] 0.5 µM |  | **0.748×** | -3.3 | 0.042 | 22/49 (A549, PANC-1, …) | rises with dose | position effect removed |
| [[Captopril (drug)]] 5 µM |  | **0.757×** | -3.2 | 0.063 | 19/48 (A498, A549, …) | top dose only | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -3.0 | 0.095 | 21/48 (SW 900, COLO 205, …) | rises with dose | position effect removed |
| [[Ciclopirox (drug)]] 5 µM |  | **0.822×** | -3.0 | 0.095 | 21/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | **0.818×** | -3.0 | 0.095 | 15/49 (NCI-H1792, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 101 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +12.2) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.164× (z -20.3) |
| [[HOP62 (line)]] | alt | 51.8 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 5 µM 2.84× (z +9.4) | [[Pentamidine (isethionate) (drug)]] 5 µM 0.227× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 96.4 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +12.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.178× (z -19.7) |
| [[PANC-1 (line)]] | alt | 110 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +11.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.171× (z -20.3) |
| [[A498 (line)]] | wt | 91.0 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.257× (z -15.3) |
| [[Hs 766T (line)]] | wt | 119 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.81× (z +8.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.151× (z -18.6) |
| [[SW 900 (line)]] | alt | 77.4 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +10.2) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.243× (z -13.6) |
| [[SW480 (line)]] | alt | 86.4 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +12.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.208× (z -13.0) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.326× (z -12.8) |
| [[A-427 (line)]] | wt | 104 | 2 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.68× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 5 µM 2.31× (z +8.8) | [[Docetaxel (drug)]] 0.05 µM 0.136× (z -15.4) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.254× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 79.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +10.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.210× (z -11.9) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 85.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +12.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.201× (z -12.8) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 85.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +12.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.197× (z -12.8) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 60.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +11.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.199× (z -11.7) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 73.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +10.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.244× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 73.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.240× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 58.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +10.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.291× (z -8.6) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 72.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +8.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.230× (z -10.7) ⚠ transcription drop |
| [[NCI-H2347 (line)]] | alt | 67.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.286× (z -10.3) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 140 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.79× (z +8.7) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.0730× (z -18.5) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 66.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.330× (z -9.3) |
| [[SNU-423 (line)]] | alt | 86.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.93× (z +9.7) | [[Docetaxel (drug)]] 0.05 µM 0.129× (z -13.6) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 89.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.58× (z +9.8) | [[Docetaxel (drug)]] 0.05 µM 0.194× (z -12.3) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 62.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.319× (z -9.9) |
| [[AN3 CA (line)]] | alt | 89.2 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0953× (z -12.0) ⚠ transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 66.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +10.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.252× (z -10.3) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 68.3 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.152× (z -11.8) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.257× (z -11.6) |
| [[C32 (line)]] | wt | 66.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +9.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.316× (z -11.4) |
| [[COLO 205 (line)]] | alt | 65.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +9.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -10.7) ⚠ transcription drop |
| [[H4 (line)]] | wt | 69.7 | 0 | 2 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.283× (z -10.7) |
| [[HS-578T (line)]] | alt | 57.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +8.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.262× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 50.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.51× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 5 µM 2.98× (z +8.8) | — |
| [[KATO III (line)]] | alt | 124 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +9.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.193× (z -12.2) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 57.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +10.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.222× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 105 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.191× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 169 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.179× (z -13.7) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.321× (z -12.3) |
| [[SHP-77 (line)]] | alt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +8.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.112× (z -15.5) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.209× (z -12.1) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 48.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.73× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 64.0 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.349× (z -8.9) |
| [[J82 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.178× (z -12.2) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 89.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.115× (z -9.0) ⚠ transcription drop |
| [[RKO (line)]] | wt | 99.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.275× (z -9.4) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.197× (z -11.5) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.4 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | mitochondrially encoded cytochrome c oxidase II |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:7,586-8,269 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COX2, CO2; previously MTCO2 |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits; Mitochondrially encoded protein coding genes; Cupredoxin superfamily |
| Reactome | 23 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P00403](https://www.uniprot.org/uniprotkb/P00403) (Cytochrome c oxidase subunit 2):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [4513](https://www.ncbi.nlm.nih.gov/gene/4513):

> Contributes to cytochrome-c oxidase activity. Predicted to be involved in mitochondrial electron transport, cytochrome c to oxygen and positive regulation of vasoconstriction. Located in mitochondrial inner membrane. Part of respiratory chain complex IV. Biomarker of Huntington's disease and stomach cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7421) · Entrez [4513](https://www.ncbi.nlm.nih.gov/gene/4513) · UniProt [P00403](https://www.uniprot.org/uniprotkb/P00403) · Ensembl [ENSG00000198712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198712)

## Data

Gene col 12648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12648); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12648, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12648]; `tensor/DDL_lfc|DDL_z.npy` [12648]; `embed/gene_vectors.npy` [12648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12648 or target_col == 12648). Every well: [[MT-CO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-CO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
