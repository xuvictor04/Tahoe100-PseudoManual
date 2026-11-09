---
symbol: "AJM1"
type: "gene"
col: 13847
ensembl_id: "ENSG00000232434"
name: "apical junction component 1 homolog"
location: "9q34.3"
module: 126
arm: "+"
pooled_cpm: 4.14
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# AJM1

*apical junction component 1 homolog* — 9q34.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.215× (z -12.1, q 8e-31, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L2]] (+0.61, fdr 7e-06), [[CRYBB2P1]] (+0.61, fdr 7e-06), [[PXN-AS1]] (+0.58, fdr 1e-05); moves opposite to [[EIF6]] (-0.52, fdr 3e-05), [[SETX]] (-0.51, fdr 3e-05), [[TAF1B]] (-0.48, fdr 3e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.49× | +3.1 | 0.73 | 3/41 (HOP62, NCI-H23, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.215×** | -12.1 | 8e-31 | 42/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.220×** | -11.9 | 3e-30 | 39/45 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.358×** | -8.1 | 1e-13 | 33/45 (LoVo, COLO 205, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.349×** | -8.0 | 2e-13 | 30/42 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.441×** | -6.4 | 1e-08 | 29/46 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.458×** | -6.1 | 7e-08 | 22/37 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.562×** | -6.1 | 7e-08 | 23/37 (SNU-423, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.611×** | -3.9 | 0.007 | 15/45 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.621×** | -3.8 | 0.011 | 11/38 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.725×** | -3.5 | 0.023 | 20/46 (MIA PaCa-2, SNU-423, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.726×** | -3.5 | 0.023 | 10/45 (NCI-H2347, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 6.25 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0641× (z -10.4) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Pimozide (drug)]] 0.05 µM 0.0948× (z -9.3) |
| [[LoVo (line)]] | wt | 3.81 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0467× (z -10.6) |
| [[LS 180 (line)]] | wt | 6.23 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0948× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 4.84 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.139× (z -8.7) |
| [[SNU-423 (line)]] | alt | 6.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -9.4) |
| [[SW480 (line)]] | alt | 2.94 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.100× (z -9.1) |
| [[A-172 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L2]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CRYBB2P1]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PXN-AS1]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[EOLA1]] | +0.58 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PRSS53]] | +0.58 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[EOLA2]] | +0.57 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CCDC183]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 | ⚠ same locus (34.7 kb, same strand: neighbours can correlate without regulation) |
| [[LDB1]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[USP21]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[HOXA3]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TMEM94]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SH2B1]] | +0.55 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[IL11RA]] | +0.55 | +0.42 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF6]] | -0.52 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SETX]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[TAF1B]] | -0.48 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CRK]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SRGAP1]] | -0.48 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ASAP1]] | -0.47 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[KPNA4]] | -0.46 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[ZSWIM6]] | -0.46 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[EHBP1]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[BZW1]] | -0.45 | -0.37 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises AJM1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises AJM1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FGF11]] | B | FGF11 activity lowers AJM1's level | lines that do not express FGF11 (9) vs lines expressing it (41) | 1.38× higher at baseline in the lines without FGF11 | 0.096 | ⚠ within organs, on part of the lines; also absent: C9orf64, CYB5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.1, -23.1); signed map (-0.4, 3.9). **Vector** length 51.3, 6.48% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -8.0 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.2 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -3.9 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.9 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | apical junction component 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,842,478-136,848,801 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ajm-1; previously C9orf172 |
| Matched by | ensembl_id |

**Function**, from UniProt [C9J069](https://www.uniprot.org/uniprotkb/C9J069) (Apical junction component 1 homolog):

> May be involved in the control of adherens junction integrity.

**Summary**, from NCBI Gene [389813](https://www.ncbi.nlm.nih.gov/gene/389813):

> Predicted to be involved in cell-cell junction organization. Predicted to be located in adherens junction; apical plasma membrane; and cilium. Predicted to be active in apical junction complex and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37284) · Entrez [389813](https://www.ncbi.nlm.nih.gov/gene/389813) · UniProt [C9J069](https://www.uniprot.org/uniprotkb/C9J069) · Ensembl [ENSG00000232434](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232434)

## Data

Gene col 13847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13847); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13847]; `tensor/DDL_lfc|DDL_z.npy` [13847]; `embed/gene_vectors.npy` [13847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13847 or target_col == 13847). Every well: [[AJM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AJM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
