---
symbol: "SGCZ"
type: "gene"
col: 11618
ensembl_id: "ENSG00000185053"
name: "sarcoglycan zeta"
location: "8p22"
module: 61
arm: "+"
pooled_cpm: 3.3
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# SGCZ

*sarcoglycan zeta* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.59× (z +24.5, q 0e+00, up in 30 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0863×); [[Furosemide (drug)]] 0.05 µM in 1 line (SHP-77 0.0581×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.147×; ⚠ toxic; cell-cycle shift, explains ~20% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRT]] (+0.85, fdr 7e-06), [[LINC02511]] (+0.85, fdr 7e-06), [[USH2A]] (+0.84, fdr 7e-06).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.59×** | +24.5 | 0e+00 | 30/30 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.34×** | +15.7 | 0e+00 | 36/45 (NCI-H460, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.63×** | +15.3 | 0e+00 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.23×** | +15.3 | 0e+00 | 29/34 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.22×** | +15.2 | 0e+00 | 7/11 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.80×** | +13.4 | 1e-38 | 2/2 (A498, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.62×** | +11.8 | 2e-30 | 32/40 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.30×** | +7.4 | 1e-11 | 20/39 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +7.0 | 2e-10 | 22/39 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +6.7 | 9e-10 | 22/43 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +6.5 | 3e-09 | 14/36 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +6.1 | 4e-08 | 21/45 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +5.9 | 1e-07 | 21/44 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +5.7 | 4e-07 | 3/11 (A498, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.7 | 4e-07 | 10/27 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +5.7 | 4e-07 | 19/44 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.2 | 5e-06 | 13/32 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.001 | 8/30 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.003 | 3/44 (A498, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0863×); [[Furosemide (drug)]] 0.05 µM in 1 line (SHP-77 0.0581×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.147×; ⚠ toxic; cell-cycle shift, explains ~20% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.02 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 15.8× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 2.91 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 17.2× (z +10.2) | — |
| [[A-427 (line)]] | wt | 52.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0863× (z -11.0) |
| [[KATO III (line)]] | alt | 4.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.79× (z +9.3) | — |
| [[A498 (line)]] | wt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +10.9) | — |
| [[A549 (line)]] | wt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +8.9) | — |
| [[C32 (line)]] | wt | 2.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 29.3× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 2.13 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.8× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 1.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +11.2) | — |
| [[LoVo (line)]] | wt | 1.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.6× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 1.76 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.7× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 7.93 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0581× (z -9.4) |
| [[SW480 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.72× (z +10.6) | — |
| [[A-172 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRT]] | +0.85 | +0.66 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[LINC02511]] | +0.85 | +0.74 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[USH2A]] | +0.84 | +0.78 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[XKR4]] | +0.82 | +0.79 / +0.85 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.81 | +0.78 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CNBD1]] | +0.81 | +0.70 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[DLGAP2]] | +0.81 | +0.74 / +0.87 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.80 | +0.79 / +0.88 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.79 | +0.69 / +0.84 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.79 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.79 | +0.63 / +0.88 | both halves | 7e-06 |  |
| [[DACH2]] | +0.79 | +0.79 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SGCZ's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, 30.0); signed map (32.3, 16.4). **Vector** length 53.2, 6.96% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.52 to 14); *Transmission across Chemical Synapses* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +15.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +24.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +15.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | sarcoglycan zeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:14,084,845-15,238,431 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZSG1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Sarcoglycans |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LD1](https://www.uniprot.org/uniprotkb/Q96LD1) (Zeta-sarcoglycan):

> Component of the sarcoglycan complex, a subcomplex of the dystrophin-glycoprotein complex which forms a link between the F-actin cytoskeleton and the extracellular matrix. May play a role in the maintenance of striated muscle membrane stability (By similarity).

**Summary**, from NCBI Gene [137868](https://www.ncbi.nlm.nih.gov/gene/137868):

> The zeta-sarcoglycan gene measures over 465 kb and localizes to 8p22. This protein is part of the sarcoglycan complex, a group of 6 proteins. The sarcoglycans are all N-glycosylated transmembrane proteins with a short intra-cellular domain, a single transmembrane region and a large extra-cellular domain containing a carboxyl-terminal cluster with several conserved cysteine residues. The sarcoglycan complex is part of the dystrophin-associated glycoprotein complex (DGC), which bridges the inner …

**Accessions** — [HGNC:14075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14075) · Entrez [137868](https://www.ncbi.nlm.nih.gov/gene/137868) · UniProt [Q96LD1](https://www.uniprot.org/uniprotkb/Q96LD1) · Ensembl [ENSG00000185053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185053)

## Data

Gene col 11618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11618); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11618]; `tensor/DDL_lfc|DDL_z.npy` [11618]; `embed/gene_vectors.npy` [11618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11618 or target_col == 11618). Every well: [[SGCZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGCZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
