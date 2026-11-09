---
symbol: "RTN4IP1"
type: "gene"
col: 5056
ensembl_id: "ENSG00000130347"
name: "reticulon 4 interacting protein 1"
location: "6q21"
module: 4
arm: "+"
pooled_cpm: 7.19
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RTN4IP1

*reticulon 4 interacting protein 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.25× (z +10.2, q 1e-21, up in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +8.6, q 1e-15, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.598× (z -6.5, q 6e-08, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QRSL1]] (+0.62, fdr 7e-06, ⚠ same locus), [[ERCC8]] (+0.57, fdr 1e-05), [[NDUFA9]] (+0.56, fdr 3e-05), [[ORC5]] (+0.55, fdr 1e-05); moves opposite to [[PLXNA3]] (-0.50, fdr 1e-05), [[LINC02885]] (-0.45, fdr 2e-04), [[TPT1-AS1]] (-0.44, fdr 4e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.25×** | +10.2 | 1e-21 | 35/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.10×** | +9.3 | 4e-18 | 38/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.06×** | +9.1 | 2e-17 | 39/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.6 | 1e-15 | 25/44 (SNU-423, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +7.4 | 1e-11 | 26/41 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +6.7 | 3e-09 | 28/46 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +5.9 | 3e-07 | 22/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 9e-07 | 18/46 (HOP62, SK-MEL-2, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.60×** | +5.7 | 9e-07 | 16/34 (A-427, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.46×** | +4.5 | 3e-04 | 6/13 (NCI-H2347, SW480, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +4.3 | 8e-04 | 8/46 (PANC-1, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.003 | 8/46 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.003 | 8/45 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.37×** | +3.9 | 0.004 | 11/46 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.019 | 7/46 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.028 | 4/46 (A498, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.051 | 12/43 (A549, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.081 | 5/47 (SW1417, HOP62, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +2.9 | 0.099 | 5/46 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.099 | 3/46 (SW48, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.598×** | -6.5 | 6e-08 | 26/46 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -4.4 | 0.002 | 16/46 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.512×** | -4.4 | 0.002 | 14/37 (SHP-77, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.740×** | -3.8 | 0.023 | 12/46 (NCI-H2030, PANC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.764× | -3.2 | 0.13 | 14/37 (SHP-77, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.67 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.230× (z -9.9) |
| [[SW480 (line)]] | alt | 10.0 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.211× (z -10.4) |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0568× (z -15.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 8.57 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0684× (z -13.2) ⚠ transcription drop; cell-cycle shift, explains ~8% of this change |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0850× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 6.84 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0823× (z -9.4) |
| [[SNU-423 (line)]] | alt | 6.63 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0948× (z -9.6) |
| [[A-172 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRSL1]] | +0.62 | +0.69 / +0.63 | both halves | 7e-06 | STRING 565; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[ERCC8]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[NDUFA9]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ORC5]] | +0.55 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[LARS2]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[VWA8]] | +0.53 | +0.51 / +0.58 | both halves | 1e-05 | STRING 531 |
| [[TOMM40L]] | +0.53 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[PARG]] | +0.52 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[CPSF3]] | +0.51 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[GEMIN6]] | +0.51 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[TMLHE]] | +0.50 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[LCLAT1]] | +0.50 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[MRPS11]] | +0.50 | +0.63 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNA3]] | -0.50 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[LINC02885]] | -0.45 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[TPT1-AS1]] | -0.44 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[LASP1]] | -0.44 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[FAM117A]] | -0.44 | -0.14 / -0.48 | ⚠ not reproduced | 0.002 |  |
| [[FAM177A1]] | -0.44 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[TP53INP2]] | -0.43 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[MAP1LC3B]] | -0.42 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[ERN1]] | -0.42 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[ISYNA1]] | -0.42 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[WNT9A]] | -0.42 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.388). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.5, -1.8); signed map (-18.1, -23.1). **Vector** length 61.5, 9.26% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +2.5 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.2 | -6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | reticulon 4 interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:106,570,771-106,629,498 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Yim1, NIMP |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWV3](https://www.uniprot.org/uniprotkb/Q8WWV3) (NAD(P)H oxidoreductase RTN4IP1, mitochondrial):

> NAD(P)H oxidoreductase involved in the ubiquinone biosynthetic pathway. Required for the O-methyltransferase activity of COQ3. Able to catalyze the oxidoreduction of 3-demethylubiquinone into 3-demethylubiquinol in vitro. However, it is unclear if 3-demethylubiquinone constitutes a substrate in vivo. May also play a role in the regulation of retinal ganglion cell (RGC) neurite outgrowth, and hence in the development of the inner retina and optic nerve (By similarity). Appears to be a potent …

**Summary**, from NCBI Gene [84816](https://www.ncbi.nlm.nih.gov/gene/84816):

> This gene encodes a mitochondrial protein that interacts with reticulon 4, which is a potent inhibitor of regeneration following spinal cord injury. This interaction may be important for reticulon-induced inhibition of neurite growth. Mutations in this gene can cause optic atrophy 10, with or without ataxia, cognitive disability, and seizures. There is a pseudogene for this gene on chromosome 12. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:18647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18647) · Entrez [84816](https://www.ncbi.nlm.nih.gov/gene/84816) · UniProt [Q8WWV3](https://www.uniprot.org/uniprotkb/Q8WWV3) · Ensembl [ENSG00000130347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130347)

## Data

Gene col 5056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5056); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5056]; `tensor/DDL_lfc|DDL_z.npy` [5056]; `embed/gene_vectors.npy` [5056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5056 or target_col == 5056). Every well: [[RTN4IP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTN4IP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
