---
symbol: "DYNC2I1"
type: "gene"
col: 4775
ensembl_id: "ENSG00000126870"
name: "dynein 2 intermediate chain 1"
location: "7q36.3"
module: 20
arm: "-"
pooled_cpm: 173.98
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# DYNC2I1

*dynein 2 intermediate chain 1* — 7q36.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 2.10×, RKO 2.24×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 1.47×, RKO 2.03×); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 2.36×); [[Triamcinolone (drug)]] 5 µM in 1 line (NCI-H1573 1.77×).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.492× (z -14.7, q 0e+00, down in 42 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.586× (z -11.5, q 3e-28, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESYT2]] (+0.62, fdr 1e-05, ⚠ same locus), [[NPHP3]] (+0.58, fdr 1e-05), [[NOL3]] (+0.56, fdr 1e-05), [[SAP30]] (+0.55, fdr 1e-05); moves opposite to [[B3GALNT1]] (-0.57, fdr 2e-05), [[EMB]] (-0.55, fdr 2e-05), [[TMSB15B]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TSC22D3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ESYT2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4775.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 2.10×, RKO 2.24×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 1.47×, RKO 2.03×); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 2.36×); [[Triamcinolone (drug)]] 5 µM in 1 line (NCI-H1573 1.77×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.13× | +3.9 | 0.048 | 8/48 (COLO 205, HCT15, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.7 | 0.049 | 20/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.049 | 22/48 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.12× | +3.6 | 0.052 | 12/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.067 | 20/48 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.10 | 18/48 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.14 | 20/48 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.14 | 22/48 (A549, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -14.7 | 0e+00 | 42/47 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.586×** | -11.5 | 3e-28 | 42/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.686×** | -11.5 | 3e-28 | 33/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.371×** | -11.2 | 6e-27 | 46/49 (MIA PaCa-2, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -11.0 | 7e-26 | 43/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.603×** | -10.9 | 1e-25 | 40/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.602×** | -10.5 | 7e-24 | 31/43 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -10.2 | 1e-22 | 43/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -9.1 | 8e-18 | 44/48 (PANC-1, H4, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -8.9 | 4e-17 | 41/48 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.657×** | -8.7 | 2e-16 | 37/48 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.763×** | -8.2 | 1e-14 | 33/48 (PANC-1, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.671×** | -7.9 | 9e-14 | 34/45 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.696×** | -7.8 | 3e-13 | 35/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.703×** | -7.6 | 1e-12 | 30/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -7.1 | 5e-11 | 37/48 (HT-29, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.741×** | -6.1 | 4e-08 | 36/48 (NCI-H1573, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.786×** | -5.2 | 6e-06 | 31/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -5.0 | 1e-05 | 21/49 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 250 | 2 | 18 (7 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.36× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -23.6) |
| [[NCI-H460 (line)]] | wt | 255 | 0 | 17 (11 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.289× (z -19.2) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.455× (z -12.7) |
| [[C32 (line)]] | wt | 311 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -22.6) |
| [[H4 (line)]] | wt | 192 | 0 | 13 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -16.8) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.267× (z -13.5) |
| [[KATO III (line)]] | alt | 187 | 0 | 11 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -21.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -14.3) |
| [[LS 180 (line)]] | wt | 227 | 0 | 10 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -14.8) |
| [[SW480 (line)]] | alt | 261 | 0 | 10 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.299× (z -17.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.377× (z -14.9) |
| [[BT-474 (line)]] | alt | 175 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -16.2) |
| [[SNU-423 (line)]] | alt | 192 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -19.6) |
| [[CFPAC-1 (line)]] | alt | 166 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.424× (z -11.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.247× (z -9.9) |
| [[COLO 205 (line)]] | alt | 225 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -16.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -14.7) |
| [[Hs 766T (line)]] | wt | 264 | 0 | 7 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.320× (z -14.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.527× (z -12.2) |
| [[HT-29 (line)]] | alt | 199 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.392× (z -12.1) |
| [[LoVo (line)]] | wt | 325 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -26.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.429× (z -13.5) |
| [[HS-578T (line)]] | alt | 139 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -17.4) |
| [[MIA PaCa-2 (line)]] | alt | 227 | 0 | 6 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.167× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 100.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 179 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -18.3) |
| [[PANC-1 (line)]] | alt | 169 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.475× (z -12.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -12.2) |
| [[HCT15 (line)]] | alt | 296 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -19.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.347× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 190 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.375× (z -12.1) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.211× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 164 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.7) |
| [[SW 900 (line)]] | alt | 163 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.437× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -8.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HOP62 (line)]] | alt | 158 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.310× (z -14.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.349× (z -10.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.4) |
| [[RKO (line)]] | wt | 65.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.395× (z -10.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.451× (z -9.1) |
| [[A498 (line)]] | wt | 97.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.494× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 197 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 80.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -10.6) |
| [[J82 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.502× (z -8.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 194 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.606× (z -8.9) |
| [[SW1417 (line)]] | alt | 173 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.615× (z -8.5) |
| [[SW48 (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.394× (z -9.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 163 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 219 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESYT2]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 | STRING 717; ⚠ same locus (26.3 kb: neighbours can correlate without regulation) |
| [[NPHP3]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 | same gene group; pathway: Assembly of the 9+0 primary cilium |
| [[NOL3]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[SAP30]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[GPATCH1]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ZNF395]] | +0.52 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[GGNBP2]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ARID4A]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[INAFM1]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ZNF654]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TRIM7-AS2]] | +0.51 | +0.37 / +0.55 | both halves | 9e-05 |  |
| [[GIGYF2]] | +0.51 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[HMGCL]] | +0.50 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALNT1]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[EMB]] | -0.55 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TMSB15B]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[GLO1]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[RFX5]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CDYL]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TMEM98]] | -0.50 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[HAGLR]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RNF2]] | -0.49 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[KBTBD11]] | -0.49 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[TMEM33]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TUSC3]] | -0.48 | -0.36 / -0.56 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSC22D3]] | B | TSC22D3 activity strengthens DYNC2I1's drug response | lines that do not express TSC22D3 (11) vs lines expressing it (38) | the lines without TSC22D3 respond 0.66× as strongly (z diff +2.26); strongest at Digitoxin 5 µM: 0.75x vs 0.52x (z diff +3.8) | 0.020 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DHRS3]] | B | DHRS3 activity raises DYNC2I1's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without DHRS3 | 0.051 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESYT2]] | C | DYNC2I1's natural level strengthens ESYT2's drug response | DYNC2I1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.33; direction not clear | 0.027 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.386). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.6, -32.2); signed map (-31.6, 26.6). **Vector** length 111, 38.0% of its response variance represented; |z| ≥ 3 in 1,567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Triamcinolone (drug)]] 5 µM |  | +4.5 | +3.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.9 | +2.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.8 | +3.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.7 | +3.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.5 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.6 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.6 | -7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.1 | -5.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | dynein 2 intermediate chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:158,856,558-158,956,747 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10300, FAP163, CFAP163, DIC6; previously WDR60 |
| Gene groups (HGNC) | WD repeat domain containing; Cilia and flagella associated; Dynein 2 complex subunits; Dynein intermediate chains |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVS4](https://www.uniprot.org/uniprotkb/Q8WVS4) (Cytoplasmic dynein 2 intermediate chain 1):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 2 complex (dynein-2 complex), a motor protein complex that drives the movement of cargos along microtubules within cilia and flagella in concert with the intraflagellar transport (IFT) system. DYNC2I1 plays a major role in retrograde ciliary protein trafficking in cilia and flagella. Also requires to maintain a functional transition zone.

**Summary**, from NCBI Gene [55112](https://www.ncbi.nlm.nih.gov/gene/55112):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD) and may facilitate the formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes including cell cycle progression, signal transduction, apoptosis, and gene regulation. The encoded protein contains four WD repeats and may play a role in the …

**Accessions** — [HGNC:21862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21862) · Entrez [55112](https://www.ncbi.nlm.nih.gov/gene/55112) · UniProt [Q8WVS4](https://www.uniprot.org/uniprotkb/Q8WVS4) · Ensembl [ENSG00000126870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126870)

## Data

Gene col 4775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4775); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4775]; `tensor/DDL_lfc|DDL_z.npy` [4775]; `embed/gene_vectors.npy` [4775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4775 or target_col == 4775). Every well: [[DYNC2I1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC2I1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
