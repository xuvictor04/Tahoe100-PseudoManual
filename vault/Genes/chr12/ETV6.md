---
symbol: "ETV6"
type: "gene"
col: 6257
ensembl_id: "ENSG00000139083"
name: "ETS variant transcription factor 6"
location: "12p13.2"
module: 70
arm: "+"
pooled_cpm: 219.07
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 54
n_dd_up_clean: 1
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# ETV6

*ETS variant transcription factor 6* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.34× (z +3.9, q 0.060, up in 28 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H460 2.13×, Hs 766T 2.15×, RKO 2.24×, LoVo 1.80×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.05 µM in 1 line (AsPC-1 2.72×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.95×); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 2.89×).
> Pooled over the cell lines (median), lowered significantly by 54 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.429× (z -16.0, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.328× (z -14.9, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANXA2R-AS1]] (+0.61, fdr 2e-05), [[CTSS]] (+0.59, fdr 2e-05), [[NFKB1]] (+0.58, fdr 1e-05); moves opposite to [[CLTCL1]] (-0.53, fdr 2e-05), [[AP2A2]] (-0.53, fdr 8e-05), [[HDAC11]] (-0.51, fdr 5e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PLSCR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6257.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H460 2.13×, Hs 766T 2.15×, RKO 2.24×, LoVo 1.80×; ⚠ cell-cycle shift, explains ~0% of this change); [[Trametinib (drug)]] 0.05 µM in 1 line (AsPC-1 2.72×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.95×); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 2.89×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.060 | 28/46 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.29× | +3.5 | 0.10 | 30/47 (LOX-IMVI, NCI-H2347, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.10 | 23/47 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.29× | +3.4 | 0.10 | 22/47 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.27× | +3.3 | 0.11 | 25/47 (HS-578T, C-33 A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.11 | 21/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.19 | 23/46 (AsPC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 54 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.429×** | -16.0 | 0e+00 | 39/47 (COLO 205, A498, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.328×** | -14.9 | 0e+00 | 46/47 (LoVo, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.339×** | -14.5 | 3e-45 | 47/47 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.369×** | -13.4 | 1e-38 | 46/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.369×** | -13.4 | 1e-38 | 44/47 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.382×** | -12.9 | 7e-36 | 46/47 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.395×** | -12.4 | 2e-33 | 43/47 (LoVo, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.426×** | -11.4 | 3e-28 | 47/47 (C32, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.434×** | -11.2 | 4e-27 | 46/47 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.440×** | -11.0 | 3e-26 | 40/47 (C32, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -10.0 | 7e-22 | 39/47 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.461×** | -9.8 | 7e-21 | 45/47 (C32, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.494×** | -9.1 | 6e-18 | 35/46 (KATO III, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.526×** | -8.6 | 4e-16 | 44/47 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.504×** | -8.5 | 9e-16 | 37/44 (SNU-1, A498, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.682×** | -7.2 | 2e-11 | 39/48 (CFPAC-1, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.422×** | -6.0 | 5e-08 | 45/47 (SW 900, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.669×** | -5.3 | 2e-06 | 38/47 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.691×** | -4.7 | 5e-05 | 35/46 (H4, AN3 CA, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.654×** | -4.6 | 1e-04 | 33/46 (NCI-H23, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.797×** | -4.2 | 4e-04 | 26/47 (CFPAC-1, SHP-77, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 358 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -27.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -17.0) |
| [[SW 900 (line)]] | alt | 437 | 0 | 20 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.207× (z -15.6) |
| [[C32 (line)]] | wt | 316 | 0 | 19 (9 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.113× (z -22.5) |
| [[HOP62 (line)]] | alt | 347 | 0 | 17 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -17.9) |
| [[LoVo (line)]] | wt | 335 | 1 (1 ⚠) | 16 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.128× (z -22.5) |
| [[LOX-IMVI (line)]] | wt | 249 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -18.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.185× (z -14.7) |
| [[HT-29 (line)]] | alt | 557 | 0 | 15 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -16.0) |
| [[LS 180 (line)]] | wt | 338 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -21.1) |
| [[NCI-H1792 (line)]] | alt | 678 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -24.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.200× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 57.6 | 3 (2 ⚠) | 12 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.317× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 127 | 7 (1 ⚠) | 7 (3 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.72× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -10.3) |
| [[COLO 205 (line)]] | alt | 495 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0579× (z -31.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0800× (z -19.6) |
| [[SHP-77 (line)]] | alt | 143 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -22.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.177× (z -17.8) |
| [[SW480 (line)]] | alt | 145 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -18.0) |
| [[KATO III (line)]] | alt | 361 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -18.3) |
| [[SW1417 (line)]] | alt | 334 | 0 | 11 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.199× (z -14.6) |
| [[NCI-H23 (line)]] | alt | 185 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.221× (z -12.1) |
| [[PANC-1 (line)]] | alt | 106 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.320× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.330× (z -12.1) |
| [[RKO (line)]] | wt | 125 | 1 (1 ⚠) | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 131 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -15.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.224× (z -11.9) |
| [[A-427 (line)]] | wt | 231 | 0 | 7 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.326× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 116 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.288× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 577 | 0 | 7 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0906× (z -21.5) |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 7 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.173× (z -13.0) |
| [[A549 (line)]] | wt | 203 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -10.8) |
| [[J82 (line)]] | alt | 167 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -11.7) |
| [[H4 (line)]] | wt | 164 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -9.2) |
| [[HS-578T (line)]] | alt | 155 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 232 | 1 | 3 (2 ⚠) | [[Belumosudil (drug)]] 5 µM 2.61× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.282× (z -11.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.300× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -12.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -10.9) |
| [[SNU-423 (line)]] | alt | 172 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -11.1) |
| [[BT-474 (line)]] | alt | 202 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.361× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 184 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.233× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 118 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.450× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 118 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -11.8) |
| [[SNU-1 (line)]] | wt | 105 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.247× (z -11.2) |
| [[Hs 766T (line)]] | wt | 77.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.371× (z -8.5) |
| [[A-172 (line)]] | wt | 79.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -15.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2122 (line)]] | alt | 210 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.0595× (z -8.9) |
| [[SW48 (line)]] | wt | 94.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.275× (z -8.9) |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 178 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA2R-AS1]] | +0.61 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CTSS]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NFKB1]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RIGI]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[BAZ1A]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[IRF2]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 | STRING 474 |
| [[OASL]] | +0.55 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[MX2]] | +0.55 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[CASP10]] | +0.54 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[STING1]] | +0.54 | +0.32 / +0.60 | both halves | 1e-04 |  |
| [[IFIT2]] | +0.54 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[RNF213]] | +0.54 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLTCL1]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[AP2A2]] | -0.53 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[HDAC11]] | -0.51 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[RNF216P1]] | -0.51 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[SGTB]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SIN3B]] | -0.50 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[TBCE]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[CDC16]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[LINC00662]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[TOM1L1]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[KCTD21]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ANKRD36B]] | -0.47 | -0.39 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR1]] | B | PLSCR1 activity raises ETV6's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without PLSCR1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[NRP1]] | B | NRP1 activity raises ETV6's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without NRP1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[STING1]] | B | STING1 activity raises ETV6's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without STING1 | 0.040 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[TNFSF10]] | B | TNFSF10 activity raises ETV6's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 1.61× lower at baseline in the lines without TNFSF10 | 0.043 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[XAF1]] | B | XAF1 activity raises ETV6's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without XAF1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[CFB]] | B | CFB activity raises ETV6's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.57× lower at baseline in the lines without CFB | 0.059 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[SMAD3]] | B | SMAD3 activity raises ETV6's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without SMAD3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[MX2]] | B | MX2 activity raises ETV6's level | lines that do not express MX2 (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without MX2 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[CLTCL1]] | C | CLTCL1 activity lowers ETV6's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 2.72× higher at baseline in the lines without CLTCL1 | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.543). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.4, 50.8); signed map (58.4, 31.0). **Vector** length 115, 50.4% of its response variance represented; |z| ≥ 3 in 1,999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.6 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | -0.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -14.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.0 | -7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.8 | -9.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.7 | -12.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -13.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.1 | -11.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.8 | -5.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ETS variant transcription factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:11,649,674-11,895,377 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEL |
| Gene groups (HGNC) | ETS transcription factor family |
| Reactome | 5 pathways, smallest: Signaling by membrane-tethered fusions of PDGFRA or PDGFRB; Signaling by FLT3 fusion proteins; Signaling by PDGFR in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [P41212](https://www.uniprot.org/uniprotkb/P41212) (Transcription factor ETV6):

> Transcriptional repressor; binds to the DNA sequence 5'-CCGGAAGT-3'. Plays a role in hematopoiesis and malignant transformation.

**Summary**, from NCBI Gene [2120](https://www.ncbi.nlm.nih.gov/gene/2120):

> This gene encodes an ETS family transcription factor. The product of this gene contains two functional domains: a N-terminal pointed (PNT) domain that is involved in protein-protein interactions with itself and other proteins, and a C-terminal DNA-binding domain. Gene knockout studies in mice suggest that it is required for hematopoiesis and maintenance of the developing vascular network. This gene is known to be involved in a large number of chromosomal rearrangements associated with leukemia …

**Accessions** — [HGNC:3495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3495) · Entrez [2120](https://www.ncbi.nlm.nih.gov/gene/2120) · UniProt [P41212](https://www.uniprot.org/uniprotkb/P41212) · Ensembl [ENSG00000139083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139083)

## Data

Gene col 6257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6257); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6257]; `tensor/DDL_lfc|DDL_z.npy` [6257]; `embed/gene_vectors.npy` [6257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6257 or target_col == 6257). Every well: [[ETV6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETV6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
