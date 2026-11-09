---
symbol: "MAPK8IP2"
type: "gene"
col: 179
ensembl_id: "ENSG00000008735"
name: "mitogen-activated protein kinase 8 interacting protein 2"
location: "22q13.33"
module: 10
arm: "+"
pooled_cpm: 2.28
n_lines_expressing: 32
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# MAPK8IP2

*mitogen-activated protein kinase 8 interacting protein 2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.89× (z +14.3, q 1e-43, up in 16 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K2-DT]] (+0.68, fdr 9e-06), [[XKR4]] (+0.64, fdr 1e-05), [[MYL5]] (+0.63, fdr 1e-05); moves opposite to [[SHQ1]] (-0.51, fdr 3e-05), [[NHP2]] (-0.51, fdr 1e-04), [[PIGF]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SRRM3]] → it (grade B ⚠); 7 go from it, the strongest it → [[NPHS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.89×** | +14.3 | 1e-43 | 16/21 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.08×** | +11.8 | 7e-30 | 12/19 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.23×** | +10.3 | 1e-22 | 2/2 (PANC-1, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.69×** | +9.7 | 4e-20 | 6/10 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.51×** | +9.0 | 3e-17 | 4/10 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +8.3 | 7e-15 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.91×** | +7.9 | 2e-13 | 10/19 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.39×** | +6.5 | 6e-09 | 15/23 (LoVo, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +6.0 | 1e-07 | 9/28 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +5.4 | 4e-06 | 2/17 (CFPAC-1, SW480) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +5.1 | 2e-05 | 8/28 (SW480, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +4.6 | 2e-04 | 4/27 (A-427, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +4.3 | 8e-04 | 8/28 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +4.3 | 8e-04 | 9/24 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +4.2 | 0.001 | 7/27 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +4.1 | 0.001 | 9/28 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.002 | 2/18 (A-427, BT-474) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.003 | 5/27 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +3.4 | 0.016 | 5/16 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.759 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.907 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.789 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K2-DT]] | +0.68 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[XKR4]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[MYL5]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TFAP2A-AS1]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[KRTAP5-AS1]] | +0.61 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[DNAH3]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[AJUBA-DT]] | +0.59 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[PATL2]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[GUCY2C-AS1]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[GUCY1A2]] | +0.59 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ZBTB4]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CHODL]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHQ1]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[NHP2]] | -0.51 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[PIGF]] | -0.51 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[TDP1]] | -0.50 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[R3HDM1]] | -0.50 | -0.32 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM3]] | B | SRRM3 activity raises MAPK8IP2's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without SRRM3 | 0.007 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MAPK8IP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPHS1]] | B | MAPK8IP2 activity raises NPHS1's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without MAPK8IP2 | 0.015 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[ZFHX2]] | B | MAPK8IP2 activity raises ZFHX2's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 2.07× lower at baseline in the lines without MAPK8IP2 | 0.031 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[ACAD9-DT]] | B | MAPK8IP2 activity raises ACAD9-DT's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.21× lower at baseline in the lines without MAPK8IP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[SRRM3]] | B | MAPK8IP2 activity raises SRRM3's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 2.01× lower at baseline in the lines without MAPK8IP2 | 0.047 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[PAX5]] | B | MAPK8IP2 activity raises PAX5's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.63× lower at baseline in the lines without MAPK8IP2 | 0.072 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[ZC2HC1C]] | B | MAPK8IP2 activity raises ZC2HC1C's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.21× lower at baseline in the lines without MAPK8IP2 | 0.082 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[DNAH12]] | B | MAPK8IP2 activity raises DNAH12's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.14× lower at baseline in the lines without MAPK8IP2 | 0.093 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (19.1, 21.5); signed map (38.9, -6.3). **Vector** length 36.9, 5.73% of its response variance represented; |z| ≥ 3 in 606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | +0.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -0.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 8 interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,600,793-50,613,981 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IB2, JIP2; previously PRKM8IPL |
| Gene groups (HGNC) | SH3 domain containing |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13387](https://www.uniprot.org/uniprotkb/Q13387) (C-Jun-amino-terminal kinase-interacting protein 2):

> The JNK-interacting protein (JIP) group of scaffold proteins selectively mediates JNK signaling by aggregating specific components of the MAPK cascade to form a functional JNK signaling module. JIP2 inhibits IL1 beta-induced apoptosis in insulin-secreting cells. May function as a regulator of vesicle transport, through interactions with the JNK-signaling components and motor proteins (By similarity).

**Summary**, from NCBI Gene [23542](https://www.ncbi.nlm.nih.gov/gene/23542):

> This gene encodes a scaffold protein that is thought to be involved in the regulation of the c-Jun amino-terminal kinase signaling pathway. This protein has been shown to interact with and regulate the activity of MAPK8/JNK1 and MAP2K7/MKK7 kinases. [provided by RefSeq, Jun 2017]

**Accessions** — [HGNC:6883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6883) · Entrez [23542](https://www.ncbi.nlm.nih.gov/gene/23542) · UniProt [Q13387](https://www.uniprot.org/uniprotkb/Q13387) · Ensembl [ENSG00000008735](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008735)

## Data

Gene col 179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 179); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 179]; `tensor/DDL_lfc|DDL_z.npy` [179]; `embed/gene_vectors.npy` [179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 179 or target_col == 179). Every well: [[MAPK8IP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK8IP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
