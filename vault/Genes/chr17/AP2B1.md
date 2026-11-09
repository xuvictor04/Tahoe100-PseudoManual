---
symbol: "AP2B1"
type: "gene"
col: 104
ensembl_id: "ENSG00000006125"
name: "adaptor related protein complex 2 subunit beta 1"
location: "17q12"
module: 20
arm: "+"
pooled_cpm: 316.44
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# AP2B1

*adaptor related protein complex 2 subunit beta 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +17.1, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.38× (z +8.4, q 5e-15, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.566× (z -14.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCSTN]] (+0.63, fdr 1e-05), [[SELENOF]] (+0.61, fdr 1e-05), [[PPIP5K2]] (+0.60, fdr 3e-05); moves opposite to [[MRPL36]] (-0.61, fdr 2e-05), [[MRPL14]] (-0.60, fdr 2e-04), [[FOXA2]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +17.1 | 0e+00 | 48/49 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +13.6 | 6e-40 | 41/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +11.0 | 6e-26 | 39/45 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +8.4 | 5e-15 | 35/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +7.4 | 1e-11 | 34/48 (C32, A-427, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.9 | 4e-10 | 30/50 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +6.7 | 2e-09 | 36/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +6.5 | 5e-09 | 31/48 (C32, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +6.2 | 5e-08 | 35/48 (C32, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.8 | 5e-07 | 26/48 (A-172, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +5.0 | 3e-05 | 24/48 (LoVo, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +4.7 | 1e-04 | 12/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | 1.18× | +4.3 | 8e-04 | 23/48 (NCI-H23, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.002 | 29/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.0 | 0.002 | 21/38 (A-172, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Gallic acid (drug)]] 5 µM |  | 1.10× | +3.7 | 0.008 | 2/48 (H4, SW 1271) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.2 | 0.032 | 6/49 (HT-29, KATO III, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.037 | 12/49 (A498, BT-474, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.041 | 9/47 (SW480, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.081 | 20/48 (HT-29, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -14.9 | 0e+00 | 48/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.607×** | -13.0 | 2e-36 | 48/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.628×** | -12.2 | 9e-32 | 47/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.799×** | -8.3 | 2e-14 | 26/48 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -7.7 | 2e-12 | 26/48 (A-427, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.745×** | -7.7 | 2e-12 | 39/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.740×** | -7.5 | 4e-12 | 33/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.788×** | -6.2 | 4e-08 | 35/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.815×** | -4.9 | 5e-05 | 25/48 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.2 | 0.001 | 21/48 (HEC-1-A, SNU-423, …) | top dose only | composition shift |
| [[Ritonavir (drug)]] 0.5 µM |  | 0.845× | -4.0 | 0.003 | 18/48 (CHP-212, SNU-423, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.860× | -3.9 | 0.004 | 14/48 (BT-474, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.829×** | -3.5 | 0.021 | 22/48 (RPMI-7951, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.911× | -3.4 | 0.028 | 6/48 (A498, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.882× | -3.2 | 0.044 | 10/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 0.884× | -3.2 | 0.049 | 10/48 (SW 1088, C32, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.797×** | -3.1 | 0.067 | 21/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.888× | -3.1 | 0.067 | 9/49 (PANC-1, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 287 | 4 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -20.3) |
| [[HEC-1-A (line)]] | alt | 420 | 2 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.65× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.595× (z -14.1) |
| [[PANC-1 (line)]] | alt | 589 | 2 (2 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +11.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.300× (z -19.3) |
| [[SW480 (line)]] | alt | 214 | 4 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.517× (z -14.0) |
| [[A-427 (line)]] | wt | 302 | 6 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.70× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.612× (z -9.0) |
| [[LoVo (line)]] | wt | 214 | 5 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.518× (z -12.2) |
| [[A549 (line)]] | wt | 422 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +16.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.479× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 367 | 4 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 249 | 4 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.518× (z -11.6) |
| [[A498 (line)]] | wt | 513 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.549× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 429 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.557× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 209 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -11.7) |
| [[A-172 (line)]] | wt | 302 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 182 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 216 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.422× (z -13.4) |
| [[SNU-423 (line)]] | alt | 225 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.90× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.571× (z -12.8) |
| [[SW 900 (line)]] | alt | 277 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.438× (z -12.7) |
| [[C32 (line)]] | wt | 212 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.98× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 356 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -11.8) |
| [[HS-578T (line)]] | alt | 237 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +13.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.569× (z -8.7) |
| [[HT-29 (line)]] | alt | 325 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.60× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.610× (z -8.9) |
| [[J82 (line)]] | alt | 193 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.87× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 835 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.510× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 303 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +13.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.607× (z -8.6) |
| [[RKO (line)]] | wt | 278 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +18.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.426× (z -14.1) |
| [[H4 (line)]] | wt | 286 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.424× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 167 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 215 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -14.7) |
| [[LOX-IMVI (line)]] | wt | 336 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.494× (z -12.2) |
| [[LS 180 (line)]] | wt | 306 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 279 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +11.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 200 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 256 | 2 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.2) |
| [[BT-474 (line)]] | alt | 261 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.465× (z -10.3) |
| [[C-33 A (line)]] | alt | 226 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +12.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 219 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.00× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 301 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +12.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 230 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -10.4) |
| [[KATO III (line)]] | alt | 307 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 248 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 221 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.655× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 265 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 221 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.592× (z -8.9) |
| [[CHP-212 (line)]] | wt | 227 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 285 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 355 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCSTN]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 | pathway: EPH-Ephrin signaling |
| [[SELENOF]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PPIP5K2]] | +0.60 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[OGT]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PAPOLA]] | +0.58 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[CTTN]] | +0.57 | +0.42 / +0.64 | both halves | 4e-05 | pathway: Clathrin-mediated endocytosis |
| [[PGRMC1]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MTPN]] | +0.57 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CSDE1]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[FKBP9]] | +0.55 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GHITM]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[EMC1]] | +0.54 | +0.43 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 8 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL36]] | -0.61 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[MRPL14]] | -0.60 | -0.30 / -0.66 | both halves | 2e-04 |  |
| [[FOXA2]] | -0.58 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[ZNF593]] | -0.57 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[ZNF503]] | -0.56 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[KRI1]] | -0.56 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[LSM2]] | -0.55 | -0.16 / -0.67 | ⚠ one half (not replicated) | 0.001 |  |
| [[ORAI1]] | -0.55 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[KRTCAP2]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[SAC3D1]] | -0.55 | -0.27 / -0.61 | both halves | 3e-04 |  |
| [[EMC6]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[C15orf61]] ⚠ | -0.55 | -0.20 / -0.66 | both halves | 7e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MTRES1]] | -0.54 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[PUS3]] | -0.54 | -0.25 / -0.67 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises AP2B1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises AP2B1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | AP2B1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | AP2B1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | AP2B1's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | AP2B1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-46.6, -12.2); signed map (-20.2, -31.6). **Vector** length 118, 39.0% of its response variance represented; |z| ≥ 3 in 1,378 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +7.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.8 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -0.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.6 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +1.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.9 | -7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -8.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.1 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -7.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 2 subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,578,046-35,726,413 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ADTB2, CLAPB1 |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 2 |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 43 pathways, smallest: Nef Mediated CD8 Down-regulation; Nef Mediated CD4 Down-regulation; WNT5A-dependent internalization of FZD2, FZD5 and ROR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P63010](https://www.uniprot.org/uniprotkb/P63010) (AP-2 complex subunit beta):

> Component of the adaptor protein complex 2 (AP-2). Adaptor protein complexes function in protein transport via transport vesicles in different membrane traffic pathways. Adaptor protein complexes are vesicle coat components and appear to be involved in cargo selection and vesicle formation. AP-2 is involved in clathrin-dependent endocytosis in which cargo proteins are incorporated into vesicles surrounded by clathrin (clathrin-coated vesicles, CCVs) which are destined for fusion with the early …

**Summary**, from NCBI Gene [163](https://www.ncbi.nlm.nih.gov/gene/163):

> The protein encoded by this gene is one of two large chain components of the assembly protein complex 2, which serves to link clathrin to receptors in coated vesicles. The encoded protein is found on the cytoplasmic face of coated vesicles in the plasma membrane. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:563) · Entrez [163](https://www.ncbi.nlm.nih.gov/gene/163) · UniProt [P63010](https://www.uniprot.org/uniprotkb/P63010) · Ensembl [ENSG00000006125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006125)

## Data

Gene col 104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 104); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 104]; `tensor/DDL_lfc|DDL_z.npy` [104]; `embed/gene_vectors.npy` [104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 104 or target_col == 104). Every well: [[AP2B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP2B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
