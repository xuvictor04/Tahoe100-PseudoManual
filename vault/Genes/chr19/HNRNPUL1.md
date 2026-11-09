---
symbol: "HNRNPUL1"
type: "gene"
col: 2581
ensembl_id: "ENSG00000105323"
name: "heterogeneous nuclear ribonucleoprotein U like 1"
location: "19q13.2"
module: 3
arm: "-"
pooled_cpm: 147.25
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPUL1

*heterogeneous nuclear ribonucleoprotein U like 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.88× (z +19.7, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.45× (z +12.4, q 6e-33, up in 47 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 12 lines (LoVo 6.30×, A549 4.76×, HS-578T 5.30×, PANC-1 4.43×, …); [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 3.98×, NCI-H460 3.86×, SW480 3.26×, NCI-H2030 3.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 3.99×, KATO III 3.60×, A-172 3.82×, SW480 2.98×; ⚠ toxic; transcription drop); [[PH-797804 (drug)]] 5 µM in 3 lines (HEC-1-A 3.68×, LS 180 4.34×, HS-578T 3.62×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.333× (z -21.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPL]] (+0.72, fdr 7e-06), [[U2AF2]] (+0.70, fdr 7e-06), [[FOXM1]] (+0.66, fdr 7e-06); moves opposite to [[CAMLG]] (-0.67, fdr 1e-05), [[CIAO2B]] (-0.64, fdr 4e-05), [[LSM10]] (-0.64, fdr 7e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2581.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 12 lines (LoVo 6.30×, A549 4.76×, HS-578T 5.30×, PANC-1 4.43×, …); [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 3.98×, NCI-H460 3.86×, SW480 3.26×, NCI-H2030 3.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (PANC-1 3.99×, KATO III 3.60×, A-172 3.82×, SW480 2.98×; ⚠ toxic; transcription drop); [[PH-797804 (drug)]] 5 µM in 3 lines (HEC-1-A 3.68×, LS 180 4.34×, HS-578T 3.62×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +19.7 | 0e+00 | 49/49 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +17.3 | 0e+00 | 44/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.45×** | +12.4 | 6e-33 | 47/49 (LoVo, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +11.8 | 5e-30 | 38/45 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +8.1 | 4e-14 | 39/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **1.33×** | +5.4 | 5e-06 | 30/48 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.20× | +3.4 | 0.048 | 23/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.3 | 0.063 | 22/48 (PANC-1, HT-29, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.18× | +3.1 | 0.11 | 19/48 (PANC-1, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.333×** | -21.0 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.366×** | -19.2 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.439×** | -15.7 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.595×** | -9.9 | 6e-21 | 46/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.708×** | -9.3 | 2e-18 | 47/48 (H4, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.684×** | -7.2 | 4e-11 | 43/49 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.796×** | -6.1 | 7e-08 | 32/48 (A-427, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.549×** | -6.0 | 2e-07 | 44/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.765×** | -5.1 | 2e-05 | 36/48 (H4, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.772×** | -4.6 | 2e-04 | 35/48 (HOP62, SW48, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.792×** | -4.4 | 5e-04 | 30/48 (HepG2/C3A, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.796×** | -4.2 | 0.001 | 30/48 (HepG2/C3A, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.873× | -3.6 | 0.015 | 11/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.030 | 21/47 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.832×** | -3.4 | 0.030 | 22/47 (LoVo, SW 900, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.886× | -3.2 | 0.044 | 11/48 (RKO, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 239 | 5 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.80× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -17.7) |
| [[HS-578T (line)]] | alt | 164 | 6 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.30× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.314× (z -16.0) |
| [[SW480 (line)]] | alt | 180 | 4 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.45× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.242× (z -21.4) |
| [[LoVo (line)]] | wt | 133 | 5 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.30× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 145 | 4 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.96× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -12.5) |
| [[LS 180 (line)]] | wt | 156 | 5 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 4.34× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.278× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 144 | 4 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.77× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.313× (z -15.3) |
| [[SNU-423 (line)]] | alt | 91.8 | 5 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.94× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.397× (z -11.1) |
| [[A-172 (line)]] | wt | 146 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.66× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.279× (z -15.9) |
| [[A498 (line)]] | wt | 115 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +14.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -13.9) |
| [[A549 (line)]] | wt | 247 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.76× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.368× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 112 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.18× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.262× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 112 | 5 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.92× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.464× (z -10.0) |
| [[HT-29 (line)]] | alt | 198 | 3 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.76× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.281× (z -16.6) |
| [[KATO III (line)]] | alt | 175 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +17.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.242× (z -19.7) |
| [[PANC-1 (line)]] | alt | 105 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +19.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.43× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.303× (z -17.2) |
| [[SW1417 (line)]] | alt | 136 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -13.7) |
| [[A-427 (line)]] | wt | 129 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +12.2) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.500× (z -11.7) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.388× (z -11.3) |
| [[H4 (line)]] | wt | 182 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -13.6) |
| [[HCT15 (line)]] | alt | 225 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.67× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.345× (z -12.1) |
| [[HOP62 (line)]] | alt | 209 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +15.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.330× (z -14.3) |
| [[Hs 766T (line)]] | wt | 100 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +14.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.333× (z -11.6) |
| [[J82 (line)]] | alt | 183 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.247× (z -19.0) |
| [[MIA PaCa-2 (line)]] | alt | 183 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +15.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 144 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +17.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.434× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 183 | 3 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.333× (z -12.2) |
| [[SW 900 (line)]] | alt | 173 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.273× (z -16.3) |
| [[COLO 205 (line)]] | alt | 128 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.34× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.211× (z -16.9) |
| [[hTERT-HPNE (line)]] | wt | 140 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +11.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.304× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 69.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.06× (z +15.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.337× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 123 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.33× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.409× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 154 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.318× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 91.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +17.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.292× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 124 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -13.4) |
| [[SW48 (line)]] | wt | 189 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.300× (z -13.0) |
| [[BT-474 (line)]] | alt | 158 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.30× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -14.6) |
| [[C-33 A (line)]] | alt | 149 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.28× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -13.3) |
| [[C32 (line)]] | wt | 118 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +13.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.335× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 141 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -12.2) |
| [[RKO (line)]] | wt | 131 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.16× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.408× (z -10.5) |
| [[SHP-77 (line)]] | alt | 156 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.33× (z +10.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.309× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -13.0) |
| [[SNU-1 (line)]] | wt | 148 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +10.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.368× (z -9.3) |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 537 |
| [[U2AF2]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions |
| [[FOXM1]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SSU72]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[BAG6]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MCM7]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[RAVER1]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[CBX5]] | +0.63 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PCNT]] | +0.62 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[ATP13A1]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ILF2]] | +0.62 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[PTBP1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 501 |

## Genes that move opposite

*46 of its nearest partners move opposite, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | -0.67 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.64 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[LSM10]] | -0.64 | -0.38 / -0.65 | both halves | 7e-05 |  |
| [[RPP21]] | -0.63 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[SNHG7]] | -0.62 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[PDCD5]] | -0.62 | -0.43 / -0.56 | both halves | 4e-05 |  |
| [[BLVRB]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[MIEN1]] | -0.61 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[CHCHD10]] | -0.61 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[RBIS]] | -0.61 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[MED10]] | -0.61 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[ANO10]] | -0.60 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.7, -31.7); signed map (-9.5, -34.8). **Vector** length 115, 40.0% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +11.0 | +12.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +9.2 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.0 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +19.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.4 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +0.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.8 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.7 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein U like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,262,496-41,307,787 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E1B-AP5, E1BAP5, FLJ12944; previously HNRPUL1 |
| Reactome | 3 pathways, smallest: Dengue Virus-Host Interactions; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUJ2](https://www.uniprot.org/uniprotkb/Q9BUJ2) (Heterogeneous nuclear ribonucleoprotein U-like protein 1):

> Acts as a basic transcriptional regulator. Represses basic transcription driven by several virus and cellular promoters. When associated with BRD7, activates transcription of glucocorticoid-responsive promoter in the absence of ligand-stimulation. Also plays a role in mRNA processing and transport. Binds avidly to poly(G) and poly(C) RNA homopolymers in vitro.

**Summary**, from NCBI Gene [11100](https://www.ncbi.nlm.nih.gov/gene/11100):

> This gene encodes a nuclear RNA-binding protein of the heterogeneous nuclear ribonucleoprotein (hnRNP) family. This protein binds specifically to adenovirus early-1B-55kDa oncoprotein. It may play an important role in nucleocytoplasmic RNA transport, and its function is modulated by early-1B-55kDa in adenovirus-infected cells. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:17011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17011) · Entrez [11100](https://www.ncbi.nlm.nih.gov/gene/11100) · UniProt [Q9BUJ2](https://www.uniprot.org/uniprotkb/Q9BUJ2) · Ensembl [ENSG00000105323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105323)

## Data

Gene col 2581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2581); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2581]; `tensor/DDL_lfc|DDL_z.npy` [2581]; `embed/gene_vectors.npy` [2581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2581 or target_col == 2581). Every well: [[HNRNPUL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPUL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
