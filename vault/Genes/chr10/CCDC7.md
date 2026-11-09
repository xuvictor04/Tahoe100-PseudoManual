---
symbol: "CCDC7"
type: "gene"
col: 13283
ensembl_id: "ENSG00000216937"
name: "coiled-coil domain containing 7"
location: "10p11.22"
module: 10
arm: "+"
pooled_cpm: 52.75
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 62
n_dd_up_clean: 1
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CCDC7

*coiled-coil domain containing 7* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.32× (z +4.0, q 0.044, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 62 drug-doses (24 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.159× (z -26.1, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D32]] (+0.52, fdr 3e-05), [[CASC2]] (+0.52, fdr 2e-05), [[FGGY]] (+0.49, fdr 3e-05); moves opposite to [[LINC01169]] (-0.46, fdr 2e-04), [[BLACAT1]] (-0.45, fdr 1e-04), [[EPHX4]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CCDC102B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[EIF1B-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.044 | 23/46 (NCI-H1792, KATO III, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.28× | +3.4 | 0.18 | 17/45 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.26× | +3.3 | 0.18 | 20/46 (RKO, KATO III, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.27× | +3.2 | 0.18 | 11/46 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.2 | 0.18 | 11/46 (NCI-H23, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 24 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 62 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13283.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.159×** | -26.1 | 0e+00 | 46/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.163×** | -25.8 | 0e+00 | 44/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.364×** | -20.3 | 0e+00 | 42/46 (NCI-H1573, HS-578T, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.245×** | -19.9 | 0e+00 | 45/46 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.252×** | -19.6 | 0e+00 | 45/46 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.320×** | -16.2 | 0e+00 | 44/46 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.373×** | -13.5 | 2e-39 | 39/45 (HOP62, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.430×** | -12.0 | 3e-31 | 36/45 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.433×** | -11.9 | 9e-31 | 41/46 (PANC-1, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.432×** | -11.5 | 1e-28 | 34/44 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.433×** | -11.4 | 2e-28 | 38/46 (HOP62, PANC-1, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.466×** | -10.2 | 7e-23 | 38/46 (HEC-1-A, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.267×** | -9.8 | 5e-21 | 39/47 (HEC-1-A, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.280×** | -9.4 | 1e-19 | 38/45 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.516×** | -9.4 | 3e-19 | 41/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -8.1 | 2e-14 | 31/46 (HEC-1-A, COLO 205, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -6.5 | 2e-09 | 30/46 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.729×** | -6.3 | 6e-09 | 32/47 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -5.6 | 6e-07 | 29/46 (COLO 205, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.477×** | -5.5 | 8e-07 | 33/46 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.672×** | -5.5 | 9e-07 | 32/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 93.2 | 0 | 15 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -17.6) |
| [[PANC-1 (line)]] | alt | 57.9 | 0 | 15 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0731× (z -29.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -25.4) |
| [[A-427 (line)]] | wt | 73.8 | 0 | 14 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -19.6) |
| [[COLO 205 (line)]] | alt | 83.9 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -22.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.103× (z -19.5) |
| [[SW 900 (line)]] | alt | 65.5 | 0 | 13 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0861× (z -18.2) |
| [[A-172 (line)]] | wt | 113 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -18.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -13.6) |
| [[A549 (line)]] | wt | 57.6 | 0 | 12 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -15.7) |
| [[Hs 766T (line)]] | wt | 59.2 | 0 | 12 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 92.1 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -33.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0982× (z -21.0) |
| [[NCI-H23 (line)]] | alt | 107 | 0 | 12 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0704× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -20.2) |
| [[HOP62 (line)]] | alt | 52.9 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0717× (z -20.9) |
| [[HS-578T (line)]] | alt | 78.3 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -22.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0970× (z -17.7) |
| [[J82 (line)]] | alt | 43.7 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -19.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.143× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 50.4 | 0 | 11 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0773× (z -18.8) |
| [[RKO (line)]] | wt | 46.2 | 0 | 11 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -13.4) |
| [[LS 180 (line)]] | wt | 52.0 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0703× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.118× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 57.8 | 0 | 10 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.144× (z -15.0) |
| [[RPMI-7951 (line)]] | alt | 75.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -11.5) |
| [[H4 (line)]] | wt | 44.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -22.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0960× (z -13.5) |
| [[LoVo (line)]] | wt | 21.8 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -13.0) |
| [[A498 (line)]] | wt | 48.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -15.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.8) |
| [[C32 (line)]] | wt | 42.6 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -14.3) |
| [[HCT15 (line)]] | alt | 39.6 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0808× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 35.9 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0909× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0952× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 64.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -10.0) |
| [[HT-29 (line)]] | alt | 26.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.194× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 50.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -12.5) |
| [[BT-474 (line)]] | alt | 64.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -15.5) |
| [[C-33 A (line)]] | alt | 72.7 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0673× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.128× (z -14.6) |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.0747× (z -11.4) |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0552× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0712× (z -14.1) |
| [[SW480 (line)]] | alt | 18.3 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.281× (z -10.6) |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0747× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 48.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -12.8) |
| [[SNU-423 (line)]] | alt | 24.7 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 54.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change |
| [[SW48 (line)]] | wt | 28.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0463× (z -12.7) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -11.2) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 73.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0481× (z -9.1) |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0663× (z -8.8) |
| [[CHP-212 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D32]] | +0.52 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CASC2]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[FGGY]] | +0.49 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[LINC01473]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[HCCS-DT]] | +0.48 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[PRKN]] | +0.47 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SPATA17]] | +0.46 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[LINC01301]] | +0.45 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ZFHX3-AS1]] | +0.44 | +0.38 / +0.38 | both halves | 7e-05 |  |
| [[MYNN]] | +0.44 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[RAD51B]] | +0.43 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[LINC01572]] | +0.43 | +0.36 / +0.40 | both halves | 1e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01169]] | -0.46 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[BLACAT1]] | -0.45 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[EPHX4]] | -0.43 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[RRAS2]] | -0.43 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[CD58]] | -0.41 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[FBLIM1]] | -0.41 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[MFHAS1]] | -0.41 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[BACE2]] | -0.40 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[MAP7]] | -0.40 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[ARHGEF34P]] | -0.40 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[ZNF600]] | -0.40 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[INAVA]] | -0.40 | -0.35 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC102B]] | B | CCDC102B activity raises CCDC7's level | lines that do not express CCDC102B (9) vs lines expressing it (41) | 2.18× lower at baseline in the lines without CCDC102B | 0.008 | ⚠ within organs, on part of the lines; also absent: SMAD9, TTC28, ITGA10; maybe low, not absent |
| [[SPANXA2-OT1]] | B | SPANXA2-OT1 activity raises CCDC7's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without SPANXA2-OT1 | 0.031 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3 |
| [[STRIP2]] | B | STRIP2 activity lowers CCDC7's level | lines that do not express STRIP2 (6) vs lines expressing it (44) | 1.32× higher at baseline in the lines without STRIP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent |
| [[TMC3-AS1]] | C | TMC3-AS1 activity raises CCDC7's level | lines that do not express TMC3-AS1 (4) vs lines expressing it (46) | 1.75× lower at baseline in the lines without TMC3-AS1 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000243944, PAQR8, LINC01277; maybe low, not absent |
| [[SPATA17]] | C | SPATA17 activity raises CCDC7's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without SPATA17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |
| [[CCDC171]] | C | CCDC171 activity raises CCDC7's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 1.43× lower at baseline in the lines without CCDC171 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF1B-AS1]] | C | CCDC7's natural level strengthens EIF1B-AS1's drug response | CCDC7's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.45; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.236). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-26.4, 32.0); signed map (2.9, 5.4). **Vector** length 64.1, 17.2% of its response variance represented; |z| ≥ 3 in 1,553 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.0 | -11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | -4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.0 | -20.3 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +1.5 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.5 | -12.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.1 | +3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.1 | +0.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -10.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.1 | -11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | -3.8 | -6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -6.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.9 | -5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -11.9 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.22 — chr10:32,446,140-32,882,874 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32762, FLJ13031, BIOT2; previously C10orf68 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M83](https://www.uniprot.org/uniprotkb/Q96M83) (Coiled-coil domain-containing protein 7):

> May play a role in tumorigenesis.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26533) · Entrez [79741](https://www.ncbi.nlm.nih.gov/gene/79741) · UniProt [Q96M83](https://www.uniprot.org/uniprotkb/Q96M83) · Ensembl [ENSG00000216937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000216937)

## Data

Gene col 13283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13283); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13283]; `tensor/DDL_lfc|DDL_z.npy` [13283]; `embed/gene_vectors.npy` [13283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13283 or target_col == 13283). Every well: [[CCDC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
