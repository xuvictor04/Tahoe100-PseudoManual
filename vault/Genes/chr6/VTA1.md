---
symbol: "VTA1"
type: "gene"
col: 193
ensembl_id: "ENSG00000009844"
name: "vesicle trafficking 1"
location: "6q24.1-q24.2"
module: 17
arm: "+"
pooled_cpm: 90.96
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# VTA1

*vesicle trafficking 1* — 6q24.1-q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.26× (z +30.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.636× (z -23.6, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM161B]] (+0.73, fdr 7e-06), [[NDUFA8]] (+0.72, fdr 7e-06), [[SMIM8]] (+0.71, fdr 1e-05); moves opposite to [[PSMD6-AS2]] (-0.59, fdr 2e-05), [[LARP1B]] (-0.57, fdr 2e-05), [[GALNT7-DT]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RFC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +30.2 | 0e+00 | 48/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.64×** | +29.7 | 0e+00 | 48/49 (PANC-1, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +28.5 | 0e+00 | 48/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +26.6 | 0e+00 | 48/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.96×** | +21.0 | 0e+00 | 41/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +16.8 | 0e+00 | 36/48 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +11.3 | 8e-28 | 37/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +9.7 | 1e-20 | 29/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +8.1 | 3e-14 | 27/48 (LOX-IMVI, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +7.7 | 9e-13 | 30/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +7.4 | 6e-12 | 26/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +6.3 | 2e-08 | 24/49 (PANC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.9 | 2e-07 | 26/45 (RKO, A549, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +5.8 | 2e-07 | 22/48 (C32, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.3 | 4e-06 | 14/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +5.2 | 6e-06 | 16/47 (LoVo, A-427, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +5.0 | 2e-05 | 11/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-05 | 20/47 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -23.6 | 0e+00 | 42/49 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -9.8 | 4e-20 | 31/48 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -7.6 | 6e-12 | 27/50 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.865× | -5.3 | 1e-05 | 20/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -4.7 | 3e-04 | 14/48 (C-33 A, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.890× | -4.3 | 0.002 | 19/48 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.894× | -4.1 | 0.004 | 17/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.898× | -3.8 | 0.010 | 19/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.936× | -3.4 | 0.034 | 4/49 (A-427, NCI-H1792, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 0.911× | -3.4 | 0.034 | 3/49 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.912× | -3.4 | 0.038 | 20/49 (HEC-1-A, KATO III, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.909× | -3.4 | 0.038 | 12/47 (A-172, C-33 A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.911× | -3.3 | 0.044 | 6/47 (NCI-H23, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 141 | 5 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.77× (z +19.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 89.1 | 5 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.83× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -11.0) |
| [[HOP62 (line)]] | alt | 70.5 | 5 | 2 | [[TAK-901 (drug)]] 5 µM 6.75× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -10.5) |
| [[LoVo (line)]] | wt | 71.1 | 6 | 1 | [[TAK-901 (drug)]] 5 µM 12.1× (z +19.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 100 | 5 | 2 | [[TAK-901 (drug)]] 5 µM 11.3× (z +18.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -12.2) |
| [[SNU-423 (line)]] | alt | 125 | 5 | 2 | [[Panobinostat (drug)]] 5 µM 2.21× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -15.9) |
| [[A-172 (line)]] | wt | 76.5 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 2.33× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -8.6) |
| [[A549 (line)]] | wt | 62.5 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 3.16× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -12.8) |
| [[C-33 A (line)]] | alt | 248 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.20× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -22.1) |
| [[hTERT-HPNE (line)]] | wt | 81.6 | 4 | 2 | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.1) |
| [[KATO III (line)]] | alt | 114 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.24× (z +14.3) | [[Digitoxin (drug)]] 5 µM 0.397× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 106 | 5 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.49× (z +15.8) | [[Digitoxin (drug)]] 5 µM 0.513× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 105 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 3.11× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -9.6) |
| [[PANC-1 (line)]] | alt | 117 | 5 | 1 | [[TAK-901 (drug)]] 5 µM 6.92× (z +21.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -20.4) |
| [[A498 (line)]] | wt | 63.4 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.13× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -11.7) |
| [[Hs 766T (line)]] | wt | 73.5 | 5 | 0 | [[Selinexor (drug)]] 5 µM 1.90× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 86.5 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.65× (z +14.4) | — |
| [[HT-29 (line)]] | alt | 74.2 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 5.28× (z +11.0) | — |
| [[J82 (line)]] | alt | 95.9 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.67× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 104 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.28× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 67.1 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 6.75× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 99.3 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.47× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 68.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +16.9) | — |
| [[SHP-77 (line)]] | alt | 134 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.12× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 111 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 4.34× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 94.2 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 3.64× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.8) |
| [[SW48 (line)]] | wt | 89.1 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.09× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 65.5 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.21× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -15.3) |
| [[RKO (line)]] | wt | 102 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 8.42× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.3) |
| [[SNU-1 (line)]] | wt | 72.7 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.61× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.1) |
| [[SW 900 (line)]] | alt | 52.8 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.71× (z +9.5) | — |
| [[A-427 (line)]] | wt | 164 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.518× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.646× (z -9.4) |
| [[BT-474 (line)]] | alt | 55.1 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -8.7) |
| [[C32 (line)]] | wt | 73.0 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.60× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 59.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.64× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.510× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 65.9 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.23× (z +9.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 93.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 61.1 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.06× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 81.6 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.59× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -10.5) |
| [[CHP-212 (line)]] | wt | 94.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -11.1) |
| [[COLO 205 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 102 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.74× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 45.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 99.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.64× (z +9.5) | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.189× (z -9.2) |
| [[AN3 CA (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM161B]] | +0.73 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[NDUFA8]] | +0.72 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[SMIM8]] | +0.71 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MNAT1]] | +0.68 | +0.49 / +0.71 | both halves | 1e-05 | pathway: HIV Infection |
| [[CSTPP1]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[NDUFA12]] | +0.67 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ZNF420]] | +0.67 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[POLR3A]] | +0.66 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[HARS2]] | +0.66 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[COG2]] | +0.66 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ALKBH8]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[CINP]] | +0.66 | +0.61 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS2]] | -0.59 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[LARP1B]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[GALNT7-DT]] | -0.57 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[KMT2E-AS1]] | -0.56 | -0.54 / -0.20 | both halves | 7e-04 |  |
| [[HIVEP1]] | -0.54 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[LSMEM1]] | -0.54 | -0.54 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[DNMT3A]] | -0.54 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[DLEU2]] | -0.54 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[DNAI4]] | -0.54 | -0.42 / -0.24 | both halves | 4e-04 |  |
| [[INTS6-AS1]] | -0.54 | -0.38 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VTA1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFC1]] | C | VTA1's natural level weakens RFC1's drug response | VTA1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.51; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.1, -5.3); signed map (-19.4, -18.1). **Vector** length 124, 34.9% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +12.0 | +29.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +9.8 | +16.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +9.7 | +21.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.4 | +28.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.6 | +30.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +5.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.0 | -23.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -10.1 | -9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.7 | -5.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +0.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | vesicle trafficking 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.1-q24.2 — chr6:142,147,162-142,224,685 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC228, My012; previously C6orf55 |
| Gene groups (HGNC) | ESCRT-IV |
| Reactome | 8 pathways, smallest: Budding and maturation of HIV virion; Endosomal Sorting Complex Required For Transport (ESCRT); Late Phase of HIV Life Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP79](https://www.uniprot.org/uniprotkb/Q9NP79) (Vacuolar protein sorting-associated protein VTA1 homolog):

> Involved in the endosomal multivesicular bodies (MVB) pathway. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal enzymes and lipids. Thought to be a cofactor of VPS4A/B, which catalyzes disassembles membrane-associated ESCRT-III assemblies. Involved in the sorting and …

**Summary**, from NCBI Gene [51534](https://www.ncbi.nlm.nih.gov/gene/51534):

> C6ORF55 encodes a protein involved in trafficking of the multivesicular body, an endosomal compartment involved in sorting membrane proteins for degradation in lysosomes (Ward et al., 2005 [PubMed 15644320]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20954) · Entrez [51534](https://www.ncbi.nlm.nih.gov/gene/51534) · UniProt [Q9NP79](https://www.uniprot.org/uniprotkb/Q9NP79) · Ensembl [ENSG00000009844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009844)

## Data

Gene col 193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 193); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 193]; `tensor/DDL_lfc|DDL_z.npy` [193]; `embed/gene_vectors.npy` [193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 193 or target_col == 193). Every well: [[VTA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VTA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
