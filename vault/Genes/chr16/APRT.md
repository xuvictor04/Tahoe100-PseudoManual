---
symbol: "APRT"
type: "gene"
col: 12744
ensembl_id: "ENSG00000198931"
name: "adenine phosphoribosyltransferase"
location: "16q24.3"
module: 58
arm: "+"
pooled_cpm: 14.62
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# APRT

*adenine phosphoribosyltransferase* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.93× (z +9.3, q 1e-17, up in 35 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 7.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.548× (z -5.4, q 3e-05, down in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.191×, NCI-H2030 0.207×, LoVo 0.230×, MIA PaCa-2 0.270×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0568×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM147]] (+0.71, fdr 7e-06), [[UQCR11]] (+0.65, fdr 7e-06), [[MICOS13]] (+0.64, fdr 7e-06); moves opposite to [[PLEKHA3]] (-0.53, fdr 1e-04), [[EXOSC8]] (-0.49, fdr 8e-05), [[CCT6P3]] (-0.48, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12744.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (MIA PaCa-2 7.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **4.93×** | +9.3 | 1e-17 | 35/37 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.83×** | +8.2 | 6e-14 | 25/26 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.01×** | +6.5 | 2e-08 | 28/32 (A549, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **2.00×** | +4.4 | 0.001 | 32/42 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.1 | 0.004 | 33/39 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.86×** | +3.9 | 0.008 | 30/46 (NCI-H1573, HOP62, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12744.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.191×, NCI-H2030 0.207×, LoVo 0.230×, MIA PaCa-2 0.270×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0568×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.548×** | -5.4 | 3e-05 | 33/47 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.621× | -3.0 | 0.47 | 23/45 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.14× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.9) |
| [[A-427 (line)]] | wt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -12.0) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 7.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0568× (z -9.4) |
| [[SW480 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -8.5) |
| [[A-172 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM147]] | +0.71 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[MICOS13]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SLC39A4]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ATP5MF]] | +0.63 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[NAXE]] | +0.62 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[TSPO]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CD320]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[TIMM10]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CST3]] | +0.58 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[NHP2]] | +0.58 | +0.64 / +0.57 | both halves | 1e-05 | STRING 603 |
| [[ATP5MC3]] ⚠ | +0.58 | +0.57 / +0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF5AL1]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHA3]] | -0.53 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[EXOSC8]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[CCT6P3]] | -0.48 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[TSR2]] | -0.47 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[CIRBP]] | -0.47 | -0.54 / -0.20 | both halves | 7e-04 |  |
| [[SUPT5H]] | -0.46 | -0.51 / -0.41 | both halves | 4e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[DXO]] | -0.45 | -0.49 / -0.21 | both halves | 6e-04 |  |
| [[SUGT1]] | -0.45 | -0.63 / -0.27 | both halves | 3e-04 |  |
| [[SUGT1P3]] | -0.45 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[SRRM1]] | -0.44 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[AAAS]] | -0.43 | -0.49 / -0.35 | both halves | 1e-04 | pathway: HALLMARK_DNA_REPAIR |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.3, -20.9); signed map (-36.1, 11.3). **Vector** length 54.4, 12.6% of its response variance represented; |z| ≥ 3 in 545 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +3.4 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.0 | +2.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.0 | +1.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +0.9 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | adenine phosphoribosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:88,809,339-88,811,937 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphoribosyltransferases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 8 pathways, smallest: Nucleotide salvage defects; Diseases of nucleotide metabolism; Purine salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [P07741](https://www.uniprot.org/uniprotkb/P07741) (Adenine phosphoribosyltransferase):

> Catalyzes a salvage reaction resulting in the formation of AMP, that is energically less costly than de novo synthesis.

**Summary**, from NCBI Gene [353](https://www.ncbi.nlm.nih.gov/gene/353):

> Adenine phosphoribosyltransferase belongs to the purine/pyrimidine phosphoribosyltransferase family. A conserved feature of this gene is the distribution of CpG dinucleotides. This enzyme catalyzes the formation of AMP and inorganic pyrophosphate from adenine and 5-phosphoribosyl-1-pyrophosphate (PRPP). It also produces adenine as a by-product of the polyamine biosynthesis pathway. A homozygous deficiency in this enzyme causes 2,8-dihydroxyadenine urolithiasis. Two transcript variants encoding …

**Accessions** — [HGNC:626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:626) · Entrez [353](https://www.ncbi.nlm.nih.gov/gene/353) · UniProt [P07741](https://www.uniprot.org/uniprotkb/P07741) · Ensembl [ENSG00000198931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198931)

## Data

Gene col 12744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12744); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12744]; `tensor/DDL_lfc|DDL_z.npy` [12744]; `embed/gene_vectors.npy` [12744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12744 or target_col == 12744). Every well: [[APRT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APRT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
