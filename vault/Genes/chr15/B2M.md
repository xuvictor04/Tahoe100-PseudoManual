---
symbol: "B2M"
type: "gene"
col: 9346
ensembl_id: "ENSG00000166710"
name: "beta-2-microglobulin"
location: "15q21.1"
module: 70
arm: "+"
pooled_cpm: 626.4
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 42
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# B2M

*beta-2-microglobulin* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +6.8, q 5e-09, up in 43 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +3.2, q 0.079, up in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 3.69×, NCI-H460 3.12×, SW48 3.39×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 3.33×, HOP62 4.19×, SW480 3.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (LoVo 4.25×, NCI-H460 4.26×; ⚠ cell-cycle shift, explains ~63% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 2.27×, LOX-IMVI 2.39×).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.718× (z -4.1, q 0.023, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.406×, COLO 205 0.447×, C-33 A 0.426×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-B]] (+0.86, fdr 7e-06), [[HLA-F]] (+0.84, fdr 7e-06), [[HLA-A]] (+0.80, fdr 7e-06); moves opposite to [[PGAM5]] (-0.64, fdr 7e-06), [[MAPKAPK3]] (-0.59, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9346.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 3.69×, NCI-H460 3.12×, SW48 3.39×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 3.33×, HOP62 4.19×, SW480 3.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (LoVo 4.25×, NCI-H460 4.26×; ⚠ cell-cycle shift, explains ~63% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 2.27×, LOX-IMVI 2.39×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.39×** | +6.8 | 5e-09 | 43/48 (J82, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.99×** | +5.8 | 1e-06 | 39/43 (J82, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.93×** | +5.8 | 1e-06 | 45/47 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.71×** | +4.8 | 3e-04 | 42/47 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.69×** | +4.4 | 1e-03 | 41/47 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.66×** | +4.2 | 0.003 | 38/44 (J82, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.56×** | +3.9 | 0.006 | 39/47 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.9 | 0.006 | 38/46 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.079 | 27/48 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.42× | +3.1 | 0.11 | 34/47 (NCI-H460, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9346.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tofacitinib (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.406×, COLO 205 0.447×, C-33 A 0.426×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.718×** | -4.1 | 0.023 | 33/48 (MIA PaCa-2, COLO 205, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.655×** | -3.7 | 0.057 | 39/47 (AsPC-1, Hs 766T, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 0.696× | -3.2 | 0.28 | 29/47 (COLO 205, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.708× | -3.0 | 0.31 | 28/47 (COLO 205, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 613 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.01× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 352 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 213 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 291 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[J82 (line)]] | alt | 1,124 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 266 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.0) | — |
| [[SW48 (line)]] | wt | 180 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 201 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 717 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 361 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.426× (z -8.5) |
| [[COLO 205 (line)]] | alt | 1,886 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.447× (z -8.7) |
| [[LS 180 (line)]] | wt | 398 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 391 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.406× (z -9.4) |
| [[SHP-77 (line)]] | alt | 249 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 846 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 1,174 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 142 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1,141 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 369 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 462 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 425 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1,428 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 617 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 882 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 823 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 403 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1,021 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 757 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 704 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1,354 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1,198 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 479 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 598 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 716 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 572 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 402 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 931 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 401 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 388 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1,676 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 462 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 566 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 915 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1,821 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 456 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 621 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-B]] | +0.86 | +0.82 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[HLA-F]] | +0.84 | +0.76 / +0.88 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[HLA-A]] | +0.80 | +0.76 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999 |
| [[PSMB9]] | +0.79 | +0.76 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 721 |
| [[GBP4]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TAP1]] | +0.76 | +0.70 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 984 |
| [[PSME2]] | +0.76 | +0.67 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 634 |
| [[PSME1]] | +0.76 | +0.71 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 546 |
| [[ISG15]] | +0.76 | +0.72 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 473 |
| [[IFITM3]] | +0.76 | +0.68 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[HLA-E]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999 |
| [[TRIM5]] | +0.74 | +0.73 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAM5]] | -0.64 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[MAPKAPK3]] | -0.59 | -0.59 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 41, C 1. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises B2M's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.27× lower at baseline in the lines without CTSS | 5e-04 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[HLA-DRA]] | B | HLA-DRA activity raises B2M's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.21× lower at baseline in the lines without HLA-DRA | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[IFI16]] | B | IFI16 activity raises B2M's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.13× lower at baseline in the lines without IFI16 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[PLAAT4]] | B | PLAAT4 activity raises B2M's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without PLAAT4 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[IFI44]] | B | IFI44 activity raises B2M's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.09× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[HLA-DRB1]] | B | HLA-DRB1 activity raises B2M's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.92× lower at baseline in the lines without HLA-DRB1 | 0.003 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[APOL1]] | B | APOL1 activity raises B2M's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without APOL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[GBP1]] | B | GBP1 activity raises B2M's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.28× lower at baseline in the lines without GBP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CASP10]] | B | CASP10 activity raises B2M's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without CASP10 | 0.005 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IFIT2]] | B | IFIT2 activity raises B2M's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.53× lower at baseline in the lines without IFIT2 | 0.007 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[GBP2]] | B | GBP2 activity raises B2M's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without GBP2 | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[CD74]] | B | CD74 activity raises B2M's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without CD74 | 0.009 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.861). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.6, 50.0); signed map (64.3, 27.5). **Vector** length 128, 59.7% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon alpha/beta signaling* (reactome, mean cos +0.71 to 10); *Non-canonical inflammasome activation* (reactome, mean cos +0.67 to 4); *complement* (hallmark, mean cos +0.65 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +6.1 | +1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.9 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.8 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.1 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.0 | +1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.5 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.5 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.6 | -2.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.3 | -4.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.1 | -2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.1 | -1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | beta-2-microglobulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:44,711,358-44,718,851 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | C1-set domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, ANDROGEN_RESPONSE, ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE |
| Reactome | 28 pathways, smallest: Modulation by Mtb of host immune system; Nef mediated downregulation of MHC class I complex cell surface expression; Endosomal/Vacuolar pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P61769](https://www.uniprot.org/uniprotkb/P61769) (Beta-2-microglobulin):

> Component of the class I major histocompatibility complex (MHC). Involved in the presentation of peptide antigens to the immune system. Exogenously applied M.tuberculosis EsxA or EsxA-EsxB (or EsxA expressed in host) binds B2M and decreases its export to the cell surface (total protein levels do not change), probably leading to defects in class I antigen presentation.

**Summary**, from NCBI Gene [567](https://www.ncbi.nlm.nih.gov/gene/567):

> This gene encodes a serum protein found in association with the major histocompatibility complex (MHC) class I heavy chain on the surface of nearly all nucleated cells. The protein has a predominantly beta-pleated sheet structure that can form amyloid fibrils in some pathological conditions. The encoded antimicrobial protein displays antibacterial activity in amniotic fluid. A mutation in this gene has been shown to result in hypercatabolic hypoproteinemia.[provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:914](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:914) · Entrez [567](https://www.ncbi.nlm.nih.gov/gene/567) · UniProt [P61769](https://www.uniprot.org/uniprotkb/P61769) · Ensembl [ENSG00000166710](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166710)

## Data

Gene col 9346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9346); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9346]; `tensor/DDL_lfc|DDL_z.npy` [9346]; `embed/gene_vectors.npy` [9346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9346 or target_col == 9346). Every well: [[B2M — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B2M.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
