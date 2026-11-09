---
symbol: "KLHL24"
type: "gene"
col: 3590
ensembl_id: "ENSG00000114796"
name: "kelch like family member 24"
location: "3q27.1"
module: 69
arm: "+"
pooled_cpm: 154.51
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 33
n_dd_up_clean: 33
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# KLHL24

*kelch like family member 24* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.68× (z +15.8, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.0862× (z -39.3, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.0978× (z -18.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREBRF]] (+0.85, fdr 7e-06), [[TCP11L2]] (+0.80, fdr 7e-06), [[RB1CC1]] (+0.80, fdr 7e-06); moves opposite to [[AGK]] (-0.67, fdr 7e-06), [[PDSS1]] (-0.64, fdr 7e-06), [[NAA15]] (-0.64, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.68×** | +15.8 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +12.0 | 8e-31 | 43/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +10.6 | 6e-24 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +8.6 | 1e-15 | 35/49 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +8.4 | 5e-15 | 36/48 (J82, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +7.7 | 1e-12 | 39/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +7.5 | 5e-12 | 34/48 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.95×** | +5.4 | 5e-06 | 40/50 (BT-474, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 3e-05 | 28/48 (PANC-1, H4, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.26×** | +5.0 | 4e-05 | 31/48 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | **1.25×** | +4.8 | 7e-05 | 31/49 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.5 | 3e-04 | 36/48 (PANC-1, NCI-H460, …) | all doses, flat | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 5e-04 | 32/49 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.3 | 6e-04 | 25/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.3 | 6e-04 | 26/50 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.001 | 26/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.67×** | +4.2 | 0.001 | 31/49 (BT-474, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 26/48 (A-172, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.0862×** | -39.3 | 0e+00 | 48/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.0978×** | -18.8 | 0e+00 | 48/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.136×** | -16.1 | 0e+00 | 48/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.144×** | -15.6 | 0e+00 | 47/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.173×** | -14.1 | 3e-43 | 47/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.176×** | -14.0 | 1e-42 | 47/48 (NCI-H2347, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.402×** | -13.5 | 1e-39 | 41/45 (HT-29, SNU-423, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.471×** | -11.4 | 4e-28 | 45/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.350×** | -11.0 | 3e-26 | 47/48 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.524×** | -9.9 | 2e-21 | 40/43 (A-172, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.541×** | -9.8 | 4e-21 | 39/49 (SK-MEL-2, NCI-H1792, …) | all doses, flat | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.366×** | -8.1 | 3e-14 | 44/47 (Hs 766T, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.526×** | -6.7 | 8e-10 | 45/49 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.646×** | -6.6 | 2e-09 | 40/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.455×** | -6.4 | 8e-09 | 30/38 (NCI-H2347, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.570×** | -5.9 | 2e-07 | 43/48 (NCI-H1792, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.730×** | -4.8 | 4e-05 | 31/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.744×** | -4.7 | 7e-05 | 28/48 (SW480, COLO 205, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.769×** | -4.2 | 8e-04 | 30/49 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.774×** | -4.1 | 0.001 | 27/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 106 | 9 (3 ⚠) | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.04× (z +23.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0851× (z -27.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0745× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 183 | 4 (1 ⚠) | 12 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +15.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0865× (z -30.2) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0728× (z -16.2) |
| [[PANC-1 (line)]] | alt | 147 | 4 (1 ⚠) | 11 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +16.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0809× (z -29.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0693× (z -15.8) |
| [[SW 900 (line)]] | alt | 179 | 4 (1 ⚠) | 10 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.102× (z -23.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0677× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 272 | 0 | 12 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0367× (z -37.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0436× (z -17.7) |
| [[NCI-H2347 (line)]] | alt | 298 | 1 | 11 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0599× (z -37.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0454× (z -20.6) |
| [[SW480 (line)]] | alt | 129 | 3 (1 ⚠) | 9 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0646× (z -32.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0696× (z -15.7) |
| [[BT-474 (line)]] | alt | 158 | 9 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.58× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.55× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -13.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0941× (z -10.5) |
| [[COLO 205 (line)]] | alt | 238 | 3 (1 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.37× (z +14.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0705× (z -23.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0702× (z -11.8) |
| [[KATO III (line)]] | alt | 230 | 2 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0552× (z -25.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0346× (z -14.6) |
| [[SNU-423 (line)]] | alt | 281 | 2 | 9 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.75× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.102× (z -30.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0827× (z -16.5) |
| [[SW1417 (line)]] | alt | 190 | 4 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.106× (z -29.0) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0744× (z -16.9) |
| [[A-172 (line)]] | wt | 169 | 1 | 9 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.37× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.110× (z -22.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.102× (z -11.5) |
| [[HS-578T (line)]] | alt | 170 | 3 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0670× (z -31.4) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0595× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 109 | 3 (1 ⚠) | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0866× (z -25.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.108× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 261 | 0 | 10 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0903× (z -27.8) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0976× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 255 | 3 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0740× (z -31.0) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.131× (z -12.2) |
| [[HT-29 (line)]] | alt | 212 | 0 | 9 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0867× (z -26.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0840× (z -13.4) |
| [[LoVo (line)]] | wt | 96.8 | 3 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.50× (z +13.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0743× (z -22.3) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.212× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 94.0 | 2 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +13.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0576× (z -24.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.210× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 122 | 0 | 8 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0845× (z -25.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.290× (z -11.9) |
| [[RKO (line)]] | wt | 107 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0709× (z -21.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.290× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 116 | 2 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.158× (z -17.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0789× (z -12.3) |
| [[HOP62 (line)]] | alt | 101 | 5 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.23× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0769× (z -20.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.120× (z -8.7) |
| [[Hs 766T (line)]] | wt | 139 | 1 | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.110× (z -20.8) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0744× (z -12.3) |
| [[SHP-77 (line)]] | alt | 176 | 0 | 7 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0777× (z -26.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0636× (z -14.4) |
| [[A549 (line)]] | wt | 76.0 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -20.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0922× (z -12.2) |
| [[LS 180 (line)]] | wt | 113 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +14.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -16.7) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 114 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.108× (z -20.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0904× (z -11.0) |
| [[A498 (line)]] | wt | 133 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0567× (z -26.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0842× (z -11.3) |
| [[H4 (line)]] | wt | 85.2 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.15× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.94× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.121× (z -13.3) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 109 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0806× (z -20.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0825× (z -10.4) |
| [[J82 (line)]] | alt | 169 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +15.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.194× (z -13.6) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 163 | 1 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.48× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.112× (z -20.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.126× (z -9.8) |
| [[SW48 (line)]] | wt | 121 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0711× (z -21.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.215× (z -11.6) |
| [[A-427 (line)]] | wt | 245 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.139× (z -20.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.160× (z -9.7) |
| [[C32 (line)]] | wt | 122 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.107× (z -22.8) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.109× (z -11.4) |
| [[CHP-212 (line)]] | wt | 214 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0931× (z -18.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0843× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 134 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0807× (z -19.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0800× (z -9.6) |
| [[C-33 A (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.106× (z -18.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0690× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 136 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0858× (z -18.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.107× (z -8.5) |
| [[HCT15 (line)]] | alt | 123 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0754× (z -21.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0681× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 59.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0876× (z -19.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 0.05 µM 0.285× (z -9.4) |
| [[AN3 CA (line)]] | alt | 281 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.166× (z -12.1) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 1 | — | [[c-Kit-IN-1 (drug)]] 5 µM 0.0356× (z -9.3) |
| [[SNU-1 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0770× (z -17.0) ⚠ unreliable plate only |
| [[SW 1088 (line)]] | alt | 72.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0531× (z -8.6) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0787× (z -15.0) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREBRF]] | +0.85 | +0.85 / +0.86 | both halves | 7e-06 | STRING 759 |
| [[TCP11L2]] | +0.80 | +0.70 / +0.84 | both halves | 7e-06 |  |
| [[RB1CC1]] | +0.80 | +0.64 / +0.86 | both halves | 7e-06 |  |
| [[HBP1]] | +0.79 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.77 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.76 | +0.62 / +0.80 | both halves | 7e-06 |  |
| [[PIK3CA]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[JMY]] | +0.76 | +0.57 / +0.83 | both halves | 1e-05 |  |
| [[ELF2]] | +0.73 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[TNRC6B]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[WDR48]] | +0.71 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGK]] | -0.67 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[PDSS1]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[NAA15]] | -0.64 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[FARSB]] | -0.64 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.64 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[NME1]] | -0.64 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NUP205]] | -0.60 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[UBE2N]] | -0.60 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[RNGTT]] | -0.60 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[NOC3L]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[MAK16]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers KLHL24's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 7.8% of all compounds | 0.015 | ⚠ off-target possible; 6 compounds |
| [[HDAC5]] | C | HDAC5's natural level strengthens KLHL24's drug response | HDAC5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.13; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.901). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, -44.5); signed map (-14.2, 9.9). **Vector** length 171, 69.4% of its response variance represented; |z| ≥ 3 in 2,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +8.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.4 | +15.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +4.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +5.5 | +4.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +5.5 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.5 | +3.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +5.4 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -25.8 | -39.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -16.4 | -18.8 |
|  | [[EX229 (drug)]] 5 µM |  | -16.3 | -16.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -15.3 | -14.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -14.0 | -15.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -12.9 | -14.0 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:183,635,610-183,684,519 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRE1, FLJ20059, KRIP6 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Hallmark sets | HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6TFL4](https://www.uniprot.org/uniprotkb/Q6TFL4) (Kelch-like protein 24):

> Necessary to maintain the balance between intermediate filament stability and degradation, a process that is essential for skin integrity. As part of the BCR(KLHL24) E3 ubiquitin ligase complex, mediates ubiquitination of KRT14 and controls its levels during keratinocytes differentiation. Specifically reduces kainate receptor-mediated currents in hippocampal neurons, most probably by modulating channel properties (By similarity). Has a crucial role in cardiac development and function.

**Summary**, from NCBI Gene [54800](https://www.ncbi.nlm.nih.gov/gene/54800):

> The protein encoded by this gene is a ubiquitin ligase substrate receptor and is regulated by autoubiquitination. Variations in the translation initiation codon of this gene have been found, which result in an N-terminally truncated but more stable protein due to loss of the autoubiquitination function. The more stable mutant protein causes an increased ubiquitin and degradation of keratin 14, which leads to skin fragility and the potentially life-threatening disease epidermolysis bullosa. The …

**Accessions** — [HGNC:25947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25947) · Entrez [54800](https://www.ncbi.nlm.nih.gov/gene/54800) · UniProt [Q6TFL4](https://www.uniprot.org/uniprotkb/Q6TFL4) · Ensembl [ENSG00000114796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114796)

## Data

Gene col 3590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3590); `tables/drug_effects.parquet` (79 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3590]; `tensor/DDL_lfc|DDL_z.npy` [3590]; `embed/gene_vectors.npy` [3590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3590 or target_col == 3590). Every well: [[KLHL24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
