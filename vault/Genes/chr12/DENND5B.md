---
symbol: "DENND5B"
type: "gene"
col: 9956
ensembl_id: "ENSG00000170456"
name: "DENN domain containing 5B"
location: "12p11.21"
module: 222
arm: "+"
pooled_cpm: 170.59
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/222"]
generated_by: "tahoemap"
---

# DENND5B

*DENN domain containing 5B* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.38× (z +7.5, q 3e-11, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.408× (z -21.0, q 0e+00, down in 40 of 45 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.546× (z -6.2, q 3e-08, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHA5]] (+0.72, fdr 7e-06), [[GKAP1]] (+0.68, fdr 7e-06), [[BEND7]] (+0.65, fdr 7e-06); moves opposite to [[AQR]] (-0.55, fdr 6e-05), [[B4GALT7]] (-0.54, fdr 3e-05), [[ZDHHC6]] (-0.52, fdr 4e-05).
> It is in [[Module 222]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MED20]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.5 | 3e-11 | 27/45 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +7.1 | 4e-10 | 27/45 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +6.3 | 4e-08 | 30/45 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +6.3 | 4e-08 | 27/45 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.7 | 3e-04 | 21/44 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.006 | 20/45 (LoVo, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.22×** | +3.6 | 0.026 | 18/47 (MIA PaCa-2, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.16× | +3.5 | 0.033 | 18/46 (HEC-1-A, A-172, …) | all doses, flat |  |
| [[Penfluridol (drug)]] 5 µM |  | 1.17× | +3.5 | 0.033 | 12/44 (HOP62, HS-578T, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.044 | 20/47 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.064 | 16/44 (SW 900, BT-474, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.2 | 0.073 | 5/45 (HOP62, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.0 | 0.10 | 16/45 (LS 180, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 17 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.408×** | -21.0 | 0e+00 | 40/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.411×** | -20.8 | 0e+00 | 39/45 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.535×** | -14.7 | 0e+00 | 37/45 (A498, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.540×** | -13.3 | 2e-38 | 35/43 (A549, HT-29, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.638×** | -10.5 | 9e-24 | 40/45 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.634×** | -10.3 | 9e-23 | 32/42 (NCI-H23, SHP-77, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.657×** | -9.4 | 3e-19 | 34/47 (SW 900, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.748×** | -9.2 | 4e-18 | 27/46 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **0.677×** | -9.1 | 4e-18 | 28/46 (RKO, A-427, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.715×** | -7.9 | 2e-13 | 37/45 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.735×** | -6.9 | 2e-10 | 30/45 (NCI-H23, SW48, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.546×** | -6.2 | 3e-08 | 32/45 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.557×** | -6.0 | 1e-07 | 26/36 (SNU-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.560×** | -5.9 | 1e-07 | 28/45 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.607×** | -5.1 | 1e-05 | 27/45 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.609×** | -5.1 | 1e-05 | 26/45 (LoVo, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.625×** | -4.8 | 6e-05 | 23/46 (A498, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.646×** | -4.4 | 3e-04 | 24/44 (HEC-1-A, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.762×** | -4.4 | 4e-04 | 26/45 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.796×** | -3.7 | 0.006 | 18/45 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.858× | -3.6 | 0.008 | 16/45 (LOX-IMVI, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.853× | -3.4 | 0.013 | 18/44 (AsPC-1, AN3 CA, …) | inconsistent across doses | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **0.728×** | -3.2 | 0.027 | 20/45 (SHP-77, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.818×** | -3.2 | 0.027 | 18/46 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.872× | -3.2 | 0.029 | 14/45 (NCI-H460, A498, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.874× | -3.0 | 0.057 | 13/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.883× | -2.9 | 0.063 | 12/45 (RPMI-7951, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 216 | 0 | 11 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -15.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 238 | 0 | 9 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -15.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 189 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -17.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.469× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 9 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -16.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 565 | 0 | 9 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -19.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 155 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -19.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.258× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 331 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -21.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 175 | 1 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.86× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.340× (z -16.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 222 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SW480 (line)]] | alt | 149 | 2 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.259× (z -20.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 241 | 1 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.9) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -17.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 223 | 0 | 7 (7 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -12.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 321 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -20.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 456 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SHP-77 (line)]] | alt | 298 | 1 | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SNU-423 (line)]] | alt | 241 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -13.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 206 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -21.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 228 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -14.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 206 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HT-29 (line)]] | alt | 210 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[PANC-1 (line)]] | alt | 214 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.531× (z -10.9) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 0.318× (z -8.6) |
| [[LoVo (line)]] | wt | 110 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -13.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 116 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 117 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 198 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -9.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.392× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 99.9 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.15× (z +10.9) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HEC-1-A (line)]] | alt | 72.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.5) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.526× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[KATO III (line)]] | alt | 129 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.1) ⚠ cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.469× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H661 (line)]] | alt | 322 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 110 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.07× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 48.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.14× (z +8.6) | — |
| [[RKO (line)]] | wt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[A-172 (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 162 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 262 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHA5]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[GKAP1]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[BEND7]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CABLES1]] | +0.57 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[SPECC1]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[RUFY3]] | +0.54 | +0.58 / +0.37 | both halves | 8e-05 | same gene group |
| [[LITAF]] | +0.54 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[ABRACL]] | +0.53 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[FAM171A1]] | +0.53 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[PHIP]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PARD3]] | +0.53 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[SIK3]] | +0.51 | +0.52 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AQR]] | -0.55 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[B4GALT7]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZDHHC6]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[TBCCD1]] | -0.52 | -0.59 / -0.29 | both halves | 3e-04 |  |
| [[PIGG]] | -0.52 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[C11orf24]] | -0.51 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[UTP6]] | -0.50 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[WDR37]] | -0.49 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[TMEM214]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ARHGAP1]] | -0.49 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[PDCD6]] | -0.48 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SZT2]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MED20]] | C | DENND5B activity lowers MED20's level | lines that do not express DENND5B (3) vs lines expressing it (47) | 2.07× higher at baseline in the lines without DENND5B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC26A11, SLC4A7, USP31; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 222]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.847). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.6, 12.8); signed map (8.2, -6.5). **Vector** length 119, 36.5% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.1 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.3 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.0 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -10.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.6 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.2 | -9.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -6.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.6 | -21.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -5.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.1 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:31,382,226-31,591,136 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC24039 |
| Gene groups (HGNC) | DENN domain containing; RUN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZUT9](https://www.uniprot.org/uniprotkb/Q6ZUT9) (DENN domain-containing protein 5B):

> Guanine nucleotide exchange factor (GEF) which may activate RAB39A and/or RAB39B. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form.

**Summary**, from NCBI Gene [160518](https://www.ncbi.nlm.nih.gov/gene/160518):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in positive regulation of triglyceride transport. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28338) · Entrez [160518](https://www.ncbi.nlm.nih.gov/gene/160518) · UniProt [Q6ZUT9](https://www.uniprot.org/uniprotkb/Q6ZUT9) · Ensembl [ENSG00000170456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170456)

## Data

Gene col 9956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9956); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9956]; `tensor/DDL_lfc|DDL_z.npy` [9956]; `embed/gene_vectors.npy` [9956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9956 or target_col == 9956). Every well: [[DENND5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
