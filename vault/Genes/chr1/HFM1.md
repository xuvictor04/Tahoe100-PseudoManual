---
symbol: "HFM1"
type: "gene"
col: 8558
ensembl_id: "ENSG00000162669"
name: "helicase for meiosis 1"
location: "1p22.2"
module: 20
arm: "+"
pooled_cpm: 4.42
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# HFM1

*helicase for meiosis 1* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.38× (z +9.1, q 7e-17, up in 21 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +6.5, q 2e-08, up in 22 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD30BL]] (+0.84, fdr 7e-06), [[RPL10]] (+0.76, fdr 8e-06), [[RPL18A]] (+0.75, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.66, fdr 1e-05), [[CEBPZ]] (-0.63, fdr 3e-05), [[PIGBOS1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +9.1 | 7e-17 | 21/25 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +7.9 | 7e-13 | 8/9 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.5 | 2e-08 | 22/39 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +5.9 | 5e-07 | 7/11 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +5.7 | 1e-06 | 18/48 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +5.5 | 5e-06 | 14/27 (A-172, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +4.6 | 4e-04 | 21/44 (HEC-1-A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.004 | 13/45 (RPMI-7951, CFPAC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.035 | 4/46 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.042 | 2/46 (HEC-1-A, KATO III) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.075 | 7/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8558.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Apalutamide (drug)]] 0.05 µM |  | 0.592× | -3.4 | 0.18 | 11/43 (A-427, SW48, …) | inconsistent across doses | position effect removed |
| [[Lipoic acid (drug)]] 5 µM |  | 0.725× | -3.4 | 0.18 | 8/47 (NCI-H661, NCI-H460, …) | rises with dose | position effect removed |
| [[Apalutamide (drug)]] 5 µM |  | 0.630× | -3.3 | 0.18 | 7/44 (SNU-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.658× | -3.1 | 0.26 | 11/46 (Panc 03.27, HOP62, …) | inconsistent across doses |  |
| [[Altretamine (drug)]] 5 µM |  | 0.656× | -3.0 | 0.29 | 13/45 (J82, A-427, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD30BL]] | +0.84 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RPL10]] | +0.76 | +0.58 / +0.76 | both halves | 8e-06 | **novel candidate** |
| [[RPL18A]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[DHFR]] | +0.70 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RPS18]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RMRP]] | +0.67 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[CTSZ]] | +0.67 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[EOLA2]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[AP1G2-AS1]] | +0.67 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[LENG8]] | +0.66 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[EEF1A1P5]] | +0.66 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.66 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.63 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[PIGBOS1]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[MRPS18B]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[TTF1]] | -0.57 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[MRPS18C]] | -0.57 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[NKAP]] | -0.54 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[ZNF503]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[PDCD7]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[NEMF]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SMIM26]] ⚠ | -0.52 | -0.30 / -0.51 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL46]] | -0.52 | -0.22 / -0.55 | both halves | 6e-04 |  |
| [[ISG20L2]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers HFM1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.5, -25.3); signed map (-21.2, -34.3). **Vector** length 49.0, 5.57% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.54 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.54 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.57 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.1 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -0.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.2 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.5 | -3.1 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.4 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.2 | -0.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | helicase for meiosis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:91,260,766-91,404,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MER3, FLJ39011, FLJ36760; previously SEC63D1 |
| Matched by | ensembl_id |

**Function**, from UniProt [A2PYH4](https://www.uniprot.org/uniprotkb/A2PYH4) (Probable ATP-dependent DNA helicase HFM1):

> Required for crossover formation and complete synapsis of homologous chromosomes during meiosis.

**Summary**, from NCBI Gene [164045](https://www.ncbi.nlm.nih.gov/gene/164045):

> The protein encoded by this gene is thought to be an ATP-dependent DNA helicase and is expressed mainly in germ-line cells. Defects in this gene are a cause of premature ovarian failure 9 (POF9). [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:20193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20193) · Entrez [164045](https://www.ncbi.nlm.nih.gov/gene/164045) · UniProt [A2PYH4](https://www.uniprot.org/uniprotkb/A2PYH4) · Ensembl [ENSG00000162669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162669)

## Data

Gene col 8558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8558); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8558]; `tensor/DDL_lfc|DDL_z.npy` [8558]; `embed/gene_vectors.npy` [8558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8558 or target_col == 8558). Every well: [[HFM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HFM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
