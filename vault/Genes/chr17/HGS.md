---
symbol: "HGS"
type: "gene"
col: 11668
ensembl_id: "ENSG00000185359"
name: "hepatocyte growth factor-regulated tyrosine kinase substrate"
location: "17q25.3"
module: 2
arm: "+"
pooled_cpm: 65.28
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# HGS

*hepatocyte growth factor-regulated tyrosine kinase substrate* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.73× (z +9.3, q 6e-18, up in 39 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.73× (z +9.3, q 6e-18, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.769× (z -6.2, q 3e-07, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.162×; ⚠ toxic; cell-cycle shift, explains ~32% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOT2]] (+0.66, fdr 7e-06), [[ARL16]] (+0.64, fdr 1e-05, ⚠ same locus), [[NPIPA1]] (+0.62, fdr 1e-05), [[TAF1C]] (+0.62, fdr 1e-05); moves opposite to [[ADAM22]] (-0.49, fdr 3e-05), [[NFIA]] (-0.48, fdr 4e-05), [[TRERF1]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.73×** | +9.3 | 6e-18 | 39/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +9.3 | 6e-18 | 42/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +9.1 | 3e-17 | 45/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.59×** | +7.5 | 8e-12 | 32/42 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +7.5 | 8e-12 | 39/48 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +5.6 | 2e-06 | 32/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.0 | 4e-05 | 27/48 (SHP-77, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 2e-04 | 30/48 (PANC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.7 | 2e-04 | 31/48 (KATO III, NCI-H23, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +4.2 | 0.001 | 21/49 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.20×** | +4.2 | 0.001 | 23/48 (SHP-77, HOP62, …) | all doses, flat | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +4.2 | 0.002 | 32/48 (SW480, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.27×** | +4.1 | 0.002 | 23/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.27×** | +4.1 | 0.002 | 21/48 (HepG2/C3A, C32, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.26×** | +3.9 | 0.003 | 22/47 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.005 | 24/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.008 | 19/47 (HS-578T, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.020 | 18/47 (NCI-H1792, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.050 | 9/48 (NCI-H23, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.052 | 15/47 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.47×** | +3.0 | 0.055 | 12/48 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11668.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.162×; ⚠ toxic; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.769×** | -6.2 | 3e-07 | 35/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.712×** | -4.3 | 0.006 | 23/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | 0.811× | -3.4 | 0.12 | 19/48 (LS 180, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 70.5 | 5 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 62.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[BT-474 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 34.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.8) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[NCI-H23 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 99.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOT2]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ARL16]] | +0.64 | +0.64 / +0.50 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NPIPA1]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TAF1C]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TPD52L2]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TEPSIN]] | +0.61 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CEP170B]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[UCKL1]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 | same gene group |
| [[SBF1]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[FAM219A]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SGTA]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ANAPC2]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM22]] | -0.49 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[NFIA]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TRERF1]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-11.8, -24.2); signed map (-25.3, 0.6). **Vector** length 92.0, 27.4% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.9 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.6 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -1.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | hepatocyte growth factor-regulated tyrosine kinase substrate |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,683,326-81,703,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hrs, ZFYVE8, Vps27 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; ESCRT-0; MicroRNA protein coding host genes |
| Reactome | 26 pathways, smallest: Prevention of phagosomal-lysosomal fusion; RHOBTB3 ATPase cycle; Suppression of phagosomal maturation |
| Matched by | ensembl_id |

**Function**, from UniProt [O14964](https://www.uniprot.org/uniprotkb/O14964) (Hepatocyte growth factor-regulated tyrosine kinase substrate):

> Involved in intracellular signal transduction mediated by cytokines and growth factors. When associated with STAM, it suppresses DNA signaling upon stimulation by IL-2 and GM-CSF. Could be a direct effector of PI3-kinase in vesicular pathway via early endosomes and may regulate trafficking to early and late endosomes by recruiting clathrin. May concentrate ubiquitinated receptors within clathrin-coated regions. Involved in down-regulation of receptor tyrosine kinase via multivesicular body …

**Summary**, from NCBI Gene [9146](https://www.ncbi.nlm.nih.gov/gene/9146):

> The protein encoded by this gene regulates endosomal sorting and plays a critical role in the recycling and degradation of membrane receptors. The encoded protein sorts monoubiquitinated membrane proteins into the multivesicular body, targeting these proteins for lysosome-dependent degradation. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:4897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4897) · Entrez [9146](https://www.ncbi.nlm.nih.gov/gene/9146) · UniProt [O14964](https://www.uniprot.org/uniprotkb/O14964) · Ensembl [ENSG00000185359](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185359)

## Data

Gene col 11668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11668); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11668]; `tensor/DDL_lfc|DDL_z.npy` [11668]; `embed/gene_vectors.npy` [11668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11668 or target_col == 11668). Every well: [[HGS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HGS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
