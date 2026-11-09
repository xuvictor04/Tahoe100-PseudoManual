---
symbol: "JUNB"
type: "gene"
col: 10076
ensembl_id: "ENSG00000171223"
name: "JunB proto-oncogene, AP-1 transcription factor subunit"
location: "19p13.13"
module: 109
arm: "+"
pooled_cpm: 80.14
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 32
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# JUNB

*JunB proto-oncogene, AP-1 transcription factor subunit* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.96× (z +25.4, q 0e+00, up in 44 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 5.15× (z +18.1, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.489× (z -11.4, q 2e-27, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER2]] (+0.79, fdr 7e-06), [[ZFP36]] (+0.77, fdr 7e-06), [[CSRNP1]] (+0.75, fdr 7e-06); moves opposite to [[C8orf76]] (-0.63, fdr 1e-05), [[PSMB5]] (-0.62, fdr 1e-05), [[SOS1]] (-0.61, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **4.96×** | +25.4 | 0e+00 | 44/46 (AsPC-1, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **5.15×** | +18.1 | 0e+00 | 43/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.49×** | +15.9 | 0e+00 | 44/44 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +14.6 | 0e+00 | 45/48 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +10.4 | 2e-23 | 37/42 (NCI-H460, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.99×** | +7.9 | 3e-13 | 32/46 (HEC-1-A, A-172, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +7.7 | 1e-12 | 31/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.90×** | +7.3 | 1e-11 | 34/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.26×** | +7.1 | 9e-11 | 37/48 (HepG2/C3A, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.9 | 2e-07 | 28/46 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.58×** | +5.3 | 7e-06 | 29/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.57×** | +5.2 | 1e-05 | 28/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.6 | 1e-04 | 36/47 (NCI-H2347, Panc 03.27, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 2e-04 | 36/48 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.41×** | +3.9 | 0.003 | 25/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.037 | 23/47 (Hs 766T, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -11.4 | 2e-27 | 45/48 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.449×** | -8.6 | 3e-15 | 42/47 (NCI-H1573, SW48, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -7.4 | 3e-11 | 39/49 (SW48, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.523×** | -7.2 | 1e-10 | 41/47 (SW48, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.548×** | -6.9 | 5e-10 | 39/47 (HT-29, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.576×** | -6.4 | 2e-08 | 35/47 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.360×** | -6.1 | 6e-08 | 41/46 (HCT15, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.420×** | -5.2 | 1e-05 | 34/43 (RPMI-7951, C32, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.726×** | -5.1 | 2e-05 | 33/48 (NCI-H1573, NCI-H2030, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.745×** | -4.7 | 1e-04 | 30/47 (SW48, C32, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -4.6 | 2e-04 | 30/47 (SW48, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.755×** | -4.6 | 2e-04 | 32/47 (SW1417, HEC-1-A, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.676×** | -4.2 | 0.001 | 31/47 (SW480, LS 180, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.513×** | -4.0 | 0.002 | 37/47 (SW48, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.712×** | -3.9 | 0.003 | 31/47 (NCI-H1573, SW 1271, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.005 | 28/47 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.720×** | -3.6 | 0.009 | 26/47 (SW480, SW48, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.743×** | -3.4 | 0.019 | 27/47 (NCI-H23, A-427, …) | rises with dose | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.040 | 24/48 (C32, NCI-H2347, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.040 | 21/47 (COLO 205, SNU-423, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.3 | 16 (12 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.7× (z +24.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 15.1× (z +21.8) | — |
| [[C32 (line)]] | wt | 139 | 7 (5 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +24.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.71× (z +12.9) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 106 | 9 (7 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +21.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 9.99× (z +18.4) | [[Ixazomib citrate (drug)]] 5 µM 0.267× (z -11.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.481× (z -8.7) |
| [[SW48 (line)]] | wt | 207 | 4 (3 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.36× (z +12.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.46× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -18.3) |
| [[HOP62 (line)]] | alt | 57.5 | 9 (8 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.77× (z +21.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 12.2× (z +17.6) | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -10.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H2347 (line)]] | alt | 85.1 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +18.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.94× (z +14.8) | — |
| [[AsPC-1 (line)]] | alt | 139 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +27.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.55× (z +17.8) | — |
| [[HEC-1-A (line)]] | alt | 72.4 | 8 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +24.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.43× (z +18.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -13.9) |
| [[HepG2_C3A (line)]] | wt | 122 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +18.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.92× (z +12.7) | — |
| [[SW480 (line)]] | alt | 37.5 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +15.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.77× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 107 | 7 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +19.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.03× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -9.0) |
| [[PANC-1 (line)]] | alt | 57.2 | 7 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +21.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 12.2× (z +19.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.1) |
| [[A549 (line)]] | wt | 84.6 | 6 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 14.2× (z +21.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 12.5× (z +19.6) | [[Bortezomib (drug)]] 0.05 µM 0.299× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 108 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +18.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.15× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 50.4 | 4 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +17.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.99× (z +10.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 71.0 | 5 (3 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 7.74× (z +14.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 100 | 6 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 14.9× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 8.85× (z +15.0) | [[Bortezomib (drug)]] 5 µM 0.0648× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 53.3 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.4× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 8.46× (z +14.2) | — |
| [[SW 900 (line)]] | alt | 81.2 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +19.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.4× (z +16.0) | — |
| [[SNU-423 (line)]] | alt | 110 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +20.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.54× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -10.5) |
| [[A-172 (line)]] | wt | 52.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +21.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.8× (z +14.9) | — |
| [[CFPAC-1 (line)]] | alt | 84.0 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +24.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.52× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -8.8) |
| [[HT-29 (line)]] | alt | 104 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 86.7 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +20.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.01× (z +12.3) | [[Bortezomib (drug)]] 0.05 µM 0.226× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 62.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +16.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.57× (z +14.1) | — |
| [[Panc 03.27 (line)]] | alt | 105 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +20.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.23× (z +14.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -10.5) |
| [[SW1417 (line)]] | alt | 98.8 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +20.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.83× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.4) |
| [[A-427 (line)]] | wt | 59.6 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.65× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.85× (z +11.0) | — |
| [[A498 (line)]] | wt | 104 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +18.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.82× (z +12.8) | — |
| [[H4 (line)]] | wt | 54.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +12.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 67.4 | 2 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.62× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 89.3 | 4 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.56× (z +14.6) | — |
| [[NCI-H2030 (line)]] | alt | 114 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -11.9) |
| [[HCT15 (line)]] | alt | 83.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 4.54× (z +8.8) ⚠ toxic; transcription drop | [[NG25 (drug)]] 5 µM 0.0369× (z -10.7) |
| [[Hs 766T (line)]] | wt | 119 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +16.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.34× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -10.8) |
| [[KATO III (line)]] | alt | 41.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +16.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.98× (z +12.0) | — |
| [[LoVo (line)]] | wt | 76.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.173× (z -14.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -10.9) |
| [[C-33 A (line)]] | alt | 41.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 8.26× (z +10.8) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 96.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.40× (z +9.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 79.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 81.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -8.9) |
| [[RKO (line)]] | wt | 52.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.45× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 69.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.0) |
| [[AN3 CA (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER2]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 750 |
| [[ZFP36]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 847 |
| [[CSRNP1]] | +0.75 | +0.77 / +0.74 | both halves | 7e-06 | STRING 660 |
| [[EGR1]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 970 |
| [[NR4A1]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 696 |
| [[FOS]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[SOCS3]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 623 |
| [[NFKBIZ]] | +0.68 | +0.67 / +0.71 | both halves | 7e-06 | STRING 575 |
| [[ATP7A]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SKIL]] | +0.65 | +0.66 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_TGF_BETA_SIGNALING |
| [[NAB1]] | +0.65 | +0.55 / +0.70 | both halves | 1e-05 | pathway: NGF-stimulated transcription |
| [[EGR2]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 780 |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf76]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[PSMB5]] | -0.62 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[SOS1]] | -0.61 | -0.51 / -0.55 | both halves | 1e-05 | pathway: Signaling by NTRK1 (TRKA) |
| [[EIF4ENIF1]] | -0.61 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[TRAPPC13]] | -0.60 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TRPC4AP]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[GAPVD1]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[RTCA]] | -0.58 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ELMOD3]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[ZUP1]] | -0.58 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MFSD8]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises JUNB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DUSP2]] | B | DUSP2 activity lowers JUNB's level | lines that do not express DUSP2 (23) vs lines expressing it (27) | 1.28× higher at baseline in the lines without DUSP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ASTL, HOXA11, KCNE3; maybe low, not absent |
| [[PPL]] | B | PPL activity weakens JUNB's drug response | lines that do not express PPL (18) vs lines expressing it (31) | the lines without PPL respond 1.27× as strongly (z diff -0.78); strongest at Dinaciclib 5 µM: 4.74x vs 2.02x (z diff -3.2) | 0.093 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, 0.4); signed map (7.2, 28.1). **Vector** length 153, 55.8% of its response variance represented; |z| ≥ 3 in 1,511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.6 | +18.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +9.2 | +25.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +4.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.4 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -11.4 | -7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -11.2 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -10.9 | -6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.1 | -11.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -9.7 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.3 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -7.9 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -6.5 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -6.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | JunB proto-oncogene, AP-1 transcription factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,791,486-12,793,315 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Jun transcription factor family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, TGF_BETA_SIGNALING, UV_RESPONSE_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 16 pathways, smallest: Nuclear events stimulated by ALK signaling in cancer; NGF-stimulated transcription; SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P17275](https://www.uniprot.org/uniprotkb/P17275) (Transcription factor JunB):

> Transcription factor involved in regulating gene activity following the primary growth factor response. Binds to the DNA sequence 5'-TGA[GC]TCA-3'. Heterodimerizes with proteins of the FOS family to form an AP-1 transcription complex, thereby enhancing its DNA binding activity to an AP-1 consensus sequence and its transcriptional activity (By similarity).

**Summary**, from NCBI Gene [3726](https://www.ncbi.nlm.nih.gov/gene/3726):

> Enables sequence-specific double-stranded DNA binding activity. Involved in positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of transcription factor AP-1 complex. Implicated in head and neck squamous cell carcinoma and melanoma. Biomarker of gastrointestinal system cancer (multiple); lung non-small cell carcinoma; and lymphoma (multiple). [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6205) · Entrez [3726](https://www.ncbi.nlm.nih.gov/gene/3726) · UniProt [P17275](https://www.uniprot.org/uniprotkb/P17275) · Ensembl [ENSG00000171223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171223)

## Data

Gene col 10076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10076); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10076]; `tensor/DDL_lfc|DDL_z.npy` [10076]; `embed/gene_vectors.npy` [10076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10076 or target_col == 10076). Every well: [[JUNB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JUNB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
