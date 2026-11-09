---
symbol: "CHMP1A"
type: "gene"
col: 5180
ensembl_id: "ENSG00000131165"
name: "charged multivesicular body protein 1A"
location: "16q24.3"
module: 11
arm: "+"
pooled_cpm: 27.41
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CHMP1A

*charged multivesicular body protein 1A* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.52× (z +6.4, q 1e-07, up in 31 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.71× (z +4.1, q 0.004, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.766× (z -3.9, q 0.045, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.05 µM in 1 line (SNU-1 0.0550×); [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.326×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.247×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIAS4]] (+0.66, fdr 7e-06), [[TRIR]] (+0.65, fdr 7e-06, ⚠ TRIR in the vector space only through flagged drug-doses), [[KATNIP]] (+0.62, fdr 3e-05), [[UBE2J2]] (+0.61, fdr 1e-05); moves opposite to [[CISD2]] (-0.55, fdr 2e-05), [[STRADB]] (-0.55, fdr 3e-05), [[KDM1A]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.52×** | +6.4 | 1e-07 | 31/47 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.40×** | +5.0 | 1e-04 | 25/42 (A498, PANC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.3 | 0.003 | 22/45 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.22×** | +4.3 | 0.003 | 19/47 (PANC-1, A498, …) | inconsistent across doses | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +4.1 | 0.004 | 23/45 (A498, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +4.0 | 0.005 | 20/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.007 | 19/45 (SNU-1, KATO III, …) | two highest doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.018 | 21/45 (SW 900, LS 180, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.6 | 0.018 | 16/45 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.27×** | +3.6 | 0.018 | 15/48 (SW480, SNU-1, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +3.6 | 0.018 | 15/47 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.27×** | +3.6 | 0.018 | 18/45 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.25×** | +3.4 | 0.026 | 17/47 (NCI-H460, NCI-H1573, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.34×** | +3.4 | 0.031 | 15/39 (LoVo, SW1417, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.055 | 5/48 (A498, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.097 | 11/47 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.097 | 10/48 (SW 900, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5180.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.05 µM in 1 line (SNU-1 0.0550×); [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.326×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.247×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.766×** | -3.9 | 0.045 | 22/47 (SNU-423, NCI-H1573, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.789× | -3.4 | 0.16 | 14/48 (A498, PANC-1, …) | two highest doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.771× | -3.0 | 0.45 | 6/48 (SNU-1, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.9) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[A498 (line)]] | wt | 41.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | — |
| [[Hs 766T (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.326× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 23.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.40× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0550× (z -12.4) |
| [[A-172 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIAS4]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[TRIR]] ⚠ | +0.65 | +0.59 / +0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[KATNIP]] | +0.62 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[UBE2J2]] | +0.61 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[DMPK]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[EGLN2]] | +0.59 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[SFSWAP]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ZNF324]] | +0.58 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[PIGQ]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ENDOV]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[KMT2B]] | +0.57 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SMG6]] | +0.57 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[SIRT7]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CISD2]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[STRADB]] | -0.55 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[KDM1A]] | -0.54 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[PGM2]] | -0.53 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PAICS]] | -0.53 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[UBA5]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MATR3]] | -0.52 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SELENOF]] | -0.52 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[SLC35G1]] | -0.52 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[SLC25A30]] | -0.52 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[FAM136A]] | -0.51 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[PPP1CB]] | -0.51 | -0.48 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.270). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-27.8, -12.3); signed map (-18.5, 2.3). **Vector** length 70.0, 15.2% of its response variance represented; |z| ≥ 3 in 479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.7 | +6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.9 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +2.9 | +4.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.8 | -3.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,640,816-89,657,738 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0047, CHMP1, Vps46A; previously PRSM1, PCOLN3 |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III associated factors |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 3 pathways, smallest: HCMV Late Events; HCMV Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD42](https://www.uniprot.org/uniprotkb/Q9HD42) (Charged multivesicular body protein 1a):

> Probable peripherally associated component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal …

**Summary**, from NCBI Gene [5119](https://www.ncbi.nlm.nih.gov/gene/5119):

> This gene encodes a member of the CHMP/Chmp family of proteins which are involved in multivesicular body sorting of proteins to the interiors of lysosomes. The initial prediction of the protein sequence encoded by this gene suggested that the encoded protein was a metallopeptidase. The nomenclature has been updated recently to reflect the correct biological function of this encoded protein. Several transcripts encoding different isoforms have been found for this gene. [provided by RefSeq, Dec …

**Accessions** — [HGNC:8740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8740) · Entrez [5119](https://www.ncbi.nlm.nih.gov/gene/5119) · UniProt [Q9HD42](https://www.uniprot.org/uniprotkb/Q9HD42) · Ensembl [ENSG00000131165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131165)

## Data

Gene col 5180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5180); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5180]; `tensor/DDL_lfc|DDL_z.npy` [5180]; `embed/gene_vectors.npy` [5180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5180 or target_col == 5180). Every well: [[CHMP1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
