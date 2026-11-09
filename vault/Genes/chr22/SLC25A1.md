---
symbol: "SLC25A1"
type: "gene"
col: 1859
ensembl_id: "ENSG00000100075"
name: "solute carrier family 25 member 1"
location: "22q11.21"
module: 86
arm: "+"
pooled_cpm: 19.17
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# SLC25A1

*solute carrier family 25 member 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.28× (z +10.3, q 3e-22, up in 38 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +5.0, q 1e-04, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -8.6, q 4e-15, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERG28]] (+0.77, fdr 7e-06), [[TSEN34]] (+0.73, fdr 1e-05), [[MOSPD3]] (+0.67, fdr 7e-06); moves opposite to [[GCFC2]] (-0.56, fdr 2e-05), [[ST7L]] (-0.55, fdr 4e-05), [[SNHG26]] (-0.55, fdr 5e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.28×** | +10.3 | 3e-22 | 38/40 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.17×** | +6.1 | 4e-07 | 25/30 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.0 | 1e-04 | 26/46 (A549, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.75×** | +4.5 | 0.001 | 23/36 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.007 | 30/46 (HS-578T, BT-474, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.075 | 23/47 (HT-29, NCI-H23, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.46×** | +3.3 | 0.081 | 22/48 (HT-29, SW1417, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.499×** | -8.6 | 4e-15 | 37/46 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.411×** | -7.8 | 2e-12 | 36/46 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.601×** | -4.5 | 0.001 | 31/48 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.590×** | -4.4 | 0.002 | 31/46 (SW480, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.395×** | -4.2 | 0.002 | 27/47 (SNU-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.639×** | -3.9 | 0.007 | 27/46 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -3.9 | 0.007 | 28/46 (SNU-1, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -3.8 | 0.010 | 28/46 (SW 900, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -3.6 | 0.018 | 30/48 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.456×** | -3.6 | 0.018 | 23/45 (SW480, SW1417, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | 0.518× | -3.0 | 0.13 | 16/48 (BT-474, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 19.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0688× (z -11.7) |
| [[PANC-1 (line)]] | alt | 18.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A549 (line)]] | wt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 34.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.8) |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.7) |
| [[Hs 766T (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.3) |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.5) |
| [[LS 180 (line)]] | wt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -17.2) |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -10.6) |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -8.8) |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -8.5) |
| [[SW480 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -8.7) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERG28]] | +0.77 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[TSEN34]] | +0.73 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.67 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[FDFT1]] | +0.66 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[RUSC1]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ALDOC]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[GNB2]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZDHHC12]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HMGCR]] | +0.61 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SREBF2]] | +0.60 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[EBP]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCFC2]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ST7L]] | -0.55 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[SNHG26]] | -0.55 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[DPH5-DT]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MTHFD2L]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[RBM26-AS1]] | -0.52 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[NANOS3]] | -0.52 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[KRR1]] | -0.51 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[ZNF594]] | -0.51 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[YAE1]] | -0.51 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[ADGRL4]] | -0.51 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[GPATCH4]] | -0.51 | -0.52 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -47.2); signed map (-36.8, 13.4). **Vector** length 69.1, 16.3% of its response variance represented; |z| ≥ 3 in 681 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis* (reactome, mean cos +0.51 to 20); *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.51 to 17); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.51 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.3 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 25 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,175,581-19,178,739 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTP, CIC; previously SLC20A3 |
| Gene groups (HGNC) | Solute carrier family 25 |
| Hallmark sets | HYPOXIA, ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Organic anion transport by SLC5/17/25 transporters; SLC-mediated transport of organic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P53007](https://www.uniprot.org/uniprotkb/P53007) (Tricarboxylate transport protein, mitochondrial):

> Mitochondrial electroneutral antiporter that exports citrate from the mitochondria into the cytosol in exchange for malate. Also able to mediate the exchange of citrate for isocitrate, phosphoenolpyruvate, cis-aconitate and to a lesser extent trans-aconitate, maleate and succinate. Substrate exchange across the membrane occurs consecutively with one substrate being transported first, then dissociating from the substrate binding site before the second substrate binds for transport in the …

**Summary**, from NCBI Gene [6576](https://www.ncbi.nlm.nih.gov/gene/6576):

> This gene encodes a member of the mitochondrial carrier subfamily of solute carrier proteins. Members of this family include nuclear-encoded transporters that translocate small metabolites across the mitochondrial membrane. This protein regulates the movement of citrate across the inner membranes of the mitochondria. Mutations in this gene have been associated with combined D-2- and L-2-hydroxyglutaric aciduria. Pseudogenes of this gene have been identified on chromosomes 7, 11, 16, and 19. …

**Accessions** — [HGNC:10979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10979) · Entrez [6576](https://www.ncbi.nlm.nih.gov/gene/6576) · UniProt [P53007](https://www.uniprot.org/uniprotkb/P53007) · Ensembl [ENSG00000100075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100075)

## Data

Gene col 1859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1859); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1859]; `tensor/DDL_lfc|DDL_z.npy` [1859]; `embed/gene_vectors.npy` [1859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1859 or target_col == 1859). Every well: [[SLC25A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC25A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
