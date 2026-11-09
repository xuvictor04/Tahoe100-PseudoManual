---
symbol: "SLC9C1"
type: "gene"
col: 10215
ensembl_id: "ENSG00000172139"
name: "solute carrier family 9 member C1"
location: "3q13.2"
module: 75
arm: "+"
pooled_cpm: 2.93
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# SLC9C1

*solute carrier family 9 member C1* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.83× (z +13.3, q 2e-37, up in 30 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.167×; ⚠ toxic; transcription drop); [[Lactate (calcium) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0590×); [[Irinotecan (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0473×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC4C]] (+0.83, fdr 7e-06), [[MIR4300HG]] (+0.80, fdr 7e-06), [[USH2A]] (+0.77, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +13.3 | 2e-37 | 30/34 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.95×** | +12.4 | 5e-33 | 11/14 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +11.8 | 8e-30 | 3/4 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.14×** | +11.7 | 2e-29 | 3/6 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +10.5 | 1e-23 | 24/34 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +7.2 | 8e-11 | 11/29 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.18×** | +7.0 | 2e-10 | 24/40 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.3 | 2e-08 | 20/43 (KATO III, CFPAC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.91×** | +5.9 | 3e-07 | 3/11 (C32, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +5.6 | 1e-06 | 17/37 (HOP62, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +5.2 | 1e-05 | 15/33 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.1 | 1e-05 | 10/34 (LOX-IMVI, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.8 | 6e-05 | 12/42 (A-172, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +4.6 | 2e-04 | 13/38 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.002 | 9/38 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.003 | 11/42 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.005 | 10/43 (SNU-423, HOP62, …) | all doses, flat | cell-cycle shift (explains ~25% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.8 | 0.005 | 16/43 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.018 | 6/34 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10215.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LoVo 0.167×; ⚠ toxic; transcription drop); [[Lactate (calcium) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0590×); [[Irinotecan (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.0473×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -3.2 | 0.83 | 14/46 (SW48, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 3.71 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 5 µM 0.0473× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 2.90 | 0 | 1 | — | [[Lactate (calcium) (drug)]] 0.5 µM 0.0590× (z -9.4) |
| [[LoVo (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC4C]] | +0.83 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.80 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[USH2A]] | +0.77 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MYO16]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.76 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[OBI1-AS1]] | +0.75 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[DPP6]] | +0.75 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[XKR4]] | +0.75 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[FEZ1]] | +0.74 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.74 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.73 | +0.69 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC9C1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.3% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC00457]] | B | LINC00457 activity raises SLC9C1's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.30× lower at baseline in the lines without LINC00457 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent |
| [[ALDH1A2]] | B | ALDH1A2 activity raises SLC9C1's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.28× lower at baseline in the lines without ALDH1A2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.5, 28.0); signed map (32.0, 14.0). **Vector** length 46.5, 5.31% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.5 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:112,140,898-112,294,227 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NHE; previously SLC9A10 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0N8](https://www.uniprot.org/uniprotkb/Q4G0N8) (Solute carrier family 9 member C1):

> Sperm-specific solute carrier involved in intracellular pH regulation of spermatozoa. Required for sperm motility and fertility. Involved in sperm cell hyperactivation, a step needed for sperm motility which is essential late in the preparation of sperm for fertilization. Required for the expression and bicarbonate regulation of the soluble adenylyl cyclase (ADCY10).

**Summary**, from NCBI Gene [285335](https://www.ncbi.nlm.nih.gov/gene/285335):

> Predicted to enable potassium:proton antiporter activity and sodium:proton antiporter activity. Predicted to be involved in potassium ion transmembrane transport; regulation of intracellular pH; and sodium ion import across plasma membrane. Predicted to act upstream of or within flagellated sperm motility. Predicted to be located in membrane and motile cilium. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31401) · Entrez [285335](https://www.ncbi.nlm.nih.gov/gene/285335) · UniProt [Q4G0N8](https://www.uniprot.org/uniprotkb/Q4G0N8) · Ensembl [ENSG00000172139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172139)

## Data

Gene col 10215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10215); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10215]; `tensor/DDL_lfc|DDL_z.npy` [10215]; `embed/gene_vectors.npy` [10215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10215 or target_col == 10215). Every well: [[SLC9C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
