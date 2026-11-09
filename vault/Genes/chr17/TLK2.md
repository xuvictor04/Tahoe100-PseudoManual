---
symbol: "TLK2"
type: "gene"
col: 7130
ensembl_id: "ENSG00000146872"
name: "tousled like kinase 2"
location: "17q23.2"
module: 46
arm: "+"
pooled_cpm: 146.96
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# TLK2

*tousled like kinase 2* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +11.7, q 9e-29, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.276× (z -28.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDNK]] (+0.71, fdr 1e-05), [[WDFY3]] (+0.71, fdr 3e-05), [[RAF1]] (+0.69, fdr 7e-06); moves opposite to [[TXNL4A]] (-0.63, fdr 2e-05), [[CALU]] (-0.61, fdr 3e-05), [[DAP]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[COTL1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RBM33]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +11.7 | 9e-29 | 42/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.23×** | +10.6 | 1e-23 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +9.7 | 4e-20 | 43/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.79×** | +9.3 | 3e-18 | 48/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +7.3 | 4e-11 | 35/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +6.9 | 4e-10 | 39/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +6.1 | 6e-08 | 31/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 1e-06 | 29/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +5.6 | 1e-06 | 27/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.5 | 2e-06 | 26/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +5.3 | 5e-06 | 28/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.8 | 8e-05 | 28/47 (LoVo, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.22×** | +4.4 | 4e-04 | 27/49 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +4.0 | 0.002 | 25/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.0 | 0.002 | 16/49 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.039 | 20/49 (SW480, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.051 | 12/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.1 | 0.052 | 13/48 (KATO III, SW480, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.052 | 17/48 (HT-29, SNU-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.276×** | -28.2 | 0e+00 | 48/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.299×** | -26.4 | 0e+00 | 47/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.375×** | -21.5 | 0e+00 | 48/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.393×** | -20.5 | 0e+00 | 49/49 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.396×** | -19.5 | 0e+00 | 43/44 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.439×** | -16.1 | 0e+00 | 40/45 (CFPAC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.554×** | -12.9 | 3e-36 | 46/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -9.7 | 2e-20 | 41/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.685×** | -8.0 | 1e-13 | 39/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.729×** | -6.9 | 2e-10 | 36/48 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.763×** | -5.9 | 2e-07 | 34/49 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -5.0 | 2e-05 | 27/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.816×** | -4.5 | 4e-04 | 26/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~18% of this change | **0.832×** | -4.0 | 0.002 | 23/48 (KATO III, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.842× | -3.8 | 0.006 | 18/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.666×** | -3.7 | 0.009 | 27/49 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.714×** | -3.0 | 0.079 | 17/48 (MIA PaCa-2, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.874× | -3.0 | 0.099 | 11/49 (NCI-H2347, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 157 | 8 (1 ⚠) | 10 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.38× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -29.8) |
| [[KATO III (line)]] | alt | 149 | 5 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -20.7) |
| [[LoVo (line)]] | wt | 128 | 4 (2 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.272× (z -20.2) |
| [[NCI-H2347 (line)]] | alt | 195 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -24.6) |
| [[A-427 (line)]] | wt | 144 | 3 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.339× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 175 | 1 (1 ⚠) | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.205× (z -22.7) |
| [[SW1417 (line)]] | alt | 163 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -18.8) |
| [[NCI-H460 (line)]] | wt | 136 | 2 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 189 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -19.9) |
| [[PANC-1 (line)]] | alt | 119 | 3 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -20.0) |
| [[SK-MEL-2 (line)]] | alt | 179 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -15.9) |
| [[SNU-423 (line)]] | alt | 174 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -20.0) |
| [[A-172 (line)]] | wt | 149 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -18.3) |
| [[A498 (line)]] | wt | 147 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.369× (z -12.1) |
| [[A549 (line)]] | wt | 180 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -19.7) |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.282× (z -17.2) |
| [[HOP62 (line)]] | alt | 137 | 1 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -20.4) |
| [[LOX-IMVI (line)]] | wt | 164 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.12× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.249× (z -18.3) |
| [[NCI-H1792 (line)]] | alt | 226 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -23.1) |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 155 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0573× (z -41.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.246× (z -20.3) |
| [[SW 900 (line)]] | alt | 143 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.184× (z -21.9) |
| [[AsPC-1 (line)]] | alt | 105 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -18.7) |
| [[C-33 A (line)]] | alt | 194 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.339× (z -14.2) |
| [[C32 (line)]] | wt | 129 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -15.8) |
| [[H4 (line)]] | wt | 127 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.351× (z -10.3) |
| [[HT-29 (line)]] | alt | 98.8 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.257× (z -18.2) |
| [[SW48 (line)]] | wt | 160 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.26× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.220× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 178 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.440× (z -9.6) |
| [[Hs 766T (line)]] | wt | 85.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -16.8) |
| [[HS-578T (line)]] | alt | 119 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -15.5) |
| [[J82 (line)]] | alt | 137 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -18.4) |
| [[LS 180 (line)]] | wt | 118 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -17.6) |
| [[CHP-212 (line)]] | wt | 348 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -13.6) |
| [[COLO 205 (line)]] | alt | 132 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 7.88× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.278× (z -13.8) |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -13.5) |
| [[RKO (line)]] | wt | 137 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 2.18× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -12.8) |
| [[SHP-77 (line)]] | alt | 94.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.383× (z -11.2) |
| [[BT-474 (line)]] | alt | 100 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -18.1) |
| [[HCT15 (line)]] | alt | 148 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.423× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -13.8) |
| [[NCI-H661 (line)]] | alt | 239 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.228× (z -8.8) |
| [[AN3 CA (line)]] | alt | 183 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -8.8) |
| [[SNU-1 (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDNK]] | +0.71 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[WDFY3]] | +0.71 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[RAF1]] | +0.69 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NCOA2]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.67 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[CHD6]] | +0.67 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TLK1]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 | STRING 995 |
| [[ARID1B]] | +0.66 | +0.31 / +0.69 | both halves | 2e-04 |  |
| [[DYRK1A]] | +0.65 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[APPBP2-DT]] | +0.64 | +0.45 / +0.38 | both halves | 6e-05 |  |
| [[WAC-AS1]] | +0.64 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[ARID4B]] | +0.64 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL4A]] | -0.63 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[CALU]] | -0.61 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[DAP]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SLC25A32]] | -0.59 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[P4HB]] | -0.58 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[DGKD]] | -0.57 | -0.39 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COTL1]] | B | COTL1 activity raises TLK2's level | lines that do not express COTL1 (5) vs lines expressing it (45) | 1.09× lower at baseline in the lines without COTL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TIMP1, HOXA-AS2, ELK3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM33]] | C | TLK2's natural level strengthens RBM33's drug response | TLK2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.23; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.5, 14.5); signed map (28.0, -23.4). **Vector** length 111, 42.4% of its response variance represented; |z| ≥ 3 in 1,377 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.9 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.6 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +8.4 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +0.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.9 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.3 | -12.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -21.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -28.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.9 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | tousled like kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.2 — chr17:62,458,658-62,615,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKU-ALPHA, MGC44450 |
| Gene groups (HGNC) | Tousled like kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UE8](https://www.uniprot.org/uniprotkb/Q86UE8) (Serine/threonine-protein kinase tousled-like 2):

> Serine/threonine-protein kinase involved in the process of chromatin assembly and probably also DNA replication, transcription, repair, and chromosome segregation. Phosphorylates the chromatin assembly factors ASF1A and ASF1B. Phosphorylation of ASF1A prevents its proteasome-mediated degradation, thereby enhancing chromatin assembly. Negative regulator of amino acid starvation-induced autophagy.

**Summary**, from NCBI Gene [11011](https://www.ncbi.nlm.nih.gov/gene/11011):

> This gene encodes a nuclear serine/threonine kinase that was first identified in Arabidopsis. The encoded protein is thought to function in the regulation of chromatin assembly in the S phase of the cell cycle by regulating the levels of a histone H3/H4 chaperone. This protein is associated with double-strand break repair of DNA damage caused by radiation. Pseudogenes of this gene are present on chromosomes 10 and 17. Alternate splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:11842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11842) · Entrez [11011](https://www.ncbi.nlm.nih.gov/gene/11011) · UniProt [Q86UE8](https://www.uniprot.org/uniprotkb/Q86UE8) · Ensembl [ENSG00000146872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146872)

## Data

Gene col 7130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7130); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7130]; `tensor/DDL_lfc|DDL_z.npy` [7130]; `embed/gene_vectors.npy` [7130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7130 or target_col == 7130). Every well: [[TLK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
