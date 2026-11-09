---
symbol: "VPS33B"
type: "gene"
col: 11486
ensembl_id: "ENSG00000184056"
name: "VPS33B late endosome and lysosome associated"
location: "15q26.1"
module: 65
arm: "+"
pooled_cpm: 10.53
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# VPS33B

*VPS33B late endosome and lysosome associated* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.78× (z +9.5, q 2e-18, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.571× (z -9.2, q 3e-17, down in 24 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.823× (z -4.4, q 0.002, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HARS2]] (+0.75, fdr 7e-06), [[MINDY3]] (+0.69, fdr 1e-05), [[TBC1D13]] (+0.69, fdr 7e-06); moves opposite to [[NFATC1]] (-0.65, fdr 1e-05), [[TRIM72]] (-0.60, fdr 1e-05), [[PILRA]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +9.5 | 2e-18 | 32/47 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +9.3 | 3e-18 | 30/47 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +9.0 | 6e-17 | 32/48 (LoVo, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +8.6 | 8e-16 | 29/47 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +5.7 | 2e-06 | 15/47 (RKO, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +5.2 | 1e-05 | 15/46 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.0 | 6e-05 | 17/47 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.8 | 1e-04 | 8/20 (SW1417, A-172, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.003 | 12/42 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.005 | 10/45 (A498, CHP-212, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.008 | 12/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.010 | 5/46 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.3 | 0.040 | 8/47 (KATO III, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.571×** | -9.2 | 3e-17 | 24/35 (HS-578T, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -6.1 | 4e-07 | 12/19 (A498, J82, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -4.4 | 0.002 | 16/48 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.782×** | -4.0 | 0.009 | 11/47 (AN3 CA, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.100 | 14/46 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.821× | -3.2 | 0.13 | 11/47 (NCI-H460, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0659× (z -15.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.88 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0988× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0856× (z -10.0) |
| [[Hs 766T (line)]] | wt | 8.28 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.133× (z -9.0) |
| [[HS-578T (line)]] | alt | 6.97 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0610× (z -12.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 7.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.12 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 8.06 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.107× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -12.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HARS2]] | +0.75 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[MINDY3]] | +0.69 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D13]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[RTCA]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[USP30]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[SNX4]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[JKAMP]] | +0.67 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[ALG9]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NDUFB7]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZNF112]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[MED23]] | +0.65 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CDADC1]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFATC1]] | -0.65 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TRIM72]] | -0.60 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PILRA]] | -0.58 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[INTS6]] | -0.57 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[KDSR]] | -0.57 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SLIT2]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SEMA4A]] | -0.57 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[TEX14]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[LINC00910]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SKIL]] | -0.56 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[IQCN]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[NLGN3]] | -0.55 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.6, -11.2); signed map (-31.7, -11.7). **Vector** length 71.5, 11.8% of its response variance represented; |z| ≥ 3 in 814 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.6 | +9.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.1 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.0 | +9.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.5 | +8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | VPS33B late endosome and lysosome associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,998,673-91,022,603 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14848 |
| Gene groups (HGNC) | SM family of SNARE chaperones |
| Reactome | 10 pathways, smallest: Prevention of phagosomal-lysosomal fusion; SARS-CoV-2 modulates autophagy; Suppression of phagosomal maturation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H267](https://www.uniprot.org/uniprotkb/Q9H267) (Vacuolar protein sorting-associated protein 33B):

> May play a role in vesicle-mediated protein trafficking to lysosomal compartments and in membrane docking/fusion reactions of late endosomes/lysosomes. Required for proper trafficking and targeting of the collagen-modifying enzyme lysyl hydroxylase 3 (LH3) to intracellular collagen. Mediates phagolysosomal fusion in macrophages. Proposed to be involved in endosomal maturation implicating VIPAS39. In epithelial cells, the VPS33B:VIPAS39 complex may play a role in the apical recycling pathway and …

**Summary**, from NCBI Gene [26276](https://www.ncbi.nlm.nih.gov/gene/26276):

> Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene is a member of the Sec-1 domain family, and encodes the human ortholog of rat Vps33b which is homologous to the yeast class C Vps33 protein. The mammalian class C vacuolar protein sorting proteins are predominantly associated with …

**Accessions** — [HGNC:12712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12712) · Entrez [26276](https://www.ncbi.nlm.nih.gov/gene/26276) · UniProt [Q9H267](https://www.uniprot.org/uniprotkb/Q9H267) · Ensembl [ENSG00000184056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184056)

## Data

Gene col 11486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11486); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11486]; `tensor/DDL_lfc|DDL_z.npy` [11486]; `embed/gene_vectors.npy` [11486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11486 or target_col == 11486). Every well: [[VPS33B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS33B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
