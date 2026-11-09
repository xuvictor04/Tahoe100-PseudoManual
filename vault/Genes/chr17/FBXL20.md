---
symbol: "FBXL20"
type: "gene"
col: 2931
ensembl_id: "ENSG00000108306"
name: "F-box and leucine rich repeat protein 20"
location: "17q12"
module: 145
arm: "+"
pooled_cpm: 193.07
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# FBXL20

*F-box and leucine rich repeat protein 20* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.78× (z +13.3, q 2e-37, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.178× (z -39.9, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.198× (z -16.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.77, fdr 7e-06), [[ATXN3]] (+0.76, fdr 7e-06), [[WIPI2]] (+0.74, fdr 1e-05); moves opposite to [[TMEM185B]] (-0.64, fdr 7e-06), [[GTF2H3]] (-0.63, fdr 7e-06), [[ZNF121]] (-0.63, fdr 1e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FBXO33]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +13.3 | 2e-37 | 48/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +13.0 | 4e-36 | 36/49 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +11.4 | 9e-28 | 41/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +11.2 | 8e-27 | 44/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +10.4 | 4e-23 | 39/48 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +8.5 | 2e-15 | 33/50 (NCI-H23, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +5.9 | 2e-07 | 26/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.9 | 6e-05 | 26/48 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.23×** | +3.9 | 0.006 | 24/50 (SW480, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.012 | 25/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.015 | 20/48 (H4, COLO 205, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.015 | 20/50 (BT-474, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.11× | +3.4 | 0.027 | 6/49 (PANC-1, A-427, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.4 | 0.027 | 5/48 (A-427, NCI-H1573, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.11× | +3.4 | 0.029 | 2/48 (HCT15, NCI-H661) | rises with dose | position effect removed |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.029 | 14/49 (SHP-77, A-427, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.031 | 15/49 (SW480, A-427, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.081 | 9/48 (PANC-1, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.178×** | -39.9 | 0e+00 | 48/48 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -19.6 | 0e+00 | 42/44 (A549, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.418×** | -18.6 | 0e+00 | 42/45 (CFPAC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.450×** | -18.4 | 0e+00 | 43/49 (NCI-H23, Panc 03.27, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.198×** | -16.4 | 0e+00 | 48/48 (A549, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.210×** | -15.8 | 0e+00 | 48/48 (A549, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.224×** | -15.1 | 0e+00 | 47/48 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.253×** | -13.9 | 5e-42 | 48/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.255×** | -13.8 | 1e-41 | 46/48 (NCI-H2347, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.590×** | -12.1 | 3e-32 | 38/48 (NCI-H23, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -10.9 | 1e-25 | 42/48 (NCI-H460, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.637×** | -9.8 | 4e-21 | 41/48 (LoVo, SW48, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.647×** | -9.6 | 2e-20 | 33/48 (PANC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.451×** | -8.4 | 2e-15 | 46/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.698×** | -8.3 | 5e-15 | 35/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.519×** | -6.6 | 1e-09 | 44/47 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -6.2 | 2e-08 | 28/48 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.592×** | -5.5 | 8e-07 | 41/49 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.596×** | -5.2 | 4e-06 | 30/49 (NCI-H2347, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.802×** | -5.1 | 9e-06 | 30/49 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 177 | 1 | 15 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 1.83× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.140× (z -31.3) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.353× (z -16.6) |
| [[A498 (line)]] | wt | 147 | 7 (2 ⚠) | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.172× (z -24.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.159× (z -11.0) |
| [[A549 (line)]] | wt | 217 | 1 | 13 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 1.80× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.151× (z -29.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0919× (z -16.1) |
| [[SW1417 (line)]] | alt | 192 | 5 (1 ⚠) | 9 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.162× (z -25.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.141× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 222 | 0 | 13 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.134× (z -28.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.125× (z -12.8) |
| [[SW480 (line)]] | alt | 121 | 3 | 10 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -28.2) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.340× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 305 | 0 | 12 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -27.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.151× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 212 | 1 | 11 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.74× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.117× (z -33.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.419× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 250 | 0 | 12 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -27.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.176× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 189 | 2 | 10 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -28.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -13.1) |
| [[SNU-423 (line)]] | alt | 234 | 0 | 12 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -23.0) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.189× (z -11.0) |
| [[HT-29 (line)]] | alt | 160 | 2 | 9 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -25.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.127× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 193 | 0 | 11 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.120× (z -31.4) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.122× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 270 | 0 | 11 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.164× (z -26.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.165× (z -11.4) |
| [[SW 900 (line)]] | alt | 186 | 0 | 11 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -22.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -11.7) |
| [[BT-474 (line)]] | alt | 1,505 | 1 (1 ⚠) | 9 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.87× (z +8.9) ⚠ cell-cycle shift, explains ~42% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -19.6) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.137× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 206 | 4 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.247× (z -19.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.190× (z -10.4) |
| [[KATO III (line)]] | alt | 155 | 5 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.135× (z -21.9) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.129× (z -9.8) |
| [[LoVo (line)]] | wt | 116 | 5 (1 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.161× (z -24.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.323× (z -14.0) |
| [[PANC-1 (line)]] | alt | 83.4 | 0 | 10 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.148× (z -27.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.405× (z -12.9) |
| [[A-172 (line)]] | wt | 184 | 0 | 9 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -20.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.403× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 131 | 1 | 7 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.105× (z -26.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0907× (z -12.5) |
| [[HOP62 (line)]] | alt | 178 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -23.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.188× (z -9.8) |
| [[LS 180 (line)]] | wt | 134 | 4 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 297 | 0 | 8 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.151× (z -23.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.146× (z -10.5) |
| [[HS-578T (line)]] | alt | 149 | 0 | 7 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.245× (z -19.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.187× (z -9.9) |
| [[C32 (line)]] | wt | 192 | 0 | 6 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.239× (z -18.6) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.467× (z -9.9) |
| [[COLO 205 (line)]] | alt | 147 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.185× (z -18.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.109× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 183 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.221× (z -19.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.361× (z -13.3) |
| [[A-427 (line)]] | wt | 249 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.243× (z -17.9) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.395× (z -11.8) |
| [[CHP-212 (line)]] | wt | 406 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -18.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.128× (z -9.6) |
| [[J82 (line)]] | alt | 126 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -13.8) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 127 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.252× (z -16.4) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.359× (z -12.2) |
| [[SNU-1 (line)]] | wt | 162 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0868× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[EX229 (drug)]] 0.05 µM 0.374× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 122 | 1 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.434× (z -8.6) |
| [[SW48 (line)]] | wt | 145 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -17.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.297× (z -10.3) |
| [[AN3 CA (line)]] | alt | 179 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -8.6) |
| [[H4 (line)]] | wt | 95.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.141× (z -15.3) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -13.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.383× (z -9.5) |
| [[Hs 766T (line)]] | wt | 91.3 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -16.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.141× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.181× (z -18.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.132× (z -9.7) |
| [[RKO (line)]] | wt | 141 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -16.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.412× (z -8.8) |
| [[SHP-77 (line)]] | alt | 148 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -16.3) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.465× (z -8.7) |
| [[C-33 A (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -15.5) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -15.3) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 219 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0637× (z -16.5) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 111 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.77 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[ATXN3]] | +0.76 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[WIPI2]] | +0.74 | +0.53 / +0.81 | both halves | 1e-05 |  |
| [[ELF2]] | +0.74 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[ZER1]] | +0.73 | +0.51 / +0.79 | both halves | 1e-05 |  |
| [[ULK1]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NARF]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.73 | +0.59 / +0.74 | both halves | 7e-06 | pathway: Neddylation |
| [[CNNM2]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.72 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[HINFP]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.71 | +0.66 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.64 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[GTF2H3]] | -0.63 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[ZNF121]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[MAK16]] | -0.62 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.62 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.62 | -0.70 / -0.55 | both halves | 1e-05 |  |
| [[VARS1]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[NAA15]] | -0.61 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.60 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[MGA]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.60 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[COA7]] | -0.60 | -0.60 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FBXL20's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO33]] | C | FBXL20's natural level strengthens FBXO33's drug response | FBXL20's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.11; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.8, -42.9); signed map (-16.6, 11.7). **Vector** length 153, 60.5% of its response variance represented; |z| ≥ 3 in 1,675 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +13.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +8.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.9 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +11.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[MK-3903 (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -21.5 | -39.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -13.8 | -16.4 |
|  | [[EX229 (drug)]] 5 µM |  | -12.8 | -15.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -12.6 | -13.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -12.5 | -15.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -10.2 | -13.9 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,252,663-39,402,523 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15482, Fbl2, Fbl20 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IG2](https://www.uniprot.org/uniprotkb/Q96IG2) (F-box/LRR-repeat protein 20):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Role in neural transmission (By similarity).

**Summary**, from NCBI Gene [84961](https://www.ncbi.nlm.nih.gov/gene/84961):

> Members of the F-box protein family, such as FBXL20, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24679) · Entrez [84961](https://www.ncbi.nlm.nih.gov/gene/84961) · UniProt [Q96IG2](https://www.uniprot.org/uniprotkb/Q96IG2) · Ensembl [ENSG00000108306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108306)

## Data

Gene col 2931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2931); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2931]; `tensor/DDL_lfc|DDL_z.npy` [2931]; `embed/gene_vectors.npy` [2931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2931 or target_col == 2931). Every well: [[FBXL20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
