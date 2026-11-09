---
symbol: "AZIN2"
type: "gene"
col: 6665
ensembl_id: "ENSG00000142920"
name: "antizyme inhibitor 2"
location: "1p35.1"
module: 88
arm: "-"
pooled_cpm: 14.29
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 32
n_dd_up_clean: 12
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# AZIN2

*antizyme inhibitor 2* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.98× (z +23.9, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (17 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.422× (z -12.8, q 1e-34, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKMY2]] (+0.66, fdr 7e-06), [[NQO2]] (+0.63, fdr 7e-06), [[SLC27A1]] (+0.62, fdr 2e-05); moves opposite to [[CPSF2]] (-0.66, fdr 1e-05), [[AASDHPPT]] (-0.65, fdr 1e-05), [[DNAJC11]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.98×** | +23.9 | 0e+00 | 45/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.80×** | +23.3 | 0e+00 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.38×** | +18.1 | 0e+00 | 43/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +14.6 | 0e+00 | 37/46 (SW480, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +11.1 | 1e-26 | 32/43 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +9.1 | 9e-18 | 29/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.66×** | +7.6 | 2e-12 | 28/45 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +6.8 | 5e-10 | 27/45 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +4.9 | 7e-05 | 20/46 (LoVo, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.37×** | +4.7 | 1e-04 | 16/44 (LS 180, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 13/47 (HOP62, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.003 | 15/45 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.007 | 12/47 (A-427, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.28×** | +3.6 | 0.014 | 15/44 (C32, NCI-H460, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.091 | 3/46 (A-427, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.422×** | -12.8 | 1e-34 | 34/46 (A498, SW480, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.445×** | -11.6 | 2e-28 | 32/46 (SNU-423, A498, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.232×** | -11.3 | 2e-27 | 37/45 (SK-MEL-2, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.478×** | -11.0 | 8e-26 | 24/37 (MIA PaCa-2, LoVo, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.545×** | -9.0 | 2e-17 | 26/42 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.569×** | -8.4 | 5e-15 | 28/47 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.574×** | -8.2 | 1e-14 | 28/47 (SNU-423, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.593×** | -7.8 | 6e-13 | 29/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.380×** | -7.5 | 4e-12 | 26/43 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.703×** | -7.4 | 8e-12 | 23/45 (HS-578T, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.637×** | -6.7 | 1e-09 | 22/43 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.650×** | -6.1 | 4e-08 | 21/41 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.771×** | -5.5 | 2e-06 | 22/47 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.702×** | -5.2 | 7e-06 | 16/44 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.705×** | -5.0 | 2e-05 | 21/45 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.726×** | -4.8 | 7e-05 | 19/46 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.658×** | -4.4 | 3e-04 | 15/44 (HOP62, SK-MEL-2, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.001 | 13/47 (SK-MEL-2, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.5 | 0.010 | 16/45 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.643×** | -3.4 | 0.012 | 5/41 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.654×** | -3.3 | 0.019 | 11/39 (HCT15, hTERT-HPNE, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.05 µM |  | **0.791×** | -3.3 | 0.020 | 10/46 (MIA PaCa-2, Hs 766T, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.663×** | -3.2 | 0.026 | 12/44 (Hs 766T, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **0.813×** | -3.0 | 0.056 | 10/46 (A-172, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.6 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.00× (z +11.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -16.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.255× (z -9.8) |
| [[SW480 (line)]] | alt | 14.1 | 6 | 1 | [[Panobinostat (drug)]] 0.5 µM 10.3× (z +18.1) | [[Harringtonine (drug)]] 0.5 µM 0.294× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 6.41 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 12.2× (z +14.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[PANC-1 (line)]] | alt | 10.1 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 9.46× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0663× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0587× (z -9.5) |
| [[HOP62 (line)]] | alt | 24.1 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.216× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HT-29 (line)]] | alt | 4.42 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 20.2× (z +10.0) | — |
| [[LoVo (line)]] | wt | 23.3 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.02× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 15.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0831× (z -19.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 32.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.94× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -20.4) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 4.95 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 18.2× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.55× (z +10.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -10.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 10.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.11× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 5.19 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.57× (z +9.8) | [[Docetaxel (drug)]] 0.05 µM 0.123× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.07× (z +8.8) | [[TAK-901 (drug)]] 5 µM 0.0505× (z -9.9) |
| [[SNU-423 (line)]] | alt | 18.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.06× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.0579× (z -15.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 6.93 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 8.51 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0587× (z -9.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.0636× (z -9.1) |
| [[H4 (line)]] | wt | 19.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -9.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[Hs 766T (line)]] | wt | 41.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.92× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.00× (z +8.9) | — |
| [[KATO III (line)]] | alt | 5.09 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.9× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 17.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.27× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 15.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.77× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 12.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.54× (z +10.2) | — |
| [[A-427 (line)]] | wt | 11.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 5.35 | 0 | 1 | — | [[Budesonide (drug)]] 0.05 µM 0.0705× (z -8.6) |
| [[C32 (line)]] | wt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 11.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.24× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 6.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H1573 (line)]] | alt | 6.12 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.53× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 6.46 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.66× (z +8.6) | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0825× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 6.21 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0850× (z -9.5) |
| [[SW 900 (line)]] | alt | 9.67 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0505× (z -13.0) |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKMY2]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NQO2]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[KCTD7]] | +0.62 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.62 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[UBA6]] | +0.62 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[LPCAT2]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SEMA6C]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[STK32C]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[MOSPD3]] | +0.60 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[SH3PXD2B]] | +0.59 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[F11R]] | +0.59 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | -0.66 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.65 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.64 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.64 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[ZNF252P-1]] | -0.63 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[MTHFSD]] | -0.63 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ST7L]] | -0.63 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ZC3H4]] | -0.62 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.62 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[TASOR]] | -0.62 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SENP1]] | -0.61 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[ANAPC13]] | -0.61 | -0.59 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AZIN2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TCF7L1]] | B | TCF7L1 activity raises AZIN2's level | lines that do not express TCF7L1 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without TCF7L1 | 0.075 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A |
| [[PMP22]] | B | PMP22 activity raises AZIN2's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without PMP22 | 0.085 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[STARD9]] | B | STARD9 activity raises AZIN2's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.97× lower at baseline in the lines without STARD9 | 0.094 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-5.1, 3.0); signed map (-32.0, 19.5). **Vector** length 73.9, 14.6% of its response variance represented; |z| ≥ 3 in 1,376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +23.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +23.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +14.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +18.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +6.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.5 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.9 | -11.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.7 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.7 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -7.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.1 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | antizyme inhibitor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:33,081,104-33,123,492 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ODC-p, ODC1L, KIAA1945, ODCp; previously ADC |
| Gene groups (HGNC) | Antizyme inhibitor family |
| Reactome | 2 pathways, smallest: Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A70](https://www.uniprot.org/uniprotkb/Q96A70) (Antizyme inhibitor 2):

> Antizyme inhibitor (AZI) protein that positively regulates ornithine decarboxylase (ODC) activity and polyamine uptake. AZI is an enzymatically inactive ODC homolog that counteracts the negative effect of ODC antizymes (AZs) OAZ1, OAZ2 and OAZ3 on ODC activity by competing with ODC for antizyme-binding. Inhibits antizyme-dependent ODC degradation and releases ODC monomers from their inactive complex with antizymes, leading to formation of the catalytically active ODC homodimer and restoring …

**Summary**, from NCBI Gene [113451](https://www.ncbi.nlm.nih.gov/gene/113451):

> The protein encoded by this gene belongs to the antizyme inhibitor family, which plays a role in cell growth and proliferation by maintaining polyamine homeostasis within the cell. Antizyme inhibitors are homologs of ornithine decarboxylase (ODC, the key enzyme in polyamine biosynthesis) that have lost the ability to decarboxylase ornithine; however, retain the ability to bind to antizymes. Antizymes negatively regulate intracellular polyamine levels by binding to ODC and targeting it for …

**Accessions** — [HGNC:29957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29957) · Entrez [113451](https://www.ncbi.nlm.nih.gov/gene/113451) · UniProt [Q96A70](https://www.uniprot.org/uniprotkb/Q96A70) · Ensembl [ENSG00000142920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142920)

## Data

Gene col 6665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6665); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6665]; `tensor/DDL_lfc|DDL_z.npy` [6665]; `embed/gene_vectors.npy` [6665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6665 or target_col == 6665). Every well: [[AZIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AZIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
