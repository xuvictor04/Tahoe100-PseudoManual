---
symbol: "ATP7B"
type: "gene"
col: 4414
ensembl_id: "ENSG00000123191"
name: "ATPase copper transporting beta"
location: "13q14.3"
module: 77
arm: "+"
pooled_cpm: 14.44
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 27
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# ATP7B

*ATPase copper transporting beta* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Brivudine (drug)]] 5 µM: 2.25× (z +6.9, q 4e-09, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.294× (z -27.9, q 0e+00, down in 40 of 44 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.310× (z -18.1, q 0e+00, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.75, fdr 7e-06), [[RGS10]] (+0.74, fdr 7e-06), [[SGTB]] (+0.71, fdr 1e-05); moves opposite to [[PATL2]] (-0.67, fdr 6e-05), [[ANGPT2]] (-0.67, fdr 7e-05), [[RAB30-DT]] (-0.67, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LMX1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Brivudine (drug)]] 5 µM |  | **2.25×** | +6.9 | 4e-09 | 27/46 (COLO 205, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +6.7 | 5e-09 | 22/45 (COLO 205, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +6.6 | 7e-09 | 21/45 (COLO 205, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.3 | 4e-08 | 21/45 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.0 | 6e-05 | 18/46 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 9e-05 | 16/45 (NCI-H2030, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 9e-05 | 18/45 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.013 | 6/46 (MIA PaCa-2, SW48, …) | top dose only |  |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.037 | 6/45 (BT-474, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.14× | +3.1 | 0.11 | 2/45 (KATO III, HOP62) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.0 | 0.13 | 6/45 (KATO III, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4414.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.294×** | -27.9 | 0e+00 | 40/44 (A498, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.310×** | -18.1 | 0e+00 | 37/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.348×** | -17.0 | 0e+00 | 37/43 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.400×** | -14.7 | 0e+00 | 34/45 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.498×** | -11.2 | 3e-27 | 28/44 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.521×** | -10.5 | 8e-24 | 33/45 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.525×** | -10.4 | 3e-23 | 35/45 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.573×** | -9.0 | 2e-17 | 28/45 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.574×** | -8.9 | 3e-17 | 23/36 (HOP62, Panc 03.27, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.598×** | -8.3 | 8e-15 | 26/45 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.574×** | -8.3 | 8e-15 | 19/28 (SNU-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.604×** | -8.1 | 3e-14 | 27/45 (HOP62, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -7.3 | 1e-11 | 25/41 (SW48, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.641×** | -6.9 | 3e-10 | 22/42 (COLO 205, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.450×** | -6.7 | 7e-10 | 22/43 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -6.1 | 4e-08 | 25/44 (A-172, SNU-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -4.3 | 4e-04 | 17/45 (RKO, HT-29, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.793×** | -3.7 | 0.006 | 18/45 (Panc 03.27, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **0.801×** | -3.4 | 0.016 | 8/45 (Panc 03.27, A-172, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.743×** | -3.4 | 0.016 | 11/45 (COLO 205, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.802×** | -3.3 | 0.020 | 12/44 (Panc 03.27, COLO 205, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.811×** | -3.2 | 0.027 | 6/46 (SNU-1, J82, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.868× | -3.2 | 0.029 | 9/46 (SW 900, HOP62, …) | top dose only |  |
| [[Aliskiren (drug)]] 0.5 µM |  | **0.826×** | -3.0 | 0.047 | 6/45 (A549, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 14.7 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -18.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.103× (z -14.7) |
| [[A498 (line)]] | wt | 15.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0918× (z -24.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.113× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 17.8 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0257× (z -24.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0634× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.115× (z -12.6) |
| [[A-172 (line)]] | wt | 27.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0293× (z -24.7) |
| [[A549 (line)]] | wt | 14.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -17.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.106× (z -13.6) |
| [[KATO III (line)]] | alt | 19.6 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -15.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -9.8) |
| [[LS 180 (line)]] | wt | 26.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -19.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0919× (z -18.9) |
| [[SNU-1 (line)]] | wt | 127 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0773× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.227× (z -13.4) |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -14.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0503× (z -13.4) |
| [[HS-578T (line)]] | alt | 9.85 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0463× (z -16.1) |
| [[LoVo (line)]] | wt | 20.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -17.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -9.4) |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -18.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -9.2) |
| [[J82 (line)]] | alt | 14.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -16.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0861× (z -14.8) |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -9.2) |
| [[RKO (line)]] | wt | 12.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0890× (z -11.6) |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -13.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.136× (z -10.4) |
| [[C32 (line)]] | wt | 8.07 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0933× (z -13.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.103× (z -9.1) |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 7.74 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0994× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SW480 (line)]] | alt | 17.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.335× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.05 µM 0.0506× (z -8.9) |
| [[HCT15 (line)]] | alt | 9.93 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0928× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 9.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 5.70 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0738× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 6.08 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 9.53 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.144× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0907× (z -10.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.75 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[RGS10]] | +0.74 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[SGTB]] | +0.71 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[HEBP1]] | +0.69 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[IMPDH1]] | +0.69 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[MPST]] | +0.68 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[EIF4E3]] | +0.67 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[MPZL1]] | +0.67 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MMS19]] | +0.66 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[GNA12]] | +0.65 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[WASF3]] | +0.65 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[COG5]] | +0.64 | +0.65 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | -0.67 | -0.70 / -0.39 | both halves | 6e-05 |  |
| [[ANGPT2]] | -0.67 | -0.66 / -0.38 | both halves | 7e-05 |  |
| [[RAB30-DT]] | -0.67 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.66 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[VPS35L]] | -0.66 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ARMCX4]] | -0.65 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.65 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | -0.65 | -0.71 / -0.34 | both halves | 1e-04 |  |
| [[C11orf58]] | -0.65 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[LINC02889]] | -0.65 | -0.65 / -0.37 | both halves | 7e-05 |  |
| [[MMADHC-DT]] | -0.64 | -0.70 / -0.23 | both halves | 5e-04 |  |
| [[EPC2]] | -0.64 | -0.56 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMX1B]] | B | LMX1B activity raises ATP7B's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.07× lower at baseline in the lines without LMX1B | 0.047 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ATP7B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ATP7B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GULP1]] | C | GULP1 activity lowers ATP7B's level | lines that do not express GULP1 (4) vs lines expressing it (46) | 2.50× higher at baseline in the lines without GULP1 | 0.085 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.745). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.6, 2.0); signed map (-40.7, -3.8). **Vector** length 76.2, 14.6% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +5.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.9 | +0.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -17.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.7 | -27.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -18.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -8.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ATPase copper transporting beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:51,930,436-52,012,125 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously WND |
| Gene groups (HGNC) | ATPase copper transporting |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P35670](https://www.uniprot.org/uniprotkb/P35670) (Copper-transporting ATPase 2):

> Copper ion transmembrane transporter involved in the export of copper out of the cells. It is involved in copper homeostasis in the liver, where it ensures the efflux of copper from hepatocytes into the bile in response to copper overload.

**Summary**, from NCBI Gene [540](https://www.ncbi.nlm.nih.gov/gene/540):

> This gene is a member of the P-type cation transport ATPase family and encodes a protein with several membrane-spanning domains, an ATPase consensus sequence, a hinge domain, a phosphorylation site, and at least 2 putative copper-binding sites. This protein is a monomer, and functions as a copper-transporting ATPase which exports copper out of the cells, such as the efflux of hepatic copper into the bile. Alternate transcriptional splice variants, encoding different isoforms with distinct …

**Accessions** — [HGNC:870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:870) · Entrez [540](https://www.ncbi.nlm.nih.gov/gene/540) · UniProt [P35670](https://www.uniprot.org/uniprotkb/P35670) · Ensembl [ENSG00000123191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123191)

## Data

Gene col 4414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4414); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4414]; `tensor/DDL_lfc|DDL_z.npy` [4414]; `embed/gene_vectors.npy` [4414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4414 or target_col == 4414). Every well: [[ATP7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
