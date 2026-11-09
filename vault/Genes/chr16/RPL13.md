---
symbol: "RPL13"
type: "gene"
col: 9480
ensembl_id: "ENSG00000167526"
name: "ribosomal protein L13"
location: "16q24.3"
module: 43
arm: "+"
pooled_cpm: 130.88
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPL13

*ribosomal protein L13* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.32× (z +7.8, q 3e-12, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 6.16×, NCI-H1573 5.37×, LoVo 4.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.535× (z -5.8, q 4e-06, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 0.325×, NCI-H2030 0.356×, C-33 A 0.348×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL26]] (+0.97, fdr 7e-06), [[RPL31]] (+0.97, fdr 7e-06), [[RPS14]] (+0.96, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF532]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9480.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1792 6.16×, NCI-H1573 5.37×, LoVo 4.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.32×** | +7.8 | 3e-12 | 49/49 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.76×** | +6.4 | 4e-08 | 41/44 (NCI-H1792, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.03×** | +4.6 | 7e-04 | 42/48 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.99×** | +4.2 | 0.004 | 37/45 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.9 | 0.012 | 44/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9480.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 0.325×, NCI-H2030 0.356×, C-33 A 0.348×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.535×** | -5.8 | 4e-06 | 42/48 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9480. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -8.8) |
| [[LoVo (line)]] | wt | 203 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1573 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 268 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -8.9) |
| [[RKO (line)]] | wt | 204 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.4) |
| [[A-172 (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 110 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 146 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 147 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9480), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 23 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL26]] | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.97 | +0.95 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.96 | +0.95 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.95 | +0.93 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.95 | +0.90 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL27]] | +0.95 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.95 | +0.93 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | +0.94 | +0.92 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF532]] | B | ZNF532 activity lowers RPL13's level | lines that do not express ZNF532 (6) vs lines expressing it (44) | 1.55× higher at baseline in the lines without ZNF532 | 0.079 | ⚠ within organs, on part of the lines; also absent: PXMP4, ADAL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.965). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.8, -27.8); signed map (-60.5, -4.3). **Vector** length 86.9, 49.1% of its response variance represented; |z| ≥ 3 in 427 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.81 to 19); *Translation initiation complex formation* (reactome, mean cos +0.78 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.78 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +0.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.4 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -6.2 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -0.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -0.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,560,677-89,564,542 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D16S444E, BBC1, L13, eL13 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P26373](https://www.uniprot.org/uniprotkb/P26373) (Large ribosomal subunit protein eL13):

> Component of the ribosome, a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. The small ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the encoded message by selecting cognate aminoacyl-transfer RNA (tRNA) molecules (Probable). The large subunit (LSU) contains the ribosomal catalytic site termed the peptidyl transferase center (PTC), which catalyzes the formation of peptide bonds, thereby polymerizing the amino acids delivered by tRNAs …

**Summary**, from NCBI Gene [6137](https://www.ncbi.nlm.nih.gov/gene/6137):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L13E family of ribosomal proteins. It is located in the cytoplasm. This gene is expressed at significantly higher levels in benign breast lesions than in breast carcinomas. …

**Accessions** — [HGNC:10303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10303) · Entrez [6137](https://www.ncbi.nlm.nih.gov/gene/6137) · UniProt [P26373](https://www.uniprot.org/uniprotkb/P26373) · Ensembl [ENSG00000167526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167526)

## Data

Gene col 9480: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9480); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9480, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9480]; `tensor/DDL_lfc|DDL_z.npy` [9480]; `embed/gene_vectors.npy` [9480]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9480 or target_col == 9480). Every well: [[RPL13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
