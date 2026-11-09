---
symbol: "MAPKAPK5-AS1"
type: "gene"
col: 13969
ensembl_id: "ENSG00000234608"
name: "MAPKAPK5 antisense RNA 1"
location: "12q24.12"
module: 40
arm: "+"
pooled_cpm: 11.47
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# MAPKAPK5-AS1

*MAPKAPK5 antisense RNA 1* — 12q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +11.7, q 1e-28, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.691× (z -4.6, q 0.002, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFAF7]] (+0.70, fdr 3e-05), [[SCNM1]] (+0.69, fdr 7e-06), [[NCK1]] (+0.68, fdr 7e-06); moves opposite to [[DDX5]] (-0.59, fdr 3e-05), [[HNRNPA2B1]] (-0.59, fdr 3e-05), [[ASAP1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +11.7 | 1e-28 | 35/45 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +8.8 | 3e-16 | 34/40 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +8.6 | 1e-15 | 41/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +7.4 | 2e-11 | 37/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +6.3 | 3e-08 | 28/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +6.1 | 1e-07 | 29/48 (A498, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +5.8 | 5e-07 | 27/41 (NCI-H2030, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.2 | 0.002 | 18/35 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.8 | 0.008 | 8/21 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.094 | 9/48 (PANC-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.691×** | -4.6 | 0.002 | 20/47 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.748×** | -3.6 | 0.077 | 16/46 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.757×** | -3.5 | 0.077 | 14/47 (SW480, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.818×** | -3.5 | 0.077 | 18/46 (NCI-H460, SNU-423, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.773× | -3.0 | 0.28 | 7/48 (SHP-77, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.5 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -9.4) |
| [[PANC-1 (line)]] | alt | 12.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SK-MEL-2 (line)]] | alt | 6.48 | 0 | 2 | — | [[Tadalafil (drug)]] 5 µM 0.0472× (z -11.0) |
| [[A549 (line)]] | wt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +8.9) | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0861× (z -8.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HepG2_C3A (line)]] | wt | 9.52 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.101× (z -8.8) |
| [[KATO III (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.01× (z +14.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -8.6) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW48 (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -8.5) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-172 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | +0.70 | +0.46 / +0.74 | both halves | 3e-05 |  |
| [[SCNM1]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NCK1]] | +0.68 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.65 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[PPOX]] | +0.65 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CDADC1]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[ZNF836]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ELP2]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[MORN4]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MED10]] | +0.63 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ZFPL1]] | +0.62 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | +0.62 | +0.47 / +0.62 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.59 | -0.44 / -0.67 | both halves | 3e-05 |  |
| [[HNRNPA2B1]] | -0.59 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[ASAP1]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.57 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[CHD4]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[WDR1]] | -0.56 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[TEAD1]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[RASAL2]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[SMC1A]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[PSMD1]] | -0.55 | -0.51 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MAPKAPK5-AS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-1.6, -15.1); signed map (-35.8, -2.6). **Vector** length 64.6, 10.6% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.6 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +11.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -2.1 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -4.6 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -0.6 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | MAPKAPK5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q24.12 — chr12:111,839,758-111,842,902 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ39616, MAAS, lncRNA-cCSC1; previously C12orf47 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q8N8E1](https://www.uniprot.org/uniprotkb/Q8N8E1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24091) · Entrez [51275](https://www.ncbi.nlm.nih.gov/gene/51275) · UniProt [Q8N8E1](https://www.uniprot.org/uniprotkb/Q8N8E1) · Ensembl [ENSG00000234608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234608)

## Data

Gene col 13969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13969); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13969]; `tensor/DDL_lfc|DDL_z.npy` [13969]; `embed/gene_vectors.npy` [13969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13969 or target_col == 13969). Every well: [[MAPKAPK5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPKAPK5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
