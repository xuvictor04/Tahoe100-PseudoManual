---
symbol: "HGSNAT"
type: "gene"
col: 9067
ensembl_id: "ENSG00000165102"
name: "heparan-alpha-glucosaminide N-acetyltransferase"
location: "8p11.21-p11.1"
module: 15
arm: "+"
pooled_cpm: 56.11
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 38
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# HGSNAT

*heparan-alpha-glucosaminide N-acetyltransferase* — 8p11.21-p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.51× (z +5.5, q 2e-05, up in 33 of 46 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 1.24× (z +4.1, q 0.012, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (18 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.308× (z -16.0, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TECPR2]] (+0.69, fdr 1e-05), [[RXYLT1]] (+0.59, fdr 3e-05), [[ACTR3B]] (+0.58, fdr 2e-05); moves opposite to [[MAPRE2]] (-0.55, fdr 1e-05), [[GALM]] (-0.55, fdr 3e-05), [[THRA]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RNF128]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +5.5 | 2e-05 | 33/46 (A-427, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.012 | 22/47 (A-427, A498, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.037 | 18/47 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.051 | 23/46 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.19 | 20/47 (COLO 205, SNU-1, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.23 | 16/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.308×** | -16.0 | 0e+00 | 42/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.436×** | -15.9 | 0e+00 | 45/47 (NCI-H1573, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.332×** | -15.0 | 0e+00 | 45/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.333×** | -15.0 | 0e+00 | 44/47 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.339×** | -14.7 | 0e+00 | 46/47 (LoVo, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.351×** | -14.2 | 5e-44 | 43/47 (H4, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.296×** | -12.7 | 4e-35 | 47/47 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.410×** | -11.7 | 2e-29 | 42/47 (A549, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.475×** | -10.1 | 3e-22 | 42/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -9.5 | 2e-19 | 34/47 (H4, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.492×** | -9.3 | 1e-18 | 40/46 (BT-474, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.558×** | -7.9 | 1e-13 | 33/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.335×** | -7.8 | 3e-13 | 39/47 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.482×** | -7.6 | 1e-12 | 39/47 (J82, H4, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.348×** | -7.5 | 2e-12 | 41/48 (A549, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.573×** | -7.1 | 4e-11 | 36/47 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.599×** | -6.9 | 1e-10 | 36/47 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.559×** | -6.1 | 4e-08 | 38/47 (SW48, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.593×** | -3.7 | 0.005 | 23/48 (A549, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.604×** | -3.6 | 0.007 | 24/47 (SHP-77, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -3.4 | 0.013 | 20/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.776×** | -3.2 | 0.023 | 18/47 (PANC-1, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 74.0 | 0 | 17 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -14.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.202× (z -14.2) |
| [[H4 (line)]] | wt | 85.2 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -19.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -16.4) |
| [[LoVo (line)]] | wt | 74.4 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.232× (z -14.9) |
| [[A549 (line)]] | wt | 126 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -19.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.187× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 65.8 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -14.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -12.0) |
| [[HOP62 (line)]] | alt | 98.4 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 50.2 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.206× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 80.9 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.211× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 86.5 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -22.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -14.9) |
| [[LS 180 (line)]] | wt | 58.0 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.226× (z -9.4) |
| [[PANC-1 (line)]] | alt | 26.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -17.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -10.2) |
| [[SW480 (line)]] | alt | 26.2 | 0 | 8 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.205× (z -13.8) |
| [[HS-578T (line)]] | alt | 75.2 | 0 | 7 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.226× (z -11.5) |
| [[J82 (line)]] | alt | 64.5 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -12.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.270× (z -10.3) |
| [[A-172 (line)]] | wt | 114 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.333× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 57.1 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -14.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.134× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 48.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -18.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -10.5) |
| [[KATO III (line)]] | alt | 41.5 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.275× (z -10.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 54.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -15.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.293× (z -11.7) |
| [[RKO (line)]] | wt | 72.4 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0782× (z -19.5) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.246× (z -11.2) |
| [[SNU-423 (line)]] | alt | 37.1 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.175× (z -12.8) |
| [[A498 (line)]] | wt | 57.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -9.5) |
| [[HCT15 (line)]] | alt | 51.3 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 58.3 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.304× (z -8.6) |
| [[SHP-77 (line)]] | alt | 54.3 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.240× (z -11.3) |
| [[SW 900 (line)]] | alt | 44.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -12.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.287× (z -8.8) |
| [[C-33 A (line)]] | alt | 74.3 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.230× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 49.3 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.234× (z -10.9) |
| [[SW48 (line)]] | wt | 76.7 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.198× (z -10.1) |
| [[A-427 (line)]] | wt | 61.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 47.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 21.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -14.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.213× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.243× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 45.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -12.2) |
| [[AN3 CA (line)]] | alt | 58.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.131× (z -9.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[BT-474 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[CFPAC-1 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 46.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.266× (z -8.8) |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.157× (z -9.8) |
| [[SW1417 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -13.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TECPR2]] | +0.69 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[RXYLT1]] | +0.59 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ACTR3B]] | +0.58 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[PPP3CB]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[FAM86HP]] | +0.56 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ITCH]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[GATD1-DT]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[KLHL22]] | +0.56 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[LTO1]] | +0.56 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TLNRD1]] | +0.55 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[LCA5L]] | +0.55 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[ING2-DT]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE2]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[GALM]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 | pathway: Diseases of metabolism |
| [[THRA]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[RAB20]] | -0.53 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[NIPSNAP1]] | -0.51 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[SEPTIN6]] | -0.49 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[FAM234B]] | -0.49 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[PNKD]] | -0.49 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[RHOXF1]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[FOS]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PIK3C2B]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NCKAP5L]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF128]] | B | RNF128 activity lowers HGSNAT's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.44× higher at baseline in the lines without RNF128 | 0.088 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (16.5, 0.4); signed map (12.9, 0.1). **Vector** length 75.9, 22.8% of its response variance represented; |z| ≥ 3 in 1,402 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +0.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.7 | -0.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.6 | +3.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -16.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -6.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.7 | -2.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -6.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Allopurinol (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | heparan-alpha-glucosaminide N-acetyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21-p11.1 — chr8:43,140,464-43,202,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32731, HGNAT; previously TMEM76 |
| Gene groups (HGNC) | Acyltransferases |
| Reactome | 9 pathways, smallest: Mucopolysaccharidoses; HS-GAG degradation; Diseases of carbohydrate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68CP4](https://www.uniprot.org/uniprotkb/Q68CP4) (Heparan-alpha-glucosaminide N-acetyltransferase):

> Lysosomal acetyltransferase that acetylates the non-reducing terminal alpha-glucosamine residue of intralysosomal heparin or heparan sulfate, converting it into a substrate for luminal alpha-N-acetyl glucosaminidase.

**Summary**, from NCBI Gene [138050](https://www.ncbi.nlm.nih.gov/gene/138050):

> This gene encodes a lysosomal acetyltransferase, which is one of several enzymes involved in the lysosomal degradation of heparin sulfate. Mutations in this gene are associated with Sanfilippo syndrome C, one type of the lysosomal storage disease mucopolysaccaridosis III, which results from impaired degradation of heparan sulfate. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:26527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26527) · Entrez [138050](https://www.ncbi.nlm.nih.gov/gene/138050) · UniProt [Q68CP4](https://www.uniprot.org/uniprotkb/Q68CP4) · Ensembl [ENSG00000165102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165102)

## Data

Gene col 9067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9067); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9067]; `tensor/DDL_lfc|DDL_z.npy` [9067]; `embed/gene_vectors.npy` [9067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9067 or target_col == 9067). Every well: [[HGSNAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HGSNAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
