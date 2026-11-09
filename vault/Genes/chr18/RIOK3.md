---
symbol: "RIOK3"
type: "gene"
col: 2172
ensembl_id: "ENSG00000101782"
name: "RIO kinase 3"
location: "18q11.2"
module: 1
arm: "-"
pooled_cpm: 239.81
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RIOK3

*RIO kinase 3* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +13.0, q 5e-36, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.05× (z +11.4, q 1e-27, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.718× (z -5.0, q 4e-04, down in 26 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Palmatine (chloride) (drug)]] 0.05 µM: 0.786× (z -3.8, q 0.031, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.299×, CFPAC-1 0.256×, NCI-H2347 0.393×, NCI-H1792 0.321×, …; ⚠ toxic; transcription drop); [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (AsPC-1 0.424×, NCI-H2347 0.437×, Panc 03.27 0.511×; ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2347 0.369×, CFPAC-1 0.327×, Panc 03.27 0.460×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2347 0.475×); [[TAK-733 (drug)]] 5 µM in 1 line (AsPC-1 0.289×); [[Panobinostat (drug)]] 5 µM in 1 line (AsPC-1 0.528×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNPLA8]] (+0.65, fdr 7e-06), [[WASF2]] (+0.65, fdr 1e-05), [[KDM5B]] (+0.64, fdr 7e-06); moves opposite to [[ARMC6]] (-0.68, fdr 7e-06), [[ANAPC7]] (-0.63, fdr 7e-06), [[IPO9]] (-0.62, fdr 7e-06).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[VSIR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.81×** | +13.0 | 5e-36 | 43/47 (A-427, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.05×** | +11.4 | 1e-27 | 47/48 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +9.4 | 7e-19 | 42/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.96×** | +8.8 | 1e-16 | 43/47 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +7.1 | 1e-10 | 35/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.3 | 3e-08 | 33/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +5.4 | 7e-06 | 28/47 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 31/47 (A-427, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +5.1 | 2e-05 | 29/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.6 | 2e-04 | 27/37 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.001 | 24/47 (A-427, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 32/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.63×** | +4.0 | 0.003 | 32/47 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.009 | 23/47 (A-427, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.27×** | +3.6 | 0.013 | 25/47 (A-427, NCI-H1573, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.013 | 24/47 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | 1.16× | +3.3 | 0.034 | 12/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.16× | +3.3 | 0.034 | 10/48 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.043 | 18/48 (CFPAC-1, CHP-212, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2172.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (Panc 03.27 0.299×, CFPAC-1 0.256×, NCI-H2347 0.393×, NCI-H1792 0.321×, …; ⚠ toxic; transcription drop); [[c-Kit-IN-1 (drug)]] 0.05 µM in 3 lines (AsPC-1 0.424×, NCI-H2347 0.437×, Panc 03.27 0.511×; ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2347 0.369×, CFPAC-1 0.327×, Panc 03.27 0.460×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2347 0.475×); [[TAK-733 (drug)]] 5 µM in 1 line (AsPC-1 0.289×); [[Panobinostat (drug)]] 5 µM in 1 line (AsPC-1 0.528×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.718×** | -5.0 | 4e-04 | 26/43 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.735×** | -4.8 | 4e-04 | 32/47 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.786×** | -3.8 | 0.031 | 29/48 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.858× | -3.4 | 0.094 | 15/47 (NCI-H1573, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Artesunate (drug)]] 0.05 µM |  | 0.814× | -3.2 | 0.13 | 23/47 (KATO III, SHP-77, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.815× | -3.2 | 0.13 | 20/48 (SHP-77, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.686× | -3.1 | 0.17 | 21/47 (AsPC-1, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 108 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +17.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.01× (z +16.8) | — |
| [[AsPC-1 (line)]] | alt | 1,065 | 3 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.424× (z -11.9) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.289× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 191 | 7 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.47× (z +14.7) | — |
| [[PANC-1 (line)]] | alt | 151 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 166 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.87× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 211 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.99× (z +12.6) | [[Selinexor (drug)]] 5 µM 0.555× (z -10.3) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H2347 (line)]] | alt | 350 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.475× (z -9.6) |
| [[SW480 (line)]] | alt | 191 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.72× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 557 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 530 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.85× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -12.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 625 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -16.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 202 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.87× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.474× (z -9.6) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 157 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.97× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.459× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 115 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +14.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.04× (z +9.9) | — |
| [[RKO (line)]] | wt | 135 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +13.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.68× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 184 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 178 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.98× (z +9.0) | — |
| [[A498 (line)]] | wt | 149 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +9.3) | — |
| [[C32 (line)]] | wt | 207 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 333 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.41× (z +9.4) | — |
| [[KATO III (line)]] | alt | 195 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 253 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 236 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.99× (z +8.7) | — |
| [[SW48 (line)]] | wt | 108 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 3.50× (z +8.8) | — |
| [[A-172 (line)]] | wt | 228 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 195 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.63× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 179 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[H4 (line)]] | wt | 152 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 320 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 185 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 174 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW 900 (line)]] | alt | 257 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.81× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 157 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 201 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 228 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 208 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPLA8]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[WASF2]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.64 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[ANG]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[CTR9]] | +0.63 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[MXD1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RNASE4]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FBXO33]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[OSER1]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 |  |
| [[RAB1A]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[MINDY2]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC6]] | -0.68 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.63 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[IPO9]] | -0.62 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ADGRA3]] | -0.62 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.61 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[CAD]] | -0.60 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[WDR77]] | -0.59 | -0.53 / -0.54 | both halves | 1e-05 | STRING 446 |
| [[WDR4]] | -0.58 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.58 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PAXIP1]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PFAS]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[ATR]] | -0.57 | -0.61 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VSIR]] | B | VSIR activity raises RIOK3's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.67× lower at baseline in the lines without VSIR | 0.001 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |
| [[GPRC5A]] | B | GPRC5A activity raises RIOK3's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without GPRC5A | 0.053 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[LINC00482]] | B | LINC00482 activity raises RIOK3's level | lines that do not express LINC00482 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without LINC00482 | 0.058 | ⚠ within organs, on part of the lines; also absent: SOX13, SEPTIN9-DT |
| [[NDRG1]] | B | NDRG1 activity raises RIOK3's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without NDRG1 | 0.091 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (7.5, -41.2); signed map (-23.7, 14.0). **Vector** length 125, 47.7% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -0.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +1.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.4 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.5 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.7 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.9 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.0 | +7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.3 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.0 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | RIO kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:23,453,287-23,486,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SUDD |
| Gene groups (HGNC) | Ribosome biogenesis factors; RIO kinase family |
| Hallmark sets | HEME_METABOLISM, ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [O14730](https://www.uniprot.org/uniprotkb/O14730) (Serine/threonine-protein kinase RIO3):

> Serine/threonine-protein kinase involved in a ribosome quality control that takes place when ribosomes have stalled, leading to 18S non-functional rRNA decay and degradation of the 40S ribosomal subunit. Acts downstream of RNF10: specifically recognizes and binds RPS2/us5 and RPS3/us3 monoubiquitinated by RNF10, promoting degradation of the 40S ribosomal subunit in a kinase-dependent manner. The RNF10-RIOK3 ribosome quality control takes place in response to ribosome subunit imbalance or …

**Summary**, from NCBI Gene [8780](https://www.ncbi.nlm.nih.gov/gene/8780):

> This gene was first identified by the similarity of its product to the Aspergillus nidulans SUDD protein. This gene is now recognized as a member of the right open reading frame (RIO) kinase gene family. This gene encodes a serine/threonine kinase that localizes to the cytoplasm and plays a role in the processing of the pre-40 S ribosomal subunit. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:11451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11451) · Entrez [8780](https://www.ncbi.nlm.nih.gov/gene/8780) · UniProt [O14730](https://www.uniprot.org/uniprotkb/O14730) · Ensembl [ENSG00000101782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101782)

## Data

Gene col 2172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2172); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2172]; `tensor/DDL_lfc|DDL_z.npy` [2172]; `embed/gene_vectors.npy` [2172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2172 or target_col == 2172). Every well: [[RIOK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIOK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
