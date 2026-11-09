---
symbol: "SH2B1"
type: "gene"
col: 10906
ensembl_id: "ENSG00000178188"
name: "SH2B adaptor protein 1"
location: "16p11.2"
module: 157
arm: "+"
pooled_cpm: 20.55
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# SH2B1

*SH2B adaptor protein 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +8.9, q 3e-16, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.779× (z -4.7, q 0.001, down in 19 of 47 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.661× (z -4.2, q 0.004, down in 15 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HCT15 0.183×, SK-MEL-2 0.253×, A-427 0.300×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.150×, NCI-H1792 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW 900 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (H4 0.0703×); [[Pralsetinib (drug)]] 5 µM in 1 line (HCT15 0.0744×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPPL1]] (+0.63, fdr 1e-05), [[FBRS]] (+0.62, fdr 1e-05), [[MED24]] (+0.62, fdr 1e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +8.9 | 3e-16 | 29/47 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.27×** | +6.6 | 1e-08 | 25/48 (AsPC-1, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.9 | 2e-04 | 19/48 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.012 | 12/47 (AsPC-1, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.012 | 13/46 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.016 | 13/48 (C-33 A, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10906.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HCT15 0.183×, SK-MEL-2 0.253×, A-427 0.300×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.150×, NCI-H1792 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW 900 0.128×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (H4 0.0703×); [[Pralsetinib (drug)]] 5 µM in 1 line (HCT15 0.0744×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.779×** | -4.7 | 0.001 | 19/47 (H4, A549, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.796×** | -4.5 | 0.002 | 19/47 (HOP62, LOX-IMVI, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.661×** | -4.2 | 0.004 | 15/46 (BT-474, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.808×** | -4.2 | 0.004 | 17/47 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.814×** | -4.0 | 0.005 | 17/47 (A-427, NCI-H460, …) | all doses, flat |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.814×** | -4.0 | 0.005 | 9/47 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.829×** | -3.7 | 0.019 | 9/48 (A-427, BT-474, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.825×** | -3.6 | 0.019 | 12/47 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.835× | -3.5 | 0.025 | 10/48 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.3 | 0.047 | 6/48 (C32, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 0.845× | -3.3 | 0.047 | 18/48 (A-427, PANC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.889× | -3.3 | 0.054 | 18/47 (RKO, PANC-1, …) | rises with dose | composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.852× | -3.2 | 0.070 | 8/48 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.853× | -3.0 | 0.093 | 14/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.897× | -3.0 | 0.093 | 9/48 (NCI-H460, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Pralsetinib (drug)]] 5 µM 0.0744× (z -8.5) |
| [[A-427 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 15.8 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0703× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -8.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPPL1]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 | same gene group; STRING 521 |
| [[FBRS]] | +0.62 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MED24]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DTX3]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PCED1A]] | +0.61 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[GSK3A]] | +0.60 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[EME2]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GPATCH3]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[STRN4]] | +0.58 | +0.62 / +0.36 | both halves | 1e-04 |  |
| [[DHX38]] | +0.57 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[WDR6]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[RAE1]] | +0.57 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.7, -21.7); signed map (22.7, -22.6). **Vector** length 60.4, 8.64% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.7 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | -0.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.8 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.7 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SH2B adaptor protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:28,846,600-28,874,212 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30542, SH2B |
| Gene groups (HGNC) | Pleckstrin homology domain containing; SH2 domain containing; SH2B adaptor protein family |
| Hallmark sets | MYOGENESIS |
| Reactome | 6 pathways, smallest: Signaling by Leptin; Prolactin receptor signaling; Growth hormone receptor signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRF2](https://www.uniprot.org/uniprotkb/Q9NRF2) (SH2B adapter protein 1):

> Adapter protein for several members of the tyrosine kinase receptor family. Involved in multiple signaling pathways mediated by Janus kinase (JAK) and receptor tyrosine kinases, including the receptors of insulin (INS), insulin-like growth factor 1 (IGF1), nerve growth factor (NGF), brain-derived neurotrophic factor (BDNF), glial cell line-derived neurotrophic factor (GDNF), platelet-derived growth factor (PDGF) and fibroblast growth factors (FGFs). In growth hormone (GH) signaling, …

**Summary**, from NCBI Gene [25970](https://www.ncbi.nlm.nih.gov/gene/25970):

> This gene encodes a member of the SH2-domain containing mediators family. The encoded protein mediates activation of various kinases and may function in cytokine and growth factor receptor signaling and cellular transformation. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:30417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30417) · Entrez [25970](https://www.ncbi.nlm.nih.gov/gene/25970) · UniProt [Q9NRF2](https://www.uniprot.org/uniprotkb/Q9NRF2) · Ensembl [ENSG00000178188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178188)

## Data

Gene col 10906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10906); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10906]; `tensor/DDL_lfc|DDL_z.npy` [10906]; `embed/gene_vectors.npy` [10906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10906 or target_col == 10906). Every well: [[SH2B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH2B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
