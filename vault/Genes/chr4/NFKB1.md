---
symbol: "NFKB1"
type: "gene"
col: 3042
ensembl_id: "ENSG00000109320"
name: "nuclear factor kappa B subunit 1"
location: "4q24"
module: 14
arm: "+"
pooled_cpm: 174.88
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NFKB1

*nuclear factor kappa B subunit 1* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.57× (z +45.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.222× (z -25.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIVEP2]] (+0.72, fdr 7e-06), [[CXCL2]] (+0.69, fdr 7e-06), [[CXCL3]] (+0.66, fdr 1e-05); moves opposite to [[PWWP3A]] (-0.65, fdr 1e-05), [[AP2A2]] (-0.64, fdr 1e-05), [[ANKRD27]] (-0.64, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02605]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.57×** | +45.5 | 0e+00 | 48/48 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.61×** | +26.8 | 0e+00 | 48/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +20.5 | 0e+00 | 48/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **9.82×** | +20.4 | 0e+00 | 49/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.21×** | +19.9 | 0e+00 | 48/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.01×** | +18.8 | 0e+00 | 45/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.71×** | +15.5 | 0e+00 | 45/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.43×** | +15.2 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.23×** | +13.7 | 4e-41 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.92×** | +12.2 | 2e-32 | 48/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +9.8 | 9e-21 | 34/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.83×** | +9.3 | 7e-19 | 35/38 (A-172, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.62×** | +8.3 | 5e-15 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +8.1 | 3e-14 | 35/45 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +5.3 | 4e-06 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.001 | 25/50 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.032 | 19/48 (CFPAC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.042 | 17/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.222×** | -25.7 | 0e+00 | 48/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.247×** | -23.9 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.255×** | -23.4 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.457×** | -13.4 | 9e-39 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -13.0 | 1e-36 | 36/44 (Panc 03.27, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.495×** | -12.0 | 3e-31 | 40/48 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.531×** | -10.8 | 2e-25 | 44/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.390×** | -8.4 | 3e-15 | 41/49 (SW480, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -6.9 | 4e-10 | 31/49 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.684×** | -6.5 | 5e-09 | 31/48 (RKO, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.775×** | -6.2 | 3e-08 | 35/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.705×** | -6.0 | 1e-07 | 29/49 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.538×** | -5.5 | 1e-06 | 30/45 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.644×** | -5.5 | 1e-06 | 33/48 (A549, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.735×** | -5.3 | 5e-06 | 35/49 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.745×** | -5.0 | 2e-05 | 32/49 (LoVo, SNU-423, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.616×** | -4.3 | 5e-04 | 25/47 (NCI-H2347, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.791×** | -4.0 | 0.002 | 25/48 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.803×** | -3.8 | 0.005 | 23/48 (A-427, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 82.9 | 13 (4 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +23.8) | [[Belinostat (drug)]] 5 µM 0.145× (z -28.6) |
| [[NCI-H460 (line)]] | wt | 153 | 15 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +34.4) | [[Panobinostat (drug)]] 5 µM 0.290× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 252 | 8 (2 ⚠) | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +26.8) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -15.3) |
| [[LoVo (line)]] | wt | 140 | 11 (3 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +35.2) | [[Panobinostat (drug)]] 5 µM 0.155× (z -24.6) |
| [[PANC-1 (line)]] | alt | 143 | 10 (3 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +31.9) | [[Belinostat (drug)]] 5 µM 0.257× (z -15.9) |
| [[A-172 (line)]] | wt | 107 | 13 (4 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +38.8) | [[Panobinostat (drug)]] 5 µM 0.335× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 449 | 10 (2 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +21.2) | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 109 | 9 (2 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +19.2) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -19.9) |
| [[SW48 (line)]] | wt | 187 | 10 (2 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +18.2) | [[Belinostat (drug)]] 5 µM 0.127× (z -15.8) |
| [[H4 (line)]] | wt | 168 | 11 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +25.1) | [[Panobinostat (drug)]] 5 µM 0.130× (z -16.4) |
| [[HOP62 (line)]] | alt | 194 | 11 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +30.3) | [[Panobinostat (drug)]] 5 µM 0.213× (z -12.6) |
| [[LS 180 (line)]] | wt | 118 | 10 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +23.7) | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 353 | 9 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +30.0) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.315× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 191 | 7 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +33.6) | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -22.1) |
| [[Hs 766T (line)]] | wt | 152 | 10 (3 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +36.6) | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -14.9) |
| [[KATO III (line)]] | alt | 91.3 | 9 (2 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +24.1) | [[Panobinostat (drug)]] 5 µM 0.149× (z -22.3) |
| [[SNU-1 (line)]] | wt | 202 | 9 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +25.5) | [[Panobinostat (drug)]] 5 µM 0.311× (z -10.9) |
| [[SNU-423 (line)]] | alt | 105 | 9 (3 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +29.9) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -12.8) |
| [[BT-474 (line)]] | alt | 170 | 10 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +29.1) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -13.8) |
| [[HT-29 (line)]] | alt | 120 | 8 (3 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 8.21× (z +28.2) | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -17.5) |
| [[hTERT-HPNE (line)]] | wt | 219 | 11 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +27.3) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.325× (z -8.9) |
| [[J82 (line)]] | alt | 165 | 9 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.74× (z +34.8) | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 223 | 11 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +25.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 189 | 7 (3 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +27.8) | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -19.2) |
| [[HS-578T (line)]] | alt | 160 | 11 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +25.6) | [[Panobinostat (drug)]] 5 µM 0.342× (z -9.0) |
| [[A-427 (line)]] | wt | 87.7 | 6 | 5 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +26.6) | [[Panobinostat (drug)]] 5 µM 0.158× (z -21.5) |
| [[C32 (line)]] | wt | 151 | 6 | 5 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +27.5) | [[Belinostat (drug)]] 5 µM 0.179× (z -18.1) |
| [[Panc 03.27 (line)]] | alt | 262 | 4 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +30.7) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.275× (z -13.5) |
| [[SW 900 (line)]] | alt | 160 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +27.7) | — |
| [[A549 (line)]] | wt | 227 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +28.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -15.0) |
| [[HCT15 (line)]] | alt | 139 | 7 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.180× (z -15.9) |
| [[LOX-IMVI (line)]] | wt | 150 | 5 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +19.1) | [[Panobinostat (drug)]] 5 µM 0.137× (z -18.5) |
| [[NCI-H2030 (line)]] | alt | 173 | 7 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +21.1) | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -14.6) |
| [[RKO (line)]] | wt | 276 | 2 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -24.9) |
| [[CFPAC-1 (line)]] | alt | 296 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +32.1) | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -14.5) |
| [[SW1417 (line)]] | alt | 103 | 4 | 5 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +23.9) | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -18.7) |
| [[HepG2_C3A (line)]] | wt | 160 | 6 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +20.4) | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 185 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +25.8) | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -11.7) |
| [[A498 (line)]] | wt | 217 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.435× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 155 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +22.0) | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -18.2) |
| [[AN3 CA (line)]] | alt | 163 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.210× (z -10.2) |
| [[COLO 205 (line)]] | alt | 124 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.0741× (z -15.1) |
| [[SHP-77 (line)]] | alt | 97.2 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.144× (z -14.5) |
| [[C-33 A (line)]] | alt | 81.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 3.00× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -16.4) |
| [[CHP-212 (line)]] | wt | 176 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.144× (z -9.7) |
| [[SW 1088 (line)]] | alt | 129 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +12.6) | — |
| [[SW 1271 (line)]] | alt | 161 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +14.1) | — |
| [[NCI-H2122 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIVEP2]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 | STRING 559 |
| [[CXCL2]] | +0.69 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 969 |
| [[CXCL3]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 942 |
| [[PATL2]] | +0.65 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[BIRC2]] | +0.65 | +0.52 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 773 |
| [[LINC02605]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[REL]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[CCNL1]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IFNGR2]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[RELB]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PWWP3A]] | -0.65 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[AP2A2]] | -0.64 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ANKRD27]] | -0.64 | -0.53 / -0.59 | both halves | 1e-05 | same gene group |
| [[ZCCHC17]] | -0.63 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[RBAK-RBAKDN]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RNF216P1]] | -0.62 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[FLYWCH1]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[DCUN1D2]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[NFRKB]] | -0.59 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[MACO1]] | -0.59 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[USP35]] | -0.59 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[BICD2]] | -0.58 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02605]] | B | LINC02605 activity raises NFKB1's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 1.50× lower at baseline in the lines without LINC02605 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[CSF1]] | B | CSF1 activity raises NFKB1's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without CSF1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[NFKBIZ]] | C | NFKBIZ activity raises NFKB1's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without NFKBIZ | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 6.2); signed map (42.2, 6.9). **Vector** length 119, 47.8% of its response variance represented; |z| ≥ 3 in 1,879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.9 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.6 | +26.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +45.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +0.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -11.1 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -10.8 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.0 | -12.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.5 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.5 | -10.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.6 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -4.0 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -8.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor kappa B subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:102,501,330-102,617,302 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KBF1, p105, NFKB-p50, p50, NF-kappaB, NFkappaB, NF-kB1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; NF-kappa B complex subunits; IPT domain containing; NFKB inhibitor family |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 96 pathways, smallest: CLEC7A/inflammasome pathway; DEx/H-box helicases activate type I IFN and inflammatory cytokines production; IkBA variant leads to EDA-ID |
| Matched by | ensembl_id |

