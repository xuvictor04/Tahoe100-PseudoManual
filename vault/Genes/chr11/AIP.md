---
symbol: "AIP"
type: "gene"
col: 3158
ensembl_id: "ENSG00000110711"
name: "AHR interacting HSP90 co-chaperone"
location: "11q13.2"
module: 130
arm: "+"
pooled_cpm: 13.61
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# AIP

*AHR interacting HSP90 co-chaperone* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.29× (z +9.4, q 3e-18, up in 39 of 48 measured lines) ⚠ position not correctable. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.591× (z -5.9, q 2e-06, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKRN1]] (+0.58, fdr 3e-05), [[POLDIP3]] (+0.56, fdr 2e-05), [[UBXN6]] (+0.55, fdr 1e-05); moves opposite to [[LCP1]] (-0.42, fdr 5e-04), [[PPM1G]] (-0.42, fdr 1e-04), [[CCDC88A]] (-0.42, fdr 5e-05).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.29×** | +9.4 | 3e-18 | 39/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +7.9 | 8e-13 | 29/37 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +7.0 | 4e-10 | 28/42 (NCI-H2030, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.8 | 1e-09 | 19/26 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.0 | 8e-05 | 21/33 (Hs 766T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -5.9 | 2e-06 | 27/46 (NCI-H2347, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.649×** | -4.8 | 4e-04 | 24/47 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.669×** | -4.5 | 0.001 | 22/48 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -3.9 | 0.013 | 19/48 (NCI-H23, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -3.6 | 0.032 | 18/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.061 | 25/47 (AsPC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.754× | -3.2 | 0.13 | 14/47 (NCI-H661, A-427, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 0.762× | -3.0 | 0.16 | 16/45 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | 0.550× | -3.0 | 0.16 | 8/48 (A-427, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.2) |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.0) |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.8) |
| [[A-172 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN1]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[POLDIP3]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[UBXN6]] | +0.55 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ALKBH7]] | +0.55 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PTRHD1]] ⚠ | +0.54 | +0.53 / +0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC115]] | +0.51 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[TSEN34]] | +0.51 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SHISA4]] | +0.50 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[GID8]] | +0.50 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[KLC4]] | +0.50 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[MRPL11]] | +0.49 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MRPL43]] | +0.49 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[XAB2]] | +0.49 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCP1]] | -0.42 | -0.24 / -0.38 | both halves | 5e-04 | pathway: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation |
| [[PPM1G]] | -0.42 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CCDC88A]] | -0.42 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PALM2AKAP2]] | -0.42 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[CHML]] | -0.42 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[LYAR]] | -0.41 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[DCBLD2]] | -0.40 | -0.27 / -0.39 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises AIP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.5, -51.8); signed map (-10.9, 2.0). **Vector** length 43.8, 5.97% of its response variance represented; |z| ≥ 3 in 579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.9 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | -0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.1 | -0.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | AHR interacting HSP90 co-chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,468,174-67,491,154 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XAP2, ARA9, FKBP16, FKBP37 |
| Gene groups (HGNC) | FKBP prolyl isomerase family; MicroRNA protein coding host genes |
| Reactome | 8 pathways, smallest: Aryl hydrocarbon receptor signalling; Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O00170](https://www.uniprot.org/uniprotkb/O00170) (AH receptor-interacting protein):

> May play a positive role in AHR-mediated (aromatic hydrocarbon receptor) signaling, possibly by influencing its receptivity for ligand and/or its nuclear targeting.; Cellular negative regulator of the hepatitis B virus (HBV) X protein.

**Summary**, from NCBI Gene [9049](https://www.ncbi.nlm.nih.gov/gene/9049):

> The protein encoded by this gene is a receptor for aryl hydrocarbons and a ligand-activated transcription factor. The encoded protein is found in the cytoplasm as part of a multiprotein complex, but upon binding of ligand is transported to the nucleus. This protein can regulate the expression of many xenobiotic metabolizing enzymes. Also, the encoded protein can bind specifically to and inhibit the activity of hepatitis B virus. Three transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:358) · Entrez [9049](https://www.ncbi.nlm.nih.gov/gene/9049) · UniProt [O00170](https://www.uniprot.org/uniprotkb/O00170) · Ensembl [ENSG00000110711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110711)

## Data

Gene col 3158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3158); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3158]; `tensor/DDL_lfc|DDL_z.npy` [3158]; `embed/gene_vectors.npy` [3158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3158 or target_col == 3158). Every well: [[AIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
