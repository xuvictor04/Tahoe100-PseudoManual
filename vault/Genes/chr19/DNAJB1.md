---
symbol: "DNAJB1"
type: "gene"
col: 5265
ensembl_id: "ENSG00000132002"
name: "DnaJ heat shock protein family (Hsp40) member B1"
location: "19p13.12"
module: 60
arm: "+"
pooled_cpm: 80.95
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# DNAJB1

*DnaJ heat shock protein family (Hsp40) member B1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 21.6× (z +41.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -11.7, q 1e-28, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSRB1]] (+0.66, fdr 1e-05), [[CYB5R1]] (+0.66, fdr 1e-05), [[UBC]] (+0.65, fdr 7e-06); moves opposite to [[LINC00938]] (-0.63, fdr 2e-05), [[RNF170]] (-0.62, fdr 3e-05), [[VPS13B-DT]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **21.6×** | +41.2 | 0e+00 | 48/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **17.0×** | +38.1 | 0e+00 | 48/48 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **12.9×** | +34.3 | 0e+00 | 48/48 (A-172, SW480, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **11.3×** | +30.7 | 0e+00 | 48/48 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.82×** | +21.1 | 0e+00 | 47/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.07×** | +18.8 | 0e+00 | 47/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.33×** | +15.5 | 0e+00 | 44/47 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **12.0×** | +14.8 | 0e+00 | 45/45 (A-172, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **2.84×** | +14.0 | 1e-42 | 45/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **6.24×** | +11.9 | 1e-30 | 48/49 (A-172, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.69×** | +9.9 | 2e-21 | 33/48 (C32, NCI-H1792, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.72×** | +7.0 | 1e-10 | 34/48 (HEC-1-A, A-172, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **3.16×** | +6.8 | 4e-10 | 46/48 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +6.0 | 9e-08 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +4.9 | 3e-05 | 29/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.3 | 5e-04 | 24/48 (A498, KATO III, …) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.5 µM |  | **1.91×** | +4.2 | 9e-04 | 30/49 (A-172, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.97×** | +4.0 | 0.002 | 26/49 (A-172, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.009 | 22/48 (CFPAC-1, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -11.7 | 1e-28 | 40/49 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -6.9 | 2e-09 | 34/50 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -6.7 | 4e-09 | 34/48 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.711×** | -4.6 | 5e-04 | 29/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.791×** | -4.5 | 8e-04 | 25/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.760×** | -3.7 | 0.018 | 23/48 (LoVo, LS 180, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -3.4 | 0.059 | 25/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.784×** | -3.3 | 0.059 | 24/48 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.841× | -3.3 | 0.059 | 19/48 (MIA PaCa-2, HT-29, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.786×** | -3.3 | 0.059 | 21/48 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.790×** | -3.2 | 0.069 | 19/49 (HepG2/C3A, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.1 | 19 (11 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 17.8× (z +22.1) | — |
| [[A498 (line)]] | wt | 129 | 11 (2 ⚠) | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 18.9× (z +31.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -16.8) |
| [[C32 (line)]] | wt | 102 | 13 (7 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +28.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 34.6× (z +24.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 148 | 11 (4 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 28.2× (z +29.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -17.7) |
| [[A-172 (line)]] | wt | 114 | 9 (3 ⚠) | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 45.9× (z +38.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -16.4) |
| [[C-33 A (line)]] | alt | 57.0 | 13 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 73.3× (z +29.5) | — |
| [[HEC-1-A (line)]] | alt | 67.0 | 13 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 63.1× (z +35.4) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 13 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 30.1× (z +32.2) | — |
| [[SW480 (line)]] | alt | 94.4 | 12 (3 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 30.1× (z +34.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.4) |
| [[KATO III (line)]] | alt | 89.2 | 9 (1 ⚠) | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 24.5× (z +28.0) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 116 | 10 (3 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 17.2× (z +24.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -14.4) |
| [[HS-578T (line)]] | alt | 69.3 | 11 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 40.7× (z +30.1) | — |
| [[LoVo (line)]] | wt | 82.3 | 10 (3 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 32.3× (z +30.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.3) |
| [[LS 180 (line)]] | wt | 75.1 | 10 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 17.5× (z +26.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 159 | 9 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 22.0× (z +29.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -12.5) |
| [[SNU-423 (line)]] | alt | 79.2 | 9 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 47.8× (z +30.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -9.9) |
| [[SW48 (line)]] | wt | 61.1 | 8 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 58.1× (z +23.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 92.0 | 8 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 7.75× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -13.9) |
| [[J82 (line)]] | alt | 54.2 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 23.9× (z +25.5) | — |
| [[NCI-H1792 (line)]] | alt | 52.7 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +24.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.34× (z +12.2) | — |
| [[RKO (line)]] | wt | 46.5 | 9 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 33.2× (z +24.3) | — |
| [[A549 (line)]] | wt | 45.7 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 12.6× (z +17.8) | — |
| [[HCT15 (line)]] | alt | 120 | 7 | 1 | [[Ixazomib citrate (drug)]] 5 µM 10.5× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -12.3) |
| [[HOP62 (line)]] | alt | 41.4 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 45.3× (z +27.1) | — |
| [[NCI-H2030 (line)]] | alt | 51.6 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 27.9× (z +24.5) | — |
| [[NCI-H2347 (line)]] | alt | 77.3 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.0× (z +25.6) | — |
| [[PANC-1 (line)]] | alt | 59.1 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.4× (z +27.2) | — |
| [[RPMI-7951 (line)]] | alt | 80.7 | 7 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 32.8× (z +22.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -9.3) |
| [[A-427 (line)]] | wt | 82.0 | 7 | 0 | [[Auranofin (drug)]] 5 µM 43.9× (z +31.2) | — |
| [[HepG2_C3A (line)]] | wt | 168 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.12× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 6.92× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 41.4 | 7 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 40.3× (z +20.0) | — |
| [[LOX-IMVI (line)]] | wt | 38.8 | 7 | 0 | [[Auranofin (drug)]] 5 µM 35.5× (z +20.8) | — |
| [[NCI-H1573 (line)]] | alt | 36.3 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.72× (z +15.5) | — |
| [[SHP-77 (line)]] | alt | 72.2 | 7 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 36.8× (z +17.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 22.4× (z +15.2) | — |
| [[SW 900 (line)]] | alt | 113 | 6 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 16.2× (z +20.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -8.9) |
| [[BT-474 (line)]] | alt | 151 | 5 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 27.6× (z +30.2) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.393× (z -12.0) |
| [[CHP-212 (line)]] | wt | 58.0 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 23.4× (z +13.1) | — |
| [[H4 (line)]] | wt | 72.9 | 6 | 0 | [[Auranofin (drug)]] 5 µM 34.5× (z +20.2) | — |
| [[Hs 766T (line)]] | wt | 56.8 | 6 | 0 | [[Auranofin (drug)]] 5 µM 18.8× (z +19.3) | — |
| [[HT-29 (line)]] | alt | 78.5 | 5 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 28.5× (z +25.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -12.7) |
| [[SNU-1 (line)]] | wt | 44.2 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 60.6× (z +22.7) | — |
| [[SW1417 (line)]] | alt | 156 | 5 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 11.7× (z +23.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -13.5) |
| [[COLO 205 (line)]] | alt | 88.7 | 5 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 24.3× (z +21.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 11.6× (z +17.2) | — |
| [[NCI-H23 (line)]] | alt | 61.7 | 3 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 19.6× (z +25.8) | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.7) |
| [[AN3 CA (line)]] | alt | 58.3 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 51.1× (z +18.5) | — |
| [[NCI-H661 (line)]] | alt | 97.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 16.1× (z +11.4) | — |
| [[SW 1271 (line)]] | alt | 82.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 72.3× (z +14.4) | — |
| [[SW 1088 (line)]] | alt | 61.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 38.5× (z +9.2) | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSRB1]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[CYB5R1]] | +0.66 | +0.54 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[UBC]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[HSPA1B]] | +0.63 | +0.62 / +0.74 | both halves | 7e-06 | pathway: Attenuation phase; STRING 998 |
| [[HSP90AA1]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 | pathway: Attenuation phase; STRING 999 |
| [[HSP90AA2P]] | +0.62 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ULBP3]] | +0.61 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[TWF2]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SLC45A4]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[BAG3]] | +0.60 | +0.67 / +0.76 | both halves | 7e-06 | pathway: Cellular response to heat stress; STRING 891 |
| [[PWWP3A]] | +0.60 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[SH3PXD2B]] | +0.58 | +0.40 / +0.43 | both halves | 5e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00938]] | -0.63 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RNF170]] | -0.62 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[VPS13B-DT]] | -0.60 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[RC3H2]] | -0.57 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[PCMTD1-DT]] | -0.57 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[TSTD3]] | -0.57 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[FBXW4]] | -0.57 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[CBR4]] | -0.56 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[C5orf15]] | -0.56 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[DICER1-AS1]] | -0.56 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[TMA7]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TAPT1]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DNAJB1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ETNK2]] | B | ETNK2 activity raises DNAJB1's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without ETNK2 | 0.012 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.0, 11.8); signed map (-22.8, -26.6). **Vector** length 143, 49.1% of its response variance represented; |z| ≥ 3 in 1,506 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial unfolded protein response (UPRmt)* (reactome, mean cos +0.51 to 5); *Chaperone Mediated Autophagy* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.5 | +41.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +12.2 | +30.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +11.7 | +34.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.6 | +38.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +9.4 | +14.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.9 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.3 | +1.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -12.2 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.9 | -11.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -11.5 | -6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.2 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,514,769-14,560,391 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hsp40, Sis1, RSPH16B; previously HSPF1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 10 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [P25685](https://www.uniprot.org/uniprotkb/P25685) (DnaJ homolog subfamily B member 1):

