---
symbol: "SECISBP2L"
type: "gene"
col: 6188
ensembl_id: "ENSG00000138593"
name: "SECIS binding protein 2 like"
location: "15q21.1"
module: 5
arm: "-"
pooled_cpm: 126.85
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SECISBP2L

*SECIS binding protein 2 like* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.60× (z +15.0, q 0e+00, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.461× (z -23.3, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 0.748× (z -4.6, q 3e-04, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CWC15]] (+0.77, fdr 7e-06), [[TRIM23]] (+0.75, fdr 7e-06), [[ASB8]] (+0.73, fdr 7e-06); moves opposite to [[CTPS1]] (-0.67, fdr 7e-06), [[SLFNL1-AS1]] (-0.67, fdr 7e-06), [[WDR4]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6188.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +15.0 | 0e+00 | 43/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +10.0 | 5e-21 | 37/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +8.7 | 7e-16 | 26/48 (PANC-1, HT-29, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +7.2 | 1e-10 | 19/48 (NCI-H1573, LS 180, …) | rises with dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **1.57×** | +7.1 | 2e-10 | 39/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.19× | +5.1 | 3e-05 | 21/48 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.14× | +3.8 | 0.010 | 19/48 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.13× | +3.7 | 0.018 | 1/49 (C-33 A) | top dose only | plate-row cell shift |
| [[Terfenadine (drug)]] 5 µM |  | 1.08× | +3.4 | 0.038 | 3/48 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.12× | +3.3 | 0.047 | 9/49 (LOX-IMVI, CFPAC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.12× | +3.2 | 0.060 | 12/47 (C32, AsPC-1, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.08× | +3.2 | 0.064 | 2/48 (SHP-77, AN3 CA) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.064 | 14/48 (C32, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6188.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.461×** | -23.3 | 0e+00 | 47/49 (RKO, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -19.4 | 0e+00 | 38/44 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.671×** | -11.1 | 3e-26 | 30/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.783×** | -7.4 | 3e-11 | 33/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.843× | -7.3 | 4e-11 | 24/49 (A-172, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.793×** | -6.7 | 2e-09 | 32/50 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -5.2 | 2e-05 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.844× | -4.9 | 7e-05 | 23/48 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.748×** | -4.6 | 3e-04 | 23/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.854× | -4.6 | 3e-04 | 20/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~68% of this change | 0.871× | -4.0 | 0.004 | 18/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.913× | -3.9 | 0.005 | 8/48 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.782×** | -3.9 | 0.005 | 20/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.886× | -3.6 | 0.011 | 11/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.924× | -3.4 | 0.028 | 5/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.891× | -3.3 | 0.032 | 11/48 (CHP-212, RPMI-7951, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.897× | -3.3 | 0.038 | 8/48 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.928× | -3.2 | 0.045 | 3/48 (SW1417, RKO, …) | top dose only |  |
| [[Olanzapine (drug)]] 5 µM |  | 0.928× | -3.2 | 0.045 | 0/48 | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.906× | -3.0 | 0.083 | 16/48 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.829×** | -2.9 | 0.083 | 14/48 (BT-474, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.831×** | -2.9 | 0.085 | 13/48 (NCI-H2347, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.908× | -2.9 | 0.085 | 8/49 (SW1417, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6188. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 175 | 7 | 5 (5 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 2.17× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -19.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.567× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 219 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -22.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 173 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -20.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 96.3 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +19.2) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.96× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.521× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 120 | 3 (2 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.51× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.99× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 147 | 2 (2 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.22× (z +12.8) ⚠ cell-cycle shift, explains ~4% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -15.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SNU-423 (line)]] | alt | 116 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 126 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.79× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 162 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -17.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 126 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -15.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 155 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -11.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 150 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -16.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -17.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 102 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.5) ⚠ cell-cycle shift, explains ~13% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 134 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -9.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 119 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.2) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.66× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0747× (z -28.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 154 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.8) ⚠ cell-cycle shift, explains ~13% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 96.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.6) ⚠ cell-cycle shift, explains ~13% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -9.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -12.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 149 | 0 | 2 (1 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.185× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -10.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 99.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -13.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 230 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -17.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 64.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -11.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 118 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.59× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 82.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.473× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -18.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 87.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.37× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.519× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 85.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 157 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6188), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC15]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[ASB8]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CIR1]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[DCAF5]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[METTL14]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[EXOC1]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[FRG1]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[MPHOSPH8]] | +0.64 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[IK]] | +0.64 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[VIRMA]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MRPL22]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS1]] | -0.67 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | -0.67 | -0.67 / -0.68 | both halves | 7e-06 |  |
| [[WDR4]] | -0.66 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[HNRNPAB]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[UBE2G2]] | -0.65 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[NUP188]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[LRP8]] | -0.62 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[XXYLT1]] | -0.62 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[PRMT3]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[PUS1]] | -0.60 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[IRAK1]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PKP4]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.9, -28.3); signed map (-15.0, -5.9). **Vector** length 122, 36.1% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.8 | +7.2 |
|  | [[NG25 (drug)]] 5 µM |  | +6.5 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +15.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +5.0 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +4.5 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +10.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.4 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.8 | -7.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -4.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Volasertib (drug)]] 0.5 µM |  | -3.2 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | SECIS binding protein 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:48,988,476-49,046,447 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0256 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93073](https://www.uniprot.org/uniprotkb/Q93073) (Selenocysteine insertion sequence-binding protein 2-like):

> Binds SECIS (Sec insertion sequence) elements present on selenocysteine (Sec) protein mRNAs, but does not promote Sec incorporation into selenoproteins in vitro.

**Summary**, from NCBI Gene [9728](https://www.ncbi.nlm.nih.gov/gene/9728):

> Enables RNA binding activity. Predicted to be involved in selenocysteine incorporation. Predicted to be part of ribonucleoprotein complex. Predicted to be active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28997) · Entrez [9728](https://www.ncbi.nlm.nih.gov/gene/9728) · UniProt [Q93073](https://www.uniprot.org/uniprotkb/Q93073) · Ensembl [ENSG00000138593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138593)

## Data

Gene col 6188: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6188); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6188, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6188]; `tensor/DDL_lfc|DDL_z.npy` [6188]; `embed/gene_vectors.npy` [6188]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6188 or target_col == 6188). Every well: [[SECISBP2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SECISBP2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
