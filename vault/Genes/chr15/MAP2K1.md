---
symbol: "MAP2K1"
type: "gene"
col: 9741
ensembl_id: "ENSG00000169032"
name: "mitogen-activated protein kinase kinase 1"
location: "15q22.31"
module: 105
arm: "+"
pooled_cpm: 207.32
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 26
n_dd_up_clean: 17
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 5
direction_downstream: 963
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# MAP2K1

*mitogen-activated protein kinase kinase 1* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.09× (z +13.4, q 3e-38, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.486× (z -13.8, q 8e-41, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.650× (z -11.7, q 3e-29, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO9B]] (+0.75, fdr 7e-06), [[HK1]] (+0.74, fdr 7e-06), [[UBE2O]] (+0.74, fdr 1e-05); moves opposite to [[TIA1]] (-0.69, fdr 2e-05), [[MED12]] (-0.65, fdr 1e-05), [[CASC9]] (-0.63, fdr 2e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TM4SF19]], [[TM4SF19-DYNLT2B]] → it (grade B ⚠); 963 go from it, the strongest it → [[ST3GAL6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.09×** | +13.4 | 3e-38 | 47/49 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.4 | 1e-14 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +8.3 | 2e-14 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.69×** | +8.1 | 6e-14 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +8.0 | 1e-13 | 39/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +7.1 | 2e-10 | 34/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.25×** | +6.7 | 2e-09 | 42/48 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.6 | 4e-09 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +6.1 | 5e-08 | 32/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.9 | 2e-07 | 37/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +5.4 | 4e-06 | 26/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 1e-04 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 5e-04 | 27/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.001 | 26/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +4.2 | 0.001 | 29/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.001 | 28/49 (SW480, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.017 | 24/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.019 | 24/48 (LoVo, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9741.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.486×** | -13.8 | 8e-41 | 46/49 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -13.2 | 2e-37 | 41/44 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -11.7 | 3e-29 | 35/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -7.6 | 4e-12 | 37/48 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.718×** | -6.1 | 1e-07 | 34/48 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.747×** | -5.4 | 7e-06 | 32/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -5.4 | 7e-06 | 30/45 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.754×** | -5.2 | 2e-05 | 31/47 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.773×** | -4.9 | 5e-05 | 30/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.832×** | -4.9 | 6e-05 | 23/48 (NCI-H2347, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.814×** | -4.8 | 6e-05 | 24/48 (SK-MEL-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.769×** | -4.8 | 6e-05 | 26/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.836× | -4.7 | 1e-04 | 24/49 (NCI-H2347, SK-MEL-2, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.6 | 2e-04 | 22/49 (HEC-1-A, J82, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.783×** | -4.4 | 4e-04 | 25/48 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.789×** | -4.4 | 5e-04 | 31/48 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.797×** | -4.3 | 5e-04 | 27/48 (PANC-1, J82, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.802×** | -4.2 | 8e-04 | 27/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.826×** | -4.1 | 9e-04 | 24/48 (PANC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -4.1 | 0.001 | 18/48 (NCI-H2347, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 204 | 23 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 3.04× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 217 | 12 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -15.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 172 | 11 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.79× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.512× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 306 | 2 | 8 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.81× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -23.4) |
| [[HEC-1-A (line)]] | alt | 247 | 2 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.92× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.505× (z -9.9) |
| [[C32 (line)]] | wt | 275 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.49× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -19.1) |
| [[NCI-H2347 (line)]] | alt | 300 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.40× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.576× (z -11.5) |
| [[HT-29 (line)]] | alt | 188 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +13.7) | — |
| [[NCI-H460 (line)]] | wt | 175 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.02× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.67× (z +14.3) | — |
| [[SNU-1 (line)]] | wt | 210 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.5× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 251 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.614× (z -11.1) |
| [[KATO III (line)]] | alt | 136 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 215 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.42× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -12.4) |
| [[A-172 (line)]] | wt | 196 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 314 | 2 | 3 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.76× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -13.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 137 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.63× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 192 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.69× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -12.1) |
| [[LS 180 (line)]] | wt | 140 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.93× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 217 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.534× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 284 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 360 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -13.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 312 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 258 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -17.1) |
| [[A-427 (line)]] | wt | 66.8 | 1 (1 ⚠) | 2 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.7) |
| [[A549 (line)]] | wt | 286 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.39× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -11.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 164 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 275 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 191 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.01× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.558× (z -9.0) |
| [[RKO (line)]] | wt | 265 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.39× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -15.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 155 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.91× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.92× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -12.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 152 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 259 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 279 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.63× (z +10.1) | — |
| [[hTERT-HPNE (line)]] | wt | 241 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 159 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.59× (z +12.4) | — |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.2) |
| [[SNU-423 (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -9.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 180 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +10.1) | — |
| [[A498 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 172 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 125 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 257 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | +0.75 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[HK1]] | +0.74 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.74 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[PRKRIP1]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[DNAJC5]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[POM121]] | +0.69 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[ZFYVE28]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.68 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | +0.67 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[LINC03009-1]] | +0.67 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | +0.67 | +0.69 / +0.54 | both halves | 1e-05 | STRING 418 |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.69 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[MED12]] | -0.65 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[CASC9]] | -0.63 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ZNF280D]] | -0.63 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.62 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[PMF1]] | -0.61 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[REPIN1]] | -0.60 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.59 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[BMI1]] | -0.59 | -0.55 / -0.47 | both halves | 2e-05 | STRING 433 |
| [[PTPRK]] | -0.59 | -0.66 / -0.38 | both halves | 7e-05 |  |
| [[ZNF260]] | -0.59 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.59 | -0.53 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF19]], [[TM4SF19-DYNLT2B]] | B | TM4SF19, TM4SF19-DYNLT2B activity raises MAP2K1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.52× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[ELL2]] | B | ELL2 activity raises MAP2K1's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without ELL2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[GLRX]] | B | GLRX activity raises MAP2K1's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.46× lower at baseline in the lines without GLRX | 0.069 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity raises MAP2K1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without NDRG1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[TCAF2]] | C | TCAF2 activity raises MAP2K1's level | lines that do not express TCAF2 (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without TCAF2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*963 arrows, 963 of them with an alert ⚠; grade A 0, B 963, C 0. Shown: the 12 strongest; 951 more arrows (951 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL6]] | B | MAP2K1 activity raises ST3GAL6's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIH1D1]] | B | MAP2K1 activity raises PIH1D1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds |
| [[CCT2]] | B | MAP2K1 activity raises CCT2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[EPHA2-AS1]] | B | MAP2K1 activity raises EPHA2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00963]] | B | MAP2K1 activity lowers LINC00963's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[LRFN5]] | B | MAP2K1 activity raises LRFN5's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PFDN2]] | B | MAP2K1 activity raises PFDN2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds |
| [[PRKG2-AS1]] | B | MAP2K1 activity raises PRKG2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RRP9]] | B | MAP2K1 activity raises RRP9's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TBC1D32]] | B | MAP2K1 activity lowers TBC1D32's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF630]] | B | MAP2K1 activity lowers ZNF630's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 0.8% of all compounds | 0.007 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FOXL1]] | B | MAP2K1 activity raises FOXL1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.1, -15.1); signed map (-42.0, 23.0). **Vector** length 131, 50.2% of its response variance represented; |z| ≥ 3 in 1,651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +8.4 | +3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +8.2 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.7 | +0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.7 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -11.0 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.4 | -7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.7 | -4.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.6 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:66,386,837-66,491,656 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MEK1, MAPKK1, MKK1; previously PRKMK1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinases |
| Reactome | 56 pathways, smallest: Signaling by MAP2K mutants; Negative feedback regulation of MAPK pathway; MAPK3 (ERK1) activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02750](https://www.uniprot.org/uniprotkb/Q02750) (Dual specificity mitogen-activated protein kinase kinase 1):

> Dual specificity protein kinase which acts as an essential component of the MAP kinase signal transduction pathway. Binding of extracellular ligands such as growth factors, cytokines and hormones to their cell-surface receptors activates RAS and this initiates RAF1 activation. RAF1 then further activates the dual-specificity protein kinases MAP2K1/MEK1 and MAP2K2/MEK2. Both MAP2K1/MEK1 and MAP2K2/MEK2 function specifically in the MAPK/ERK cascade, and catalyze the concomitant phosphorylation of …

**Summary**, from NCBI Gene [5604](https://www.ncbi.nlm.nih.gov/gene/5604):

> The protein encoded by this gene is a member of the dual specificity protein kinase family, which acts as a mitogen-activated protein (MAP) kinase kinase. MAP kinases, also known as extracellular signal-regulated kinases (ERKs), act as an integration point for multiple biochemical signals. This protein kinase lies upstream of MAP kinases and stimulates the enzymatic activity of MAP kinases upon wide variety of extra- and intracellular signals. As an essential component of MAP kinase signal …

**Accessions** — [HGNC:6840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6840) · Entrez [5604](https://www.ncbi.nlm.nih.gov/gene/5604) · UniProt [Q02750](https://www.uniprot.org/uniprotkb/Q02750) · Ensembl [ENSG00000169032](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169032)

## Data

Gene col 9741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9741); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9741]; `tensor/DDL_lfc|DDL_z.npy` [9741]; `embed/gene_vectors.npy` [9741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9741 or target_col == 9741). Every well: [[MAP2K1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP2K1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
