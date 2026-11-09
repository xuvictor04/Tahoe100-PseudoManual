---
symbol: "PPP1R16A"
type: "gene"
col: 8403
ensembl_id: "ENSG00000160972"
name: "protein phosphatase 1 regulatory subunit 16A"
location: "8q24.3"
module: 3
arm: "+"
pooled_cpm: 14.54
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PPP1R16A

*protein phosphatase 1 regulatory subunit 16A* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.10× (z +5.6, q 8e-06, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.604× (z -10.4, q 1e-22, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D10B]] (+0.62, fdr 9e-06), [[PPP6R1]] (+0.59, fdr 1e-05), [[FZR1]] (+0.59, fdr 1e-05); moves opposite to [[EFR3A]] (-0.46, fdr 5e-05), [[PYDC2-AS1]] (-0.45, fdr 6e-05), [[GCFC2]] (-0.45, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DOK3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +5.6 | 8e-06 | 24/45 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +5.5 | 8e-06 | 22/43 (A498, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.4 | 0.003 | 11/29 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.006 | 16/43 (SW1417, H4, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.6 | 0.043 | 0/48 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.24× | +3.1 | 0.18 | 6/46 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.18 | 8/44 (A498, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.18 | 12/44 (HT-29, A549, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.604×** | -10.4 | 1e-22 | 37/47 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.532×** | -9.2 | 7e-18 | 28/44 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -6.9 | 9e-10 | 26/46 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.753×** | -5.9 | 6e-07 | 22/46 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.701×** | -5.2 | 2e-05 | 23/45 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -5.0 | 6e-05 | 22/46 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.713×** | -4.8 | 1e-04 | 19/41 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.811×** | -4.4 | 9e-04 | 21/47 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.795×** | -3.4 | 0.047 | 14/46 (J82, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 34.0 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.303× (z -11.2) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -14.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.356× (z -9.4) |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.114× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.9) |
| [[J82 (line)]] | alt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -9.0) |
| [[SW 900 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D10B]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[PPP6R1]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FZR1]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NELFB]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ENKD1]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ESS2]] | +0.56 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[MARK4]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZNF324]] | +0.55 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[DDX41]] | +0.55 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[BRPF1]] | +0.54 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[MAPK7]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.53 | +0.32 / +0.55 | both halves | 1e-04 | STRING 552 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFR3A]] | -0.46 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[PYDC2-AS1]] | -0.45 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[GCFC2]] | -0.45 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[CCN3]] | -0.45 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[PON2]] | -0.45 | -0.26 / -0.47 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOK3]] | C | DOK3's natural level strengthens PPP1R16A's drug response | DOK3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.25; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.435). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.3, -6.0); signed map (-41.4, 4.1). **Vector** length 84.4, 16.8% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.8 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.7 | -10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.0 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -2.9 | -4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.1 |
|  | [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 16A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,477,969-144,502,121 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14333, MYPT3 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Protein phosphatase 1 regulatory subunits; Myosin phosphatase targeting family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I34](https://www.uniprot.org/uniprotkb/Q96I34) (Protein phosphatase 1 regulatory subunit 16A):

> Inhibits protein phosphatase 1 activity toward phosphorylase, myosin light chain and myosin substrates.

**Summary**, from NCBI Gene [84988](https://www.ncbi.nlm.nih.gov/gene/84988):

> Myosin light chain kinase and phosphatase (MLCP) complexes control the phosphorylation states of regulatory myosin light chains, which is crucial for muscle and intracellular movement. MLCPs typically contain a catalytic protein phosphatase 1 (PP1c) subunit, a myosin phosphatase targeting (MYPT) subunit, and another smaller subunit. The protein encoded by this gene represents an MYPT subunit, which is responsible for directing PP1c to its intended targets. However, while the phosphorylation of …

**Accessions** — [HGNC:14941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14941) · Entrez [84988](https://www.ncbi.nlm.nih.gov/gene/84988) · UniProt [Q96I34](https://www.uniprot.org/uniprotkb/Q96I34) · Ensembl [ENSG00000160972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160972)

## Data

Gene col 8403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8403); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8403]; `tensor/DDL_lfc|DDL_z.npy` [8403]; `embed/gene_vectors.npy` [8403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8403 or target_col == 8403). Every well: [[PPP1R16A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R16A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
