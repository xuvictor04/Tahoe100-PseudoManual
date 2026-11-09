---
symbol: "ATP13A1"
type: "gene"
col: 2656
ensembl_id: "ENSG00000105726"
name: "ATPase 13A1"
location: "19p13.11"
module: 153
arm: "+"
pooled_cpm: 10.3
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# ATP13A1

*ATPase 13A1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +7.0, q 1e-09, up in 28 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0694×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.127×; ⚠ cell-cycle shift, explains ~79% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0837×); [[Menadione (drug)]] 0.05 µM in 1 line (C32 0.0974×); [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (SW 900 0.0804×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[U2AF2]] (+0.82, fdr 7e-06), [[SF3B4]] (+0.78, fdr 7e-06), [[VARS1]] (+0.75, fdr 7e-06); moves opposite to [[RPL36AL]] (-0.67, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[RPL18]] (-0.66, fdr 1e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[TMEM191A-1]] (-0.65, fdr 2e-05), [[CAMLG]] (-0.64, fdr 1e-05), [[GABARAPL2]] (-0.63, fdr 1e-05).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +7.0 | 1e-09 | 28/47 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.9 | 1e-09 | 14/21 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +5.7 | 2e-06 | 16/27 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.0 | 8e-05 | 18/36 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 0.05 µM |  | **1.45×** | +4.0 | 0.007 | 12/48 (LS 180, NCI-H460, …) | all doses, flat | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +3.9 | 0.009 | 13/43 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.011 | 15/44 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.26×** | +3.6 | 0.019 | 15/48 (J82, KATO III, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +3.6 | 0.023 | 12/47 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.4 | 0.034 | 12/41 (A498, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.051 | 8/46 (A498, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.051 | 6/48 (NCI-H460, LS 180, …) | inconsistent across doses | position effect removed |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.082 | 7/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2656.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0694×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.127×; ⚠ cell-cycle shift, explains ~79% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (A549 0.0837×); [[Menadione (drug)]] 0.05 µM in 1 line (C32 0.0974×); [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM in 1 line (SW 900 0.0804×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.742× | -3.4 | 0.40 | 17/46 (SHP-77, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Allantoin (drug)]] 0.5 µM |  | 0.755× | -3.2 | 0.41 | 8/46 (A549, NCI-H460, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 7.15 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0837× (z -10.3) |
| [[C32 (line)]] | wt | 11.4 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0974× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.127× (z -10.9) ⚠ cell-cycle shift, explains ~79% of this change |
| [[RKO (line)]] | wt | 14.3 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.151× (z -9.3) |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0694× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 6.71 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0804× (z -9.3) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.78 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[VARS1]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[WIZ]] | +0.75 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[USP19]] | +0.74 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[PIGO]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[IPO4]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[EMC1]] | +0.72 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[BAP1]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[WASH8P]] ⚠ | +0.72 | +0.52 / +0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[STK36]] | +0.72 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[PRPF8]] | +0.70 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[SF3A1]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL36AL]] ⚠ | -0.67 | -0.53 / -0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL18]] ⚠ | -0.66 | -0.49 / -0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM191A-1]] | -0.65 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[CAMLG]] | -0.64 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[GABARAPL2]] | -0.63 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[ADGRL3-AS1]] | -0.63 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[C4orf48]] | -0.62 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[ATP5MJ]] | -0.62 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[RPS29]] | -0.62 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[RPS13]] ⚠ | -0.62 | -0.44 / -0.67 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[COMMD6]] | -0.61 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.61 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[RPL35A]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.899). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.2, -24.8); signed map (-13.0, -34.0). **Vector** length 74.1, 12.8% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.0 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +7.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.7 | +2.5 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -3.4 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.1 | -1.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ATPase 13A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,645,198-19,663,676 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1825, FLJ31858, CGI-152; previously ATP13A |
| Gene groups (HGNC) | ATPase orphan transporters |
| Reactome | 3 pathways, smallest: Ion transport by P-type ATPases; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD20](https://www.uniprot.org/uniprotkb/Q9HD20) (Endoplasmic reticulum transmembrane helix translocase):

> Endoplasmic reticulum translocase required to remove mitochondrial transmembrane proteins mistargeted to the endoplasmic reticulum. Acts as a dislocase that mediates the ATP-dependent extraction of mislocalized mitochondrial transmembrane proteins from the endoplasmic reticulum membrane. Specifically binds mitochondrial tail-anchored transmembrane proteins: has an atypically large substrate-binding pocket that recognizes and binds moderately hydrophobic transmembranes with short hydrophilic …

**Summary**, from NCBI Gene [57130](https://www.ncbi.nlm.nih.gov/gene/57130):

> Enables membrane protein dislocase activity. Involved in extraction of mislocalized protein from ER membrane. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24215](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24215) · Entrez [57130](https://www.ncbi.nlm.nih.gov/gene/57130) · UniProt [Q9HD20](https://www.uniprot.org/uniprotkb/Q9HD20) · Ensembl [ENSG00000105726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105726)

## Data

Gene col 2656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2656); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2656]; `tensor/DDL_lfc|DDL_z.npy` [2656]; `embed/gene_vectors.npy` [2656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2656 or target_col == 2656). Every well: [[ATP13A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP13A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
