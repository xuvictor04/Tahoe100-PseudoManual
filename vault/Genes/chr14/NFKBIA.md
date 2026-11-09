---
symbol: "NFKBIA"
type: "gene"
col: 2040
ensembl_id: "ENSG00000100906"
name: "NFKB inhibitor alpha"
location: "14q13.2"
module: 14
arm: "+"
pooled_cpm: 141.56
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NFKBIA

*NFKB inhibitor alpha* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.4× (z +33.5, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.336× (z -10.6, q 2e-23, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP3]] (+0.85, fdr 7e-06), [[CXCL2]] (+0.73, fdr 7e-06), [[BCL3]] (+0.73, fdr 7e-06); moves opposite to [[ZCCHC17]] (-0.62, fdr 1e-05), [[UFD1]] (-0.60, fdr 1e-05), [[MBOAT7]] (-0.60, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[BIRC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.4×** | +33.5 | 0e+00 | 47/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **10.8×** | +22.2 | 0e+00 | 47/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.01×** | +15.6 | 0e+00 | 47/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **16.3×** | +14.2 | 3e-43 | 48/48 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.36×** | +11.3 | 1e-27 | 45/46 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +9.5 | 2e-19 | 45/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.58×** | +9.2 | 4e-18 | 41/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.65×** | +8.8 | 1e-16 | 42/47 (SW48, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.40×** | +8.5 | 1e-15 | 44/47 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.5 µM |  | **2.49×** | +6.3 | 1e-08 | 41/47 (PANC-1, HEC-1-A, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.86×** | +6.0 | 8e-08 | 36/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.71×** | +5.2 | 8e-06 | 34/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.70×** | +5.2 | 1e-05 | 33/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.67×** | +5.0 | 2e-05 | 37/47 (AsPC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +4.5 | 3e-04 | 29/44 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.018 | 25/47 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.019 | 27/47 (Panc 03.27, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.035 | 24/47 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.037 | 27/47 (HCT15, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.040 | 26/47 (RPMI-7951, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.044 | 23/48 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.066 | 25/47 (HT-29, RKO, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.53×** | +2.9 | 0.079 | 24/47 (PANC-1, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.336×** | -10.6 | 2e-23 | 45/47 (SW 1271, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -8.3 | 2e-14 | 37/48 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.425×** | -8.3 | 2e-14 | 44/47 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -7.8 | 7e-13 | 44/47 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.546×** | -5.9 | 5e-07 | 38/47 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.720×** | -4.5 | 6e-04 | 31/47 (HOP62, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.621×** | -4.4 | 9e-04 | 27/47 (NCI-H1573, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.638×** | -4.4 | 9e-04 | 37/47 (HOP62, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.431×** | -4.3 | 0.001 | 35/46 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.470×** | -3.8 | 0.007 | 37/48 (H4, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.675×** | -3.7 | 0.012 | 31/47 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -3.3 | 0.040 | 27/47 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.539×** | -3.1 | 0.074 | 25/44 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.78 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 109 | 15 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +27.2) | — |
| [[PANC-1 (line)]] | alt | 123 | 11 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 25.7× (z +37.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 268 | 7 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +20.4) | [[Auranofin (drug)]] 5 µM 0.128× (z -15.5) |
| [[HOP62 (line)]] | alt | 129 | 6 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +31.7) | [[Auranofin (drug)]] 5 µM 0.201× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 206 | 8 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 39.5× (z +35.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 361 | 7 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +25.8) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 339 | 6 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +28.9) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.190× (z -14.3) |
| [[SNU-1 (line)]] | wt | 107 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +22.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -9.3) |
| [[SW 900 (line)]] | alt | 144 | 8 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +19.8) | [[Auranofin (drug)]] 5 µM 0.123× (z -14.5) |
| [[HS-578T (line)]] | alt | 122 | 7 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +25.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -11.7) |
| [[KATO III (line)]] | alt | 41.4 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +28.1) | — |
| [[A-427 (line)]] | wt | 53.7 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +24.3) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 235 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +32.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 138 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +33.2) | [[Auranofin (drug)]] 5 µM 0.313× (z -9.0) |
| [[BT-474 (line)]] | alt | 197 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +29.9) | — |
| [[LS 180 (line)]] | wt | 83.0 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +23.5) | — |
| [[NCI-H23 (line)]] | alt | 161 | 3 | 5 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +14.0) | [[Auranofin (drug)]] 5 µM 0.155× (z -14.3) |
| [[SW48 (line)]] | wt | 224 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +23.7) | — |
| [[A-172 (line)]] | wt | 87.9 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +26.5) | [[Auranofin (drug)]] 5 µM 0.255× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 181 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +30.7) | — |
| [[SNU-423 (line)]] | alt | 103 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +33.2) | [[Auranofin (drug)]] 5 µM 0.237× (z -9.9) |
| [[C32 (line)]] | wt | 51.6 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 22.4× (z +23.6) | [[Auranofin (drug)]] 5 µM 0.188× (z -8.9) |
| [[H4 (line)]] | wt | 103 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.56× (z +17.6) | [[Auranofin (drug)]] 5 µM 0.181× (z -10.5) |
| [[J82 (line)]] | alt | 105 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +27.8) | — |
| [[NCI-H2030 (line)]] | alt | 172 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +25.2) | — |
| [[RPMI-7951 (line)]] | alt | 113 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +20.3) | [[Auranofin (drug)]] 5 µM 0.209× (z -10.0) |
| [[Hs 766T (line)]] | wt | 149 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.2) |
| [[LoVo (line)]] | wt | 114 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +24.5) | [[Auranofin (drug)]] 5 µM 0.323× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 176 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +25.3) | — |
| [[Panc 03.27 (line)]] | alt | 217 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +33.6) | [[Auranofin (drug)]] 5 µM 0.292× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 44.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +20.7) | — |
| [[A498 (line)]] | wt | 200 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +22.8) | — |
| [[CFPAC-1 (line)]] | alt | 292 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.5× (z +35.8) | — |
| [[HCT15 (line)]] | alt | 95.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +15.0) | — |
| [[SW1417 (line)]] | alt | 97.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +23.4) | — |
| [[SW480 (line)]] | alt | 39.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +19.6) | — |
| [[AN3 CA (line)]] | alt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +17.0) | — |
| [[COLO 205 (line)]] | alt | 72.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +17.6) | [[Belinostat (drug)]] 5 µM 0.180× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 149 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +23.8) | — |
| [[HT-29 (line)]] | alt | 70.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +20.8) | — |
| [[RKO (line)]] | wt | 93.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +16.7) | — |
| [[SW 1271 (line)]] | alt | 198 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +14.0) | [[Auranofin (drug)]] 5 µM 0.0226× (z -15.7) |
| [[LOX-IMVI (line)]] | wt | 55.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +19.2) | — |
| [[SW 1088 (line)]] | alt | 175 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +12.6) | — |
| [[CHP-212 (line)]] | wt | 137 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 73.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 33.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 288 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP3]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 870 |
| [[CXCL2]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 681 |
| [[BCL3]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 904 |
| [[ZC3H12A]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 530 |
| [[WTAP]] | +0.70 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[CX3CL1]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[REL]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[CSF1]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 519 |
| [[TNFAIP2]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 426 |
| [[IRF1]] | +0.67 | +0.72 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 681 |
| [[CEBPD]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 489 |
| [[PER1]] | +0.65 | +0.58 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC17]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[UFD1]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 | pathway: Deubiquitination |
| [[MBOAT7]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.59 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SENP5]] | -0.56 | -0.47 / -0.60 | both halves | 2e-05 | pathway: SUMOylation |
| [[VPS53]] | -0.55 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[POC1B]] | -0.55 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[GPR89A]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[MFN1]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIRC3]] | B | BIRC3 activity raises NFKBIA's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without BIRC3 | 0.036 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |
| [[TOP2A]] | B | TOP2A activity raises NFKBIA's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CSF1]] | B | CSF1 activity raises NFKBIA's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without CSF1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[NFKBIZ]] | C | NFKBIZ activity raises NFKBIA's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 3.45× lower at baseline in the lines without NFKBIZ | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |
| [[SMAD7]] | C | SMAD7's natural level strengthens NFKBIA's drug response | SMAD7's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.45; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MAP3K8]] | C | MAP3K8 activity raises NFKBIA's level | lines that do not express MAP3K8 (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without MAP3K8 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02649, LINC02656, SOX9; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, 5.2); signed map (43.6, 6.9). **Vector** length 137, 54.9% of its response variance represented; |z| ≥ 3 in 1,420 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IL6 JAK STAT3 signaling* (hallmark, mean cos +0.52 to 11); *Nucleotide-binding domain, leucine rich repeat containing receptor (NLR) signaling pathways* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +33.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.5 | +22.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +14.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.0 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.6 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -14.3 | -10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -9.1 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -8.3 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.6 | +0.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | -5.5 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | +0.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | NFKB inhibitor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.2 — chr14:35,401,079-35,404,749 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IKBA, MAD-3, IkappaBalpha; previously NFKBI |
| Gene groups (HGNC) | Ankyrin repeat domain containing; NFKB inhibitor family |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_UP, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 61 pathways, smallest: IkBA variant leads to EDA-ID; SUMOylation of immune response proteins; NF-kB is activated and signals survival |
| Matched by | ensembl_id |

