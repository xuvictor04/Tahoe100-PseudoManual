---
symbol: "PTPN3"
type: "gene"
col: 940
ensembl_id: "ENSG00000070159"
name: "protein tyrosine phosphatase non-receptor type 3"
location: "9q31.3"
module: 23
arm: "-"
pooled_cpm: 69.39
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PTPN3

*protein tyrosine phosphatase non-receptor type 3* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.77× (z +12.0, q 3e-30, up in 43 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 0.05 µM in 2 lines (PANC-1 2.26×, NCI-H460 2.53×); [[Selinexor (drug)]] 0.5 µM in 1 line (PANC-1 2.02×; ⚠ cell-cycle shift, explains ~53% of this change).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.401× (z -25.3, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKS6]] (+0.58, fdr 4e-05), [[PPP2R2C]] (+0.55, fdr 4e-05), [[GJB3]] (+0.54, fdr 3e-05); moves opposite to [[ZCWPW2]] (-0.59, fdr 1e-05), [[MEF2C-AS1]] (-0.55, fdr 2e-05), [[GTF2IRD2]] (-0.53, fdr 2e-04).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC29A2]] → it (grade B ⚠); 13 go from it, the strongest it → [[KIAA1671]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 940.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 0.05 µM in 2 lines (PANC-1 2.26×, NCI-H460 2.53×); [[Selinexor (drug)]] 0.5 µM in 1 line (PANC-1 2.02×; ⚠ cell-cycle shift, explains ~53% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **1.77×** | +12.0 | 3e-30 | 43/46 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.53×** | +8.9 | 1e-16 | 40/45 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.27×** | +6.8 | 2e-09 | 22/45 (MIA PaCa-2, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.38×** | +6.7 | 3e-09 | 30/45 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.6 | 0.031 | 17/45 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +3.6 | 0.031 | 17/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.401×** | -25.3 | 0e+00 | 41/46 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.464×** | -21.1 | 0e+00 | 38/44 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.478×** | -15.5 | 0e+00 | 37/44 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.485×** | -15.2 | 0e+00 | 35/46 (A549, SW480, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.502×** | -14.4 | 6e-45 | 38/45 (SW480, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.523×** | -13.6 | 7e-40 | 39/45 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.508×** | -13.1 | 2e-37 | 34/41 (HCT15, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.541×** | -12.9 | 5e-36 | 36/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.561×** | -11.6 | 2e-29 | 29/39 (C-33 A, A-427, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.663×** | -8.3 | 8e-15 | 28/45 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.677×** | -8.2 | 2e-14 | 24/45 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -7.8 | 3e-13 | 26/45 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.696×** | -7.3 | 1e-11 | 28/45 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -7.2 | 2e-11 | 27/46 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.721×** | -6.8 | 3e-10 | 29/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.579×** | -6.0 | 8e-08 | 27/46 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -4.5 | 2e-04 | 21/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.667×** | -4.4 | 3e-04 | 19/45 (RKO, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.844× | -4.2 | 6e-04 | 17/45 (CFPAC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.863× | -3.8 | 0.003 | 20/45 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.847× | -3.5 | 0.013 | 16/46 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.845× | -3.4 | 0.017 | 15/45 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.860× | -3.1 | 0.035 | 14/46 (RKO, LS 180, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.038 | 11/45 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 276 | 0 | 15 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -20.2) |
| [[MIA PaCa-2 (line)]] | alt | 99.2 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0648× (z -33.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -19.2) |
| [[J82 (line)]] | alt | 79.5 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -16.7) |
| [[SW480 (line)]] | alt | 84.6 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -21.3) |
| [[NCI-H460 (line)]] | wt | 33.4 | 1 | 10 (8 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.53× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.315× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -17.8) |
| [[A549 (line)]] | wt | 101 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -22.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 71.1 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.139× (z -18.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -17.4) |
| [[LoVo (line)]] | wt | 63.2 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -22.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -11.9) |
| [[A498 (line)]] | wt | 74.8 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -23.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -18.7) |
| [[HOP62 (line)]] | alt | 51.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -16.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -14.9) |
| [[LS 180 (line)]] | wt | 150 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -10.3) |
| [[PANC-1 (line)]] | alt | 47.8 | 2 (1 ⚠) | 5 (3 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.26× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -15.9) |
| [[C32 (line)]] | wt | 48.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -20.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -17.6) |
| [[RKO (line)]] | wt | 82.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.272× (z -12.9) |
| [[SW48 (line)]] | wt | 95.8 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.238× (z -10.7) |
| [[HCT15 (line)]] | alt | 88.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0531× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 55.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -12.9) |
| [[SW1417 (line)]] | alt | 139 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.8) |
| [[A-172 (line)]] | wt | 51.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.272× (z -10.9) |
| [[COLO 205 (line)]] | alt | 84.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 30.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.255× (z -9.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H23 (line)]] | alt | 71.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -11.4) |
| [[SHP-77 (line)]] | alt | 78.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -11.5) |
| [[SW 900 (line)]] | alt | 36.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -11.0) |
| [[A-427 (line)]] | wt | 50.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 68.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -12.4) |
| [[C-33 A (line)]] | alt | 85.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -8.8) |
| [[HT-29 (line)]] | alt | 79.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -13.3) |
| [[KATO III (line)]] | alt | 70.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 56.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.4) |
| [[SNU-1 (line)]] | wt | 39.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -8.7) |
| [[SNU-423 (line)]] | alt | 43.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -15.0) |
| [[BT-474 (line)]] | alt | 63.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -15.3) |
| [[H4 (line)]] | wt | 33.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.209× (z -8.5) |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -9.5) |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 53.3 | 0 | 1 | — | [[Fusidic acid (drug)]] 0.5 µM 0.0550× (z -10.0) |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.66 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKS6]] | +0.58 | +0.66 / +0.40 | both halves | 4e-05 |  |
| [[PPP2R2C]] | +0.55 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[GJB3]] | +0.54 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[SLC29A1]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SLC29A2]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RGS19]] | +0.51 | +0.45 / +0.38 | both halves | 7e-05 | same gene group |
| [[FMNL2]] | +0.51 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PAQR5]] | +0.51 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[CKLF]] | +0.51 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[SNX10]] | +0.50 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[PROSER2]] | +0.50 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[SLCO4A1]] | +0.50 | +0.55 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCWPW2]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[MEF2C-AS1]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[GTF2IRD2]] | -0.53 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[ALOX12-AS1]] | -0.53 | -0.55 / -0.37 | both halves | 9e-05 |  |
| [[ZNF846]] | -0.51 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[CHD1-DT]] | -0.51 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[NAALADL2]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 | same gene group |
| [[TMEM91]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[B9D2]] | -0.49 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[TBCE-1]] | -0.49 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[PIPOX]] | -0.48 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[EFCAB6]] | -0.48 | -0.54 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC29A2]] | B | SLC29A2 activity raises PTPN3's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 2.27× lower at baseline in the lines without SLC29A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[SH2D3A]] | B | SH2D3A activity raises PTPN3's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.08× lower at baseline in the lines without SH2D3A | 0.079 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[BLACAT1]] | B | BLACAT1 activity raises PTPN3's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without BLACAT1 | 0.092 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[PBX4]] | C | PBX4 activity raises PTPN3's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 5.10× lower at baseline in the lines without PBX4 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561; co-absent with the target |
| [[KIAA1671]] | C | KIAA1671 activity raises PTPN3's level | lines that do not express KIAA1671 (3) vs lines expressing it (47) | 4.71× lower at baseline in the lines without KIAA1671 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: SOX13, FZD5, PDCD6P1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1671]] | C | PTPN3 activity raises KIAA1671's level | lines that do not express PTPN3 (3) vs lines expressing it (47) | 3.51× lower at baseline in the lines without PTPN3 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4; co-absent with the target |
| [[IPO9-AS1]] | C | PTPN3 activity lowers IPO9-AS1's level | lines that do not express PTPN3 (3) vs lines expressing it (47) | 2.11× higher at baseline in the lines without PTPN3 | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| cells under [[Carbamazepine (drug)]] 0.5 µM | C | PTPN3 activity raises the cells' numbers under Carbamazepine 0.5 µM (protects the cells) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 0.71× the cells of the other lines | 0.050 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | C | PTPN3 activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 0.75× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| cells under [[Methylthiouracil (drug)]] 0.05 µM | C | PTPN3 activity lowers the cells' numbers under Methylthiouracil 0.05 µM (makes them more sensitive) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 1.34× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | PTPN3 activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 0.71× the cells of the other lines | 0.063 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| cells under [[Omeprazole (drug)]] 0.05 µM | C | PTPN3 activity lowers the cells' numbers under Omeprazole 0.05 µM (makes them more sensitive) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 1.40× the cells of the other lines | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| [[PBX4]] | C | PTPN3 activity raises PBX4's level | lines that do not express PTPN3 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without PTPN3 | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4; co-absent with the target |
| cells under [[Imiquimod (hydrochloride) (drug)]] 0.05 µM | C | PTPN3 activity raises the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (protects the cells) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 0.73× the cells of the other lines | 0.074 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| cells under [[Peretinoin (drug)]] 5 µM | C | PTPN3 activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 0.72× the cells of the other lines | 0.079 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| cells under [[Pemetrexed (drug)]] 5 µM | C | PTPN3 activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 0.70× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| cells under [[Allopurinol (drug)]] 0.05 µM | C | PTPN3 activity lowers the cells' numbers under Allopurinol 0.05 µM (makes them more sensitive) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 1.34× the cells of the other lines | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (16.7, 3.8); signed map (-13.2, 43.4). **Vector** length 105, 30.4% of its response variance represented; |z| ≥ 3 in 1,295 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +6.8 | +6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +6.0 | +6.7 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.0 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +0.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.4 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.6 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -25.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -13.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -14.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -15.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.9 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:109,375,466-109,498,313 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTPH1 |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type; PDZ domain containing; FERM domain containing; MicroRNA protein coding host genes |
| Reactome | 7 pathways, smallest: EGFR downregulation; Negative regulation of MAPK pathway; Signaling by EGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [P26045](https://www.uniprot.org/uniprotkb/P26045) (Tyrosine-protein phosphatase non-receptor type 3):

> May act at junctions between the membrane and the cytoskeleton. Possesses tyrosine phosphatase activity.

**Summary**, from NCBI Gene [5774](https://www.ncbi.nlm.nih.gov/gene/5774):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This protein contains a C-terminal PTP domain and an N-terminal domain homologous to the band 4.1 superfamily of cytoskeletal-associated proteins. P97, a cell cycle regulator involved in a variety of membrane related functions, has …

**Accessions** — [HGNC:9655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9655) · Entrez [5774](https://www.ncbi.nlm.nih.gov/gene/5774) · UniProt [P26045](https://www.uniprot.org/uniprotkb/P26045) · Ensembl [ENSG00000070159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070159)

## Data

Gene col 940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 940); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 940]; `tensor/DDL_lfc|DDL_z.npy` [940]; `embed/gene_vectors.npy` [940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 940 or target_col == 940). Every well: [[PTPN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
