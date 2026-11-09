---
symbol: "RPL36"
type: "gene"
col: 5041
ensembl_id: "ENSG00000130255"
name: "ribosomal protein L36"
location: "19p13.3"
module: 43
arm: "+"
pooled_cpm: 245.15
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL36

*ribosomal protein L36* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.25× (z +6.0, q 1e-06, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.589× (z -3.8, q 0.078, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL35A]] (+0.95, fdr 7e-06), [[RPL31]] (+0.95, fdr 7e-06), [[RPL18]] (+0.95, fdr 7e-06, ⚠ RPL18 in the vector space only through flagged drug-doses), [[RPS27]] (+0.95, fdr 7e-06); moves opposite to [[PSME3]] (-0.75, fdr 7e-06), [[PNPO]] (-0.73, fdr 7e-06), [[FGD5-AS1]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.25×** | +6.0 | 1e-06 | 49/49 (COLO 205, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.8 | 3e-04 | 47/47 (HepG2/C3A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.66×** | +4.8 | 3e-04 | 43/44 (HT-29, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **2.08×** | +3.8 | 0.024 | 44/48 (NCI-H2347, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | 1.88× | +3.2 | 0.14 | 43/48 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | 1.89× | +3.0 | 0.25 | 32/45 (Panc 03.27, SW480, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.589×** | -3.8 | 0.078 | 38/48 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.521× | -3.1 | 0.44 | 48/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.524× | -3.0 | 0.44 | 46/48 (RKO, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 288 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 231 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 238 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 249 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 224 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 228 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 215 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 209 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 261 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 218 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 178 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 431 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 361 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 385 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 271 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 325 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 315 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 377 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 248 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 7 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL35A]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL18]] ⚠ | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: HALLMARK_P53_PATHWAY; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS17]] ⚠ | +0.95 | +0.90 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35]] ⚠ | +0.94 | +0.88 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS19]] | +0.94 | +0.93 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL9]] ⚠ | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS29]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS12]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 999 |
| [[RPL34]] | +0.92 | +0.87 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL26]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.91 | +0.88 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.91 | +0.82 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.75 | -0.63 / -0.77 | both halves | 7e-06 |  |
| [[PNPO]] | -0.73 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[FGD5-AS1]] | -0.73 | -0.69 / -0.68 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.912). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.9, -26.5); signed map (-59.5, -3.6). **Vector** length 91.9, 64.4% of its response variance represented; |z| ≥ 3 in 385 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.75 to 19); *Translation initiation complex formation* (reactome, mean cos +0.70 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.70 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.1 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -8.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -8.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -7.8 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.7 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | +0.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.2 | -0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,674,947-5,691,875 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp566B023, L36, eL36 |
| Gene groups (HGNC) | L ribosomal proteins |
| Hallmark sets | P53_PATHWAY |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [C0HME6](https://www.uniprot.org/uniprotkb/C0HME6) (RPL36 alternative reading frame protein):

> Inhibits C2CD2L/TMEM24-dependent transport of phosphatidylinositol, the precursor of phosphatidylinositol 4,5-bisphosphate (PI(4,5)P2), from its site of synthesis in the endoplasmic reticulum to the cell membrane. This leads to down-regulation of the PI3K-AKT-mTOR signaling pathway.

**Summary**, from NCBI Gene [25873](https://www.ncbi.nlm.nih.gov/gene/25873):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L36E family of ribosomal proteins. It is located in the cytoplasm. Transcript variants derived from alternative splicing exist; they encode the same protein. As is typical …

**Accessions** — [HGNC:13631](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13631) · Entrez [25873](https://www.ncbi.nlm.nih.gov/gene/25873) · UniProt [C0HME6](https://www.uniprot.org/uniprotkb/C0HME6) · Ensembl [ENSG00000130255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130255)

## Data

Gene col 5041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5041); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5041]; `tensor/DDL_lfc|DDL_z.npy` [5041]; `embed/gene_vectors.npy` [5041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5041 or target_col == 5041). Every well: [[RPL36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
