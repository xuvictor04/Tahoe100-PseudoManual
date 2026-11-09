---
symbol: "RPL32"
type: "gene"
col: 6918
ensembl_id: "ENSG00000144713"
name: "ribosomal protein L32"
location: "3p25.2"
module: 131
arm: "+"
pooled_cpm: 248.72
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPL32

*ribosomal protein L32* — 3p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.39× (z +8.3, q 6e-14, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 6.49×, NCI-H1573 4.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 5.62×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.594× (z -5.0, q 3e-04, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS25]] (+0.95, fdr 7e-06), [[RPS10]] (+0.95, fdr 7e-06), [[RPL28]] (+0.95, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RGS10]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6918.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 6.49×, NCI-H1573 4.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 5.62×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.39×** | +8.3 | 6e-14 | 48/49 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.76×** | +6.3 | 8e-08 | 41/44 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.21×** | +4.9 | 2e-04 | 43/45 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.97×** | +4.6 | 6e-04 | 47/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.4 | 0.057 | 39/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.65×** | +3.4 | 0.057 | 39/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.594×** | -5.0 | 3e-04 | 42/48 (C-33 A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 130 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.62× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 226 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 278 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 260 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 265 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 279 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 378 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 241 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 218 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 230 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 247 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 227 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 385 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 321 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 298 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 243 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 339 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 316 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 395 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 291 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS25]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS10]] | +0.95 | +0.94 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL28]] | +0.95 | +0.94 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS11]] | +0.94 | +0.94 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS21]] | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPLP2]] | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL8]] ⚠ | +0.94 | +0.89 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS23]] | +0.93 | +0.90 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL11]] | +0.93 | +0.90 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.93 | +0.87 / +0.92 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS5]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.93 | +0.89 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS10]] | C | RGS10 activity raises RPL32's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without RGS10 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |
| [[SPDL1]] | C | SPDL1 activity raises RPL32's level | lines that do not express SPDL1 (3) vs lines expressing it (47) | 1.39× lower at baseline in the lines without SPDL1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.952). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.8, -27.5); signed map (-61.5, -3.7). **Vector** length 85.9, 56.3% of its response variance represented; |z| ≥ 3 in 418 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-2 modulates host translation machinery* (reactome, mean cos +0.91 to 12); *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.92 to 11); *Formation of the ternary complex, and subsequently, the 43S complex* (reactome, mean cos +0.92 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +1.9 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.3 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -6.1 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -5.8 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.7 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -0.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.2 — chr3:12,834,485-12,841,582 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L32, eL32 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62910](https://www.uniprot.org/uniprotkb/P62910) (Large ribosomal subunit protein eL32):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6161](https://www.ncbi.nlm.nih.gov/gene/6161):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L32E family of ribosomal proteins. It is located in the cytoplasm. Although some studies have mapped this gene to 3q13.3-q21, it is believed to map to 3p25-p24. As is …

**Accessions** — [HGNC:10336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10336) · Entrez [6161](https://www.ncbi.nlm.nih.gov/gene/6161) · UniProt [P62910](https://www.uniprot.org/uniprotkb/P62910) · Ensembl [ENSG00000144713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144713)

## Data

Gene col 6918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6918); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6918]; `tensor/DDL_lfc|DDL_z.npy` [6918]; `embed/gene_vectors.npy` [6918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6918 or target_col == 6918). Every well: [[RPL32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
