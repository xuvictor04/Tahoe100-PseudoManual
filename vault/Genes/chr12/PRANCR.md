---
symbol: "PRANCR"
type: "gene"
col: 15067
ensembl_id: "ENSG00000257815"
name: "progenitor renewal associated non-coding RNA"
location: "12q15"
module: 23
arm: "+"
pooled_cpm: 40.93
n_lines_expressing: 49
n_dd_up: 35
n_dd_down: 32
n_dd_up_clean: 34
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PRANCR

*progenitor renewal associated non-coding RNA* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.83× (z +22.8, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (18 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.291× (z -11.3, q 8e-27, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.436× (z -7.6, q 3e-12, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHD1-DT]] (+0.87, fdr 7e-06), [[ANKRD17-DT]] (+0.82, fdr 7e-06), [[ATE1OSP]] (+0.81, fdr 7e-06); moves opposite to [[SH3PXD2B]] (-0.65, fdr 4e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.83×** | +22.8 | 0e+00 | 45/47 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.10×** | +14.3 | 5e-44 | 46/47 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +10.9 | 4e-25 | 42/48 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.62×** | +8.8 | 2e-16 | 42/47 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +6.0 | 3e-07 | 29/44 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +5.6 | 2e-06 | 29/47 (A-172, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.53×** | +5.3 | 1e-05 | 32/47 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +5.0 | 3e-05 | 31/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.0 | 3e-05 | 29/47 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.82×** | +5.0 | 3e-05 | 31/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.70×** | +4.8 | 7e-05 | 34/47 (RKO, C-33 A, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.69×** | +4.8 | 9e-05 | 30/47 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.60×** | +4.3 | 9e-04 | 26/47 (KATO III, COLO 205, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.58×** | +4.2 | 0.001 | 27/46 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 21/46 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.004 | 23/47 (LoVo, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.291×** | -11.3 | 8e-27 | 42/47 (LS 180, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.327×** | -10.2 | 4e-22 | 37/46 (LS 180, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.348×** | -9.7 | 9e-20 | 43/47 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.382×** | -8.5 | 3e-15 | 34/45 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.436×** | -7.6 | 3e-12 | 37/47 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.453×** | -7.3 | 4e-11 | 37/47 (HT-29, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.443×** | -6.8 | 1e-09 | 37/47 (C32, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.487×** | -6.6 | 3e-09 | 35/47 (HT-29, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.274×** | -6.0 | 1e-07 | 30/45 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.492×** | -5.9 | 2e-07 | 35/47 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.502×** | -5.7 | 5e-07 | 36/47 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.507×** | -5.7 | 7e-07 | 32/47 (LS 180, C32, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.312×** | -5.4 | 2e-06 | 33/48 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.544×** | -5.1 | 2e-05 | 29/46 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.558×** | -5.1 | 2e-05 | 30/46 (HT-29, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.354×** | -4.8 | 5e-05 | 36/46 (HT-29, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.357×** | -4.8 | 5e-05 | 26/46 (HT-29, A498, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.429×** | -3.9 | 0.002 | 27/46 (Hs 766T, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.433×** | -3.9 | 0.002 | 24/46 (NCI-H23, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.646×** | -3.8 | 0.004 | 24/46 (Hs 766T, SW48, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.564×** | -3.7 | 0.004 | 23/47 (SNU-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.683×** | -3.5 | 0.010 | 22/47 (C32, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.525×** | -3.0 | 0.053 | 15/46 (HT-29, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.736×** | -2.8 | 0.086 | 11/47 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.62 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 214 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.4) |
| [[HT-29 (line)]] | alt | 71.1 | 3 | 8 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.128× (z -12.8) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.169× (z -10.4) |
| [[LS 180 (line)]] | wt | 178 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0492× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.375× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 49.4 | 6 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.63× (z +18.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -13.9) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 30.4 | 2 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -9.9) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 29.1 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.181× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[COLO 205 (line)]] | alt | 66.9 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +14.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0970× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 15.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +19.5) | — |
| [[C-33 A (line)]] | alt | 49.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.194× (z -9.8) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 0.0489× (z -9.2) |
| [[Hs 766T (line)]] | wt | 31.2 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +15.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -9.4) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 32.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.80× (z +10.8) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 13.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +18.6) | — |
| [[A498 (line)]] | wt | 136 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 35.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.110× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 17.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.98× (z +17.0) | — |
| [[KATO III (line)]] | alt | 59.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 39.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 33.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.05× (z +16.2) | — |
| [[NCI-H1573 (line)]] | alt | 41.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.122× (z -11.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 14.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.83× (z +15.2) | — |
| [[RKO (line)]] | wt | 33.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +14.5) | — |
| [[A-172 (line)]] | wt | 22.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 11.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +12.9) | — |
| [[HCT15 (line)]] | alt | 38.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 40.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.34× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 16.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.23× (z +13.9) | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 27.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 12.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +15.9) | — |
| [[SW 900 (line)]] | alt | 30.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.07× (z +13.4) | — |
| [[A549 (line)]] | wt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +12.4) | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +16.0) | — |
| [[H4 (line)]] | wt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +8.5) | — |
| [[J82 (line)]] | alt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.16× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +16.8) | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.6) | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD1-DT]] | +0.87 | +0.84 / +0.72 | both halves | 7e-06 |  |
| [[ANKRD17-DT]] | +0.82 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.81 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[SPESP1]] | +0.80 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.79 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[TAS2R4]] | +0.79 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[UFL1-AS1]] | +0.79 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[BDNF-AS]] | +0.78 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[MGAM]] | +0.78 | +0.85 / +0.52 | both halves | 1e-05 |  |
| [[HEXIM2-AS1]] | +0.77 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.76 | +0.77 / +0.45 | both halves | 3e-05 |  |
| [[INTS6-AS1]] | +0.76 | +0.78 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.65 | -0.65 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRANCR's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.842). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.2, 17.3); signed map (26.6, -7.7). **Vector** length 129, 44.9% of its response variance represented; |z| ≥ 3 in 1,535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.0 | +22.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +14.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.3 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +5.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.9 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.0 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +5.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.5 | +2.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -8.9 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -8.9 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -8.5 | -7.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.5 | -5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.1 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.6 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | +0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | progenitor renewal associated non-coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q15 — chr12:69,901,918-70,243,405 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC01481, CNOT2-DT |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51126) · Entrez [101928062](https://www.ncbi.nlm.nih.gov/gene/101928062) · Ensembl [ENSG00000257815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257815)

## Data

Gene col 15067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15067); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15067]; `tensor/DDL_lfc|DDL_z.npy` [15067]; `embed/gene_vectors.npy` [15067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15067 or target_col == 15067). Every well: [[PRANCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRANCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
