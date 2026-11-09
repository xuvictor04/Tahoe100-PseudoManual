---
symbol: "MRPL41"
type: "gene"
col: 11248
ensembl_id: "ENSG00000182154"
name: "mitochondrial ribosomal protein L41"
location: "9q34.3"
module: 58
arm: "+"
pooled_cpm: 13.86
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# MRPL41

*mitochondrial ribosomal protein L41* — 9q34.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.35× (z +6.7, q 9e-09, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0597×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOB]] (+0.83, fdr 7e-06), [[ANAPC11]] (+0.83, fdr 7e-06), [[SF3B5]] (+0.81, fdr 8e-06, ⚠ SF3B5 in the vector space only through flagged drug-doses), [[C4orf48]] (+0.80, fdr 1e-05); moves opposite to [[DDX39B]] (-0.69, fdr 1e-05), [[EIF4G2]] (-0.68, fdr 2e-05), [[U2AF2]] (-0.68, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **3.35×** | +6.7 | 9e-09 | 46/47 (KATO III, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.16×** | +6.2 | 2e-07 | 39/42 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.76×** | +5.7 | 3e-06 | 44/47 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.39×** | +4.9 | 2e-04 | 40/47 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **2.15×** | +4.3 | 0.002 | 32/41 (HS-578T, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **2.32×** | +4.0 | 0.005 | 25/34 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **2.08×** | +3.9 | 0.007 | 18/26 (MIA PaCa-2, NCI-H460, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.96×** | +3.8 | 0.012 | 33/46 (SHP-77, SW480, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.89×** | +3.3 | 0.063 | 17/29 (KATO III, A549, …) | all doses, flat | composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0597×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.77 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0597× (z -8.9) |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 16 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOB]] | +0.83 | +0.73 / +0.81 | both halves | 7e-06 | STRING 422 |
| [[ANAPC11]] | +0.83 | +0.61 / +0.84 | both halves | 7e-06 |  |
| [[SF3B5]] ⚠ | +0.81 | +0.58 / +0.86 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[C4orf48]] | +0.80 | +0.52 / +0.82 | both halves | 1e-05 |  |
| [[MICOS13]] | +0.79 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[ATP5MK]] | +0.79 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.78 | +0.47 / +0.81 | both halves | 2e-05 |  |
| [[ROMO1]] | +0.78 | +0.64 / +0.80 | both halves | 7e-06 | STRING 402 |
| [[POP7]] | +0.77 | +0.47 / +0.80 | both halves | 2e-05 |  |
| [[LSM2]] | +0.77 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[LAGE3]] | +0.76 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.76 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.76 | +0.41 / +0.81 | both halves | 4e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX39B]] | -0.69 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.68 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[U2AF2]] | -0.68 | -0.30 / -0.64 | both halves | 2e-04 |  |
| [[HNRNPL]] | -0.67 | -0.49 / -0.59 | both halves | 1e-05 | STRING 453 |
| [[CHD3]] | -0.66 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TUG1]] | -0.65 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[EWSR1]] | -0.65 | -0.38 / -0.65 | both halves | 7e-05 |  |
| [[DDX3X]] | -0.65 | -0.30 / -0.67 | both halves | 2e-04 |  |
| [[PAPOLA]] | -0.64 | -0.34 / -0.68 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MRPL41's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-46.0, -18.9); signed map (-33.3, 7.7). **Vector** length 67.7, 19.7% of its response variance represented; |z| ≥ 3 in 481 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.53 to 12); *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.53 to 12); *Complex I biogenesis* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.3 | +6.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.1 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +3.0 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | +2.3 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | +1.0 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +2.1 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | +0.9 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +0.9 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | -5.5 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | -5.2 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | -4.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,551,879-137,552,555 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-L27, RPML27, BMRP, PIG3, MRPL27, mL41 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IXM3](https://www.uniprot.org/uniprotkb/Q8IXM3) (Large ribosomal subunit protein mL41):

> Component of the mitochondrial ribosome large subunit. Also involved in apoptosis and cell cycle. Enhances p53/TP53 stability, thereby contributing to p53/TP53-induced apoptosis in response to growth-inhibitory condition. Enhances p53/TP53 translocation to the mitochondria. Has the ability to arrest the cell cycle at the G1 phase, possibly by stabilizing the CDKN1A and CDKN1B (p27Kip1) proteins.

**Summary**, from NCBI Gene [64975](https://www.ncbi.nlm.nih.gov/gene/64975):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14492) · Entrez [64975](https://www.ncbi.nlm.nih.gov/gene/64975) · UniProt [Q8IXM3](https://www.uniprot.org/uniprotkb/Q8IXM3) · Ensembl [ENSG00000182154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182154)

## Data

Gene col 11248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11248); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11248]; `tensor/DDL_lfc|DDL_z.npy` [11248]; `embed/gene_vectors.npy` [11248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11248 or target_col == 11248). Every well: [[MRPL41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
