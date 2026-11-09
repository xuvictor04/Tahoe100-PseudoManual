---
symbol: "SLX9"
type: "gene"
col: 8329
ensembl_id: "ENSG00000160256"
name: "SLX9 ribosome biogenesis factor"
location: "21q22.3"
module: 33
arm: "+"
pooled_cpm: 14.47
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SLX9

*SLX9 ribosome biogenesis factor* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.68× (z +7.9, q 2e-12, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.703× (z -7.6, q 2e-11, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLRMT]] (+0.79, fdr 7e-06), [[NLE1]] (+0.71, fdr 7e-06), [[DHODH]] (+0.67, fdr 7e-06); moves opposite to [[KANSL1L]] (-0.56, fdr 1e-03, ⚠ one half only (not replicated)), [[LNC-LBCS]] (-0.55, fdr 4e-05), [[HMGN2]] (-0.55, fdr 9e-05), [[ZNF846]] (-0.53, fdr 3e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8329.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +7.9 | 2e-12 | 34/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +7.3 | 6e-11 | 26/47 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +6.4 | 2e-08 | 26/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.47×** | +5.9 | 6e-07 | 25/47 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +5.4 | 9e-06 | 19/40 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 9e-06 | 20/46 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.9 | 8e-05 | 18/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 5e-04 | 19/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.004 | 6/46 (NCI-H2347, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **1.30×** | +3.9 | 0.006 | 13/41 (SW 900, LoVo, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.010 | 9/45 (NCI-H1792, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.017 | 18/44 (BT-474, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.26×** | +3.2 | 0.055 | 10/33 (SW480, LS 180, …) | inconsistent across doses | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.055 | 9/45 (NCI-H460, A498, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.067 | 9/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.067 | 5/46 (HEC-1-A, Hs 766T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.067 | 7/45 (CFPAC-1, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.067 | 7/43 (Hs 766T, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.068 | 6/46 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.068 | 7/43 (RPMI-7951, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8329.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.703×** | -7.6 | 2e-11 | 26/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.777×** | -5.4 | 2e-05 | 21/47 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.756×** | -4.3 | 0.004 | 17/47 (C-33 A, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.679× | -3.1 | 0.29 | 4/47 (H4, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.821× | -3.0 | 0.30 | 3/48 (LS 180, Hs 766T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8329. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 17.7 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.115× (z -10.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -10.0) |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.112× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.6) |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.2) |
| [[HS-578T (line)]] | alt | 9.75 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[RKO (line)]] | wt | 19.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 7.69 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[SW48 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8329), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLRMT]] | +0.79 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[NLE1]] | +0.71 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[DHODH]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[HDHD5]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NEIL2]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.65 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ZNF74]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[EIF3M]] | +0.64 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[DDX55]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[DNAJA3]] | +0.63 | +0.49 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANSL1L]] | -0.56 | -0.59 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[LNC-LBCS]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[HMGN2]] | -0.55 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[ZNF846]] | -0.53 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[GNAS]] | -0.52 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.0, -41.7); signed map (-8.5, -51.5). **Vector** length 79.1, 14.8% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.3 | +5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -7.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | SLX9 ribosome biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,940,025-44,976,973 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRED56; previously C21orf70, FAM207A |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSI2](https://www.uniprot.org/uniprotkb/Q9NSI2) (Ribosome biogenesis protein SLX9 homolog):

> May be involved in ribosome biogenesis.

**Summary**, from NCBI Gene [85395](https://www.ncbi.nlm.nih.gov/gene/85395):

> Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15811) · Entrez [85395](https://www.ncbi.nlm.nih.gov/gene/85395) · UniProt [Q9NSI2](https://www.uniprot.org/uniprotkb/Q9NSI2) · Ensembl [ENSG00000160256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160256)

## Data

Gene col 8329: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8329); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8329, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8329]; `tensor/DDL_lfc|DDL_z.npy` [8329]; `embed/gene_vectors.npy` [8329]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8329 or target_col == 8329). Every well: [[SLX9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLX9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
