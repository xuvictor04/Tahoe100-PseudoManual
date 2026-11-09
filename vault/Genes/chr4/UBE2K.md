---
symbol: "UBE2K"
type: "gene"
col: 1211
ensembl_id: "ENSG00000078140"
name: "ubiquitin conjugating enzyme E2 K"
location: "4p14"
module: 18
arm: "+"
pooled_cpm: 252.19
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# UBE2K

*ubiquitin conjugating enzyme E2 K* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.86× (z +19.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.712× (z -15.2, q 0e+00, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA3]] (+0.67, fdr 7e-06), [[PDS5A]] (+0.62, fdr 1e-05, ⚠ same locus), [[UBE3C]] (+0.57, fdr 1e-05), [[DAP3]] (+0.57, fdr 1e-05); moves opposite to [[RNF139]] (-0.57, fdr 1e-04), [[CFAP20]] (-0.57, fdr 1e-05), [[RARA]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AKR1C1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ERC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.86×** | +19.5 | 0e+00 | 48/48 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +18.7 | 0e+00 | 48/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +17.8 | 0e+00 | 48/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +17.0 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +15.8 | 0e+00 | 46/48 (SW480, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.68×** | +15.4 | 0e+00 | 45/48 (HT-29, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +13.3 | 2e-38 | 45/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +10.7 | 9e-25 | 40/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +8.1 | 2e-14 | 32/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +7.9 | 2e-13 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +7.3 | 1e-11 | 35/48 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +7.2 | 3e-11 | 37/45 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +6.9 | 2e-10 | 28/49 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +6.6 | 1e-09 | 40/49 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +6.2 | 2e-08 | 24/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +4.3 | 6e-04 | 6/49 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.9 | 0.004 | 9/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.037 | 18/48 (SK-MEL-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -15.2 | 0e+00 | 38/49 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.667×** | -12.8 | 4e-35 | 40/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -11.7 | 2e-29 | 38/48 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.840× | -5.5 | 5e-06 | 20/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 0.847× | -5.0 | 5e-05 | 21/47 (HepG2/C3A, RKO, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.860× | -4.8 | 2e-04 | 12/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.898× | -3.4 | 0.050 | 13/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.927× | -3.4 | 0.050 | 7/48 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.930× | -3.3 | 0.064 | 12/48 (A-172, A-427, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.904× | -3.2 | 0.080 | 5/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.907× | -3.1 | 0.095 | 11/48 (BT-474, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 261 | 11 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +23.7) | [[Panobinostat (drug)]] 0.5 µM 0.556× (z -13.5) |
| [[HT-29 (line)]] | alt | 287 | 9 (2 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +16.5) | [[Panobinostat (drug)]] 0.5 µM 0.580× (z -10.3) |
| [[LoVo (line)]] | wt | 271 | 9 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.572× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 225 | 10 (3 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.14× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -12.6) |
| [[HOP62 (line)]] | alt | 286 | 7 (1 ⚠) | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.09× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.513× (z -13.9) |
| [[COLO 205 (line)]] | alt | 184 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.58× (z +16.4) | — |
| [[KATO III (line)]] | alt | 200 | 7 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.529× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 307 | 7 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.18× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.560× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 228 | 8 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.45× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.660× (z -8.7) |
| [[PANC-1 (line)]] | alt | 227 | 8 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +19.2) | [[Panobinostat (drug)]] 0.5 µM 0.626× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 227 | 8 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.16× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +13.6) | — |
| [[H4 (line)]] | wt | 299 | 8 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.91× (z +19.5) | — |
| [[NCI-H23 (line)]] | alt | 276 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.20× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -25.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[A498 (line)]] | wt | 274 | 4 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 1.79× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 299 | 4 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 1.80× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -13.7) |
| [[LS 180 (line)]] | wt | 270 | 6 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +19.7) | [[Panobinostat (drug)]] 0.5 µM 0.591× (z -9.6) |
| [[A549 (line)]] | wt | 187 | 4 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.66× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -17.1) |
| [[J82 (line)]] | alt | 243 | 3 (2 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 1.62× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 210 | 4 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.73× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 248 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 186 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.60× (z +14.3) | — |
| [[A-172 (line)]] | wt | 248 | 2 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.65× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -17.1) |
| [[HCT15 (line)]] | alt | 300 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.18× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.12× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 185 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 212 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 230 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 265 | 3 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 1.73× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.561× (z -10.3) |
| [[SW 900 (line)]] | alt | 436 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +13.9) | — |
| [[C32 (line)]] | wt | 200 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +13.0) | — |
| [[HepG2_C3A (line)]] | wt | 219 | 1 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.526× (z -9.2) |
| [[HS-578T (line)]] | alt | 212 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.84× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -9.2) |
| [[RKO (line)]] | wt | 352 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -14.6) |
| [[SW48 (line)]] | wt | 320 | 3 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.31× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 231 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.92× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.82× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 261 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -12.8) |
| [[C-33 A (line)]] | alt | 315 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 307 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 205 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +13.3) | — |
| [[A-427 (line)]] | wt | 313 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.590× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 204 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +11.8) | — |
| [[SK-MEL-2 (line)]] | alt | 270 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.606× (z -8.8) |
| [[AN3 CA (line)]] | alt | 264 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 265 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 359 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 295 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 326 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA3]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[PDS5A]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 | STRING 527; ⚠ same locus (40.1 kb: neighbours can correlate without regulation) |
| [[UBE3C]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 439 |
| [[DAP3]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LARP4]] | +0.55 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[EXOC2]] | +0.55 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[PCGF6]] | +0.54 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[HSPE1]] | +0.54 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[IDE]] | +0.53 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[NUTM2A-AS1]] | +0.53 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[ME2]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.52 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[HERC2P9]] | +0.52 | +0.72 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF139]] | -0.57 | -0.36 / -0.67 | both halves | 1e-04 | STRING 520 |
| [[CFAP20]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[RARA]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[RBM22]] | -0.55 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[LAMTOR3]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 | STRING 485 |
| [[ING1]] | -0.52 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[KLHL15]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[NFKB2]] | -0.50 | -0.56 / -0.46 | both halves | 2e-05 | pathway: DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| [[ZNF574]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SOX9]] | -0.50 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[NR1D1]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PTGER4]] | -0.50 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C1]] | B | AKR1C1 activity lowers UBE2K's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 1.21× higher at baseline in the lines without AKR1C1 | 0.020 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERC1]] | C | UBE2K's natural level strengthens ERC1's drug response | UBE2K's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.29; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.3, -33.6); signed map (-18.0, -50.9). **Vector** length 109, 38.4% of its response variance represented; |z| ≥ 3 in 1,356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.8 | +19.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.6 | +15.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +8.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.3 | +6.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -15.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -0.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -4.5 | +3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -4.2 | -0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -1.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.5 | -1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.3 | -1.7 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -2.1 | -0.9 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,698,109-39,782,792 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HYPG, UBC1; previously HIP2 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 8 pathways, smallest: Synthesis of active ubiquitin: roles of E1 and E2 enzymes; Negative regulators of DDX58/IFIH1 signaling; DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| Matched by | ensembl_id |

