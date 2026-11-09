---
symbol: "SLC25A5"
type: "gene"
col: 63
ensembl_id: "ENSG00000005022"
name: "solute carrier family 25 member 5"
location: "Xq24"
module: 43
arm: "+"
pooled_cpm: 147.61
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# SLC25A5

*solute carrier family 25 member 5* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.64× (z +8.6, q 3e-15, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (A-172 6.00×, NCI-H460 4.53×, A498 4.32×, A549 5.40×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 5.16×, A498 3.85×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.658× (z -4.0, q 0.016, down in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~96% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.659× (z -4.0, q 0.016, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (A-427 0.293×, SNU-1 0.270×, HCT15 0.249×, HT-29 0.381×, …); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.387×; ⚠ cell-cycle shift, explains ~96% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NME2]] (+0.72, fdr 7e-06), [[RPLP2]] (+0.70, fdr 7e-06), [[RPS5]] (+0.69, fdr 7e-06); moves opposite to [[ZBED9]] (-0.67, fdr 2e-05), [[ZFP41]] (-0.63, fdr 1e-05), [[ACTR8]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 63.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 13 lines (A-172 6.00×, NCI-H460 4.53×, A498 4.32×, A549 5.40×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 5.16×, A498 3.85×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.64×** | +8.6 | 3e-15 | 49/49 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.98×** | +7.1 | 3e-10 | 41/44 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.34×** | +5.8 | 1e-06 | 47/48 (COLO 205, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.07×** | +4.6 | 7e-04 | 42/45 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.91×** | +4.4 | 0.001 | 44/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.6 | 0.031 | 41/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.64×** | +3.2 | 0.098 | 34/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.59× | +3.1 | 0.12 | 36/48 (COLO 205, KATO III, …) | all doses, flat | composition shift |
| [[Arbutin (drug)]] 5 µM |  | 1.59× | +3.0 | 0.16 | 43/48 (A498, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 63.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (A-427 0.293×, SNU-1 0.270×, HCT15 0.249×, HT-29 0.381×, …); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.387×; ⚠ cell-cycle shift, explains ~96% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.658×** | -4.0 | 0.016 | 38/48 (A-427, HCT15, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.659×** | -4.0 | 0.016 | 31/48 (A-427, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 63. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 151 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.3) |
| [[A498 (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A549 (line)]] | wt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[C-33 A (line)]] | alt | 80.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -9.5) |
| [[HT-29 (line)]] | alt | 238 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.6) |
| [[A-172 (line)]] | wt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[COLO 205 (line)]] | alt | 70.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[HCT15 (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.2) |
| [[J82 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[KATO III (line)]] | alt | 192 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 70.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.63× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2347 (line)]] | alt | 149 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H460 (line)]] | wt | 248 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[Panc 03.27 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RKO (line)]] | wt | 139 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.9) |
| [[SNU-1 (line)]] | wt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.4) |
| [[SNU-423 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SW48 (line)]] | wt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.1) |
| [[AN3 CA (line)]] | alt | 141 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 191 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 136 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 143 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 231 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 63), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 15 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME2]] | +0.72 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[RPLP2]] | +0.70 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[RPS5]] | +0.69 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[RPS3]] ⚠ | +0.69 | +0.50 / +0.71 | both halves | 1e-05 | STRING 510; ⚠ in the vector space only through flagged drug-doses |
| [[RPS25]] | +0.68 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[RPL7A]] | +0.68 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[RPS16]] ⚠ | +0.68 | +0.56 / +0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[RPLP1]] | +0.67 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[COX5A]] ⚠ | +0.67 | +0.55 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 666; ⚠ in the vector space only through flagged drug-doses |
| [[RPS21]] | +0.67 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RPS12]] | +0.67 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[RPL13]] | +0.66 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[RPS14]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 | STRING 485 |
| [[RPL12]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBED9]] | -0.67 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ZFP41]] | -0.63 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[ACTR8]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TACO1]] | -0.63 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[ZNF408]] | -0.63 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[ZNF252P-1]] | -0.62 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ZNF621]] | -0.61 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.61 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[ZNF268]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[GDAP1]] | -0.61 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MOCS3]] | -0.60 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[ZNF655]] | -0.60 | -0.41 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-47.8, -28.3); signed map (-60.6, -2.3). **Vector** length 69.2, 33.6% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.56 to 55); *Peptide chain elongation* (reactome, mean cos +0.57 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.56 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +2.7 | +5.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | -0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.3 | -0.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -5.8 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | -5.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -5.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -5.0 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 25 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,468,422-119,471,396 (+) |
| Ensembl biotype | protein_coding |
| Also known as | T2, 2F1, T3; previously ANT2 |
| Gene groups (HGNC) | Solute carrier family 25 |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 10 pathways, smallest: Vpr-mediated induction of apoptosis by mitochondrial outer membrane permeabilization; Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane; Transport of vitamins, nucleosides, and related molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P05141](https://www.uniprot.org/uniprotkb/P05141) (ADP/ATP translocase 2):

> ADP:ATP antiporter that mediates import of ADP into the mitochondrial matrix for ATP synthesis, and export of ATP out to fuel the cell (By similarity). Cycles between the cytoplasmic-open state (c-state) and the matrix-open state (m-state): operates by the alternating access mechanism with a single substrate-binding site intermittently exposed to either the cytosolic (c-state) or matrix (m-state) side of the inner mitochondrial membrane (By similarity). In addition to its ADP:ATP antiporter …

**Summary**, from NCBI Gene [292](https://www.ncbi.nlm.nih.gov/gene/292):

> This gene is a member of the mitochondrial carrier subfamily of solute carrier protein genes. The product of this gene functions as a gated pore that translocates ADP from the cytoplasm into the mitochondrial matrix and ATP from the mitochondrial matrix into the cytoplasm. The protein forms a homodimer embedded in the inner mitochondria membrane. Suppressed expression of this gene has been shown to induce apoptosis and inhibit tumor growth. The human genome contains several non-transcribed …

**Accessions** — [HGNC:10991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10991) · Entrez [292](https://www.ncbi.nlm.nih.gov/gene/292) · UniProt [P05141](https://www.uniprot.org/uniprotkb/P05141) · Ensembl [ENSG00000005022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005022)

## Data

Gene col 63: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 63); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 63, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 63]; `tensor/DDL_lfc|DDL_z.npy` [63]; `embed/gene_vectors.npy` [63]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 63 or target_col == 63). Every well: [[SLC25A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC25A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
