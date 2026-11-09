---
symbol: "CLIC4"
type: "gene"
col: 9813
ensembl_id: "ENSG00000169504"
name: "CLIC family member 4"
location: "1p36.11"
module: 111
arm: "+"
pooled_cpm: 245.04
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# CLIC4

*CLIC family member 4* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.12× (z +7.9, q 2e-12, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.595× (z -10.1, q 4e-21, down in 38 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.683× (z -7.7, q 4e-12, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOA]] (+0.54, fdr 3e-05), [[CHP1]] (+0.52, fdr 4e-05), [[CDC42]] (+0.52, fdr 1e-05); moves opposite to [[MRPL32]] (-0.52, fdr 2e-05), [[YBEY]] (-0.50, fdr 4e-05), [[LARS2]] (-0.49, fdr 4e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BCAT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +7.9 | 2e-12 | 37/49 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.22×** | +5.6 | 6e-06 | 27/48 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 3e-05 | 36/48 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +5.0 | 6e-05 | 26/44 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.9 | 9e-05 | 29/49 (COLO 205, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 1e-04 | 26/48 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +4.6 | 3e-04 | 27/50 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.6 | 3e-04 | 28/48 (C-33 A, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +4.5 | 4e-04 | 24/48 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +4.4 | 6e-04 | 19/49 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.4 | 7e-04 | 23/48 (A498, hTERT-HPNE, …) | top dose only | composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.009 | 23/48 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.18× | +3.3 | 0.041 | 18/49 (A-172, A-427, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.055 | 18/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.058 | 22/48 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.083 | 19/48 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Encorafenib (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.083 | 16/48 (SW480, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.083 | 12/48 (C-33 A, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.094 | 18/48 (SNU-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -10.1 | 4e-21 | 38/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -7.7 | 4e-12 | 29/48 (NCI-H23, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.688×** | -7.5 | 9e-12 | 39/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -7.5 | 1e-11 | 34/48 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -6.6 | 4e-09 | 33/48 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.724×** | -6.5 | 7e-09 | 32/48 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -6.4 | 2e-08 | 33/48 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.779×** | -5.0 | 4e-05 | 26/48 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.841× | -4.9 | 5e-05 | 21/48 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **0.784×** | -4.9 | 5e-05 | 29/48 (RPMI-7951, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -4.7 | 1e-04 | 19/48 (Hs 766T, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -4.4 | 4e-04 | 22/48 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.770×** | -4.4 | 4e-04 | 26/47 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | 0.868× | -4.0 | 0.002 | 13/48 (J82, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.822×** | -3.9 | 0.003 | 25/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.712×** | -3.6 | 0.011 | 26/47 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.717×** | -3.5 | 0.014 | 20/47 (HCT15, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.038 | 21/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.898× | -3.1 | 0.053 | 4/49 (A-172, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 201 | 3 (1 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +11.6) | [[Harringtonine (drug)]] 0.5 µM 0.233× (z -21.9) |
| [[C32 (line)]] | wt | 356 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.94× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -10.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 162 | 1 | 3 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.75× (z +8.5) | [[Harringtonine (drug)]] 0.5 µM 0.383× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 103 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.09× (z +9.0) | [[Harringtonine (drug)]] 0.5 µM 0.341× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 231 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.564× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.545× (z -8.6) |
| [[A498 (line)]] | wt | 210 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +30.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.69× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 245 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 293 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.75× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.474× (z -9.1) |
| [[HOP62 (line)]] | alt | 579 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.278× (z -11.2) |
| [[HT-29 (line)]] | alt | 203 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 145 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.13× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 368 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.513× (z -9.0) |
| [[A549 (line)]] | wt | 163 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.396× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 185 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.08× (z +11.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -12.0) |
| [[BT-474 (line)]] | alt | 210 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.9× (z +14.7) | — |
| [[COLO 205 (line)]] | alt | 76.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 100 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 338 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.96× (z +11.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.465× (z -9.2) |
| [[KATO III (line)]] | alt | 63.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.7) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.424× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 291 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.45× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 229 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 1.72× (z +8.8) | [[Homoharringtonine (drug)]] 0.05 µM 0.558× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 667 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 161 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.73× (z +9.2) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.559× (z -10.0) |
| [[A-172 (line)]] | wt | 264 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.481× (z -8.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 153 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.99× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 205 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[Hs 766T (line)]] | wt | 440 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.383× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 397 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +15.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 396 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.501× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 215 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.67× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 293 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 158 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.361× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 153 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 250 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.441× (z -10.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 265 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.404× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 190 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.432× (z -9.4) |
| [[SW1417 (line)]] | alt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 232 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 291 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 675 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 229 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 419 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 494 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOA]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CHP1]] | +0.52 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[CDC42]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FERMT2]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[GNB1]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[SLC7A5]] | +0.50 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[MAGT1]] | +0.49 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[CAPZB]] | +0.48 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[ULBP1]] | +0.47 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[TPM4]] | +0.47 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[IQGAP1]] | +0.47 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[GLIPR1]] | +0.46 | +0.39 / +0.48 | both halves | 6e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL32]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[YBEY]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[LARS2]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[COA6]] | -0.49 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[IGHMBP2]] | -0.47 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[TTC4]] | -0.47 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC17]] | -0.46 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[LSM6]] | -0.46 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[MLH3]] | -0.46 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[POLL]] | -0.45 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[MRM3]] | -0.44 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[RPAP1]] | -0.44 | -0.41 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAT1]] | B | BCAT1 activity raises CLIC4's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 1.63× lower at baseline in the lines without BCAT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX |
| [[GFPT2]] | B | GFPT2 activity raises CLIC4's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 1.63× lower at baseline in the lines without GFPT2 | 0.021 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[CNN3]] | B | CNN3 activity raises CLIC4's level | lines that do not express CNN3 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without CNN3 | 0.082 | ⚠ within organs, on part of the lines; also absent: SLC9A9, SLC35F1, CNN3-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-52.9, -1.1); signed map (-9.5, 35.2). **Vector** length 153, 52.5% of its response variance represented; |z| ≥ 3 in 1,455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +6.6 | +5.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +6.6 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.4 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +4.0 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.1 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.3 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.2 | -6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.1 | -7.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.9 | -10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.0 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -4.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | CLIC family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,745,382-24,844,321 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566G223, CLIC4L, P64H1, H1, huH1, p64H1 |
| Gene groups (HGNC) | CLIC family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y696](https://www.uniprot.org/uniprotkb/Q9Y696) (Chloride intracellular channel protein 4):

> In the soluble state, catalyzes glutaredoxin-like thiol disulfide exchange reactions with reduced glutathione as electron donor. Can insert into membranes and form voltage-dependent multi-ion conductive channels. Membrane insertion seems to be redox-regulated and may occur only under oxidizing conditions (By similarity). Has alternate cellular functions like a potential role in angiogenesis or in maintaining apical-basolateral membrane polarity during mitosis and cytokinesis. Could also promote …

**Summary**, from NCBI Gene [25932](https://www.ncbi.nlm.nih.gov/gene/25932):

> Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. Chloride intracellular channel 4 (CLIC4) protein, encoded by the CLIC4 gene, is a member of the p64 family; the gene is expressed in many tissues and exhibits a intracellular vesicular pattern in Panc-1 cells (pancreatic cancer cells). [provided by RefSeq, Jul …

**Accessions** — [HGNC:13518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13518) · Entrez [25932](https://www.ncbi.nlm.nih.gov/gene/25932) · UniProt [Q9Y696](https://www.uniprot.org/uniprotkb/Q9Y696) · Ensembl [ENSG00000169504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169504)

## Data

Gene col 9813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9813); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9813]; `tensor/DDL_lfc|DDL_z.npy` [9813]; `embed/gene_vectors.npy` [9813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9813 or target_col == 9813). Every well: [[CLIC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLIC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
