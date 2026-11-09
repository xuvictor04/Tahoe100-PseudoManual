---
symbol: "MRPL10"
type: "gene"
col: 8217
ensembl_id: "ENSG00000159111"
name: "mitochondrial ribosomal protein L10"
location: "17q21.32"
module: 12
arm: "+"
pooled_cpm: 12.47
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MRPL10

*mitochondrial ribosomal protein L10* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.66× (z +12.8, q 1e-34, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.657× (z -5.5, q 2e-05, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.114×, A-172 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.0857×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.192×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.120×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOF1]] (+0.76, fdr 7e-06), [[TMEM11]] (+0.71, fdr 7e-06), [[MYG1]] (+0.69, fdr 8e-06); moves opposite to [[ARGLU1]] (-0.61, fdr 3e-05), [[FAM81A]] (-0.56, fdr 4e-05), [[ATP11C]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +12.8 | 1e-34 | 47/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +10.7 | 3e-24 | 44/47 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.72×** | +9.0 | 6e-17 | 35/47 (SW480, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +7.7 | 3e-12 | 37/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.1 | 1e-07 | 29/46 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.0 | 2e-07 | 26/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.3 | 9e-06 | 21/40 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.49×** | +5.2 | 1e-05 | 20/43 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.49×** | +5.0 | 4e-05 | 24/46 (NCI-H2030, LOX-IMVI, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.31×** | +5.0 | 4e-05 | 19/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.002 | 16/47 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.002 | 15/47 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.009 | 13/42 (NCI-H460, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.012 | 16/47 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.051 | 8/45 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.065 | 12/45 (NCI-H2030, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.069 | 12/47 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.093 | 5/45 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8217.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.114×, A-172 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (HCT15 0.0857×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.192×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.120×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.657×** | -5.5 | 2e-05 | 24/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -4.0 | 0.016 | 18/46 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.781× | -3.3 | 0.19 | 14/47 (LS 180, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.784× | -3.2 | 0.19 | 8/46 (HCT15, SW48, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 12.8 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0857× (z -10.6) |
| [[A-172 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.120× (z -8.9) |
| [[KATO III (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -9.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 15.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.11× (z +8.7) | — |
| [[A-427 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOF1]] | +0.76 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[TMEM11]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MYG1]] | +0.69 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[C18orf21]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PUS3]] | +0.67 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[ZNHIT3]] | +0.67 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZNF557]] | +0.66 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[TRAPPC5]] | +0.66 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[MRPL43]] | +0.65 | +0.51 / +0.64 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 988 |
| [[ABT1]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NKIRAS2]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARGLU1]] | -0.61 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[FAM81A]] | -0.56 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[ATP11C]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[HMGB1]] | -0.54 | -0.48 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-42.0, -7.9); signed map (-12.1, -10.5). **Vector** length 76.5, 14.3% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +12.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | +3.1 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.8 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | -0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.4 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.2 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -5.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Elagolix sodium (drug)]] 0.5 µM |  | -1.2 | -0.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,823,272-47,831,541 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPML8, MRP-L8, L10MT, MRP-L10, MRPL8, MGC17973, uL10m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q7Z7H8](https://www.uniprot.org/uniprotkb/Q7Z7H8) carries no function annotation.

**Summary**, from NCBI Gene [124995](https://www.ncbi.nlm.nih.gov/gene/124995):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14055) · Entrez [124995](https://www.ncbi.nlm.nih.gov/gene/124995) · UniProt [Q7Z7H8](https://www.uniprot.org/uniprotkb/Q7Z7H8) · Ensembl [ENSG00000159111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159111)

## Data

Gene col 8217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8217); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8217]; `tensor/DDL_lfc|DDL_z.npy` [8217]; `embed/gene_vectors.npy` [8217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8217 or target_col == 8217). Every well: [[MRPL10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
