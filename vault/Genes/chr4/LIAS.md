---
symbol: "LIAS"
type: "gene"
col: 4303
ensembl_id: "ENSG00000121897"
name: "lipoic acid synthetase"
location: "4p14"
module: 17
arm: "+"
pooled_cpm: 12.17
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# LIAS

*lipoic acid synthetase* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.75× (z +13.6, q 3e-39, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.500× (z -9.3, q 7e-18, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD17]] (+0.65, fdr 7e-06), [[FRA10AC1]] (+0.58, fdr 1e-05), [[HEATR6]] (+0.57, fdr 2e-05); moves opposite to [[CFL1]] (-0.57, fdr 2e-05), [[TP53I11]] (-0.52, fdr 3e-05), [[DDX5]] (-0.50, fdr 4e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.75×** | +13.6 | 3e-39 | 44/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.54×** | +12.5 | 2e-33 | 45/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +12.2 | 3e-32 | 19/23 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +11.9 | 3e-30 | 42/47 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +10.5 | 1e-23 | 30/37 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.6 | 5e-16 | 30/46 (NCI-H1792, SW 900, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.4 | 7e-06 | 23/47 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.3 | 1e-05 | 20/44 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +5.1 | 3e-05 | 20/47 (HT-29, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.40×** | +4.2 | 0.002 | 11/26 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.003 | 16/46 (NCI-H23, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.004 | 16/47 (HOP62, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.024 | 17/45 (KATO III, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **1.30×** | +3.4 | 0.026 | 13/40 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.29×** | +3.4 | 0.026 | 12/40 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.029 | 12/47 (A-427, LoVo, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.029 | 5/42 (SW480, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.036 | 5/47 (A-172, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +2.9 | 0.091 | 4/48 (SW 900, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.500×** | -9.3 | 7e-18 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -8.8 | 3e-16 | 36/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.571×** | -7.5 | 9e-12 | 28/46 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -7.0 | 4e-10 | 27/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -4.4 | 0.001 | 16/43 (NCI-H2030, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.560×** | -4.1 | 0.004 | 15/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.592×** | -3.7 | 0.018 | 15/45 (Panc 03.27, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.768×** | -3.6 | 0.027 | 15/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.831×** | -3.5 | 0.027 | 16/48 (SW 1271, KATO III, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.790× | -3.1 | 0.13 | 11/46 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -9.4) |
| [[C32 (line)]] | wt | 8.74 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0719× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 8.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0857× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.22 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.38× (z +8.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -10.9) |
| [[SHP-77 (line)]] | alt | 6.35 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0764× (z -9.3) |
| [[SW 900 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.79× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 18.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -8.5) |
| [[A-172 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD17]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[FRA10AC1]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[MRPL21]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.57 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[GTF2H2C]] | +0.56 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[PRMT7]] | +0.56 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[RNF20]] | +0.56 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[NOB1]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[TAMM41]] | +0.56 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[AARSD1]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ATG4C]] | +0.55 | +0.42 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL1]] | -0.57 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TP53I11]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DDX5]] | -0.50 | -0.26 / -0.58 | both halves | 4e-04 |  |
| [[SNRPB]] | -0.49 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[C2CD3]] | -0.48 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[EIF4EBP2]] | -0.48 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.511). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.4, -9.6); signed map (-26.5, -16.0). **Vector** length 58.6, 8.85% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | -9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -0.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | lipoic acid synthetase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,459,004-39,485,109 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAS |
| Gene groups (HGNC) | Radical S-adenosylmethionine domain containing |
| Reactome | 1 pathways, smallest: Protein lipoylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43766](https://www.uniprot.org/uniprotkb/O43766) (Lipoyl synthase, mitochondrial):

> Catalyzes the radical-mediated insertion of two sulfur atoms into the C-6 and C-8 positions of the octanoyl moiety bound to the lipoyl domains of lipoate-dependent enzymes, thereby converting the octanoylated domains into lipoylated derivatives.

**Summary**, from NCBI Gene [11019](https://www.ncbi.nlm.nih.gov/gene/11019):

> The protein encoded by this gene belongs to the biotin and lipoic acid synthetases family. Localized in the mitochondrion, this iron-sulfur enzyme catalyzes the final step in the de novo pathway for the biosynthesis of lipoic acid, a potent antioxidant. The deficient expression of this enzyme has been linked to conditions such as diabetes, atherosclerosis and neonatal-onset epilepsy. Alternative splicing occurs at this locus, and several transcript variants encoding distinct isoforms have been …

**Accessions** — [HGNC:16429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16429) · Entrez [11019](https://www.ncbi.nlm.nih.gov/gene/11019) · UniProt [O43766](https://www.uniprot.org/uniprotkb/O43766) · Ensembl [ENSG00000121897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121897)

## Data

Gene col 4303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4303); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4303]; `tensor/DDL_lfc|DDL_z.npy` [4303]; `embed/gene_vectors.npy` [4303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4303 or target_col == 4303). Every well: [[LIAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
