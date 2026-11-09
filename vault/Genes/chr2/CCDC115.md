---
symbol: "CCDC115"
type: "gene"
col: 5891
ensembl_id: "ENSG00000136710"
name: "vacuolar ATPase assembly factor VMA22"
location: "2q21.1"
module: 130
arm: "+"
pooled_cpm: 9.65
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# CCDC115

*vacuolar ATPase assembly factor VMA22* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.42× (z +10.7, q 6e-24, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.517× (z -5.7, q 9e-06, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WBP1]] (+0.78, fdr 7e-06), [[IST1]] (+0.71, fdr 7e-06), [[DNAJC4]] (+0.70, fdr 1e-05); moves opposite to [[EEFSEC]] (-0.62, fdr 1e-05), [[PTPN11]] (-0.61, fdr 6e-05), [[UGGT2]] (-0.61, fdr 1e-05).
> It is in [[Module 130]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +10.7 | 6e-24 | 41/41 (AsPC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +7.8 | 2e-12 | 25/31 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +6.0 | 4e-07 | 31/37 (SW1417, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +5.8 | 8e-07 | 11/20 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.25×** | +4.2 | 0.002 | 24/41 (LS 180, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +4.2 | 0.002 | 21/43 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.14×** | +4.0 | 0.006 | 21/40 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.12×** | +3.9 | 0.007 | 18/44 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +3.7 | 0.012 | 15/25 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.03×** | +3.7 | 0.013 | 15/44 (HEC-1-A, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.015 | 21/44 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.050 | 18/42 (PANC-1, A498, …) | two highest doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.84×** | +3.2 | 0.060 | 10/45 (SW480, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.060 | 14/46 (KATO III, A-427, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.060 | 14/48 (AsPC-1, Hs 766T, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.062 | 17/46 (KATO III, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.517×** | -5.7 | 9e-06 | 35/46 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -5.1 | 9e-05 | 30/46 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.559×** | -5.0 | 1e-04 | 30/47 (PANC-1, NCI-H661, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -4.9 | 2e-04 | 29/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.609×** | -4.2 | 0.002 | 23/46 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.695× | -3.1 | 0.17 | 19/45 (MIA PaCa-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 5.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 9.39 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0459× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0994× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.17 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.84× (z +8.6) ⚠ position not correctable | — |
| [[SNU-1 (line)]] | wt | 9.52 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0790× (z -8.7) |
| [[SW480 (line)]] | alt | 10.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -8.7) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP1]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[IST1]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[DNAJC4]] | +0.70 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[RSRP1]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[KLC4]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[CIR1]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.65 | +0.45 / +0.78 | both halves | 3e-05 |  |
| [[CDK7]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[DCAF5]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[FBXL15]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[CCNG2]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ZNF821]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.61 | -0.38 / -0.73 | both halves | 6e-05 |  |
| [[UGGT2]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[REEP3]] | -0.61 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[CCT5]] | -0.60 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[MACROH2A1]] | -0.60 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[SACS]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.59 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[TMEM33]] | -0.59 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[CTPS1]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SPCS3]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | -0.58 | -0.48 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.9, -39.1); signed map (-10.9, 3.5). **Vector** length 76.7, 16.7% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +10.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.7 | +3.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -5.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar ATPase assembly factor VMA22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:130,337,933-130,342,699 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC12981, FLJ30131, ccp1; previously CCDC115 |
| Reactome | 4 pathways, smallest: RHOA GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NT0](https://www.uniprot.org/uniprotkb/Q96NT0) (Vacuolar ATPase assembly protein VMA22):

> Accessory component of the proton-transporting vacuolar (V)-ATPase protein pump involved in intracellular iron homeostasis. In aerobic conditions, required for intracellular iron homeostasis, thus triggering the activity of Fe(2+) prolyl hydroxylase (PHD) enzymes, and leading to HIF1A hydroxylation and subsequent proteasomal degradation. Necessary for endolysosomal acidification and lysosomal degradation. May be involved in Golgi homeostasis.

**Summary**, from NCBI Gene [84317](https://www.ncbi.nlm.nih.gov/gene/84317):

> The protein encoded by this gene has been observed to localize to the endoplasmic reticulum (ER)-Golgi intermediate compartment (ERGIC) and coat protein complex I (COPI) vesicles in some human cells. The encoded protein shares some homology with the yeast V-ATPase assembly factor Vma22p, and the orthologous protein in mouse promotes cell proliferation and suppresses cell death. Defects in this gene are a cause of congenital disorder of glycosylation, type IIo in humans. [provided by RefSeq, Mar …

**Accessions** — [HGNC:28178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28178) · Entrez [84317](https://www.ncbi.nlm.nih.gov/gene/84317) · UniProt [Q96NT0](https://www.uniprot.org/uniprotkb/Q96NT0) · Ensembl [ENSG00000136710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136710)

## Data

Gene col 5891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5891); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5891]; `tensor/DDL_lfc|DDL_z.npy` [5891]; `embed/gene_vectors.npy` [5891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5891 or target_col == 5891). Every well: [[CCDC115 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC115.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
