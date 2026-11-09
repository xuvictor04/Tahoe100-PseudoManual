---
symbol: "CKAP5"
type: "gene"
col: 10583
ensembl_id: "ENSG00000175216"
name: "cytoskeleton associated protein 5"
location: "11p11.2"
module: 22
arm: "+"
pooled_cpm: 213.27
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CKAP5

*cytoskeleton associated protein 5* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +12.4, q 1e-32, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~90% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.60× (z +5.5, q 3e-06, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (Panc 03.27 2.54×, A549 2.76×, PANC-1 2.02×, RKO 2.18×, …; ⚠ cell-cycle shift, explains ~90% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 3.27×, LoVo 2.69×; ⚠ cell-cycle shift, explains ~69% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 2.73×, LoVo 2.17×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LoVo 3.94×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.527× (z -14.3, q 6e-44, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUB1]] (+0.89, fdr 7e-06), [[ARHGAP11A]] (+0.88, fdr 7e-06), [[CCNA2]] (+0.87, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10583.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (Panc 03.27 2.54×, A549 2.76×, PANC-1 2.02×, RKO 2.18×, …; ⚠ cell-cycle shift, explains ~90% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (KATO III 3.27×, LoVo 2.69×; ⚠ cell-cycle shift, explains ~69% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 2.73×, LoVo 2.17×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 1 line (LoVo 3.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.48×** | +12.4 | 1e-32 | 35/48 (Panc 03.27, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.43×** | +8.0 | 3e-13 | 35/48 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.84×** | +7.2 | 1e-10 | 41/47 (J82, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +6.2 | 9e-08 | 32/48 (LoVo, SW480, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +6.2 | 9e-08 | 32/48 (KATO III, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +5.6 | 2e-06 | 29/48 (KATO III, COLO 205, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.5 | 3e-06 | 31/48 (LoVo, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.28×** | +5.5 | 3e-06 | 27/48 (KATO III, COLO 205, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **1.28×** | +5.4 | 5e-06 | 27/47 (NCI-H1792, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.24×** | +4.9 | 6e-05 | 26/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.51×** | +4.8 | 7e-05 | 28/49 (LoVo, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.22×** | +4.5 | 4e-04 | 24/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.20×** | +4.2 | 0.001 | 22/47 (NCI-H23, H4, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.13× | +3.8 | 0.006 | 10/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.017 | 6/49 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.052 | 16/49 (AsPC-1, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.15× | +3.0 | 0.073 | 15/47 (HOP62, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -14.3 | 6e-44 | 47/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.713×** | -7.3 | 9e-11 | 37/47 (NCI-H2030, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.811×** | -6.6 | 6e-09 | 26/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.780×** | -5.6 | 4e-06 | 28/48 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.798×** | -4.9 | 1e-04 | 28/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.811×** | -4.7 | 2e-04 | 26/49 (SNU-1, A549, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.811×** | -4.7 | 2e-04 | 27/48 (A498, H4, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.820×** | -4.4 | 7e-04 | 24/48 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.837× | -4.0 | 0.004 | 23/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.843× | -3.8 | 0.007 | 23/48 (H4, A-427, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.844× | -3.8 | 0.007 | 20/49 (A-427, LOX-IMVI, …) | two highest doses |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.844× | -3.8 | 0.007 | 22/48 (SHP-77, H4, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.793×** | -3.7 | 0.009 | 25/48 (CHP-212, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.839× | -3.6 | 0.011 | 23/47 (H4, A-427, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.853× | -3.5 | 0.015 | 16/48 (HS-578T, SW1417, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.902× | -3.3 | 0.035 | 13/48 (A498, NCI-H2347, …) | top dose only |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 0.855× | -3.2 | 0.035 | 14/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 0.855× | -3.2 | 0.035 | 19/48 (HOP62, H4, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.822×** | -3.1 | 0.051 | 20/47 (AsPC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.056 | 14/48 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.908× | -3.0 | 0.063 | 7/48 (A-427, LS 180, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.875× | -3.0 | 0.073 | 10/48 (A549, SW 1271, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.831×** | -3.0 | 0.075 | 23/48 (AN3 CA, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.880× | -2.8 | 0.099 | 10/48 (A-172, HepG2/C3A, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.914× | -2.8 | 0.099 | 4/48 (HCT15, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 133 | 8 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +13.9) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.94× (z +10.1) | — |
| [[KATO III (line)]] | alt | 179 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +15.3) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[A-427 (line)]] | wt | 309 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 253 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +13.4) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.405× (z -15.4) |
| [[HOP62 (line)]] | alt | 228 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.1) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.295× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 129 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.6) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[H4 (line)]] | wt | 208 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -9.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 133 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.8) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[LOX-IMVI (line)]] | wt | 197 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.1) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.377× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 160 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.5) ⚠ cell-cycle shift, explains ~90% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.435× (z -10.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 218 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.9) ⚠ cell-cycle shift, explains ~69% of this change | [[Auranofin (drug)]] 5 µM 0.351× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 229 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.8) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.456× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 167 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.4) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.551× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 271 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +19.2) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.500× (z -10.1) |
| [[PANC-1 (line)]] | alt | 264 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +16.1) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[RKO (line)]] | wt | 248 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.3) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.376× (z -13.7) |
| [[SNU-1 (line)]] | wt | 247 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.472× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 226 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.9) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.412× (z -10.2) |
| [[SW1417 (line)]] | alt | 331 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.2) ⚠ cell-cycle shift, explains ~90% of this change | [[Auranofin (drug)]] 5 µM 0.531× (z -9.8) |
| [[SW480 (line)]] | alt | 277 | 1 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 1.75× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.419× (z -14.2) |
| [[A-172 (line)]] | wt | 251 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.509× (z -9.7) |
| [[A498 (line)]] | wt | 238 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.604× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 233 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +17.3) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[C-33 A (line)]] | alt | 294 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.457× (z -9.2) |
| [[C32 (line)]] | wt | 158 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.376× (z -11.5) |
| [[COLO 205 (line)]] | alt | 78.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.85× (z +8.5) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[HS-578T (line)]] | alt | 171 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.7) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[J82 (line)]] | alt | 279 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.532× (z -9.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.4) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[SHP-77 (line)]] | alt | 313 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.394× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 219 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.399× (z -11.2) |
| [[SW 1271 (line)]] | alt | 304 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.238× (z -9.7) |
| [[SW48 (line)]] | wt | 282 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.329× (z -12.2) |
| [[AN3 CA (line)]] | alt | 368 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 199 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUB1]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 766 |
| [[ARHGAP11A]] | +0.88 | +0.87 / +0.89 | both halves | 7e-06 |  |
| [[CCNA2]] | +0.87 | +0.85 / +0.85 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[DLGAP5]] | +0.87 | +0.85 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 726 |
| [[BUB1B]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 823 |
| [[KIF4A]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 672 |
| [[TOP2A]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 541 |
| [[CCNB1]] | +0.85 | +0.82 / +0.85 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 780 |
| [[CCNB2]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 752 |
| [[INCENP]] | +0.84 | +0.80 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 513 |
| [[TPX2]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 723 |
| [[CEP55]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CKAP5's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without PIMREG | 0.038 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises CKAP5's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without NEURL1B | 0.099 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[FAM72D]] | C | FAM72D activity raises CKAP5's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[PBK]] | C | PBK activity raises CKAP5's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without PBK | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CKAP5's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 1.96× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises CKAP5's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.1, -55.4); signed map (-49.2, -42.9). **Vector** length 156, 59.1% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.69 to 60); *DREAM G2/M down* (control, mean cos +0.78 to 28); *E2F targets* (hallmark, mean cos +0.66 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.8 | +7.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.1 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +4.4 | +12.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.7 | +4.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -14.2 | -14.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.5 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.9 | -6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.9 | -5.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | -4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.3 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.9 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -3.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cytoskeleton associated protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:46,743,048-46,846,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ch-TOG, KIAA0097, TOG, TOGp |
| Gene groups (HGNC) | TOG domain containing; MicroRNA protein coding host genes; Small nucleolar RNA protein coding host genes |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 30 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14008](https://www.uniprot.org/uniprotkb/Q14008) (Cytoskeleton-associated protein 5):

> Binds to the plus end of microtubules and regulates microtubule dynamics and microtubule organization. Acts as a processive microtubule polymerase. Promotes cytoplasmic microtubule nucleation and elongation. Plays a major role in organizing spindle poles. In spindle formation protects kinetochore microtubules from depolymerization by KIF2C and has an essential role in centrosomal microtubule assembly independently of KIF2C activity. Contributes to centrosome integrity. Acts as a component of …

**Summary**, from NCBI Gene [9793](https://www.ncbi.nlm.nih.gov/gene/9793):

> This gene encodes a cytoskeleton-associated protein which belongs to the TOG/XMAP215 family. The N-terminal half of this protein contains a microtubule-binding domain and the C-terminal half contains a KXGS motif for binding tubulin dimers. This protein has two distinct roles in spindle formation; it protects kinetochore microtubules from depolymerization and plays an essential role in centrosomal microtubule assembly. This protein may be necessary for the proper interaction of microtubules …

**Accessions** — [HGNC:28959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28959) · Entrez [9793](https://www.ncbi.nlm.nih.gov/gene/9793) · UniProt [Q14008](https://www.uniprot.org/uniprotkb/Q14008) · Ensembl [ENSG00000175216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175216)

## Data

Gene col 10583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10583); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10583]; `tensor/DDL_lfc|DDL_z.npy` [10583]; `embed/gene_vectors.npy` [10583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10583 or target_col == 10583). Every well: [[CKAP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKAP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
