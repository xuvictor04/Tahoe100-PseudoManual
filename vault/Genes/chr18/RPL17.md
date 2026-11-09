---
symbol: "RPL17"
type: "gene"
col: 15464
ensembl_id: "ENSG00000265681"
name: "ribosomal protein L17"
location: "18q21.1"
module: 43
arm: "+"
pooled_cpm: 230.64
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

# RPL17

*ribosomal protein L17* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.35× (z +5.0, q 3e-04, up in 44 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.31×; ⚠ cell-cycle shift, explains ~17% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.598× (z -5.1, q 2e-04, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C-33 A 0.268×, RKO 0.358×, AN3 CA 0.321×, SNU-1 0.379×, …).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL26]] (+0.97, fdr 7e-06), [[RPL23]] (+0.96, fdr 7e-06), [[RPL34]] (+0.96, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NID1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15464.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.31×; ⚠ cell-cycle shift, explains ~17% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.35×** | +5.0 | 3e-04 | 44/49 (COLO 205, A549, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.99×** | +4.9 | 3e-04 | 46/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.4 | 0.002 | 46/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.89×** | +4.3 | 0.002 | 34/44 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.85×** | +4.2 | 0.003 | 42/47 (COLO 205, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | 1.59× | +3.0 | 0.20 | 34/45 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | 1.53× | +3.0 | 0.20 | 38/48 (NCI-H460, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15464.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C-33 A 0.268×, RKO 0.358×, AN3 CA 0.321×, SNU-1 0.379×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -5.1 | 2e-04 | 40/48 (C-33 A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 288 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.4) |
| [[BT-474 (line)]] | alt | 226 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.5) |
| [[C-33 A (line)]] | alt | 400 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.9) |
| [[CHP-212 (line)]] | wt | 261 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 292 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.5) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[RKO (line)]] | wt | 364 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.7) |
| [[SNU-1 (line)]] | wt | 286 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.3) |
| [[A-172 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 205 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 226 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 249 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 263 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 214 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 259 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 262 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 238 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 408 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 353 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 358 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 374 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 239 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 467 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL26]] | +0.97 | +0.95 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.96 | +0.93 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.96 | +0.93 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 997 |
| [[RPL31]] | +0.95 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS17]] ⚠ | +0.95 | +0.88 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL13]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35]] ⚠ | +0.94 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL9]] ⚠ | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPS3]] ⚠ | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL19]] | +0.93 | +0.90 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS8]] | +0.93 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL5]] | +0.93 | +0.91 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RPS12]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NID1]] | B | NID1 activity lowers RPL17's level | lines that do not express NID1 (20) vs lines expressing it (30) | 1.39× higher at baseline in the lines without NID1 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL4A2, FBXO17, COL4A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.963). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.3, -27.7); signed map (-60.0, -4.3). **Vector** length 91.6, 55.1% of its response variance represented; |z| ≥ 3 in 437 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.81 to 19); *Translation initiation complex formation* (reactome, mean cos +0.77 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.77 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | -0.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +0.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.9 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -5.7 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.3 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | +0.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:49,488,453-49,492,508 (-) |
| Ensembl biotype | protein_coding |
| Also known as | rpL23, L17, uL22 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P18621](https://www.uniprot.org/uniprotkb/P18621) (Large ribosomal subunit protein uL22):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6139](https://www.ncbi.nlm.nih.gov/gene/6139):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L22P family of ribosomal proteins. It is located in the cytoplasm. This gene has been referred to as rpL23 because the encoded protein shares amino acid identity with …

**Accessions** — [HGNC:10307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10307) · Entrez [6139](https://www.ncbi.nlm.nih.gov/gene/6139) · UniProt [P18621](https://www.uniprot.org/uniprotkb/P18621) · Ensembl [ENSG00000265681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265681)

## Data

Gene col 15464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15464); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15464]; `tensor/DDL_lfc|DDL_z.npy` [15464]; `embed/gene_vectors.npy` [15464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15464 or target_col == 15464). Every well: [[RPL17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
