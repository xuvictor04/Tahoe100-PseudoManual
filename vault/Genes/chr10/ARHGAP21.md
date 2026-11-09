---
symbol: "ARHGAP21"
type: "gene"
col: 2890
ensembl_id: "ENSG00000107863"
name: "Rho GTPase activating protein 21"
location: "10p12.1"
module: 11
arm: "-"
pooled_cpm: 207.33
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ARHGAP21

*Rho GTPase activating protein 21* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.34× (z +6.7, q 1e-08, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.25× (z +5.4, q 2e-05, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.278× (z -30.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARGE1]] (+0.57, fdr 2e-04), [[TSPAN17]] (+0.54, fdr 7e-06), [[PINK1]] (+0.53, fdr 3e-05); moves opposite to [[MRPL1]] (-0.52, fdr 1e-05), [[ZNF45]] (-0.51, fdr 4e-05), [[DRG2]] (-0.51, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IRAK3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +6.7 | 1e-08 | 36/47 (RKO, SW48, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +5.4 | 2e-05 | 30/47 (RKO, SW48, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +4.8 | 4e-04 | 26/48 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +4.6 | 7e-04 | 15/48 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +4.3 | 0.002 | 23/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.7 | 0.019 | 7/48 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.044 | 20/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.050 | 20/48 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.3 | 0.050 | 16/49 (CFPAC-1, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.050 | 16/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.056 | 18/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.056 | 18/48 (C32, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.056 | 14/48 (HT-29, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.056 | 14/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.061 | 18/48 (NCI-H1573, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.10× | +3.1 | 0.061 | 4/49 (NCI-H2030, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.278×** | -30.6 | 0e+00 | 48/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.304×** | -28.4 | 0e+00 | 48/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.393×** | -22.3 | 0e+00 | 48/48 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.578×** | -18.5 | 0e+00 | 42/48 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.477×** | -17.7 | 0e+00 | 45/49 (RKO, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.498×** | -16.0 | 0e+00 | 40/44 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.517×** | -14.5 | 1e-45 | 41/45 (RKO, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.578×** | -12.6 | 1e-34 | 39/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -12.0 | 3e-31 | 41/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.667×** | -9.7 | 2e-20 | 33/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.763×** | -9.1 | 4e-18 | 31/48 (C32, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.738×** | -7.3 | 2e-11 | 35/48 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -6.5 | 3e-09 | 30/48 (C32, hTERT-HPNE, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.616×** | -6.1 | 6e-08 | 36/48 (RKO, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.784×** | -5.8 | 2e-07 | 25/48 (A-172, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -5.7 | 5e-07 | 23/48 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.670×** | -5.0 | 2e-05 | 28/49 (A-172, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -4.7 | 6e-05 | 25/49 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.691×** | -4.6 | 1e-04 | 26/48 (LoVo, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.825×** | -4.6 | 1e-04 | 25/49 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.826×** | -4.6 | 1e-04 | 23/48 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 203 | 6 (3 ⚠) | 9 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.46× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0553× (z -39.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 196 | 7 (7 ⚠) | 7 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.48× (z +18.1) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -22.1) |
| [[NCI-H1573 (line)]] | alt | 235 | 1 (1 ⚠) | 12 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -20.3) |
| [[A-172 (line)]] | wt | 225 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -34.3) |
| [[C32 (line)]] | wt | 207 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -16.7) |
| [[A549 (line)]] | wt | 260 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -20.8) |
| [[CFPAC-1 (line)]] | alt | 217 | 6 (3 ⚠) | 5 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.07× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.337× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 310 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -24.9) |
| [[AN3 CA (line)]] | alt | 524 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -17.8) |
| [[HS-578T (line)]] | alt | 172 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.263× (z -18.3) |
| [[hTERT-HPNE (line)]] | wt | 608 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 125 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -21.0) |
| [[HepG2_C3A (line)]] | wt | 310 | 1 (1 ⚠) | 8 (3 ⚠) | [[Daptomycin (drug)]] 5 µM 2.91× (z +11.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -20.2) |
| [[LoVo (line)]] | wt | 297 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -20.7) |
| [[SK-MEL-2 (line)]] | alt | 257 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -19.7) |
| [[SW48 (line)]] | wt | 236 | 2 (1 ⚠) | 7 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.56× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -19.0) |
| [[A498 (line)]] | wt | 182 | 2 (1 ⚠) | 6 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.13× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.508× (z -10.5) |
| [[Hs 766T (line)]] | wt | 408 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -20.1) |
| [[AsPC-1 (line)]] | alt | 335 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -25.8) |
| [[HOP62 (line)]] | alt | 194 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -17.1) |
| [[LS 180 (line)]] | wt | 353 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -24.0) |
| [[NCI-H1792 (line)]] | alt | 299 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -18.5) |
| [[A-427 (line)]] | wt | 118 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.417× (z -16.9) |
| [[BT-474 (line)]] | alt | 110 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -18.7) |
| [[J82 (line)]] | alt | 169 | 1 (1 ⚠) | 5 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.08× (z +11.4) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.336× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 206 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.620× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 194 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -20.0) |
| [[Panc 03.27 (line)]] | alt | 165 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -16.7) |
| [[SNU-1 (line)]] | wt | 179 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.270× (z -15.5) |
| [[SW480 (line)]] | alt | 133 | 2 | 4 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.58× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.311× (z -18.1) |
| [[COLO 205 (line)]] | alt | 132 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.214× (z -15.8) |
| [[HT-29 (line)]] | alt | 245 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.214× (z -19.7) |
| [[KATO III (line)]] | alt | 217 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -20.8) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 2 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -11.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.459× (z -9.1) |
| [[SHP-77 (line)]] | alt | 168 | 1 | 4 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.04× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -12.3) |
| [[SNU-423 (line)]] | alt | 183 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -17.8) |
| [[H4 (line)]] | wt | 178 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -11.1) |
| [[CHP-212 (line)]] | wt | 144 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 77.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.8) |
| [[PANC-1 (line)]] | alt | 147 | 1 (1 ⚠) | 2 (2 ⚠) | [[Daptomycin (drug)]] 5 µM 1.66× (z +9.1) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.514× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 144 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -11.5) |
| [[SW1417 (line)]] | alt | 175 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -16.4) |
| [[C-33 A (line)]] | alt | 122 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -13.8) |
| [[NCI-H661 (line)]] | alt | 246 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 219 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -11.8) |
| [[HCT15 (line)]] | alt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -9.9) |
| [[SW 1271 (line)]] | alt | 237 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.1) |
| [[NCI-H2122 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARGE1]] | +0.57 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[TSPAN17]] | +0.54 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PINK1]] | +0.53 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[SERINC5]] | +0.50 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[RAPGEF2]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 | same gene group |
| [[GPR161]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[SRGAP2C]] | +0.49 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ACVR1]] | +0.49 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[C17orf67]] | +0.49 | +0.29 / +0.48 | both halves | 3e-04 |  |
| [[DGKE]] | +0.49 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[PRPSAP1]] | +0.49 | +0.17 / +0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[DOP1B]] | +0.49 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.49 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL1]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ZNF45]] | -0.51 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[DRG2]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ARMCX5]] | -0.51 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[PIGB]] | -0.51 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[RNF40]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ZNF182]] | -0.50 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[JPH2]] | -0.50 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[AAAS]] | -0.49 | -0.41 / -0.55 | both halves | 4e-05 | pathway: RHOA GTPase cycle |
| [[RBM18]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PICK1]] | -0.49 | -0.34 / -0.42 | both halves | 1e-04 | same gene group |
| [[PRPF3]] | -0.49 | -0.29 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAK3]] | B | IRAK3 activity raises ARHGAP21's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 1.41× lower at baseline in the lines without IRAK3 | 0.094 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5 |
| [[SESTD1]] | C | SESTD1 activity raises ARHGAP21's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without SESTD1 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.242). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.3, 14.9); signed map (-15.4, 15.9). **Vector** length 110, 37.5% of its response variance represented; |z| ≥ 3 in 1,893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +14.3 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +10.5 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +10.1 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.9 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.6 | +5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -12.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.9 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.8 | -4.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.4 | -9.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.3 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.8 | -0.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.7 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:24,583,609-24,723,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1424, ARHGAP10 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho GTPase activating proteins; PDZ domain containing |
| Reactome | 16 pathways, smallest: RND3 GTPase cycle; RHOF GTPase cycle; RHOD GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T5U3](https://www.uniprot.org/uniprotkb/Q5T5U3) (Rho GTPase-activating protein 21):

> Functions as a GTPase-activating protein (GAP) for RHOA and CDC42. Downstream partner of ARF1 which may control Golgi apparatus structure and function. Also required for CTNNA1 recruitment to adherens junctions.

**Summary**, from NCBI Gene [57584](https://www.ncbi.nlm.nih.gov/gene/57584):

> ARHGAP21 functions preferentially as a GTPase-activating protein (GAP) for CDC42 (MIM 116952) and regulates the ARP2/3 complex (MIM 604221) and F-actin dynamics at the Golgi through control of CDC42 activity (Dubois et al., 2005 [PubMed 15793564]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23725) · Entrez [57584](https://www.ncbi.nlm.nih.gov/gene/57584) · UniProt [Q5T5U3](https://www.uniprot.org/uniprotkb/Q5T5U3) · Ensembl [ENSG00000107863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107863)

## Data

Gene col 2890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2890); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2890]; `tensor/DDL_lfc|DDL_z.npy` [2890]; `embed/gene_vectors.npy` [2890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2890 or target_col == 2890). Every well: [[ARHGAP21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
