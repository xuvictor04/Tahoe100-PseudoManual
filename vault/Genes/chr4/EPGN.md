---
symbol: "EPGN"
type: "gene"
col: 11304
ensembl_id: "ENSG00000182585"
name: "epithelial mitogen"
location: "4q13.3"
module: 19
arm: "+"
pooled_cpm: 9.86
n_lines_expressing: 9
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# EPGN

*epithelial mitogen* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.93× (z +8.9, q 2e-16, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.72× (z +3.7, q 0.026, up in 1 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.525× (z -4.1, q 0.028, down in 2 of 7 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRD1]] (+0.72, fdr 7e-06), [[LINC03000]] (+0.72, fdr 7e-06), [[SLC15A5]] (+0.72, fdr 7e-06); moves opposite to [[NR0B1]] (-0.48, fdr 1e-04), [[SPNS2]] (-0.46, fdr 1e-04), [[ADRA2C]] (-0.44, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ESM1]] → it (grade C ⚠); 6 go from it, the strongest it → [[ADRA2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.93×** | +8.9 | 2e-16 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +7.4 | 3e-11 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +6.2 | 1e-07 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +4.4 | 0.002 | 1/6 (NCI-H2030) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +3.7 | 0.026 | 1/7 (NCI-H1573) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.46×** | +3.6 | 0.031 | 0/6 | top dose only | composition shift; position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +3.3 | 0.081 | 0/5 | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.95×** | +3.2 | 0.087 | 2/6 (NCI-H2030, A-427) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.90× | +3.1 | 0.13 | 2/6 (NCI-H2030, NCI-H460) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.525×** | -4.1 | 0.028 | 2/7 (BT-474, H4) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.581×** | -3.7 | 0.060 | 3/7 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.599×** | -3.5 | 0.087 | 4/7 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.621× | -3.0 | 0.37 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0568× (z -22.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0482× (z -17.1) |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0770× (z -18.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.174× (z -8.9) |
| [[A-172 (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.972 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.785 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.897 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRD1]] | +0.72 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[SLC15A5]] | +0.72 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.71 | +0.65 / +0.62 | both halves | 7e-06 | pathway: Intracellular signaling by second messengers |
| [[SERPINB11]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[DPP10]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.70 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[GTF2I-AS1]] | +0.67 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CTNND2]] | +0.67 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[COL4A6]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MAPK4]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 | pathway: MAPK family signaling cascades |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR0B1]] | -0.48 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[SPNS2]] | -0.46 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ADRA2C]] | -0.44 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[TOMM20L-DT]] | -0.42 | -0.50 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESM1]] | C | ESM1 activity raises EPGN's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.23× lower at baseline in the lines without ESM1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[GDA]] | C | GDA activity raises EPGN's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.71× lower at baseline in the lines without GDA | 0.062 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[MAPK4]] | C | MAPK4 activity raises EPGN's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 2.56× lower at baseline in the lines without MAPK4 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADRA2C]] | B | EPGN activity raises ADRA2C's level | lines that do not express EPGN (41) vs lines expressing it (9) | 2.32× lower at baseline in the lines without EPGN | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418 |
| [[MAPK4]] | C | EPGN activity raises MAPK4's level | lines that do not express EPGN (41) vs lines expressing it (9) | 3.31× lower at baseline in the lines without EPGN | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |
| [[NR2E3]] | C | EPGN activity raises NR2E3's level | lines that do not express EPGN (41) vs lines expressing it (9) | 3.03× lower at baseline in the lines without EPGN | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |
| [[GRAMD1B]] | C | EPGN activity raises GRAMD1B's level | lines that do not express EPGN (41) vs lines expressing it (9) | 6.52× lower at baseline in the lines without EPGN | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |
| [[LRRC63]] | C | EPGN activity raises LRRC63's level | lines that do not express EPGN (41) vs lines expressing it (9) | 2.38× lower at baseline in the lines without EPGN | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |
| [[CTNND2]] | C | EPGN activity raises CTNND2's level | lines that do not express EPGN (41) vs lines expressing it (9) | 3.80× lower at baseline in the lines without EPGN | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, 36.8); signed map (43.5, 44.2). **Vector** length 34.8, 15.3% of its response variance represented; |z| ≥ 3 in 206 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.0 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.0 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.8 | +8.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.7 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.6 | +1.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.5 | +1.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.5 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -0.7 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.6 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.5 | -2.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.5 | +0.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | epithelial mitogen |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:74,308,470-74,316,789 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EPG, PRO9904, ALGV3072 |
| Gene groups (HGNC) | EGF ligand family |
| Reactome | 28 pathways, smallest: Inhibition of Signaling by Overexpressed EGFR; Signaling by Overexpressed Wild-Type EGFR in Cancer; EGFR interacts with phospholipase C-gamma |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UW88](https://www.uniprot.org/uniprotkb/Q6UW88) (Epigen):

> Promotes the growth of epithelial cells. May stimulate the phosphorylation of EGFR and mitogen-activated protein kinases.

**Summary**, from NCBI Gene [255324](https://www.ncbi.nlm.nih.gov/gene/255324):

> The protein encoded by this gene is a member of the epidermal growth factor family. Members of this family are ligands for the epidermal growth factor receptor and play a role in cell survival, proliferation and migration. This protein has been reported to have high mitogenic activity but low affinity for its receptor. Expression of this transcript and protein have been reported in cancer specimens of the breast, bladder, and prostate. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:17470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17470) · Entrez [255324](https://www.ncbi.nlm.nih.gov/gene/255324) · UniProt [Q6UW88](https://www.uniprot.org/uniprotkb/Q6UW88) · Ensembl [ENSG00000182585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182585)

## Data

Gene col 11304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11304); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11304]; `tensor/DDL_lfc|DDL_z.npy` [11304]; `embed/gene_vectors.npy` [11304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11304 or target_col == 11304). Every well: [[EPGN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPGN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
