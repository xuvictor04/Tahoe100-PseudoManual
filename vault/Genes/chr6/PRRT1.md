---
symbol: "PRRT1"
type: "gene"
col: 12851
ensembl_id: "ENSG00000204314"
name: "proline rich transmembrane protein 1"
location: "6p21.32"
module: 35
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PRRT1

*proline rich transmembrane protein 1* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.06× (z +6.3, q 1e-07, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +6.2, q 1e-07, up in 15 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.382× (z -8.7, q 2e-15, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF821]] (+0.66, fdr 1e-05), [[IST1]] (+0.65, fdr 3e-05), [[CREB3L4]] (+0.63, fdr 2e-05); moves opposite to [[EEFSEC]] (-0.59, fdr 3e-05), [[BOP1]] (-0.56, fdr 4e-05), [[TREX2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +6.3 | 1e-07 | 2/4 (NCI-H2030, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.2 | 1e-07 | 15/33 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +5.9 | 9e-07 | 11/44 (A-427, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.9 | 1e-04 | 5/15 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +4.8 | 1e-04 | 3/11 (A-427, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.020 | 6/43 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.062 | 6/39 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.46× | +3.2 | 0.11 | 1/7 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Saquinavir (drug)]] 0.05 µM |  | 1.41× | +3.1 | 0.13 | 2/32 (SW480, Hs 766T) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.382×** | -8.7 | 2e-15 | 25/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.388×** | -8.5 | 4e-15 | 30/45 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.511×** | -6.0 | 3e-07 | 23/45 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.536×** | -5.6 | 3e-06 | 20/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -4.8 | 2e-04 | 15/24 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.618×** | -4.2 | 0.003 | 13/40 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -4.0 | 0.006 | 11/31 (Hs 766T, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.742×** | -3.8 | 0.010 | 7/42 (HepG2/C3A, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -3.7 | 0.014 | 14/39 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.675×** | -3.5 | 0.023 | 9/38 (LS 180, NCI-H23, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.679×** | -3.2 | 0.067 | 4/44 (SW48, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 0.712× | -3.1 | 0.10 | 14/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.714× | -3.0 | 0.10 | 16/44 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.715× | -3.0 | 0.10 | 4/45 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 3.20 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.05 µM 0.0401× (z -10.2) |
| [[SW480 (line)]] | alt | 3.98 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.133× (z -9.8) |
| [[HOP62 (line)]] | alt | 3.83 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0696× (z -10.2) ⚠ toxic |
| [[LoVo (line)]] | wt | 2.73 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0512× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 5.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0820× (z -9.5) |
| [[A-172 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF821]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[IST1]] | +0.65 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CREB3L4]] | +0.63 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[KMT2E]] | +0.63 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CA11]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CLK1]] | +0.60 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RELA-DT]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[RPRD2]] | +0.59 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[CCDC115]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ATP23]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SPEN-AS1]] | +0.59 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.59 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[BOP1]] | -0.56 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TREX2]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[TCOF1]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MTG1]] | -0.54 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[EFTUD2]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[NOC2L]] | -0.53 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[LAS1L]] | -0.53 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[RUVBL1]] | -0.53 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[XPO5]] | -0.52 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[CHID1]] | -0.52 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[UBE2G2]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (5.5, 24.9); signed map (39.5, -2.1). **Vector** length 42.1, 4.88% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +3.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +1.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | proline rich transmembrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,148,359-32,153,083 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NG5, IFITMD7, DSPD1, SynDIG4; previously C6orf31 |
| Gene groups (HGNC) | Dispanins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99946](https://www.uniprot.org/uniprotkb/Q99946) (Proline-rich transmembrane protein 1):

> Required to maintain a pool of extrasynaptic AMPA-regulated glutamate receptors (AMPAR) which is necessary for synapse development and function. Regulates basal AMPAR function and synaptic transmission during development but is dispensable at mature hippocampal synapses. Plays a role in regulating basal phosphorylation levels of glutamate receptor GRIA1 and promotes GRIA1 and GRIA2 cell surface expression.

**Summary**, from NCBI Gene [80863](https://www.ncbi.nlm.nih.gov/gene/80863):

> Enables identical protein binding activity. Predicted to be involved in several processes, including long-term synaptic depression; protein localization to cell surface; and regulation of AMPA receptor activity. Predicted to act upstream of or within intracellular protein localization; learning or memory; and long-term synaptic potentiation. Predicted to be located in plasma membrane and synaptic vesicle membrane. Predicted to be active in glutamatergic synapse and postsynaptic density …

**Accessions** — [HGNC:13943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13943) · Entrez [80863](https://www.ncbi.nlm.nih.gov/gene/80863) · UniProt [Q99946](https://www.uniprot.org/uniprotkb/Q99946) · Ensembl [ENSG00000204314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204314)

## Data

Gene col 12851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12851); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12851]; `tensor/DDL_lfc|DDL_z.npy` [12851]; `embed/gene_vectors.npy` [12851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12851 or target_col == 12851). Every well: [[PRRT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
