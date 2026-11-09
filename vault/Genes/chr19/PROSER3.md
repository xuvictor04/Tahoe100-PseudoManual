---
symbol: "PROSER3"
type: "gene"
col: 9495
ensembl_id: "ENSG00000167595"
name: "proline and serine rich 3"
location: "19q13.12"
module: 182
arm: "-"
pooled_cpm: 15.92
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# PROSER3

*proline and serine rich 3* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.30× (z +4.1, q 0.022, up in 15 of 40 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.720× (z -7.2, q 4e-10, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENDOV]] (+0.61, fdr 7e-06), [[OPA3]] (+0.58, fdr 1e-05), [[DMPK]] (+0.56, fdr 1e-05); moves opposite to [[ATP5F1C]] (-0.54, fdr 1e-05), [[CREG1]] (-0.54, fdr 2e-05), [[FBXO7]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TMEM91]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.1 | 0.022 | 15/40 (SW1417, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.37 | 8/44 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.22× | +3.1 | 0.37 | 5/47 (NCI-H2030, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.720×** | -7.2 | 4e-10 | 31/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.653×** | -6.6 | 1e-08 | 24/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.708×** | -5.3 | 2e-05 | 25/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.720×** | -5.1 | 6e-05 | 22/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.802×** | -4.8 | 1e-04 | 21/48 (SNU-1, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -4.8 | 1e-04 | 21/44 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.726×** | -4.8 | 2e-04 | 18/45 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.570×** | -4.5 | 4e-04 | 18/48 (Panc 03.27, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -4.5 | 5e-04 | 22/47 (PANC-1, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -4.3 | 0.001 | 20/46 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.765×** | -4.1 | 0.002 | 16/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.782×** | -3.8 | 0.007 | 17/46 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.796×** | -3.5 | 0.019 | 16/46 (NCI-H23, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.805×** | -3.3 | 0.033 | 13/47 (SW 1271, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.055 | 11/47 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 20.2 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -17.4) |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.350× (z -8.9) |
| [[A-172 (line)]] | wt | 19.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.208× (z -9.8) |
| [[C32 (line)]] | wt | 9.74 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0825× (z -10.1) |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0716× (z -10.1) |
| [[H4 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 8.01 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0894× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -11.2) |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -11.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -9.1) |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENDOV]] | +0.61 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[OPA3]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DMPK]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PNKP]] | +0.54 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[MZF1]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[FBXO36]] | +0.53 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GMEB2]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[QRICH1]] | +0.52 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[BCL2L12]] | +0.52 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[CDK11A]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[HROB]] | +0.51 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CRK]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1C]] | -0.54 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[CREG1]] | -0.54 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[FBXO7]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PYURF]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MANBA]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[LTA4H]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ACP1]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ABHD10]] | -0.49 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[PAPSS1]] | -0.49 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TMEM183A]] | -0.49 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[MRS2]] | -0.48 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[STX7]] | -0.48 | -0.39 / -0.52 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM91]] | C | PROSER3's natural level strengthens TMEM91's drug response | PROSER3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.8, -7.1); signed map (1.6, -6.0). **Vector** length 69.5, 11.6% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.1 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | proline and serine rich 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,758,143-35,771,166 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30657; previously C19orf55 |
| Matched by | ensembl_id |

UniProt [Q2NL68](https://www.uniprot.org/uniprotkb/Q2NL68) carries no function annotation.

**Summary**, from NCBI Gene [148137](https://www.ncbi.nlm.nih.gov/gene/148137):

> Located in centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25204) · Entrez [148137](https://www.ncbi.nlm.nih.gov/gene/148137) · UniProt [Q2NL68](https://www.uniprot.org/uniprotkb/Q2NL68) · Ensembl [ENSG00000167595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167595)

## Data

Gene col 9495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9495); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9495]; `tensor/DDL_lfc|DDL_z.npy` [9495]; `embed/gene_vectors.npy` [9495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9495 or target_col == 9495). Every well: [[PROSER3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROSER3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
