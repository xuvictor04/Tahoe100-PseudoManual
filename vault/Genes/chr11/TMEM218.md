---
symbol: "TMEM218"
type: "gene"
col: 7433
ensembl_id: "ENSG00000150433"
name: "transmembrane protein 218"
location: "11q24.2"
module: 146
arm: "+"
pooled_cpm: 5.21
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# TMEM218

*transmembrane protein 218* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.95× (z +11.5, q 5e-28, up in 7 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.52× (z +4.6, q 5e-04, up in 16 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.505× (z -10.7, q 4e-24, down in 30 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRAK1BP1]] (+0.64, fdr 1e-05), [[RPP30]] (+0.64, fdr 1e-05), [[RFXAP]] (+0.62, fdr 1e-05); moves opposite to [[C6orf62]] (-0.57, fdr 1e-05), [[RIPK1]] (-0.55, fdr 3e-05), [[TRPV1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 146]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +11.5 | 5e-28 | 7/7 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +9.0 | 7e-17 | 15/23 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +5.3 | 2e-05 | 10/15 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 5e-04 | 16/39 (HOP62, HT-29, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.5 | 6e-04 | 15/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.5 | 6e-04 | 11/46 (A549, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.013 | 7/44 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.030 | 8/45 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.035 | 9/44 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.035 | 6/25 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.074 | 6/47 (hTERT-HPNE, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.084 | 7/43 (SW480, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.1 | 0.084 | 2/48 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.084 | 2/47 (SW480, PANC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.505×** | -10.7 | 4e-24 | 30/39 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.501×** | -7.7 | 5e-12 | 27/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -5.8 | 2e-06 | 22/38 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.612×** | -5.1 | 4e-05 | 13/42 (SW1417, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.658×** | -4.6 | 4e-04 | 19/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.674×** | -4.4 | 0.001 | 16/47 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.492×** | -4.1 | 0.003 | 11/44 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -4.1 | 0.003 | 16/37 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.703×** | -3.9 | 0.006 | 17/46 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.702×** | -3.8 | 0.009 | 18/45 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.738×** | -3.4 | 0.039 | 18/38 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 8.29 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -12.8) |
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.5) |
| [[A-427 (line)]] | wt | 7.89 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 6.11 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0625× (z -12.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 6.09 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 3.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0647× (z -20.5) |
| [[NCI-H460 (line)]] | wt | 4.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -8.6) |
| [[RKO (line)]] | wt | 4.47 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0772× (z -8.5) |
| [[SW480 (line)]] | alt | 5.07 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0914× (z -12.4) |
| [[A-172 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK1BP1]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RPP30]] | +0.64 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[RFXAP]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.58 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[NDUFAF5]] | +0.58 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[OTUD6B]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TNRC6A]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[HSF2]] | +0.54 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[AIFM1]] | +0.53 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[COPS8-DT]] | +0.53 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[GSTA4]] | +0.53 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[DLX6-AS1]] | +0.52 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf62]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[RIPK1]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TRPV1]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[C21orf91-OT1]] | -0.53 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[AVIL]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[OGDH]] | -0.53 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[SLC9A1]] | -0.53 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[LINC00910]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SHPK]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CFAP251]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[PHYHD1]] | -0.51 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ADCY10P1]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.0, -12.1); signed map (-33.7, -18.3). **Vector** length 43.4, 4.70% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -5.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 218 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,094,389-125,111,763 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RU14](https://www.uniprot.org/uniprotkb/A2RU14) (Transmembrane protein 218):

> May be involved in ciliary biogenesis or function.

**Summary**, from NCBI Gene [219854](https://www.ncbi.nlm.nih.gov/gene/219854):

> Predicted to be located in cilium and membrane. Implicated in Joubert syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27344) · Entrez [219854](https://www.ncbi.nlm.nih.gov/gene/219854) · UniProt [A2RU14](https://www.uniprot.org/uniprotkb/A2RU14) · Ensembl [ENSG00000150433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150433)

## Data

Gene col 7433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7433); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7433]; `tensor/DDL_lfc|DDL_z.npy` [7433]; `embed/gene_vectors.npy` [7433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7433 or target_col == 7433). Every well: [[TMEM218 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM218.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
