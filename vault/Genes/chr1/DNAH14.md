---
symbol: "DNAH14"
type: "gene"
col: 11740
ensembl_id: "ENSG00000185842"
name: "dynein axonemal heavy chain 14"
location: "1q42.12"
module: 16
arm: "+"
pooled_cpm: 120.33
n_lines_expressing: 40
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 20
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DNAH14

*dynein axonemal heavy chain 14* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.94× (z +13.5, q 9e-39, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.536× (z -12.7, q 4e-34, down in 35 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COA7]] (+0.70, fdr 7e-06), [[GCFC2]] (+0.68, fdr 7e-06), [[SLC25A13]] (+0.65, fdr 7e-06); moves opposite to [[NARF]] (-0.66, fdr 7e-06), [[KDELR1]] (-0.62, fdr 7e-06), [[COG7]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF480]] → it (grade C ⚠); 6 go from it, the strongest it → [[ZNF260]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +13.5 | 9e-39 | 37/38 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +8.8 | 3e-16 | 35/39 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.52×** | +8.5 | 3e-15 | 29/38 (PANC-1, J82, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +8.5 | 3e-15 | 32/38 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +8.0 | 1e-13 | 25/38 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +7.0 | 3e-10 | 24/38 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +6.4 | 1e-08 | 31/38 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.8 | 4e-07 | 27/38 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +5.7 | 8e-07 | 34/38 (J82, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +4.8 | 7e-05 | 27/38 (HCT15, NCI-H1573, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +4.6 | 2e-04 | 24/38 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.002 | 21/38 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.32×** | +4.0 | 0.003 | 21/38 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.004 | 23/38 (HCT15, LS 180, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.004 | 17/38 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.008 | 22/39 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.018 | 20/39 (A498, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.033 | 16/38 (NCI-H2347, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.536×** | -12.7 | 4e-34 | 35/39 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -5.8 | 1e-06 | 32/39 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.462×** | -5.8 | 1e-06 | 27/38 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.578×** | -4.1 | 0.005 | 22/35 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.776×** | -3.5 | 0.062 | 20/38 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.648× | -3.3 | 0.10 | 20/37 (RKO, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.793× | -3.2 | 0.11 | 23/40 (SK-MEL-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.671× | -3.0 | 0.19 | 17/38 (HCT15, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 164 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.217× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 70.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 60.9 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.66× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 211 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -12.5) |
| [[SW 900 (line)]] | alt | 207 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -14.5) |
| [[SW480 (line)]] | alt | 225 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -15.9) |
| [[CHP-212 (line)]] | wt | 344 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 184 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 288 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -11.2) |
| [[A549 (line)]] | wt | 103 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.94× (z +9.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.89× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 183 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.214× (z -10.1) ⚠ transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -9.1) |
| [[BT-474 (line)]] | alt | 466 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.0) | — |
| [[C32 (line)]] | wt | 95.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.62× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 68.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 168 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.95× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -14.1) |
| [[J82 (line)]] | alt | 74.7 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.12× (z +10.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.98× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 141 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 125 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.42× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 76.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +19.4) | — |
| [[NCI-H460 (line)]] | wt | 222 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 79.4 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.98× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 220 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -14.2) |
| [[SNU-423 (line)]] | alt | 105 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.09× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.4) |
| [[A-427 (line)]] | wt | 208 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.09× (z +9.0) | — |
| [[A498 (line)]] | wt | 82.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.02× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 250 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.1) |
| [[HS-578T (line)]] | alt | 30.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.58× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 77.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.18× (z +8.7) | — |
| [[NCI-H661 (line)]] | alt | 299 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 51.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +9.7) | — |
| [[A-172 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 24.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 27.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 14.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA7]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[GCFC2]] | +0.68 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[SLC25A13]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MGA]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[DPH6]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FKTN]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ZNF480]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RRP15]] | +0.59 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[ZNF260]] | +0.59 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[POGK]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[CEP83]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | -0.66 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.62 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[COG7]] | -0.60 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[APAF1]] | -0.60 | -0.71 / -0.49 | both halves | 1e-05 |  |
| [[MED26]] | -0.60 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[PMS2P4-1]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[RAB40C]] | -0.58 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[ZNHIT1]] | -0.57 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[HELZ]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ALKBH5]] | -0.57 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[SPAG4]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SPICE1]] | -0.57 | -0.64 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF480]] | C | ZNF480 activity raises DNAH14's level | lines that do not express ZNF480 (3) vs lines expressing it (47) | 5.99× lower at baseline in the lines without ZNF480 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF260]] | B | DNAH14 activity raises ZNF260's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 3.04× lower at baseline in the lines without DNAH14 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |
| [[ZNF254]] | B | DNAH14 activity raises ZNF254's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without DNAH14 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |
| [[SMAP2]] | B | DNAH14 activity raises SMAP2's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 1.28× lower at baseline in the lines without DNAH14 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |
| [[VDAC1P8]] | B | DNAH14 activity raises VDAC1P8's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 1.21× lower at baseline in the lines without DNAH14 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |
| [[AIG1]] | B | DNAH14 activity raises AIG1's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without DNAH14 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |
| [[NARF]] | B | DNAH14 activity raises NARF's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without DNAH14 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (4.0, -38.8); signed map (7.8, -45.3). **Vector** length 124, 40.7% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +7.1 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +8.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.5 | -12.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.1 | -1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:224,896,262-225,399,292 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dnahc14, HL-18, HL18, DKFZp781B1548, MGC27277; previously C1orf67 |
| Gene groups (HGNC) | Dyneins, axonemal inner arm I1/f complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VDD8](https://www.uniprot.org/uniprotkb/Q0VDD8) (Dynein axonemal heavy chain 14):

> Force generating protein of respiratory cilia. Produces force towards the minus ends of microtubules. Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP. Involved in sperm motility; implicated in sperm flagellar assembly (By similarity).

**Summary**, from NCBI Gene [127602](https://www.ncbi.nlm.nih.gov/gene/127602):

> Dyneins are microtubule-associated motor protein complexes composed of several heavy, light, and intermediate chains. Two major classes of dyneins, axonemal and cytoplasmic, have been identified. DNAH14 is an axonemal dynein heavy chain (DHC) (Vaughan et al., 1996 [PubMed 8812413]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:2945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2945) · Entrez [127602](https://www.ncbi.nlm.nih.gov/gene/127602) · UniProt [Q0VDD8](https://www.uniprot.org/uniprotkb/Q0VDD8) · Ensembl [ENSG00000185842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185842)

## Data

Gene col 11740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11740); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11740]; `tensor/DDL_lfc|DDL_z.npy` [11740]; `embed/gene_vectors.npy` [11740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11740 or target_col == 11740). Every well: [[DNAH14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
