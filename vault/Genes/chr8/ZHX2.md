---
symbol: "ZHX2"
type: "gene"
col: 10958
ensembl_id: "ENSG00000178764"
name: "zinc fingers and homeoboxes 2"
location: "8q24.13"
module: 80
arm: "+"
pooled_cpm: 97.21
n_lines_expressing: 43
n_dd_up: 21
n_dd_down: 23
n_dd_up_clean: 16
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 23
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# ZHX2

*zinc fingers and homeoboxes 2* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.36× (z +21.5, q 0e+00, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.135× (z -35.5, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMADHC-DT]] (+0.73, fdr 6e-05), [[LINC00571]] (+0.72, fdr 1e-05), [[ZNF341-AS1]] (+0.72, fdr 2e-05); moves opposite to [[ARL6]] (-0.70, fdr 1e-05), [[WASF3]] (-0.69, fdr 1e-05), [[SDHAF3]] (-0.68, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RBPMS]] → it (grade B ⚠); 23 go from it, the strongest it → [[ZNF569]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +21.5 | 0e+00 | 35/41 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +18.5 | 0e+00 | 36/42 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +9.3 | 2e-18 | 27/41 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.9 | 5e-13 | 26/40 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +6.2 | 6e-08 | 22/41 (HT-29, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +5.3 | 1e-05 | 24/41 (HT-29, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.33×** | +5.0 | 5e-05 | 23/41 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +4.5 | 5e-04 | 26/41 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.3 | 9e-04 | 17/41 (HOP62, SW1417, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.005 | 21/41 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.005 | 19/42 (HEC-1-A, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +3.9 | 0.005 | 19/41 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.16× | +3.8 | 0.007 | 16/41 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.007 | 19/43 (J82, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.007 | 17/41 (NCI-H460, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.007 | 20/40 (HS-578T, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.016 | 18/41 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.135×** | -35.5 | 0e+00 | 40/41 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.147×** | -34.0 | 0e+00 | 40/41 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.166×** | -31.8 | 0e+00 | 41/41 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.461×** | -13.7 | 1e-40 | 37/41 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.477×** | -13.1 | 3e-37 | 33/41 (SNU-423, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.468×** | -12.4 | 1e-33 | 27/38 (HepG2/C3A, HEC-1-A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.538×** | -10.6 | 4e-24 | 25/35 (SNU-423, A498, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.568×** | -10.0 | 8e-22 | 35/41 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.360×** | -9.5 | 2e-19 | 34/42 (AsPC-1, HepG2/C3A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.700×** | -9.0 | 2e-17 | 27/41 (HepG2/C3A, SW1417, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.423×** | -8.0 | 8e-14 | 36/41 (HepG2/C3A, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.713×** | -6.0 | 1e-07 | 28/42 (HT-29, SNU-423, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.832×** | -4.6 | 2e-04 | 20/41 (SW1417, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.774×** | -4.6 | 2e-04 | 23/40 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.624×** | -4.4 | 5e-04 | 17/32 (BT-474, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.781×** | -4.2 | 9e-04 | 23/41 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.795×** | -4.1 | 0.002 | 21/41 (J82, SNU-423, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.650×** | -4.0 | 0.002 | 18/41 (HEC-1-A, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.858× | -3.8 | 0.003 | 13/41 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.799×** | -3.8 | 0.003 | 18/41 (RPMI-7951, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 278 | 0 | 15 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0436× (z -30.1) |
| [[SNU-423 (line)]] | alt | 316 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0289× (z -31.5) |
| [[HEC-1-A (line)]] | alt | 177 | 2 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.0902× (z -33.9) |
| [[HT-29 (line)]] | alt | 125 | 6 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +19.2) | [[Panobinostat (drug)]] 0.5 µM 0.0973× (z -23.0) |
| [[LS 180 (line)]] | wt | 120 | 2 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.0976× (z -24.4) |
| [[NCI-H460 (line)]] | wt | 38.9 | 7 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 6.82× (z +26.6) | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -15.6) |
| [[SW 900 (line)]] | alt | 123 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +16.9) | [[Panobinostat (drug)]] 5 µM 0.136× (z -19.6) |
| [[A-172 (line)]] | wt | 51.2 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +21.7) | [[Panobinostat (drug)]] 5 µM 0.107× (z -19.2) |
| [[HOP62 (line)]] | alt | 60.3 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +24.7) | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -15.0) |
| [[SW480 (line)]] | alt | 51.4 | 3 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.125× (z -26.0) |
| [[A498 (line)]] | wt | 188 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -25.0) |
| [[AsPC-1 (line)]] | alt | 219 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.0684× (z -32.6) |
| [[CFPAC-1 (line)]] | alt | 122 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.134× (z -21.7) |
| [[J82 (line)]] | alt | 181 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +24.1) | [[Panobinostat (drug)]] 0.5 µM 0.0879× (z -24.9) |
| [[LoVo (line)]] | wt | 92.9 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +18.3) | [[Panobinostat (drug)]] 5 µM 0.123× (z -25.4) |
| [[NCI-H1792 (line)]] | alt | 111 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.0961× (z -24.0) |
| [[BT-474 (line)]] | alt | 341 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +19.9) | [[Panobinostat (drug)]] 0.5 µM 0.0826× (z -30.7) |
| [[NCI-H1573 (line)]] | alt | 103 | 2 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.164× (z -18.7) |
| [[SW1417 (line)]] | alt | 170 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.119× (z -23.7) |
| [[hTERT-HPNE (line)]] | wt | 59.7 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 34.5 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.110× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 123 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.228× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 151 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.108× (z -22.5) |
| [[SK-MEL-2 (line)]] | alt | 46.0 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -17.9) |
| [[SW48 (line)]] | wt | 251 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0822× (z -20.5) |
| [[COLO 205 (line)]] | alt | 246 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.102× (z -21.2) |
| [[HCT15 (line)]] | alt | 119 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.155× (z -17.0) |
| [[Hs 766T (line)]] | wt | 37.4 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +23.7) | [[Panobinostat (drug)]] 5 µM 0.187× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 176 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0695× (z -18.1) |
| [[C32 (line)]] | wt | 54.2 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +12.1) | [[Belinostat (drug)]] 5 µM 0.274× (z -9.2) |
| [[H4 (line)]] | wt | 30.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +14.7) | [[Belinostat (drug)]] 5 µM 0.141× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 36.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -11.3) |
| [[A549 (line)]] | wt | 41.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.137× (z -15.1) |
| [[AN3 CA (line)]] | alt | 45.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.0599× (z -12.4) |
| [[HS-578T (line)]] | alt | 54.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 32.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.239× (z -11.0) |
| [[NCI-H596 (line)]] | alt | 96.6 | 0 | 2 (1 ⚠) | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.113× (z -20.6) |
| [[CHP-212 (line)]] | wt | 46.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 85.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -9.4) |
| [[RKO (line)]] | wt | 50.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +12.0) | — |
| [[A-427 (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | +0.73 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[LINC00571]] | +0.72 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.72 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[KMO]] | +0.69 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[PPP1R12A-AS2]] | +0.69 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[C1orf54]] | +0.69 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TTC6]] | +0.67 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.67 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PATL2]] | +0.67 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[GGPS1]] | +0.66 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[ARHGAP15]] | +0.66 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[NEK8]] | +0.66 | +0.54 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | -0.70 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[WASF3]] | -0.69 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.68 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[HACE1]] | -0.67 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SPATA6]] | -0.67 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[FAM234B]] | -0.67 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[NBPF3]] | -0.65 | -0.54 / -0.49 | both halves | 2e-05 |  |
| [[METAP1]] | -0.65 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.64 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.64 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ELP1]] | -0.63 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ATG4C]] | -0.63 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBPMS]] | B | RBPMS activity raises ZHX2's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 3.51× lower at baseline in the lines without RBPMS | 0.013 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[KMO]] | B | KMO activity raises ZHX2's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.14× lower at baseline in the lines without KMO | 0.037 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[LRRN1]] | B | LRRN1 activity raises ZHX2's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without LRRN1 | 0.053 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises ZHX2's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.93× lower at baseline in the lines without CTSS | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[LINC02889]] | B | LINC02889 activity raises ZHX2's level | lines that do not express LINC02889 (12) vs lines expressing it (38) | 1.78× lower at baseline in the lines without LINC02889 | 0.069 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, SAMD5, ENSG00000226640; maybe low, not absent |
| [[ZNF341-AS1]] | C | ZNF341-AS1 activity raises ZHX2's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 4.29× lower at baseline in the lines without ZNF341-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent; co-absent with the target |
| [[LINC00571]] | C | LINC00571 activity raises ZHX2's level | lines that do not express LINC00571 (5) vs lines expressing it (45) | 3.87× lower at baseline in the lines without LINC00571 | 0.073 | ⚠ within organs, on part of the lines; also absent: KIFC3, NDRG1, DELEC1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 21, C 2. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF569]] | B | ZHX2 activity lowers ZNF569's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 2.08× higher at baseline in the lines without ZHX2 | 0.031 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[SERPINB9P1]] | B | ZHX2 activity raises SERPINB9P1's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without ZHX2 | 0.047 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[BCL10-AS1]] | B | ZHX2 activity raises BCL10-AS1's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without ZHX2 | 0.055 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[ZFAND4]] | B | ZHX2 activity lowers ZFAND4's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.81× higher at baseline in the lines without ZHX2 | 0.056 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[PHF6]] | B | ZHX2 activity lowers PHF6's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.57× higher at baseline in the lines without ZHX2 | 0.057 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[SPATA6]] | B | ZHX2 activity lowers SPATA6's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 2.33× higher at baseline in the lines without ZHX2 | 0.074 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[HACE1]] | B | ZHX2 activity strengthens HACE1's drug response | lines that do not express ZHX2 (7) vs lines expressing it (39) | the lines without ZHX2 respond 0.74× as strongly (z diff +0.84); strongest at Ouabain (Octahydrate) 5 µM: 0.79x vs 0.43x (z diff +4.5) | 0.075 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1; target measured in part of the lines; artifact flags |
| [[LRFN3]] | B | ZHX2 activity lowers LRFN3's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.52× higher at baseline in the lines without ZHX2 | 0.077 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[ATG4C]] | B | ZHX2 activity lowers ATG4C's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.49× higher at baseline in the lines without ZHX2 | 0.077 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[ABCA10]] | B | ZHX2 activity raises ABCA10's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without ZHX2 | 0.080 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[CTSS]] | B | ZHX2 activity raises CTSS's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 2.66× lower at baseline in the lines without ZHX2 | 0.081 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| cells under [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM | B | ZHX2 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ZHX2 (7) vs lines expressing it (41) | the lines without ZHX2: 1.22× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.9, 10.1); signed map (22.5, -6.4). **Vector** length 129, 40.3% of its response variance represented; |z| ≥ 3 in 1,516 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.3 | +18.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.5 | +21.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.4 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.2 | -31.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.5 | -13.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.2 | -10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.6 | -35.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.4 | -9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -9.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc fingers and homeoboxes 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:122,781,655-122,974,510 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0854 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6X8](https://www.uniprot.org/uniprotkb/Q9Y6X8) (Zinc fingers and homeoboxes protein 2):

> Acts as a transcriptional repressor. Represses the promoter activity of the CDC25C gene stimulated by NFYA. May play a role in retinal development where it regulates the composition of bipolar cell populations, by promoting differentiation of bipolar OFF-type cells (By similarity). In the brain, may promote maintenance and suppress differentiation of neural progenitor cells in the developing cortex (By similarity).

**Summary**, from NCBI Gene [22882](https://www.ncbi.nlm.nih.gov/gene/22882):

> The members of the zinc fingers and homeoboxes gene family are nuclear homodimeric transcriptional repressors that interact with the A subunit of nuclear factor-Y (NF-YA) and contain two C2H2-type zinc fingers and five homeobox DNA-binding domains. This gene encodes member 2 of this gene family. In addition to forming homodimers, this protein heterodimerizes with member 1 of the zinc fingers and homeoboxes family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18513) · Entrez [22882](https://www.ncbi.nlm.nih.gov/gene/22882) · UniProt [Q9Y6X8](https://www.uniprot.org/uniprotkb/Q9Y6X8) · Ensembl [ENSG00000178764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178764)

## Data

Gene col 10958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10958); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10958]; `tensor/DDL_lfc|DDL_z.npy` [10958]; `embed/gene_vectors.npy` [10958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10958 or target_col == 10958). Every well: [[ZHX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZHX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
