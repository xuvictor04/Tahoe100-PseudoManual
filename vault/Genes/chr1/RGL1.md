---
symbol: "RGL1"
type: "gene"
col: 6719
ensembl_id: "ENSG00000143344"
name: "ral guanine nucleotide dissociation stimulator like 1"
location: "1q25.3"
module: 109
arm: "+"
pooled_cpm: 36.28
n_lines_expressing: 46
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 18
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# RGL1

*ral guanine nucleotide dissociation stimulator like 1* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 16.1× (z +53.9, q 0e+00, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.613× (z -9.5, q 1e-18, down in 28 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.668× (z -7.8, q 1e-12, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCUN1D3]] (+0.59, fdr 3e-05), [[PELO]] (+0.54, fdr 3e-05), [[LINC02832]] (+0.53, fdr 2e-05); moves opposite to [[PTPN9]] (-0.52, fdr 2e-05), [[CRTC3]] (-0.48, fdr 5e-05), [[ENTPD3-AS1]] (-0.47, fdr 3e-04).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PROX1]] → it (grade B ⚠); 2 go from it, the strongest it → [[MEIS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **16.1×** | +53.9 | 0e+00 | 43/44 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **10.5×** | +45.5 | 0e+00 | 42/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.89×** | +44.5 | 0e+00 | 42/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.98×** | +29.9 | 0e+00 | 40/44 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.18×** | +27.7 | 0e+00 | 41/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +20.0 | 0e+00 | 29/43 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **6.42×** | +18.9 | 0e+00 | 42/44 (NCI-H460, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.55×** | +18.2 | 0e+00 | 37/44 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +14.4 | 7e-45 | 27/44 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +13.4 | 5e-39 | 27/43 (J82, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +12.1 | 4e-32 | 36/42 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +8.0 | 4e-14 | 24/45 (A-172, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.4 | 6e-09 | 18/44 (NCI-H460, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.21×** | +5.2 | 7e-06 | 17/44 (RKO, NCI-H460, …) | top dose only | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +5.1 | 1e-05 | 15/42 (A-172, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.7 | 9e-05 | 17/44 (A-172, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -9.5 | 1e-18 | 28/42 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -7.8 | 1e-12 | 23/44 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.774×** | -7.0 | 4e-10 | 25/44 (SHP-77, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -6.3 | 5e-08 | 22/44 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.748×** | -5.6 | 2e-06 | 21/44 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.751×** | -5.5 | 3e-06 | 19/42 (Hs 766T, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.758×** | -5.4 | 6e-06 | 21/44 (NCI-H23, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.758×** | -5.3 | 1e-05 | 21/39 (HepG2/C3A, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.783×** | -4.7 | 1e-04 | 15/43 (SHP-77, NCI-H2030, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.4 | 5e-04 | 3/45 (NCI-H1792, C-33 A, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.728×** | -4.4 | 6e-04 | 13/43 (LS 180, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.804×** | -4.2 | 0.001 | 13/44 (C-33 A, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.809×** | -4.1 | 0.002 | 17/44 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.805×** | -4.1 | 0.002 | 17/42 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.800×** | -4.0 | 0.002 | 16/35 (HepG2/C3A, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.832×** | -3.5 | 0.017 | 10/43 (H4, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.020 | 12/43 (COLO 205, HepG2/C3A, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.834× | -3.4 | 0.022 | 10/44 (NCI-H2030, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.039 | 19/44 (SW480, PANC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.731×** | -3.2 | 0.042 | 8/41 (C32, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.855× | -3.0 | 0.063 | 9/44 (PANC-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 35.7 | 10 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 17.8× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 15.4 | 11 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 49.5× (z +27.5) | — |
| [[HepG2_C3A (line)]] | wt | 372 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0632× (z -19.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -19.0) |
| [[J82 (line)]] | alt | 34.1 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +24.8) | — |
| [[Hs 766T (line)]] | wt | 62.9 | 7 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 13.7× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 0.324× (z -8.6) |
| [[RKO (line)]] | wt | 38.4 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +18.9) | — |
| [[SW480 (line)]] | alt | 159 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.247× (z -9.9) |
| [[A498 (line)]] | wt | 26.0 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +22.9) | — |
| [[LoVo (line)]] | wt | 18.5 | 8 | 0 | [[Belinostat (drug)]] 5 µM 19.2× (z +21.1) | — |
| [[A549 (line)]] | wt | 9.11 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 43.7× (z +17.8) | — |
| [[C32 (line)]] | wt | 26.4 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 16.5× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 22.0 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 19.2× (z +20.3) | — |
| [[hTERT-HPNE (line)]] | wt | 48.0 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.1× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.0472× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 56.3 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.75× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 38.7× (z +19.9) | — |
| [[SW1417 (line)]] | alt | 29.6 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.4× (z +15.6) | [[Digitoxin (drug)]] 5 µM 0.263× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -8.5) |
| [[HOP62 (line)]] | alt | 14.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 37.1× (z +22.7) | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 36.3× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 17.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 15.7× (z +21.3) | — |
| [[SHP-77 (line)]] | alt | 98.6 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.08× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0933× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -8.5) |
| [[SNU-423 (line)]] | alt | 17.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 30.1× (z +19.0) | — |
| [[SW 900 (line)]] | alt | 78.6 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.70× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 9.78 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 13.3× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 26.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 19.3× (z +19.7) | — |
| [[KATO III (line)]] | alt | 13.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 29.0× (z +18.7) | — |
| [[LS 180 (line)]] | wt | 20.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 11.1× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 23.4× (z +16.7) | — |
| [[NCI-H23 (line)]] | alt | 21.7 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.01× (z +15.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.239× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 54.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.72× (z +17.6) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.1× (z +18.4) | — |
| [[COLO 205 (line)]] | alt | 20.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 19.5× (z +14.7) | — |
| [[HCT15 (line)]] | alt | 12.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 19.1× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.0950× (z -8.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 9.92 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 23.6× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 18.3× (z +17.3) | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 17.6× (z +16.3) | — |
| [[AsPC-1 (line)]] | alt | 15.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 21.6× (z +16.4) | — |
| [[C-33 A (line)]] | alt | 37.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +16.0) | — |
| [[H4 (line)]] | wt | 50.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.5× (z +16.2) | — |
| [[SW48 (line)]] | wt | 13.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 20.9× (z +10.7) | — |
| [[CHP-212 (line)]] | wt | 325 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0956× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D3]] | +0.59 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[PELO]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[LINC02832]] | +0.53 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[LINC00460]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PDGFB]] | +0.51 | +0.44 / +0.40 | both halves | 5e-05 | pathway: MAPK family signaling cascades |
| [[ISM1]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ITGA1]] | +0.50 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RORB]] | +0.50 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[IGFL4]] | +0.50 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[VSIG1]] | +0.49 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[MAML2]] | +0.49 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[NFKBIE]] | +0.49 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN9]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CRTC3]] | -0.48 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ENTPD3-AS1]] | -0.47 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[VAX2]] | -0.46 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[POU6F1]] | -0.45 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[PHF2]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ECPAS]] | -0.45 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[ZNF460-AS1]] | -0.43 | -0.32 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROX1]] | B | PROX1 activity raises RGL1's level | lines that do not express PROX1 (30) vs lines expressing it (20) | 2.28× lower at baseline in the lines without PROX1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[RIMBP2]] | B | RIMBP2 activity raises RGL1's level | lines that do not express RIMBP2 (31) vs lines expressing it (19) | 1.55× lower at baseline in the lines without RIMBP2 | 0.090 | ⚠ within organs, on part of the lines; also absent: SNTG1, ST18, RUNX1T1; maybe low, not absent |
| [[ISM1]] | C | ISM1's natural level weakens RGL1's drug response | ISM1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.55; direction not clear | 0.096 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEIS1]] | C | RGL1 activity raises MEIS1's level | lines that do not express RGL1 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without RGL1 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01138, CDK6, IGF2BP3; maybe low, not absent |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | RGL1's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | RGL1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.60 | 0.511 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.426). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, 3.1); signed map (9.3, 38.0). **Vector** length 91.1, 21.9% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.6 | +29.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.0 | +18.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.1 | +8.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.3 | +27.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +20.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +18.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +4.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -4.5 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | +0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | ral guanine nucleotide dissociation stimulator like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:183,636,085-183,928,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RGL |
| Gene groups (HGNC) | Ral guanine nucleotide dissociation stimulator family |
| Reactome | 6 pathways, smallest: PPARA activates gene expression; Regulation of lipid metabolism by PPARalpha; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZL6](https://www.uniprot.org/uniprotkb/Q9NZL6) (Ral guanine nucleotide dissociation stimulator-like 1):

> Probable guanine nucleotide exchange factor.

**Summary**, from NCBI Gene [23179](https://www.ncbi.nlm.nih.gov/gene/23179):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in Ras protein signal transduction. Predicted to be located in cytosol. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30281) · Entrez [23179](https://www.ncbi.nlm.nih.gov/gene/23179) · UniProt [Q9NZL6](https://www.uniprot.org/uniprotkb/Q9NZL6) · Ensembl [ENSG00000143344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143344)

## Data

Gene col 6719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6719); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6719]; `tensor/DDL_lfc|DDL_z.npy` [6719]; `embed/gene_vectors.npy` [6719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6719 or target_col == 6719). Every well: [[RGL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
