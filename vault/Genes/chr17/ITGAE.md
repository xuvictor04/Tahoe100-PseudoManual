---
symbol: "ITGAE"
type: "gene"
col: 1371
ensembl_id: "ENSG00000083457"
name: "integrin subunit alpha E"
location: "17p13.2"
module: 21
arm: "+"
pooled_cpm: 11.22
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ITGAE

*integrin subunit alpha E* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +11.4, q 3e-27, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.679× (z -4.1, q 0.020, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.205×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.213×; ⚠ cell-cycle shift, would explain all of this change); [[Arbutin (drug)]] 0.05 µM in 1 line (SW48 0.0761×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASP6]] (+0.65, fdr 1e-05), [[NDUFS3]] (+0.61, fdr 1e-05), [[MAIP1]] (+0.60, fdr 1e-05); moves opposite to [[SERBP1]] (-0.53, fdr 2e-04), [[PPM1G]] (-0.49, fdr 1e-04), [[EML4]] (-0.48, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +11.4 | 3e-27 | 36/45 (A498, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +10.4 | 4e-23 | 17/20 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +10.1 | 1e-21 | 31/35 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.0 | 4e-10 | 23/29 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.76×** | +6.1 | 1e-07 | 29/47 (NCI-H460, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.5 | 5e-06 | 27/43 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +5.4 | 6e-06 | 24/47 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +5.0 | 4e-05 | 23/48 (HS-578T, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.1 | 0.002 | 17/40 (hTERT-HPNE, HCT15, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.9 | 0.005 | 19/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.44×** | +3.9 | 0.005 | 19/40 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1371.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.205×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.213×; ⚠ cell-cycle shift, would explain all of this change); [[Arbutin (drug)]] 0.05 µM in 1 line (SW48 0.0761×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -4.1 | 0.020 | 19/47 (HepG2/C3A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 8.96 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.09× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.33× (z +12.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.7) | — |
| [[A549 (line)]] | wt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.70× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 8.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.205× (z -9.6) |
| [[PANC-1 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 11.8 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0761× (z -8.5) |
| [[A-172 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP6]] | +0.65 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[NDUFS3]] | +0.61 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CARNMT1-AS1]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[RPRD2]] | +0.58 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[MYLK3]] | +0.58 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[ZNF451-AS1]] | +0.57 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[ABCC11]] | +0.57 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[PPP1R42]] | +0.56 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MDP1]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[TMEM94]] | +0.55 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[FHIP2A]] | +0.55 | +0.32 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERBP1]] | -0.53 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[PPM1G]] | -0.49 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[EML4]] | -0.48 | -0.49 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.1, 17.5); signed map (22.8, -13.2). **Vector** length 55.6, 8.55% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +11.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.5 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -2.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.0 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,714,628-3,801,188 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD103, HUMINAE |
| Gene groups (HGNC) | CD molecules; Integrin alpha subunits |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 2 pathways, smallest: Integrin cell surface interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P38570](https://www.uniprot.org/uniprotkb/P38570) (Integrin alpha-E):

> Integrin ITGAE/ITGB7 (alpha-E/beta-7) is a receptor for E-cadherin. It mediates adhesion of intra-epithelial T-lymphocytes to epithelial cell monolayers.

**Summary**, from NCBI Gene [3682](https://www.ncbi.nlm.nih.gov/gene/3682):

> Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. This gene encodes an I-domain-containing alpha integrin that undergoes post-translational cleavage in the extracellular domain, yielding disulfide-linked heavy and light chains. In combination with the beta 7 integrin, this protein forms the E-cadherin binding integrin known as the human mucosal lymphocyte-1 antigen. This protein is preferentially expressed in human intestinal intraepithelial …

**Accessions** — [HGNC:6147](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6147) · Entrez [3682](https://www.ncbi.nlm.nih.gov/gene/3682) · UniProt [P38570](https://www.uniprot.org/uniprotkb/P38570) · Ensembl [ENSG00000083457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083457)

## Data

Gene col 1371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1371); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1371]; `tensor/DDL_lfc|DDL_z.npy` [1371]; `embed/gene_vectors.npy` [1371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1371 or target_col == 1371). Every well: [[ITGAE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGAE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
