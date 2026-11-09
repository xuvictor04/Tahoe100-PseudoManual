---
symbol: "RPS29"
type: "gene"
col: 13132
ensembl_id: "ENSG00000213741"
name: "ribosomal protein S29"
location: "14q21.3"
module: 131
arm: "+"
pooled_cpm: 224.29
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPS29

*ribosomal protein S29* — 14q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.65× (z +6.6, q 3e-08, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +3.5, q 0.035, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.594× (z -4.1, q 0.025, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.300×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP2]] (+0.96, fdr 7e-06), [[RPS13]] (+0.94, fdr 7e-06, ⚠ RPS13 in the vector space only through flagged drug-doses), [[RPS27A]] (+0.94, fdr 7e-06, ⚠ RPS27A in the vector space only through flagged drug-doses), [[RPS10]] (+0.94, fdr 7e-06), [[RPL36A]] (+0.94, fdr 7e-06); moves opposite to [[PNPO]] (-0.73, fdr 7e-06), [[EIF4G1]] (-0.71, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ESRP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13132.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.65×** | +6.6 | 3e-08 | 49/49 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.66×** | +5.2 | 6e-05 | 42/44 (A549, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.23×** | +4.1 | 0.009 | 42/45 (HT-29, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.98×** | +3.8 | 0.021 | 44/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.97×** | +3.7 | 0.021 | 44/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.7 | 0.023 | 45/47 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.035 | 41/49 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13132.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.300×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.594×** | -4.1 | 0.025 | 39/48 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13132. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 262 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.3) |
| [[A-172 (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 278 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 193 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 202 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 243 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 282 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 178 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 215 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 426 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 239 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 293 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 262 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 301 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 422 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13132), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP2]] | +0.96 | +0.95 / +0.98 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS27A]] ⚠ | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS10]] | +0.94 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL36A]] | +0.94 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.93 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL36]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL28]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL9]] ⚠ | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.93 | +0.88 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.92 | +0.86 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL32]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNPO]] | -0.73 | -0.66 / -0.73 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.71 | -0.67 / -0.68 | both halves | 7e-06 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 856 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRP2]] | B | ESRP2 activity raises RPS29's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.44× lower at baseline in the lines without ESRP2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.961). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.3, -26.7); signed map (-61.0, -3.2). **Vector** length 88.5, 60.5% of its response variance represented; |z| ≥ 3 in 401 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.91 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +2.3 | +3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -7.6 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -7.5 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -7.1 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | +1.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | -3.5 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | +0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.3 — chr14:49,570,984-49,599,164 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S29, uS14 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62273](https://www.uniprot.org/uniprotkb/P62273) (Small ribosomal subunit protein uS14):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6235](https://www.ncbi.nlm.nih.gov/gene/6235):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit and a member of the S14P family of ribosomal proteins. The protein, which contains a C2-C2 zinc finger-like domain that can bind to zinc, can enhance the tumor suppressor activity of Ras-related …

**Accessions** — [HGNC:10419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10419) · Entrez [6235](https://www.ncbi.nlm.nih.gov/gene/6235) · UniProt [P62273](https://www.uniprot.org/uniprotkb/P62273) · Ensembl [ENSG00000213741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213741)

## Data

Gene col 13132: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13132); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13132, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13132]; `tensor/DDL_lfc|DDL_z.npy` [13132]; `embed/gene_vectors.npy` [13132]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13132 or target_col == 13132). Every well: [[RPS29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
