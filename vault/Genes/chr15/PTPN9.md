---
symbol: "PTPN9"
type: "gene"
col: 9804
ensembl_id: "ENSG00000169410"
name: "protein tyrosine phosphatase non-receptor type 9"
location: "15q24.2"
module: 15
arm: "+"
pooled_cpm: 61.33
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PTPN9

*protein tyrosine phosphatase non-receptor type 9* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.19× (z +5.5, q 2e-05, up in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~99% of this change. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.26× (z +5.1, q 8e-05, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 2.31×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (HT-29 1.88×; ⚠ cell-cycle shift, explains ~99% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.240× (z -31.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRTC3]] (+0.71, fdr 7e-06), [[PPP1R26-AS1]] (+0.68, fdr 7e-06), [[ZNF710]] (+0.63, fdr 7e-06); moves opposite to [[GDE1]] (-0.58, fdr 6e-05), [[NR4A1]] (-0.57, fdr 1e-05), [[MAPRE2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF600]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9804.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 2.31×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (HT-29 1.88×; ⚠ cell-cycle shift, explains ~99% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | 1.19× | +5.5 | 2e-05 | 21/48 (HT-29, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.2 | 5e-05 | 23/49 (HT-29, SW480, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +5.1 | 8e-05 | 24/48 (A498, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.24×** | +4.8 | 2e-04 | 21/48 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.22×** | +4.5 | 9e-04 | 21/49 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.19× | +3.7 | 0.023 | 18/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.038 | 12/48 (NCI-H460, CFPAC-1, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.2 | 0.076 | 6/48 (SK-MEL-2, Hs 766T, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.076 | 10/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.076 | 14/47 (NCI-H2030, RKO, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.077 | 6/48 (NCI-H2030, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9804.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.240×** | -31.6 | 0e+00 | 48/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.284×** | -27.9 | 0e+00 | 47/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.461×** | -24.3 | 0e+00 | 44/48 (NCI-H23, A-172, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.361×** | -22.6 | 0e+00 | 46/48 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.561×** | -12.8 | 1e-35 | 40/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.624×** | -10.5 | 1e-23 | 34/49 (A-172, C-33 A, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -10.3 | 7e-23 | 41/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -10.0 | 1e-21 | 34/49 (NCI-H460, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.632×** | -9.4 | 4e-19 | 29/45 (A-427, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.644×** | -9.4 | 5e-19 | 33/47 (A-172, SHP-77, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.650×** | -9.2 | 2e-18 | 30/48 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.741×** | -6.6 | 2e-09 | 26/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -6.5 | 5e-09 | 2/49 (MIA PaCa-2, NCI-H1792) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.585×** | -6.2 | 2e-08 | 29/49 (A549, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.761×** | -6.0 | 5e-08 | 30/48 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.789×** | -5.2 | 5e-06 | 24/49 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.800×** | -4.9 | 2e-05 | 23/48 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.771×** | -3.0 | 0.065 | 21/48 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.895× | -2.9 | 0.094 | 9/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.8 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -24.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.203× (z -22.9) |
| [[A-172 (line)]] | wt | 92.4 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -31.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -22.4) |
| [[A549 (line)]] | wt | 105 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -24.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.163× (z -22.7) |
| [[HEC-1-A (line)]] | alt | 92.8 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -23.0) |
| [[HOP62 (line)]] | alt | 74.0 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -25.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.210× (z -17.8) |
| [[hTERT-HPNE (line)]] | wt | 62.3 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.211× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 68.3 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -23.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.283× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -19.8) |
| [[PANC-1 (line)]] | alt | 66.9 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -21.4) |
| [[A-427 (line)]] | wt | 45.1 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -18.0) |
| [[C32 (line)]] | wt | 55.8 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.229× (z -14.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.293× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 62.8 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -17.5) |
| [[A498 (line)]] | wt | 48.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.318× (z -12.9) |
| [[BT-474 (line)]] | alt | 60.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.210× (z -13.2) |
| [[LoVo (line)]] | wt | 88.8 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -24.3) |
| [[MIA PaCa-2 (line)]] | alt | 64.9 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -23.2) |
| [[NCI-H2347 (line)]] | alt | 65.9 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 50.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.204× (z -15.8) |
| [[SNU-423 (line)]] | alt | 41.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -17.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.173× (z -14.5) |
| [[AN3 CA (line)]] | alt | 88.9 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -12.8) |
| [[C-33 A (line)]] | alt | 102 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.149× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 59.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -14.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.286× (z -12.9) |
| [[HCT15 (line)]] | alt | 55.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0857× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.154× (z -10.3) |
| [[HS-578T (line)]] | alt | 34.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -11.2) |
| [[HT-29 (line)]] | alt | 38.4 | 2 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.285× (z -12.1) |
| [[J82 (line)]] | alt | 66.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -16.8) |
| [[LS 180 (line)]] | wt | 35.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 70.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -11.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 48.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0938× (z -32.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.225× (z -14.3) |
| [[SNU-1 (line)]] | wt | 54.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -13.2) |
| [[SW480 (line)]] | alt | 46.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -20.6) |
| [[AsPC-1 (line)]] | alt | 46.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -13.4) |
| [[H4 (line)]] | wt | 55.5 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -10.1) |
| [[KATO III (line)]] | alt | 47.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -12.4) |
| [[RKO (line)]] | wt | 50.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -12.1) |
| [[SHP-77 (line)]] | alt | 50.9 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.321× (z -10.5) |
| [[SW1417 (line)]] | alt | 55.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -15.2) |
| [[SW48 (line)]] | wt | 64.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -12.8) |
| [[Hs 766T (line)]] | wt | 40.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 47.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -16.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HepG2_C3A (line)]] | wt | 44.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRTC3]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R26-AS1]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZNF710]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RILPL1]] | +0.63 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CCNJ]] | +0.63 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[POU6F1]] | +0.62 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.62 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[MOB1B]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RCC1L]] | +0.59 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[TMEM267]] | +0.59 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[GPR161]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[CDR2]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDE1]] | -0.58 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[NR4A1]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MAPRE2]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[USP9X]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ATP7A]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SNAP25]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[RASSF4]] | -0.53 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[LMCD1]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PRDX2]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[JUNB]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RGL1]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ECH1]] | -0.52 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF600]] | B | ZNF600 activity lowers PTPN9's level | lines that do not express ZNF600 (9) vs lines expressing it (41) | 1.27× higher at baseline in the lines without ZNF600 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZNF320, ZNF28, ZNF468 |
| [[ZNF785]] | B | ZNF785 activity weakens PTPN9's drug response | lines that do not express ZNF785 (9) vs lines expressing it (40) | the lines without ZNF785 respond 1.41× as strongly (z diff -1.71); strongest at Dinaciclib 0.5 µM: 0.33x vs 0.63x (z diff -5.0) | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, BDH1, PARP8; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.2, 18.2); signed map (2.7, 10.0). **Vector** length 110, 32.1% of its response variance represented; |z| ≥ 3 in 1,235 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.5 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +7.9 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.4 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.3 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -10.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -12.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.0 | -31.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,463,251-75,579,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEG2 |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type; CRAL-TRIO lipid binding domain containing |
| Reactome | 4 pathways, smallest: Interleukin-37 signaling; Interleukin-1 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [P43378](https://www.uniprot.org/uniprotkb/P43378) (Tyrosine-protein phosphatase non-receptor type 9):

> Protein-tyrosine phosphatase that could participate in the transfer of hydrophobic ligands or in functions of the Golgi apparatus.

**Summary**, from NCBI Gene [5780](https://www.ncbi.nlm.nih.gov/gene/5780):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains an N-terminal domain that shares a significant similarity with yeast SEC14, which is a protein that has phosphatidylinositol transfer activity and is required for protein secretion through the Golgi complex in …

**Accessions** — [HGNC:9661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9661) · Entrez [5780](https://www.ncbi.nlm.nih.gov/gene/5780) · UniProt [P43378](https://www.uniprot.org/uniprotkb/P43378) · Ensembl [ENSG00000169410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169410)

## Data

Gene col 9804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9804); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9804]; `tensor/DDL_lfc|DDL_z.npy` [9804]; `embed/gene_vectors.npy` [9804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9804 or target_col == 9804). Every well: [[PTPN9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
