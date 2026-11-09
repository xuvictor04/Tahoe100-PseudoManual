---
symbol: "OPLAH"
type: "gene"
col: 10963
ensembl_id: "ENSG00000178814"
name: "5-oxoprolinase, ATP-hydrolysing"
location: "8q24.3"
module: 96
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 40
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/096", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# OPLAH

*5-oxoprolinase, ATP-hydrolysing* — 8q24.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.10× (z +8.0, q 5e-13, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.566× (z -4.0, q 0.030, down in 13 of 33 measured lines) ⚠ cell-cycle shift, explains ~49% of this change.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR6]] (+0.70, fdr 7e-06), [[ZNF783]] (+0.67, fdr 7e-06, ⚠ ZNF783 in the vector space only through flagged drug-doses), [[PLA2G4B]] (+0.65, fdr 7e-06), [[JMJD7]] (+0.65, fdr 7e-06); moves opposite to [[MLLT3]] (-0.49, fdr 3e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MLLT3]] → it (grade B ⚠); 6 go from it, the strongest it → cells under [[Ixazomib citrate (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +8.0 | 5e-13 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +5.1 | 1e-04 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +5.0 | 1e-04 | 2/7 (AsPC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.39×** | +3.5 | 0.075 | 3/36 (NCI-H23, COLO 205, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.566×** | -4.0 | 0.030 | 13/33 (RKO, SW1417, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.634× | -3.3 | 0.25 | 10/35 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 0.645× | -3.1 | 0.30 | 9/27 (LoVo, A549, …) | top dose only | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | 0.656× | -3.1 | 0.30 | 12/35 (HOP62, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.135 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.643 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.755 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.929 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR6]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ZNF783]] ⚠ | +0.67 | +0.61 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PLA2G4B]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[JMJD7]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[EME2]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MED16]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[WIZ]] | +0.62 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[MAPK12]] | +0.62 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[KAT2A]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NSMF]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 | same gene group |
| [[SLC4A3]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NRBP2]] | +0.60 | +0.55 / +0.64 | both halves | 1e-05 | same gene group |
| [[ANAPC2]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLLT3]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MLLT3]] | B | MLLT3 activity lowers OPLAH's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.01× higher at baseline in the lines without MLLT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ixazomib citrate (drug)]] 5 µM | C | OPLAH activity raises the cells' numbers under Ixazomib citrate 5 µM (protects the cells) | lines that do not express OPLAH (10) vs lines expressing it (38) | the lines without OPLAH: 0.66× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; co-occurs with TERT; also absent: TNFRSF10D, PATJ, EPHX2 |
| cells under [[Neratinib (maleate) (drug)]] 5 µM | C | OPLAH activity raises the cells' numbers under Neratinib (maleate) 5 µM (protects the cells) | lines that do not express OPLAH (10) vs lines expressing it (38) | the lines without OPLAH: 0.89× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; co-occurs with TERT; also absent: TNFRSF10D, PATJ, EPHX2 |
| cells under [[Bortezomib (drug)]] 0.5 µM | C | OPLAH activity raises the cells' numbers under Bortezomib 0.5 µM (protects the cells) | lines that do not express OPLAH (10) vs lines expressing it (38) | the lines without OPLAH: 0.84× the cells of the other lines | 0.029 | ⚠ tissue-confounded; across organs; co-occurs with TERT; also absent: TNFRSF10D, PATJ, EPHX2 |
| cells under [[Topotecan (hydrochloride) (drug)]] 0.5 µM | C | OPLAH activity raises the cells' numbers under Topotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express OPLAH (10) vs lines expressing it (38) | the lines without OPLAH: 0.81× the cells of the other lines | 0.060 | ⚠ tissue-confounded; across organs; co-occurs with TERT; also absent: TNFRSF10D, PATJ, EPHX2 |
| cells under [[Elimusertib hydrochloride (drug)]] 5 µM | C | OPLAH activity raises the cells' numbers under Elimusertib hydrochloride 5 µM (protects the cells) | lines that do not express OPLAH (10) vs lines expressing it (38) | the lines without OPLAH: 0.77× the cells of the other lines | 0.076 | ⚠ tissue-confounded; across organs; co-occurs with TERT; also absent: TNFRSF10D, PATJ, EPHX2 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | C | OPLAH activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express OPLAH (10) vs lines expressing it (38) | the lines without OPLAH: 0.87× the cells of the other lines | 0.096 | ⚠ tissue-confounded; across organs; co-occurs with TERT; also absent: TNFRSF10D, PATJ, EPHX2 |

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: all its genes lie on one side of its main direction.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-10.7, -24.1); signed map (-11.9, -32.1). **Vector** length 40.1, 5.21% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | 5-oxoprolinase, ATP-hydrolysing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,051,266-144,063,965 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OPLA, 5-Opase |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Glutathione synthesis and recycling; Metabolic disorders of biological oxidation enzymes; Glutathione conjugation |
| Matched by | ensembl_id |

**Function**, from UniProt [O14841](https://www.uniprot.org/uniprotkb/O14841) (5-oxoprolinase):

> Catalyzes the cleavage of 5-oxo-L-proline to form L-glutamate coupled to the hydrolysis of ATP to ADP and inorganic phosphate.

**Summary**, from NCBI Gene [26873](https://www.ncbi.nlm.nih.gov/gene/26873):

> The protein encoded by this gene acts as a homodimer, using ATP hydrolysis to catalyze the conversion of 5-oxo-L-proline to L-glutamate. Defects in this gene are a cause of 5-oxoprolinase deficiency (OPLAHD). [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:8149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8149) · Entrez [26873](https://www.ncbi.nlm.nih.gov/gene/26873) · UniProt [O14841](https://www.uniprot.org/uniprotkb/O14841) · Ensembl [ENSG00000178814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178814)

## Data

Gene col 10963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10963); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10963]; `tensor/DDL_lfc|DDL_z.npy` [10963]; `embed/gene_vectors.npy` [10963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10963 or target_col == 10963). Every well: [[OPLAH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OPLAH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
