---
symbol: "C1QTNF7-AS1"
type: "gene"
col: 14598
ensembl_id: "ENSG00000249252"
name: "C1QTNF7 antisense RNA 1"
location: "4p15.32"
module: 26
arm: "+"
pooled_cpm: 73.98
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 33
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 13
direction_downstream: 2
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# C1QTNF7-AS1

*C1QTNF7 antisense RNA 1* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 5 µM: 3.16× (z +11.6, q 4e-28, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (18 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.277× (z -24.7, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPTE2]] (+0.67, fdr 7e-06), [[C1QTNF7]] (+0.66, fdr 7e-06, ⚠ same locus), [[FSIP2-AS1]] (+0.64, fdr 2e-05), [[CXCL13]] (+0.64, fdr 1e-05); moves opposite to [[GPC4]] (-0.43, fdr 6e-05), [[LYPD6]] (-0.42, fdr 7e-05), [[PARD6G]] (-0.41, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[LINC01917]] → it (grade B ⚠); 2 go from it, the strongest it → [[TNNI3K]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **3.16×** | +11.6 | 4e-28 | 42/46 (SW480, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +5.9 | 1e-06 | 22/44 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.8 | 1e-06 | 21/45 (A-172, SNU-423, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.4 | 8e-06 | 22/45 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.21×** | +5.3 | 1e-05 | 24/45 (C32, HOP62, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.21×** | +5.3 | 1e-05 | 17/46 (PANC-1, NCI-H460, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.64×** | +5.0 | 5e-05 | 16/45 (A-427, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 8e-05 | 22/44 (LoVo, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 2e-04 | 19/45 (SW480, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.58×** | +4.6 | 2e-04 | 17/46 (BT-474, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.0 | 0.003 | 16/45 (C-33 A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.20×** | +3.6 | 0.017 | 20/45 (C-33 A, SW480, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.027 | 12/45 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.060 | 12/44 (SK-MEL-2, SW48, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.2 | 0.060 | 18/45 (A498, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.060 | 10/46 (LS 180, A498, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.0 | 0.088 | 12/46 (A498, SNU-423, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.17× | +3.0 | 0.093 | 8/44 (HS-578T, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 24 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.277×** | -24.7 | 0e+00 | 45/45 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.419×** | -15.6 | 0e+00 | 37/44 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.599×** | -13.9 | 9e-42 | 28/46 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.584×** | -10.3 | 8e-23 | 32/45 (HCT15, PANC-1, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.569×** | -10.1 | 9e-22 | 31/45 (HEC-1-A, SW 900, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -9.1 | 6e-18 | 32/46 (HEC-1-A, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.631×** | -8.9 | 7e-17 | 27/45 (HCT15, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.642×** | -8.5 | 1e-15 | 32/45 (HCT15, H4, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.644×** | -8.5 | 2e-15 | 30/45 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.655×** | -8.1 | 3e-14 | 34/45 (HCT15, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.759×** | -7.5 | 4e-12 | 30/45 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.665×** | -7.3 | 2e-11 | 29/44 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -7.1 | 5e-11 | 31/45 (NCI-H1792, A-427, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.695×** | -7.0 | 1e-10 | 27/45 (PANC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.533×** | -6.3 | 1e-08 | 24/45 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.802×** | -6.0 | 8e-08 | 29/45 (HEC-1-A, HCT15, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -5.5 | 1e-06 | 22/45 (hTERT-HPNE, HOP62, …) | top dose only | plate-row cell shift |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.762×** | -5.2 | 5e-06 | 19/45 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.832×** | -5.0 | 1e-05 | 21/45 (A-172, HCT15, …) | rises with dose |  |
| [[Irinotecan (drug)]] 5 µM |  | **0.621×** | -4.8 | 4e-05 | 19/47 (HCT15, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.784×** | -4.7 | 6e-05 | 19/45 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.850× | -4.4 | 2e-04 | 18/45 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.681×** | -3.9 | 0.002 | 14/45 (HEC-1-A, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 275 | 0 | 14 (13 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0796× (z -20.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.102× (z -19.5) |
| [[PANC-1 (line)]] | alt | 69.3 | 0 | 14 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -14.6) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.236× (z -13.4) |
| [[SW 900 (line)]] | alt | 279 | 0 | 14 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -18.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.130× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 403 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -25.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.129× (z -20.8) |
| [[HCT15 (line)]] | alt | 199 | 0 | 11 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0527× (z -23.9) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0928× (z -20.7) |
| [[C-33 A (line)]] | alt | 129 | 1 (1 ⚠) | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0674× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0984× (z -18.7) |
| [[hTERT-HPNE (line)]] | wt | 169 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0498× (z -22.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.101× (z -18.1) |
| [[SNU-1 (line)]] | wt | 180 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -21.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.126× (z -16.1) |
| [[A-172 (line)]] | wt | 77.1 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.108× (z -18.7) |
| [[H4 (line)]] | wt | 109 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.204× (z -11.0) |
| [[HOP62 (line)]] | alt | 97.0 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.121× (z -19.4) |
| [[SW 1271 (line)]] | alt | 215 | 0 | 5 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0527× (z -14.7) ⚠ transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0986× (z -11.6) |
| [[C32 (line)]] | wt | 148 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0992× (z -18.1) |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.144× (z -15.4) |
| [[AN3 CA (line)]] | alt | 94.3 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.102× (z -10.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.126× (z -9.8) |
| [[COLO 205 (line)]] | alt | 98.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0636× (z -19.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0933× (z -18.0) |
| [[HS-578T (line)]] | alt | 93.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.135× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 50.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.300× (z -12.1) |
| [[SW480 (line)]] | alt | 27.2 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.274× (z -11.6) |
| [[CHP-212 (line)]] | wt | 81.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0635× (z -11.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.131× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 45.9 | 0 | 2 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.143× (z -11.3) |
| [[LoVo (line)]] | wt | 55.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.249× (z -11.5) |
| [[LS 180 (line)]] | wt | 63.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.179× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 51.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.280× (z -9.5) |
| [[A-427 (line)]] | wt | 22.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0825× (z -8.7) |
| [[A498 (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.42× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 47.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.281× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 26.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.262× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 45.0 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.156× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.242× (z -9.2) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 99.3 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.233× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTE2]] | +0.67 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[C1QTNF7]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[FSIP2-AS1]] | +0.64 | +0.48 / +0.71 | both halves | 2e-05 | same gene group |
| [[CXCL13]] | +0.64 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[LINC01031]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[LVRN]] | +0.59 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[KAZN]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[PRR4]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[LINC02641]] | +0.55 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[LINC01505]] | +0.54 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[MTERF1]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[BAALC-AS1]] | +0.52 | +0.43 / +0.58 | both halves | 3e-05 | same gene group |
| [[LINC01252]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPC4]] | -0.43 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[LYPD6]] | -0.42 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[PARD6G]] | -0.41 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[CRACD]] | -0.40 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[TP73]] | -0.40 | -0.28 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01917]] | B | LINC01917 activity raises C1QTNF7-AS1's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 2.64× lower at baseline in the lines without LINC01917 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[LINC02641]] | B | LINC02641 activity strengthens C1QTNF7-AS1's drug response | lines that do not express LINC02641 (12) vs lines expressing it (34) | the lines without LINC02641 respond 0.50× as strongly (z diff +3.16); strongest at Idarubicin (hydrochloride) 5 µM: 0.99x vs 0.45x (z diff +6.8) | 0.020 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LINC02641]] | B | LINC02641 activity raises C1QTNF7-AS1's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 2.54× lower at baseline in the lines without LINC02641 | 0.031 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises C1QTNF7-AS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02398]] | B | LINC02398 activity raises C1QTNF7-AS1's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without LINC02398 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[KAZN]] | B | KAZN activity raises C1QTNF7-AS1's level | lines that do not express KAZN (5) vs lines expressing it (45) | 2.41× lower at baseline in the lines without KAZN | 0.073 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity raises C1QTNF7-AS1's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01505]] | B | LINC01505 activity raises C1QTNF7-AS1's level | lines that do not express LINC01505 (5) vs lines expressing it (45) | 2.77× lower at baseline in the lines without LINC01505 | 0.086 | ⚠ within organs, on part of the lines; also absent: EID2, CENPP, ENSG00000223727; maybe low, not absent |
| [[ENOX1]] | B | ENOX1 activity raises C1QTNF7-AS1's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without ENOX1 | 0.090 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises C1QTNF7-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.62× lower at baseline in the lines without FSIP2-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[TMEM225B]] | B | TMEM225B activity raises C1QTNF7-AS1's level | lines that do not express TMEM225B (7) vs lines expressing it (43) | 2.45× lower at baseline in the lines without TMEM225B | 0.0997 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[C1QTNF7]] | C | C1QTNF7's natural level strengthens C1QTNF7-AS1's drug response | C1QTNF7's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.77, reverse -0.18; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNNI3K]] | C | C1QTNF7-AS1 activity raises TNNI3K's level | lines that do not express C1QTNF7-AS1 (3) vs lines expressing it (47) | 3.16× lower at baseline in the lines without C1QTNF7-AS1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IMPG2, ENSG00000251379, ENSG00000273184; maybe low, not absent; co-absent with the target; its own permutation p |
| cells under [[Belzutifan (drug)]] 5 µM | C | C1QTNF7-AS1's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | C1QTNF7-AS1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.419 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.344). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.7, 15.8); signed map (23.3, 2.2). **Vector** length 115, 31.2% of its response variance represented; |z| ≥ 3 in 1,340 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.8 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.8 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +0.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +4.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.2 | +11.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +0.0 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +2.7 | +5.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -9.2 | -24.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -15.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.1 | -8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -5.8 | -8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.9 | -13.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -6.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.5 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -5.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.5 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | C1QTNF7 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p15.32 — chr4:15,004,942-15,427,914 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40683) · Entrez [101929095](https://www.ncbi.nlm.nih.gov/gene/101929095) · Ensembl [ENSG00000249252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249252)

## Data

Gene col 14598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14598); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14598]; `tensor/DDL_lfc|DDL_z.npy` [14598]; `embed/gene_vectors.npy` [14598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14598 or target_col == 14598). Every well: [[C1QTNF7-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QTNF7-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
