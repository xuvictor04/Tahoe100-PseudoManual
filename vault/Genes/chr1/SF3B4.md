---
symbol: "SF3B4"
type: "gene"
col: 6724
ensembl_id: "ENSG00000143368"
name: "splicing factor 3b subunit 4"
location: "1q21.2"
module: 153
arm: "+"
pooled_cpm: 13.44
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# SF3B4

*splicing factor 3b subunit 4* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 11.5× (z +11.0, q 2e-25, up in 44 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0696×); [[Celecoxib (drug)]] 0.5 µM in 1 line (SHP-77 0.0808×); [[Adenosine (drug)]] 0.05 µM in 1 line (H4 0.0717×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRAS]] (+0.81, fdr 7e-06), [[ATP13A1]] (+0.78, fdr 7e-06), [[U2AF2]] (+0.76, fdr 7e-06); moves opposite to [[LAMTOR5]] (-0.72, fdr 7e-06), [[RPL36]] (-0.71, fdr 1e-05), [[RPL18]] (-0.71, fdr 1e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[CAMLG]] (-0.70, fdr 1e-05).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **11.5×** | +11.0 | 2e-25 | 44/46 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +8.3 | 2e-14 | 39/47 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **5.96×** | +8.1 | 1e-13 | 37/44 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.33×** | +7.3 | 5e-11 | 42/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.31×** | +6.9 | 5e-10 | 39/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +6.3 | 3e-08 | 22/28 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +5.8 | 5e-07 | 35/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +5.2 | 1e-05 | 13/48 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +5.1 | 2e-05 | 28/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +4.3 | 8e-04 | 29/47 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +4.3 | 8e-04 | 26/47 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +4.3 | 8e-04 | 26/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.2 | 9e-04 | 22/41 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +4.0 | 0.002 | 24/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.58×** | +3.9 | 0.003 | 22/46 (A498, LoVo, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 0.5 µM |  | **1.58×** | +3.9 | 0.003 | 21/47 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.003 | 21/48 (A549, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.008 | 18/46 (SW480, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.4 | 0.017 | 23/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6724.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0696×); [[Celecoxib (drug)]] 0.5 µM in 1 line (SHP-77 0.0808×); [[Adenosine (drug)]] 0.05 µM in 1 line (H4 0.0717×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Celecoxib (drug)]] 0.5 µM |  | 0.556× | -3.7 | 0.14 | 22/46 (SHP-77, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.588× | -3.3 | 0.26 | 20/45 (BT-474, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +9.4) | — |
| [[H4 (line)]] | wt | 8.85 | 0 | 1 | — | [[Adenosine (drug)]] 0.05 µM 0.0717× (z -8.8) |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.120× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 9.16 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0696× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 13.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 24.3× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.77× (z +8.7) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 11.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 21.7× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 1 | — | [[Celecoxib (drug)]] 0.5 µM 0.0808× (z -9.5) |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRAS]] | +0.81 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.78 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[U2AF2]] | +0.76 | +0.67 / +0.76 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[CAPRIN1]] | +0.73 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[MTA2]] | +0.73 | +0.62 / +0.71 | both halves | 7e-06 | pathway: ATP-dependent chromatin remodelers |
| [[PSME3]] | +0.72 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SSU72]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[SZRD1]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[MSANTD7]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[EMC1]] | +0.70 | +0.61 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMTOR5]] | -0.72 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[RPL36]] | -0.71 | -0.52 / -0.75 | both halves | 1e-05 |  |
| [[RPL18]] ⚠ | -0.71 | -0.49 / -0.73 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | -0.70 | -0.56 / -0.73 | both halves | 1e-05 |  |
| [[NACA4P]] ⚠ | -0.70 | -0.45 / -0.76 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | -0.69 | -0.57 / -0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | -0.69 | -0.48 / -0.74 | both halves | 2e-05 |  |
| [[COX5A]] ⚠ | -0.69 | -0.48 / -0.69 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARID3A]] | -0.68 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.67 | -0.53 / -0.71 | both halves | 1e-05 |  |
| [[RPL35A]] | -0.67 | -0.49 / -0.72 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.67 | -0.48 / -0.72 | both halves | 2e-05 |  |
| [[RPS29]] | -0.66 | -0.46 / -0.75 | both halves | 2e-05 |  |
| [[ATP5MJ]] | -0.66 | -0.48 / -0.71 | both halves | 2e-05 |  |
| [[TMEM258]] | -0.65 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[NDUFA1]] | -0.65 | -0.56 / -0.72 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.5, -24.8); signed map (-13.1, -34.8). **Vector** length 82.3, 17.1% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +6.9 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +6.0 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +11.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.7 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.6 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3b subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:149,923,317-149,927,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAP49, SF3b49, Hsh49 |
| Gene groups (HGNC) | RNA binding motif containing; SF3b complex |
| Reactome | 14 pathways, smallest: mRNA Splicing - Minor Pathway; CHD1 and CHD2 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15427](https://www.uniprot.org/uniprotkb/Q15427) (Splicing factor 3B subunit 4):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3B4 is part of the SF3B subcomplex, which is …

**Summary**, from NCBI Gene [10262](https://www.ncbi.nlm.nih.gov/gene/10262):

> This gene encodes one of four subunits of the splicing factor 3B. The protein encoded by this gene cross-links to a region in the pre-mRNA immediately upstream of the branchpoint sequence in pre-mRNA in the prespliceosomal complex A. It also may be involved in the assembly of the B, C and E spliceosomal complexes. In addition to RNA-binding activity, this protein interacts directly and highly specifically with subunit 2 of the splicing factor 3B. This protein contains two N-terminal …

**Accessions** — [HGNC:10771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10771) · Entrez [10262](https://www.ncbi.nlm.nih.gov/gene/10262) · UniProt [Q15427](https://www.uniprot.org/uniprotkb/Q15427) · Ensembl [ENSG00000143368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143368)

## Data

Gene col 6724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6724); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6724]; `tensor/DDL_lfc|DDL_z.npy` [6724]; `embed/gene_vectors.npy` [6724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6724 or target_col == 6724). Every well: [[SF3B4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3B4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
