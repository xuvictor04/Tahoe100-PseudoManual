---
symbol: "WIZ"
type: "gene"
col: 241
ensembl_id: "ENSG00000011451"
name: "WIZ zinc finger"
location: "19p13.12"
module: 96
arm: "+"
pooled_cpm: 10.22
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# WIZ

*WIZ zinc finger* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.65× (z +12.8, q 1e-34, up in 19 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +7.5, q 1e-11, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.737× (z -4.0, q 0.032, down in 18 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.189×; ⚠ toxic); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SHP-77 0.128×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (Hs 766T 0.115×); [[Sonidegib (drug)]] 5 µM in 1 line (NCI-H460 0.0715×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP13A1]] (+0.75, fdr 7e-06), [[TAF1C]] (+0.71, fdr 7e-06), [[PIGO]] (+0.70, fdr 7e-06); moves opposite to [[COX6A1]] (-0.62, fdr 1e-05), [[GMCL1]] (-0.56, fdr 3e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +12.8 | 1e-34 | 19/22 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +11.4 | 8e-28 | 34/35 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +9.0 | 4e-17 | 23/28 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +7.5 | 1e-11 | 23/46 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +7.0 | 2e-10 | 22/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +5.2 | 2e-05 | 17/41 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.1 | 0.004 | 14/38 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.006 | 14/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.8 | 0.008 | 11/47 (SW480, KATO III, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.028 | 6/41 (SW480, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.035 | 13/47 (A498, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.053 | 5/46 (LS 180, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.18× | +3.2 | 0.053 | 11/44 (NCI-H2347, A498, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.083 | 15/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.095 | 8/45 (HS-578T, BT-474, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 241.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.189×; ⚠ toxic); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SHP-77 0.128×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (Hs 766T 0.115×); [[Sonidegib (drug)]] 5 µM in 1 line (NCI-H460 0.0715×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.737×** | -4.0 | 0.032 | 18/46 (NCI-H460, AN3 CA, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.792× | -3.1 | 0.57 | 10/47 (SNU-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 10.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.6) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.189× (z -9.8) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 9.50 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[A498 (line)]] | wt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 7.07 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.0794× (z -8.6) |
| [[Hs 766T (line)]] | wt | 8.26 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.115× (z -9.2) |
| [[LoVo (line)]] | wt | 8.77 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 7.86 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.0715× (z -8.6) |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.128× (z -9.6) |
| [[A-172 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP13A1]] | +0.75 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[TAF1C]] | +0.71 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[PIGO]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[STRN4]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[PPP2R1A]] | +0.69 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[NCDN]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MED16]] | +0.67 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[ACP2]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[MED12]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[USP19]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[WDR6]] | +0.65 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PRRC2B]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6A1]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.56 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises WIZ's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.32× lower at baseline in the lines without SLC4A3 | 0.080 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.0, -24.6); signed map (-9.6, -32.3). **Vector** length 69.7, 11.3% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +7.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.5 | +5.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +3.5 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | WIZ zinc finger |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,419,978-15,449,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF803 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [O95785](https://www.uniprot.org/uniprotkb/O95785) (Protein Wiz):

> May link EHMT1 and EHMT2 histone methyltransferases to the CTBP corepressor machinery. May be involved in EHMT1-EHMT2 heterodimer formation and stabilization (By similarity).

**Summary**, from NCBI Gene [58525](https://www.ncbi.nlm.nih.gov/gene/58525):

> Enables several functions, including DNA-binding transcription factor activity, RNA polymerase II-specific; histone methyltransferase binding activity; and transcription corepressor binding activity. Involved in positive regulation of nuclear cell cycle DNA replication and protein stabilization. Located in nucleoplasm. Biomarker of atherosclerosis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30917) · Entrez [58525](https://www.ncbi.nlm.nih.gov/gene/58525) · UniProt [O95785](https://www.uniprot.org/uniprotkb/O95785) · Ensembl [ENSG00000011451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011451)

## Data

Gene col 241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 241); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 241]; `tensor/DDL_lfc|DDL_z.npy` [241]; `embed/gene_vectors.npy` [241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 241 or target_col == 241). Every well: [[WIZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WIZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
