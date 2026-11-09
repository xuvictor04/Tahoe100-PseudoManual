---
symbol: "PSD"
type: "gene"
col: 681
ensembl_id: "ENSG00000059915"
name: "pleckstrin and Sec7 domain containing"
location: "10q24.32"
module: 90
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# PSD

*pleckstrin and Sec7 domain containing* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.51× (z +27.9, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.603× (z -5.3, q 5e-05, down in 14 of 36 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.608× (z -5.2, q 5e-05, down in 15 of 40 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00861]] (+0.66, fdr 1e-05), [[MYT1L]] (+0.65, fdr 9e-06), [[RELA-DT]] (+0.65, fdr 1e-05); moves opposite to [[TMTC3]] (-0.60, fdr 3e-05), [[COMMD2]] (-0.54, fdr 5e-05).
> It is in [[Module 090]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.51×** | +27.9 | 0e+00 | 29/30 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +9.3 | 6e-18 | 14/31 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +8.6 | 2e-15 | 11/25 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +8.1 | 1e-13 | 14/32 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +7.4 | 2e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +6.9 | 4e-10 | 13/45 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.8 | 7e-10 | 3/11 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.9 | 3e-07 | 6/10 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +5.0 | 4e-05 | 13/42 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 0.002 | 8/17 (KATO III, A-172, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +4.2 | 0.002 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.002 | 6/43 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.8 | 0.007 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.007 | 1/19 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.7 | 0.009 | 1/15 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.014 | 4/45 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.032 | 1/21 (NCI-H23) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.032 | 2/40 (LoVo, HS-578T) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.033 | 4/36 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.033 | 1/32 (C-33 A) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.052 | 4/31 (A498, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 681.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.603×** | -5.3 | 5e-05 | 14/36 (NCI-H23, LoVo, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.608×** | -5.2 | 5e-05 | 15/40 (NCI-H2030, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -4.5 | 0.001 | 17/41 (SHP-77, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -4.1 | 0.007 | 14/45 (LOX-IMVI, HCT15, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.699×** | -3.8 | 0.019 | 14/37 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.703×** | -3.5 | 0.033 | 9/32 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -3.5 | 0.033 | 13/45 (SW1417, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -3.5 | 0.035 | 14/38 (HCT15, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.740× | -3.0 | 0.16 | 9/34 (NCI-H23, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 4.03 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.0537× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mozavaptan (drug)]] 0.05 µM 0.0715× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 2.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 1.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.56× (z +8.6) | — |
| [[LoVo (line)]] | wt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.26× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 3.63 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.05 µM 0.0475× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 1.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.6× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.64× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 3.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +10.5) | — |
| [[A-172 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.706 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.841 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00861]] | +0.66 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[MYT1L]] | +0.65 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[RELA-DT]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[G2E3-AS1]] | +0.64 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[HRG-AS1]] | +0.62 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[CHMP3-AS1]] | +0.62 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[SPATA21]] | +0.62 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CTDSPL2-DT]] | +0.61 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[USH2A]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[CNTNAP5]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ST7-AS2]] | +0.60 | +0.35 / +0.59 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC3]] | -0.60 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[COMMD2]] | -0.54 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.1, 28.5); signed map (34.9, 10.4). **Vector** length 40.6, 4.17% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +27.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.0 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.4 | -5.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin and Sec7 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,402,617-102,421,539 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA2011, TYL, PSD1, EFA6A, EFA6 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Pleckstrin and Sec7 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A5PKW4](https://www.uniprot.org/uniprotkb/A5PKW4) (PH and SEC7 domain-containing protein 1):

> Guanine nucleotide exchange factor for ARF6. Induces cytoskeletal remodeling (By similarity).

**Summary**, from NCBI Gene [5662](https://www.ncbi.nlm.nih.gov/gene/5662):

> This gene encodes a Plekstrin homology and SEC7 domains-containing protein that functions as a guanine nucleotide exchange factor. The encoded protein regulates signal transduction by activating ADP-ribosylation factor 6. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:9507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9507) · Entrez [5662](https://www.ncbi.nlm.nih.gov/gene/5662) · UniProt [A5PKW4](https://www.uniprot.org/uniprotkb/A5PKW4) · Ensembl [ENSG00000059915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059915)

## Data

Gene col 681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 681); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 681]; `tensor/DDL_lfc|DDL_z.npy` [681]; `embed/gene_vectors.npy` [681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 681 or target_col == 681). Every well: [[PSD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
