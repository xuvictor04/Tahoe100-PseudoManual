---
symbol: "ZDHHC24"
type: "gene"
col: 10468
ensembl_id: "ENSG00000174165"
name: "zDHHC palmitoyltransferase 24"
location: "11q13.2"
module: 221
arm: "+"
pooled_cpm: 10.11
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# ZDHHC24

*zDHHC palmitoyltransferase 24* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.01× (z +11.4, q 3e-27, up in 13 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.53× (z +10.1, q 1e-21, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.611× (z -11.8, q 2e-29, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHIP2A]] (+0.61, fdr 1e-05), [[FAM219B]] (+0.61, fdr 1e-05), [[COQ4]] (+0.58, fdr 1e-05); moves opposite to [[MYH15]] (-0.61, fdr 7e-06), [[MYLK2]] (-0.56, fdr 1e-05), [[SVIL]] (-0.53, fdr 2e-05).
> It is in [[Module 221]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +11.4 | 3e-27 | 13/18 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +10.1 | 1e-21 | 32/48 (A-427, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.9 | 1e-20 | 30/45 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +9.0 | 3e-17 | 25/34 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.4 | 1e-08 | 19/39 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 6e-08 | 14/47 (HOP62, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +5.9 | 2e-07 | 12/25 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +5.9 | 2e-07 | 18/39 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 2e-04 | 10/45 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.4 | 5e-04 | 13/47 (SNU-423, A-172, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.010 | 6/44 (PANC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.25×** | +3.6 | 0.013 | 16/45 (RKO, hTERT-HPNE, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.013 | 8/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +3.3 | 0.044 | 10/47 (HEC-1-A, AsPC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.20×** | +3.1 | 0.074 | 10/47 (HOP62, KATO III, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.074 | 8/39 (HS-578T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.087 | 4/48 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.611×** | -11.8 | 2e-29 | 31/44 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.626×** | -7.9 | 6e-13 | 20/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.435×** | -7.4 | 3e-11 | 24/43 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.722×** | -5.3 | 2e-05 | 19/46 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -5.2 | 2e-05 | 17/47 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.833× | -4.4 | 0.001 | 12/48 (NCI-H1573, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.791×** | -3.8 | 0.014 | 14/47 (SW480, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.824×** | -3.3 | 0.077 | 8/46 (SW 1271, NCI-H2347, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | 0.830× | -3.2 | 0.10 | 9/46 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.40× (z +10.5) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.156× (z -8.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -8.8) |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.9) |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP2A]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[FAM219B]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[COQ4]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[C12orf76]] | +0.58 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[TP53I13]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SEC61A2]] | +0.57 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[FAHD2A]] | +0.57 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[FBXO44]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LINC00115]] | +0.56 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DNASE2]] | +0.55 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[NUDT2]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SLC41A3]] | +0.54 | +0.59 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH15]] | -0.61 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[MYLK2]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[SVIL]] | -0.53 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[BCAN-AS2]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[EGR3]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TRA2B]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[LINC00460]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[DNMT1]] | -0.50 | -0.29 / -0.65 | both halves | 3e-04 |  |
| [[MTNR1A]] | -0.50 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[EGR2]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MMP25]] | -0.49 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[BCAN-AS1]] | -0.49 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.6, -10.5); signed map (-24.5, -1.0). **Vector** length 57.0, 7.85% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.5 | +10.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.1 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +9.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.3 | +1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -3.5 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -7.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,520,637-66,546,235 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX98](https://www.uniprot.org/uniprotkb/Q6UX98) (Probable palmitoyltransferase ZDHHC24):

> Probable palmitoyltransferase that could catalyze the addition of palmitate onto various protein substrates.

**Summary**, from NCBI Gene [254359](https://www.ncbi.nlm.nih.gov/gene/254359):

> Predicted to enable protein-cysteine S-palmitoyltransferase activity. Predicted to be involved in protein targeting to membrane. Predicted to be located in membrane. Predicted to be active in Golgi apparatus and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27387](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27387) · Entrez [254359](https://www.ncbi.nlm.nih.gov/gene/254359) · UniProt [Q6UX98](https://www.uniprot.org/uniprotkb/Q6UX98) · Ensembl [ENSG00000174165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174165)

## Data

Gene col 10468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10468); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10468]; `tensor/DDL_lfc|DDL_z.npy` [10468]; `embed/gene_vectors.npy` [10468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10468 or target_col == 10468). Every well: [[ZDHHC24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
