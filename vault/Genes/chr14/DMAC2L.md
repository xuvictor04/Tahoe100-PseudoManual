---
symbol: "DMAC2L"
type: "gene"
col: 4607
ensembl_id: "ENSG00000125375"
name: "distal membrane arm assembly component 2 like"
location: "14q21.3"
module: 1
arm: "+"
pooled_cpm: 15.0
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DMAC2L

*distal membrane arm assembly component 2 like* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +13.6, q 2e-39, up in 36 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.27× (z +4.0, q 0.009, up in 10 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.677× (z -6.6, q 3e-08, down in 24 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.521× (z -5.7, q 1e-06, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AIMP2]] (+0.70, fdr 7e-06), [[HDHD2]] (+0.67, fdr 1e-05), [[MRRF]] (+0.63, fdr 1e-05); moves opposite to [[ING2]] (-0.61, fdr 4e-05), [[NUDT22]] (-0.61, fdr 4e-05), [[RNF122]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +13.6 | 2e-39 | 36/38 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +11.9 | 2e-30 | 20/24 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +11.8 | 1e-29 | 25/31 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.009 | 10/47 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.9 | 0.009 | 13/41 (SW1417, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.009 | 11/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.051 | 4/47 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.052 | 9/47 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | 1.14× | +3.1 | 0.13 | 9/48 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | 1.42× | +3.1 | 0.13 | 3/44 (RPMI-7951, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.677×** | -6.6 | 3e-08 | 24/46 (C-33 A, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.691×** | -6.2 | 1e-07 | 26/47 (NCI-H23, PANC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.521×** | -5.7 | 1e-06 | 22/47 (SHP-77, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.712×** | -5.7 | 1e-06 | 23/45 (NCI-H23, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -4.8 | 2e-04 | 18/44 (Panc 03.27, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.662×** | -3.6 | 0.027 | 15/38 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Malotilate (drug)]] 0.05 µM |  | **0.809×** | -3.6 | 0.029 | 9/47 (C-33 A, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.829× | -3.2 | 0.11 | 11/47 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.881× | -3.0 | 0.16 | 10/47 (A-427, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.0344× (z -10.9) |
| [[A-427 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -13.9) ⚠ cell-cycle shift, explains ~12% of this change |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.0) ⚠ cell-cycle shift, explains ~12% of this change |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0865× (z -8.6) |
| [[SW48 (line)]] | wt | 18.8 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.102× (z -9.8) |
| [[SW480 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIMP2]] | +0.70 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.67 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[MRRF]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[COA7]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TEX261]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[TMBIM4]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[RNASEH1]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[GMFB]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[GUF1]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[VMA21]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ALG10B]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.58 | +0.38 / +0.52 | both halves | 7e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING2]] | -0.61 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[NUDT22]] | -0.61 | -0.43 / -0.58 | both halves | 4e-05 |  |
| [[RNF122]] | -0.61 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SMAP2]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[UBE2O]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PMM1]] | -0.59 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[SEC61G]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[NARF]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[APAF1]] | -0.58 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[ZMAT5]] | -0.57 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[COG7]] | -0.57 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[MRPL55]] | -0.57 | -0.39 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.8, -17.6); signed map (1.0, -37.3). **Vector** length 66.6, 10.5% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.7 | +3.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +3.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.3 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -1.7 | -3.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | distal membrane arm assembly component 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:50,312,324-50,335,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSU79253, ATPW; previously ATP5S |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99766](https://www.uniprot.org/uniprotkb/Q99766) (ATP synthase subunit s, mitochondrial):

> Involved in regulation of mitochondrial membrane ATP synthase. Necessary for H(+) conduction of ATP synthase. Facilitates energy-driven catalysis of ATP synthesis by blocking a proton leak through an alternative proton exit pathway.

**Summary**, from NCBI Gene [27109](https://www.ncbi.nlm.nih.gov/gene/27109):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. This gene encodes the subunit s, also known as factor B, of the proton channel. This subunit is necessary for …

**Accessions** — [HGNC:18799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18799) · Entrez [27109](https://www.ncbi.nlm.nih.gov/gene/27109) · UniProt [Q99766](https://www.uniprot.org/uniprotkb/Q99766) · Ensembl [ENSG00000125375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125375)

## Data

Gene col 4607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4607); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4607]; `tensor/DDL_lfc|DDL_z.npy` [4607]; `embed/gene_vectors.npy` [4607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4607 or target_col == 4607). Every well: [[DMAC2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMAC2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
