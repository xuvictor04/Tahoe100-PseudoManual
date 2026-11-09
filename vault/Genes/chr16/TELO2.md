---
symbol: "TELO2"
type: "gene"
col: 2015
ensembl_id: "ENSG00000100726"
name: "telomere maintenance 2"
location: "16p13.3"
module: 2
arm: "+"
pooled_cpm: 5.96
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TELO2

*telomere maintenance 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.09× (z +10.7, q 7e-24, up in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.64× (z +5.1, q 4e-05, up in 11 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.667× (z -5.7, q 9e-06, down in 18 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (NCI-H460 0.0506×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0735×); [[Naproxen (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0628×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND19]] (+0.73, fdr 7e-06), [[CHTF18]] (+0.73, fdr 7e-06), [[CDK10]] (+0.72, fdr 7e-06); moves opposite to [[TTC33]] (-0.57, fdr 5e-05), [[AK9]] (-0.56, fdr 6e-05), [[PAXIP1-AS2]] (-0.55, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.09×** | +10.7 | 7e-24 | 32/47 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.75×** | +8.1 | 2e-13 | 30/46 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.66×** | +7.3 | 6e-11 | 16/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +5.1 | 4e-05 | 11/36 (Hs 766T, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +4.3 | 0.002 | 11/45 (NCI-H23, NCI-H460, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.34×** | +4.3 | 0.002 | 10/26 (LS 180, NCI-H460, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +4.0 | 0.004 | 8/41 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.33×** | +4.0 | 0.004 | 6/35 (LoVo, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.35×** | +4.0 | 0.004 | 5/18 (HEC-1-A, SNU-423, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.31×** | +3.9 | 0.006 | 10/40 (LoVo, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.30×** | +3.7 | 0.012 | 5/11 (SNU-423, NCI-H2347, …) | all doses, flat | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.032 | 7/37 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.042 | 2/44 (SHP-77, BT-474) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.045 | 7/33 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.074 | 2/46 (C-33 A, hTERT-HPNE) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.075 | 3/39 (A498, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.081 | 4/37 (AsPC-1, SW 900, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.083 | 3/43 (SK-MEL-2, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.084 | 5/41 (A-427, HCT15, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.084 | 5/36 (SW480, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2015.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (NCI-H460 0.0506×); [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0735×); [[Naproxen (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0628×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.667×** | -5.7 | 9e-06 | 18/44 (A-172, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.744×** | -4.3 | 0.005 | 15/44 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Valdecoxib (drug)]] 0.05 µM |  | **0.760×** | -4.0 | 0.013 | 10/43 (SW48, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.842× | -3.5 | 0.056 | 16/47 (SNU-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.808× | -3.1 | 0.19 | 12/44 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.809× | -3.1 | 0.19 | 5/48 (HCT15, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.864× | -3.0 | 0.21 | 11/48 (AN3 CA, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 5.21 | 0 | 2 | — | [[Pimozide (drug)]] 0.05 µM 0.0735× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 5.99 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.0984× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 3.94 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0506× (z -13.4) |
| [[A-172 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND19]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[CHTF18]] | +0.73 | +0.65 / +0.64 | both halves | 7e-06 | STRING 572 |
| [[CDK10]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[TONSL]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[RECQL4]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TMEM201]] | +0.69 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.69 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TCF3]] | +0.69 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[TREX2]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[WDR5]] | +0.67 | +0.62 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC33]] | -0.57 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[AK9]] | -0.56 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[PAXIP1-AS2]] | -0.55 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[NQO1-DT]] | -0.55 | -0.54 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-27.2, -45.3); signed map (-47.0, -16.0). **Vector** length 60.2, 8.43% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.8 | +10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.3 | +8.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.0 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +4.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +3.3 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.0 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -5.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | telomere maintenance 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,493,344-1,510,457 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0683, hCLK2, TEL2 |
| Gene groups (HGNC) | TTT complex; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4R8](https://www.uniprot.org/uniprotkb/Q9Y4R8) (Telomere length regulation protein TEL2 homolog):

> Regulator of the DNA damage response (DDR). Part of the TTT complex that is required to stabilize protein levels of the phosphatidylinositol 3-kinase-related protein kinase (PIKK) family proteins. The TTT complex is involved in the cellular resistance to DNA damage stresses, like ionizing radiation (IR), ultraviolet (UV) and mitomycin C (MMC). Together with the TTT complex and HSP90 may participate in the proper folding of newly synthesized PIKKs. Promotes assembly, stabilizes and maintains the …

**Summary**, from NCBI Gene [9894](https://www.ncbi.nlm.nih.gov/gene/9894):

> This gene encodes a protein that functions as an S-phase checkpoint protein in the cell cycle. The protein may also play a role in DNA repair.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:29099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29099) · Entrez [9894](https://www.ncbi.nlm.nih.gov/gene/9894) · UniProt [Q9Y4R8](https://www.uniprot.org/uniprotkb/Q9Y4R8) · Ensembl [ENSG00000100726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100726)

## Data

Gene col 2015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2015); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2015]; `tensor/DDL_lfc|DDL_z.npy` [2015]; `embed/gene_vectors.npy` [2015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2015 or target_col == 2015). Every well: [[TELO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TELO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
