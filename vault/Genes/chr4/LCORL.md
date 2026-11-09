---
symbol: "LCORL"
type: "gene"
col: 10904
ensembl_id: "ENSG00000178177"
name: "ligand dependent nuclear receptor corepressor like"
location: "4p15.31"
module: 225
arm: "+"
pooled_cpm: 229.6
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# LCORL

*ligand dependent nuclear receptor corepressor like* — 4p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.42× (z +17.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.387× (z -18.5, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.786× (z -4.7, q 2e-04, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A40]] (+0.64, fdr 7e-06), [[CNNM2]] (+0.63, fdr 1e-05), [[SAP30]] (+0.63, fdr 1e-05); moves opposite to [[ZPR1]] (-0.59, fdr 1e-05), [[IKBKG]] (-0.59, fdr 1e-05), [[LSG1]] (-0.59, fdr 1e-05).
> It is in [[Module 225]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM83H]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.42×** | +17.3 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +13.8 | 1e-40 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.80×** | +11.5 | 4e-28 | 45/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +11.1 | 2e-26 | 43/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +9.2 | 6e-18 | 30/48 (NCI-H460, HEC-1-A, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +7.2 | 5e-11 | 32/48 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +6.2 | 5e-08 | 35/49 (C32, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.1 | 8e-08 | 33/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +5.3 | 8e-06 | 31/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.009 | 26/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +3.7 | 0.009 | 25/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.028 | 20/48 (AsPC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.046 | 24/48 (HCT15, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10904.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.387×** | -18.5 | 0e+00 | 46/49 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.391×** | -17.6 | 0e+00 | 40/44 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -11.1 | 2e-26 | 44/45 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.692×** | -6.9 | 8e-10 | 40/47 (SNU-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.720×** | -6.4 | 2e-08 | 34/48 (RPMI-7951, SHP-77, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.770×** | -5.1 | 3e-05 | 33/48 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.7 | 2e-04 | 33/48 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.841× | -4.5 | 4e-04 | 20/48 (HOP62, A-427, …) | top dose only | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.645×** | -4.5 | 5e-04 | 26/38 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -4.3 | 9e-04 | 17/48 (HCT15, SK-MEL-2, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.657×** | -4.3 | 1e-03 | 35/47 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.816×** | -4.0 | 0.003 | 28/48 (SHP-77, HCT15, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.006 | 26/48 (RKO, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.837× | -3.5 | 0.022 | 20/48 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.026 | 20/48 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.848× | -3.2 | 0.046 | 17/47 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.849× | -3.2 | 0.046 | 17/49 (SW 900, hTERT-HPNE, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.733×** | -3.2 | 0.046 | 23/46 (COLO 205, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.851× | -3.1 | 0.049 | 11/48 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.776×** | -3.1 | 0.053 | 22/48 (COLO 205, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.863× | -2.9 | 0.097 | 15/49 (J82, LoVo, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.856× | -2.9 | 0.097 | 15/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 169 | 10 (4 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 6.30× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -12.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 418 | 5 (1 ⚠) | 5 (5 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.05× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -12.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 351 | 4 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 317 | 4 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 144 | 7 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.62× (z +18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.55× (z +18.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.466× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 292 | 3 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -21.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 489 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -14.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 189 | 5 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -18.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 284 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -14.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 188 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.61× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.554× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 338 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -13.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 247 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -15.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 239 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -14.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 245 | 3 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.67× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 276 | 4 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.47× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -23.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 337 | 1 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -13.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 281 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -12.4) ⚠ cell-cycle shift, explains ~79% of this change |
| [[BT-474 (line)]] | alt | 135 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 278 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.03× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -14.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 293 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 192 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +13.3) | [[Ixazomib citrate (drug)]] 5 µM 0.458× (z -11.2) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.517× (z -9.5) |
| [[SW48 (line)]] | wt | 255 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.54× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -13.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 361 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -17.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 310 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -23.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 185 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -16.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 210 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -13.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 321 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -16.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 231 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -17.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 173 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.7) ⚠ cell-cycle shift, explains ~24% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -12.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 315 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -16.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 364 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -17.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 198 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 303 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -12.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 157 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.5) | — |
| [[C32 (line)]] | wt | 212 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 186 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -15.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 280 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -16.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 338 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -23.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.3) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[A498 (line)]] | wt | 67.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.9) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[HS-578T (line)]] | alt | 168 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 174 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.63× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 90.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -9.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 314 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 178 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 332 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A40]] | +0.64 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.63 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[SAP30]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TESK2]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CUTA]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TXNDC16]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PHIP]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[MIS18BP1]] | +0.57 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[PTTG1]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[FOXN3]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[A2MP1]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[CNOT6L]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZPR1]] | -0.59 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[IKBKG]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[LSG1]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PSMD12]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[HARS1]] | -0.55 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[MAK16]] | -0.54 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[FTSJ3]] | -0.53 | -0.73 / -0.28 | both halves | 3e-04 |  |
| [[ZNF562]] | -0.53 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[ABCF2]] | -0.53 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[EXOC7]] | -0.53 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[DHX37]] | -0.53 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[ELAC2]] | -0.53 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83H]] | B | FAM83H activity lowers LCORL's level | lines that do not express FAM83H (13) vs lines expressing it (37) | 1.19× higher at baseline in the lines without FAM83H | 0.032 | ⚠ within organs, on part of the lines; also absent: IQANK1, EVPL, OCLN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.1, -41.3); signed map (-15.7, 13.7). **Vector** length 115, 44.3% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +13.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.9 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -8.3 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.5 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ligand dependent nuclear receptor corepressor like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.31 — chr4:17,841,187-18,021,876 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MLR1, FLJ30696 |
| Gene groups (HGNC) | Helix-turn-helix motif Psq family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3X6](https://www.uniprot.org/uniprotkb/Q8N3X6) (Ligand-dependent nuclear receptor corepressor-like protein):

> May act as transcription activator that binds DNA elements with the sequence 5'-CCCTATCGATCGATCTCTACCT-3'. May play a role in spermatogenesis (By similarity).

**Summary**, from NCBI Gene [254251](https://www.ncbi.nlm.nih.gov/gene/254251):

> This gene encodes a transcription factor that appears to function in spermatogenesis. Polymorphisms in this gene are associated with measures of skeletal frame size and adult height. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:30776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30776) · Entrez [254251](https://www.ncbi.nlm.nih.gov/gene/254251) · UniProt [Q8N3X6](https://www.uniprot.org/uniprotkb/Q8N3X6) · Ensembl [ENSG00000178177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178177)

## Data

Gene col 10904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10904); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10904]; `tensor/DDL_lfc|DDL_z.npy` [10904]; `embed/gene_vectors.npy` [10904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10904 or target_col == 10904). Every well: [[LCORL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LCORL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
