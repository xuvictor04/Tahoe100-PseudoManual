---
symbol: "ZKSCAN1"
type: "gene"
col: 2735
ensembl_id: "ENSG00000106261"
name: "zinc finger with KRAB and SCAN domains 1"
location: "7q22.1"
module: 20
arm: "-"
pooled_cpm: 199.02
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ZKSCAN1

*zinc finger with KRAB and SCAN domains 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.47× (z +7.4, q 1e-10, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.464× (z -14.1, q 2e-42, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.246× (z -14.0, q 3e-42, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCL]] (+0.71, fdr 7e-06), [[NKAP]] (+0.69, fdr 7e-06), [[GCC2]] (+0.69, fdr 7e-06); moves opposite to [[TFDP1]] (-0.69, fdr 7e-06), [[RPSA]] (-0.65, fdr 1e-05), [[SKP2]] (-0.64, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +7.4 | 1e-10 | 34/48 (A498, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +7.3 | 1e-10 | 30/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.0 | 4e-07 | 29/49 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 6e-07 | 27/48 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.7 | 1e-06 | 31/48 (RKO, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.28×** | +4.7 | 2e-04 | 30/48 (A498, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.005 | 21/48 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.005 | 28/49 (KATO III, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.005 | 24/48 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.21×** | +3.6 | 0.020 | 22/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.020 | 27/48 (HCT15, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.039 | 21/48 (BT-474, SW48, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.2 | 0.060 | 0/50 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.079 | 21/50 (AsPC-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.464×** | -14.1 | 2e-42 | 45/47 (C-33 A, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.246×** | -14.0 | 3e-42 | 49/49 (H4, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.263×** | -13.4 | 2e-38 | 46/48 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -9.4 | 6e-19 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -8.6 | 1e-15 | 33/44 (SNU-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -8.6 | 1e-15 | 35/48 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -8.4 | 3e-15 | 40/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.621×** | -8.4 | 3e-15 | 38/45 (KATO III, H4, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.652×** | -7.8 | 3e-13 | 38/49 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.692×** | -7.0 | 1e-10 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.723×** | -6.2 | 4e-08 | 36/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.758×** | -5.3 | 6e-06 | 30/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.795×** | -4.3 | 6e-04 | 30/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.795×** | -4.2 | 0.001 | 27/48 (C32, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.826×** | -3.6 | 0.011 | 23/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.829×** | -3.5 | 0.014 | 23/48 (SW480, HCT15, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.704×** | -3.5 | 0.016 | 29/48 (C32, J82, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.834× | -3.2 | 0.034 | 21/47 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.885× | -3.2 | 0.034 | 10/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.851× | -2.9 | 0.084 | 16/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 321 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.342× (z -17.1) |
| [[PANC-1 (line)]] | alt | 162 | 3 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.6) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.371× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.387× (z -14.9) |
| [[COLO 205 (line)]] | alt | 534 | 0 | 9 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -15.2) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.289× (z -14.4) |
| [[H4 (line)]] | wt | 216 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -15.3) |
| [[HT-29 (line)]] | alt | 237 | 0 | 9 (5 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.177× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 316 | 2 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.165× (z -12.4) |
| [[C32 (line)]] | wt | 359 | 2 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.6) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.01× (z +8.9) | [[PH-797804 (drug)]] 5 µM 0.180× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 205 | 0 | 8 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.295× (z -13.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.472× (z -8.8) |
| [[HOP62 (line)]] | alt | 179 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +8.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.375× (z -12.6) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.193× (z -11.5) |
| [[KATO III (line)]] | alt | 370 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.386× (z -11.9) |
| [[LS 180 (line)]] | wt | 265 | 0 | 7 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.129× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 206 | 5 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +20.6) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.280× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 181 | 1 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.6) ⚠ cell-cycle shift, explains ~24% of this change | [[Digitoxin (drug)]] 0.05 µM 0.400× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 316 | 0 | 7 (4 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.160× (z -12.6) |
| [[A549 (line)]] | wt | 150 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.92× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.246× (z -10.1) |
| [[Hs 766T (line)]] | wt | 235 | 2 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.266× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 242 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.2) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.1) | [[TAK-901 (drug)]] 5 µM 0.151× (z -13.3) |
| [[A-172 (line)]] | wt | 159 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.3) ⚠ cell-cycle shift, explains ~24% of this change | [[PH-797804 (drug)]] 5 µM 0.166× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 175 | 3 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.3) | [[TAK-901 (drug)]] 5 µM 0.173× (z -10.8) |
| [[HCT15 (line)]] | alt | 230 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.520× (z -8.7) |
| [[J82 (line)]] | alt | 134 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.90× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.355× (z -12.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.462× (z -9.9) |
| [[LoVo (line)]] | wt | 213 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +19.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +13.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.360× (z -15.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 182 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.116× (z -14.6) |
| [[SNU-423 (line)]] | alt | 197 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.173× (z -11.4) |
| [[HS-578T (line)]] | alt | 140 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.9) | [[PH-797804 (drug)]] 5 µM 0.169× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 144 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.409× (z -9.4) ⚠ toxic |
| [[RKO (line)]] | wt | 214 | 2 | 1 | [[Homoharringtonine (drug)]] 0.05 µM 2.35× (z +10.2) | [[PH-797804 (drug)]] 5 µM 0.209× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 191 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.230× (z -9.6) |
| [[A-427 (line)]] | wt | 103 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +10.4) | — |
| [[A498 (line)]] | wt | 135 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 220 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -9.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.184× (z -15.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.225× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 129 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +17.9) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 79.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +17.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.01× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 145 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.8) ⚠ cell-cycle shift, explains ~24% of this change | [[Dinaciclib (drug)]] 5 µM 0.124× (z -19.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 362 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0483× (z -9.8) |
| [[SW 900 (line)]] | alt | 196 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.200× (z -10.1) |
| [[SW48 (line)]] | wt | 209 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 240 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.11× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.182× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 149 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.222× (z -9.5) |
| [[SW1417 (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[CHP-212 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 158 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 210 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCL]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[NKAP]] | +0.69 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[GCC2]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[OFD1]] | +0.65 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.65 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MFAP1]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.63 | +0.55 / +0.69 | both halves | 1e-05 | same gene group |
| [[ADPRM]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GATAD1]] | +0.63 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[AK6]] | +0.63 | +0.57 / +0.69 | both halves | 9e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFDP1]] | -0.69 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[RPSA]] | -0.65 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[SKP2]] | -0.64 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[MFSD14B]] | -0.64 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[ICMT]] | -0.63 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[ARF3]] | -0.63 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[TMEM109]] | -0.63 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[PABIR2]] | -0.62 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[FAR1]] | -0.62 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.62 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[EMB]] | -0.61 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[SEPHS1]] | -0.60 | -0.61 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-27.6, -33.4); signed map (-4.6, 3.0). **Vector** length 140, 51.8% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +9.3 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +5.3 | +3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.2 | +4.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.2 | +3.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.6 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.3 | -8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.4 | -8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.1 | -7.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.9 | -14.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.3 | -13.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.4 | -3.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger with KRAB and SCAN domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,015,572-100,041,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX18, PHZ-37, ZSCAN33; previously ZNF139, ZNF36 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17029](https://www.uniprot.org/uniprotkb/P17029) (Zinc finger protein with KRAB and SCAN domains 1):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7586](https://www.ncbi.nlm.nih.gov/gene/7586):

> This gene encodes a member of the Kruppel C2H2-type zinc-finger family of proteins. This encoded protein may function as a transcription factor that regulates the expression of GABA type-A receptors in the brain. Transcripts from this gene have been shown to form stable and abundant circular RNAs. Elevated expression of this gene has been observed in gastric cancer and the encoded protein may stimulate migration and invasion of human gastric cancer cells. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:13101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13101) · Entrez [7586](https://www.ncbi.nlm.nih.gov/gene/7586) · UniProt [P17029](https://www.uniprot.org/uniprotkb/P17029) · Ensembl [ENSG00000106261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106261)

## Data

Gene col 2735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2735); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2735]; `tensor/DDL_lfc|DDL_z.npy` [2735]; `embed/gene_vectors.npy` [2735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2735 or target_col == 2735). Every well: [[ZKSCAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZKSCAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