**Function**, from UniProt [P19838](https://www.uniprot.org/uniprotkb/P19838) (Nuclear factor NF-kappa-B p105 subunit):

> NF-kappa-B is a pleiotropic transcription factor present in almost all cell types and is the endpoint of a series of signal transduction events that are initiated by a vast array of stimuli related to many biological processes such as inflammation, immunity, differentiation, cell growth, tumorigenesis and apoptosis. NF-kappa-B is a homo- or heterodimeric complex formed by the Rel-like domain-containing proteins RELA/p65, RELB, NFKB1/p105, NFKB1/p50, REL and NFKB2/p52 and the heterodimeric …

**Summary**, from NCBI Gene [4790](https://www.ncbi.nlm.nih.gov/gene/4790):

> This gene encodes a 105 kD protein which can undergo cotranslational processing by the 26S proteasome to produce a 50 kD protein. The 105 kD protein is a Rel protein-specific transcription inhibitor and the 50 kD protein is a DNA binding subunit of the NF-kappa-B (NFKB) protein complex. NFKB is a transcription regulator that is activated by various intra- and extra-cellular stimuli such as cytokines, oxidant-free radicals, ultraviolet irradiation, and bacterial or viral products. Activated NFKB …

**Accessions** — [HGNC:7794](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7794) · Entrez [4790](https://www.ncbi.nlm.nih.gov/gene/4790) · UniProt [P19838](https://www.uniprot.org/uniprotkb/P19838) · Ensembl [ENSG00000109320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109320)

## Data

Gene col 3042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3042); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3042]; `tensor/DDL_lfc|DDL_z.npy` [3042]; `embed/gene_vectors.npy` [3042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3042 or target_col == 3042). Every well: [[NFKB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFKB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
