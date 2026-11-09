---
symbol: "IDUA"
type: "gene"
col: 4806
ensembl_id: "ENSG00000127415"
name: "alpha-L-iduronidase"
location: "4p16.3"
module: 96
arm: "+"
pooled_cpm: 6.49
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# IDUA

*alpha-L-iduronidase* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.61× (z +4.7, q 0.001, up in 11 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 1.28× (z +3.4, q 0.074, up in 9 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.580× (z -5.4, q 5e-05, down in 22 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.750× (z -4.0, q 0.011, down in 19 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA20]] (+0.68, fdr 1e-05), [[EME2]] (+0.65, fdr 1e-05), [[SLC4A3]] (+0.65, fdr 1e-05); moves opposite to [[COX7A2]] (-0.52, fdr 2e-05, ⚠ COX7A2 in the vector space only through flagged drug-doses), [[MRPS36]] (-0.52, fdr 3e-05, ⚠ MRPS36 in the vector space only through flagged drug-doses), [[NDUFA1]] (-0.51, fdr 4e-05), [[SEC61G]] (-0.49, fdr 1e-04), [[ACTR6]] (-0.49, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +4.7 | 0.001 | 11/29 (NCI-H1573, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.6 | 0.001 | 5/17 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.48×** | +3.8 | 0.023 | 14/46 (HEC-1-A, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.6 | 0.044 | 3/11 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.074 | 9/46 (PANC-1, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.074 | 11/46 (RKO, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +3.3 | 0.087 | 12/45 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.39× | +3.1 | 0.15 | 8/39 (NCI-H460, CFPAC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.580×** | -5.4 | 5e-05 | 22/40 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.641×** | -4.4 | 0.003 | 20/44 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.750×** | -4.0 | 0.011 | 19/38 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.677×** | -3.6 | 0.041 | 17/41 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.703×** | -3.5 | 0.057 | 15/46 (SNU-1, PANC-1, …) | all doses, flat | composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **0.713×** | -3.3 | 0.081 | 11/42 (C32, A-172, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.731× | -3.1 | 0.17 | 13/42 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.735× | -3.0 | 0.17 | 9/45 (NCI-H23, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.72 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0973× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.30 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -8.9) |
| [[J82 (line)]] | alt | 7.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0931× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LoVo (line)]] | wt | 7.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.193× (z -8.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H460 (line)]] | wt | 5.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.93 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0795× (z -8.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 9.26 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0365× (z -10.1) ⚠ cell-cycle shift, explains ~70% of this change |
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA20]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[EME2]] | +0.65 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SLC4A3]] | +0.65 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ADAMTS13]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[TKFC]] | +0.60 | +0.61 / +0.49 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[NPEPL1]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PTP4A3]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ARPIN]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ARFRP1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[GAA]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 | pathway: Diseases of carbohydrate metabolism |
| [[ATP13A1]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[OPLAH]] ⚠ | +0.57 | +0.57 / +0.53 | both halves | 1e-05 | pathway: Diseases of metabolism; ⚠ in the vector space only through flagged drug-doses |
| [[HYI]] | +0.56 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX7A2]] ⚠ | -0.52 | -0.50 / -0.46 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS36]] ⚠ | -0.52 | -0.45 / -0.50 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA1]] | -0.51 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[SEC61G]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[ACTR6]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[COX6C]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[UQCR10]] ⚠ | -0.48 | -0.43 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX8A]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ATP5MK]] | -0.47 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[COX6B1]] | -0.47 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[FBXO34]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ATP5PF]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-29.1, 24.0); signed map (18.1, -42.3). **Vector** length 59.7, 8.63% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.6 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.5 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.8 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | alpha-L-iduronidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:986,997-1,004,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MPS1, MPSI |
| Gene groups (HGNC) | Glycoside hydrolase family |
| Hallmark sets | KRAS_SIGNALING_DN, GLYCOLYSIS |
| Reactome | 9 pathways, smallest: Mucopolysaccharidoses; CS/DS degradation; HS-GAG degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P35475](https://www.uniprot.org/uniprotkb/P35475) (Alpha-L-iduronidase):

> Lysosomal hydrolase responsible for the degradation of the glycosaminoglycans heparan sulfate and dermatan sulfate.

**Summary**, from NCBI Gene [3425](https://www.ncbi.nlm.nih.gov/gene/3425):

> This gene encodes an enzyme that hydrolyzes the terminal alpha-L-iduronic acid residues of two glycosaminoglycans, dermatan sulfate and heparan sulfate. This hydrolysis is required for the lysosomal degradation of these glycosaminoglycans. Mutations in this gene that result in enzymatic deficiency lead to the autosomal recessive disease mucopolysaccharidosis type I (MPS I). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5391) · Entrez [3425](https://www.ncbi.nlm.nih.gov/gene/3425) · UniProt [P35475](https://www.uniprot.org/uniprotkb/P35475) · Ensembl [ENSG00000127415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127415)

## Data

Gene col 4806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4806); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4806]; `tensor/DDL_lfc|DDL_z.npy` [4806]; `embed/gene_vectors.npy` [4806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4806 or target_col == 4806). Every well: [[IDUA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDUA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
