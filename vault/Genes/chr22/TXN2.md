---
symbol: "TXN2"
type: "gene"
col: 1935
ensembl_id: "ENSG00000100348"
name: "thioredoxin 2"
location: "22q12.3"
module: 212
arm: "+"
pooled_cpm: 24.42
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# TXN2

*thioredoxin 2* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +11.6, q 3e-28, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +4.8, q 2e-04, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (HEC-1-A 5.08×, LoVo 4.33×, A498 4.35×, NCI-H460 4.39×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.88×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.719× (z -4.6, q 1e-03, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECD]] (+0.65, fdr 1e-05), [[DCUN1D3]] (+0.61, fdr 1e-05), [[SLC39A9]] (+0.61, fdr 1e-05); moves opposite to [[PRELID3A]] (-0.51, fdr 5e-05), [[ZNF706]] (-0.49, fdr 1e-04), [[BEND7]] (-0.49, fdr 4e-05).
> It is in [[Module 212]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1935.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (HEC-1-A 5.08×, LoVo 4.33×, A498 4.35×, NCI-H460 4.39×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.88×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.17×** | +11.6 | 3e-28 | 43/43 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.44×** | +8.6 | 2e-15 | 35/37 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.12×** | +7.0 | 6e-10 | 29/39 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.8 | 2e-04 | 31/48 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.9 | 0.011 | 27/46 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.46×** | +3.8 | 0.015 | 26/46 (KATO III, H4, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.37× | +3.1 | 0.14 | 24/48 (HOP62, HS-578T, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1935.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.719×** | -4.6 | 1e-03 | 28/47 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.629×** | -4.6 | 1e-03 | 31/48 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -4.6 | 1e-03 | 29/47 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.641×** | -4.4 | 0.001 | 30/48 (RPMI-7951, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.688×** | -3.7 | 0.020 | 27/46 (H4, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -3.7 | 0.020 | 27/47 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1935. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 39.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Digitoxin (drug)]] 5 µM 0.262× (z -10.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 21.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 30.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0576× (z -9.2) |
| [[H4 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 26.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1935), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECD]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[DCUN1D3]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC39A9]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[SYS1-DBNDD2]] | +0.56 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[SYAP1]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ARF4]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ETF1]] | +0.51 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[BSCL2]] | +0.51 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[STK19]] | +0.50 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[UBE4A]] | +0.50 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[C5AR1]] | +0.50 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[TMEM87A]] | +0.50 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3A]] | -0.51 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[ZNF706]] | -0.49 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[BEND7]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[TLCD5]] | -0.48 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[NUP50-DT]] | -0.46 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[SVIL-AS1-1]] | -0.45 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ZDHHC2]] | -0.44 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[C2orf69]] | -0.44 | -0.47 / -0.29 | both halves | 3e-04 |  |
| [[YWHAH]] | -0.44 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[ZNRF2P2]] | -0.42 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[KRAS]] | -0.42 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[VRK2]] | -0.42 | -0.46 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.4, -26.5); signed map (3.5, 27.2). **Vector** length 54.8, 10.5% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +1.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +1.3 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.1 | +0.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.4 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,467,046-36,481,640 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MT-TRX |
| Reactome | 7 pathways, smallest: Degradation of cysteine and homocysteine; Sulfur amino acid metabolism; Detoxification of Reactive Oxygen Species |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99757](https://www.uniprot.org/uniprotkb/Q99757) (Thioredoxin, mitochondrial):

> Important for the control of mitochondrial reactive oxygen species homeostasis, apoptosis regulation and cell viability Is involved in various redox reactions including the reduction of protein disulfide bonds, through the reversible oxidation of its active center dithiol to a disulfide (By similarity).

**Summary**, from NCBI Gene [25828](https://www.ncbi.nlm.nih.gov/gene/25828):

> This nuclear gene encodes a mitochondrial member of the thioredoxin family, a group of small multifunctional redox-active proteins. The encoded protein may play important roles in the regulation of the mitochondrial membrane potential and in protection against oxidant-induced apoptosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17772) · Entrez [25828](https://www.ncbi.nlm.nih.gov/gene/25828) · UniProt [Q99757](https://www.uniprot.org/uniprotkb/Q99757) · Ensembl [ENSG00000100348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100348)

## Data

Gene col 1935: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1935); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1935, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1935]; `tensor/DDL_lfc|DDL_z.npy` [1935]; `embed/gene_vectors.npy` [1935]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1935 or target_col == 1935). Every well: [[TXN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TXN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
