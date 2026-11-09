---
symbol: "TRNAU1AP"
type: "gene"
col: 11080
ensembl_id: "ENSG00000180098"
name: "tRNA selenocysteine 1 associated protein 1"
location: "1p35.3"
module: 4
arm: "-"
pooled_cpm: 39.6
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TRNAU1AP

*tRNA selenocysteine 1 associated protein 1* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +16.2, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.514× (z -11.5, q 6e-28, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.558× (z -9.7, q 5e-20, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGCL]] (+0.68, fdr 7e-06), [[LRRC37B]] (+0.65, fdr 7e-06), [[LRSAM1]] (+0.65, fdr 7e-06); moves opposite to [[RUVBL1]] (-0.66, fdr 7e-06), [[AGPS]] (-0.66, fdr 7e-06), [[ICMT]] (-0.66, fdr 9e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EMP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +16.2 | 0e+00 | 44/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 4e-04 | 27/46 (HS-578T, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.005 | 23/48 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.013 | 20/47 (LoVo, C32, …) | top dose only | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.20× | +3.1 | 0.25 | 13/47 (NCI-H2030, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11080.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.514×** | -11.5 | 6e-28 | 41/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.532×** | -10.9 | 3e-25 | 40/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.557×** | -9.7 | 4e-20 | 34/47 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.558×** | -9.7 | 5e-20 | 35/48 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.372×** | -8.9 | 4e-17 | 38/49 (SNU-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.627×** | -8.1 | 7e-14 | 35/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.632×** | -7.9 | 2e-13 | 34/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.689×** | -6.4 | 9e-09 | 28/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.504×** | -6.2 | 4e-08 | 30/48 (NCI-H2347, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.721×** | -5.6 | 9e-07 | 24/46 (HCT15, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.748×** | -5.0 | 3e-05 | 26/48 (LOX-IMVI, HOP62, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.733×** | -4.9 | 4e-05 | 22/43 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.759×** | -4.7 | 9e-05 | 22/48 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -4.5 | 2e-04 | 22/48 (LOX-IMVI, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.2 | 0.001 | 21/48 (SK-MEL-2, HCT15, …) | top dose only | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.632×** | -4.1 | 0.001 | 22/48 (A-172, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.824×** | -3.2 | 0.040 | 17/48 (C32, SNU-1, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.833× | -3.1 | 0.048 | 8/47 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Procainamide (hydrochloride) (drug)]] 0.5 µM |  | 0.841× | -3.0 | 0.076 | 9/47 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.05 µM |  | 0.845× | -2.9 | 0.097 | 5/48 (HEC-1-A, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 68.2 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.364× (z -8.8) |
| [[HCT15 (line)]] | alt | 91.2 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0791× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.265× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 50.0 | 3 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 68.1 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.351× (z -9.8) |
| [[HOP62 (line)]] | alt | 60.0 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.296× (z -11.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.392× (z -8.8) |
| [[HS-578T (line)]] | alt | 60.0 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1792 (line)]] | alt | 53.4 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +17.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 48.3 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.347× (z -8.5) |
| [[A-172 (line)]] | wt | 34.8 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.315× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 37.4 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +23.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -16.3) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 51.3 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.508× (z -8.7) |
| [[J82 (line)]] | alt | 46.4 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.376× (z -9.4) |
| [[LoVo (line)]] | wt | 23.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +25.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +13.9) | — |
| [[NCI-H23 (line)]] | alt | 41.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.253× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 27.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +21.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.6) | [[Selinexor (drug)]] 5 µM 0.417× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 42.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0607× (z -9.2) |
| [[SW480 (line)]] | alt | 31.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 24.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 24.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 47.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 36.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.423× (z -8.9) |
| [[SW48 (line)]] | wt | 29.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +9.5) | — |
| [[A549 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[AsPC-1 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[Hs 766T (line)]] | wt | 43.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.5) | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H1573 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 31.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.70× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW 1088 (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0510× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.298× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGCL]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[LRRC37B]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[LRSAM1]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ASB14]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[TMEM91]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[KPNB1-DT]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[NPHP3]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.62 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUVBL1]] | -0.66 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[AGPS]] | -0.66 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ICMT]] | -0.66 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[PRELID3B]] | -0.63 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[ATIC]] | -0.63 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[MTHFD1]] | -0.62 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.61 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[RPRD1A]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[PRPF19]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.59 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[PRPS1]] | -0.59 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[B3GALT9]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMP3]] | B | EMP3 activity raises TRNAU1AP's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without EMP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.3, -32.9); signed map (-4.5, 1.3). **Vector** length 119, 32.7% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.5 | +16.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.5 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.9 | -9.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -4.1 | -4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -6.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | tRNA selenocysteine 1 associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,553,085-28,578,545 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SECP43, FLJ20503; previously TRSPAP1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX07](https://www.uniprot.org/uniprotkb/Q9NX07) (tRNA selenocysteine 1-associated protein 1):

> Involved in the early steps of selenocysteine biosynthesis and tRNA(Sec) charging to the later steps resulting in the cotranslational incorporation of selenocysteine into selenoproteins. Stabilizes the SECISBP2, EEFSEC and tRNA(Sec) complex. May be involved in the methylation of tRNA(Sec). Enhances efficiency of selenoproteins synthesis.

**Summary**, from NCBI Gene [54952](https://www.ncbi.nlm.nih.gov/gene/54952):

> Enables RNA binding activity. Predicted to be involved in selenocysteine incorporation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30813) · Entrez [54952](https://www.ncbi.nlm.nih.gov/gene/54952) · UniProt [Q9NX07](https://www.uniprot.org/uniprotkb/Q9NX07) · Ensembl [ENSG00000180098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180098)

## Data

Gene col 11080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11080); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11080]; `tensor/DDL_lfc|DDL_z.npy` [11080]; `embed/gene_vectors.npy` [11080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11080 or target_col == 11080). Every well: [[TRNAU1AP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRNAU1AP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
