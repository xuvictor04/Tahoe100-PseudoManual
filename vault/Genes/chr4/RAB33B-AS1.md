---
symbol: "RAB33B-AS1"
type: "gene"
col: 15771
ensembl_id: "ENSG00000273247"
name: "RAB33B antisense RNA 1"
location: "4q31.1"
module: 24
arm: "+"
pooled_cpm: 45.95
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 37
n_dd_up_clean: 4
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RAB33B-AS1

*RAB33B antisense RNA 1* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.50× (z +6.5, q 6e-08, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.456× (z -17.7, q 0e+00, down in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.379× (z -15.5, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD18]] (+0.62, fdr 7e-06), [[SCAMP2]] (+0.62, fdr 7e-06), [[FAU]] (+0.61, fdr 1e-05); moves opposite to [[PLCG1]] (-0.56, fdr 1e-05), [[IPO8]] (-0.55, fdr 1e-05), [[VARS1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC03041]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.50×** | +6.5 | 6e-08 | 35/49 (KATO III, SW480, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.70×** | +4.4 | 0.003 | 22/48 (SW480, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.27×** | +3.8 | 0.031 | 21/47 (LoVo, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.031 | 17/47 (SW 900, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.031 | 20/48 (J82, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.058 | 11/48 (HT-29, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.076 | 15/48 (NCI-H460, SW48, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.22× | +3.1 | 0.13 | 18/47 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.15 | 13/48 (LoVo, SNU-423, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15771.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.456×** | -17.7 | 0e+00 | 45/47 (H4, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.379×** | -15.5 | 0e+00 | 44/47 (HT-29, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -15.3 | 0e+00 | 47/48 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.430×** | -13.0 | 3e-36 | 38/47 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.448×** | -12.8 | 1e-35 | 42/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.504×** | -11.0 | 6e-26 | 41/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.275×** | -10.8 | 3e-25 | 42/49 (HT-29, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.526×** | -10.3 | 6e-23 | 39/48 (RPMI-7951, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.544×** | -9.7 | 1e-20 | 36/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.525×** | -9.5 | 9e-20 | 29/41 (LS 180, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.570×** | -9.0 | 2e-17 | 32/45 (HT-29, COLO 205, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.561×** | -8.9 | 3e-17 | 27/39 (HCT15, BT-474, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.366×** | -8.4 | 2e-15 | 41/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.620×** | -7.6 | 1e-12 | 35/48 (HOP62, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.631×** | -7.3 | 8e-12 | 32/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.759×** | -4.4 | 3e-04 | 26/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.636×** | -3.8 | 0.004 | 17/48 (HT-29, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.780×** | -3.7 | 0.005 | 18/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.787×** | -3.7 | 0.006 | 16/49 (SNU-423, PANC-1, …) | top dose only | plate-row cell shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.656×** | -3.5 | 0.009 | 17/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.672×** | -3.3 | 0.019 | 18/48 (HCT15, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.810×** | -3.2 | 0.030 | 19/47 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.807×** | -3.2 | 0.030 | 17/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 138 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0567× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -14.3) |
| [[HT-29 (line)]] | alt | 107 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -21.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -15.2) |
| [[SW480 (line)]] | alt | 47.3 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.289× (z -14.1) |
| [[PANC-1 (line)]] | alt | 40.4 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -18.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -13.4) |
| [[HOP62 (line)]] | alt | 51.8 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.293× (z -9.1) |
| [[H4 (line)]] | wt | 54.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -22.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.150× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 68.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.127× (z -10.0) |
| [[LoVo (line)]] | wt | 64.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.391× (z -10.0) |
| [[LS 180 (line)]] | wt | 64.6 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.157× (z -9.1) |
| [[A-427 (line)]] | wt | 40.0 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.270× (z -10.2) |
| [[A549 (line)]] | wt | 39.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -16.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -12.2) |
| [[KATO III (line)]] | alt | 82.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H1792 (line)]] | alt | 41.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -16.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 36.0 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.335× (z -10.6) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.396× (z -9.0) |
| [[A-172 (line)]] | wt | 40.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -15.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.304× (z -9.6) |
| [[COLO 205 (line)]] | alt | 95.8 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -15.0) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.181× (z -8.5) |
| [[HS-578T (line)]] | alt | 34.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -16.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.158× (z -12.7) |
| [[SNU-423 (line)]] | alt | 35.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.205× (z -11.0) |
| [[SW 900 (line)]] | alt | 39.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0741× (z -9.8) |
| [[A498 (line)]] | wt | 42.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -11.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 53.8 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.273× (z -9.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.309× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 53.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.271× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 70.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 27.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.227× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 39.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.254× (z -9.6) |
| [[BT-474 (line)]] | alt | 47.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0550× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[MIA PaCa-2 (line)]] | alt | 39.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.302× (z -8.8) |
| [[C-33 A (line)]] | alt | 64.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[Panc 03.27 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD18]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SCAMP2]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[FAU]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[POLR2J4]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 | same gene group |
| [[TPT1-AS1]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 | same gene group |
| [[STX5]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TULP3]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.55 | +0.56 / +0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TPT1]] | +0.55 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MUC20-OT1]] | +0.55 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MIF]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SF3B5]] ⚠ | +0.54 | +0.52 / +0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ETFDH]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SMBD1P]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCG1]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[IPO8]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[VARS1]] | -0.55 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[AADAT]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[AIFM1]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NEK6]] | -0.53 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[SEPTIN11]] | -0.53 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[RUVBL1]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[DHX9]] | -0.51 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TRAF5]] | -0.51 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[BTBD1]] | -0.51 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[PSMG1]] | -0.50 | -0.58 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03041]] | B | LINC03041 activity lowers RAB33B-AS1's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 1.55× higher at baseline in the lines without LINC03041 | 0.040 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.8, -29.0); signed map (-39.7, 10.9). **Vector** length 88.4, 24.8% of its response variance represented; |z| ≥ 3 in 1,264 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.9 | +6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.8 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.6 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.0 | -11.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | -0.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.8 | +2.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -8.3 | -8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -7.7 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.0 | -9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.7 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.6 | -17.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -2.7 | -0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | RAB33B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q31.1 — chr4:139,411,927-139,454,034 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55153) · Entrez [107984036](https://www.ncbi.nlm.nih.gov/gene/107984036) · Ensembl [ENSG00000273247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273247)

## Data

Gene col 15771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15771); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15771]; `tensor/DDL_lfc|DDL_z.npy` [15771]; `embed/gene_vectors.npy` [15771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15771 or target_col == 15771). Every well: [[RAB33B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB33B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
