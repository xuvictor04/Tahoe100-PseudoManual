---
symbol: "SEPTIN10"
type: "gene"
col: 11826
ensembl_id: "ENSG00000186522"
name: "septin 10"
location: "2q13"
module: 78
arm: "+"
pooled_cpm: 189.14
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 36
n_dd_up_clean: 1
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# SEPTIN10

*septin 10* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.53× (z +9.6, q 5e-19, up in 29 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.16× (z +5.1, q 6e-05, up in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 6 lines (PANC-1 2.21×, A498 2.07×, A549 2.38×, NCI-H1573 2.61×, …; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 2.07×, MIA PaCa-2 1.88×; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 2.14×, A-427 1.85×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 2 lines (A-172 1.56×, SW480 1.59×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 1.99×); [[Panobinostat (drug)]] 0.05 µM in 1 line (SW480 1.83×).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.637× (z -10.6, q 2e-23, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARPC2]] (+0.72, fdr 7e-06), [[ITGA2]] (+0.70, fdr 7e-06), [[STK4]] (+0.70, fdr 7e-06); moves opposite to [[RPRD2]] (-0.66, fdr 1e-05), [[THAP3]] (-0.60, fdr 1e-05), [[RAF1]] (-0.59, fdr 4e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MIR31HG]] → it (grade B ⚠); 2 go from it, the strongest it → [[BCAP29]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 6 lines (PANC-1 2.21×, A498 2.07×, A549 2.38×, NCI-H1573 2.61×, …; ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 2.07×, MIA PaCa-2 1.88×; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 2.14×, A-427 1.85×; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 2 lines (A-172 1.56×, SW480 1.59×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 1.99×); [[Panobinostat (drug)]] 0.05 µM in 1 line (SW480 1.83×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +9.6 | 5e-19 | 29/43 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +8.8 | 3e-16 | 30/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +7.6 | 6e-12 | 33/49 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +5.1 | 6e-05 | 16/48 (A-172, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +4.5 | 9e-04 | 22/48 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +4.2 | 0.003 | 20/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.7 | 0.020 | 16/47 (LOX-IMVI, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.15× | +3.4 | 0.047 | 17/48 (A-172, SW480, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.15× | +3.4 | 0.047 | 16/47 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.066 | 18/49 (A-172, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -10.6 | 2e-23 | 37/48 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.742×** | -9.9 | 2e-20 | 37/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -9.8 | 2e-20 | 38/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.715×** | -9.8 | 3e-20 | 39/48 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.660×** | -9.4 | 9e-19 | 34/48 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.677×** | -9.1 | 6e-18 | 30/48 (A549, A-427, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.777×** | -8.4 | 5e-15 | 32/48 (RKO, AsPC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -8.3 | 7e-15 | 41/49 (HOP62, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.710×** | -8.0 | 7e-14 | 37/49 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.713×** | -7.9 | 1e-13 | 36/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.463×** | -7.4 | 8e-12 | 36/45 (NCI-H460, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.469×** | -7.3 | 2e-11 | 38/48 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.774×** | -7.2 | 3e-11 | 26/48 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.706×** | -7.0 | 8e-11 | 33/48 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.734×** | -7.0 | 1e-10 | 34/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.485×** | -6.9 | 1e-10 | 37/47 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.768×** | -6.8 | 5e-10 | 32/49 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 260 | 2 (2 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.88× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.506× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 293 | 1 (1 ⚠) | 7 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.61× (z +10.4) ⚠ unreliable plate only | [[Trametinib (drug)]] 0.5 µM 0.439× (z -11.4) |
| [[A-172 (line)]] | wt | 203 | 5 (4 ⚠) | 2 | [[Belinostat (drug)]] 5 µM 1.93× (z +10.6) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.56× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.660× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 422 | 1 (1 ⚠) | 6 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.27× (z +9.9) ⚠ unreliable plate only | [[Trametinib (drug)]] 0.5 µM 0.456× (z -11.5) |
| [[LoVo (line)]] | wt | 313 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -15.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.248× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 287 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -12.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.489× (z -10.7) |
| [[A549 (line)]] | wt | 182 | 1 (1 ⚠) | 5 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.38× (z +11.4) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -17.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -14.0) |
| [[HOP62 (line)]] | alt | 268 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.411× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.456× (z -9.6) |
| [[A498 (line)]] | wt | 132 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +12.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 122 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.313× (z -14.5) |
| [[LS 180 (line)]] | wt | 183 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.401× (z -9.0) |
| [[A-427 (line)]] | wt | 199 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.85× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -20.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.583× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 125 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 224 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.552× (z -11.5) |
| [[SW480 (line)]] | alt | 146 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 1.59× (z +9.2) | [[Trametinib (drug)]] 0.5 µM 0.601× (z -8.8) |
| [[H4 (line)]] | wt | 211 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.353× (z -10.8) |
| [[HS-578T (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.434× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 323 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.428× (z -12.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.605× (z -10.5) |
| [[PANC-1 (line)]] | alt | 251 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.21× (z +12.1) ⚠ unreliable plate only | [[Digitoxin (drug)]] 5 µM 0.564× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[RKO (line)]] | wt | 169 | 0 | 3 | — | [[Radotinib (drug)]] 5 µM 0.525× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 164 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Selinexor (drug)]] 5 µM 0.517× (z -11.4) |
| [[J82 (line)]] | alt | 150 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.410× (z -13.4) |
| [[BT-474 (line)]] | alt | 69.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.99× (z +9.0) ⚠ unreliable plate only | — |
| [[CFPAC-1 (line)]] | alt | 167 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.555× (z -8.5) |
| [[HCT15 (line)]] | alt | 235 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 184 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.36× (z +9.8) ⚠ unreliable plate only | — |
| [[HT-29 (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 191 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 221 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 74.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.463× (z -8.9) |
| [[SNU-423 (line)]] | alt | 136 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.471× (z -9.7) |
| [[SW 900 (line)]] | alt | 212 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.470× (z -8.7) |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 175 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 137 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC2]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[STK4]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CAPRIN2]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[SOWAHC]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | STRING 534; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[NT5E]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ITGB1]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.66 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[ITPRID2]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[BZW1]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.64 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPRD2]] | -0.66 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[THAP3]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[RAF1]] | -0.59 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[MRPL44]] | -0.59 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[BTN3A2]] | -0.57 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[SETD2]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[KCTD3]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ZNF148]] | -0.56 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DENND2B]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[BTN3A3]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PPP4R3A]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TLK2]] | -0.55 | -0.55 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR31HG]] | B | MIR31HG activity raises SEPTIN10's level | lines that do not express MIR31HG (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without MIR31HG | 0.020 | ⚠ within organs, on part of the lines; also absent: SMCO2, POU5F1, PLA2R1 |
| [[ITGA2]] | B | ITGA2 activity raises SEPTIN10's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.42× lower at baseline in the lines without ITGA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[IL1RAP]] | B | IL1RAP activity raises SEPTIN10's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without IL1RAP | 0.041 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[DENND2B]] | B | DENND2B activity lowers SEPTIN10's level | lines that do not express DENND2B (6) vs lines expressing it (44) | 1.79× higher at baseline in the lines without DENND2B | 0.067 | ⚠ within organs, on part of the lines; also absent: POGLUT3, METRNL, MEX3A; maybe low, not absent |
| [[CD59]] | B | CD59 activity raises SEPTIN10's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without CD59 | 0.069 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAP29]] | C | SEPTIN10's natural level strengthens BCAP29's drug response | SEPTIN10's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.29; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | SEPTIN10's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | SEPTIN10's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.461 over the table, 0.072 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.4, 5.6); signed map (5.7, 45.0). **Vector** length 157, 54.9% of its response variance represented; |z| ≥ 3 in 1,729 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *apical junction* (hallmark, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.7 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +6.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.7 | +2.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.5 | +4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.8 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.6 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.8 | -9.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -9.7 | -9.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.6 | -7.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -8.5 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.4 | -8.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.4 | -6.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -8.2 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | septin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:109,542,799-109,614,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11619, Septin-10; previously SEPT10 |
| Gene groups (HGNC) | Septins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0V9](https://www.uniprot.org/uniprotkb/Q9P0V9) (Septin-10):

> Filament-forming cytoskeletal GTPase. May play a role in cytokinesis (Potential).

**Summary**, from NCBI Gene [151011](https://www.ncbi.nlm.nih.gov/gene/151011):

> This gene encodes a member of the septin family of cytoskeletal proteins with GTPase activity. This protein localizes to the cytoplasm and nucleus and displays GTP-binding and GTPase activity. A pseudogene for this gene is located on chromosome 8. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:14349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14349) · Entrez [151011](https://www.ncbi.nlm.nih.gov/gene/151011) · UniProt [Q9P0V9](https://www.uniprot.org/uniprotkb/Q9P0V9) · Ensembl [ENSG00000186522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186522)

## Data

Gene col 11826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11826); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11826]; `tensor/DDL_lfc|DDL_z.npy` [11826]; `embed/gene_vectors.npy` [11826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11826 or target_col == 11826). Every well: [[SEPTIN10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
