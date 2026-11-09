---
symbol: "ALKBH7"
type: "gene"
col: 4639
ensembl_id: "ENSG00000125652"
name: "alkB homolog 7, RNA demethylase"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 5.86
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ALKBH7

*alkB homolog 7, RNA demethylase* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 2.23× (z +6.0, q 1e-06, up in 22 of 33 measured lines) ⚠ transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.08× (z +3.9, q 0.018, up in 11 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.425× (z -9.1, q 7e-17, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX14]] (+0.80, fdr 7e-06), [[RABAC1]] (+0.80, fdr 7e-06), [[PTOV1]] (+0.77, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.68, fdr 7e-06), [[HNRNPA2B1]] (-0.65, fdr 8e-06), [[PDAP1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.23×** | +6.0 | 1e-06 | 22/33 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +4.7 | 8e-04 | 18/27 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.08×** | +3.9 | 0.018 | 11/30 (SW480, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.92×** | +3.5 | 0.076 | 15/43 (AsPC-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.56× | +3.2 | 0.15 | 1/11 (J82) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.80× | +3.1 | 0.17 | 11/40 (Hs 766T, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.50× | +3.0 | 0.19 | 15/40 (SNU-423, NCI-H23, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.425×** | -9.1 | 7e-17 | 32/41 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.302×** | -9.0 | 8e-17 | 34/39 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -5.2 | 5e-05 | 28/45 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.589×** | -4.0 | 0.010 | 22/43 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.612×** | -3.7 | 0.026 | 16/46 (SNU-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.612×** | -3.5 | 0.049 | 18/44 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.641×** | -3.3 | 0.069 | 15/47 (HS-578T, HCT15, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.635× | -3.1 | 0.12 | 18/38 (NCI-H460, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.662× | -3.1 | 0.13 | 15/47 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -10.3) |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -10.3) |
| [[HT-29 (line)]] | alt | 5.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -8.7) |
| [[J82 (line)]] | alt | 4.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0686× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 9.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 6.08 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -8.9) |
| [[PANC-1 (line)]] | alt | 6.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 4.90 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0623× (z -8.6) |
| [[SW 900 (line)]] | alt | 6.04 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0465× (z -10.2) |
| [[SW480 (line)]] | alt | 4.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -9.8) |
| [[A-172 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX14]] | +0.80 | +0.59 / +0.81 | both halves | 7e-06 |  |
| [[RABAC1]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[PTOV1]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.75 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[NENF]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[WDR83OS]] ⚠ | +0.74 | +0.53 / +0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | +0.74 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[RPS11]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.73 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[LAMTOR2]] | +0.73 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[HIGD2A]] | +0.72 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.72 | +0.58 / +0.71 | both halves | 8e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.68 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[HNRNPA2B1]] | -0.65 | -0.57 / -0.61 | both halves | 8e-06 |  |
| [[PDAP1]] | -0.64 | -0.52 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.4, -21.5); signed map (-32.8, 10.6). **Vector** length 61.2, 11.1% of its response variance represented; |z| ≥ 3 in 636 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | alkB homolog 7, RNA demethylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,372,794-6,375,250 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10974; previously SPATA11 |
| Gene groups (HGNC) | Alkylation repair homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT30](https://www.uniprot.org/uniprotkb/Q9BT30) (RNA demethylase ALKBH7, mitochondrial):

> RNA demethylase that demethylates N(2)-dimethylguanosine and N(1)-methyladenosine within mitochondrial pre-tRNA regions. This demethylation activity plays a crucial role in regulating the processing of nascent polycistronic mitochondrial RNA, thereby influencing mitochondrial gene expression and overall mitochondrial activity. In response to extensive DNA damage is required for programmed necrosis induced by alkylation and oxidation. Acts by triggering the collapse of mitochondrial membrane …

**Summary**, from NCBI Gene [84266](https://www.ncbi.nlm.nih.gov/gene/84266):

> Enables tRNA demethylase activity. Involved in DNA damage response; oxidative RNA demethylation; and regulation of mitochondrial membrane permeability involved in programmed necrotic cell death. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21306) · Entrez [84266](https://www.ncbi.nlm.nih.gov/gene/84266) · UniProt [Q9BT30](https://www.uniprot.org/uniprotkb/Q9BT30) · Ensembl [ENSG00000125652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125652)

## Data

Gene col 4639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4639); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4639]; `tensor/DDL_lfc|DDL_z.npy` [4639]; `embed/gene_vectors.npy` [4639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4639 or target_col == 4639). Every well: [[ALKBH7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALKBH7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
