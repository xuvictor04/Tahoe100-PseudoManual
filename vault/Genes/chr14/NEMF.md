---
symbol: "NEMF"
type: "gene"
col: 9139
ensembl_id: "ENSG00000165525"
name: "nuclear export mediator factor"
location: "14q21.3"
module: 12
arm: "+"
pooled_cpm: 173.02
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NEMF

*nuclear export mediator factor* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +20.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.616× (z -17.9, q 0e+00, down in 47 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H2347 0.433×, SNU-1 0.332×, SW480 0.548×, LoVo 0.550×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-1 0.0669×, HEC-1-A 0.367×, LS 180 0.399×, SW48 0.362×, …; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRA10AC1]] (+0.75, fdr 7e-06), [[RBMX2]] (+0.74, fdr 7e-06), [[TARS2]] (+0.73, fdr 7e-06); moves opposite to [[PGRMC1]] (-0.62, fdr 1e-05), [[TXNDC5]] (-0.62, fdr 9e-06), [[RPN1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +20.7 | 0e+00 | 45/48 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +19.7 | 0e+00 | 48/48 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +10.3 | 1e-22 | 43/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +7.6 | 5e-12 | 33/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +7.0 | 3e-10 | 32/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.8 | 1e-09 | 32/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +5.6 | 2e-06 | 30/49 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +5.2 | 2e-05 | 28/48 (SNU-423, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.4 | 6e-04 | 22/48 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.002 | 22/48 (BT-474, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.16× | +3.8 | 0.007 | 19/48 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.8 | 0.007 | 13/48 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.027 | 19/49 (A-427, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.13× | +3.1 | 0.068 | 11/49 (SW 900, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.1 | 0.074 | 20/45 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 1.09× | +3.0 | 0.084 | 1/48 (A-172) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9139.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H2347 0.433×, SNU-1 0.332×, SW480 0.548×, LoVo 0.550×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-1 0.0669×, HEC-1-A 0.367×, LS 180 0.399×, SW48 0.362×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -17.9 | 0e+00 | 47/49 (NCI-H2347, SNU-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.640×** | -10.8 | 1e-24 | 35/45 (A-427, SW48, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -9.7 | 4e-20 | 37/44 (SNU-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.723×** | -8.5 | 3e-15 | 34/49 (Panc 03.27, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.812×** | -5.4 | 6e-06 | 27/48 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.818×** | -5.1 | 4e-05 | 27/47 (SW 900, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -5.0 | 4e-05 | 17/48 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.906× | -3.7 | 0.016 | 5/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.876× | -3.5 | 0.033 | 13/48 (SW480, J82, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.891× | -3.0 | 0.14 | 7/48 (HOP62, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 217 | 5 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +18.5) | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -12.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 263 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.23× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -14.6) |
| [[A-427 (line)]] | wt | 170 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 331 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 221 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -14.6) |
| [[SW 900 (line)]] | alt | 205 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -15.4) |
| [[SW48 (line)]] | wt | 325 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -8.5) |
| [[SW480 (line)]] | alt | 175 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -16.2) |
| [[LoVo (line)]] | wt | 202 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 247 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -21.1) |
| [[PANC-1 (line)]] | alt | 137 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.8) | — |
| [[A549 (line)]] | wt | 181 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 154 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -14.9) |
| [[A-172 (line)]] | wt | 89.2 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.31× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -9.5) |
| [[A498 (line)]] | wt | 101 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -9.3) |
| [[C-33 A (line)]] | alt | 184 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -13.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 157 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 140 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.5) |
| [[HT-29 (line)]] | alt | 93.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -11.7) |
| [[KATO III (line)]] | alt | 141 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +15.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 150 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +18.8) | — |
| [[LS 180 (line)]] | wt | 228 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 187 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -9.5) |
| [[RKO (line)]] | wt | 202 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.0) | [[Dinaciclib (drug)]] 0.05 µM 0.516× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 187 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -13.8) |
| [[AN3 CA (line)]] | alt | 187 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 172 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -11.0) |
| [[C32 (line)]] | wt | 172 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.9) | — |
| [[H4 (line)]] | wt | 138 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +12.5) | — |
| [[HCT15 (line)]] | alt | 174 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 134 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.0) | — |
| [[Hs 766T (line)]] | wt | 149 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 150 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.483× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 167 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 146 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.4) |
| [[SHP-77 (line)]] | alt | 215 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.98× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 165 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 218 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0669× (z -32.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -19.4) |
| [[COLO 205 (line)]] | alt | 163 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.7) |
| [[J82 (line)]] | alt | 129 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 212 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.538× (z -9.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 197 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRA10AC1]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TARS2]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PPIG]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 | STRING 572 |
| [[COIL]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[RP9]] | +0.66 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[LEO1]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[FAM133B]] | +0.66 | +0.58 / +0.61 | both halves | 8e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGRMC1]] | -0.62 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.62 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[RPN1]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[TMBIM6]] | -0.58 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.58 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD30BL]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[PRPS2]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CA5BP1-1]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CDK2]] | -0.56 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[YWHAQ]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[BSG]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers NEMF's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.7, -9.2); signed map (-16.2, -9.5). **Vector** length 133, 43.4% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +20.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +19.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +2.0 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +4.1 | +2.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +3.9 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.0 | -17.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -10.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.5 | +3.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -3.7 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -5.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -3.0 | -1.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -3.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear export mediator factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,782,083-49,852,821 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-1, FLJ10051, RQC2; previously SDCCAG1 |
| Reactome | 3 pathways, smallest: Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide; Ribosome-associated quality control; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [O60524](https://www.uniprot.org/uniprotkb/O60524) (Ribosome quality control complex subunit NEMF):

> Key component of the ribosome quality control complex (RQC), a ribosome-associated complex that mediates the extraction of incompletely synthesized nascent chains from stalled ribosomes as well as their ubiquitin-mediated proteasomal degradation. Thereby, frees 60S subunit ribosomes from the stalled translation complex and prevents the accumulation of nascent polypeptide chains that are potentially toxic for the cell. Within the RQC complex, NEMF specifically binds stalled 60S ribosomal …

**Summary**, from NCBI Gene [9147](https://www.ncbi.nlm.nih.gov/gene/9147):

> This gene encodes a component of the ribosome quality control complex. The encoded protein facilitates the recognition and ubiquitination of stalled 60S subunits by the ubiquitin ligase listerin. A similar protein in fly functions as a tumor suppressor. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:10663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10663) · Entrez [9147](https://www.ncbi.nlm.nih.gov/gene/9147) · UniProt [O60524](https://www.uniprot.org/uniprotkb/O60524) · Ensembl [ENSG00000165525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165525)

## Data

Gene col 9139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9139); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9139]; `tensor/DDL_lfc|DDL_z.npy` [9139]; `embed/gene_vectors.npy` [9139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9139 or target_col == 9139). Every well: [[NEMF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEMF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
