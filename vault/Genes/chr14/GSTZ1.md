---
symbol: "GSTZ1"
type: "gene"
col: 1989
ensembl_id: "ENSG00000100577"
name: "glutathione S-transferase zeta 1"
location: "14q24.3"
module: 35
arm: "+"
pooled_cpm: 4.18
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# GSTZ1

*glutathione S-transferase zeta 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +9.4, q 3e-18, up in 14 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +7.5, q 2e-11, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.674× (z -5.7, q 5e-06, down in 18 of 38 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRRM2-AS1]] (+0.67, fdr 1e-05), [[CCDC90B-AS1]] (+0.65, fdr 2e-05), [[FBXL19-AS1]] (+0.65, fdr 5e-05); moves opposite to [[NBPF3]] (-0.54, fdr 7e-05), [[MAST3]] (-0.52, fdr 5e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +9.4 | 3e-18 | 14/22 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +8.9 | 2e-16 | 4/8 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +7.5 | 2e-11 | 24/36 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.88×** | +4.6 | 6e-04 | 7/22 (SNU-423, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.55×** | +4.5 | 7e-04 | 10/46 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.9 | 0.007 | 5/9 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +3.9 | 0.008 | 8/24 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.16 | 10/45 (A549, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1989.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.674×** | -5.7 | 5e-06 | 18/38 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.629×** | -4.8 | 4e-04 | 15/45 (HS-578T, KATO III, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.631×** | -4.7 | 4e-04 | 19/44 (J82, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.647×** | -4.5 | 0.001 | 17/47 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.699×** | -3.7 | 0.026 | 15/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.717×** | -3.4 | 0.050 | 13/47 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.529×** | -3.4 | 0.050 | 12/35 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -3.2 | 0.089 | 14/37 (HCT15, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.36 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.107× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 5.97 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0972× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0790× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 6.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -9.2) |
| [[A-172 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRM2-AS1]] | +0.67 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.65 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[FBXL19-AS1]] | +0.65 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[IDNK]] | +0.64 | +0.58 / +0.40 | both halves | 4e-05 |  |
| [[FAM174B]] | +0.64 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[MED13]] | +0.62 | +0.50 / +0.22 | both halves | 6e-04 |  |
| [[C11orf71]] | +0.62 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[RNPC3-DT]] | +0.61 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[NINJ2]] | +0.61 | +0.42 / +0.28 | both halves | 3e-04 |  |
| [[AP5S1]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[AHI1-DT]] | +0.59 | +0.54 / +0.30 | both halves | 2e-04 |  |
| [[MZF1-AS1]] | +0.59 | +0.39 / +0.57 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.54 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[MAST3]] | -0.52 | -0.37 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GSTZ1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.8, 13.3); signed map (25.3, -4.9). **Vector** length 38.4, 3.70% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase zeta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,320,996-77,331,597 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GSTZ1-1, MAAI, MAI |
| Gene groups (HGNC) | Soluble glutathione S-transferases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 10 pathways, smallest: Tyrosine catabolism; Phenylalanine and tyrosine metabolism; Regulation of pyruvate dehydrogenase (PDH) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O43708](https://www.uniprot.org/uniprotkb/O43708) (Maleylacetoacetate isomerase):

> Bifunctional enzyme showing minimal glutathione-conjugating activity with ethacrynic acid and 7-chloro-4-nitrobenz-2-oxa-1,3-diazole and maleylacetoacetate isomerase activity. Also has low glutathione peroxidase activity with T-butyl and cumene hydroperoxides. Is able to catalyze the glutathione dependent oxygenation of dichloroacetic acid to glyoxylic acid.

**Summary**, from NCBI Gene [2954](https://www.ncbi.nlm.nih.gov/gene/2954):

> This gene is a member of the glutathione S-transferase (GSTs) super-family which encodes multifunctional enzymes important in the detoxification of electrophilic molecules, including carcinogens, mutagens, and several therapeutic drugs, by conjugation with glutathione. This enzyme catalyzes the conversion of maleylacetoacetate to fumarylacetoacatate, which is one of the steps in the phenylalanine/tyrosine degradation pathway. Deficiency of a similar gene in mouse causes oxidative stress. …

**Accessions** — [HGNC:4643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4643) · Entrez [2954](https://www.ncbi.nlm.nih.gov/gene/2954) · UniProt [O43708](https://www.uniprot.org/uniprotkb/O43708) · Ensembl [ENSG00000100577](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100577)

## Data

Gene col 1989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1989); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1989]; `tensor/DDL_lfc|DDL_z.npy` [1989]; `embed/gene_vectors.npy` [1989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1989 or target_col == 1989). Every well: [[GSTZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