**Function**, from UniProt [P61086](https://www.uniprot.org/uniprotkb/P61086) (Ubiquitin-conjugating enzyme E2 K):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro, in the presence or in the absence of BRCA1-BARD1 E3 ubiquitin-protein ligase complex, catalyzes the synthesis of 'Lys-48'-linked polyubiquitin chains. Does not transfer ubiquitin directly to but elongates monoubiquitinated substrate protein. Mediates the selective degradation of short-lived and abnormal proteins, such as the endoplasmic reticulum-associated degradation (ERAD) of misfolded …

**Summary**, from NCBI Gene [3093](https://www.ncbi.nlm.nih.gov/gene/3093):

> The protein encoded by this gene belongs to the ubiquitin-conjugating enzyme family. This protein interacts with RING finger proteins, and it can ubiquitinate huntingtin, the gene product for Huntington's disease. Known functions for this protein include a role in aggregate formation of expanded polyglutamine proteins and the suppression of apoptosis in polyglutamine diseases, a role in the dislocation of newly synthesized MHC class I heavy chains from the endoplasmic reticulum, and involvement …

**Accessions** — [HGNC:4914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4914) · Entrez [3093](https://www.ncbi.nlm.nih.gov/gene/3093) · UniProt [P61086](https://www.uniprot.org/uniprotkb/P61086) · Ensembl [ENSG00000078140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078140)

## Data

Gene col 1211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1211); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1211]; `tensor/DDL_lfc|DDL_z.npy` [1211]; `embed/gene_vectors.npy` [1211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1211 or target_col == 1211). Every well: [[UBE2K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
