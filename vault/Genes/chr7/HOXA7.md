---
symbol: "HOXA7"
type: "gene"
col: 4357
ensembl_id: "ENSG00000122592"
name: "homeobox A7"
location: "7p15.2"
module: 68
arm: "+"
pooled_cpm: 2.62
n_lines_expressing: 24
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# HOXA7

*homeobox A7* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.45× (z +10.8, q 1e-24, up in 13 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.203×; ⚠ cell-cycle shift, explains ~79% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA10-AS]] (+0.76, fdr 7e-06, ⚠ same locus), [[ZCCHC3]] (+0.61, fdr 1e-05), [[HNF1A]] (+0.60, fdr 2e-05), [[PPP4R3A]] (+0.60, fdr 9e-05); moves opposite to [[CALU]] (-0.60, fdr 1e-05), [[SEC22B]] (-0.59, fdr 1e-05), [[GGCX]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SAR1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4357.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +10.8 | 1e-24 | 13/18 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.19×** | +9.5 | 5e-19 | 2/3 (A498, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.62×** | +9.5 | 5e-19 | 5/7 (RPMI-7951, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.82×** | +7.7 | 3e-12 | 2/6 (SW1417, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.37×** | +7.0 | 3e-10 | 8/9 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +5.6 | 2e-06 | 11/20 (RKO, C-33 A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +4.6 | 4e-04 | 8/12 (LoVo, SNU-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.68×** | +4.5 | 5e-04 | 10/17 (LS 180, RPMI-7951, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.004 | 9/17 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.82×** | +3.7 | 0.012 | 5/19 (RPMI-7951, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +3.4 | 0.041 | 7/18 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.1 | 0.099 | 0/14 | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.1 | 0.099 | 3/15 (HT-29, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4357.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SW480 0.203×; ⚠ cell-cycle shift, explains ~79% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyurea (drug)]] 5 µM |  | 0.580× | -3.2 | 0.83 | 3/20 (NCI-H1573, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +12.3) | — |
| [[SW1417 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +11.4) | — |
| [[SW480 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -9.3) ⚠ cell-cycle shift, explains ~79% of this change |
| [[A-172 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.856 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.925 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA10-AS]] | +0.76 | +0.62 / +0.80 | both halves | 7e-06 | ⚠ same locus (10.7 kb: neighbours can correlate without regulation) |
| [[ZCCHC3]] | +0.61 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[HNF1A]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[PPP4R3A]] | +0.60 | +0.37 / +0.50 | both halves | 9e-05 |  |
| [[NNT-AS1]] | +0.60 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[LATS1]] | +0.59 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[ZNF747]] | +0.59 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[REST]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[RNF146]] | +0.58 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[TLK2]] | +0.58 | +0.27 / +0.41 | both halves | 3e-04 |  |
| [[ZNF101]] | +0.58 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ZNF689]] | +0.58 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[TOPORS]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALU]] | -0.60 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SEC22B]] | -0.59 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[GGCX]] | -0.57 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TPMT]] | -0.57 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[ARHGAP8]] | -0.57 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[DAP]] | -0.55 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[RSU1]] | -0.54 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[TPD52L2]] | -0.54 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[KIF21B]] | -0.54 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[STRAP]] | -0.53 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[FAM91A1]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SAR1A]] | -0.52 | -0.54 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HOXA7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAR1A]] | B | HOXA7 activity raises SAR1A's level | lines that do not express HOXA7 (26) vs lines expressing it (24) | 1.14× lower at baseline in the lines without HOXA7 | 0.095 | ⚠ within organs, on part of the lines; also absent: NKD1, GRIN2B, LINC02253 |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (0.3, 9.3); signed map (28.3, -26.9). **Vector** length 33.8, 6.56% of its response variance represented; |z| ≥ 3 in 403 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +10.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.2 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.7 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +3.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -1.1 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.7 | -1.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.6 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.6 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.5 | -1.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | homeobox A7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,153,716-27,157,936 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX1A, HOX1 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P31268](https://www.uniprot.org/uniprotkb/P31268) (Homeobox protein Hox-A7):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3204](https://www.ncbi.nlm.nih.gov/gene/3204):

> In vertebrates, the genes encoding the class of transcription factors called homeobox genes are found in clusters named A, B, C, and D on four separate chromosomes. Expression of these proteins is spatially and temporally regulated during embryonic development. This gene is part of the A cluster on chromosome 7 and encodes a DNA-binding transcription factor which may regulate gene expression, morphogenesis, and differentiation. For example, the encoded protein represses the transcription of …

**Accessions** — [HGNC:5108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5108) · Entrez [3204](https://www.ncbi.nlm.nih.gov/gene/3204) · UniProt [P31268](https://www.uniprot.org/uniprotkb/P31268) · Ensembl [ENSG00000122592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122592)

## Data

Gene col 4357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4357); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4357]; `tensor/DDL_lfc|DDL_z.npy` [4357]; `embed/gene_vectors.npy` [4357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4357 or target_col == 4357). Every well: [[HOXA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
