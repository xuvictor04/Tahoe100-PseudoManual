---
symbol: "ADGRE3"
type: "gene"
col: 5194
ensembl_id: "ENSG00000131355"
name: "adhesion G protein-coupled receptor E3"
location: "19p13.12"
module: 78
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ADGRE3

*adhesion G protein-coupled receptor E3* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.11× (z +16.6, q 0e+00, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +9.5, q 3e-19, up in 15 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.722× (z -3.5, q 0.094, down in 11 of 43 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB1]] (+0.66, fdr 1e-05), [[BTNL12P]] (+0.63, fdr 2e-04), [[TMBIM6]] (+0.57, fdr 3e-05); moves opposite to [[NSUN5]] (-0.58, fdr 3e-05), [[MRPL58]] (-0.56, fdr 3e-05), [[KBTBD6]] (-0.56, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.11×** | +16.6 | 0e+00 | 3/3 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.89×** | +14.4 | 2e-44 | 11/11 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.67×** | +12.7 | 8e-35 | 5/6 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +9.5 | 3e-19 | 15/30 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.1 | 1e-07 | 7/22 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.93×** | +5.9 | 3e-07 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +5.2 | 1e-05 | 9/36 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.002 | 5/31 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.47×** | +4.1 | 0.003 | 2/9 (SW480, PANC-1) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.5 | 0.026 | 5/20 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.39×** | +3.4 | 0.028 | 7/46 (AsPC-1, PANC-1, …) | rises with dose | composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.58×** | +3.4 | 0.028 | 1/2 (hTERT-HPNE) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.040 | 4/32 (hTERT-HPNE, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.35×** | +3.1 | 0.074 | 6/39 (SW480, NCI-H460, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.0 | 0.088 | 2/19 (NCI-H2347, A549) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5194.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.722×** | -3.5 | 0.094 | 11/43 (RKO, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Trimetrexate (drug)]] 0.5 µM |  | **0.723×** | -3.5 | 0.094 | 5/34 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.716×** | -3.5 | 0.094 | 7/37 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | 0.737× | -3.2 | 0.18 | 7/38 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.739× | -3.2 | 0.18 | 6/41 (NCI-H2030, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.758× | -3.0 | 0.24 | 10/36 (PANC-1, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 24 of them with an alert (⚠; 24 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1]] | +0.66 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[BTNL12P]] | +0.63 | +0.30 / +0.73 | both halves | 2e-04 |  |
| [[TMBIM6]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[APLP2]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[LINC02458]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[LAMC1]] | +0.55 | +0.68 / +0.37 | both halves | 8e-05 |  |
| [[SAXO1]] | +0.54 | +0.23 / +0.61 | both halves | 5e-04 |  |
| [[MATN3]] | +0.54 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ATP8A2]] | +0.54 | +0.12 / +0.60 | ⚠ one half (not replicated) | 0.002 |  |
| [[HRG-AS1]] | +0.54 | +0.12 / +0.67 | ⚠ one half (not replicated) | 0.002 |  |
| [[MYH11]] | +0.53 | +0.17 / +0.66 | ⚠ one half (not replicated) | 0.001 |  |
| [[GEMIN7-AS1]] | +0.53 | +0.11 / +0.68 | ⚠ one half (not replicated) | 0.002 |  |
| [[ASPH]] | +0.53 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[SNX32]] | +0.52 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[ECM1]] | +0.52 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[IDS]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[MRPL58]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[KBTBD6]] | -0.56 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[MKS1]] | -0.54 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[PHAX]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CIAO3]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SNHG11]] | -0.52 | -0.49 / -0.49 | both halves | 2e-05 |  |
| [[RBMX2]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MRPS18B]] | -0.52 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[EXOSC9]] | -0.52 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[TMEM265]] | -0.52 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[WDR75]] | -0.50 | -0.31 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.1, 22.9); signed map (35.3, 9.0). **Vector** length 25.5, 1.74% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +14.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.5 | +1.5 |
|  | [[Pimozide (drug)]] 0.05 µM |  | +0.4 | +0.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.7 | -0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -1.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -0.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor E3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,619,117-14,690,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EMR3 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily E |
| Reactome | 5 pathways, smallest: Class B/2 (Secretin family receptors); GPCR ligand binding; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY15](https://www.uniprot.org/uniprotkb/Q9BY15) (Adhesion G protein-coupled receptor E3):

> Orphan receptor that may play a role myeloid-myeloid interactions during immune and inflammatory responses. A ligand for the soluble form of this receptor is present at the surface of monocytes-derived macrophages and activated neutrophils.

**Summary**, from NCBI Gene [84658](https://www.ncbi.nlm.nih.gov/gene/84658):

> This gene encodes a member of the class B seven-span transmembrane (TM7) receptor family expressed predominantly by cells of the immune system. Family members are characterized by an extended extracellular region with a variable number of N-terminal epidermal growth factor (EGF)-like domains coupled to a TM7 domain via a mucin-like spacer domain. This gene is closely linked to the gene encoding egf-like molecule containing mucin-like hormone receptor 2 on chromosome 19. This protein may play a …

**Accessions** — [HGNC:23647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23647) · Entrez [84658](https://www.ncbi.nlm.nih.gov/gene/84658) · UniProt [Q9BY15](https://www.uniprot.org/uniprotkb/Q9BY15) · Ensembl [ENSG00000131355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131355)

## Data

Gene col 5194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5194); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5194]; `tensor/DDL_lfc|DDL_z.npy` [5194]; `embed/gene_vectors.npy` [5194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5194 or target_col == 5194). Every well: [[ADGRE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
