---
symbol: "COX4I1"
type: "gene"
col: 5175
ensembl_id: "ENSG00000131143"
name: "cytochrome c oxidase subunit 4I1"
location: "16q24.1"
module: 43
arm: "+"
pooled_cpm: 138.22
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# COX4I1

*cytochrome c oxidase subunit 4I1* — 16q24.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.94× (z +9.1, q 8e-17, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (SW480 5.27×, NCI-H460 5.29×, HOP62 4.98×, LoVo 4.61×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.326×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRB]] (+0.88, fdr 7e-06, ⚠ UQCRB in the vector space only through flagged drug-doses), [[RPS27A]] (+0.87, fdr 7e-06, ⚠ RPS27A in the vector space only through flagged drug-doses), [[RPS29]] (+0.86, fdr 7e-06), [[RPS19]] (+0.85, fdr 7e-06), [[RPLP2]] (+0.85, fdr 7e-06); moves opposite to [[PNPO]] (-0.69, fdr 1e-05), [[ZNF460]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 15 lines (SW480 5.27×, NCI-H460 5.29×, HOP62 4.98×, LoVo 4.61×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.94×** | +9.1 | 8e-17 | 48/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.97×** | +6.9 | 1e-09 | 44/44 (LoVo, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.45×** | +5.5 | 8e-06 | 43/45 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.06×** | +4.8 | 3e-04 | 47/48 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.91×** | +4.3 | 0.002 | 41/48 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.326×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.416× | -3.0 | 0.51 | 42/49 (BT-474, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 135 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C-33 A (line)]] | alt | 115 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 179 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 153 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 196 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[COLO 205 (line)]] | alt | 94.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 199 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 199 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H460 (line)]] | wt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 99.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 89.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 144 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 141 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 142 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 178 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 158 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 25 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRB]] ⚠ | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | +0.87 | +0.82 / +0.86 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | +0.86 | +0.78 / +0.87 | both halves | 7e-06 | STRING 432 |
| [[RPS19]] | +0.85 | +0.78 / +0.86 | both halves | 7e-06 | STRING 435 |
| [[RPLP2]] | +0.85 | +0.73 / +0.85 | both halves | 7e-06 | STRING 512 |
| [[RPL37A]] ⚠ | +0.84 | +0.76 / +0.84 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.84 | +0.70 / +0.87 | both halves | 7e-06 | STRING 403 |
| [[RPL36]] | +0.84 | +0.75 / +0.83 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.84 | +0.78 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[RPL9]] ⚠ | +0.84 | +0.72 / +0.86 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS3]] ⚠ | +0.84 | +0.71 / +0.84 | both halves | 7e-06 | STRING 616; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1E]] | +0.83 | +0.78 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 700 |
| [[TOMM7]] | +0.83 | +0.75 / +0.80 | both halves | 7e-06 | STRING 469 |
| [[RPS27]] | +0.82 | +0.69 / +0.85 | both halves | 7e-06 | STRING 421 |
| [[RPS12]] | +0.82 | +0.69 / +0.85 | both halves | 7e-06 |  |
| [[RPLP1]] | +0.82 | +0.70 / +0.83 | both halves | 7e-06 |  |
| [[RPL31]] | +0.81 | +0.65 / +0.84 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.69 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[ZNF460]] | -0.67 | -0.46 / -0.67 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.6, -24.8); signed map (-59.8, -2.7). **Vector** length 63.3, 35.0% of its response variance represented; |z| ≥ 3 in 447 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.67 to 55); *Peptide chain elongation* (reactome, mean cos +0.68 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.67 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +2.7 | +4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.3 | -0.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.3 | -0.2 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.2 | -1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | -0.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -4.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -4.5 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.4 | +9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.6 | -0.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 4I1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:85,798,633-85,807,068 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COX4-1, COXIV, COXIV-1; previously COX4 |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 10 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P13073](https://www.uniprot.org/uniprotkb/P13073) (Cytochrome c oxidase subunit 4 isoform 1, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1327](https://www.ncbi.nlm.nih.gov/gene/1327):

> Cytochrome c oxidase (COX) is the terminal enzyme of the mitochondrial respiratory chain. It is a multi-subunit enzyme complex that couples the transfer of electrons from cytochrome c to molecular oxygen and contributes to a proton electrochemical gradient across the inner mitochondrial membrane. The complex consists of 13 mitochondrial- and nuclear-encoded subunits. The mitochondrially-encoded subunits perform the electron transfer and proton pumping activities. The functions of the …

**Accessions** — [HGNC:2265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2265) · Entrez [1327](https://www.ncbi.nlm.nih.gov/gene/1327) · UniProt [P13073](https://www.uniprot.org/uniprotkb/P13073) · Ensembl [ENSG00000131143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131143)

## Data

Gene col 5175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5175); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5175]; `tensor/DDL_lfc|DDL_z.npy` [5175]; `embed/gene_vectors.npy` [5175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5175 or target_col == 5175). Every well: [[COX4I1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX4I1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
