---
symbol: "CTDSPL2"
type: "gene"
col: 6063
ensembl_id: "ENSG00000137770"
name: "CTD small phosphatase like 2"
location: "15q15.3-q21.1"
module: 67
arm: "+"
pooled_cpm: 152.81
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CTDSPL2

*CTD small phosphatase like 2* — 15q15.3-q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.82× (z +18.3, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.715× (z -10.6, q 1e-23, down in 36 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIS18BP1]] (+0.71, fdr 7e-06), [[RAD54B]] (+0.70, fdr 7e-06), [[TTK]] (+0.69, fdr 7e-06); moves opposite to [[MIR22HG]] (-0.61, fdr 1e-05), [[ZNF783]] (-0.57, fdr 2e-05, ⚠ ZNF783 in the vector space only through flagged drug-doses), [[EIF3J]] (-0.56, fdr 2e-05, ⚠ same locus), [[FAM83G]] (-0.55, fdr 1e-05), [[LINC00520]] (-0.55, fdr 2e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KDM2B-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.82×** | +18.3 | 0e+00 | 48/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +14.0 | 4e-42 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +13.0 | 2e-36 | 44/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +11.6 | 5e-29 | 43/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +9.6 | 7e-20 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +9.2 | 5e-18 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +6.1 | 6e-08 | 30/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.19× | +5.4 | 4e-06 | 24/48 (A549, BT-474, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +4.7 | 1e-04 | 27/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.013 | 15/48 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.017 | 3/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.032 | 19/48 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.2 | 0.049 | 15/49 (C-33 A, HEC-1-A, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.049 | 16/48 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.16× | +3.2 | 0.049 | 13/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -10.6 | 1e-23 | 36/49 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -8.7 | 6e-16 | 32/44 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.716×** | -7.5 | 1e-11 | 34/48 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.721×** | -7.3 | 3e-11 | 34/49 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.773×** | -5.4 | 9e-06 | 26/45 (C-33 A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.861× | -4.8 | 2e-04 | 19/48 (A-427, A-172, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.885× | -3.9 | 0.007 | 18/48 (SW1417, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | 0.836× | -3.9 | 0.007 | 23/47 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.844× | -3.8 | 0.008 | 20/48 (HepG2/C3A, RKO, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.841× | -3.8 | 0.009 | 20/48 (NCI-H1573, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.5 | 0.020 | 16/48 (J82, SW480, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.902× | -3.3 | 0.039 | 6/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.864× | -3.3 | 0.039 | 12/49 (PANC-1, NCI-H2030, …) | all doses, flat |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.067 | 9/48 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.871× | -3.1 | 0.067 | 13/48 (HOP62, CHP-212, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.874× | -3.0 | 0.081 | 18/47 (NCI-H460, LoVo, …) | two highest doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 0.876× | -3.0 | 0.082 | 14/48 (A-172, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.912× | -3.0 | 0.084 | 7/48 (SNU-1, A498, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.878× | -2.9 | 0.094 | 6/48 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.781×** | -2.9 | 0.097 | 15/48 (SW 1271, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 197 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +18.5) | — |
| [[SW480 (line)]] | alt | 156 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +17.8) | — |
| [[CFPAC-1 (line)]] | alt | 187 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.16× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.430× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -10.3) |
| [[LoVo (line)]] | wt | 142 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.29× (z +18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +17.7) | — |
| [[NCI-H460 (line)]] | wt | 140 | 5 (3 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.04× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 191 | 2 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.87× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -18.6) |
| [[NCI-H23 (line)]] | alt | 149 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.65× (z +12.7) | — |
| [[KATO III (line)]] | alt | 164 | 4 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.87× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -9.8) |
| [[LS 180 (line)]] | wt | 118 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 180 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.82× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -13.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 245 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -15.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 178 | 2 | 2 | [[PH-797804 (drug)]] 5 µM 4.98× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -11.9) |
| [[HCT15 (line)]] | alt | 246 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.21× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -12.4) |
| [[HOP62 (line)]] | alt | 158 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 207 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.8) |
| [[A-172 (line)]] | wt | 116 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +10.0) | [[Selinexor (drug)]] 5 µM 0.633× (z -8.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 134 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.32× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.608× (z -9.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[BT-474 (line)]] | alt | 124 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.7) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.89× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 208 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.76× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 145 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -12.1) |
| [[SW1417 (line)]] | alt | 157 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.82× (z +11.8) | — |
| [[A498 (line)]] | wt | 122 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.2) ⚠ cell-cycle shift, explains ~75% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -12.8) |
| [[A549 (line)]] | wt | 105 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.2) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.85× (z +10.9) | — |
| [[H4 (line)]] | wt | 140 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.53× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 163 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.61× (z +12.0) | — |
| [[J82 (line)]] | alt | 189 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 171 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.33× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 143 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.13× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.477× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 151 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.99× (z +10.3) | — |
| [[RKO (line)]] | wt | 162 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.6) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.93× (z +11.2) | — |
| [[SW48 (line)]] | wt | 153 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.87× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[COLO 205 (line)]] | alt | 173 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.97× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.314× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[HS-578T (line)]] | alt | 104 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.64× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 142 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.94× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 185 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.22× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 159 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.35× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 109 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS18BP1]] | +0.71 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[RAD54B]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TTK]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TICRR]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SLC25A40]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[BARD1]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PBK]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[GMNN]] | +0.67 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[CCDC34]] | +0.67 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SASS6]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[MTF2]] | +0.67 | +0.75 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR22HG]] | -0.61 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | -0.57 | -0.63 / -0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF3J]] | -0.56 | -0.67 / -0.46 | both halves | 2e-05 | ⚠ same locus (8.1 kb, same strand: neighbours can correlate without regulation) |
| [[FAM83G]] | -0.55 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[LINC00520]] | -0.55 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[MICALL1]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDM2B-DT]] | B | KDM2B-DT activity raises CTDSPL2's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.18× lower at baseline in the lines without KDM2B-DT | 0.041 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.0, -50.6); signed map (-44.6, -36.8). **Vector** length 109, 37.6% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.58 to 12); *G2/M checkpoint* (hallmark, mean cos +0.59 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +18.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +11.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.1 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.4 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.4 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | CTD small phosphatase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3-q21.1 — chr15:44,427,622-44,529,038 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC129, FLJ10523 |
| Gene groups (HGNC) | CTD family phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05D32](https://www.uniprot.org/uniprotkb/Q05D32) (CTD small phosphatase-like protein 2):

> Serine/threonine phosphatase that promotes gluconeogenesis by dephosphorylating FOXO1 and FOXO3A, promoting their nuclear retention and enhancing their transcriptional activity on PCK1 and G6PC1, key enzymes in hepatic gluconeogenesis. Essential for proper embryonic skeletal development by regulating chondrocyte survival through dephosphorylation of FOXO3 (By similarity). By maintaining FOXO3 in its active, dephosphorylated form, inhibits excessive apoptosis of chondrocytes, which is essential …

**Summary**, from NCBI Gene [51496](https://www.ncbi.nlm.nih.gov/gene/51496):

> Enables RNA polymerase II CTD heptapeptide repeat phosphatase activity. Involved in positive regulation of gluconeogenesis. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26936) · Entrez [51496](https://www.ncbi.nlm.nih.gov/gene/51496) · UniProt [Q05D32](https://www.uniprot.org/uniprotkb/Q05D32) · Ensembl [ENSG00000137770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137770)

## Data

Gene col 6063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6063); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6063]; `tensor/DDL_lfc|DDL_z.npy` [6063]; `embed/gene_vectors.npy` [6063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6063 or target_col == 6063). Every well: [[CTDSPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTDSPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
