---
symbol: "ACBD6"
type: "gene"
col: 13736
ensembl_id: "ENSG00000230124"
name: "acyl-CoA binding domain containing 6"
location: "1q25.2-q25.3"
module: 213
arm: "+"
pooled_cpm: 174.5
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# ACBD6

*acyl-CoA binding domain containing 6* — 1q25.2-q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.30× (z +10.2, q 9e-22, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.582× (z -17.9, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZZZ3]] (+0.74, fdr 7e-06), [[TGFBRAP1]] (+0.68, fdr 7e-06), [[RBM26]] (+0.66, fdr 1e-05); moves opposite to [[CCNYL1]] (-0.58, fdr 1e-05), [[SYNJ1]] (-0.58, fdr 2e-05), [[MXD1]] (-0.57, fdr 1e-05).
> It is in [[Module 213]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +10.2 | 9e-22 | 40/49 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.22×** | +6.5 | 2e-08 | 23/48 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +6.4 | 3e-08 | 30/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.5 | 6e-06 | 31/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +5.4 | 6e-06 | 30/48 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.25×** | +5.3 | 1e-05 | 28/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.5 | 5e-04 | 23/48 (A-172, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.008 | 21/48 (LS 180, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.16× | +3.3 | 0.054 | 16/47 (SW480, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.090 | 9/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.0 | 0.12 | 10/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.12 | 17/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -17.9 | 0e+00 | 46/49 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -12.5 | 1e-33 | 40/44 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.653×** | -9.6 | 2e-19 | 40/50 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -9.4 | 5e-19 | 35/48 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.674×** | -9.2 | 4e-18 | 40/49 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -9.1 | 1e-17 | 35/48 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.658×** | -9.0 | 1e-17 | 34/45 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **0.720×** | -7.7 | 1e-12 | 37/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -6.0 | 1e-07 | 23/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.777×** | -5.9 | 2e-07 | 28/48 (MIA PaCa-2, HCT15, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.818×** | -4.7 | 2e-04 | 24/48 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.822×** | -4.6 | 2e-04 | 25/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.821×** | -4.4 | 4e-04 | 24/48 (C32, PANC-1, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | **0.825×** | -4.3 | 7e-04 | 24/47 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.833×** | -4.2 | 8e-04 | 21/48 (LOX-IMVI, LS 180, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.782×** | -4.1 | 0.002 | 29/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.840× | -3.9 | 0.003 | 19/48 (HS-578T, LoVo, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.821×** | -3.3 | 0.027 | 20/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.881× | -2.9 | 0.077 | 12/47 (NCI-H460, HT-29, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | 0.842× | -2.9 | 0.095 | 10/49 (HOP62, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 254 | 0 | 14 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -14.6) |
| [[PANC-1 (line)]] | alt | 214 | 0 | 14 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -23.0) |
| [[SW480 (line)]] | alt | 172 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.446× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -12.5) |
| [[C32 (line)]] | wt | 145 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -22.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 181 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -21.2) |
| [[SK-MEL-2 (line)]] | alt | 229 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.65× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.341× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 200 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -26.8) |
| [[HOP62 (line)]] | alt | 161 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 185 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.70× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -12.4) |
| [[A549 (line)]] | wt | 166 | 3 (2 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.57× (z +9.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.11× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -15.4) |
| [[Hs 766T (line)]] | wt | 162 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.51× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 294 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +24.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.07× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 253 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -14.5) |
| [[SNU-423 (line)]] | alt | 162 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -16.2) |
| [[SW48 (line)]] | wt | 223 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.3) |
| [[A-427 (line)]] | wt | 306 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -11.3) |
| [[HCT15 (line)]] | alt | 307 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.5) |
| [[KATO III (line)]] | alt | 129 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.73× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -15.9) |
| [[RKO (line)]] | wt | 184 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.0) |
| [[AN3 CA (line)]] | alt | 213 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -10.0) |
| [[C-33 A (line)]] | alt | 236 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.4) |
| [[H4 (line)]] | wt | 160 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.368× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 118 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -9.6) |
| [[A-172 (line)]] | wt | 145 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -10.5) |
| [[COLO 205 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.8) |
| [[J82 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -14.4) |
| [[LoVo (line)]] | wt | 162 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.10× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -16.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 178 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -9.5) |
| [[A498 (line)]] | wt | 147 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.462× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~5% of this change |
| [[CHP-212 (line)]] | wt | 278 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -14.6) |
| [[HS-578T (line)]] | alt | 107 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 138 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -8.9) |
| [[LS 180 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 142 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 132 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.43× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 153 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -14.5) |
| [[SHP-77 (line)]] | alt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -11.4) |
| [[SW 900 (line)]] | alt | 178 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 145 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZZZ3]] | +0.74 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[TGFBRAP1]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[RBM26]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[LDAH]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SHPRH]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NUFIP1]] | +0.64 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[NUBPL]] | +0.62 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[TMLHE]] | +0.62 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[THUMPD2]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[ABCB7]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[MRPS9]] | +0.61 | +0.42 / +0.68 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | -0.58 | -0.53 / -0.53 | both halves | 1e-05 | same gene group |
| [[SYNJ1]] | -0.58 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[MXD1]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[GTPBP1]] | -0.56 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[IRGQ]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MDGA1]] | -0.52 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[HECA]] | -0.52 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[ADGRL1-AS1]] | -0.52 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[RAB5B]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises ACBD6's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.39× lower at baseline in the lines without ANK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-18.9, 3.0); signed map (5.5, -39.8). **Vector** length 122, 39.9% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.3 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +8.6 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +5.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.3 | +5.3 |
|  | [[EX229 (drug)]] 5 µM |  | +5.3 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -17.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -9.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -9.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.7 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA binding domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2-q25.3 — chr1:180,269,653-180,502,954 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2404 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BR61](https://www.uniprot.org/uniprotkb/Q9BR61) (Acyl-CoA-binding domain-containing protein 6):

> Binds long-chain acyl-coenzyme A molecules with a strong preference for unsaturated C18:1-CoA, lower affinity for unsaturated C20:4-CoA, and very weak affinity for saturated C16:0-CoA. Does not bind fatty acids. Plays a role in protein N-myristoylation.

**Summary**, from NCBI Gene [84320](https://www.ncbi.nlm.nih.gov/gene/84320):

> Enables fatty-acyl-CoA binding activity. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23339) · Entrez [84320](https://www.ncbi.nlm.nih.gov/gene/84320) · UniProt [Q9BR61](https://www.uniprot.org/uniprotkb/Q9BR61) · Ensembl [ENSG00000230124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230124)

## Data

Gene col 13736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13736); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13736]; `tensor/DDL_lfc|DDL_z.npy` [13736]; `embed/gene_vectors.npy` [13736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13736 or target_col == 13736). Every well: [[ACBD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACBD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
