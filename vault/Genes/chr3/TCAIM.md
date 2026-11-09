---
symbol: "TCAIM"
type: "gene"
col: 11006
ensembl_id: "ENSG00000179152"
name: "T cell activation inhibitor, mitochondrial"
location: "3p21.31"
module: 62
arm: "+"
pooled_cpm: 41.25
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# TCAIM

*T cell activation inhibitor, mitochondrial* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +7.1, q 6e-10, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.490× (z -16.8, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.261× (z -11.7, q 1e-29, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANXA4]] (+0.59, fdr 3e-05), [[BORCS7-ASMT]] (+0.57, fdr 2e-05), [[SESN1]] (+0.55, fdr 3e-05); moves opposite to [[NCKAP5L]] (-0.46, fdr 1e-04), [[LMCD1-AS1]] (-0.46, fdr 3e-04), [[TRA2B]] (-0.45, fdr 9e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.1 | 6e-10 | 32/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +5.0 | 1e-04 | 33/48 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +4.5 | 0.001 | 22/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +4.5 | 0.001 | 21/48 (A-172, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.008 | 21/48 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.26×** | +3.9 | 0.008 | 18/48 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.008 | 19/48 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.008 | 19/47 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.009 | 17/49 (HEC-1-A, HepG2/C3A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.010 | 15/48 (SW480, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +3.7 | 0.010 | 22/48 (RKO, NCI-H460, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +3.7 | 0.010 | 21/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.014 | 16/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.018 | 19/47 (SW480, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.20× | +3.4 | 0.022 | 18/48 (C-33 A, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.022 | 17/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.028 | 12/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.036 | 13/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11006.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.490×** | -16.8 | 0e+00 | 42/48 (SNU-423, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.458×** | -13.0 | 3e-36 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.461×** | -12.9 | 6e-36 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.261×** | -11.7 | 1e-29 | 45/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -10.8 | 6e-25 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.532×** | -10.5 | 8e-24 | 41/48 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.325×** | -9.8 | 1e-20 | 40/48 (HEC-1-A, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.586×** | -8.9 | 4e-17 | 35/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.593×** | -8.7 | 2e-16 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.601×** | -8.5 | 1e-15 | 38/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.601×** | -8.2 | 2e-14 | 34/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.661×** | -6.6 | 1e-09 | 32/47 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.688×** | -5.9 | 2e-07 | 35/48 (CHP-212, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.517×** | -5.7 | 4e-07 | 20/35 (LOX-IMVI, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.709×** | -5.7 | 4e-07 | 29/48 (AN3 CA, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.751×** | -4.8 | 6e-05 | 27/48 (NCI-H661, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.791×** | -3.9 | 0.003 | 18/48 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.722×** | -3.9 | 0.003 | 16/48 (C-33 A, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.831×** | -3.0 | 0.077 | 11/48 (CFPAC-1, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Silodosin (drug)]] 5 µM |  | **0.832×** | -2.9 | 0.081 | 19/46 (RPMI-7951, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 39.0 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.316× (z -12.4) |
| [[SW480 (line)]] | alt | 43.8 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -15.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.313× (z -13.1) |
| [[LS 180 (line)]] | wt | 81.6 | 4 (2 ⚠) | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.6) | [[TAK-901 (drug)]] 5 µM 0.168× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 39.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.335× (z -9.0) |
| [[KATO III (line)]] | alt | 51.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.382× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 39.7 | 3 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 55.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -11.6) |
| [[SNU-423 (line)]] | alt | 52.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 89.1 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.122× (z -11.7) |
| [[Hs 766T (line)]] | wt | 41.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LOX-IMVI (line)]] | wt | 37.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 40.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.6) ⚠ cell-cycle shift, explains ~1% of this change | [[Digitoxin (drug)]] 5 µM 0.310× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 30.2 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 80.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HS-578T (line)]] | alt | 34.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -8.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 49.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.372× (z -8.5) |
| [[SW 900 (line)]] | alt | 30.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 47.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.109× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[C-33 A (line)]] | alt | 71.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.333× (z -8.5) |
| [[C32 (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[COLO 205 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HT-29 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -11.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H1792 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW48 (line)]] | wt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA4]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[BORCS7-ASMT]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[SESN1]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TNFSF13B]] | +0.55 | +0.64 / +0.37 | both halves | 7e-05 |  |
| [[DCP1B]] | +0.54 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[ACTA2]] | +0.54 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[DARS1-AS1]] | +0.54 | +0.64 / +0.30 | both halves | 2e-04 |  |
| [[TMEM68]] | +0.54 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[LVRN]] | +0.54 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[DDB2]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[KLRD1]] | +0.53 | +0.65 / +0.35 | both halves | 1e-04 |  |
| [[FAM185A]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP5L]] | -0.46 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[LMCD1-AS1]] | -0.46 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[TRA2B]] | -0.45 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[MAP3K14]] | -0.45 | -0.41 / -0.24 | both halves | 4e-04 |  |
| [[OAF]] | -0.45 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[DGKD]] | -0.44 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[HIVEP3]] | -0.44 | -0.41 / -0.23 | both halves | 5e-04 |  |
| [[AFAP1]] | -0.44 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[OSBPL5]] | -0.43 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[RNFT2]] | -0.43 | -0.41 / -0.16 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TCAIM's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.2, 33.5); signed map (40.7, -26.4). **Vector** length 73.0, 17.3% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +3.3 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +3.1 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +3.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.0 | -16.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.6 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -8.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | T cell activation inhibitor, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:44,338,119-44,409,451 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313N0621, TOAG-1; previously C3orf23 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3R3](https://www.uniprot.org/uniprotkb/Q8N3R3) (T-cell activation inhibitor, mitochondrial):

> May regulate T-cell apoptosis.

**Summary**, from NCBI Gene [285343](https://www.ncbi.nlm.nih.gov/gene/285343):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25241) · Entrez [285343](https://www.ncbi.nlm.nih.gov/gene/285343) · UniProt [Q8N3R3](https://www.uniprot.org/uniprotkb/Q8N3R3) · Ensembl [ENSG00000179152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179152)

## Data

Gene col 11006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11006); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11006]; `tensor/DDL_lfc|DDL_z.npy` [11006]; `embed/gene_vectors.npy` [11006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11006 or target_col == 11006). Every well: [[TCAIM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCAIM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
