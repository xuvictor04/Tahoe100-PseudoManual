---
symbol: "TEPSIN"
type: "gene"
col: 9449
ensembl_id: "ENSG00000167302"
name: "TEPSIN adaptor related protein complex 4 accessory protein"
location: "17q25.3"
module: 138
arm: "+"
pooled_cpm: 4.25
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# TEPSIN

*TEPSIN adaptor related protein complex 4 accessory protein* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +9.6, q 3e-19, up in 26 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.560× (z -6.5, q 6e-08, down in 20 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM: 0.779× (z -3.7, q 0.050, down in 0 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFTRAF1]] (+0.79, fdr 7e-06), [[CACTIN]] (+0.69, fdr 1e-05), [[CRTC2]] (+0.67, fdr 7e-06); moves opposite to [[GGCT]] (-0.52, fdr 4e-05), [[BOLA3]] (-0.48, fdr 7e-05), [[PPAT]] (-0.47, fdr 4e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BOLA3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9449.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +9.6 | 3e-19 | 26/38 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.9 | 2e-09 | 17/38 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +6.6 | 9e-09 | 21/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +6.4 | 2e-08 | 16/38 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +5.6 | 2e-06 | 18/47 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +5.6 | 2e-06 | 9/46 (SNU-423, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.5 | 3e-06 | 12/24 (NCI-H2030, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +5.4 | 6e-06 | 16/45 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.1 | 2e-05 | 15/37 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +5.0 | 4e-05 | 16/45 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.8 | 8e-05 | 14/44 (SW480, BT-474, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.6 | 2e-04 | 12/36 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 7e-04 | 9/36 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.001 | 5/46 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.009 | 7/43 (NCI-H2030, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.021 | 6/39 (KATO III, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.021 | 7/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9449.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.560×** | -6.5 | 6e-08 | 20/46 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.779×** | -3.7 | 0.050 | 0/46 | rises with dose | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.722×** | -3.5 | 0.082 | 3/44 (Panc 03.27, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.652×** | -3.4 | 0.082 | 6/46 (PANC-1, SNU-423, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.564×** | -3.3 | 0.082 | 7/37 (SHP-77, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.729×** | -3.3 | 0.082 | 13/44 (HS-578T, KATO III, …) | all doses, flat |  |
| [[Relugolix (drug)]] 0.5 µM |  | 0.755× | -3.1 | 0.12 | 3/46 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.755× | -3.1 | 0.12 | 2/44 (C-33 A, PANC-1) | rises with dose | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.759× | -3.1 | 0.13 | 9/45 (NCI-H1573, SW 900, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | 0.595× | -3.0 | 0.14 | 12/36 (LoVo, KATO III, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9449. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 3.46 | 0 | 1 | — | [[Retinoic acid (drug)]] 0.5 µM 0.0770× (z -8.6) |
| [[RKO (line)]] | wt | 4.92 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0725× (z -8.6) |
| [[A-172 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9449), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFTRAF1]] | +0.79 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CACTIN]] | +0.69 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[CRTC2]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ZNF740]] | +0.66 | +0.53 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[RXRB]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TAF1C]] | +0.65 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[USP19]] | +0.63 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[WDR6]] | +0.63 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[RNF44]] | +0.62 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[GIGYF1]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MED16]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.61 | +0.76 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGCT]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[BOLA3]] | -0.48 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[PPAT]] | -0.47 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3]] | C | BOLA3's natural level strengthens TEPSIN's drug response | BOLA3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.05; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.8, -22.9); signed map (3.2, -7.9). **Vector** length 52.0, 6.45% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.0 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.2 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | TEPSIN adaptor related protein complex 4 accessory protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,228,277-81,239,091 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31528; previously C17orf56, ENTHD2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N21](https://www.uniprot.org/uniprotkb/Q96N21) (AP-4 complex accessory subunit Tepsin):

> Associates with the adapter-like complex 4 (AP-4) and may therefore play a role in vesicular trafficking of proteins at the trans-Golgi network.

**Summary**, from NCBI Gene [146705](https://www.ncbi.nlm.nih.gov/gene/146705):

> Located in coated vesicle membrane and trans-Golgi network membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26458) · Entrez [146705](https://www.ncbi.nlm.nih.gov/gene/146705) · UniProt [Q96N21](https://www.uniprot.org/uniprotkb/Q96N21) · Ensembl [ENSG00000167302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167302)

## Data

Gene col 9449: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9449); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9449, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9449]; `tensor/DDL_lfc|DDL_z.npy` [9449]; `embed/gene_vectors.npy` [9449]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9449 or target_col == 9449). Every well: [[TEPSIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEPSIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