**Function**, from UniProt [P25963](https://www.uniprot.org/uniprotkb/P25963) (NF-kappa-B inhibitor alpha):

> Inhibits the activity of dimeric NF-kappa-B/REL complexes by trapping REL (RELA/p65 and NFKB1/p50) dimers in the cytoplasm by masking their nuclear localization signals. On cellular stimulation by immune and pro-inflammatory responses, becomes phosphorylated promoting ubiquitination and degradation, enabling the dimeric RELA to translocate to the nucleus and activate transcription.

**Summary**, from NCBI Gene [4792](https://www.ncbi.nlm.nih.gov/gene/4792):

> This gene encodes a member of the NF-kappa-B inhibitor family, which contain multiple ankrin repeat domains. The encoded protein interacts with REL dimers to inhibit NF-kappa-B/REL complexes which are involved in inflammatory responses. The encoded protein moves between the cytoplasm and the nucleus via a nuclear localization signal and CRM1-mediated nuclear export. Mutations in this gene have been found in ectodermal dysplasia anhidrotic with T-cell immunodeficiency autosomal dominant disease. …

**Accessions** — [HGNC:7797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7797) · Entrez [4792](https://www.ncbi.nlm.nih.gov/gene/4792) · UniProt [P25963](https://www.uniprot.org/uniprotkb/P25963) · Ensembl [ENSG00000100906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100906)

## Data

Gene col 2040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2040); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2040]; `tensor/DDL_lfc|DDL_z.npy` [2040]; `embed/gene_vectors.npy` [2040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2040 or target_col == 2040). Every well: [[NFKBIA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFKBIA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
