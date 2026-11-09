---
symbol: "YTHDC2"
type: "gene"
col: 509
ensembl_id: "ENSG00000047188"
name: "YTH N6-methyladenosine RNA binding protein C2"
location: "5q22.2"
module: 1
arm: "+"
pooled_cpm: 59.61
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# YTHDC2

*YTH N6-methyladenosine RNA binding protein C2* — 5q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +15.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.408× (z -7.9, q 1e-12, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCFC2]] (+0.76, fdr 7e-06), [[SMARCB1]] (+0.74, fdr 7e-06), [[ZNF280D]] (+0.74, fdr 7e-06); moves opposite to [[MED26]] (-0.69, fdr 7e-06), [[ALKBH5]] (-0.66, fdr 7e-06), [[SBNO1]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +15.8 | 0e+00 | 46/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +10.3 | 3e-22 | 43/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +10.2 | 4e-22 | 44/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.6 | 3e-06 | 31/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +5.1 | 4e-05 | 30/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.033 | 23/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.4 | 0.041 | 21/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.041 | 18/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.062 | 15/48 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 1.14× | +3.3 | 0.062 | 19/48 (NCI-H2347, SNU-423, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -7.9 | 1e-12 | 42/49 (Hs 766T, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -7.5 | 2e-11 | 36/48 (SNU-1, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -6.9 | 1e-09 | 35/48 (SW480, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.696×** | -6.3 | 4e-08 | 32/48 (PANC-1, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.539×** | -5.5 | 5e-06 | 28/48 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -5.1 | 3e-05 | 24/50 (AN3 CA, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.762×** | -4.6 | 4e-04 | 26/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **0.791×** | -4.1 | 0.003 | 28/48 (NCI-H661, J82, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.647×** | -3.9 | 0.007 | 23/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.747×** | -3.6 | 0.016 | 18/48 (hTERT-HPNE, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.819×** | -3.5 | 0.026 | 20/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.825×** | -3.4 | 0.036 | 20/48 (HCT15, HepG2/C3A, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.879× | -3.2 | 0.066 | 7/49 (SHP-77, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | 0.836× | -3.0 | 0.11 | 19/44 (SNU-1, AN3 CA, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 87.7 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.2) | [[Auranofin (drug)]] 5 µM 0.376× (z -14.0) |
| [[PANC-1 (line)]] | alt | 66.3 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.323× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 58.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.50× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.348× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 111 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -11.5) |
| [[A-427 (line)]] | wt | 107 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.3) | [[PH-797804 (drug)]] 5 µM 0.0765× (z -15.7) |
| [[AN3 CA (line)]] | alt | 146 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -11.6) |
| [[LoVo (line)]] | wt | 104 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.30× (z +9.7) | [[Auranofin (drug)]] 5 µM 0.460× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 49.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 73.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.380× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[AsPC-1 (line)]] | alt | 33.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +18.9) | — |
| [[Hs 766T (line)]] | wt | 54.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.4) | [[TAK-901 (drug)]] 5 µM 0.111× (z -9.5) |
| [[HT-29 (line)]] | alt | 33.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +15.2) | — |
| [[KATO III (line)]] | alt | 40.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 47.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 65.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 58.2 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.08× (z +12.8) | — |
| [[SW48 (line)]] | wt | 64.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +11.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -8.5) |
| [[A-172 (line)]] | wt | 50.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.2) | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.140× (z -10.0) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HCT15 (line)]] | alt | 56.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 63.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.468× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 54.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 48.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 59.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 57.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.5) | — |
| [[NCI-H23 (line)]] | alt | 61.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.5) | — |
| [[NCI-H661 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0998× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SHP-77 (line)]] | alt | 67.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SW 900 (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.0) | — |
| [[A498 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | +0.76 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[SMARCB1]] | +0.74 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[ZNF280D]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[CPLANE1]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MIOS]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ZNF678]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[GUF1]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 | STRING 407 |
| [[ANAPC7]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[FKTN]] | +0.68 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[NHLRC2]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ICE2]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | -0.69 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[ALKBH5]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 | STRING 921 |
| [[SBNO1]] | -0.65 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[MGAT1]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ADIPOR1]] | -0.64 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[UBTD1]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[DPM1]] | -0.63 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[TBC1D22A-DT]] | -0.63 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.63 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.62 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[MOSPD3]] | -0.62 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[MTMR14]] | -0.62 | -0.68 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.2, 4.5); signed map (10.0, -34.0). **Vector** length 115, 32.8% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.5 | +15.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.2 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.2 | +10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.3 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -7.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | YTH N6-methyladenosine RNA binding protein C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.2 — chr5:113,513,694-113,595,285 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ2194, FLJ10053, DKFZp564A186 |
| Gene groups (HGNC) | YTH domain containing N6-methyladenosine readers |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6S0](https://www.uniprot.org/uniprotkb/Q9H6S0) (3'-5' RNA helicase YTHDC2):

> 3'-5' RNA helicase that plays a key role in the male and female germline by promoting transition from mitotic to meiotic divisions in stem cells. Specifically recognizes and binds N6-methyladenosine (m6A)-containing RNAs, a modification present at internal sites of mRNAs and some non-coding RNAs that plays a role in the efficiency of RNA processing and stability. Essential for ensuring a successful progression of the meiotic program in the germline by regulating the level of m6A-containing RNAs …

**Summary**, from NCBI Gene [64848](https://www.ncbi.nlm.nih.gov/gene/64848):

> This gene encodes a member of the DEAH (Asp-Glu-Ala-His) subfamily of proteins, part of the DEAD (Asp-Glu-Ala-Asp) box family of RNA helicases. The encoded protein binds to N6-methyladenosine, a common modified RNA nucleotide that is enriched in the stop codons and 3' UTRs of eukaryotic messenger RNAs. Binding of proteins to this modified nucleotide may regulate mRNA translation and stability. This gene may be associated with susceptibility to pancreatic cancer in human patients, and knockdown …

**Accessions** — [HGNC:24721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24721) · Entrez [64848](https://www.ncbi.nlm.nih.gov/gene/64848) · UniProt [Q9H6S0](https://www.uniprot.org/uniprotkb/Q9H6S0) · Ensembl [ENSG00000047188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047188)

## Data

Gene col 509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 509); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 509]; `tensor/DDL_lfc|DDL_z.npy` [509]; `embed/gene_vectors.npy` [509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 509 or target_col == 509). Every well: [[YTHDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YTHDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
