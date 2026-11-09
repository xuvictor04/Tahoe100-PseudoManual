---
symbol: "SERPINH1"
type: "gene"
col: 7355
ensembl_id: "ENSG00000149257"
name: "serpin family H member 1"
location: "11q13.5"
module: 60
arm: "+"
pooled_cpm: 50.8
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 26
n_dd_up_clean: 12
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# SERPINH1

*serpin family H member 1* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 9.15× (z +29.7, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.254× (z -26.0, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL18]] (+0.76, fdr 7e-06), [[AHSA1]] (+0.71, fdr 7e-06), [[HSP90AA2P]] (+0.71, fdr 7e-06); moves opposite to [[ARL13B]] (-0.56, fdr 1e-05), [[NUDCD2]] (-0.55, fdr 1e-04), [[UGCG]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **9.15×** | +29.7 | 0e+00 | 45/45 (SW480, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.77×** | +17.8 | 0e+00 | 42/45 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.66×** | +17.4 | 0e+00 | 44/45 (NCI-H2347, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **9.28×** | +15.6 | 0e+00 | 41/42 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.14×** | +14.5 | 1e-45 | 43/45 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +12.0 | 3e-31 | 35/45 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +11.8 | 5e-30 | 34/44 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **3.36×** | +11.6 | 3e-29 | 43/45 (A-427, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +9.9 | 2e-21 | 31/39 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.7 | 9e-10 | 25/40 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM |  | **2.20×** | +5.5 | 2e-06 | 33/44 (A-172, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.9 | 6e-05 | 32/44 (LS 180, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.94×** | +4.7 | 1e-04 | 29/45 (AsPC-1, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 21/45 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.49×** | +3.8 | 0.006 | 21/43 (A-427, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Zileuton (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.037 | 16/45 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.037 | 13/45 (J82, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.042 | 16/45 (RPMI-7951, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.254×** | -26.0 | 0e+00 | 44/45 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.243×** | -19.0 | 0e+00 | 43/45 (H4, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.267×** | -17.7 | 0e+00 | 44/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.276×** | -17.2 | 0e+00 | 43/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.289×** | -16.0 | 0e+00 | 45/45 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.385×** | -12.8 | 2e-35 | 42/45 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.409×** | -12.0 | 4e-31 | 40/45 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.460×** | -10.4 | 2e-23 | 42/45 (Panc 03.27, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.464×** | -10.3 | 5e-23 | 37/45 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.465×** | -10.3 | 6e-23 | 38/45 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.513×** | -8.9 | 2e-17 | 35/45 (H4, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -8.6 | 4e-16 | 35/45 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.654×** | -8.0 | 4e-14 | 37/45 (C32, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.342×** | -7.5 | 2e-12 | 37/45 (SW480, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -6.7 | 6e-10 | 32/45 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.649×** | -5.8 | 2e-07 | 29/45 (H4, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 156 | 8 (3 ⚠) | 9 | [[Ixazomib citrate (drug)]] 0.5 µM 5.29× (z +17.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.0966× (z -24.2) |
| [[H4 (line)]] | wt | 304 | 2 (1 ⚠) | 15 (1 ⚠) | [[Bortezomib (drug)]] 5 µM 9.41× (z +9.8) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.94× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.0489× (z -36.0) |
| [[A-172 (line)]] | wt | 98.1 | 8 (3 ⚠) | 8 | [[Auranofin (drug)]] 5 µM 9.58× (z +19.5) | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -26.2) |
| [[SW480 (line)]] | alt | 32.7 | 8 (2 ⚠) | 8 | [[Auranofin (drug)]] 5 µM 26.1× (z +31.5) | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -20.2) |
| [[A-427 (line)]] | wt | 57.6 | 6 (1 ⚠) | 9 (2 ⚠) | [[Auranofin (drug)]] 5 µM 24.4× (z +28.5) | [[Belinostat (drug)]] 5 µM 0.191× (z -14.7) |
| [[J82 (line)]] | alt | 65.4 | 8 (4 ⚠) | 7 | [[Auranofin (drug)]] 5 µM 5.66× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -22.0) |
| [[C32 (line)]] | wt | 76.9 | 4 (1 ⚠) | 10 | [[Auranofin (drug)]] 5 µM 21.3× (z +24.2) | [[Panobinostat (drug)]] 0.5 µM 0.0936× (z -18.7) |
| [[HS-578T (line)]] | alt | 134 | 6 (2 ⚠) | 8 | [[Auranofin (drug)]] 5 µM 4.74× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.9) |
| [[KATO III (line)]] | alt | 49.0 | 7 (2 ⚠) | 6 | [[Auranofin (drug)]] 5 µM 8.11× (z +17.2) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 64.3 | 6 (1 ⚠) | 7 | [[Ixazomib citrate (drug)]] 5 µM 6.73× (z +18.4) | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -21.9) |
| [[NCI-H23 (line)]] | alt | 85.9 | 2 (1 ⚠) | 10 (2 ⚠) | [[Auranofin (drug)]] 5 µM 14.2× (z +24.3) | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -21.9) |
| [[RPMI-7951 (line)]] | alt | 198 | 1 | 11 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.95× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.0865× (z -29.1) |
| [[Panc 03.27 (line)]] | alt | 30.9 | 5 (1 ⚠) | 6 | [[Auranofin (drug)]] 5 µM 12.1× (z +17.3) | [[Belinostat (drug)]] 5 µM 0.243× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 38.7 | 7 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 10.3× (z +18.6) | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 122 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.0625× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 66.5 | 3 | 7 | [[Auranofin (drug)]] 5 µM 9.92× (z +16.2) | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -16.6) |
| [[RKO (line)]] | wt | 53.0 | 3 | 7 | [[Auranofin (drug)]] 5 µM 8.22× (z +16.5) | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -22.0) |
| [[SW1417 (line)]] | alt | 29.3 | 6 (1 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 14.7× (z +20.6) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 48.9 | 4 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.10× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -14.5) |
| [[LoVo (line)]] | wt | 18.1 | 5 (3 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 28.3× (z +23.7) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 48.9 | 5 (1 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 12.7× (z +20.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.0464× (z -24.1) |
| [[HT-29 (line)]] | alt | 16.4 | 5 | 3 | [[Auranofin (drug)]] 5 µM 64.0× (z +25.4) | [[Belinostat (drug)]] 5 µM 0.147× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 29.8 | 4 (2 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -12.6) |
| [[PANC-1 (line)]] | alt | 21.6 | 5 (3 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 7.45× (z +16.8) | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 31.5 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 30.9× (z +25.8) | — |
| [[HOP62 (line)]] | alt | 17.2 | 4 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 26.4× (z +19.0) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.3) |
| [[LS 180 (line)]] | wt | 23.2 | 3 | 3 | [[Auranofin (drug)]] 5 µM 6.97× (z +13.8) | [[Belinostat (drug)]] 5 µM 0.173× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 41.1 | 3 | 3 | [[Auranofin (drug)]] 5 µM 5.84× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -15.4) |
| [[SW 900 (line)]] | alt | 50.7 | 1 | 5 | [[Auranofin (drug)]] 5 µM 9.95× (z +16.8) | [[Belinostat (drug)]] 5 µM 0.0970× (z -17.0) |
| [[BT-474 (line)]] | alt | 37.3 | 4 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 49.0× (z +25.5) | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.4) |
| [[Hs 766T (line)]] | wt | 35.3 | 1 | 4 | [[Auranofin (drug)]] 5 µM 8.04× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -11.2) |
| [[AN3 CA (line)]] | alt | 121 | 1 | 3 | [[Auranofin (drug)]] 5 µM 4.48× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -18.1) |
| [[HCT15 (line)]] | alt | 37.3 | 1 | 3 | [[Auranofin (drug)]] 5 µM 9.35× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.114× (z -12.3) |
| [[A549 (line)]] | wt | 18.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +13.5) | — |
| [[C-33 A (line)]] | alt | 21.7 | 2 | 1 | [[Auranofin (drug)]] 5 µM 18.5× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.0) |
| [[SHP-77 (line)]] | alt | 50.6 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 17.9× (z +15.8) | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -13.7) |
| [[SNU-423 (line)]] | alt | 35.8 | 1 | 2 | [[Auranofin (drug)]] 5 µM 17.9× (z +19.5) | [[Harringtonine (drug)]] 5 µM 0.140× (z -12.8) |
| [[SW48 (line)]] | wt | 22.4 | 1 | 2 | [[Auranofin (drug)]] 5 µM 39.4× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.108× (z -10.4) |
| [[CHP-212 (line)]] | wt | 46.3 | 1 | 1 | [[Auranofin (drug)]] 5 µM 8.95× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.8) |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.1) |
| [[SNU-1 (line)]] | wt | 34.5 | 1 | 1 | [[Auranofin (drug)]] 5 µM 17.0× (z +16.3) | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 28.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.99× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.6) |
| [[SW 1088 (line)]] | alt | 93.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0357× (z -10.9) |
| [[SW 1271 (line)]] | alt | 35.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 37.5× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 8.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL18]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 | pathway: Attenuation phase |
| [[AHSA1]] | +0.71 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[HSP90AA2P]] | +0.71 | +0.80 / +0.62 | both halves | 7e-06 |  |
| [[B4GALNT1]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[DNAJA4]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ATP2C1]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[SOD1]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[FKBP4]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 | pathway: Attenuation phase |
| [[GPN1]] | +0.64 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[VCP]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[HSPA8]] | +0.63 | +0.72 / +0.63 | both halves | 7e-06 | pathway: Attenuation phase; STRING 707 |
| [[ALKBH6]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL13B]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[NUDCD2]] | -0.55 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[UGCG]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GTF2H5]] | -0.54 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[PIM3]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[DOP1A]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.53 | -0.52 / -0.44 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TXNIP]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[POLR2L]] | -0.51 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[IKBKB]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[BIRC3]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SAV1]] | -0.50 | -0.34 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.2, -10.3); signed map (-25.7, -28.2). **Vector** length 131, 44.7% of its response variance represented; |z| ≥ 3 in 1,577 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.50 to 13); *HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand* (reactome, mean cos +0.50 to 12); *AUF1 (hnRNP D0) binds and destabilizes mRNA* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +16.6 | +29.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +14.0 | +14.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +13.7 | +17.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.7 | +12.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +12.5 | +15.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.0 | +17.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +7.0 | +11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.6 | +4.0 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.9 | +4.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.5 | -8.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -7.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | serpin family H member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:75,562,056-75,572,783 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSP47; previously CBP1, CBP2, SERPINH2 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION, MTORC1_SIGNALING |
| Reactome | 10 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [P50454](https://www.uniprot.org/uniprotkb/P50454) (Serpin H1):

> Binds specifically to collagen. Could be involved as a chaperone in the biosynthetic pathway of collagen.

**Summary**, from NCBI Gene [871](https://www.ncbi.nlm.nih.gov/gene/871):

> This gene encodes a member of the serpin superfamily of serine proteinase inhibitors. The encoded protein is localized to the endoplasmic reticulum and plays a role in collagen biosynthesis as a collagen-specific molecular chaperone. Autoantibodies to the encoded protein have been found in patients with rheumatoid arthritis. Expression of this gene may be a marker for cancer, and nucleotide polymorphisms in this gene may be associated with preterm birth caused by preterm premature rupture of …

**Accessions** — [HGNC:1546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1546) · Entrez [871](https://www.ncbi.nlm.nih.gov/gene/871) · UniProt [P50454](https://www.uniprot.org/uniprotkb/P50454) · Ensembl [ENSG00000149257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149257)

## Data

Gene col 7355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7355); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7355]; `tensor/DDL_lfc|DDL_z.npy` [7355]; `embed/gene_vectors.npy` [7355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7355 or target_col == 7355). Every well: [[SERPINH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
