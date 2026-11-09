---
symbol: "FAAP24"
type: "gene"
col: 5260
ensembl_id: "ENSG00000131944"
name: "FA core complex associated protein 24"
location: "19q13.11"
module: 203
arm: "+"
pooled_cpm: 5.72
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/203"]
generated_by: "tahoemap"
---

# FAAP24

*FA core complex associated protein 24* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.00× (z +5.3, q 5e-05, up in 20 of 26 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.59× (z +5.2, q 5e-05, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.462× (z -6.1, q 6e-07, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTF1]] (+0.61, fdr 2e-05), [[C1orf131]] (+0.61, fdr 1e-05), [[ZNF430]] (+0.60, fdr 3e-05); moves opposite to [[NCOR2]] (-0.58, fdr 3e-05), [[RSU1]] (-0.53, fdr 4e-05), [[FKBP1A]] (-0.53, fdr 6e-05).
> It is in [[Module 203]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +5.3 | 5e-05 | 20/26 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +5.2 | 5e-05 | 16/46 (NCI-H2030, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +4.6 | 9e-04 | 12/28 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +4.4 | 0.001 | 19/47 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +4.4 | 0.001 | 3/8 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.016 | 15/41 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.027 | 17/45 (HT-29, A549, …) | top dose only | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.462×** | -6.1 | 6e-07 | 28/47 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.518×** | -5.2 | 6e-05 | 25/47 (SNU-423, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -4.4 | 0.002 | 22/45 (LS 180, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.597×** | -4.1 | 0.006 | 17/47 (RPMI-7951, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -4.0 | 0.006 | 18/43 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.401×** | -3.8 | 0.015 | 22/38 (A-172, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.719×** | -3.7 | 0.018 | 18/45 (RPMI-7951, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.720×** | -3.7 | 0.018 | 15/39 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.452×** | -3.3 | 0.064 | 15/43 (A-172, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.662×** | -3.3 | 0.065 | 12/47 (SNU-423, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **0.674×** | -3.1 | 0.095 | 11/43 (NCI-H23, AN3 CA, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.86 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 6.27 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0670× (z -9.7) |
| [[SNU-423 (line)]] | alt | 4.84 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0357× (z -12.3) |
| [[A-427 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTF1]] | +0.61 | +0.46 / +0.74 | both halves | 2e-05 |  |
| [[C1orf131]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[ZNF430]] | +0.60 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[ZCCHC10]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[COIL]] | +0.59 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[ZNF85]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[KBTBD4]] | +0.59 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[CPT2]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[ADPRS]] | +0.58 | +0.42 / +0.69 | both halves | 4e-05 |  |
| [[TOPORS]] | +0.58 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[ZNF830]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.57 | +0.45 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOR2]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[RSU1]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[FKBP1A]] | -0.53 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[CNN2]] | -0.52 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[COL18A1]] | -0.52 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[GNG12]] | -0.51 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RFLNA]] | -0.51 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[STT3B]] | -0.51 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[G6PD]] | -0.51 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[CORO1C]] | -0.51 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[ACTN4]] | -0.50 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[MPRIP]] | -0.50 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 203]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-51.8, -6.0); signed map (-7.5, -12.7). **Vector** length 61.8, 10.5% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.2 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | FA core complex associated protein 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:32,972,209-32,978,229 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46828, MGC32020; previously C19orf40 |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTP7](https://www.uniprot.org/uniprotkb/Q9BTP7) (Fanconi anemia core complex-associated protein 24):

> Plays a role in DNA repair through recruitment of the FA core complex to damaged DNA. Regulates FANCD2 monoubiquitination upon DNA damage. Induces chromosomal instability as well as hypersensitivity to DNA cross-linking agents, when repressed. Targets FANCM/FAAP24 complex to the DNA, preferentially to single strand DNA.

**Summary**, from NCBI Gene [91442](https://www.ncbi.nlm.nih.gov/gene/91442):

> FAAP24 is a component of the Fanconi anemia (FA) core complex (see MIM 227650), which plays a crucial role in DNA damage response (Ciccia et al., 2007 [PubMed 17289582]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28467) · Entrez [91442](https://www.ncbi.nlm.nih.gov/gene/91442) · UniProt [Q9BTP7](https://www.uniprot.org/uniprotkb/Q9BTP7) · Ensembl [ENSG00000131944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131944)

## Data

Gene col 5260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5260); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5260]; `tensor/DDL_lfc|DDL_z.npy` [5260]; `embed/gene_vectors.npy` [5260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5260 or target_col == 5260). Every well: [[FAAP24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAAP24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
