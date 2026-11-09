---
symbol: "GEMIN4"
type: "gene"
col: 11032
ensembl_id: "ENSG00000179409"
name: "gem nuclear organelle associated protein 4"
location: "17p13.3"
module: 5
arm: "+"
pooled_cpm: 5.91
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# GEMIN4

*gem nuclear organelle associated protein 4* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.54× (z +5.0, q 4e-04, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.591× (z -6.1, q 7e-07, down in 22 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.629× (z -5.4, q 2e-05, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.108×, NCI-H2030 0.145×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (PANC-1 0.0952×, SW480 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (RKO 0.0634×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.139×); [[Zileuton (drug)]] 0.05 µM in 1 line (BT-474 0.0632×); [[Auranofin (drug)]] 5 µM in 1 line (RKO 0.153×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBRG4]] (+0.76, fdr 7e-06), [[BYSL]] (+0.74, fdr 7e-06), [[ALDH1B1]] (+0.74, fdr 7e-06); moves opposite to [[TALAM1]] (-0.62, fdr 1e-05), [[ZBTB47-AS1]] (-0.59, fdr 1e-05), [[STAG3L4-1]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 4e-04 | 19/46 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.7 | 0.063 | 10/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +3.5 | 0.100 | 15/42 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.74× | +3.3 | 0.12 | 5/16 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.33× | +3.3 | 0.12 | 6/47 (PANC-1, KATO III, …) | two highest doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.32× | +3.2 | 0.15 | 8/41 (AsPC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.30× | +3.0 | 0.19 | 2/47 (HEC-1-A, RKO) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11032.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HEC-1-A 0.108×, NCI-H2030 0.145×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (PANC-1 0.0952×, SW480 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (RKO 0.0634×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.139×); [[Zileuton (drug)]] 0.05 µM in 1 line (BT-474 0.0632×); [[Auranofin (drug)]] 5 µM in 1 line (RKO 0.153×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -6.1 | 7e-07 | 22/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.629×** | -5.4 | 2e-05 | 21/47 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.689×** | -4.1 | 0.006 | 17/43 (LOX-IMVI, A498, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.813×** | -3.4 | 0.094 | 12/47 (J82, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0634× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.153× (z -8.9) |
| [[SW480 (line)]] | alt | 10.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.54 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.112× (z -8.8) |
| [[BT-474 (line)]] | alt | 4.92 | 0 | 1 | — | [[Zileuton (drug)]] 0.05 µM 0.0632× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 8.37 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -12.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 9.63 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.138× (z -10.2) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 5.70 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 6.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -11.5) |
| [[PANC-1 (line)]] | alt | 5.15 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0952× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBRG4]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[BYSL]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[ALDH1B1]] | +0.74 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[NOP16]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.73 | +0.78 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[GRWD1]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[NIP7]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[NOP2]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[TWNK]] | +0.70 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[PPRC1]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ZBTB9]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[APEX2]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALAM1]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ZBTB47-AS1]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[STAG3L4-1]] | -0.58 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ERP29]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[USP33]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[RTN3]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises GEMIN4's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without TERT | 0.046 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.4, -37.6); signed map (-2.3, -46.0). **Vector** length 65.4, 9.90% of its response variance represented; |z| ≥ 3 in 841 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.64 to 13); *rRNA processing* (reactome, mean cos +0.54 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +2.7 | +3.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.4 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.9 | -2.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.3 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.2 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | gem nuclear organelle associated protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:744,421-753,999 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HHRF-1, DKFZP434B131, p97, DKFZP434D174, HC56, HCAP1 |
| Gene groups (HGNC) | Minor histocompatibility antigens; Gemins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MITOTIC_SPINDLE |
| Reactome | 8 pathways, smallest: SARS-CoV-2 modulates host translation machinery; Metabolism of non-coding RNA; snRNP Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P57678](https://www.uniprot.org/uniprotkb/P57678) (Gem-associated protein 4):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [50628](https://www.ncbi.nlm.nih.gov/gene/50628):

> The product of this gene is part of a large complex localized to the cytoplasm, nucleoli, and to discrete nuclear bodies called Gemini bodies (gems). The complex functions in spliceosomal snRNP assembly in the cytoplasm, and regenerates spliceosomes required for pre-mRNA splicing in the nucleus. The encoded protein directly interacts with a DEAD box protein and several spliceosome core proteins. Alternatively spliced transcript variants have been described, but their biological validity has not …

**Accessions** — [HGNC:15717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15717) · Entrez [50628](https://www.ncbi.nlm.nih.gov/gene/50628) · UniProt [P57678](https://www.uniprot.org/uniprotkb/P57678) · Ensembl [ENSG00000179409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179409)

## Data

Gene col 11032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11032); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11032]; `tensor/DDL_lfc|DDL_z.npy` [11032]; `embed/gene_vectors.npy` [11032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11032 or target_col == 11032). Every well: [[GEMIN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GEMIN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
