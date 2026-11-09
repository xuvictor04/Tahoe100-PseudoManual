---
symbol: "UBXN4"
type: "gene"
col: 6855
ensembl_id: "ENSG00000144224"
name: "UBX domain protein 4"
location: "2q21.3"
module: 64
arm: "+"
pooled_cpm: 227.11
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# UBXN4

*UBX domain protein 4* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +14.1, q 4e-42, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.84× (z +13.7, q 4e-40, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.513× (z -15.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRNP27]] (+0.73, fdr 2e-05), [[PPID]] (+0.72, fdr 1e-05), [[PSMD4]] (+0.72, fdr 7e-06); moves opposite to [[SMARCD2]] (-0.68, fdr 1e-05), [[COLGALT1]] (-0.63, fdr 1e-05), [[PODXL2]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GLB1L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.56×** | +14.1 | 4e-42 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +13.7 | 4e-40 | 47/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +11.9 | 3e-30 | 46/48 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +11.4 | 4e-28 | 46/48 (A-172, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +11.4 | 6e-28 | 45/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +10.8 | 3e-25 | 43/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +10.1 | 5e-22 | 42/49 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +8.9 | 3e-17 | 36/44 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +8.2 | 2e-14 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.2 | 2e-08 | 37/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +5.0 | 4e-05 | 30/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +4.3 | 6e-04 | 25/45 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.1 | 0.002 | 26/45 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.064 | 16/47 (A549, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | 1.15× | +3.1 | 0.072 | 20/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.1 | 0.075 | 13/48 (KATO III, HT-29, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.090 | 23/48 (Hs 766T, A498, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.513×** | -15.0 | 0e+00 | 47/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.522×** | -14.6 | 0e+00 | 48/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.565×** | -12.8 | 3e-35 | 46/48 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -8.2 | 3e-14 | 40/48 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.703×** | -7.9 | 2e-13 | 44/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.709×** | -7.7 | 1e-12 | 32/48 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.787×** | -5.4 | 6e-06 | 31/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -5.1 | 2e-05 | 31/49 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -4.8 | 1e-04 | 40/49 (HepG2/C3A, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.677×** | -4.6 | 3e-04 | 36/49 (C32, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.682×** | -4.5 | 3e-04 | 37/48 (C32, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.2 | 0.001 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.886× | -3.9 | 0.005 | 2/48 (SHP-77, SW 1271) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.890× | -3.7 | 0.009 | 18/49 (A549, AN3 CA, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.852× | -3.6 | 0.012 | 18/48 (SW1417, HT-29, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.036 | 4/48 (HCT15, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.877× | -2.9 | 0.085 | 15/48 (hTERT-HPNE, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 270 | 4 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.22× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -14.7) |
| [[SW480 (line)]] | alt | 259 | 7 (3 ⚠) | 4 | [[Ixazomib citrate (drug)]] 0.5 µM 1.94× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.568× (z -10.3) |
| [[A-172 (line)]] | wt | 315 | 7 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +16.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.22× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -13.5) |
| [[A549 (line)]] | wt | 197 | 6 (3 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +14.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.96× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -11.8) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.496× (z -11.4) |
| [[HOP62 (line)]] | alt | 192 | 7 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +18.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.20× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.514× (z -11.0) |
| [[LoVo (line)]] | wt | 235 | 5 (1 ⚠) | 5 | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.386× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 139 | 7 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +21.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.450× (z -12.3) |
| [[PANC-1 (line)]] | alt | 218 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +23.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +17.1) | — |
| [[COLO 205 (line)]] | alt | 236 | 6 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.95× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -11.6) |
| [[LS 180 (line)]] | wt | 229 | 6 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.12× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.398× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 259 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.74× (z +15.2) | — |
| [[HT-29 (line)]] | alt | 260 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +12.1) | [[Belinostat (drug)]] 5 µM 0.423× (z -13.2) |
| [[SNU-423 (line)]] | alt | 203 | 5 (2 ⚠) | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 2.04× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -13.2) |
| [[A498 (line)]] | wt | 313 | 4 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.91× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.500× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 218 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +17.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +12.3) | — |
| [[Panc 03.27 (line)]] | alt | 195 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.43× (z +13.5) | [[Lonafarnib (drug)]] 5 µM 0.0743× (z -20.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.452× (z -11.9) |
| [[H4 (line)]] | wt | 214 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.382× (z -11.4) |
| [[Hs 766T (line)]] | wt | 190 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.86× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.481× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 194 | 4 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +20.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.560× (z -9.1) |
| [[HS-578T (line)]] | alt | 170 | 3 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.94× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.92× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.526× (z -9.0) |
| [[KATO III (line)]] | alt | 186 | 2 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 1.88× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 208 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.13× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.464× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 348 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.85× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.460× (z -12.7) |
| [[C32 (line)]] | wt | 211 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.32× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 344 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 178 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.45× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 317 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.0) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 0.5 µM 0.481× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 230 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.91× (z +8.6) | — |
| [[RKO (line)]] | wt | 274 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.86× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 213 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.02× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 222 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -16.2) |
| [[NCI-H2347 (line)]] | alt | 153 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 1.89× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.524× (z -9.7) |
| [[SW1417 (line)]] | alt | 224 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.494× (z -10.4) |
| [[A-427 (line)]] | wt | 210 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 217 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.01× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.482× (z -10.5) |
| [[HCT15 (line)]] | alt | 285 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.02× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.488× (z -8.6) |
| [[SW48 (line)]] | wt | 218 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 266 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -8.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[J82 (line)]] | alt | 224 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.506× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 233 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 86.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 95.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 232 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 259 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 234 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP27]] | +0.73 | +0.85 / +0.46 | both halves | 2e-05 |  |
| [[PPID]] | +0.72 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[PSMD4]] | +0.72 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[RNF6]] | +0.69 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[MRPL45]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TSR2]] | +0.69 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[CLIP1]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[PSMD7]] | +0.68 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[CCDC117]] | +0.66 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[FCF1]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCD2]] | -0.68 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[COLGALT1]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[PODXL2]] | -0.62 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[SUMF2]] | -0.62 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[METAP1]] | -0.61 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[NHP2]] | -0.60 | -0.68 / -0.31 | both halves | 2e-04 |  |
| [[GLB1L2]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[MDH2]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[C20orf27]] | -0.58 | -0.66 / -0.38 | both halves | 6e-05 |  |
| [[MED14]] | -0.58 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[NFYA]] | -0.58 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLB1L2]] | B | GLB1L2 activity raises UBXN4's level | lines that do not express GLB1L2 (16) vs lines expressing it (34) | 1.23× lower at baseline in the lines without GLB1L2 | 0.078 | ⚠ within organs, on part of the lines; also absent: CHDH, PLS1, ASTL |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UBXN4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UBXN4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers UBXN4's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-19.7, 9.1); signed map (7.7, -29.9). **Vector** length 151, 57.1% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *proteasome* (control, mean cos +0.52 to 9); *Proteasome assembly* (reactome, mean cos +0.52 to 9); *G2/M Transition* (reactome, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +14.9 | +14.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +13.1 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.9 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.7 | +11.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.5 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.5 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.1 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.4 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.7 | -15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.3 | -14.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.8 | -12.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -4.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -4.0 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | UBX domain protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.3 — chr2:135,741,734-135,785,056 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0242; previously UBXDC1, UBXD2 |
| Gene groups (HGNC) | UBX domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92575](https://www.uniprot.org/uniprotkb/Q92575) (UBX domain-containing protein 4):

> Involved in endoplasmic reticulum-associated protein degradation (ERAD). Acts as a platform to recruit both UBQLN1 and VCP to the ER during ERAD.

**Summary**, from NCBI Gene [23190](https://www.ncbi.nlm.nih.gov/gene/23190):

> UBXD2 is an integral membrane protein of the endoplasmic reticulum (ER) that binds valosin-containing protein (VCP; MIM 601023) and promotes ER-associated protein degradation (ERAD) (Liang et al., 2006 [PubMed 16968747]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:14860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14860) · Entrez [23190](https://www.ncbi.nlm.nih.gov/gene/23190) · UniProt [Q92575](https://www.uniprot.org/uniprotkb/Q92575) · Ensembl [ENSG00000144224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144224)

## Data

Gene col 6855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6855); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6855]; `tensor/DDL_lfc|DDL_z.npy` [6855]; `embed/gene_vectors.npy` [6855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6855 or target_col == 6855). Every well: [[UBXN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBXN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
