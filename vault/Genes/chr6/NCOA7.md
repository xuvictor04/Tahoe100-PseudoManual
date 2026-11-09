---
symbol: "NCOA7"
type: "gene"
col: 3307
ensembl_id: "ENSG00000111912"
name: "nuclear receptor coactivator 7"
location: "6q22.31-q22.32"
module: 70
arm: "+"
pooled_cpm: 173.32
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 35
n_dd_up_clean: 13
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# NCOA7

*nuclear receptor coactivator 7* — 6q22.31-q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.25× (z +7.7, q 8e-12, up in 27 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.503× (z -12.4, q 1e-32, down in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.541× (z -11.1, q 4e-26, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFH]] (+0.65, fdr 7e-06), [[CFB]] (+0.61, fdr 1e-05), [[GBP2]] (+0.61, fdr 1e-05); moves opposite to [[DIP2A]] (-0.57, fdr 1e-05), [[ITGB1BP1]] (-0.53, fdr 2e-05), [[KLC1]] (-0.53, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[OAS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +7.7 | 8e-12 | 27/49 (LoVo, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 4e-07 | 32/49 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +5.2 | 5e-05 | 25/50 (AsPC-1, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +5.0 | 7e-05 | 22/49 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +5.0 | 7e-05 | 24/48 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 4e-04 | 23/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | **1.61×** | +4.5 | 5e-04 | 29/48 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +4.5 | 5e-04 | 24/49 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +4.4 | 8e-04 | 23/47 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.003 | 20/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.16× | +3.8 | 0.007 | 16/49 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.008 | 14/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.008 | 23/48 (RKO, SNU-1, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.010 | 18/48 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.013 | 18/48 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.038 | 15/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3307.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -12.4 | 1e-32 | 40/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.541×** | -11.1 | 4e-26 | 34/48 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.663×** | -10.5 | 2e-23 | 29/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.611×** | -8.9 | 9e-17 | 36/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -8.5 | 3e-15 | 34/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.633×** | -8.2 | 2e-14 | 34/48 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -7.1 | 1e-10 | 31/48 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.669×** | -7.0 | 2e-10 | 30/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -6.8 | 6e-10 | 27/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.691×** | -6.7 | 2e-09 | 31/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.694×** | -6.6 | 2e-09 | 31/48 (KATO III, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -6.2 | 3e-08 | 27/49 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.525×** | -6.1 | 5e-08 | 28/45 (SW48, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.716×** | -6.0 | 7e-08 | 27/48 (HepG2/C3A, KATO III, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.723×** | -5.9 | 2e-07 | 30/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.735×** | -5.3 | 5e-06 | 28/48 (SW 900, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.748×** | -5.2 | 5e-06 | 32/48 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.743×** | -5.2 | 8e-06 | 29/47 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.820×** | -5.0 | 1e-05 | 26/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.619×** | -4.5 | 2e-04 | 28/46 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.805×** | -3.9 | 0.002 | 24/48 (BT-474, COLO 205, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 248 | 1 | 18 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 7.85× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0650× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 214 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -17.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -16.7) |
| [[KATO III (line)]] | alt | 241 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -19.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 398 | 1 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 8.16× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 83.3 | 9 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.99× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 268 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -20.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -11.9) |
| [[PANC-1 (line)]] | alt | 191 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -32.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -16.7) |
| [[SW 900 (line)]] | alt | 339 | 1 | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.38× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -12.4) |
| [[CHP-212 (line)]] | wt | 240 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -11.9) |
| [[HT-29 (line)]] | alt | 163 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -15.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -10.9) |
| [[SNU-423 (line)]] | alt | 251 | 0 | 7 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -12.9) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.9) |
| [[SW480 (line)]] | alt | 76.8 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 170 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -27.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.377× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 462 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 326 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -19.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -12.2) |
| [[RKO (line)]] | wt | 117 | 1 (1 ⚠) | 5 (3 ⚠) | [[Artesunate (drug)]] 5 µM 2.08× (z +11.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -26.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -9.9) |
| [[LoVo (line)]] | wt | 209 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.23× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.247× (z -15.3) |
| [[NCI-H2347 (line)]] | alt | 182 | 4 (4 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.95× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.299× (z -11.6) |
| [[SHP-77 (line)]] | alt | 146 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -10.3) |
| [[SW1417 (line)]] | alt | 126 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -12.4) |
| [[A549 (line)]] | wt | 358 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -16.9) |
| [[HS-578T (line)]] | alt | 114 | 4 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.94× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.08× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 1 | 3 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.01× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -15.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 80.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -9.9) |
| [[A498 (line)]] | wt | 112 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.5) |
| [[C32 (line)]] | wt | 293 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.7) |
| [[J82 (line)]] | alt | 112 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.90× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 267 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -16.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 67.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.75× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 51.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +12.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 176 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.09× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.277× (z -10.4) |
| [[SNU-1 (line)]] | wt | 93.0 | 2 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.34× (z +9.6) | — |
| [[SW 1271 (line)]] | alt | 97.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0891× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.133× (z -8.8) |
| [[A-172 (line)]] | wt | 84.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.90× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 84.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -12.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.402× (z -9.2) |
| [[HCT15 (line)]] | alt | 132 | 1 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 1.94× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.339× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 79.2 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.153× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 184 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.2× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 79.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[AN3 CA (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFH]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CFB]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GBP2]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[GBP1]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[AHR]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TNFAIP6]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ALPK1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NFKBIZ]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[IFIT2]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[LAMP3]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TRANK1]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[APOL6]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ITGB1BP1]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[KLC1]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CERS5]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[BCL7C]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[CROCCP3]] | -0.50 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[CCM2]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[DPP9]] | -0.48 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ARHGEF1]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RGS12]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZFYVE21]] | -0.47 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS1]] | B | OAS1 activity raises NCOA7's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.91× lower at baseline in the lines without OAS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises NCOA7's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without GBP4 | 0.015 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[CASP10]] | B | CASP10 activity raises NCOA7's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.54× lower at baseline in the lines without CASP10 | 0.023 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[TRANK1]] | B | TRANK1 activity raises NCOA7's level | lines that do not express TRANK1 (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without TRANK1 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM140]] | B | TMEM140 activity raises NCOA7's level | lines that do not express TMEM140 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without TMEM140 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises NCOA7's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.41× lower at baseline in the lines without SAMD9L | 0.038 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[CYP1B1]] | B | CYP1B1 activity raises NCOA7's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 1.56× lower at baseline in the lines without CYP1B1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[MAP2K1]] | B | MAP2K1 activity lowers NCOA7's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PLPP3]] | B | PLPP3 activity raises NCOA7's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without PLPP3 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity strengthens NCOA7's drug response | lines that do not express OAS1 (13) vs lines expressing it (36) | the lines without OAS1 respond 0.49× as strongly (z diff +2.30); strongest at Auranofin 5 µM: 0.98x vs 0.59x (z diff +4.2) | 0.070 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[APOL6]] | B | APOL6 activity raises NCOA7's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without APOL6 | 0.072 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises NCOA7's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without GBP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.3, 49.2); signed map (60.0, 27.7). **Vector** length 135, 46.1% of its response variance represented; |z| ≥ 3 in 1,902 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Non-canonical inflammasome activation* (reactome, mean cos +0.53 to 4); *CASP4 inflammasome assembly* (reactome, mean cos +0.57 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.5 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +6.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.8 | +3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +4.7 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.9 | +4.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.9 | +5.0 |
| fall | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.7 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.4 | -5.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.6 | -3.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor coactivator 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31-q22.32 — chr6:125,781,161-125,932,034 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERAP140, dJ187J11.3, TLDC4 |
| Gene groups (HGNC) | TLDc domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI08](https://www.uniprot.org/uniprotkb/Q8NI08) (Nuclear receptor coactivator 7):

> Transcriptional coactivator which enhances the transcriptional activities of several nuclear receptors including ESR1, THRB, PPARG and RARA. Inhibits the activity of the vacuolar-type ATPase (V-ATPase) by inducing disassembly of the V-ATPase complex. Protects the Golgi apparatus lumen from excess acidification by inhibiting V-ATPase ATP hydrolytic activity through interaction with V-ATPase catalytic subunit ATP6V1A, maintaining optimal conditions for glycosylation enzymes (By similarity). …

**Summary**, from NCBI Gene [135112](https://www.ncbi.nlm.nih.gov/gene/135112):

> Enables nuclear receptor binding activity and transcription coactivator activity. Involved in positive regulation of transcription by RNA polymerase II. Predicted to be located in mitochondrion. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21081) · Entrez [135112](https://www.ncbi.nlm.nih.gov/gene/135112) · UniProt [Q8NI08](https://www.uniprot.org/uniprotkb/Q8NI08) · Ensembl [ENSG00000111912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111912)

## Data

Gene col 3307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3307); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3307]; `tensor/DDL_lfc|DDL_z.npy` [3307]; `embed/gene_vectors.npy` [3307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3307 or target_col == 3307). Every well: [[NCOA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCOA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
