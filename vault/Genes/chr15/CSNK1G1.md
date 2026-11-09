---
symbol: "CSNK1G1"
type: "gene"
col: 9755
ensembl_id: "ENSG00000169118"
name: "casein kinase 1 gamma 1"
location: "15q22.31"
module: 118
arm: "+"
pooled_cpm: 165.4
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# CSNK1G1

*casein kinase 1 gamma 1* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +18.2, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.429× (z -25.5, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.683× (z -16.2, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UROD]] (+0.63, fdr 2e-04), [[FAM185A]] (+0.60, fdr 5e-05), [[SYNRG]] (+0.60, fdr 3e-05); moves opposite to [[R3HDM4]] (-0.52, fdr 1e-04), [[ATP1A3]] (-0.50, fdr 5e-04), [[CSRP1]] (-0.50, fdr 9e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +18.2 | 0e+00 | 41/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.08×** | +16.8 | 0e+00 | 45/49 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +14.8 | 0e+00 | 34/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +13.2 | 8e-38 | 36/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +12.7 | 6e-35 | 40/50 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +11.2 | 5e-27 | 40/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +11.1 | 6e-27 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +9.7 | 2e-20 | 27/48 (SW1417, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +8.3 | 9e-15 | 36/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +7.5 | 4e-12 | 32/49 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +6.3 | 1e-08 | 25/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +6.1 | 6e-08 | 26/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.19× | +5.3 | 4e-06 | 22/48 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.8 | 5e-05 | 24/38 (A549, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.16× | +4.4 | 4e-04 | 19/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.8 | 0.005 | 15/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.050 | 11/48 (HOP62, CHP-212, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.11× | +3.0 | 0.076 | 11/49 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.10× | +3.0 | 0.077 | 14/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.10× | +2.9 | 0.082 | 14/48 (NCI-H460, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.429×** | -25.5 | 0e+00 | 47/49 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -25.2 | 0e+00 | 42/44 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.683×** | -16.2 | 0e+00 | 44/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.676×** | -11.8 | 7e-30 | 44/49 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.735×** | -8.6 | 1e-15 | 26/45 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.757×** | -8.4 | 5e-15 | 32/48 (AsPC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.775×** | -7.7 | 1e-12 | 28/48 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.816×** | -6.1 | 6e-08 | 25/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -4.0 | 0.005 | 0/50 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.883× | -3.8 | 0.010 | 18/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.889× | -3.5 | 0.021 | 10/49 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.931× | -3.1 | 0.100 | 1/49 (NCI-H661) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 138 | 14 (7 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.506× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 145 | 10 (6 ⚠) | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.664× (z -9.8) |
| [[SW480 (line)]] | alt | 174 | 9 (2 ⚠) | 4 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.594× (z -11.0) |
| [[LS 180 (line)]] | wt | 144 | 6 (1 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -17.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 229 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.574× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 186 | 5 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.67× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.641× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 190 | 5 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -21.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 237 | 5 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -17.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 258 | 5 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.78× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -15.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 171 | 5 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -15.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 154 | 3 (1 ⚠) | 4 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.593× (z -12.6) |
| [[J82 (line)]] | alt | 151 | 2 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.626× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 162 | 5 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.44× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -28.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 203 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.77× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.567× (z -9.7) |
| [[HT-29 (line)]] | alt | 163 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -10.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 164 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.68× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -19.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 146 | 3 | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 160 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.71× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 163 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.479× (z -17.2) |
| [[RPMI-7951 (line)]] | alt | 241 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.36× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.509× (z -14.6) |
| [[SW1417 (line)]] | alt | 155 | 2 (1 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.52× (z +9.6) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.08× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.618× (z -11.0) |
| [[A498 (line)]] | wt | 193 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -16.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 209 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 6.05× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 104 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.6) | [[Docetaxel (drug)]] 0.05 µM 0.521× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 110 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.618× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 157 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.637× (z -11.7) |
| [[SW48 (line)]] | wt | 177 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.89× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -14.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 131 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.10× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 170 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -13.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 118 | 0 | 3 (2 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.503× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 184 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.15× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 224 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -17.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 142 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -14.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 168 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.87× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -24.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 137 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 113 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.12× (z +11.0) | — |
| [[CHP-212 (line)]] | wt | 238 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -11.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 219 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -13.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.508× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 144 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 210 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 179 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 196 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UROD]] | +0.63 | +0.29 / +0.64 | both halves | 2e-04 |  |
| [[FAM185A]] | +0.60 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[SYNRG]] | +0.60 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[RABL2A]] | +0.60 | +0.29 / +0.62 | both halves | 2e-04 |  |
| [[FRS2]] | +0.57 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[ATP6V1H]] | +0.56 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[PRPF18]] | +0.56 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[DNAJC30]] | +0.54 | +0.23 / +0.51 | both halves | 5e-04 |  |
| [[MFSD5]] | +0.54 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[ATP5PF]] | +0.54 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[NADSYN1]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[RABL2B]] | +0.53 | +0.23 / +0.57 | both halves | 5e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM4]] | -0.52 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[ATP1A3]] | -0.50 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[CSRP1]] | -0.50 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[SNPH]] | -0.49 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[TMEM170B]] | -0.49 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[RPAP3]] | -0.48 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[CCDC112]] | -0.48 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[NCOR2]] | -0.47 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[CDCA7L]] | -0.47 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[RNF157]] | -0.47 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[TNKS1BP1]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[MPDZ]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSNK1G1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CSNK1G1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MOCS1]] | B | MOCS1 activity raises CSNK1G1's level | lines that do not express MOCS1 (13) vs lines expressing it (36) | 1.11× lower at baseline in the lines without MOCS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SNRPN, MYH10, ANKRD6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-5.3, 25.3); signed map (-1.9, -3.6). **Vector** length 133, 44.3% of its response variance represented; |z| ≥ 3 in 1,428 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +12.7 | +18.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +12.5 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +11.6 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.6 | +14.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +12.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +11.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.2 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +3.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.6 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -13.3 | -16.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.7 | -11.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.9 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.1 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.1 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 1 gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,165,525-64,356,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CK1gamma1 |
| Gene groups (HGNC) | Casein kinase 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCP0](https://www.uniprot.org/uniprotkb/Q9HCP0) (Casein kinase I isoform gamma-1):

> Serine/threonine-protein kinase. Casein kinases are operationally defined by their preferential utilization of acidic proteins such as caseins as substrates. It can phosphorylate a large number of proteins. Participates in Wnt signaling. Regulates fast synaptic transmission mediated by glutamate (By similarity). Phosphorylates CLSPN.

**Summary**, from NCBI Gene [53944](https://www.ncbi.nlm.nih.gov/gene/53944):

> This gene encodes a member of the casein kinase I gene family. This family is comprised of serine/threonine kinases that phosphorylate acidic proteins such as caseins. The encoded kinase plays a role in cell cycle checkpoint arrest in response to stalled replication forks by phosphorylating Claspin. A mutation in this gene may be associated with non-syndromic early-onset epilepsy (NSEOE). [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:2454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2454) · Entrez [53944](https://www.ncbi.nlm.nih.gov/gene/53944) · UniProt [Q9HCP0](https://www.uniprot.org/uniprotkb/Q9HCP0) · Ensembl [ENSG00000169118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169118)

## Data

Gene col 9755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9755); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9755]; `tensor/DDL_lfc|DDL_z.npy` [9755]; `embed/gene_vectors.npy` [9755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9755 or target_col == 9755). Every well: [[CSNK1G1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK1G1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