> Interacts with HSP70 and can stimulate its ATPase activity. Acts also with TTC1 as a chaperone adapter that regulates HSP70-dependent folding process by interacting with the HSP70 amino terminal region. Stimulates the association between HSC70 and HIP. Negatively regulates heat shock-induced HSF1 transcriptional activity during the attenuation and recovery phase period of the heat shock response. Stimulates ATP hydrolysis and the folding of unfolded proteins mediated by HSPA1A/B (in vitro).

**Summary**, from NCBI Gene [3337](https://www.ncbi.nlm.nih.gov/gene/3337):

> This gene encodes a member of the DnaJ or Hsp40 (heat shock protein 40 kD) family of proteins. DNAJ family members are characterized by a highly conserved amino acid stretch called the 'J-domain' and function as one of the two major classes of molecular chaperones involved in a wide range of cellular events, such as protein folding and oligomeric protein complex assembly. The encoded protein is a molecular chaperone that stimulates the ATPase activity of Hsp70 heat-shock proteins in order to …

**Accessions** — [HGNC:5270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5270) · Entrez [3337](https://www.ncbi.nlm.nih.gov/gene/3337) · UniProt [P25685](https://www.uniprot.org/uniprotkb/P25685) · Ensembl [ENSG00000132002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132002)

## Data

Gene col 5265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5265); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5265]; `tensor/DDL_lfc|DDL_z.npy` [5265]; `embed/gene_vectors.npy` [5265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5265 or target_col == 5265). Every well: [[DNAJB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
