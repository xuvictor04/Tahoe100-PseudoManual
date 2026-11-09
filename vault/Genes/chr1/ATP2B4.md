---
symbol: "ATP2B4"
type: "gene"
col: 664
ensembl_id: "ENSG00000058668"
name: "ATPase plasma membrane Ca2+ transporting 4"
location: "1q32.1"
module: 113
arm: "+"
pooled_cpm: 196.92
n_lines_expressing: 42
n_dd_up: 28
n_dd_down: 28
n_dd_up_clean: 26
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# ATP2B4

*ATPase plasma membrane Ca2+ transporting 4* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.71× (z +11.0, q 2e-25, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.389× (z -27.2, q 0e+00, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP13]] (+0.62, fdr 1e-05), [[A4GALT]] (+0.61, fdr 3e-05), [[LRRFIP1]] (+0.56, fdr 3e-05); moves opposite to [[LINC01134]] (-0.48, fdr 2e-04), [[UNC119B]] (-0.47, fdr 1e-04), [[DPY19L3-DT]] (-0.47, fdr 2e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[CAST]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.71×** | +11.0 | 2e-25 | 32/39 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.55×** | +9.4 | 1e-18 | 29/39 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.9 | 7e-13 | 27/40 (RKO, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +7.8 | 1e-12 | 26/40 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +7.6 | 3e-12 | 26/40 (NCI-H460, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +7.3 | 3e-11 | 24/40 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.41×** | +7.3 | 3e-11 | 25/40 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +6.8 | 7e-10 | 21/40 (NCI-H460, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +6.8 | 7e-10 | 23/40 (C32, SW 900, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +6.5 | 5e-09 | 27/39 (C32, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +6.3 | 1e-08 | 26/40 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +6.2 | 3e-08 | 24/39 (C32, SW 900, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +6.1 | 3e-08 | 19/41 (C32, NCI-H460, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +6.1 | 4e-08 | 21/40 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.63×** | +5.5 | 1e-06 | 26/40 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.27×** | +5.3 | 4e-06 | 21/42 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.2 | 6e-06 | 18/40 (KATO III, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.389×** | -27.2 | 0e+00 | 39/41 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.545×** | -17.6 | 0e+00 | 27/40 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.522×** | -13.3 | 2e-38 | 34/39 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.667×** | -11.7 | 3e-29 | 31/40 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -10.9 | 1e-25 | 30/40 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.680×** | -8.2 | 2e-14 | 31/40 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.709×** | -7.3 | 2e-11 | 30/41 (COLO 205, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.718×** | -7.1 | 1e-10 | 25/41 (AsPC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.705×** | -6.9 | 3e-10 | 23/37 (AsPC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.820×** | -6.1 | 7e-08 | 18/40 (HOP62, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.753×** | -6.0 | 7e-08 | 26/40 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.754×** | -6.0 | 7e-08 | 27/40 (HOP62, MIA PaCa-2, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -5.9 | 1e-07 | 24/40 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -5.8 | 3e-07 | 24/40 (SW48, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -5.7 | 4e-07 | 23/42 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.774×** | -5.5 | 1e-06 | 20/40 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.622×** | -5.3 | 4e-06 | 25/40 (PANC-1, C32, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.628×** | -5.2 | 6e-06 | 21/40 (PANC-1, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.640×** | -5.0 | 2e-05 | 20/40 (C32, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.798×** | -4.8 | 4e-05 | 16/40 (HOP62, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.2 | 23 (2 ⚠) | 1 | [[Trametinib (drug)]] 0.5 µM 3.44× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.6) |
| [[HOP62 (line)]] | alt | 309 | 3 | 15 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.00× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -27.9) |
| [[NCI-H1573 (line)]] | alt | 98.8 | 14 | 4 | [[Betamethasone dipropionate (drug)]] 5 µM 3.25× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -23.4) |
| [[SNU-423 (line)]] | alt | 263 | 14 (1 ⚠) | 3 | [[Dexamethasone (drug)]] 0.5 µM 2.35× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -19.1) |
| [[C32 (line)]] | wt | 528 | 6 (2 ⚠) | 9 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.53× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -29.7) |
| [[COLO 205 (line)]] | alt | 143 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0734× (z -28.3) |
| [[A-172 (line)]] | wt | 566 | 5 (2 ⚠) | 6 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.53× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -16.0) |
| [[PANC-1 (line)]] | alt | 169 | 6 (3 ⚠) | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.98× (z +19.6) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 736 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -23.9) |
| [[CFPAC-1 (line)]] | alt | 297 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -22.7) |
| [[KATO III (line)]] | alt | 67.1 | 5 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.48× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -22.8) |
| [[RPMI-7951 (line)]] | alt | 193 | 4 (1 ⚠) | 4 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.98× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -19.7) |
| [[J82 (line)]] | alt | 212 | 3 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.03× (z +15.7) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -18.5) |
| [[LoVo (line)]] | wt | 126 | 3 (1 ⚠) | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.98× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -20.1) |
| [[Panc 03.27 (line)]] | alt | 171 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -18.3) |
| [[SK-MEL-2 (line)]] | alt | 250 | 1 | 6 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.23× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -21.6) |
| [[A549 (line)]] | wt | 112 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.92× (z +16.3) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.3) | — |
| [[H4 (line)]] | wt | 162 | 4 | 2 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 6.56× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 206 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.44× (z +14.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.92× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 118 | 3 | 3 | [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 90.3 | 3 | 3 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.80× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.5) |
| [[RKO (line)]] | wt | 78.7 | 2 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.79× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.3) |
| [[SW 900 (line)]] | alt | 352 | 3 | 3 (1 ⚠) | [[Trametinib (drug)]] 5 µM 2.51× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -15.0) |
| [[BT-474 (line)]] | alt | 109 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +15.2) | — |
| [[Hs 766T (line)]] | wt | 469 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -20.2) |
| [[HT-29 (line)]] | alt | 171 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 486 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -28.7) |
| [[SW48 (line)]] | wt | 191 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.6) |
| [[HS-578T (line)]] | alt | 317 | 3 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.62× (z +14.1) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 5 µM 2.54× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 320 | 2 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 3.23× (z +13.9) ⚠ cell-cycle shift, explains ~19% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 92.1 | 1 | 3 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.69× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 349 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -14.3) |
| [[A498 (line)]] | wt | 250 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.57× (z +13.6) ⚠ cell-cycle shift, explains ~5% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.526× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 49.4 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.31× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.5) |
| [[A-427 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 274 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 40.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 29.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP13]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[A4GALT]] | +0.61 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[LRRFIP1]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[FLNB]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[DUSP1]] | +0.54 | +0.40 / +0.56 | both halves | 5e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[RHOB]] | +0.54 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[ERGIC1]] | +0.54 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[AGTPBP1]] | +0.54 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[RTN2]] | +0.53 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[UBE2E2]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TMOD3]] | +0.53 | +0.55 / +0.54 | both halves | 1e-05 | pathway: Muscle contraction |
| [[DENND3]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01134]] | -0.48 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[UNC119B]] | -0.47 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[DPY19L3-DT]] | -0.47 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ZNF460-AS1]] | -0.46 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[PLPP5]] | -0.46 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[PACRGL]] | -0.46 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[SPRYD4]] | -0.46 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[KMT2E-AS1]] | -0.45 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[ZNF213-AS1]] | -0.45 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[LINC00938]] | -0.45 | -0.33 / -0.29 | both halves | 3e-04 |  |
| [[PNISR-AS1]] | -0.45 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[TSTD3]] | -0.45 | -0.33 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ATP2B4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EHD2]] | B | EHD2 activity raises ATP2B4's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 3.28× lower at baseline in the lines without EHD2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[LINC01139]] | B | LINC01139 activity lowers ATP2B4's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.31× higher at baseline in the lines without LINC01139 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |
| [[CAPG]] | B | CAPG activity raises ATP2B4's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.12× lower at baseline in the lines without CAPG | 0.074 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[FLNB]] | C | FLNB activity raises ATP2B4's level | lines that do not express FLNB (3) vs lines expressing it (47) | 4.08× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAST]] | B | ATP2B4 activity raises CAST's level | lines that do not express ATP2B4 (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without ATP2B4 | 0.022 | ⚠ within organs, on part of the lines; also absent: PROCR, ARSJ, LAMB1 |
| [[AKAP13]] | B | ATP2B4 activity raises AKAP13's level | lines that do not express ATP2B4 (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without ATP2B4 | 0.071 | ⚠ within organs, on part of the lines; also absent: PROCR, ARSJ, LAMB1 |
| [[RTN2]] | B | ATP2B4 activity lowers RTN2's level | lines that do not express ATP2B4 (8) vs lines expressing it (42) | 1.47× higher at baseline in the lines without ATP2B4 | 0.078 | ⚠ within organs, on part of the lines; also absent: PROCR, ARSJ, LAMB1 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.3, 11.8); signed map (12.5, 30.9). **Vector** length 154, 51.8% of its response variance represented; |z| ≥ 3 in 2,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.1 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.9 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.8 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.4 | +6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.3 | +7.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +7.4 | +9.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.9 | +6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.8 | +6.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.1 | -11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -27.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.1 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -10.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | -5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.8 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | ATPase plasma membrane Ca2+ transporting 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:203,626,832-203,744,081 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PMCA4; previously ATP2B2, MXRA1 |
| Gene groups (HGNC) | ATPases Ca2+ transporting; Small nucleolar RNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_DN, ESTROGEN_RESPONSE_LATE |
| Reactome | 10 pathways, smallest: Reduction of cytosolic Ca++ levels; Platelet calcium homeostasis; Ion homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P23634](https://www.uniprot.org/uniprotkb/P23634) (Plasma membrane calcium-transporting ATPase 4):

> Calcium/calmodulin-regulated and magnesium-dependent enzyme that catalyzes the hydrolysis of ATP coupled with the transport of calcium out of the cell. By regulating sperm cell calcium homeostasis, may play a role in sperm motility (By similarity).

**Summary**, from NCBI Gene [493](https://www.ncbi.nlm.nih.gov/gene/493):

> The protein encoded by this gene belongs to the family of P-type primary ion transport ATPases characterized by the formation of an aspartyl phosphate intermediate during the reaction cycle. These enzymes remove bivalent calcium ions from eukaryotic cells against very large concentration gradients and play a critical role in intracellular calcium homeostasis. The mammalian plasma membrane calcium ATPase isoforms are encoded by at least four separate genes and the diversity of these enzymes is …

**Accessions** — [HGNC:817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:817) · Entrez [493](https://www.ncbi.nlm.nih.gov/gene/493) · UniProt [P23634](https://www.uniprot.org/uniprotkb/P23634) · Ensembl [ENSG00000058668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058668)

## Data

Gene col 664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 664); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 664]; `tensor/DDL_lfc|DDL_z.npy` [664]; `embed/gene_vectors.npy` [664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 664 or target_col == 664). Every well: [[ATP2B4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP2B4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
