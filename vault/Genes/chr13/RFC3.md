---
symbol: "RFC3"
type: "gene"
col: 5421
ensembl_id: "ENSG00000133119"
name: "replication factor C subunit 3"
location: "13q13.2"
module: 6
arm: "+"
pooled_cpm: 88.83
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RFC3

*replication factor C subunit 3* — 13q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.28× (z +15.1, q 0e+00, up in 37 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 1.63× (z +5.1, q 2e-05, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[palbociclib (drug)]] 0.5 µM: 0.681× (z -5.4, q 3e-05, down in 29 of 47 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.666× (z -4.2, q 0.004, down in 16 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTBP]] (+0.84, fdr 7e-06), [[CENPK]] (+0.83, fdr 7e-06), [[DTL]] (+0.82, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.28×** | +15.1 | 0e+00 | 37/44 (NCI-H460, SHP-77, …) | inconsistent across doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.70×** | +10.1 | 2e-21 | 38/47 (J82, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.66×** | +10.0 | 3e-21 | 38/47 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.62×** | +9.5 | 3e-19 | 36/47 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.57×** | +9.0 | 3e-17 | 33/47 (LoVo, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.40×** | +6.4 | 1e-08 | 33/49 (SW480, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~90% of this change | **1.36×** | +5.8 | 5e-07 | 26/46 (NCI-H2030, J82, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +5.3 | 7e-06 | 25/47 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +5.1 | 2e-05 | 22/48 (Panc 03.27, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.0 | 3e-05 | 22/47 (J82, Panc 03.27, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.0 | 3e-05 | 24/47 (LoVo, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.8 | 7e-05 | 22/47 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.27×** | +4.7 | 1e-04 | 20/47 (RKO, HT-29, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 6e-04 | 22/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.16× | +4.2 | 9e-04 | 16/47 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 14/47 (SW480, SW 900, …) | rises with dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.011 | 17/47 (A-427, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.044 | 14/47 (KATO III, LoVo, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.046 | 11/46 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.052 | 13/47 (BT-474, NCI-H1573, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.17× | +2.9 | 0.060 | 11/47 (LoVo, A549, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.11× | +2.9 | 0.063 | 2/47 (MIA PaCa-2, COLO 205) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +2.8 | 0.074 | 9/46 (SHP-77, J82, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.681×** | -5.4 | 3e-05 | 29/47 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.782×** | -4.9 | 3e-04 | 21/47 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.848× | -4.6 | 7e-04 | 24/47 (A498, MIA PaCa-2, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.666×** | -4.2 | 0.004 | 16/47 (MIA PaCa-2, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.821×** | -3.9 | 0.009 | 22/47 (A498, H4, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.05 µM |  | **0.812×** | -3.9 | 0.009 | 20/47 (SW 900, PANC-1, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.017 | 20/47 (COLO 205, RKO, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.879× | -3.6 | 0.019 | 17/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.706×** | -3.6 | 0.019 | 16/47 (SW480, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.835× | -3.6 | 0.019 | 13/47 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.714×** | -3.5 | 0.024 | 9/47 (SK-MEL-2, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 0.884× | -3.5 | 0.024 | 14/47 (KATO III, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.833×** | -3.4 | 0.027 | 18/47 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.841× | -3.3 | 0.039 | 15/46 (J82, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.855× | -3.1 | 0.068 | 16/46 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.896× | -3.1 | 0.071 | 13/47 (RKO, H4, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.853× | -3.0 | 0.079 | 7/47 (NCI-H2347, LoVo, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.79 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 140 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -21.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.485× (z -9.3) |
| [[LS 180 (line)]] | wt | 52.4 | 4 (4 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.23× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.415× (z -11.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.503× (z -8.9) |
| [[SHP-77 (line)]] | alt | 223 | 5 (4 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.85× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.74× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 128 | 4 (3 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.10× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.02× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -14.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-427 (line)]] | wt | 70.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 230 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 55.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.24× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Selinexor (drug)]] 0.5 µM 0.192× (z -10.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 364 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -12.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 53.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.87× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.50× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 131 | 3 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.9) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A-172 (line)]] | wt | 77.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 78.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.58× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Selinexor (drug)]] 5 µM 0.544× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H460 (line)]] | wt | 67.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 8.70× (z +20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.39× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 73.5 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.0) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A549 (line)]] | wt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.26× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[C32 (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.40× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[CHP-212 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.216× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 72.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 44.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +8.6) ⚠ cell-cycle shift, explains ~99% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 56.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.74× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SNU-1 (line)]] | wt | 235 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTBP]] | +0.84 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CENPK]] | +0.83 | +0.79 / +0.84 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[DTL]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 | pathway: DNA Damage Bypass; STRING 778 |
| [[POLQ]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |
| [[FANCD2]] | +0.81 | +0.78 / +0.81 | both halves | 7e-06 | STRING 526 |
| [[ZGRF1]] | +0.80 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[EXO1]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 908 |
| [[TOPBP1]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 785 |
| [[WDR76]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.80 | +0.80 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 726 |
| [[MMS22L]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FANCB]] | +0.80 | +0.80 / +0.84 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises RFC3's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.81× lower at baseline in the lines without CDC25A | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises RFC3's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.01× lower at baseline in the lines without E2F2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers RFC3's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF876P]] | B | ZNF876P activity raises RFC3's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without ZNF876P | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[ZNF695]] | B | ZNF695 activity raises RFC3's level | lines that do not express ZNF695 (10) vs lines expressing it (40) | 1.78× lower at baseline in the lines without ZNF695 | 0.099 | ⚠ within organs, on part of the lines |
| [[DSCC1]] | C | DSCC1 activity raises RFC3's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.59× lower at baseline in the lines without DSCC1 | 0.038 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises RFC3's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.97× lower at baseline in the lines without MCM10 | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[CENPP]] | C | CENPP activity raises RFC3's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without CENPP | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises RFC3's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 2.86× lower at baseline in the lines without DIAPH3, MELK | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.8, -47.3); signed map (-40.0, -42.8). **Vector** length 144, 47.8% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.63 to 23); *Activation of the pre-replicative complex* (reactome, mean cos +0.69 to 22); *Mitotic G1 phase and G1/S transition* (reactome, mean cos +0.66 to 34).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.3 | +5.1 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +4.2 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -9.7 | -4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.6 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.4 | -4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.0 | -3.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.4 | -3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[palbociclib (drug)]] 0.05 µM |  | -3.5 | -3.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -3.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | replication factor C subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.2 — chr13:33,818,069-33,966,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RFC38, MGC5276 |
| Gene groups (HGNC) | AAA ATPases; Replication factor C |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 59 pathways, smallest: Leading Strand Synthesis; Polymerase switching; Translesion synthesis by REV1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P40938](https://www.uniprot.org/uniprotkb/P40938) (Replication factor C subunit 3):

> Subunit of the replication factor C (RFC) complex which acts during elongation of primed DNA templates by DNA polymerases delta and epsilon, and is necessary for ATP-dependent loading of proliferating cell nuclear antigen (PCNA) onto primed DNA.

**Summary**, from NCBI Gene [5983](https://www.ncbi.nlm.nih.gov/gene/5983):

> The elongation of primed DNA templates by DNA polymerase delta and DNA polymerase epsilon requires the accessory proteins proliferating cell nuclear antigen (PCNA) and replication factor C (RFC). RFC, also named activator 1, is a protein complex consisting of five distinct subunits of 140, 40, 38, 37, and 36 kDa. This gene encodes the 38 kDa subunit. This subunit is essential for the interaction between the 140 kDa subunit and the core complex that consists of the 36, 37, and 40 kDa subunits. …

**Accessions** — [HGNC:9971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9971) · Entrez [5983](https://www.ncbi.nlm.nih.gov/gene/5983) · UniProt [P40938](https://www.uniprot.org/uniprotkb/P40938) · Ensembl [ENSG00000133119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133119)

## Data

Gene col 5421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5421); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5421]; `tensor/DDL_lfc|DDL_z.npy` [5421]; `embed/gene_vectors.npy` [5421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5421 or target_col == 5421). Every well: [[RFC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
