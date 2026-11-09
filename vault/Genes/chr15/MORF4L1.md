---
symbol: "MORF4L1"
type: "gene"
col: 11731
ensembl_id: "ENSG00000185787"
name: "mortality factor 4 like 1"
location: "15q25.1"
module: 25
arm: "+"
pooled_cpm: 169.41
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MORF4L1

*mortality factor 4 like 1* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.34× (z +16.6, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.627× (z -14.3, q 7e-44, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD23B]] (+0.64, fdr 7e-06), [[PRPF8]] (+0.62, fdr 1e-05), [[PAPOLA]] (+0.61, fdr 1e-05); moves opposite to [[FBXO45]] (-0.69, fdr 3e-05), [[ORAI1]] (-0.64, fdr 1e-05), [[ZNF593]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.34×** | +16.6 | 0e+00 | 48/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +14.5 | 3e-45 | 44/49 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +14.3 | 7e-44 | 40/44 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.83×** | +11.8 | 8e-30 | 44/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +11.4 | 7e-28 | 7/50 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +11.1 | 8e-27 | 42/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +9.1 | 6e-18 | 41/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +9.0 | 2e-17 | 35/45 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +8.2 | 2e-14 | 42/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +6.9 | 3e-10 | 32/48 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 2e-09 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 6e-07 | 31/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +5.1 | 1e-05 | 30/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +4.7 | 9e-05 | 28/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.001 | 24/48 (HT-29, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11731.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -14.3 | 7e-44 | 45/49 (RKO, HCT15, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.520×** | -14.2 | 3e-43 | 45/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.559×** | -12.6 | 3e-34 | 46/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.637×** | -9.8 | 2e-20 | 45/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.644×** | -9.3 | 2e-18 | 44/48 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.695×** | -7.6 | 3e-12 | 39/48 (SW480, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.714×** | -7.3 | 2e-11 | 42/48 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.739×** | -6.3 | 2e-08 | 35/47 (LoVo, HT-29, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.747×** | -6.1 | 7e-08 | 32/50 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.608×** | -5.6 | 9e-07 | 38/49 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -4.9 | 4e-05 | 18/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.802×** | -4.8 | 7e-05 | 35/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.842× | -3.7 | 0.007 | 22/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.842× | -3.7 | 0.007 | 22/48 (J82, A549, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.871× | -3.0 | 0.096 | 6/48 (NCI-H2030, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 183 | 11 (6 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +23.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +18.1) | [[Belinostat (drug)]] 5 µM 0.497× (z -13.2) |
| [[SW480 (line)]] | alt | 145 | 10 (5 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.45× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 187 | 7 (4 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 10.8× (z +20.1) | [[Panobinostat (drug)]] 5 µM 0.450× (z -12.9) |
| [[HOP62 (line)]] | alt | 181 | 4 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +18.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.97× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.431× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 121 | 7 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.7) | [[Belinostat (drug)]] 5 µM 0.501× (z -10.2) |
| [[LoVo (line)]] | wt | 201 | 4 (2 ⚠) | 5 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +15.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.15× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -11.9) |
| [[SW 900 (line)]] | alt | 152 | 3 (1 ⚠) | 6 | [[TAK-901 (drug)]] 5 µM 4.61× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.357× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 152 | 5 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 5.13× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -11.1) |
| [[KATO III (line)]] | alt | 230 | 6 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 267 | 5 (3 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 6.64× (z +13.6) | [[Belinostat (drug)]] 5 µM 0.489× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 155 | 2 (1 ⚠) | 5 | [[TAK-901 (drug)]] 5 µM 6.46× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.364× (z -14.5) |
| [[HT-29 (line)]] | alt | 223 | 4 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.36× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -13.1) |
| [[A-172 (line)]] | wt | 150 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.58× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.514× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 208 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.99× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 146 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.0) | — |
| [[A498 (line)]] | wt | 191 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 4.34× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.5) |
| [[A549 (line)]] | wt | 219 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.85× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.530× (z -9.4) |
| [[C32 (line)]] | wt | 115 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 6.65× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 139 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 238 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.477× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 132 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.83× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 163 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +13.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 178 | 2 (1 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 4.34× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.445× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 107 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +10.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.433× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 260 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.373× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 140 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.54× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.477× (z -10.0) |
| [[RKO (line)]] | wt | 139 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 7.23× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.0) |
| [[SW48 (line)]] | wt | 143 | 3 | 1 | [[TAK-901 (drug)]] 0.05 µM 3.01× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -10.9) |
| [[A-427 (line)]] | wt | 109 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.22× (z +9.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.482× (z -9.4) |
| [[COLO 205 (line)]] | alt | 190 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.00× (z +14.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.61× (z +10.0) | — |
| [[H4 (line)]] | wt | 202 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.405× (z -9.9) |
| [[HCT15 (line)]] | alt | 240 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 4.93× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -13.6) |
| [[HS-578T (line)]] | alt | 146 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.02× (z +9.4) | — |
| [[J82 (line)]] | alt | 168 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 3.68× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -9.5) |
| [[SHP-77 (line)]] | alt | 158 | 2 (2 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.22× (z +9.5) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 164 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.82× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 159 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.09× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 150 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.10× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +10.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 142 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -12.8) |
| [[C-33 A (line)]] | alt | 160 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 125 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.84× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 166 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.14× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD23B]] | +0.64 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.62 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[PAPOLA]] | +0.61 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[CDC42]] | +0.60 | +0.43 / +0.72 | both halves | 3e-05 |  |
| [[SUMO1]] | +0.59 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.58 | +0.36 / +0.68 | both halves | 1e-04 |  |
| [[PPP1CB]] | +0.58 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.57 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[UBQLN1]] | +0.57 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.57 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[VAMP7]] | +0.57 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PCBP2]] | +0.57 | +0.35 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO45]] | -0.69 | -0.44 / -0.80 | both halves | 3e-05 |  |
| [[ORAI1]] | -0.64 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.62 | -0.41 / -0.72 | both halves | 4e-05 |  |
| [[PLEKHJ1]] | -0.62 | -0.43 / -0.67 | both halves | 4e-05 |  |
| [[NR2C2AP]] | -0.59 | -0.28 / -0.68 | both halves | 3e-04 |  |
| [[MRPL36]] | -0.58 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[EMC6]] | -0.56 | -0.21 / -0.70 | both halves | 6e-04 |  |
| [[TRAPPC4]] | -0.55 | -0.27 / -0.72 | both halves | 3e-04 |  |
| [[MSX1]] | -0.55 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[CCDC137]] | -0.54 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[ENDOG]] | -0.54 | -0.37 / -0.62 | both halves | 8e-05 |  |
| [[SCLY]] | -0.54 | -0.57 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MORF4L1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MORF4L1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.7, -23.9); signed map (-24.2, -33.3). **Vector** length 93.4, 31.7% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +12.5 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.4 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +11.2 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | -2.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +16.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +11.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.5 | +0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | -0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -7.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | mortality factor 4 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,810,487-78,898,139 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRG15, MORFRG15, HsT17725, Eaf3, MEAF3 |
| Gene groups (HGNC) | EMSY complex; Tip60/Nua4 histone acetyltransferase complex subunits |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBU8](https://www.uniprot.org/uniprotkb/Q9UBU8) (Mortality factor 4-like protein 1):

> Component of the NuA4 histone acetyltransferase (HAT) complex which is involved in transcriptional activation of select genes principally by acetylation of nucleosomal histones H4 and H2A. This modification may both alter nucleosome - DNA interactions and promote interaction of the modified histones with other proteins which positively regulate transcription. This complex may be required for the activation of transcriptional programs associated with oncogene and proto-oncogene mediated growth …

**Summary**, from NCBI Gene [10933](https://www.ncbi.nlm.nih.gov/gene/10933):

> Predicted to enable chromatin binding activity. Involved in double-strand break repair via homologous recombination; positive regulation of double-strand break repair via homologous recombination; and regulation of cell cycle. Located in nuclear speck. Part of NuA4 histone acetyltransferase complex and Sin3-type complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16989) · Entrez [10933](https://www.ncbi.nlm.nih.gov/gene/10933) · UniProt [Q9UBU8](https://www.uniprot.org/uniprotkb/Q9UBU8) · Ensembl [ENSG00000185787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185787)

## Data

Gene col 11731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11731); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11731]; `tensor/DDL_lfc|DDL_z.npy` [11731]; `embed/gene_vectors.npy` [11731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11731 or target_col == 11731). Every well: [[MORF4L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORF4L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
