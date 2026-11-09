---
symbol: "RFC1"
type: "gene"
col: 434
ensembl_id: "ENSG00000035928"
name: "replication factor C subunit 1"
location: "4p14"
module: 17
arm: "+"
pooled_cpm: 119.43
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# RFC1

*replication factor C subunit 1* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.88× (z +15.1, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.82× (z +13.0, q 2e-36, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.682× (z -13.0, q 9e-36, down in 40 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A498 0.411×, HOP62 0.388×, A-172 0.419×, NCI-H460 0.458×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.483×, CFPAC-1 0.633×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.213×; ⚠ toxic).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH11]] (+0.73, fdr 1e-05), [[POT1]] (+0.69, fdr 3e-05), [[THYN1]] (+0.67, fdr 1e-05); moves opposite to [[GCNT4]] (-0.64, fdr 8e-05), [[SPON1-AS1]] (-0.61, fdr 4e-05), [[RCC1]] (-0.58, fdr 6e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.88×** | +15.1 | 0e+00 | 48/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.80×** | +14.1 | 5e-43 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.82×** | +13.0 | 2e-36 | 47/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.72×** | +13.0 | 2e-36 | 48/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +5.7 | 1e-06 | 31/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.50×** | +5.1 | 3e-05 | 36/47 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.7 | 2e-04 | 30/49 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.20×** | +4.4 | 8e-04 | 23/48 (A-427, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.19× | +4.1 | 0.002 | 23/48 (PANC-1, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.002 | 18/48 (A498, Panc 03.27, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.1 | 0.002 | 10/48 (PANC-1, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.006 | 18/48 (A498, J82, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | 1.15× | +3.4 | 0.025 | 19/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.10× | +3.4 | 0.029 | 5/48 (A-427, RKO, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.15× | +3.1 | 0.064 | 9/49 (A-427, HOP62, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.096 | 9/48 (CFPAC-1, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 434.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A498 0.411×, HOP62 0.388×, A-172 0.419×, NCI-H460 0.458×, …); [[Homoharringtonine (drug)]] 5 µM in 2 lines (AsPC-1 0.483×, CFPAC-1 0.633×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.213×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -13.0 | 9e-36 | 40/49 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -6.2 | 1e-07 | 25/47 (HepG2/C3A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -4.5 | 0.001 | 13/48 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.5 | 0.063 | 21/48 (A498, HOP62, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.875× | -3.2 | 0.14 | 14/47 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.830× | -3.2 | 0.14 | 15/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 177 | 3 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.71× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 84.0 | 4 (3 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 2.19× (z +11.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.13× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -16.4) |
| [[A-427 (line)]] | wt | 145 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.86× (z +9.2) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 69.1 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.30× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 91.9 | 1 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -14.1) |
| [[LoVo (line)]] | wt | 108 | 4 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.36× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 105 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +12.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.15× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 118 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +10.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.06× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 83.2 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +12.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.25× (z +9.2) | — |
| [[RKO (line)]] | wt | 125 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.67× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -13.0) |
| [[A498 (line)]] | wt | 178 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.64× (z +8.9) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -22.5) |
| [[BT-474 (line)]] | alt | 91.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +10.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[LOX-IMVI (line)]] | wt | 66.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.26× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.60× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 72.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 163 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 1.96× (z +10.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[CFPAC-1 (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.633× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 124 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.10× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.02× (z +9.6) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 138 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.32× (z +10.5) | — |
| [[A-172 (line)]] | wt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -17.3) |
| [[C32 (line)]] | wt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.4) |
| [[H4 (line)]] | wt | 147 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 90.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.213× (z -14.3) ⚠ toxic |
| [[HOP62 (line)]] | alt | 119 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -19.0) |
| [[HT-29 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 128 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.98× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 98.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -9.0) |
| [[SNU-1 (line)]] | wt | 135 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.07× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -9.2) |
| [[SW 900 (line)]] | alt | 200 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -11.9) |
| [[AN3 CA (line)]] | alt | 172 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 104 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | +0.73 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[POT1]] | +0.69 | +0.68 / +0.43 | both halves | 3e-05 | pathway: Base Excision Repair; STRING 509 |
| [[THYN1]] | +0.67 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RNF20]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PARP2]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 | pathway: Base Excision Repair |
| [[SKIC3]] | +0.62 | +0.65 / +0.31 | both halves | 2e-04 |  |
| [[HAUS4]] | +0.62 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[RAD17]] | +0.61 | +0.57 / +0.41 | both halves | 4e-05 | pathway: DNA Double-Strand Break Repair; STRING 869 |
| [[HEATR6]] | +0.61 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[ALAD]] | +0.61 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[NDUFA12]] | +0.61 | +0.52 / +0.31 | both halves | 2e-04 |  |
| [[MRPS31P4]] | +0.61 | +0.62 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT4]] | -0.64 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[SPON1-AS1]] | -0.61 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[RCC1]] | -0.58 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[CSRNP2]] | -0.57 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[NACC2]] | -0.57 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[LINC01829]] | -0.57 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.56 | -0.44 / -0.20 | both halves | 7e-04 |  |
| [[TLNRD1]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ZNF124]] | -0.56 | -0.48 / -0.23 | both halves | 5e-04 |  |
| [[CROCC]] | -0.56 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[CCDC17]] | -0.56 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[EPM2A]] | -0.55 | -0.46 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RFC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[VTA1]] | C | VTA1's natural level weakens RFC1's drug response | VTA1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.51; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-2.6, -8.3); signed map (-28.5, -10.9). **Vector** length 133, 41.0% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +8.8 | +14.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +8.8 | +13.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.7 | +15.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +13.0 |
|  | [[NG25 (drug)]] 5 µM |  | +4.5 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -13.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.6 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[Ivermectin (drug)]] 5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | replication factor C subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,287,456-39,366,375 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A1, PO-GA, RFC140, MHCBFB |
| Gene groups (HGNC) | AAA ATPases; Replication factor C |
| Hallmark sets | MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 44 pathways, smallest: Leading Strand Synthesis; Polymerase switching; Translesion synthesis by REV1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P35251](https://www.uniprot.org/uniprotkb/P35251) (Replication factor C subunit 1):

> Subunit of the replication factor C (RFC) complex which acts during elongation of primed DNA templates by DNA polymerases delta and epsilon, and is necessary for ATP-dependent loading of proliferating cell nuclear antigen (PCNA) onto primed DNA. This subunit binds to the primer-template junction. Binds the PO-B transcription element as well as other GA rich DNA sequences. Can bind single- or double-stranded DNA.

**Summary**, from NCBI Gene [5981](https://www.ncbi.nlm.nih.gov/gene/5981):

> This gene encodes the large subunit of replication factor C, a five subunit DNA polymerase accessory protein, which is a DNA-dependent ATPase required for eukaryotic DNA replication and repair. The large subunit acts as an activator of DNA polymerases, binds to the 3' end of primers, and promotes coordinated synthesis of both strands. It may also have a role in telomere stability. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by …

**Accessions** — [HGNC:9969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9969) · Entrez [5981](https://www.ncbi.nlm.nih.gov/gene/5981) · UniProt [P35251](https://www.uniprot.org/uniprotkb/P35251) · Ensembl [ENSG00000035928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035928)

## Data

Gene col 434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 434); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 434]; `tensor/DDL_lfc|DDL_z.npy` [434]; `embed/gene_vectors.npy` [434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 434 or target_col == 434). Every well: [[RFC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
