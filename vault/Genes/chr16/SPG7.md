---
symbol: "SPG7"
type: "gene"
col: 12487
ensembl_id: "ENSG00000197912"
name: "SPG7 matrix AAA peptidase subunit, paraplegin"
location: "16q24.3"
module: 52
arm: "+"
pooled_cpm: 116.56
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SPG7

*SPG7 matrix AAA peptidase subunit, paraplegin* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +10.7, q 4e-24, up in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (HT-29 1.90×, RKO 1.84×, KATO III 1.77×, Hs 766T 1.74×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 1.89×, COLO 205 2.50×; ⚠ cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 2.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.649× (z -9.8, q 5e-20, down in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.813× (z -5.1, q 3e-05, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD6]] (+0.61, fdr 1e-05), [[GLYR1]] (+0.58, fdr 1e-05), [[RSKR]] (+0.57, fdr 2e-05); moves opposite to [[COMMD8]] (-0.61, fdr 1e-05), [[ZNF711]] (-0.57, fdr 1e-05), [[TIGD2]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12487.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (HT-29 1.90×, RKO 1.84×, KATO III 1.77×, Hs 766T 1.74×, …); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 1.89×, COLO 205 2.50×; ⚠ cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 2.12×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +10.7 | 4e-24 | 37/49 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +6.8 | 3e-09 | 34/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +6.0 | 3e-07 | 29/48 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +5.8 | 1e-06 | 30/48 (SW480, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.23×** | +4.8 | 2e-04 | 22/48 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.20×** | +4.5 | 6e-04 | 22/48 (A549, RKO, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.19× | +4.0 | 0.005 | 19/48 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.005 | 23/48 (LOX-IMVI, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.019 | 14/48 (SNU-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.019 | 20/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.049 | 14/49 (LS 180, NCI-H1792, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.066 | 13/48 (SW1417, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 1.14× | +3.2 | 0.066 | 16/48 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.095 | 9/49 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.649×** | -9.8 | 5e-20 | 37/47 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.780×** | -8.6 | 2e-15 | 28/48 (AsPC-1, AN3 CA, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.758×** | -6.8 | 2e-09 | 27/48 (SNU-1, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.775×** | -6.3 | 5e-08 | 27/48 (HOP62, J82, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.773×** | -5.9 | 5e-07 | 30/48 (J82, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.791×** | -5.8 | 7e-07 | 28/48 (A549, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **0.801×** | -5.5 | 4e-06 | 22/48 (HCT15, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -5.1 | 3e-05 | 30/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.817×** | -5.0 | 4e-05 | 24/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.711×** | -4.4 | 6e-04 | 24/49 (A-427, AsPC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.1 | 0.002 | 23/48 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.895× | -3.9 | 0.005 | 4/48 (Hs 766T, A-172, …) | rises with dose |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.861× | -3.7 | 0.011 | 14/48 (NCI-H460, SNU-1, …) | two highest doses |  |
| [[Neratinib (drug)]] 5 µM |  | 0.863× | -3.6 | 0.012 | 17/48 (SHP-77, C-33 A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.031 | 21/48 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.793×** | -3.0 | 0.094 | 10/48 (AsPC-1, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.879× | -3.0 | 0.094 | 11/47 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 119 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.406× (z -11.2) ⚠ cell-cycle shift, explains ~62% of this change |
| [[A-427 (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -10.5) ⚠ cell-cycle shift, explains ~85% of this change |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.381× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 107 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.499× (z -11.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[Panc 03.27 (line)]] | alt | 73.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[RKO (line)]] | wt | 112 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 92.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -12.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -8.7) |
| [[A549 (line)]] | wt | 158 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.367× (z -11.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[AN3 CA (line)]] | alt | 80.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -11.4) ⚠ cell-cycle shift, explains ~85% of this change |
| [[AsPC-1 (line)]] | alt | 92.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -12.1) ⚠ cell-cycle shift, explains ~85% of this change |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.611× (z -9.3) ⚠ cell-cycle shift, explains ~85% of this change |
| [[COLO 205 (line)]] | alt | 87.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +8.6) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[H4 (line)]] | wt | 156 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -8.9) ⚠ toxic |
| [[HCT15 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.414× (z -8.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 132 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 89.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 89.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -9.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[KATO III (line)]] | alt | 111 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.7) | — |
| [[LoVo (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.426× (z -12.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.477× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[NCI-H1792 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.460× (z -9.2) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -11.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.512× (z -8.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 89.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.616× (z -8.5) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SW 900 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -9.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 92.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.89× (z +9.7) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[A-172 (line)]] | wt | 169 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 79.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 93.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[GLYR1]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[RSKR]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[DCAKD]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[FAM120B]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DAP3]] | +0.55 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[NPIPB11]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ING5]] | +0.54 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[DRD4]] | +0.54 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[DPP9]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[USP20]] | +0.53 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[MEF2B]] | +0.53 | +0.46 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD8]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ZNF711]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[TIGD2]] | -0.54 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[PTPN13]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CYP2U1]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 | STRING 540 |
| [[ISOC1]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TLR3]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CDC73]] | -0.52 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[MSRB2]] | -0.52 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ENPP4]] | -0.52 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[DUSP19]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TBL1XR1]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SPG7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-15.8, -0.5); signed map (-47.3, -0.8). **Vector** length 107, 28.8% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | +4.6 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +0.5 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +2.2 | +2.7 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | +2.0 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -7.8 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.2 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -5.9 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | SPG7 matrix AAA peptidase subunit, paraplegin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,490,719-89,557,766 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAR, SPG5C; previously CMAR |
| Gene groups (HGNC) | AAA ATPases |
| Reactome | 4 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ90](https://www.uniprot.org/uniprotkb/Q9UQ90) (Mitochondrial inner membrane m-AAA protease component paraplegin):

> Catalytic component of the m-AAA protease, a protease that plays a key role in proteostasis of inner mitochondrial membrane proteins, and which is essential for axonal and neuron development. SPG7 possesses both ATPase and protease activities: the ATPase activity is required to unfold substrates, threading them into the internal proteolytic cavity for hydrolysis into small peptide fragments (By similarity). The m-AAA protease exerts a dual role in the mitochondrial inner membrane: it mediates …

**Summary**, from NCBI Gene [6687](https://www.ncbi.nlm.nih.gov/gene/6687):

> This gene encodes a mitochondrial metalloprotease protein that is a member of the AAA family. Members of this protein family share an ATPase domain and have roles in diverse cellular processes including membrane trafficking, intracellular motility, organelle biogenesis, protein folding, and proteolysis. Mutations in this gene cause autosomal recessive spastic paraplegia 7. Two transcript variants encoding distinct isoforms have been identified. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:11237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11237) · Entrez [6687](https://www.ncbi.nlm.nih.gov/gene/6687) · UniProt [Q9UQ90](https://www.uniprot.org/uniprotkb/Q9UQ90) · Ensembl [ENSG00000197912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197912)

## Data

Gene col 12487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12487); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12487]; `tensor/DDL_lfc|DDL_z.npy` [12487]; `embed/gene_vectors.npy` [12487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12487 or target_col == 12487). Every well: [[SPG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
