---
symbol: "TRAPPC6A"
type: "gene"
col: 141
ensembl_id: "ENSG00000007255"
name: "trafficking protein particle complex subunit 6A"
location: "19q13.32"
module: 24
arm: "+"
pooled_cpm: 7.19
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TRAPPC6A

*trafficking protein particle complex subunit 6A* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +6.9, q 4e-09, up in 31 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 8.20×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 4.64×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.426× (z -6.8, q 8e-09, down in 29 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.512× (z -5.3, q 3e-05, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM7-AS2]] (+0.67, fdr 1e-05), [[SMIM27]] (+0.67, fdr 1e-05), [[IST1]] (+0.65, fdr 2e-05); moves opposite to [[STIP1]] (-0.62, fdr 3e-05), [[CCT5]] (-0.60, fdr 3e-05), [[CCT7]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[RALB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 141.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 8.20×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 4.64×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.9 | 4e-09 | 31/39 (BT-474, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +6.7 | 4e-09 | 20/25 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +6.3 | 5e-08 | 8/14 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.8 | 0.019 | 13/31 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +3.7 | 0.024 | 10/18 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +3.5 | 0.040 | 16/32 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.040 | 15/46 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.47× | +3.1 | 0.14 | 14/45 (KATO III, LS 180, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.48× | +3.0 | 0.15 | 9/35 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 141.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.426×** | -6.8 | 8e-09 | 29/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -5.3 | 3e-05 | 25/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.516×** | -5.2 | 3e-05 | 26/46 (KATO III, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -5.1 | 3e-05 | 26/45 (COLO 205, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.632×** | -5.1 | 3e-05 | 26/39 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.552×** | -4.7 | 3e-04 | 25/46 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 5 µM |  | **0.695×** | -4.1 | 0.004 | 26/47 (KATO III, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.606×** | -3.6 | 0.023 | 16/44 (SW480, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.20× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.28 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0682× (z -8.9) |
| [[KATO III (line)]] | alt | 20.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.167× (z -9.4) |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.4) |
| [[SW480 (line)]] | alt | 9.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.1) |
| [[A-427 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 7 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM7-AS2]] | +0.67 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[SMIM27]] | +0.67 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[IST1]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CCDC115]] | +0.64 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[ILF3-DT]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[DNAJC4]] | +0.62 | +0.42 / +0.71 | both halves | 4e-05 |  |
| [[CREBRF]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CNNM2]] | +0.62 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[C1orf56]] | +0.62 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[C11orf1]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ACSM3]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MINCR]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIP1]] | -0.62 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[CCT5]] | -0.60 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[CCT7]] | -0.59 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[MACROH2A1]] | -0.55 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[CCT6A]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CCT3]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[GLO1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[FKBP4]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[DYNC1H1]] | -0.52 | -0.45 / -0.55 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[RALB]] | -0.51 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PRPS1]] | -0.51 | -0.43 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALB]] | C | TRAPPC6A's natural level strengthens RALB's drug response | TRAPPC6A's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.20; direction not clear | 0.093 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.0, -22.2); signed map (-7.1, 3.2). **Vector** length 54.0, 8.89% of its response variance represented; |z| ≥ 3 in 699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -2.0 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.6 | +2.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 6A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,162,928-45,178,237 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRS33, MGC2650, HSPC289 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 8 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O75865](https://www.uniprot.org/uniprotkb/O75865) (Trafficking protein particle complex subunit 6A):

> May play a role in vesicular transport during the biogenesis of melanosomes.

**Summary**, from NCBI Gene [79090](https://www.ncbi.nlm.nih.gov/gene/79090):

> This gene encodes a component of the trafficking protein particle complex, which tethers transport vesicles to the cis-Golgi membrane. Loss of expression of the related gene in mouse affects coat and eye pigmentation, suggesting that the encoded protein may be involved in melanosome biogenesis. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:23069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23069) · Entrez [79090](https://www.ncbi.nlm.nih.gov/gene/79090) · UniProt [O75865](https://www.uniprot.org/uniprotkb/O75865) · Ensembl [ENSG00000007255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007255)

## Data

Gene col 141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 141); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 141]; `tensor/DDL_lfc|DDL_z.npy` [141]; `embed/gene_vectors.npy` [141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 141 or target_col == 141). Every well: [[TRAPPC6A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC6A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
