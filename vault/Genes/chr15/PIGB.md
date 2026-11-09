---
symbol: "PIGB"
type: "gene"
col: 929
ensembl_id: "ENSG00000069943"
name: "phosphatidylinositol glycan anchor biosynthesis class B"
location: "15q21.3"
module: 64
arm: "+"
pooled_cpm: 22.81
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PIGB

*phosphatidylinositol glycan anchor biosynthesis class B* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.33× (z +6.1, q 7e-07, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~83% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.71× (z +4.3, q 0.004, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.334× (z -23.5, q 0e+00, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.457× (z -16.8, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMLHE]] (+0.73, fdr 7e-06), [[EFCAB7]] (+0.72, fdr 7e-06), [[DYNC2LI1]] (+0.68, fdr 7e-06); moves opposite to [[KLF13]] (-0.58, fdr 4e-05), [[KLF12]] (-0.56, fdr 1e-05), [[DDX5]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.33×** | +6.1 | 7e-07 | 24/48 (RKO, LoVo, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +4.3 | 0.004 | 19/48 (RKO, HT-29, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.71×** | +4.3 | 0.004 | 19/46 (HT-29, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.035 | 14/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.23× | +3.2 | 0.17 | 11/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.18 | 11/48 (LS 180, A549, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.334×** | -23.5 | 0e+00 | 43/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.457×** | -16.8 | 0e+00 | 41/47 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.348×** | -16.0 | 0e+00 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.356×** | -15.7 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.396×** | -14.0 | 1e-42 | 45/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.398×** | -14.0 | 2e-42 | 44/47 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.416×** | -13.3 | 2e-38 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.425×** | -13.0 | 1e-36 | 43/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.438×** | -12.0 | 1e-31 | 39/44 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.476×** | -11.2 | 1e-27 | 38/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.471×** | -11.0 | 2e-26 | 42/47 (PANC-1, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.500×** | -10.5 | 4e-24 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.551×** | -8.7 | 2e-16 | 31/47 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.586×** | -7.5 | 3e-12 | 21/35 (PANC-1, HEC-1-A, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.628×** | -7.1 | 6e-11 | 35/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.636×** | -6.9 | 2e-10 | 34/45 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -6.5 | 3e-09 | 28/47 (SNU-423, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -6.4 | 4e-09 | 31/48 (PANC-1, MIA PaCa-2, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.517×** | -5.2 | 4e-06 | 22/45 (MIA PaCa-2, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.788×** | -5.1 | 8e-06 | 26/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -4.7 | 6e-05 | 22/47 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.591×** | -4.2 | 6e-04 | 18/48 (SNU-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.787×** | -3.6 | 0.005 | 13/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.783×** | -3.6 | 0.007 | 14/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.793×** | -3.5 | 0.008 | 14/46 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 15 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.238× (z -12.4) |
| [[PANC-1 (line)]] | alt | 32.7 | 0 | 13 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -21.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -16.0) |
| [[SW480 (line)]] | alt | 27.4 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.192× (z -15.4) |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -18.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.196× (z -10.7) |
| [[COLO 205 (line)]] | alt | 38.6 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 28.3 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -15.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 22.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -13.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.2) |
| [[A549 (line)]] | wt | 33.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 23.2 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 34.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.9) |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.259× (z -9.3) |
| [[C32 (line)]] | wt | 30.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -17.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.6) |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0957× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PF-06260933 (drug)]] 5 µM 0.0499× (z -10.4) |
| [[KATO III (line)]] | alt | 23.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -10.4) |
| [[LoVo (line)]] | wt | 29.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -20.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -11.5) |
| [[A-427 (line)]] | wt | 19.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -10.2) |
| [[A498 (line)]] | wt | 18.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 24.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -12.8) |
| [[H4 (line)]] | wt | 25.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0896× (z -17.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0885× (z -23.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.272× (z -8.7) |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.147× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -8.8) |
| [[SW48 (line)]] | wt | 23.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -8.5) |
| [[RKO (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.267× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -10.5) |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMLHE]] | +0.73 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[EFCAB7]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[DYNC2LI1]] | +0.68 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[PGGT1B]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZNF138]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CUL5]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[THUMPD2]] | +0.62 | +0.37 / +0.71 | both halves | 8e-05 |  |
| [[MRPL1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LEPROTL1]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SHLD1]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[PYROXD1]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[METTL22]] | +0.59 | +0.49 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF13]] | -0.58 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[KLF12]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[DDX5]] | -0.56 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CFL1]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[DIAPH1]] | -0.55 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[AHRR]] | -0.54 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SRGAP2]] | -0.53 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[SCHIP1]] | -0.53 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[MAMLD1]] | -0.53 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[LINC01128]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SRGAP2C]] | -0.52 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[MAPKAPK2]] | -0.52 | -0.28 / -0.58 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIGB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF594-DT]] | B | ZNF594-DT activity raises PIGB's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.29× lower at baseline in the lines without ZNF594-DT | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[CPPED1]] | B | CPPED1 activity raises PIGB's level | lines that do not express CPPED1 (5) vs lines expressing it (45) | 1.40× lower at baseline in the lines without CPPED1 | 0.081 | ⚠ within organs, on part of the lines; also absent: CCDC144CP |
| [[ZBED3]] | C | ZBED3 activity raises PIGB's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-23.6, -0.1); signed map (-20.9, -21.0). **Vector** length 64.4, 13.8% of its response variance represented; |z| ≥ 3 in 1,249 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +6.7 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.9 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.0 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -16.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | -3.4 | -12.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.0 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -8.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -6.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | +0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,318,960-55,355,648 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIG-B, GPI-MT-III |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases; Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92521](https://www.uniprot.org/uniprotkb/Q92521) (GPI alpha-1,2-mannosyltransferase 3):

> Alpha-1,2-mannosyltransferase that catalyzes the transfer of the third mannose, via an alpha-1,2 bond, from a dolichol-phosphate-mannose (Dol-P-Man) to a 2-acyl-6-[alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol intermediate to generate a …

**Summary**, from NCBI Gene [9488](https://www.ncbi.nlm.nih.gov/gene/9488):

> This gene encodes a transmembrane protein that is located in the endoplasmic reticulum and is involved in GPI-anchor biosynthesis. The glycosylphosphatidylinositol (GPI) anchor is a glycolipid found on many blood cells and serves to anchor proteins to the cell surface. This gene is thought to encode a member of a family of dolichol-phosphate-mannose (Dol-P-Man) dependent mannosyltransferases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8959) · Entrez [9488](https://www.ncbi.nlm.nih.gov/gene/9488) · UniProt [Q92521](https://www.uniprot.org/uniprotkb/Q92521) · Ensembl [ENSG00000069943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069943)

## Data

Gene col 929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 929); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 929]; `tensor/DDL_lfc|DDL_z.npy` [929]; `embed/gene_vectors.npy` [929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 929 or target_col == 929). Every well: [[PIGB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
