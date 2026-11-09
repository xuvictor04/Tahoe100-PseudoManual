---
symbol: "ANKRD36C"
type: "gene"
col: 10501
ensembl_id: "ENSG00000174501"
name: "ankyrin repeat domain 36C"
location: "2q11.1"
module: 175
arm: "+"
pooled_cpm: 130.62
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ANKRD36C

*ankyrin repeat domain 36C* — 2q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.39× (z +4.5, q 0.004, up in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~24% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 3.21×; ⚠ cell-cycle shift, explains ~29% of this change); [[Trametinib (drug)]] 5 µM in 1 line (AsPC-1 3.68×; ⚠ cell-cycle shift, explains ~59% of this change); [[Bimiralisib (drug)]] 5 µM in 1 line (AsPC-1 9.93×); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 2.74×); [[Binimetinib (drug)]] 5 µM in 1 line (AsPC-1 3.02×).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.416× (z -16.5, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00342]] (+0.67, fdr 7e-06, ⚠ same locus), [[ANKRD36]] (+0.62, fdr 7e-06), [[YWHAH]] (+0.52, fdr 8e-05), [[RTKN2]] (+0.48, fdr 6e-05); moves opposite to [[OXSM]] (-0.48, fdr 5e-05), [[ALG11]] (-0.43, fdr 1e-04), [[BET1]] (-0.42, fdr 1e-04).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10501.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 3.21×; ⚠ cell-cycle shift, explains ~29% of this change); [[Trametinib (drug)]] 5 µM in 1 line (AsPC-1 3.68×; ⚠ cell-cycle shift, explains ~59% of this change); [[Bimiralisib (drug)]] 5 µM in 1 line (AsPC-1 9.93×); [[Trametinib (drug)]] 0.5 µM in 1 line (AsPC-1 2.74×); [[Binimetinib (drug)]] 5 µM in 1 line (AsPC-1 3.02×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +4.5 | 0.004 | 32/47 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.58× | +3.4 | 0.12 | 27/49 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.28× | +3.4 | 0.12 | 26/47 (LoVo, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.51× | +3.0 | 0.32 | 25/50 (AsPC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.416×** | -16.5 | 0e+00 | 47/49 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.454×** | -15.1 | 0e+00 | 42/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.432×** | -11.5 | 2e-28 | 44/48 (A-172, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.259×** | -10.1 | 1e-21 | 49/49 (NCI-H23, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.508×** | -9.7 | 5e-20 | 46/48 (HCT15, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.501×** | -9.5 | 2e-19 | 39/48 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.528×** | -9.1 | 6e-18 | 44/48 (HCT15, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.561×** | -8.0 | 6e-14 | 37/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.611×** | -7.0 | 1e-10 | 40/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.613×** | -7.0 | 2e-10 | 36/48 (BT-474, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -6.5 | 6e-09 | 35/47 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.624×** | -6.4 | 1e-08 | 41/48 (HT-29, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -6.3 | 2e-08 | 38/48 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.636×** | -6.2 | 2e-08 | 38/50 (BT-474, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -5.5 | 2e-06 | 38/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -5.2 | 6e-06 | 38/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.699×** | -5.1 | 1e-05 | 33/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.724×** | -4.6 | 1e-04 | 29/48 (BT-474, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -3.9 | 0.002 | 27/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.006 | 22/48 (SNU-423, SNU-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -3.4 | 0.011 | 27/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.749×** | -3.0 | 0.062 | 19/48 (H4, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 552 | 0 | 44 (20 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -16.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -15.6) |
| [[A-172 (line)]] | wt | 213 | 0 | 15 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.182× (z -17.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.8) |
| [[PANC-1 (line)]] | alt | 140 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -20.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -19.4) |
| [[NCI-H23 (line)]] | alt | 237 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 95.9 | 8 (1 ⚠) | 2 (2 ⚠) | [[Trametinib (drug)]] 5 µM 3.68× (z +11.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Bimiralisib (drug)]] 5 µM 9.93× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 216 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 169 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -19.5) |
| [[SNU-423 (line)]] | alt | 149 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 137 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.284× (z -14.8) |
| [[A549 (line)]] | wt | 141 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -20.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -15.4) |
| [[HOP62 (line)]] | alt | 115 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -12.2) |
| [[HS-578T (line)]] | alt | 109 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 143 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +15.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Harringtonine (drug)]] 5 µM 0.280× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 154 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -14.2) |
| [[SNU-1 (line)]] | wt | 213 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -12.8) |
| [[SW48 (line)]] | wt | 158 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -10.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.3) |
| [[COLO 205 (line)]] | alt | 73.3 | 4 | 0 | [[Vinblastine (sulfate) (drug)]] 0.5 µM 5.01× (z +9.9) | — |
| [[H4 (line)]] | wt | 96.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -10.1) |
| [[Hs 766T (line)]] | wt | 80.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -16.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 91.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 106 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -12.4) |
| [[RKO (line)]] | wt | 191 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.232× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.1) |
| [[A-427 (line)]] | wt | 130 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.212× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 144 | 1 (1 ⚠) | 2 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.91× (z +8.8) ⚠ cell-cycle shift, explains ~24% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.3) |
| [[HCT15 (line)]] | alt | 135 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.8) |
| [[HT-29 (line)]] | alt | 113 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +9.7) | [[Bortezomib (drug)]] 0.05 µM 0.295× (z -8.8) |
| [[KATO III (line)]] | alt | 88.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 53.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.315× (z -9.2) |
| [[A498 (line)]] | wt | 41.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 92.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -12.2) |
| [[J82 (line)]] | alt | 138 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -16.2) |
| [[SW 900 (line)]] | alt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.72× (z +8.8) ⚠ cell-cycle shift, explains ~24% of this change | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.499× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.267× (z -8.5) |
| [[C-33 A (line)]] | alt | 160 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.0) |
| [[CHP-212 (line)]] | wt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.9) |
| [[LoVo (line)]] | wt | 84.5 | 1 | 0 | [[BAY1125976 (drug)]] 5 µM 4.69× (z +9.2) | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.310× (z -8.8) |
| [[SW 1088 (line)]] | alt | 146 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0599× (z -10.5) |
| [[SW1417 (line)]] | alt | 91.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -10.6) |
| [[AN3 CA (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 93.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00342]] | +0.67 | +0.61 / +0.73 | both halves | 7e-06 | ⚠ same locus (1.9 kb, same strand: neighbours can correlate without regulation) |
| [[ANKRD36]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 | STRING 999 |
| [[YWHAH]] | +0.52 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[RTKN2]] | +0.48 | +0.39 / +0.38 | both halves | 6e-05 |  |
| [[CHML]] | +0.47 | +0.31 / +0.47 | both halves | 2e-04 |  |
| [[FAM161A]] | +0.47 | +0.34 / +0.32 | both halves | 2e-04 |  |
| [[ARL6IP6]] | +0.47 | +0.28 / +0.42 | both halves | 3e-04 |  |
| [[KATNAL1]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[STX2]] | +0.46 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[CENPI]] | +0.46 | +0.40 / +0.33 | both halves | 1e-04 |  |
| [[CEP55]] | +0.45 | +0.40 / +0.36 | both halves | 1e-04 |  |
| [[CEP128]] | +0.45 | +0.39 / +0.34 | both halves | 1e-04 |  |
| [[ANKRD36B]] | +0.45 | +0.45 / +0.42 | both halves | 4e-05 | same gene group; STRING 896 |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXSM]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[ALG11]] | -0.43 | -0.42 / -0.32 | both halves | 1e-04 |  |
| [[BET1]] | -0.42 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[ISCU]] | -0.42 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[EAPP]] | -0.42 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[ZNF791]] | -0.41 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[XBP1]] | -0.41 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[ENPP3]] | -0.41 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[HMG20A]] | -0.41 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[RWDD2A]] | -0.41 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[SPAG4]] | -0.41 | -0.19 / -0.35 | ⚠ not reproduced | 8e-04 |  |
| [[DPF2]] | -0.41 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[KBTBD4]] | -0.40 | -0.23 / -0.37 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ANKRD36C's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DNMT3B]] | C | DNMT3B activity raises ANKRD36C's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without DNMT3B | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.144). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.0, -53.4); signed map (-49.5, -14.2). **Vector** length 91.2, 28.9% of its response variance represented; |z| ≥ 3 in 1,644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.3 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.2 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | +5.9 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.2 | -4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.1 | -5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +0.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -16.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.9 | -4.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 36C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.1 — chr2:95,836,919-95,991,831 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp667P0924 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q5JPF3](https://www.uniprot.org/uniprotkb/Q5JPF3) carries no function annotation.

**Summary**, from NCBI Gene [400986](https://www.ncbi.nlm.nih.gov/gene/400986):

> Predicted to enable ion channel inhibitor activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32946) · Entrez [400986](https://www.ncbi.nlm.nih.gov/gene/400986) · UniProt [Q5JPF3](https://www.uniprot.org/uniprotkb/Q5JPF3) · Ensembl [ENSG00000174501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174501)

## Data

Gene col 10501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10501); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10501]; `tensor/DDL_lfc|DDL_z.npy` [10501]; `embed/gene_vectors.npy` [10501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10501 or target_col == 10501). Every well: [[ANKRD36C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD36C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
