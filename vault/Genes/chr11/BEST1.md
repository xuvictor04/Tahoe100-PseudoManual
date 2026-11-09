---
symbol: "BEST1"
type: "gene"
col: 9574
ensembl_id: "ENSG00000167995"
name: "bestrophin 1"
location: "11q12.3"
module: 21
arm: "+"
pooled_cpm: 8.24
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# BEST1

*bestrophin 1* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +10.9, q 1e-24, up in 31 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 1.63× (z +4.7, q 3e-04, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Simotinib (drug)]] 0.05 µM: 0.492× (z -5.2, q 1e-04, down in 20 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FTH1]] (+0.75, fdr 7e-06, ⚠ same locus), [[RPS18]] (+0.61, fdr 1e-05), [[RPL18A]] (+0.58, fdr 3e-05), [[TNS2-AS1]] (+0.58, fdr 1e-05); moves opposite to [[NOL11]] (-0.50, fdr 7e-05), [[TASOR2]] (-0.48, fdr 1e-04), [[FBXO45]] (-0.47, fdr 8e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +10.9 | 1e-24 | 31/32 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +9.6 | 2e-19 | 13/18 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.50×** | +8.9 | 1e-16 | 35/41 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +8.2 | 5e-14 | 26/27 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.63×** | +4.7 | 3e-04 | 23/47 (A498, LS 180, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.5 | 6e-04 | 17/47 (SW480, SNU-423, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.005 | 16/44 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.006 | 20/45 (HT-29, LoVo, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.011 | 16/44 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.70×** | +3.7 | 0.014 | 15/44 (BT-474, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.017 | 19/44 (SW1417, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.022 | 19/47 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.65×** | +3.5 | 0.022 | 15/45 (J82, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.042 | 15/43 (HEC-1-A, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.045 | 12/45 (BT-474, SW 900, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.049 | 13/45 (NCI-H2030, A498, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.05 µM |  | **1.52×** | +3.1 | 0.060 | 15/46 (SW 900, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.077 | 8/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.077 | 19/47 (J82, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Simotinib (drug)]] 0.05 µM |  | **0.492×** | -5.2 | 1e-04 | 20/43 (SW1417, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.641×** | -4.3 | 0.003 | 18/46 (HT-29, A498, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.643×** | -4.3 | 0.003 | 19/44 (SHP-77, HCT15, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.882× | -4.2 | 0.004 | 19/48 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.644×** | -4.1 | 0.004 | 16/47 (LoVo, PANC-1, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.018 | 16/47 (H4, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Ranolazine (drug)]] 0.05 µM |  | **0.704×** | -3.4 | 0.052 | 14/45 (hTERT-HPNE, CHP-212, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.616×** | -3.4 | 0.054 | 4/47 (LOX-IMVI, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Delamanid (drug)]] 0.05 µM |  | **0.715×** | -3.3 | 0.070 | 10/46 (LOX-IMVI, CHP-212, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.26 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTH1]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RPS18]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[RPL18A]] | +0.58 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[TNS2-AS1]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SNHG22]] | +0.57 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[HFM1]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[DSG2-AS1]] | +0.55 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[RPL10]] | +0.54 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[RPL41]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[PRDX5]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TALAM1]] | +0.54 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[TICAM2-AS1]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL11]] | -0.50 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[TASOR2]] | -0.48 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[FBXO45]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[SIPA1L3]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[GEMIN4]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[HAUS7]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[PDE12]] | -0.44 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[CCDC137]] | -0.44 | -0.30 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.7, -25.9); signed map (-21.3, -33.7). **Vector** length 59.0, 8.93% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -1.8 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.4 | -0.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -0.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | bestrophin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:61,950,063-61,965,515 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BMD, BEST, RP50; previously VMD2 |
| Gene groups (HGNC) | Bestrophins |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O76090](https://www.uniprot.org/uniprotkb/O76090) (Bestrophin-1):

> Ligand-gated anion channel that allows the movement of anions across cell membranes when activated by calcium (Ca2+). Allows the movement of chloride and hydrogencarbonate. Found in a partially open conformation leading to significantly smaller chloride movement. Upon F2R/PAR-1 activation, the sequestered calcium is released into the cytosol of astrocytes, leading to the (Ca2+)-dependent release of L-glutamate into the synaptic cleft that targets the neuronal postsynaptic GRIN2A/NMDAR receptor …

**Summary**, from NCBI Gene [7439](https://www.ncbi.nlm.nih.gov/gene/7439):

> This gene encodes a member of the bestrophin gene family. This small gene family is characterized by proteins with a highly conserved N-terminus with four to six transmembrane domains. Bestrophins may form chloride ion channels or may regulate voltage-gated L-type calcium-ion channels. Bestrophins are generally believed to form calcium-activated chloride-ion channels in epithelial cells but they have also been shown to be highly permeable to bicarbonate ion transport in retinal tissue. …

**Accessions** — [HGNC:12703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12703) · Entrez [7439](https://www.ncbi.nlm.nih.gov/gene/7439) · UniProt [O76090](https://www.uniprot.org/uniprotkb/O76090) · Ensembl [ENSG00000167995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167995)

## Data

Gene col 9574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9574); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9574]; `tensor/DDL_lfc|DDL_z.npy` [9574]; `embed/gene_vectors.npy` [9574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9574 or target_col == 9574). Every well: [[BEST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
