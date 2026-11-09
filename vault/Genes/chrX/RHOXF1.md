---
symbol: "RHOXF1"
type: "gene"
col: 2185
ensembl_id: "ENSG00000101883"
name: "Rhox homeobox family member 1"
location: "Xq24"
module: 45
arm: "+"
pooled_cpm: 28.05
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 58
n_dd_up_clean: 14
n_dd_down_clean: 41
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# RHOXF1

*Rhox homeobox family member 1* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.76× (z +8.5, q 8e-15, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 58 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.296× (z -25.9, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNRC6A]] (+0.65, fdr 7e-06), [[THRA]] (+0.64, fdr 1e-05), [[MED30]] (+0.63, fdr 8e-06); moves opposite to [[MICALL1]] (-0.66, fdr 7e-06), [[CLCF1]] (-0.59, fdr 1e-05), [[GATAD2A]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +8.5 | 8e-15 | 35/47 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +7.2 | 2e-10 | 32/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +6.3 | 5e-08 | 29/46 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 1e-04 | 21/47 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +4.6 | 5e-04 | 24/46 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 0.001 | 20/47 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.006 | 19/47 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.9 | 0.006 | 19/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.012 | 17/47 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.013 | 16/47 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.022 | 16/47 (PANC-1, HOP62, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.028 | 13/47 (AsPC-1, HT-29, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.25×** | +3.4 | 0.028 | 14/47 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.031 | 16/46 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.031 | 10/46 (NCI-H1573, SW 900, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.046 | 14/46 (LS 180, NCI-H23, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.046 | 8/47 (NCI-H460, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 58 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.296×** | -25.9 | 0e+00 | 41/46 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.339×** | -16.3 | 0e+00 | 37/46 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.370×** | -14.9 | 0e+00 | 46/47 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.508×** | -14.4 | 1e-44 | 35/47 (COLO 205, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.391×** | -13.5 | 1e-39 | 38/46 (A549, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.428×** | -12.7 | 4e-35 | 33/45 (NCI-H1573, SNU-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.420×** | -12.5 | 5e-34 | 37/45 (COLO 205, HCT15, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.461×** | -11.6 | 3e-29 | 44/46 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.463×** | -11.5 | 5e-29 | 34/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.449×** | -11.4 | 4e-28 | 41/47 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.476×** | -11.1 | 5e-27 | 41/47 (PANC-1, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.487×** | -10.8 | 2e-25 | 31/44 (COLO 205, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.509×** | -9.4 | 4e-19 | 28/39 (NCI-H460, HCT15, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.526×** | -9.3 | 8e-19 | 33/46 (CHP-212, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.542×** | -9.2 | 2e-18 | 32/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -8.1 | 2e-14 | 34/47 (H4, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[EX229 (drug)]] 5 µM |  | **0.351×** | -7.9 | 1e-13 | 31/47 (A498, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.699×** | -7.6 | 1e-12 | 37/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.369×** | -7.5 | 2e-12 | 35/46 (RPMI-7951, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.374×** | -7.4 | 4e-12 | 31/46 (PANC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.379×** | -7.3 | 7e-12 | 35/47 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.382×** | -7.2 | 1e-11 | 26/47 (LoVo, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.6 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -23.2) |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 1 (1 ⚠) | 13 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.57× (z +10.2) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -14.5) |
| [[PANC-1 (line)]] | alt | 24.7 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -24.5) |
| [[NCI-H1573 (line)]] | alt | 49.3 | 0 | 13 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0514× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.127× (z -24.1) |
| [[HCT15 (line)]] | alt | 95.6 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.1) |
| [[COLO 205 (line)]] | alt | 67.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0850× (z -25.5) |
| [[A498 (line)]] | wt | 38.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -28.0) |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0416× (z -27.8) |
| [[H4 (line)]] | wt | 40.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -19.7) |
| [[HT-29 (line)]] | alt | 30.1 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -12.1) |
| [[LoVo (line)]] | wt | 37.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.2) |
| [[NCI-H23 (line)]] | alt | 53.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -13.6) |
| [[SW480 (line)]] | alt | 33.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -15.6) |
| [[A549 (line)]] | wt | 35.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0802× (z -26.0) |
| [[CFPAC-1 (line)]] | alt | 31.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -21.7) |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0851× (z -14.8) |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0503× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.144× (z -11.0) |
| [[C32 (line)]] | wt | 20.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Silodosin (drug)]] 5 µM 0.189× (z -9.7) |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0933× (z -24.8) |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0281× (z -20.0) |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -18.6) |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.4) |
| [[A-172 (line)]] | wt | 9.62 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.0) |
| [[C-33 A (line)]] | alt | 40.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 26.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -10.5) |
| [[J82 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.4) |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.5) |
| [[A-427 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -8.9) |
| [[BT-474 (line)]] | alt | 7.97 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.115× (z -8.6) |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0631× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -8.8) |
| [[KATO III (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 42.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -13.0) |
| [[RKO (line)]] | wt | 7.47 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0721× (z -9.0) |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.8) |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -9.6) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6A]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[THRA]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[MED30]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[MBIP]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ACACB]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[AUH]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[IFT172]] | +0.61 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[BTN3A2]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CTDSPL2]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PEX2]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICALL1]] | -0.66 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[CLCF1]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.59 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[C11orf91]] | -0.59 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[STK10]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CAPN2]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[DESI1]] | -0.55 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TECPR2]] | -0.55 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[TBILA]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZNF710]] | -0.54 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers RHOXF1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[HOXA3]] | B | HOXA3 activity raises RHOXF1's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without HOXA3 | 0.083 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[MAP2K6]] | B | MAP2K6 activity raises RHOXF1's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without MAP2K6 | 0.086 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (17.7, -11.0); signed map (-27.3, -8.6). **Vector** length 85.5, 23.5% of its response variance represented; |z| ≥ 3 in 1,578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +8.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.9 | +7.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +2.9 | -12.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.7 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -14.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -14.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.8 | -6.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.6 | -6.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.4 | -7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -7.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.6 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | Rhox homeobox family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:120,109,051-120,245,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OTEX, PEPP1 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHV9](https://www.uniprot.org/uniprotkb/Q8NHV9) (Rhox homeobox family member 1):

> Transcription factor maybe involved in reproductive processes. Modulates expression of target genes encoding proteins involved in processes relevant to spermatogenesis.

**Summary**, from NCBI Gene [158800](https://www.ncbi.nlm.nih.gov/gene/158800):

> This gene is a member of the PEPP subfamily of paired-like homoebox genes. The gene may be regulated by androgens and epigenetic mechanisms. The encoded nuclear protein is likely a transcription factor that may play a role in human reproduction. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:29993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29993) · Entrez [158800](https://www.ncbi.nlm.nih.gov/gene/158800) · UniProt [Q8NHV9](https://www.uniprot.org/uniprotkb/Q8NHV9) · Ensembl [ENSG00000101883](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101883)

## Data

Gene col 2185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2185); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2185]; `tensor/DDL_lfc|DDL_z.npy` [2185]; `embed/gene_vectors.npy` [2185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2185 or target_col == 2185). Every well: [[RHOXF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHOXF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
